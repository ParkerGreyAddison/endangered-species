// Copy and paste this into the console after conducting a search
// (and scrolling down to load all desired images)

function saveFile (name, type, data) {
    if (data != null && navigator.msSaveBlob)
        return navigator.msSaveBlob(new Blob([data], { type: type }), name);
    var a = document.createElement("a");
    var url = window.URL.createObjectURL(new Blob([data], {type: type}));
    var mouseclick = new MouseEvent("click");
    a.setAttribute("href", url);
    a.setAttribute("download", name);
    a.dispatchEvent(mouseclick);
    window.URL.revokeObjectURL(url);
    a.remove();
}

images = document.getElementsByClassName("rg_ic");
urls = Array.from(images).map(elem => elem.src);
text = urls.join("\r\n");

saveFile("urls.txt", "data:attachment/text", text);