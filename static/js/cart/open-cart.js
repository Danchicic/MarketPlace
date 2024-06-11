// Получаем элементы кнопки открытия корзины и оверлея корзины
const openCartBtn = document.getElementById('openCartBtn');


openCartBtn.addEventListener('click', function () {

    //1 создать темный фон
    const bodyOverlay = document.createElement('div');

    bodyOverlay.classList.add('body_overlay');
    document.querySelector('body').style.overflow = 'hidden';


    const cart_preview = document.createElement('div');
    //cart-preview;
    cart_preview.classList.add("cart_preview");
    cart_preview.setAttribute('id', 'cart-wrapper');
    cart_preview.style.display = 'flex';
    // //csrf protect
    // const csrfTokenHtml = document.createElement("input");
    // csrfTokenHtml.type = 'hidden';
    // csrfTokenHtml.name = 'csrfmiddlewaretoken';
    // csrfTokenHtml.value = CSRF_TOKEN;
    // // cart_preview.appendChild(csrfTokenHtml);

    //creating cart products
    const cart_items = document.createElement('ul');
    cart_items.classList.add('cart_items');

    //creating and styling close button
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

    if (cart.length === 0) {
        const middleText = document.createElement('p');
        middleText.textContent = "Your cart is empty"
        cart_preview.style.alignItems = "center";

        cart_preview.appendChild(middleText);
        cart_preview.appendChild(closingSpan);


    } else {
        cart.forEach(function (product) {
            //create product html block
            let htmlProduct = document.createElement('li');

            let htmlProductImg = document.createElement("img");
            let htmlProductName = document.createElement('div');
            let htmlProductPrice = document.createElement('div');
            let htmlProductQuantity = document.createElement('div');

            htmlProduct.classList.add("product");
            htmlProduct.setAttribute('name', product.product_id);

            htmlProductImg.setAttribute('src', product.img_src);
            htmlProductImg.classList.add("product_img");

            htmlProductName.textContent = product.name;
            htmlProductName.classList.add("product_name");

            htmlProductPrice.textContent = product.price;
            htmlProductPrice.classList.add("product_price");

            htmlProductQuantity.classList.add("product_quantity");

            htmlProduct.appendChild(htmlProductImg);
            htmlProduct.appendChild(htmlProductName);
            htmlProduct.appendChild(htmlProductPrice);
            htmlProduct.appendChild(htmlProductQuantity);

            cart_items.appendChild(htmlProduct);


        });

        //creating submit button
        const submitButtonWrapper = document.createElement("div");
        submitButtonWrapper.classList.add('submit-wrapper');
        //create <a> to redirect user
        const urlWrapper = document.createElement('a');

        const inputButton = document.createElement("input");
        inputButton.id = "createUserCart";
        //get user.is_authorized from django template
        const isUserAuthenticated = document.body.getAttribute('data-user-authenticated') === 'True';

        if (isUserAuthenticated) {
            inputButton.classList.add("open_order");
            inputButton.type = 'submit';
            inputButton.value = 'Go to order page';

            //get url from django
            const createOrderSrc = document.body.getAttribute('data-create-order-src');
            urlWrapper.href = createOrderSrc;
            /////////////
            cart_preview.setAttribute('action', createOrderSrc);

        } else {
            inputButton.classList.add("create_profile");
            inputButton.type = 'button';
            inputButton.value = 'Create profile or login';
            //get url from django
            const loginSrc = document.body.getAttribute('data-login-url');
            urlWrapper.href = loginSrc;
            /////////////////
            cart_preview.setAttribute('action', loginSrc);

        }
        //appending button to link tag
        // urlWrapper.appendChild(inputButton);
        //appending button block
        submitButtonWrapper.appendChild(inputButton);
        //appending products from localStorage
        cart_preview.appendChild(closingSpan);

        cart_preview.appendChild(cart_items);
        //append submit button
        cart_preview.appendChild(submitButtonWrapper);

    }


    //appending black-overlay and cart to body
    document.querySelector("body").appendChild(cart_preview);
    document.querySelector("body").appendChild(bodyOverlay);
    addListenerToCreateOrderButton();


});

