let hidden_list = document.querySelector('.hidden-list');
let more_btn = document.querySelector('.more');
let isOpen = false;

more_btn.addEventListener('click',function() {
    if (isOpen == false) {
        hidden_list.style.display = 'block';
        isOpen = true;
    }
    else {
        hidden_list.style.display = 'none';
        isOpen = false;
    };
});