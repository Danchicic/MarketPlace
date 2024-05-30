document.addEventListener("DOMContentLoaded", function () {
    cards.forEach((card) => {
        const buttonAdd = card.querySelector(".add-product");
        const buttonDelete = card.querySelector(".remove-product");
        let count = parseInt(card.dataset.count) || 0;
        const product_id = card.querySelector('a').getAttribute('href');


        buttonAdd.addEventListener("click", () => {
            //parse product index
            const productIndex = cart.findIndex(function (product) {
                return product.product_id === product_id;
            })
            //get product object
            const existingProduct = cart[productIndex];

            //update card counter
            count++;
            //styling new buttons
            buttonDelete.style.display = "inline-block";
            buttonAdd.textContent = "+";
            counterSpan.style.display = "inline-block";
            // update cart counter
            counterSpan.textContent++;
            //saving cart

            // Проверяем, есть ли товар с данным product_id в корзине
            if (existingProduct) {
                // Если товар уже есть в корзине, обновляем его количество
                existingProduct.product_quantity = count;
            } else {
                // Если товара нет в корзине, добавляем его как новый элемент
                const product_json = {
                    "product_id": product_id,
                    "img_src": card.querySelector('img').getAttribute('src'),
                    'price': card.querySelector('.price').textContent,
                    'product_quantity': count
                };
                // Добавляем новый товар в корзину
                cart.push(product_json);
            }

            // Сохраняем обновленное содержимое корзины в локальное хранилище
            localStorage.setItem('cart', JSON.stringify(cart));

        });

        buttonDelete.addEventListener("click", () => {
            //parse product index
            const productIndex = cart.findIndex(function (product) {
                return product.product_id === product_id;
            })
            //get product object
            const existingProduct = cart[productIndex];

            count--; // update card count
            counterSpan.textContent--; // update cart count
            if (parseInt(counterSpan.textContent) === 0) {
                counterSpan.style.display = 'none'; //check 0 cart items
            }
            //update local storage
            if (parseInt(existingProduct.product_quantity) === 1) {
                buttonDelete.style.display = "none";
                buttonAdd.textContent = "add";
                if (productIndex !== -1) {
                    cart.splice(productIndex, 1); // Удаляем элемент из массива по индексу

                }
            } else {
                // Если товар уже есть в корзине, обновляем его количество
                existingProduct.product_quantity = count;
            }

            localStorage.setItem('cart', JSON.stringify(cart));
        });
    });
});