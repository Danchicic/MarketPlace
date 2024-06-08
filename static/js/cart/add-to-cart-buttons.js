document.addEventListener("DOMContentLoaded", function () {
    cards.forEach((card) => {
        const buttonAdd = card.querySelector(".add-product");
        const buttonDelete = card.querySelector(".remove-product");
        const product_id = card.querySelector('a').getAttribute('href');

        buttonAdd.addEventListener("click", () => {
            //parse product index
            const userProductIndex = cart.findIndex(function (product) {
                return product.product_id === product_id;
            })
            //get product object
            const existingProduct = cart[userProductIndex];

            // Проверяем, есть ли товар с данным product_id в корзине
            if (existingProduct) {
                // Если товар уже есть в корзине, обновляем его количество
                existingProduct.product_quantity = parseInt(existingProduct.product_quantity) + 1;
            } else { // the first product in cart
                //styling new buttons
                buttonDelete.style.display = "inline-block";
                buttonAdd.textContent = "+";
                counterSpan.style.display = "inline-block";

                // Если товара нет в корзине, добавляем его как новый элемент
                const product_json = createUserProductJson(card, product_id);
                // Добавляем новый товар в корзину
                cart.push(product_json);
            }

            // Сохраняем обновленное содержимое корзины в локальное хранилище
            localStorage.setItem('cart', JSON.stringify(cart));
            updateGlobalCounter();
        });

        buttonDelete.addEventListener("click", () => {
            //get product object
            const productIndex = cart.findIndex(function (product) {
                return product.product_id === product_id;
            })
            const existingProduct = cart[productIndex];
            let productQuantity = parseInt(existingProduct.product_quantity);
            //update local storage
            if (productQuantity <= 1) {
                buttonDelete.style.display = "none";
                buttonAdd.textContent = "add";
                if (productIndex !== -1) {
                    cart.splice(productIndex, 1); // Удаляем элемент из массива по индексу
                }

            } else {
                // Если товар уже есть в корзине, обновляем его количество
                existingProduct.product_quantity = parseInt(existingProduct.product_quantity) - 1;
            }

            localStorage.setItem('cart', JSON.stringify(cart));
            updateGlobalCounter();
        });

    });
});


function createUserProductJson(card, product_id) {
    //returning cart product json
    return {
        "product_id": product_id,
        "name": card.querySelector('.product-name').textContent,
        "img_src": card.querySelector('img').getAttribute('src'),
        'price': card.querySelector('.price').textContent,
        'product_quantity': 1
    };
}

function updateGlobalCounter() {
    //update user cart
    //set temp variable
    let localCount = 0;
    //iterating cart objects
    for (let i = 0; i < cart.length; i++) {
        const productObject = cart[i]; //get product json
        let productQuantity = parseInt(productObject.product_quantity); // get product quantity

        if (productQuantity <= 0) {
            cart.splice(i, 1); // check foolish user
        } else {
            localCount += parseInt(productObject.product_quantity); // update temp var
        }
    }
    if (localCount <= 0) { // check foolish user
        localStorage.clear();
        hideGlobalCounter();
    }
    counterSpan.textContent = localCount; // updating user count
}

function hideGlobalCounter() {
    counterSpan.style.display = "none";
    counterSpan.textContent = "0";

}