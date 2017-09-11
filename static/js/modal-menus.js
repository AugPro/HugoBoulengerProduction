var cropper;
var actionsxs = document.getElementById('actions-xs')
var actionssm = document.getElementById('actions-sm')

function menuOn(id) {
    if(id=="auth-form"){
        cropper.disable();
    }
    element = document.getElementById(id);
    element.style.left='0';
}

function menuOff(id) {
    if(id=="auth-form"){
        cropper.enable();
    }
    else{
        destroyCropper();
    }
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
        console.log(cropper);
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
    cropper.setAspectRatio(1/cropper.options.aspectRatio)
}

function changeRatio(ratio) {
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
