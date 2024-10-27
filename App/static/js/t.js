const btn_vertify = document.querySelector('#vertify')
btn_vertify.addEventListener('click', async (event) => {
    event.preventDefault();
    let email = document.querySelector('#email').value;
    let messege = document.querySelector('#messege');
    if (!email) {
        messege.innerHTML = 'email is empty!!';
    } else {
        try {
            const res = await fetch(`/vertify?email=${email}`);
            const data = await res.json();
            if (data['status'] == 200) {
                messege.innerHTML = 'email vertifa code has send.';
                btn_vertify.disabled = true;
                let delta = 10;
                const interval = setInterval(() => {
                    if (!delta) {
                        btn_vertify.disabled = false;
                        btn_vertify.innerHTML = 'send code';
                        clearInterval(interval);
                    } else {
                        btn_vertify.innerHTML = delta;
                        delta -= 1;
                    }
                }, 1000);
            }
        } catch (err) {
            messege.innerHTML = 'Error: ' + err.message;
        }
    }
});