const toggleTag = document.querySelector('a.toggle-nav');
const mainTag = document.querySelector('main');
const ul = document.querySelector('ul.navbar-nav');

// When I click the toggle tag add a class of open to the main tag

toggleTag.addEventListener('click', function () {
    mainTag.classList.toggle('open');
})


ul.addEventListener('click', handleClick);

function handleClick(e) {
    console.log(e.target);
}

function menuToggle(x) {
    x.classList.toggle("change");
}