// function toggleMenu() {
//     let getMenu = document.querySelector(".mainMenu");
//     getMenu.classList.toggle("hamburger");
// }
// let getHamburger = document.querySelector("#toggle-bar");

// getHamburger.addEventListener("click", toggleMenu);

const $menu = $('.tootle-menu').on("click", function(event) {
    console.log("Clicked")
    $('.mainMenu').toggle();
});