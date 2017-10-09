var cropper;
var actionsxs = document.getElementById('actions-xs')
var actionssm = document.getElementById('actions-sm')
var material;
var size;

function menuOn(id) {
    material = id
    element = document.getElementById(id);
    element.style.left='0';
}

function menuOff(id) {
    destroyCropper();
    element = document.getElementById(id);
    element.style.left='100%';
}

function createCropper(ratio = 16/9) {
    if(!isCropperPresent()){
        var image = document.getElementById('image');
        cropper = new Cropper(image, {
            aspectRatio: ratio,
            background: false,
            viewMode:1,
            highlight:false,
            zoomable:false,
        });
        actionsxs.classList.add('visible-xs');
        actionssm.style.display="block";
    }

}

function destroyCropper() {
    if(isCropperPresent()){
        cropper.destroy();
    }
    actionsxs.classList.remove('visible-xs');
    actionssm.style.display="";
}

$(window).resize(function() {
    if(isCropperPresent()){
        destroyCropper();
        createCropper();
    }
})

function rotateCrop() {
    cropper.setAspectRatio(1/cropper.options.aspectRatio);
}

function changeRatio(width,height) {
    size = {"width":width,"height":height};
    ratio = width/height;
    if (isCropperPresent()) {
        cropper.setAspectRatio(ratio);
    }
    else{
        createCropper(ratio);
    }
}

function isCropperPresent() {
    return(!(cropper==null || cropper.cropper==null));
}

$('#myModal').on('hidden.bs.modal', function (e) {
    destroyCropper();
    menus=document.getElementById('selection-menu').children;
    for (var i = 0; i < menus.length; i++) {
        menus[i].style.left="";
    }
})

function post(path) {
    method = "post"; // Set method to post by default if not specified.

    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    var form = document.getElementById("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);

    var cropper_data = document.createElement("input");
    cropper_data.setAttribute("type","hidden");
    cropper_data.setAttribute("name", "cropper_data");
    cropper_data.setAttribute("value",JSON.stringify(cropper.getData()));
    form.appendChild(cropper_data);

    var size_form = document.createElement("input");
    size_form.setAttribute("type", "hidden");
    size_form.setAttribute("name", "size");
    size_form.setAttribute("value", JSON.stringify(size));
    form.appendChild(size_form);

    var material_form = document.createElement("input");
    material_form.setAttribute("type", "hidden");
    material_form.setAttribute("name", "material");
    material_form.setAttribute("value", material);
    form.appendChild(material_form);

    document.body.appendChild(form);
    form.submit();
}
