var wood=0;
var countw=0;
var rock=0;
var countr=0;
var gold=0;
var countg=0;
var countl=0;
function addWood(){
    wood+=countw;
    document.getElementById("wood-count").innerHTML=wood;
}
function setWood(){
    countw=Math.floor((Math.random()*4)+5);
    document.getElementById("count-wood").innerHTML=countw;
}
function addRock(){
    rock+=countr;
    document.getElementById("rock-count").innerHTML=rock;
}
function setRock(){
    countr=Math.floor((Math.random()*6)+10);
    document.getElementById("count-rock").innerHTML=countr;
}
function addGold(){
    gold+=countg;
    document.getElementById("gold-count").innerHTML=gold;
}
function setGold(){
    countg=Math.floor((Math.random()*3)+6);
    document.getElementById("count-gold").innerHTML=countg;
}
function upgrade(){
    if(wood>10 && rock>15 && gold>8 && countl==0)
         {
         alert("Вы апнули замок на 1 уровень");
         wood -=10;
         rock -=15;
         gold -=8;
         countl++;
         document.getElementById("wood-count").innerHTML=wood;
         document.getElementById("rock-count").innerHTML=rock;
         document.getElementById("gold-count").innerHTML=gold;
         document.getElementById("count-level").innerHTML=countl;
         document.getElementById("level-count").innerHTML=countl;
         }
    else if(wood>100 && rock>150 && gold>80 && countl==1)
         {
         alert("Вы апнули замок на 2 уровень");
         wood -=100;
         rock -=150;
         gold -=80;
         countl++;
         document.getElementById("wood-count").innerHTML=wood;
         document.getElementById("rock-count").innerHTML=rock;
         document.getElementById("gold-count").innerHTML=gold;
         document.getElementById("count-level").innerHTML=countl;
         document.getElementById("level-count").innerHTML=countl;
         }
    else if(wood>1000 && rock>1500 && gold>800 && countl==2)
         {
         alert("Вы апнули замок на 3 уровень");
         wood -=1000;
         rock -=1500;
         gold -=800;
         countl++;
         document.getElementById("wood-count").innerHTML=wood;
         document.getElementById("rock-count").innerHTML=rock;
         document.getElementById("gold-count").innerHTML=gold;
         document.getElementById("count-level").innerHTML=countl;
         document.getElementById("level-count").innerHTML=countl;
         }
}
function add(){
    setInterval(addWood,10000);
    setInterval(addRock,14000);
    setInterval(addGold,18000);
    setInterval(upgrade,1000);
}
function set(){
    setWood();
    setRock();
    setGold();
}
function Run(){
    set();
    add();
}