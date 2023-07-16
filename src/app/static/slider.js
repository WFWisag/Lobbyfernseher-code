const sliderContainer = document.getElementById("slider");
let currentIndex = 0;
let sliderData = null;

// Fetch slider data from slider.json
fetch("../data/slider.json")
  .then((response) => response.json())
  .then((data) => {
    sliderData = data;
    generateSlides();
    startSlider();
  })
  .catch((error) => console.error(error));

function generateSlides() {
  const { duration, media } = sliderData;

  media.forEach((item) => {
    const slide = document.createElement("div");
    slide.className = "slider-item";

    if (item.type === "image") {
      const image = document.createElement("img");
      image.src = `../uploads/${item.filename}`;
      slide.appendChild(image);
    } else if (item.type === "video") {
      const video = document.createElement("video");
      video.src = `../uploads/${item.filename}`;
      video.controls = true;
      slide.appendChild(video);
    }

    sliderContainer.appendChild(slide);
  });

  // Set the duration for all slides
  const slides = document.querySelectorAll(".slider-item");
  slides.forEach((slide) => slide.setAttribute("data-duration", duration));
}

function startSlider() {
  const slides = document.querySelectorAll(".slider-item");
  const duration = parseInt(slides[currentIndex].getAttribute("data-duration"));

  slides[currentIndex].style.transform = "translateX(0)";

  setTimeout(() => {
    slides[currentIndex].style.transform = "translateX(-100%)";

    currentIndex = (currentIndex + 1) % slides.length;

    slides[currentIndex].style.transform = "translateX(0)";

    startSlider();
  }, duration);
}
