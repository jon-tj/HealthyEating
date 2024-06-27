function bmr_mifflinJeor(profile){
    let bmr = 10*profile.weight + 6.25*profile.height - 5*profile.age
    switch(profile.gender){
        case "male": bmr += 5; break; 
        case "female": bmr -= 161; break;
        case "none": bmr -= 48; break;
    }
    return bmr * [1.2, 1.375, 1.55, 1.725, 1.9][profile.activityCode];
}


let container = document.querySelector("#bmr-calc");
let outputHeader = document.querySelector("#bmr-result");
let bmrProfile=null;

if(container && outputHeader){
    function bmr_updateResult(){
        bmr = bmr_mifflinJeor(bmrProfile);
        if(units["bmr"]=="kj")
        bmr *= 4.184;
        outputHeader.innerText = Math.round(bmr,2);
    }
    addSwitchEvent("bmr",bmr_updateResult);
    function resetProfile() {
        bmrProfile={gender:"none", weight:70, height:180, age:22, activityCode:0};
        bmr_updateResult();
    }
    resetProfile();
    
    let profileUpdateRule={
        age:container.querySelector("input[name='age']"),
        gender:container.querySelector("select[name='gender']"),
        height:container.querySelector("input[name='height']"),
        weight:container.querySelector("input[name='weight']"),
        activityCode:container.querySelector("select[name='activityCode']"),
    }
    
    profileUpdateRule.age.addEventListener('input', function() {
        bmrProfile.age = this.value;
        bmr_updateResult();
    });

    profileUpdateRule.gender.addEventListener('change', function() {
        bmrProfile.gender = this.value;
        bmr_updateResult();
        switch(bmrProfile.gender){
            case "male": profileUpdateRule.height.value = 180; break; 
            case "female": profileUpdateRule.height.value = 167; break;
        }
    });

    profileUpdateRule.height.addEventListener('input', function() {
        bmrProfile.height = this.value;
        bmr_updateResult();
        let inches = this.value * 0.39;
        switch(bmrProfile.gender){
            case "male": profileUpdateRule.weight.value = Math.round(50+2.3*(inches-60)); break; 
            case "female": profileUpdateRule.weight.value = Math.round(45.5+2.3*(inches-60)); break;
        }
    });

    profileUpdateRule.weight.addEventListener('input', function() {
        bmrProfile.weight = this.value;
        bmr_updateResult();
    });

    profileUpdateRule.activityCode.addEventListener('change', function() {
        bmrProfile.activityCode = this.value;
        bmr_updateResult();
    });
    container.querySelector(".reset").addEventListener('click', resetProfile);

}else{
    console.warn("No container/result header found!");
}