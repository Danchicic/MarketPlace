document.addEventListener("DOMContentLoaded", function () {
    cards.forEach((card) => {
        const buttonAdd = card.querySelector(".add-product");
        const buttonDelete = card.querySelector(".remove-product");

        let count = parseInt(card.dataset.count) || 0;

        const product_id = card.querySelector('a').getAttribute('href');

        buttonAdd.addEventListener("click", () => {
            count++;
            buttonDelete.style.display = "inline-block";
            buttonAdd.textContent = "+";
            counterSpan.style.display = "inline-block";
            counterSpan.textContent++;
            //saving cart

            // Проверяем, есть ли товар с данным product_id в корзине
            const existingProduct = cart.find(function (item) {
                return item.product_id === product_id;
            });
//////////where to here stops work with cart and local storage

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
            // console.log(product_json);

            // Сохраняем обновленное содержимое корзины в локальное хранилище
            localStorage.setItem('cart', JSON.stringify(cart));

        });
        buttonDelete.addEventListener("click", () => {
            if (count > 0) {
                console.log("press minus button");
                count--;
                counterSpan.textContent--;
                if (parseInt(counterSpan.textContent) === 0) {
                    counterSpan.style.display = 'none';

                }
                //update local storage
                // Проверяем, есть ли товар с данным product_id в корзине
                const existingProduct = cart.find(function (item) {
                    return item.product_id === product_id;
                });

                if (existingProduct) {
                    if (parseInt(existingProduct.product_quantity) === 1) {
                        buttonDelete.style.display = "none";
                        buttonAdd.textContent = "add";
                    } else {
                        // Если товар уже есть в корзине, обновляем его количество
                        existingProduct.product_quantity = count;
                        console.log('quantity more');
                    }
                }
                localStorage.setItem('cart', JSON.stringify(cart));

            } else if (count <= 0) {

                //delete item from  cart and local storage
                const product_index = cart.findIndex(function (product) {
                    return product.product_id === product_id;
                })
                if (product_index !== -1) {
                    cart.splice(product_index, 1); // Удаляем элемент из массива по индексу
                }

                // Сохраняем обновленное содержимое корзины в локальное хранилище
                localStorage.setItem('cart', JSON.stringify(cart));
                if (parseInt(counterSpan.textContent) > 0) {
                    buttonDelete.style.display = "none";
                    buttonAdd.textContent = "add";
                } else {
                    buttonDelete.style.display = "none";
                    buttonAdd.textContent = "add";
                    counterSpan.style.display = 'none';
                }

            }


        });
    });
});