var tableList=[{name:"erik",win: 0,lose:0,draw:0,points:0},
{name:"gabriel",win: 0,lose:0,draw:0,points:0}]

function calculatePoints(player){
    var points = player.win * 3 + player.draw
    return points
}

function showScreen(){
    var table = ""
    for (var i =0; i < tableList.length ;i++){
        tableList[i].points = calculatePoints(tableList[i])
        table +=`<tr></tr>`
        table += `<td>${tableList[i].name}</td>`
        table += `<td>${tableList[i].win}</td>`
        table += `<td>${tableList[i].draw}</td>`
        table += `<td>${tableList[i].lose}</td>`
        table += `<td>${tableList[i].points}</td>`
        table +=`<td><button onClick="addWin(${i})">Vitória</button></td>`
        table +=`<td><button onClick="addDraw(${i})">Empate</button></td>`
        table +=`<td><button onClick="addLose(${i})">Derrota</button></td>`
        table += `</tr>`

    }
    var tag = document.getElementById("main")
    tag.innerHTML = table
    document.getElementById("Name").value = ""
}

function addWin(player){
    tableList[player].win++
    tableList[player].points = calculatePoints(tableList[player])
    showScreen()
}

function addLose(player){
    tableList[player].lose++
    tableList[player].points = calculatePoints(tableList[player])
    showScreen()
}

function addDraw(player){
    tableList[player].draw++
    tableList[player].points = calculatePoints(tableList[player])
    showScreen()
}

function addPlayer(){
    var player = document.getElementById("Name").value 
    addToList(player)
}

function addToList(name){
    var player = {name:name,win:0,draw:0,lose:0,points:0}
    tableList.push(player)
    mostrarTela()

}