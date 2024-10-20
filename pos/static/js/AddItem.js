

imageField = document.getElementById('id_Image');

imageField.addEventListener('change', (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = (event) => {
        const image = document.getElementById('imagePreview');
        image.style.visibility = 'visible';
        image.src = event.target.result;
    }
    reader.readAsDataURL(file);
});