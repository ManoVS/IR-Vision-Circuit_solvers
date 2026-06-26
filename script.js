const uploadForm = document.getElementById("uploadForm");
const imageInput = document.getElementById("imageInput");

const sceneText = document.getElementById("sceneText");
const objectList = document.getElementById("objectList");
const objectInfo = document.getElementById("objectInfo");

const enhancedImage = document.getElementById("enhancedImage");
const colorizedImage = document.getElementById("colorizedImage");
const heatmapImage = document.getElementById("heatmapImage");
const boxedImage = document.getElementById("boxedImage");

uploadForm.addEventListener("submit", async function (e) {

    e.preventDefault();

    const file = imageInput.files[0];

    if (!file) {
        alert("Please select an image.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    sceneText.innerHTML = "Analyzing image...";
    objectList.innerHTML = "";
    objectInfo.innerHTML = "";

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/pipeline",
            {
                method: "POST",
                body: formData
            }
        );

        if (!response.ok) {
            throw new Error("Server error");
        }

        const data = await response.json();

        // Scene description
        sceneText.innerHTML =
            data.scene_description || "No description available.";

        // Detected objects
        objectList.innerHTML = "";

        if (data.objects && data.objects.length > 0) {

            data.objects.forEach(obj => {

                const li = document.createElement("li");

                li.innerHTML =
                    `${obj.name} | ${(obj.confidence * 100).toFixed(1)}%`;

                objectList.appendChild(li);
            });

        } else {

            objectList.innerHTML =
                "<li>No objects detected.</li>";
        }

        // Object information
        objectInfo.innerHTML = "";

        if (data.information && data.information.length > 0) {

            data.information.forEach(item => {

                objectInfo.innerHTML += `
                    <div class="info-box">
                        <h3>${item.name}</h3>
                        <p>${item.description}</p>
                        <strong>Applications:</strong>
                        <p>${item.applications.join(", ")}</p>
                    </div>
                `;
            });

        } else {

            objectInfo.innerHTML =
                "<p>No additional information available.</p>";
        }

        // Images
        if (data.enhanced_image) {
            enhancedImage.src =
                "http://127.0.0.1:8000/" +
                data.enhanced_image +
                "?t=" + new Date().getTime();
        }

        if (data.colorized_image) {
            colorizedImage.src =
                "http://127.0.0.1:8000/" +
                data.colorized_image +
                "?t=" + new Date().getTime();
        }

        if (data.heatmap) {
            heatmapImage.src =
                "http://127.0.0.1:8000/" +
                data.heatmap +
                "?t=" + new Date().getTime();
        }

        if (data.boxed_image) {
            boxedImage.src =
                "http://127.0.0.1:8000/" +
                data.boxed_image +
                "?t=" + new Date().getTime();
        }

    }
    catch (error) {

        console.error(error);

        sceneText.innerHTML =
            "Processing failed. Check the backend terminal.";

        objectList.innerHTML = "";

        objectInfo.innerHTML =
            "<p>Unable to retrieve results.</p>";
    }
});