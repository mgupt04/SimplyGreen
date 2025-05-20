document.querySelectorAll('.accordian .sec').forEach(item => {
    item.addEventListener('click', event => {
        const collapsable = item.nextElementSibling;
        if (collapsable.style.display === 'block') {
            collapsable.style.display = 'none';
        } else {
            collapsable.style.display = 'block';
        }
    });
});