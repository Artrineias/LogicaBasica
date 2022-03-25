var Cards = [
    {name:"Charmander",attributes :{atk:10,def:4,spell:6},imagem:"https://pbs.twimg.com/profile_images/1377854248621199360/F7S8p4xK_400x400.jpg"},
    {name:"Squirtle",attributes :{atk:5,def:10,spell:3},imagem:"https://i.pinimg.com/564x/03/e5/18/03e518436db20497bf05cf6512863935.jpg"},
    {name:"Bulbasaur",attributes :{atk:3,def:6,spell:10},imagem:"https://i.pinimg.com/originals/34/9e/2a/349e2a4d065dcc55a417ac6f0528a5cf.jpg"}
]

function drawCard(){
    var numberMachine = parseInt(Math.random()*3)
    var numberPlayer = parseInt(Math.random()*3)
    while(numberPlayer==numberMachine){
        numberMachine = parseInt(Math.random() * 3)
    }
    cardPlayer = Cards[numberPlayer]
    cardMachine = Cards[numberMachine]
    document.getElementById("btnSortear").disabled =true
    document.getElementById("btnJogar").disabled =false
    showCardPlayer()
    showCardMachine()
} 

function getAttribute(){
     var listAttributes = document.getElementsByName("attribute")
     for (var a=0;a<listAttributes.length;a++){
         if(listAttributes[a].checked){
            return listAttributes[a].value
         }
     }
}

function play(){
    playerOn = getAttribute()
    attributeMachine = cardMachine.attributes[playerOn]
    attributePlayer = cardPlayer.attributes[playerOn]
    finish = comparison(attributePlayer,attributeMachine)
    document.getElementById("resultado").innerHTML = finish
    document.getElementById("btnJogar").disabled = true
}

function comparison(player,machine){
    if(player>machine){
        return "Player Winner"
    }
    else if(player<machine){
        return "Player Losser"
    }
    else{
        return "Draw..."
    }
}

function showCardPlayer(){
    var divCardplayer = document.getElementById("cardPlayer")
    divCardplayer.style.backgroundImage = `url(${cardPlayer.imagem})`
    var moldura = 
    '<img src="https://www.alura.com.br/assets/img/imersoes/dev-2021/card-super-trunfo-transparent-ajustado.png"'+
    'style=" width: inherit; height: inherit; position: absolute;"></div>">'
    
    var tagHTMl= "<div id='chose' class='carta-status'>"
    
    var choseText = ""
    for (var attribute in cardPlayer.attributes){
        choseText += `<input type="radio" name = "attribute" 
        `+`value="${attribute}">${attribute} ${cardPlayer.attributes[attribute]}<br>`
    }
    var name = `<p class="carta-subtitle" >${cardPlayer.name}</p>`
    divCardplayer.innerHTML = moldura + name + tagHTMl + choseText+ "</div>"
}

function showCardMachine(){
    var divCardMachine = document.getElementById("cardMachine")
    divCardMachine.style.backgroundImage = `url(${cardMachine.imagem})`
    var moldura = 
    '<img src="https://www.alura.com.br/assets/img/imersoes/dev-2021/card-super-trunfo-transparent-ajustado.png"'+
    'style=" width: inherit; height: inherit; position: absolute;"></div>">'
    
    var tagHTMl= "<div id='chose' class='carta-status'>"
    
    var choseText = ""
    for (var attribute in cardMachine.attributes){
        choseText += `<p type="text" name = "attribute" 
        `+`value="${attribute}">${attribute} ${"???"}</p> `
    }
    var name = `<p class="carta-subtitle" >${cardMachine.name}</p>`
    divCardMachine.innerHTML = moldura + name + tagHTMl + choseText+ "</div>"
}