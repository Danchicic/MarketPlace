openCartBtn.addEventListener("click", () => {
    cart.forEach((product) => {
        let htmlProduct = document.createElement('li');
        let htmlProductImg = document.createElement("img");
        let htmlProductName = document.createElement('div');
        let htmlProductPrice = document.createElement('div');
        htmlProductPrice.textContent = product.price;
        htmlProductName = product.name;
    });
});