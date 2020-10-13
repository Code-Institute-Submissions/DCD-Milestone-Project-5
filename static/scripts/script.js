/*jshint esversion: 6 */

/* searchMenuToggle()

This function is called when clicking the menu toggle button on the search page, which is only visible on small viewports.
it toggles the visibility of the search menu, by targeting it via ID, then altering it's display value.

*/
function searchMenuToggle() {
	let target = document.getElementById("recipe-search-controls");
	let displayType = getComputedStyle(target).display;
	if (displayType != "none") {
		target.style.display = "none";
	} else {
        target.style.display = "flex";
	}
}

/*
searchPaginate(totalPages, targetPage, numResults)

This function takes the total number of pages, the page to transition to, and the total number of search results.

It then iterates through the page buttons, setting the targeted page's button to active while unsetting the other page buttons.

Then, it calculates the upper and lower bounds for the indexing of the current page's recipes,
before iterating through the results, setting the recipes for the targeted page to visible, and hiding the other recipes.

*/
function searchPaginate(totalPages, targetPage, numResults) {
    //first loop that changes which page is currently active.
	for (a = 1; a <= totalPages; a++) {
		var elementID = `page-button-${a}`;
		if (a === targetPage) {
			document.getElementById(elementID).classList.add('active');
		} else {
			document.getElementById(elementID).classList.remove('active');
        }
    }
    
    let upperBounds = (8 * targetPage);
    let lowerBounds = (upperBounds) -7;
    
	for (b = 1; b <= numResults; b++) {
		let recipeTarget = document.getElementById(`recipe-${b}`);
        if (b>=lowerBounds && b<=upperBounds){
            recipeTarget.style.display = 'inline-flex';
        }
        else{
            recipeTarget.style.display = 'none';
        }
        
	}
}


//tinyMCE integration
tinymce.init({
	selector: '.tiny-mce-target-bul',
	plugins: 'lists',
	toolbar: 'bullist',
	valid_elements: 'p,ul,ol,li',
	menubar: false,
	element_format: 'html',
	lists_indent_on_tab: false
});


tinymce.init({
	selector: '.tiny-mce-target-num',
	plugins: 'lists',
	toolbar: 'numlist',
	valid_elements: 'p,ul,ol,li',
	menubar: false,
	element_format: 'html',
	lists_indent_on_tab: false
});

//tinyMCE Bootstrap cross-integration
$(document).on('focusin', function(e) {
	if ($(e.target).closest(".tox-tinymce-aux, .moxman-window, .tam-assetmanager-root").length) {
		e.stopImmediatePropagation();
	}
});