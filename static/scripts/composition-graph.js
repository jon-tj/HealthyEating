let canvas = document.getElementById("composition-graph");

let ctx = canvas.getContext("2d");

w = canvas.clientWidth;
h = canvas.clientHeight;
r=Math.min(w,h)*0.45;
colors = [
    "#FF8B94",  // Saturated Pink
    "#FFB385",  // Saturated Peach
    "#FFF685",  // Saturated Yellow
    "#85FF9E",  // Saturated Green
    "#85CFFF",  // Saturated Blue
    "#A885FF",  // Saturated Lavender
    "#FF85BF",  // Saturated Rose
    "#85FFFF"   // Saturated Aqua
]

function DrawComposition(comp){
    ctx.fillStyle="white";
    ctx.fillRect(0,0,w,h);

    let angle = Math.PI;
    for(let i=0; i<comp.length; i++){
        ctx.lineWidth=r*0.3;
        let angle1=angle+comp[i].amount*Math.PI*2.001;
        let centerAngle = (angle+angle1)/2;
        ctx.beginPath();
        ctx.arc(w/2,h/2+5,r*0.6,angle,angle1);
        angle = angle1;
        ctx.strokeStyle=colors[i];
        ctx.stroke();

        let dir={x:Math.cos(centerAngle),y:Math.sin(centerAngle)};
        let arrowBegin = {x:w/2+dir.x*r*0.7, y:h/2+5+dir.y*r*0.7}
        if(Math.abs(dir.y)<0.6){
            dir.y=Math.sign(dir.y)*0.7;
            let magnitude = Math.sqrt(dir.x*dir.x+dir.y*dir.y)
            dir.y/=magnitude;
            dir.x/=magnitude;
        }
        let side=Math.sign(dir.x);
        let arrowBend = {x:arrowBegin.x+dir.x*20,y:arrowBegin.y+dir.y*20};
        let arrowEnd = {x:w/2+side*r,y:arrowBend.y};
        ctx.beginPath();
        ctx.moveTo(arrowBegin.x,arrowBegin.y);
        ctx.lineTo(arrowBend.x,arrowBend.y);
        ctx.lineTo(arrowEnd.x,arrowEnd.y);
        ctx.lineWidth=1;
        ctx.strokeStyle="black";
        ctx.stroke();
        ctx.font="15px Arial";
        ctx.fillStyle="black";
        let label=comp[i].label+` (${comp[i].amount*100}%)`
        let labelWidth = ctx.measureText(label).width;
        ctx.fillText(label,arrowEnd.x+side*3-(side==-1?labelWidth:0),arrowEnd.y+5);
    }
}

var testcomp=[
    {label:"SFA",amount:0.1},
    {label:"MUFA",amount:0.2},
    {label:"PUFA",amount:0.15},
    {label:"Carbs",amount:0.25},
    {label:"Protein",amount:0.3},

];
DrawComposition(testcomp);