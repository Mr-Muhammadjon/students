let results = document.querySelector('.results')
let history = document.querySelector('.history')
let searchBlock = document.querySelector('.liveSearch')
searchBlock.style.display = 'none'
function liveSearch (value){
    if(value === ''){
        history.style = 'display: block'
        results.style = 'display: none'
    }else{
        history.style = 'display: none'
        results.style = 'display: block'
    }
    if (window.XMLHttpRequest) {
        var xhttp=new XMLHttpRequest();
    } else {  // code for IE6, IE5
        var xhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState === 4 & xhttp.status === 200) {
            var data = JSON.parse(this.responseText);
            let products = data['history']
            for(item in products){
                template = `
                        <li>To'ladi ---> <b>${products[item].time} ${products[item].payed_money}</b> so'm</li>
                        <li>Keldi ---> <b>${products[item].time}</b></li>
                `
                results.innerHTML = template
            }
            
        }else{
            console.log('Yemadi')
        }
    }
    var url = "/search/"
    xhttp.open("GET", url+`?data=${value}`, true);
    xhttp.send();
}