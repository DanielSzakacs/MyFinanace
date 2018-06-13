var headerButtons = document.getElementsByClassName('header-button');
for (let btn of headerButtons) {
    btn.addEventListener("mouseover", function () {
        this.style.backgroundColor = 'blue'
    })
    btn.addEventListener("mouseout", function () {
        this.style.backgroundColor = "#5bc0de"
    })
}



/*
function cal() {
    let button = document.getElementById('calculate');
    button.addEventListener('click', function () {
    let income = document.getElementsByName('income');
    console.log(income);
    alert(income)
}
})
cal();
*/