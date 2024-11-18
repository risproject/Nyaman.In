document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.querySelector('#targetElement');
    const navbarToggler = document.querySelector('.navbar-toggler');

    // Event listener untuk scroll
    window.onscroll = function () {
        const fixedNav = navbar.offsetTop;

        if (window.pageYOffset > fixedNav) {
            navbar.classList.add('navbar-blur'); // Tambahkan blur saat scroll
        } else {
            navbar.classList.remove('navbar-blur'); // Hapus blur saat scroll
        }
    };

    // Event listener untuk klik tombol navbar-toggler
    navbarToggler.addEventListener('click', function () {
        if (!navbar.classList.contains('navbar-blur')) {
            navbar.classList.add('navbar-blur'); // Tambahkan blur saat toggle dibuka
        } else {
            navbar.classList.remove('navbar-blur'); // Hapus blur saat toggle ditutup
        }
    });
});
