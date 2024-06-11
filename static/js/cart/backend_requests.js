function addListenerToCreateOrderButton() {
    const createOrderButton = document.getElementById('createUserCart');

    createOrderButton.addEventListener('click', function () {
        const urlAddress = document.getElementById('cart-wrapper').getAttribute('action');

        if (urlAddress === '/orders/') {
            //check if cart already created
            if (localStorage.getItem('cart_id')) {
                window.location.href = '/orders?cart_id=' + localStorage.getItem('cart_id');
                localStorage.setItem("cart_id", data.cart_id)
            } else {
                //create a new cart by post request¬
                let request = fetch(urlAddress, {
                    method: "POST", headers: {
                        'Content-Type': 'application/json', "X-CSRFToken": CSRF_TOKEN
                    }, body: JSON.stringify(cart)
                }).then(response => response.json())
                    // get cart_id from a database and saving it in local storage
                    .then(data => {
                        window.location.href = data.redirect_url + '?cart_id=' + data.cart_id;
                        localStorage.setItem("cart_id", data.cart_id)
                    })
                    .catch(error => console.error("Ошибка fetch запроса:", error));
            }
        } else if (urlAddress === '/users/') {
            alert("user dont authorized");
            
        }
    });
}