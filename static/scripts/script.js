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