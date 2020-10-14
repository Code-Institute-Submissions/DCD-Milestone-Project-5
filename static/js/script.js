/*jshint esversion: 6 */

/* 
 * Toggles visibilty of recipe search bar and category buttons
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
 * Sets the visible recipes and the active page button
 * @param {int} totalPages - The total number of pages
 * @param {int} targetPage - The page to set as active
 * @param {int} numResults - The number of recipes in the current search results.
 */
function searchPaginate(totalPages, targetPage, numResults) {
    //first loop that changes which page is currently active.
	for (let a = 1; a <= totalPages; a++) {
		let elementID = `page-button-${a}`;
		if (a === targetPage) {
			document.getElementById(elementID).classList.add('active');
		} else {
			document.getElementById(elementID).classList.remove('active');
        }
    }
    
    let upperBounds = (8 * targetPage);
    let lowerBounds = (upperBounds) -7;
    
    //This loop changes the visiblity of recipe thumbnails
	for (let b = 1; b <= numResults; b++) {
		let recipeTarget = document.getElementById(`recipe-${b}`);
        if (b>=lowerBounds && b<=upperBounds){
            recipeTarget.style.display = 'inline-flex';
        }
        else{
            recipeTarget.style.display = 'none';
        }
        
	}
}
/*
 * Ensures the search controls are visible when resizing the viewport.
 */
function fixSearchControls(){
    if(window.innerWidth > 1100){
        document.getElementById('recipe-search-controls').removeAttribute("style");
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