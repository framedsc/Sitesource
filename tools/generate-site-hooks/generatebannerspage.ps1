# This script generates a list of banners of all game guides with links to their respective guides and writes it inside bannerslistmd.

$outputPath = ".\markdown\bannerslist.md"
Clear-Content $outputPath

Write-Output "Generating banners list"
foreach($line in Get-Content .\markdown\docnet.json) {
    if($line -match 'GameGuides'){

        $line -match 'GameGuides\\\\.*\.md' | out-null
        $guidepath = $Matches.0 -replace 'GameGuides\\\\','.\markdown\GameGuides\'

        $firstGuideLine = Get-Content -Path $guidepath -TotalCount 1

        $firstGuideLine -match 'Images.*\.(png|jpg)' | out-null
        $imagePath = $Matches.0

        $htmlGuidePath = $guidepath -replace '\\markdown', ''
        $htmlGuidePath = $htmlGuidePath -replace '\.md', '.htm'

        $htmlLine = "<a href=`"$htmlGuidePath`" target=`"_blank`"><img src=`"$imagePath`" class=`"shadowed autosize bannerli`" /></a> <br> <br>"

        $htmlLine | out-file -filepath $outputPath -append -width 200
    }
}
Write-Output "Done generating banners list"
