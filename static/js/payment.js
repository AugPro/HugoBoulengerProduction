paypal.Button.render({

    env: 'sandbox', // Or 'sandbox',

    client: {
        sandbox:    'AS-xKeq0Yz87G13Tb_qTXKk4_Fs19StF7z5F5-qPBJ9Hv8j8l55SpCzxu0_o3c3cL9gF7Ac_I-MOVQez',
        production: 'xxxxxxxxx'
    },

    style: {
        label: 'generic',
        size:  'responsive',    // small | medium | large | responsive
        shape: 'pill',     // pill | rect
        color: 'gold',     // gold | blue | silver | black
        tagline: false
    },

    commit: true, // Show a 'Pay Now' button

    payment: function(data, actions) {
        return actions.payment.create({
            payment: {
                transactions: [
                    {
                        amount: { total: '0.01', currency: 'USD' }
                    }
                ]
            }
        });
    },

    onAuthorize: function(data, actions) {
        return actions.payment.execute().then(function() {
            window.alert('Payment Complete!');
        });
    }

}, '#paypal-button');
