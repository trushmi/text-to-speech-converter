document.getElementById("textForm").addEventListener("submit", function (e) {
  e.preventDefault();

  var formData = new FormData(this);

  // Show the loader
  var loader = document.querySelector(".loader");
  loader.style.display = "block";

  fetch("/", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.blob())
    .then((data) => {
      var audio = document.getElementById("audio");
      audio.src = URL.createObjectURL(data);
      audio.load(); // This is to refresh the audio element

      // Hide the loader
      loader.style.display = "none";
    })
    .catch((error) => console.error("Error:", error));
});
