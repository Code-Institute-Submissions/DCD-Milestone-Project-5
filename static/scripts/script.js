/*
searchPaginate()

This function uses Ajax calls to perform dynamic pagination
of the serach results, to allow for a seamless browsing experience

*/
function searchPaginate(){
    
}


//TinyMCE integration
tinymce.init({
    selector:'textarea#cookingMethod'
});

$(document).on('focusin', function(e) {
  if ($(e.target).closest(".tox-tinymce-aux, .moxman-window, .tam-assetmanager-root").length) {
    e.stopImmediatePropagation();
  }
});