const toggleButton = document.getElementById('dropdown');
const toggleList = document.getElementById('toggle-list');
const drop = () => {
    toggleList.classList.toggle('active');
}
toggleButton.addEventListener('click',() =>
    {drop();})
const searchButton = document.querySelector('.dropdown1');
const search = document.getElementById('search');
const form = document.querySelector('.search')
const searchdown = () => {
    search.classList.toggle('hide');
} 
searchButton.addEventListener('click',() =>
    {searchdown();}) 
form.addEventListener('submit', (e) => {
    e.preventDefault();
})
