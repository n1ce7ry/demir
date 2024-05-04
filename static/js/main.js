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

function calculatePrice(carId, pricePerDay) {
    var startDate = document.getElementById('start_' + carId).value;
    var endDate = document.getElementById('end_' + carId).value;
    var totalDisplay = document.getElementById('total_' + carId);
    var price = document.getElementById('price_' + carId);

    if (startDate && endDate) {
        var start = new Date(startDate);
        var end = new Date(endDate);
        var timeDiff = end - start;
        var daysDiff = Math.ceil(timeDiff / (1000 * 60 * 60 * 24));
        var totalPrice = daysDiff * pricePerDay;
        price.value = totalPrice;
        totalDisplay.textContent = 'Забронировать за ' + totalPrice + ' рублей';
    }
}