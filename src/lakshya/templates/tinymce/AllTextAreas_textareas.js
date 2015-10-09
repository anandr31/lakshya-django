
tinyMCE.init({
    mode: "textareas",
    theme: "advanced",
    plugins : "autoresize",
    // width: "50%",
    theme_advanced_resizing : true,
    // resize: "both",
    browser_spellcheck: true,
    setup: function(ed) 
    {
        if ($('#'+ed.id).prop('readonly')) 
        {
            ed.settings.readonly = true;
        }
    }
    });

//     plugins:  [
//     "autoresize advlist autolink lists link image charmap print preview hr anchor pagebreak",
//     "searchreplace wordcount visualblocks visualchars code fullscreen",
//     "insertdatetime nonbreaking save table contextmenu directionality",
//     "emoticons template paste textcolor"
// ],   

    // plugins: "spellchecker,directionality,paste,searchreplace",
    // language: "{{ language }}",
    // directionality: "{{ directionality }}",
    // spellchecker_languages : "{{ spellchecker_languages }}",
    // spellchecker_rpc_url : "{{ spellchecker_rpc_url }}"
 
