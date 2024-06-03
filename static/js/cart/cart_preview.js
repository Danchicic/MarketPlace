// openCartBtn.addEventListener("click", () => {
//     cart.forEach((product) => {
//         let htmlProduct = document.createElement('li');
//         let htmlProductImg = document.createElement("img");
//         let htmlProductName = document.createElement('div');
//         let htmlProductPrice = document.createElement('div');
//         let htmlProductQuantity = document.createElement('div');
//
//         htmlProduct.classList.add("product");
//
//         htmlProductImg.setAttribute('src', product.img_src);
//         htmlProductImg.classList.add("product_img");
//
//         htmlProductName.textContent = product.name;
//         htmlProductName.classList.add("product_name");
//
//         htmlProductPrice.textContent = product.price;
//         htmlProductPrice.classList.add("product_price");
//
//         htmlProductQuantity.classList.add("product_quantity");
//
//         htmlProduct.appendChild(htmlProductImg);
//         htmlProduct.appendChild(htmlProductName);
//         htmlProduct.appendChild(htmlProductPrice);
//         htmlProduct.appendChild(htmlProductQuantity);
//
//         let cart_wrapper = document.getElementById('cart-wrapper');
//         cart_wrapper.appendChild(htmlProduct);
//
//
//     });
// });