/* searchMenuToggle()

This function is called when clicking the menu toggle button on the search page, which is only visible on small viewports.
it toggles the visibility of the search menu.

*/
function searchMenuToggle(){
    let target = document.getElementById("recipe-search-controls");
    displayType = getComputedStyle(target).display;
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
function searchPaginate(totalPages, page){
    //first loop that changes which page is currently active.
    for(let a = 1; a <= totalPages; a++)
    {
        let elementID = `page-button-${a}`;
        if(a = page){
            document.getElementById(elementID).classList.add('active');
        }
        else{
            document.getElementById(elementID).classList.remove('active');
        }
    }
    for(let b = 1; b<=totalPages*8; b++){
        recipeTarget = document.getElementById(`recipe-${b}`)
        if(recipeTarget != null && (b>(8*page-7) && b<(8*page)))
        {
            getComputedStyle(recipeTarget).display='none';
        }
    }
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