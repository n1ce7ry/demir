document.querySelectorAll('.filter__param').forEach(tag => {
    tag.addEventListener('click', (event) => {
        event.preventDefault(); 
        const selectedTag = tag.getAttribute('data-filter');

        document.querySelectorAll('.filter__param').forEach(t => {
            t.classList.remove('filter__param-active');
        });

        tag.classList.add('filter__param-active');

        document.querySelectorAll('.gallery__card').forEach(car => {
            if (selectedTag === 'all' || car.classList.contains(selectedTag)) {
                car.style.display = 'block';
            } else {
                car.style.display = 'none';
            }
        });
    });
});