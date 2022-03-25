var Cards = [
    {name:"Charmander",attributes :{atk:10,def:4,spell:6}},
    {name:"Squirtle",attributes :{atk:5,def:10,spell:3}},
    {name:"Bulbasaur",attributes :{atk:3,def:6,spell:10}}
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
    displayOptions()
} 

function displayOptions(){
    var chose = document.getElementById("chose")
    var choseText = ""
    for (var attribute in cardPlayer.attributes){
        choseText += `<input type="radio" name = "attribute" value="${attribute}">${attribute}`
    }
    chose.innerHTML = choseText
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
    document.getElementById("resultado").innerHTML = `<h1>${finish}</h1>`
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