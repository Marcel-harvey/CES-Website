const swiper = new Swiper('.swiper', {

    autoplay: {
        delay: 3000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
    },
    
    loop: true,

    autoHeight: true,
    
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
  
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  });

  // ----------------------------------For Responsive Navbar----------------------------------
const nav = document.querySelector(".navigationLinks");
const toggleButton = document.querySelector(".navToggle");

toggleButton.addEventListener("click", () => {
    const visible = nav.getAttribute("data-visible");

    if(visible === "false") {
        nav.setAttribute("data-visible", true);
        toggleButton.setAttribute("aria-expanded", true);
    }

    else {
        nav.setAttribute("data-visible", false);
        toggleButton.setAttribute("aria-expanded", false);
    }

});

document.getElementsByClassName('subnav').onclick = function() {expand()};

function expand() {
  document.getElementsByClassName('subnavContent').style.display = 'block';
}



//------------------------------------------------------------------------------------

