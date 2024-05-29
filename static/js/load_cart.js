let counterSpan = document.querySelector(".counter");
const cards = document.querySelectorAll(".item");
let cart = JSON.parse(localStorage.getItem('cart')) || [];

const shopProducts = document.querySelectorAll('.item');


shopProducts.forEach(function (card) {
    const buttonDelete = card.querySelector(".remove-product");
    const buttonAdd = card.querySelector(".add-product");
    const product_id = card.querySelector('a').getAttribute('href');

    const cartProduct = cart.find(function (product) {
        if (product.product_id === product_id) {
            return product;
        }
        return false;
    });

    if (cartProduct) {
        console.log('mew');
        console.log(cartProduct);
        counterSpan.style.display = "inline-block";
        counterSpan.textContent = parseInt(counterSpan.textContent) + cartProduct.product_quantity;
        buttonDelete.style.display = "inline-block";
        buttonAdd.textContent = "+";
        card.dataset.count = cartProduct.product_quantity; // Получаем идентификатор товара из data атрибута


    } else {

    }
})


