let allBodyElements=document.querySelectorAll('.faq-item-body');

function Accordion(el){
    let icon=el.querySelector('span');
    let icons=document.querySelectorAll('.faq-item-header span')

    for(let i=0;i<allBodyElements.length;i++){
        
        allBodyElements[i].className='faq-item-body close'
        icons[i].innerHTML='+'
    }

    el.nextElementSibling.className='faq-item-body open'
    icon.innerHTML='-'
}

function name(params) {
    
}