let myRoomSlider = new Swiper('.room__slider', {

  navigation: {
    prevEl: '.room__button-prev',
    nextEl: '.room__button-next',
  },

  pagination: {
    el: '.room__pagination',
    type: 'fraction',
  },
  spaceBetween: 32,
  grabCursor: true,

  keyboard: {
    enabled: true,
    onlyInViewport: true,
    pageUpDown: true,
  },

  // autoplay: {
  //     delay: 2000,
  // },

  speed: 1000,

  breakpoints: {
    480: {
      slidesPerView: 1,
    },
    992: {
      slidesPerView: 2,
    },
  },

});

const burgerMenu = document.querySelector('.header__burger');
const headerList = document.querySelector('.header__list');
burgerMenu.addEventListener('click', () => {
  burgerMenu.classList.toggle('_active');
  headerList.classList.toggle('_active');
})