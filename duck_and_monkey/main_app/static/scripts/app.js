// function toggleMenu() {
//     let getMenu = document.querySelector(".mainMenu");
//     getMenu.classList.toggle("hamburger");
// }
// let getHamburger = document.querySelector("#toggle-bar");

// getHamburger.addEventListener("click", toggleMenu);

const $menu = $('#toggle-menu').on("click", function(event) {
    console.log("Clicked")
    $('.main-menu').toggle();
});