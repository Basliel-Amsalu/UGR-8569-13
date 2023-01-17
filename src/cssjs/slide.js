const slides = document.querySelectorAll('.slide');
const next = document.querySelector('#next');
const prev = document.querySelector('#prev');
const auto = true;
const intervalTime = 5000;
let slideInterval;
    
const nextSlide = () => {
    const current = document.querySelector('.current');
    current.classList.remove('current');
    if(current.nextElementSibling){
        current.nextElementSibling.classList.add('current');

    }else{
        slides[0].classList.add('current');
    }
    setTimeout(() => current.classList.remove('current'));
    if (auto){
        clearInterval(slideInterval);
        slideInterval = setInterval(nextSlide,intervalTime);
    }
}
const prevSlide = () => {
    const current = document.querySelector('.current');
    current.classList.remove('current');
    if(current.previousElementSibling){
        current.previousElementSibling.classList.add('current');

    }else{
        slides[slides.length-1].classList.add('current');
    }
    setTimeout(() => current.classList.remove('current'));
    if (auto){
        clearInterval(slideInterval);
        slideInterval = setInterval(nextSlide,intervalTime);
    }
}
next.addEventListener('click',() =>
{nextSlide();});
prev.addEventListener('click',() => 
{prevSlide();});
if(auto){
    slideInterval = setInterval(nextSlide, intervalTime);
}
    
  
