let elements = document.querySelectorAll(".carousel");

elements.forEach((e)=>{
    e.setAttribute("page",0);
    var container = e.children[0];
    let width = e.clientWidth;
    for(var i=0; i<container.children.length; i++) {
        var aside = container.children[i];
        aside.style.width = width+"px";
    }
    e.querySelectorAll(".next-slide").forEach((button)=>{
        button.addEventListener("click",()=>{
            let page = parseInt(e.getAttribute("page"));
            page += 1;
            e.setAttribute("page", page);
            container.style.left = -page*width+"px";
        });
    });
    e.querySelectorAll(".reset").forEach((button)=>{
        button.addEventListener("click",()=>{
            e.setAttribute("page", 0);
            container.style.left = "0px";
        });
    });
});