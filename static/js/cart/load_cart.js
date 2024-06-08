let counterSpan = document.querySelector(".counter");
const cards = document.querySelectorAll(".item");
let cart = JSON.parse(localStorage.getItem('cart')) || [];

const shopProducts = document.querySelectorAll('.item');

cart.forEach(function (cartProduct) {

    const product_id = cartProduct.product_id;

    const shopProduct = Array.from(shopProducts).find(function (product) {
        const shopProduct_id = product.querySelector('a').getAttribute('href');
        if (shopProduct_id === product_id) {
            return product;
        }
        return false;
    });


    if (shopProduct) {
        const buttonDelete = shopProduct.querySelector(".remove-product");
        const buttonAdd = shopProduct.querySelector(".add-product");
        counterSpan.style.display = "inline-block";
        counterSpan.textContent = parseInt(counterSpan.textContent) + cartProduct.product_quantity;
        buttonDelete.style.display = "inline-block";
        buttonAdd.textContent = "+";

    } else {
        counterSpan.textContent = parseInt(counterSpan.textContent) + cartProduct.product_quantity;
        counterSpan.style.display = 'inline-block';
    }
})


