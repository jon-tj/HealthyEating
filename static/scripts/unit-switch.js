let switches = document.querySelectorAll(".unit-switch");
units={};
unitSwitchEvents={};

function addSwitchEvent(name,event){
    unitSwitchEvents[name]=event;
}

switches.forEach((s)=>{
    let name = s.getAttribute("name");
    let options = s.querySelectorAll("option");
    let thumb = s.querySelector(".thumb");
    units[name]=options[0].getAttribute("value");
    s.setAttribute("value", 0);
    s.addEventListener("click",()=>{
        let value = 1-s.getAttribute("value"); // Binary switch ;)
        s.setAttribute("value", value);
        units[name]=options[value].getAttribute("value");
        if(unitSwitchEvents[name])
            unitSwitchEvents[name]();
        thumb.style.left=(value?options[0].clientWidth:0)+"px";
    });
});