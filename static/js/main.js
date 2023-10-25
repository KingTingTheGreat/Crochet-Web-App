document.getElementById("image-form").addEventListener("submit", function (e) {
    e.preventDefault();

    const formData = new FormData(this);

    fetch("http://127.0.0.1:5000/trans", {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                console.log(data.error);
            }
            else {
                const processedImage = document.getElementById("processed-image");
                processedImage.src = 'data:image/png;base64,' + data.processedImage;
                processedImage.style.display = "block";
            }
        });
});