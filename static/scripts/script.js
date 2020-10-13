/*jshint esversion: 6 */

/* searchMenuToggle()

This function is called when clicking the menu toggle button on the search page, which is only visible on small viewports.
it toggles the visibility of the search menu.

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
searchPaginate()

*/
function searchPaginate(totalPages, currentPage, numResults) {
    //first loop that changes which page is currently active.
	for (a = 1; a <= totalPages; a++) {
		var elementID = `page-button-${a}`;
		if (a === currentPage) {
			document.getElementById(elementID).classList.add('active');
		} else {
			document.getElementById(elementID).classList.remove('active');
        }
    }
    
    let upperBounds = (8 * currentPage);
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