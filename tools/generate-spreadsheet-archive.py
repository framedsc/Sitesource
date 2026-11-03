import csv
import html
import io
import re
import urllib.request
from urllib.parse import quote, urlsplit, unquote


# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------

SPREADSHEET_ID = "1lnM2SM_RBzqile870zG70E39wuuseqQE0AaPW-P1p5E"
SHEET_GID = "0"

OUTPUT_FILE = "markdown/spreadsheet-archive.md"

MAX_URL_LABEL_LENGTH = 50

COLUMN_WIDTHS = {
    "Game": "25%",
    "Features": "25%",
    "Extra Description": "50%",
}

TABLE_STYLE = """
    width: 100%;
    table-layout: fixed;
    border-collapse: collapse;
    border: 1px solid #272727;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.15);
"""

CELL_STYLE = """
    padding: 8px;
    border: 1px solid #272727;
    vertical-align: top;
    overflow-wrap: anywhere;
    word-wrap: break-word;
"""

INTRO = """
<div class="figure">
<img src="Images/spreadsheet_archive.png" alt="Spreadsheet Archive" title="Spreadsheet Archive" class="autosize shadowed" />
<p><i>Star Wars Jedi: Survivor</i>, shot by originalnicodr</p>
</div>

Over the years we have been collecting a lot of mods that are at least tangential related to virtual photography, in an attempt cover as many games as possible by documenting all the resources we could find on [this spreadsheet](https://docs.google.com/spreadsheets/d/1lnM2SM_RBzqile870zG70E39wuuseqQE0AaPW-P1p5E/edit?usp=sharing). These go from simple freecam mods, all over to debug menus, HD textures, or entire photomode suites with posing and lighting tools.

Ideally, these would have their own guides on this site (whenever the offered URL doesn't include one of its own), but documenting them all in detail would be a monumental effort. So in the meantime, we thought that we could expose what we have on that sheet unto the site so the information can not only be searchable here, but also be indexed by search engines. Given that these were meant to be just notes lying around, our notes on them might not be the cleanest, so we appreciate your understanding.

Having said that, if you end up using one of these mods and learn more tips and tricks on how to shoot a game, please feel free to [create a guide](./contribute.htm) on the game! Or update it if there is already one.

Also, if you happen to have found some mods or tools that you want to include here, send us a DM to one of our social profiles listed [here](./joinus.htm). Or better yet, try to write a guide about it to include it on the [game guides](Gameguides.htm)!
"""

# ---------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------

GOOGLE_SHEET_URL = (
    f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}"
    f"/export?format=csv&gid={SHEET_GID}"
)

DISCORD_MESSAGE_PATTERN = re.compile(
    r"https?://(?:canary\.|ptb\.)?"
    r"discord(?:app)?\.com/channels/\d+/\d+/\d+",
    re.IGNORECASE
)

URL_PATTERN = re.compile(r"https?://[^\s<>\"']+", re.IGNORECASE)


# ---------------------------------------------------------------------
# Download and parsing
# ---------------------------------------------------------------------

def download_csv(url):
    """Download a Google Sheet exported as CSV."""

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urllib.request.urlopen(request) as response:
        content = response.read().decode("utf-8-sig")

    return list(csv.reader(io.StringIO(content, newline="")))


def process_rows(rows):
    """Clean rows, group entries by game and sort the groups."""

    if not rows:
        raise ValueError("The spreadsheet is empty.")

    headers = rows[0]

    groups = []
    current_group = None

    for row in rows[1:]:

        if not any(cell.strip() for cell in row):
            continue

        row = [
            re.sub(r"\s+", " ", cell).strip()
            for cell in row
        ]

        row = (row + [""] * len(headers))[:len(headers)]

        game = row[0]

        if game:
            current_group = {
                "name": game,
                "rows": []
            }
            groups.append(current_group)

        #print(
        #    f"Row game: {row[0]!r}, "
        #    f"Current group: {current_group['name'] if current_group else None!r}, "
        #    f"Discord: {any(DISCORD_MESSAGE_PATTERN.search(cell) for cell in row)}"
        #)

        if any(DISCORD_MESSAGE_PATTERN.search(cell) for cell in row):
            continue

        # Keep valid rows in the current group.
        if current_group is not None:
            current_group["rows"].append(row)
            row[0] = current_group["name"]

    groups.sort(key=lambda group: group["name"].casefold())

    # Flatten groups, displaying the game name only once.
    processed_rows = []

    for group in groups:
        for index, row in enumerate(group["rows"]):

            row = row.copy()

            if index > 0:
                row[0] = ""

            processed_rows.append(row)

    return headers, processed_rows


