const sliderContainer = document.getElementById("slider");
let currentIndex = 0;
let sliderData = null;

async function fetchSliderData() {
  try {
    const response = await fetch("../data/slider.json");
    sliderData = await response.json();
    generateSlides();
    startSlider();
  } catch (error) {
    console.error("Fehler beim Abrufen der Slider-Daten:", error);
  }
}

function generateSlides() {
  const { duration, media } = sliderData;

  if (!Array.isArray(media) || media.length < 1) {
    console.error("Kein Medium gefunden.");
    return;
  }

  sliderContainer.innerHTML = "";

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
      video.addEventListener("loadedmetadata", function () {
        this.currentTime = 0;
        this.play();
      });
      slide.appendChild(video);
    }

    sliderContainer.appendChild(slide);
  });

  const slides = document.querySelectorAll(".slider-item");
  slides.forEach((slide) => slide.setAttribute("data-duration", duration));
}

function startSlider() {
  const slides = document.querySelectorAll(".slider-item");
  const duration = parseInt(slides[currentIndex].getAttribute("data-duration"));

  slides.forEach((slide, index) => {
    if (index === currentIndex) {
      slide.style.transform = "translateX(0)";
    } else {
      slide.style.transform = "translateX(-100%)";
    }
  });

  setTimeout(() => {
    slides[currentIndex].style.transform = "translateX(-100%)";

    currentIndex = (currentIndex + 1) % slides.length;

    slides[currentIndex].style.transform = "translateX(0)";

    startSlider();
  }, duration);
}

fetchSliderData();
