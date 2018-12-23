// Copy and paste this into the console after conducting a search
// (and scrolling down to load all desired images)

var script = document.createElement('script');
script.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(script);

function saveFile (name, type, data) {
    if (data != null && navigator.msSaveBlob)
        return navigator.msSaveBlob(new Blob([data], { type: type }), name);
    var a = $("<a style='display: none;'/>");
    var url = window.URL.createObjectURL(new Blob([data], {type: type}));
    a.attr("href", url);
    a.attr("download", name);
    $("body").append(a);
    a[0].click();
    window.URL.revokeObjectURL(url);
    a.remove();
}

setTimeout(function() {
    images = $(".rg_ic.rg_i");
    urls = $.map(images, elem => elem.src);
    text = urls.join("\r\n");

    saveFile("urls.txt", "data:attachment/text", text);
}, 1000);