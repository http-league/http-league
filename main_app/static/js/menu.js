const toggleTag = document.querySelector('a.toggle-nav');
const mainTag = document.querySelector('main');

// When I click the toggle tag add a class of open to the main tag

toggleTag.addEventListener('click', function () {
    mainTag.classList.toggle('open');
})