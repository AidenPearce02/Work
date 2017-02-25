var Storage_Of_Events = [];

var today = new Date();

var events = [
    {
        id: 0,
        name: "Игра NaVi - EHOME",
        dateStart: new Date(2011, 10, 22, 12, 0),
        dateEnd: new Date(2011, 10, 22, 14, 0),
        location: "Кёльн"
    },
    {
        id: 1,
        name: "Игра NaVi - Team Secret",
        dateStart: new Date(2016, 6, 24, 17, 0),
        dateEnd: new Date(2016, 6, 24, 19, 0),
        location: "Лос-Анджелес"
    },
    {
        id: 2,
        name: "Чемпионат по шахматам",
        dateStart: new Date(2017, 1, 8, 12, 0),
        dateEnd: new Date(2017, 2, 8, 12, 0),
        location: "Полтава"
    },
    {
        id: 3,
        name: "Golden Byte",
        dateStart: new Date(2017, 2, 1, 12, 0),
        dateEnd: new Date(2017, 2, 10, 17, 0),
        location: "Полтава"
    },
    {
        id: 4,
        name: "1 сентября",
        dateStart: new Date(2017, 8, 1, 0, 0),
        dateEnd: new Date(2017, 8, 1, 24, 0),
        location: "Полтава"
    },
    {
        id: 5,
        name: "International 2017",
        dateStart: new Date(2017, 5, 22, 12, 0),
        dateEnd: new Date(2017, 7, 14, 12, 0),
        location: "Сиэтл"
    }
];

function dateFormat(date)
{
    var months = [
        'января',
        "февраля",
        "марта",
        "апреля",
        "мая",
        "июня",
        "июля",
        "августа",
        "сентября",
        "октября",
        "ноября",
        "декабря"
    ];
    var minutes="";
    if (date.getMinutes()<10)
        minutes="0"+date.getMinutes();
    else
        minutes=date.getMinutes();
    var hours="";
    if (date.getHours()<10)
        hours="0"+date.getHours();
    else
        hours=date.getHours();
    return date.getDate() + " "
        + months[date.getMonth()] + " "
        + date.getFullYear() + " "
        + hours + ":"
        + minutes;

}

function getDateByID(id){
    if (Storage_Of_Events[id] != undefined || Storage_Of_Events[id] != null)
        return eventToString(Storage_Of_Events[id]);
    else
        return "\nStorage doesn't have event with this id";
}

function addEventsToStorage(events)
{
    events.forEach(function(item){
        Storage_Of_Events[item.id] = {
            name : item.name,
            dateStart: item.dateStart,
            dateEnd: item.dateEnd,
            location: item.location
        }
    });
}
addEventsToStorage(events);

function getEvents(chosen){
    var temp=[];
    Storage_Of_Events.forEach(function(item,i,Storage_Of_Events){
        if(chosen==-1){
            if(item.dateEnd.getTime() < today.getTime()){
                temp[temp.length++]=item;
            }
        }
        if(chosen==0){
            if(item.dateStart.getTime() < today && item.dateEnd.getTime() >= today){
                temp[temp.length++]=item;
            }
        }
        if(chosen==1){
            if(item.dateStart.getTime() > today){
                temp[temp.length++]=item;
            }
        }
    });
    return List_Of_Event(temp);

}

function List_Of_Event(list)
{
    return list.map(function(item) {
        if(item != undefined || item != null)
            return eventToString(item);
    });
}

function eventToString(event)
{
    return "\n\nНазвание: "  + event.name + ";\nДата начала: "+ dateFormat(event.dateStart) + ";\nДата окончания: " +
    dateFormat(event.dateEnd) + ";\nМесто проведения: " + event.location;
}

console.log("Текущая дата - " + dateFormat(today));
console.log("*************************************");

console.log("1 cобытие  "+getDateByID(0));
console.log("*************************************");


console.log("228 cобытие  "+getDateByID(228));
console.log("*************************************");

console.log("Прошедшие событии  "+getEvents(-1));
console.log("*************************************");

console.log("Текущие событии  "+getEvents(0));
console.log("*************************************");

console.log("Будущие событии"+getEvents(1));
console.log("*************************************");

console.log("Все события"+List_Of_Event(Storage_Of_Events));
console.log("*************************************");



