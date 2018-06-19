// For header button color
var headerButtons = document.getElementsByClassName('header-button');
for (let btn of headerButtons) {
    btn.addEventListener("mouseover", function () {
        this.style.backgroundColor = 'blue'
    })
    btn.addEventListener("mouseout", function () {
        this.style.backgroundColor = "#5bc0de"
    })
}


var regLogButton = document.getElementsByClassName('user-reg-log-button');
for (let button of regLogButton) {
    button.addEventListener("mouseover", function () {
        this.style.backgroundColor = "#ef9a9a"
    })
    button.addEventListener("mouseout", function () {
        this.style.backgroundColor = "red"
    })
}


// For the exchange data
var exchangeButton = document.getElementById('exchange-button');
exchangeButton.addEventListener('click', exchange());


function exchange() {
    fetch('http://apilayer.net/api/live?access_key=4674244d882e754ce2c95f1f0fc907cc&currencies=EUR,GBP,RUB,HUF&source=USD&format=1')
    .then((response) => response.json())
    .then((data)=>{
        let quotes = data.quotes
        document.getElementById("eur").innerHTML = quotes['USDEUR']
        document.getElementById("gbp").innerHTML = quotes['USDGBP']
        document.getElementById("rub").innerHTML = quotes['USDRUB']
        document.getElementById("huf").innerHTML = quotes['USDHUF']
    })
}


// TO get the user current place
var accountButton = document.getElementById('account-button');
accountButton.addEventListener('click', getAddress());

function getAddress() {
    fetch('http://api.ipstack.com/80.98.112.241?access_key=857bd1f1c26ae495c8078145822f24a4&format=1')
    .then((response) => response.json())
    .then((data) => {
            document.getElementById('current-place').innerHTML = data.country_name
            document.getElementById('city-name').innerHTML = data.region_name
        })
}

// get your exchange data from this link
// https://v3.exchangerate-api.com/bulk/d9e74d595777c01c2bff96e7/HUF