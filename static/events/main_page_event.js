var headerButtons = document.getElementsByClassName('header-button')
for (let btn of headerButtons){
    btn.addEventListener("mouseover", function () {
        this.style.backgroundColor = 'red'
    })
    btn.addEventListener("mouseout", function () {
        this.style.backgroundColor = "#5bc0de"
    })
}