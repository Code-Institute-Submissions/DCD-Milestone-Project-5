/* searchMenuToggle()

This function is called when clicking the menu toggle button on the search page, which is only visible on small viewports.
it toggles the visibility of the search menu.

*/
function searchMenuToggle(){
    let target = document.getElementById("recipe-search-controls");
    displayType = target.style.display;
    if(displayType != "none"){
        target.style.display = "none";
    }
    else{
        target.style.display = "flex";
    }
}

/*
searchPaginate()

This function uses Ajax calls to perform dynamic pagination
of the serach results, to allow for a seamless browsing experience

*/
function searchPaginate(){
    
}


//TinyMCE integration
tinymce.init({
    selector:'.tiny-mce-target-bul',
    plugins:'lists',
    toolbar:'bullist',
    valid_elements:'p,ul,ol,li',
    menubar:false,
    element_format:'html',
    lists_indent_on_tab:false
});


tinymce.init({
    selector:'.tiny-mce-target-num',
    plugins:'lists',
    toolbar:'numlist',
    valid_elements:'p,ul,ol,li',
    menubar:false,
    element_format:'html',
    lists_indent_on_tab:false
});

$(document).on('focusin', function(e) {
  if ($(e.target).closest(".tox-tinymce-aux, .moxman-window, .tam-assetmanager-root").length) {
    e.stopImmediatePropagation();
  }
});