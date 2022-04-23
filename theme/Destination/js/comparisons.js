/**
 * Sliders should query all slider components on a page so we can have more than one on a page.
 */
 const sliders = Array.prototype.slice.call(
	document.querySelectorAll(".slider"),
  );
  
  /**
   * For each slider component we find, add an oninput event listener where we take the input value,
   * and set it to the polygon clip path of the before image for masking everything outside those dimensions.
   */
  sliders.forEach((slider) => {
	/* create divider */
	divider = document.createElement("DIV");
	divider.setAttribute("class", "slider__divider");
	/* place divider */
	slider.querySelector(".slider__img-after",).appendChild(divider);
	/* query slideValue */
	slider.querySelector(".slider__input").oninput = (e) => {
	  let slideValue = "calc(" + e.target.value + "% - 1px)";
	  /* set slideValue to clipPath */
	  slider.querySelector(
		".slider__img-before",
	  ).style.clipPath = `polygon(0 0,${slideValue} 0,${slideValue} 100%, 0 100%)`;
	  /* move divider based on slideValue */
	  slider.querySelector(
		".slider__divider",
	  ).style.left = "calc(" + e.target.value + "% - 1px)";
	};
  });