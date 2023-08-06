const carousel = document.querySelector('.carousel');
const prevButton = document.querySelector('.carousel-prev');
const nextButton = document.querySelector('.carousel-next');

let currentIndex = 0;
let slideTimer;

function slideTo(index) {
  currentIndex = index;
  carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
}

function slidePrev() {
  clearInterval(slideTimer);
  currentIndex = (currentIndex - 1 + 3) % 3;
  slideTo(currentIndex);
  startSlideTimer();
}

function slideNext() {
  clearInterval(slideTimer);
  currentIndex = (currentIndex + 1) % 3;
  slideTo(currentIndex);
  startSlideTimer();
}

prevButton.addEventListener('click', slidePrev);
nextButton.addEventListener('click', slideNext);

function startSlideTimer() {
  slideTimer = setInterval(slideNext, 3000);
}

// Add fade-in effect when the page loads
document.addEventListener('DOMContentLoaded', () => {
  carousel.style.opacity = 1; // Set opacity to 1 to trigger the fade-in effect
  startSlideTimer();
});
