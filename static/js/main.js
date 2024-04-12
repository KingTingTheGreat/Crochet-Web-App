const imageForm = document.getElementById("image-form");
imageForm.addEventListener("submit", processImage);

function processImage(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const URL = "http://127.0.0.1:8888/trans"

    console.log(formData.get("input-image"));

    fetch(URL, {
        method: 'POST',
        body: formData
    })
        .then(response => {
            if (response.ok) {
                let processedImage = document.getElementById("processed-image");
                processedImage.src = response.blob();
                processedImage.style.visibility = "visible";
                // console.log(response.blob());
            }
            else {
                console.log(`an error occurred`);
                console.log(`Error ${response.status}: ${response.statusText}`);
            }
        })
        .catch(error => {
            console.log(`an error occurred`);
            console.log(error);
        }
        );
}
//         .then(response => response.json())
//         .then(data => {
//             if (data.error) {
//                 console.log(`an error occurred`)
//                 console.log(data.error);
//             }
//             else {
//                 console.log(`success`);
//                 console.log(data);
//                 console.log(data.processedImage !== null);
//                 let processedImage = document.getElementById("processed-image");
//                 processedImage.src = 'data:image/png;base64,' + data.processedImage;
//                 // processedImage.src = data.processedImage;
//                 processedImage.style.visibility = "visible";
//             }
//         });
// }