const successPopup = document.getElementById('success-popup');
const backButton = document.getElementsByClassName('back-button')[0];

document.getElementById('submitButton').addEventListener('click', async () => {
    const form = document.getElementById("createOrderForm");
    const formUrl = form.getAttribute("action");
    try {
        console.log(form);
        // Отправляем AJAX-запрос на сервер
        const response = await fetch(formUrl, {
            method: 'POST', headers: {
                'Content-Type': 'application/json', 'X-CSRFToken': CSRF_token,
            }, body: JSON.stringify(Object.fromEntries(new FormData(form))),
        });

        const data = await response.json();

        if (data.success) {
            // Очищаем корзину в localStorage
            localStorage.removeItem('cart');
            localStorage.removeItem('cart_id');
            successPopup.classList.remove('hidden');
            setTimeout(() => {
                successPopup.classList.add('hidden');
                setTimeout(() => {
                    backButton.click();
                }, 500); // Задержка в 0.5 секунды перед нажатием на backButton
            }, 1500);

        } else {
            alert(data.message);
        }


    } catch (error) {
        console.log(data);
        alert('Some wrong');
    }
});