# ---------------------------------------------------------------------
# Markdown conversion
# ---------------------------------------------------------------------

def escape_markdown(text):
    """Escape Markdown table syntax in ordinary text."""

    text = text.replace("\\", "\\\\")
    text = text.replace("|", r"\|")
    text = text.replace("`", r"\`")
    text = text.replace("*", r"\*")
    text = text.replace("_", r"\_")
    text = text.replace("[", r"\[")
    text = text.replace("]", r"\]")

    return text

def shorten_url(url):
    """Truncate URLs while preserving their beginning."""

    if len(url) <= MAX_URL_LABEL_LENGTH:
        return url

    return url[:MAX_URL_LABEL_LENGTH] + "…"

def process_html_cell(text):
    """Convert URLs into clickable HTML links."""

    parts = []
    last_position = 0

    for match in URL_PATTERN.finditer(text):

        preceding_text = text[last_position:match.start()]
        parts.append(html.escape(preceding_text))

        url = match.group()

        # Remove punctuation accidentally captured at the end.
        trailing = ""
        while url and url[-1] in ".,;:!?":
            trailing = url[-1] + trailing
            url = url[:-1]

        label = shorten_url(url)

        safe_url = html.escape(url, quote=True)
        safe_label = html.escape(label)

        parts.append(
            f'<a href="{safe_url}">{safe_label}</a>'
        )

        parts.append(html.escape(trailing))

        last_position = match.end()

    parts.append(html.escape(text[last_position:]))

    return "".join(parts)

def generate_markdown(headers, rows):
    """Generate an HTML table embedded in Markdown."""

    lines = []
    lines.append(f'<table style="{TABLE_STYLE}">')
    lines.append("<colgroup>")
    for header in headers:
        width = COLUMN_WIDTHS.get(header, "auto")
        lines.append(f'<col style="width: {html.escape(width, quote=True)};">')
    lines.append("</colgroup>")

    # Header
    lines.append("<thead>")
    lines.append("<tr>")
    for header in headers:
        lines.append(
            f'<th style="{CELL_STYLE} text-align: left;">'
            f'{html.escape(header)}</th>'
        )
    lines.append("</tr>")
    lines.append("</thead>")

    # Data
    lines.append("<tbody>")
    i = 0
    while i < len(rows):
        row = rows[i]
        game = row[0]

        # Count consecutive rows belonging to this game.
        rowspan = 1
        while (
            i + rowspan < len(rows)
            and rows[i + rowspan][0] == ""
        ):
            rowspan += 1

        lines.append("<tr>")
        # First column, spanning all rows belonging to the game.
        lines.append(
            f'<td rowspan="{rowspan}" style="{CELL_STYLE}">'
            f'{process_html_cell(game)}</td>'
        )
        # Remaining columns.
        for cell in row[1:]:
            lines.append(
                f'<td style="{CELL_STYLE}">'
                f'{process_html_cell(cell)}</td>'
            )
        lines.append("</tr>")

        # Remaining rows in this group.
        for offset in range(1, rowspan):
            lines.append("<tr>")
            for cell in rows[i + offset][1:]:
                lines.append(
                    f'<td style="{CELL_STYLE}">'
                    f'{process_html_cell(cell)}</td>'
                )
            lines.append("</tr>")
        i += rowspan

    lines.append("</tbody>")
    lines.append("</table>")

    return "\n".join(lines)


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def main():

    print("Downloading spreadsheet...")

    rows = download_csv(GOOGLE_SHEET_URL)

    print(f"Downloaded {len(rows) - 1} entries.")

    headers, data = process_rows(rows)

    print(f"Remaining entries: {len(data)}")

    markdown = generate_markdown(headers, data)

    # Inject introduction at the top of the document.
    output = INTRO.strip() + "\n\n" + markdown + "\n"

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(output)

    print(f"Markdown successfully saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
