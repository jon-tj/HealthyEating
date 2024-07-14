const inputField = document.querySelector('input.query-recipe')
const outputField = document.querySelector('output.query-recipe')

inputField.addEventListener('keydown', function(event) {
    if (event.key === 'Enter' || event.keyCode === 13) {
        // Prevent the default action if needed (e.g., if the input is inside a form)
        event.preventDefault()
        GetRecipe(inputField.value)
    }
});
function GetRecipe(url){
    let success = false
    fetch(`/api/v1/analyze/${btoa(url)}`)
    .then(res=>{
        success = res.status === 200
        if(success) return res.json()
        else return res.text();
    })
    .then(data=>{
        if(!success){
            Toast(data)
            return
        }
        // Calculate the total amount of nutrients
        //console.log(data)
        let totalNutrients = {}
        for(let i=0; i < data["ings"].length; i++){
            let nutrients = data["ings"][i]["nutrition"]
            let grams = data["ings"][i]["grams"]
            let nutrientNames = Object.keys(nutrients)//Array.from(nutrients.keys())
            if(isNaN(nutrients["Energy"])){
                console.warn(`No data for ingredient: ${data["ings"][i]["name"]}`)
                continue
            }
            for(let j=0; j < nutrientNames.length; j++){
                let key = nutrientNames[j]
                if(["Category","Name"].includes(key))
                    continue
                if(!(key in totalNutrients))
                    totalNutrients[key] = 0
                totalNutrients[key] += nutrients[key] * grams/100 //Nutrition is given in per100g
            }
        }
        let totalNutrStr = ""
        for(let n of Object.keys(totalNutrients)){
            totalNutrients[n] /= data["yield"]
            if(n=="Energy")
                value=totalNutrients[n]+"kJ"
            else
                value = AmountMgToString(totalNutrients[n])
            totalNutrStr += `${n}: ${value}\n`
        }
        
        outputField.innerText = `
        Name: ${data["name"]}
        Total nutritional value: ${totalNutrStr}
        Estimated bioavailability: Not implemented
        `
        
        
        //data["nutr"]
    })
}

function AmountMgToString(mg){
    if(mg>=0.5e+3) return `${(mg * 1e-3).toFixed(2)}g`
    if(mg>=0.5e+0) return `${(mg * 1e-0).toFixed(2)}mg`
    if(mg>=0.5e-3) return `${(mg * 1e+3).toFixed(2)}mcg`
}