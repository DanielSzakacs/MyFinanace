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


