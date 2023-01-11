const sections = document.querySelectorAll('section[id]');
const ofs = document.querySelector('.navbar').offsetHeight;
console.log("offset " + ofs);
console.log(sections);

function scrollActive(){
    const scrollY = window.pageYOffset;

    sections.forEach(current => {
        const secH = current.offsetHeight
        const secT = current.offsetTop - 2 * ofs
        sectionId = current.getAttribute('id')
        
        // console.log(secH)
        // console.log(secT)
        // console.log(scrollY)
        // console.log('========================')
        if (scrollY > secT && scrollY<= secT + secH) {
            document.querySelector('.nav-links li a[href*=' + sectionId + ']').classList.add('active') 
        }
        else {
            document.querySelector('.nav-links li a[href*=' + sectionId + ']').classList.remove('active') 
        }
    })
} 
window.addEventListener('scroll', scrollActive);