let myRoomSlider = new Swiper('.main__slider', {

  navigation: {
    prevEl: '.room__button-prev',
    nextEl: '.room__button-next',
  },

  pagination: {
    el: '.room__pagination',
    type: 'fraction',
  },
  grabCursor: true,

  keyboard: {
    enabled: true,
    onlyInViewport: true,
    pageUpDown: true,
  },

  autoplay: {
      delay: 1000,
  },

  speed: 2000,
  slidesPerView: 1,
  loop: true,
});

const burgerMenu = document.querySelector('.header__burger');
const headerList = document.querySelector('.header__list');
burgerMenu.addEventListener('click', () => {
  burgerMenu.classList.toggle('_active');
  headerList.classList.toggle('_active');
})