const image_input = document.querySelector("#image_input");

var upload_image = "";
image_input.addEventListener("change", function() {
    const reader = new FileReader();
    reader.addEventListener("load", () => {
        upload_image = reader.result;
        console.log(upload_image);
        document.querySelector("#display_image").style.backgroundImage=`url(${upload_image})`
    });
    reader.readAsDataURL(this.files[0]);
    console.log(this.files[0]);
})