// Получаем элементы кнопки открытия корзины и оверлея корзины
const openCartBtn = document.getElementById('openCartBtn');


openCartBtn.addEventListener('click', function () {

    //1 создать темный фон
    const bodyOverlay = document.createElement('div');
    bodyOverlay.style.position = 'absolute';
    bodyOverlay.style.left = '0';
    bodyOverlay.style.top = '0';
    bodyOverlay.style.width = '100%';
    bodyOverlay.style.height = '100%';
    bodyOverlay.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
    document.querySelector('body').style.overflow = 'hidden';


    const cart_preview = document.createElement('div');
    //2 cart-preview position absolute;
    cart_preview.classList.add("cart-preview");
    cart_preview.style.display = 'block';
    cart_preview.style.zIndex = '1';
    cart_preview.style.position = 'absolute';
    cart_preview.style.left = '50%';
    cart_preview.style.top = '50%';


    cart_preview.textContent = "CARDS";

    const closingSpan = document.createElement('span');
    closingSpan.textContent = '×';
    closingSpan.classList.add("close-cart");
    closingSpan.addEventListener("click", function () {
        cart_preview.style.display = 'none';
        bodyOverlay.style.display = 'none';
        document.querySelector('body').style.overflow = 'initial';

    });
    closingSpan.style.zIndex = '2';
    // Отображаем содержим корзины на странице

    const cart = JSON.parse(localStorage.getItem('cart')) || [];

    cart.forEach(function (item) {
        //create product html block
        console.log(item);
        // cart_preview.appendChild(item);
    });
    cart_preview.appendChild(closingSpan);
    // localStorage.clear();
    document.querySelector("body").appendChild(cart_preview);
    document.querySelector("body").appendChild(bodyOverlay);
});

