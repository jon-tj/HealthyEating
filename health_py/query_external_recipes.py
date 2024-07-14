import requests as req
import json

def get_recipe(url):
    headers = {
        'User-Agent': 'Your User Agent String Here'
    }
    response = req.get(url, headers=headers)
    if response.status_code//100 == 2:
        # Look for recipe json
        key = "application/ld+json"
        if key in response.text:
            start = response.text.index(key)
            end = response.text[start:].index("</script>")+start
            substr = response.text[start:end]
            substr = substr[substr.index(">")+1:]
            try:
                json_ = json.loads(substr)
            except:
                return ValueError("Recipe is not JSON.")
            return json_
        else:
            return ValueError("Failed to parse recipe.")
    return ConnectionRefusedError("Failed to fetch given url.")


def analyze(r, conn):
    if isinstance(r, str) or isinstance(r, bytes):
        print("Downloading recipe from",r)
        r=get_recipe(r)
        print("Done!")
    if "@graph" in r:
        for g in r["@graph"]:
            if g["@type"]=="Recipe":
                r=g
                break
            
    if ("lang" in r and "en" not in r["lang"]) or ("inLanguage" in r and "en" not in r["inLanguage"]):
        return ValueError("Can only parse English recipes")
    ings = [
    "sugar", "butter", "salt", "garlic","spring onion", "red onion","onion", "tomato sauce","tomato paste","tomato", "tomat", "olive oil", "soy sauce","soy", "vinegar", "tortilla", "flour", "baking powder", "banana", "peach", "mango", "bread", "vegetable stock", "stock", "chicken", "lamb", "fish", "meat", "beef", "pasta", "rice", "potato", "carrot", "cayenne", "bell pepper", "pepper", "cilantro", "parsley", "rosemary", "thyme", "basil", "oregano", "cumin", "coriander", "ginger", "cinnamon", "nutmeg", "cocoa powder", "honey", "maple syrup", "vanilla extract", "chili powder", "paprika", "mustard", "mayo", "ketchup", "mushroom", "zucchini", "eggplant", "egg", "spinach", "kale", "lettuce", "avocado", "cucumber", "asparagus", "broccoli", "cauliflower",  "corn", "black beans", "kidney beans", "chickpeas","peas", "lentils", "quinoa", "barley", "walnuts", "almonds", "cashew", "peanuts", "pistachio", "sunflower seeds", "pumpkin seeds", "chia seeds", "flax seeds", "sesame seeds", "poppy seeds", "coconut", "dates", "raisins", "cranberries", "blueberries", "strawberries", "raspberries", "blackberries", "pear", "orange", "lemon", "lime", "grapefruit", "kiwi", "pineapple",  "apple","watermelon", "melon", "fig", "pomegranate", "yogurt",  "milk",  "brie", "cheddar", "mozzarella", "parmesan", "cream cheese", "gouda", "feta", "goat cheese", "cheese","ricotta", "sour cream", "cream","pine nuts", "strawberry", "ham", "sausage", "pork", "hazelnut", "white chocolate", "chocolate", "berry", "anchovies", "oil", "marzipan", "apricot", "olive", "celery", "celeriac", "cocoa", "oat", "red wine", "chilli", "tabasco", "dill", "almond extract", "oyster sauce", "leek", "noodle", "spaghetti", "prosecco", "radish", "salmon", "bay leaves", "cabbage", "whisky", "chive", "watercress", "capers", "sake", "vodka", "bourbon", "prawn", "white wine", "plum", "dulce de leche", "nori", "seaweed", "currants", "shallot", "yeast", "wasabi", "lasagn", "saffron", "pecan", "raisin", "couscous", "marmalade", "masala", "syrup", "mint", "seed", "artichoke", "crème fraîche", "squid", "parsnip", "pastry", "curry", "fruit", "bay leaf", "almond", "bacon", "pak choi", "worcestershire", "salad", "harissa", "rosé wine", "custard", "bean paste", "black tea", "green tea", "matcha", "cherry", "cherries", "penne", "port", "aubergine", "star anise", "cod", "macaroni", "amarett", "mascarpone", "bicarbonate", "pesto", "water", "treacle","beansprout", "bean", "vanilla", "walnut", "hummus", "houmous", "meringue", "gelatin", "baguette", "kirsch", "tea", "tofu", "sprinkle", "madeira", "cardamom", "molass", "turkey", "brandy", "grain", "pine nut", "beetroot", "fromage frais", "caramel", "rum", "sherry", "pea", "turmeric", "vermouth", "tahini", "wheat", "mussel", "cavolo", "gorgonzola", "miso", "mange tout", "mangetout", "sage", "stilton", "berries", "whiskey", "chicory", "passata", "rose petals", "rotis", "rhubarb", "loaf", "bun", "tartar", "hoisin", "goose", "bok cho", "tarragon", "cider", "pancetta", "gherkin", "tagliatelle", "chestnut", "spring green", "brussels sprout", "barbecue sauce", "gnocchi", "shrimp", "icing", "vegetable bouillon", "tequila", "marshmallow", "duck", "clementine", "gin", "colouring", "coloring", "dye", "halloumi", "caper", "pudding", "turnip", "courgette", "sumac", "date", "seasoning", "tamarind", "batter", "wrap", "waffle", "muffin", "agar", "herb", "quail", "polenta", "prune", "margarine", "piri-piri", "lentil", "wrapper", "semolina", "gold", "silver", "sriracha", "tamari", "pigeon", "liqueur", "liquor", "yoghurt", "mackerel", "currant", "coffee", "hot sauce", "taco shell", "pecorino", "rocket", "arugula", "suet", "cleriac", "marsala", "quark", "sauce", "gruyère", "mace", "espresso", "scallop", "camembert", "quince", "trout", "anchovy", "jalapeño", "glitter", "grape", "citric acid", "chapati", "okra", "tzatziki", "vegetables", "chorizo", "granola", "pumpkin", "bass", "chipotle", "liver", "scallion", "wine", "relish", "tilapia", "mince", "crab", "tuna", "chili", "pico de gallo", "jicama", "collard", "tongue", "malunggay", "clam", "lobster", "chayote", "pimiento", "sardine", "mahi", "taro", "bamboo", "amaranth", "pig heart", "cognac", "paneer", "haddock", "panko", "baking soda", "agave", "papaya", "hotdog", "mirin", "gourd", "squash", "pig", "crust", "croûtons", "naan", "fondant", "guacamole", "tortellini", "ciabatta", "farfalle", "aquavit", "kipper", "glycerine", "sesame", "wood", "prosciutto", "guinness", "sponge fingers", "ladyfingers", "clove", "cacao", "citrus", "halibut", "tonkatsu", "katsuobushi", "shoyu", "konbu", "broth", "pita", "chile", "sauerkraut", "bagel", "campari", "orgeat", "seltzer", "kimchi", "galangal", "soda", "fillet", "leaves", "salsa", "toffee", "sultana", "rabbit", "rutabaga", "bitters", "pickle", "marmite", "malteser", "malt", "brioche", "cannabis", "cola", "ice"]
    aliases = {
        # old name : new name 
        "tomato paste":"tomato sauce",
        "passata":"tomato sauce",
        "tomat":"tomato",
        "goat cheese":"cheese",
        "stilton":"cheese",
        "ricotta":"cheese",
        "paprika":"bell pepper",
        "bay leaf":"bay leaves",
        "houmous":"hummus",
        "cacao":"cocoa powder",
        "rutabaga":"beetroot",
        "stock":"broth",
        "shoyu":"soy sauce",
        "sponge fingers": "ladyfingers",
        "prosciutto":"ham",
        "zucchini":"squash",
        "chilli":"chili",
        "scallion":"spring onion",
        "rocket":"arugula", #rukkola
        "liqueur": "liquor",
        "colouring": "coloring",
        "dye":"coloring",
        "mange tout":"mangetout",
        "vanilla extract":"vanilla",
        "bicarbonate":"baking soda",
        "aubergine":"eggplant",
        "pak choi":"bok choy",
        "bok cho":"bok choy",
        "whiskey":"whisky",
        "cherry":"cherries"
        }
    cat_ings = {
    "salt": "seasoning",
    "sugar": "seasoning",
    "butter": "dairy",
    "garlic": "vegetable",
    "red onion": "vegetable",
    "spring onion": "vegetable",
    "onion": "vegetable",
    "tomato": "vegetable",
    "tomat": "vegetable",
    "tomato sauce": "condiment",
    "olive oil": "oil",
    "soy sauce": "seasoning",
    "soy": "legume",
    "vinegar": "seasoning",
    "flour": "starch",
    "baking powder": "other",
    "banana": "fruit",
    "peach": "fruit",
    "mango": "fruit",
    "bread": "starch",
    "chicken": "meat",
    "lamb": "meat",
    "fish": "seafood",
    "meat": "meat",
    "beef": "meat",
    "pasta": "starch",
    "rice": "starch",
    "potato": "vegetable",
    "carrot": "vegetable",
    "cayenne": "seasoning",
    "bell pepper": "vegetable",
    "pepper": "seasoning",
    "cilantro": "herb",
    "parsley": "herb",
    "rosemary": "herb",
    "thyme": "herb",
    "basil": "herb",
    "oregano": "herb",
    "cumin": "seasoning",
    "coriander": "herb",
    "ginger": "seasoning",
    "cinnamon": "seasoning",
    "nutmeg": "seasoning",
    "cocoa powder": "legume",
    "honey": "sweet",
    "maple syrup": "sweet",
    "vanilla extract": "flavoring",
    "chili powder": "seasoning",
    "paprika": "seasoning",
    "mustard": "condiment",
    "mayo": "condiment",
    "ketchup": "condiment",
    "mushroom": "vegetable",
    "zucchini": "vegetable",
    "eggplant": "vegetable",
    "egg": "dairy",
    "spinach": "vegetable",
    "kale": "vegetable",
    "lettuce": "vegetable",
    "avocado": "fruit",
    "cucumber": "vegetable",
    "asparagus": "vegetable",
    "broccoli": "vegetable",
    "cauliflower": "vegetable",
    "corn": "vegetable",
    "black beans": "legume",
    "kidney beans": "legume",
    "chickpeas": "legume",
    "peas": "vegetable",
    "lentils": "legume",
    "quinoa": "legume",
    "barley": "starch",
    "walnuts": "legume",
    "almonds": "legume",
    "cashews": "legume",
    "peanuts": "legume",
    "pistachios": "legume",
    "sunflower seeds": "legume",
    "pumpkin seeds": "legume",
    "chia seeds": "legume",
    "flax seeds": "legume",
    "sesame seeds": "legume",
    "poppy seeds": "legume",
    "coconut": "fruit",
    "dates": "fruit",
    "raisins": "fruit",
    "cranberries": "fruit",
    "blueberries": "fruit",
    "strawberries": "fruit",
    "raspberries": "fruit",
    "blackberries": "fruit",
    "pear": "fruit",
    "orange": "fruit",
    "lemon": "fruit",
    "lime": "fruit",
    "grapefruit": "fruit",
    "kiwi": "fruit",
    "pineapple": "fruit",
    "apple": "fruit",
    "watermelon": "fruit",
    "melon": "fruit",
    "fig": "fruit",
    "pomegranate": "fruit",
    "yogurt": "dairy",
    "milk": "dairy",
    "brie": "cheese",
    "cheddar": "cheese",
    "mozzarella": "cheese",
    "parmesan": "cheese",
    "cream cheese": "cheese",
    "gouda": "cheese",
    "feta": "cheese",
    "goat cheese": "cheese",
    "cheese": "dairy",
    "ricotta": "cheese",
    "sour cream": "dairy",
    "cream": "dairy",
    "pine nuts": "legume",
    "strawberry": "fruit",
    "ham": "meat",
    "sausage": "meat",
    "pork": "meat",
    "hazelnut": "legume",
    "white chocolate": "sweet",
    "chocolate": "sweet",
    "berry": "fruit",
    "anchovies": "seafood",
    "oil": "oil",
    "marzipan": "legume",
    "apricot": "fruit",
    "olive": "fruit",
    "vegetable stock": "seasoning",
    "celery": "vegetable",
    "celeriac": "vegetable",
    "cocoa": "legume",
    "oat": "starch",
    "red wine": "alcohol",
    "chilli": "seasoning",
    "tabasco": "seasoning",
    "dill": "herb",
    "almond extract": "flavoring",
    "oyster sauce": "condiment",
    "leek": "vegetable",
    "noodle": "starch",
    "spaghetti": "starch",
    "prosecco": "alcohol",
    "ice": "other",
    "radish": "vegetable",
    "salmon": "seafood",
    "bay leaves": "herb",
    "cabbage": "vegetable",
    "whisky": "alcohol",
    "chive": "herb",
    "watercress": "vegetable",
    "capers": "vegetable",
    "sake": "alcohol",
    "vodka": "alcohol",
    "bourbon": "alcohol",
    "prawn": "seafood",
    "white wine": "alcohol",
    "plum": "fruit",
    "dulce de leche": "dairy",
    "nori": "seaweed",
    "seaweed": "vegetable",
    "currants": "fruit",
    "shallot": "vegetable",
    "yeast": "other",
    "wasabi": "seasoning",
    "lasagn": "starch",
    "saffron": "seasoning",
    "pecan": "legume",
    "raisin": "fruit",
    "couscous": "starch",
    "marmalade": "fruit",
    "masala": "seasoning",
    "syrup": "sweet",
    "mint": "herb",
    "seed": "legume",
    "artichoke": "vegetable",
    "crème fraîche": "dairy",
    "squid": "seafood",
    "parsnip": "vegetable",
    "pastry": "starch",
    "curry": "seasoning",
    "fruit": "fruit",
    "bay leaf": "herb",
    "almond": "legume",
    "bacon": "meat",
    "worcestershire": "condiment",
    "salad": "vegetable",
    "harissa": "condiment",
    "rosé wine": "alcohol",
    "custard": "dairy",
    "bean paste": "condiment",
    "black tea": "beverage",
    "green tea": "beverage",
    "matcha": "beverage",
    "cherry": "fruit",
    "pistachio": "legume",
    "tortilla": "starch",
    "cherries": "fruit",
    "penne": "starch",
    "port": "alcohol",
    "aubergine": "vegetable",
    "star anise": "seasoning",
    "cod": "seafood",
    "macaroni": "starch",
    "amarett": "legume",
    "mascarpone": "dairy",
    "bicarbonate": "other",
    "pesto": "condiment",
    "water": "other",
    "treacle": "sweet",
    "beansprout": "vegetable",
    "bean": "legume",
    "vanilla": "flavoring",
    "walnut": "legume",
    "hummus": "condiment",
    "meringue": "sweet",
    "gelatin": "other",
    "baguette": "starch",
    "kirsch": "alcohol",
    "tea": "beverage",
    "tofu": "legume",
    "sprinkle": "sweet",
    "madeira": "alcohol",
    "cardamom": "flavoring",
    "molass": "sweet",
    "turkey": "meat",
    "brandy": "alcohol",
    "grain": "starch",
    "pine nut": "legume",
    "beetroot": "vegetable",
    "fromage frais": "dairy",
    "caramel": "sweet",
    "rum": "alcohol",
    "sherry": "alcohol",
    "pea": "vegetable",
    "turmeric": "seasoning",
    "vermouth": "alcohol",
    "tahini": "legume",
    "wheat": "starch",
    "mussel": "seafood",
    "cavolo": "vegetable",
    "gorgonzola": "cheese",
    "miso": "condiment",
    "mange tout": "vegetable",
    "mangetout": "vegetable",
    "sage": "herb",
    "stilton": "cheese",
    "berries": "fruit",
    "whiskey": "alcohol",
    "chicory": "vegetable",
    "passata": "condiment",
    "rose petals": "flavoring",
    "rotis": "starch",
    "rhubarb": "fruit",
    "loaf": "starch",
    "bun": "starch",
    "tartar": "condiment",
    "hoisin": "condiment",
    "goose": "meat",
    "bok choy": "vegetable",
    "tarragon": "herb",
    "cider": "alcohol",
    "pancetta": "meat",
    "gherkin": "vegetable",
    "tagliatelle": "starch",
    "chestnut": "legume",
    "spring green": "vegetable",
    "brussels sprout": "vegetable",
    "barbecue sauce": "condiment",
    "cashew": "legume",
    "gnocchi": "starch",
    "shrimp": "seafood",
    "icing": "sweet",
    "vegetable bouillon": "seasoning",
    "tequila": "alcohol",
    "marshmallow": "sweet",
    "duck": "meat",
    "clementine": "fruit",
    "gin": "alcohol",
    "colouring": "other",
    "coloring": "other",
    "dye": "other",
    "halloumi": "cheese",
    "stock": "seasoning",
    "caper": "vegetable",
    "pudding": "sweet",
    "turnip": "vegetable",
    "courgette": "vegetable",
    "sumac": "seasoning",
    "date": "fruit",
    "seasoning": "seasoning",
    "tamarind": "seasoning",
    "batter": "other",
    "wrap": "starch",
    "waffle": "starch",
    "muffin": "starch",
    "agar": "other",
    "herb": "herb",
    "quail": "meat",
    "polenta": "starch",
    "prune": "fruit",
    "margarine": "dairy",
    "piri-piri": "seasoning",
    "lentil": "legume",
    "wrapper": "starch",
    "semolina": "starch",
    "gold": "other",
    "silver": "other",
    "sriracha": "condiment",
    "tamari": "condiment",
    "pigeon": "meat",
    "liqueur": "alcohol",
    "liquor": "alcohol",
    "yoghurt": "dairy",
    "mackerel": "seafood",
    "currant": "fruit",
    "coffee": "beverage",
    "hot sauce": "condiment",
    "taco shell": "starch",
    "pecorino": "cheese",
    "rocket": "vegetable",
    "arugula": "vegetable",
    "suet": "seasoning",
    "cleriac": "vegetable",
    "marsala": "alcohol",
    "quark": "dairy",
    "sauce": "condiment",
    "gruyère": "cheese",
    "mace": "seasoning",
    "espresso": "beverage",
    "scallop": "seafood",
    "camembert": "cheese",
    "quince": "fruit",
    "trout": "seafood",
    "anchovy": "seafood",
    "jalapeño": "vegetable",
    "glitter": "other",
    "grape": "fruit",
    "citric acid": "seasoning",
    "chapati": "seasoning",
    "okra": "vegetable",
    "tzatziki": "condiment",
    "vegetables": "vegetable",
    "chorizo": "meat",
    "granola": "starch",
    "pumpkin": "vegetable",
    "bass": "seafood",
    "chipotle": "condiment",
    "liver": "meat",
    "scallion": "vegetable",
    "wine": "alcohol",
    "relish": "condiment",
    "tilapia": "seafood",
    "mince": "meat",
    "crab": "seafood",
    "tuna": "seafood",
    "chili": "seasoning",
    "pico de gallo": "condiment",
    "jicama": "vegetable",
    "collard": "vegetable",
    "tongue": "meat",
    "malunggay": "vegetable",
    "clam": "seafood",
    "lobster": "seafood",
    "chayote": "vegetable",
    "pimiento": "vegetable",
    "sardine": "seafood",
    "mahi": "seafood",
    "taro": "vegetable",
    "bamboo": "vegetable",
    "amaranth": "starch",
    "pig heart": "meat",
    "cognac": "alcohol",
    "paneer": "cheese",
    "haddock": "seafood",
    "panko": "starch",
    "baking soda": "other",
    "agave": "sweet",
    "papaya": "fruit",
    "hotdog": "meat",
    "mirin": "alcohol",
    "gourd": "vegetable",
    "squash": "vegetable",
    "pig": "meat",
    "crust": "starch",
    "croûtons": "starch",
    "naan": "starch",
    "fondant": "sweet",
    "guacamole": "condiment",
    "tortellini": "starch",
    "ciabatta": "starch",
    "farfalle": "starch",
    "aquavit": "alcohol",
    "kipper": "seafood",
    "glycerine": "other",
    "sesame": "legume",
    "wood": "other",
    "prosciutto": "meat",
    "guinness": "alcohol",
    "sponge fingers": "starch",
    "ladyfingers": "starch",
    "clove": "seasoning",
    "cacao": "legume",
    "citrus": "fruit",
    "halibut": "seafood",
    "tonkatsu": "condiment",
    "katsuobushi": "seafood",
    "shoyu": "condiment",
    "konbu": "seafood",
    "broth": "seasoning",
    "pita": "starch",
    "chile": "vegetable",
    "sauerkraut": "vegetable",
    "bagel": "starch",
    "campari": "alcohol",
    "orgeat": "flavoring",
    "seltzer": "alcohol",
    "kimchi": "vegetable",
    "galangal": "seasoning",
    "soda": "beverage",
    "fillet": "meat",
    "leaves": "vegetable",
    "salsa": "condiment",
    "toffee": "sweet",
    "sultana": "fruit",
    "rabbit": "meat",
    "rutabaga": "vegetable",
    "bitters": "other",
    "pickle": "condiment",
    "marmite": "condiment",
    "malteser": "sweet",
    "malt": "other",
    "brioche": "starch",
    "cannabis": "other",
    "cola": "beverage"
}
    print(json.dumps(r))
    # Create destination list for ingredient recognition
    r["ings"]=[]
    ings_set = set()
    cats = set()
    r["mass"] = 0
    for ing_line in r["recipeIngredient"]:
        ing_line = ing_line.lower()
        for test_ing in ings:
            if test_ing in ing_line:
                ing = aliases[test_ing] if test_ing in aliases else test_ing
                print("Querying for", ing,end="... ")
                nutrition = conn.query(ing).to_dict()
                print("Done!")
                obj = {
                    "name": ing,
                    "amount":get_amount(ing_line),
                    "unit":get_unit(ing_line),
                    "nutrition":nutrition,
                    "category": cat_ings[ing]
                }
                obj["grams"]=to_grams(obj["category"],ing,obj["amount"],obj["unit"])
                r["mass"] += obj["grams"]
                r["ings"].append(obj)
                ings_set.add(ing)
                cats.add(obj["category"])
                break
    if "meat" in cats:
        r["diet"]="meat"
    elif "seafood" in cats:
        r["diet"]="seafood"
    else:
        r["diet"]="vegetarian"
    r["alcoholic"]="alcohol" in cats
    if isinstance(r["recipeYield"], list):
        r["yield"]=r["recipeYield"][0]
    else:
        r["yield"]=get_amount(r["recipeYield"])
    conn.save_compiled()
    return r

def get_unit(ing_line):
    aliases={
        "c.":"cup",
        "g.":"g",
        "gram":"g",
        "l.":"liter",
        "teaspoon":"tsp",
        "tablespoon":"tbsp",
        "pound":"lb"
    }
    for test_unit in ["tbsp", "tsp", "lb", "kg", "cup","c.", "g.","gram","liter","l."]:
        if test_unit in ing_line:
            return aliases[test_unit] if test_unit in aliases else test_unit
    return "unit"

def get_amount(ing_line):
    num_chars = "0123456789.,/- ½"
    substr_start = 0
    while substr_start < len(ing_line) and ing_line[substr_start] not in num_chars:
        substr_start+=1
        
    substr_end = substr_start+1
    while substr_end < len(ing_line) and ing_line[substr_end] in num_chars:
        substr_end+=1
    substr = ing_line[substr_start:substr_end].strip()
    if len(substr)==0:
        return 1 # Default to 1 unit
    
    if substr[-1]=="½":
        if len(substr)>1:
            return float(substr[:-1])+0.5
        return 0.5
    
    if "-" in substr:
        # Just return the center of the interval
        i = substr.index("-")
        a = float(substr[:i].strip())
        b = float(substr[i+1:].strip())
        return (a+b)/2
    
    if "/" in substr:
        i = substr.index("/")
        a = float(substr[:i])
        b = float(substr[i+1:])
        return a/b
    
    return float(substr)

def to_grams(ing_category, ing, amount, unit):
    if unit == "g": return amount
    if unit == "kg": return amount * 1e+3
    if unit == "lb": return amount * 453.6
    volume_of_units = {
        "tbsp": 0.0147868,  # 1 tablespoon = 0.0147868 liters
        "tsp": 0.00492892,  # 1 teaspoon = 0.00492892 liters
        "cup": 0.24,        # 1 cup = 0.24 liters
        "liter": 1          # 1 liter = 1 liter
    }
    mass_density = {
        'alcohol': 950,       # g/L, average density for common alcohols
        'beverage': 1000,     # g/L, average density for water-based beverages
        'cheese': 1050,       # g/L, average density for various cheeses
        'condiment': 1100,    # g/L, average density for sauces and condiments
        'dairy': 1030,        # g/L, average density for milk and cream-based products
        'flavoring': 900,     # g/L, average density for extracts and liquid flavorings
        'fruit': 600,         # g/L, average density for fruits
        'herb': 150,          # g/L, average density for fresh herbs
        'legume': 750,        # g/L, average density for beans, lentils, etc.
        'meat': 1080,         # g/L, average density for various meats
        'oil': 915,           # g/L, average density for common cooking oils
        'other': 800,         # g/L, catch-all category for miscellaneous items
        'seafood': 1080,      # g/L, average density for fish and shellfish
        'seasoning': 400,     # g/L, average density for dried seasonings and spices
        'seaweed': 110,       # g/L, average density for dried seaweed
        'starch': 800,        # g/L, average density for grains and pasta
        'sweet': 800,         # g/L, average density for sweets and confections
        'vegetable': 350      # g/L, average density for vegetables
    }
    mass_of_ingredients = {
        "sugar": 5,  # grams per teaspoon
        "butter": 15,  # grams per tablespoon
        "salt": 5,  # grams per teaspoon
        "garlic": 5,  # grams per clove
        "spring onion": 40,  # grams per bunch
        "red onion": 150,  # grams per medium onion
        "onion": 150,  # grams per medium onion
        "tomato sauce": 240,  # grams per cup
        "tomato": 150,  # grams per medium tomato
        "olive oil": 15,  # grams per tablespoon
        "soy sauce": 15,  # grams per tablespoon
        "vinegar": 15,  # grams per tablespoon
        "tortilla": 50,  # grams per tortilla
        "flour": 120,  # grams per cup
        "baking powder": 5,  # grams per teaspoon
        "banana": 120,  # grams per medium banana
        "peach": 150,  # grams per peach
        "mango": 200,  # grams per mango
        "bread": 30,  # grams per slice
        "vegetable stock": 240,  # grams per cup
        "stock": 240,  # grams per cup
        "chicken": 170,  # grams per chicken breast
        "lamb": 250,  # grams per lamb chop
        "fish": 150,  # grams per fillet
        "meat": 170,  # grams per piece
        "beef": 170,  # grams per piece
        "pasta": 60,  # grams per serving
        "rice": 180,  # grams per cup
        "potato": 200,  # grams per medium potato
        "carrot": 60,  # grams per carrot
        "cayenne": 1,  # grams per teaspoon
        "bell pepper": 150,  # grams per bell pepper
        "pepper": 2,  # grams per peppercorn
        "cilantro": 5,  # grams per tablespoon
        "parsley": 5,  # grams per tablespoon
        "rosemary": 2,  # grams per tablespoon
        "thyme": 2,  # grams per tablespoon
        "basil": 5,  # grams per tablespoon
        "oregano": 2,  # grams per tablespoon
        "cumin": 2,  # grams per tablespoon
        "coriander": 5,  # grams per tablespoon
        "ginger": 15,  # grams per tablespoon
        "cinnamon": 2,  # grams per tablespoon
        "nutmeg": 2,  # grams per tablespoon
        "cocoa powder": 5,  # grams per tablespoon
        "honey": 21,  # grams per tablespoon
        "maple syrup": 20,  # grams per tablespoon
        "vanilla extract": 15,  # grams per tablespoon
        "chili powder": 5,  # grams per tablespoon
        "paprika": 5,  # grams per tablespoon
        "mustard": 15,  # grams per tablespoon
        "mayo": 15,  # grams per tablespoon
        "ketchup": 15,  # grams per tablespoon
        "mushroom": 20,  # grams per cup
        "zucchini": 200,  # grams per zucchini
        "eggplant": 200,  # grams per eggplant
        "egg": 50,  # grams per egg
        "spinach": 30,  # grams per cup
        "kale": 67,  # grams per cup
        "lettuce": 50,  # grams per head
        "avocado": 200,  # grams per avocado
        "cucumber": 300,  # grams per cucumber
        "asparagus": 75,  # grams per bunch
        "broccoli": 150,  # grams per head
        "cauliflower": 400,  # grams per head
        # "corn": ,  # Not specified (depends on cob or kernels)
        "black beans": 240,  # grams per cup
        "kidney beans": 240,  # grams per cup
        "chickpeas": 240,  # grams per cup
        "peas": 160,  # grams per cup
        "lentils": 180,  # grams per cup
        "quinoa": 185,  # grams per cup
        "barley": 200,  # grams per cup
        "walnuts": 30,  # grams per ounce
        "almonds": 24,  # grams per ounce
        "cashew": 33,  # grams per ounce
        "peanuts": 28,  # grams per ounce
        "pistachio": 49,  # grams per ounce
        "sunflower seeds": 35,  # grams per ounce
        "pumpkin seeds": 33,  # grams per ounce
        "chia seeds": 28,  # grams per ounce
        "flax seeds": 28,  # grams per ounce
        "sesame seeds": 27,  # grams per ounce
        "poppy seeds": 24,  # grams per ounce
        "coconut": 45,  # grams per cup
        "dates": 24,  # grams per date
        "raisins": 30,  # grams per ounce
        "cranberries": 40,  # grams per cup
        "blueberries": 150,  # grams per cup
        "strawberries": 150,  # grams per cup
        "raspberries": 123,  # grams per cup
        "blackberries": 144,  # grams per cup
        "pear": 200,  # grams per pear
        "orange": 130,  # grams per orange
        "lemon": 58,  # grams per lemon
        "lime": 67,  # grams per lime
        "grapefruit": 230,  # grams per grapefruit
        "kiwi": 76,  # grams per kiwi
        "pineapple": 900,  # grams per pineapple
        "apple": 200,  # grams per apple
        "watermelon": 5000,  # grams per watermelon
        "melon": 5000,  # grams per melon
        "fig": 50,  # grams per fig
        "pomegranate": 250,  # grams per pomegranate
        "yogurt": 225,  # grams per cup
        "milk": 240,  # grams per cup
        # "brie": ,  # Not specified (depends on wedge)
        "cheddar": 30,  
        "mozzarella": 30,  
        "parmesan": 30,
        # "cream cheese": ,  # Not specified (depends on ounce)
        # "gouda": ,  # Not specified (depends on wedge)
        # "feta": ,  # Not specified (depends on ounce)
        # "goat cheese": ,  # Not specified (depends on ounce)
        "cheese": 30,
        # "ricotta": ,  # Not specified (depends on ounce)
        "sour cream": 30,
        # "cream": ,  # Not specified (depends on cup)
        "pine nuts": 30,  # grams per ounce
        "strawberry": 19, 
        # "ham": ,  # Not specified (depends on slice)
        "sausage": 220,
        # "pork": ,  # Not specified (depends on cut)
        "hazelnut": 20,  # grams per ounce
        "white chocolate": 28,  # grams per ounce
        "chocolate": 28,  # grams per ounce
        # "berry": ,  # Not specified (depends on type)
        "anchovies": 20,  # grams per can
        "oil": 15,  # grams per tablespoon
        "marzipan": 30,  # grams per ounce
        "apricot": 35,  # grams per apricot
        "olive": 4,  # grams per olive
        "celery": 40,  # grams per cup
        "celeriac": 400,  # grams per celeriac
        "cocoa": 5,  # grams per tablespoon
        "oat": 40,  # grams per 1/2 cup
        "red wine": 150,  # grams per glass
        "chilli": 20,  # grams per chilli
        "tabasco": 7,  # grams per teaspoon
        "dill": 3,  # grams per tablespoon
        "almond extract": 15,  # grams per tablespoon
        "oyster sauce": 15,  # grams per tablespoon
        "leek": 150,  # grams per leek
        "noodle": 55,  # grams per cup
        "spaghetti": 210,  # grams per serving
        "prosecco": 150,  # grams per glass
        "radish": 20,  # grams per cup
        "salmon": 170,  # grams per fillet
        "bay leaves": 1,  # grams per leaf
        
        "cabbage": 100,  # grams per cabbage
        "whisky": 40,  # grams per shot
        "chive": 3,  # grams per tablespoon
        "watercress": 25,  # grams per cup
        "capers": 4,  # grams per tablespoon
        "sake": 40,  # grams per shot
        "vodka": 40,  # grams per shot
        "bourbon": 40,  # grams per shot
        "prawn": 100,  # grams per prawn
        "white wine": 150,  # grams per glass
        "plum": 60,  # grams per plum
        "dulce de leche": 30,  # grams per tablespoon
        "nori": 3,  # grams per sheet
        "seaweed": 10,  # grams per cup
        "currants": 40,  # grams per cup
        "shallot": 20,  # grams per shallot
        "yeast": 8,  # grams per packet
        "wasabi": 5,  # grams per tablespoon
        "lasagn": 100,  # grams per serving
        "saffron": 0.5,  # grams per teaspoon
        "pecan": 20,  # grams per ounce
        "raisin": 30,  # grams per ounce
        "couscous": 60,  # grams per serving
        "marmalade": 30,  # grams per tablespoon
        "masala": 5,  # grams per tablespoon
        "syrup": 30,  # grams per tablespoon
        "mint": 5,  # grams per tablespoon
        "seed": 5,  # grams per tablespoon
        "artichoke": 100,  # grams per artichoke
        "crème fraîche": 15,  # grams per tablespoon
        "squid": 200,  # grams per squid
        "parsnip": 100,  # grams per parsnip
        "pastry": 50,  # grams per sheet
        "curry": 5,  # grams per tablespoon
        "fruit": 150,  # grams per cup
        "bay leaf": 1,  # grams per leaf
        "almond": 1,  # grams per almond
        "bacon": 20,  # grams per slice
        "pak choi": 150,  # grams per pak choi
        "worcestershire": 5,  # grams per tablespoon
        "salad": 100,  # grams per serving
        "harissa": 15,  # grams per tablespoon
        "rosé wine": 150,  # grams per glass
        "custard": 150,  # grams per serving
        "bean paste": 30,  # grams per tablespoon
        "black tea": 2,  # grams per teaspoon
        "green tea": 2,  # grams per teaspoon
        "matcha": 2,  # grams per teaspoon
        "cherry": 5,  # grams per cherry
        "cherries": 100,  # grams per cup
        "penne": 100,  # grams per serving
        "port": 150,  # grams per glass
        "aubergine": 200,  # grams per eggplant
        "star anise": 1,  # grams per star
        "cod": 150,  # grams per fillet
        "macaroni": 100,  # grams per serving
        "amarett": 5,  # grams per tablespoon
        "mascarpone": 30,  # grams per ounce
        "bicarbonate": 5,  # grams per tablespoon
        "pesto": 30,  # grams per tablespoon
        "water": 240,  # grams per cup
        "treacle": 30,  # grams per tablespoon
        "beansprout": 50,  # grams per cup
        "bean": 170,  # grams per cup
        "vanilla": 1,  # grams per vanilla bean
        "walnut": 20,  # grams per ounce
        "hummus": 30,  # grams per tablespoon
        "houmous": 30,  # grams per tablespoon
        "meringue": 30,  # grams per meringue
        "gelatin": 7,  # grams per tablespoon
        "baguette": 250,  # grams per baguette
        "kirsch": 30,  # grams per tablespoon
        "tea": 2,  # grams per teaspoon
        "tofu": 100,  # grams per serving
        "sprinkle": 5,  # grams per tablespoon
        "madeira": 150,  # grams per glass
        "cardamom": 2,  # grams per teaspoon
        "molass": 30,  # grams per tablespoon
        "turkey": 170,  # grams per turkey breast
        "brandy": 40,  # grams per shot
        "grain": 50,  # grams per cup
        "pine nut": 20,  # grams per ounce
        "beetroot": 150,  # grams per beetroot
        "fromage frais": 15,  # grams per tablespoon
        "caramel": 30,  # grams per tablespoon
        "rum": 40,  # grams per shot
        "sherry": 40,  # grams per glass
        "pea": 30,  # grams per cup
        "turmeric": 2,  # grams per teaspoon
        "vermouth": 150,  # grams per glass
        "tahini": 30,  # grams per tablespoon
        "wheat": 50,  # grams per cup
        "mussel": 20,  # grams per mussel
        "cavolo": 100,  # grams per cavolo nero
        "gorgonzola": 30,  # grams per ounce
        "miso": 30,  # grams per tablespoon
        "mange tout": 100,  # grams per serving
        "mangetout": 100,  # grams per serving
        "sage": 5,  # grams per tablespoon
        "stilton": 30,  # grams per ounce
        "berries": 100,  # grams per cup
        "whiskey": 40,  # grams per shot
        "chicory": 100,  # grams per chicory
        "passata": 240,  # grams per cup
        "rose petals": 1,  # grams per petal
        "rotis": 50,  # grams per roti
        "rhubarb": 150,  # grams per cup
        "loaf": 900,  # grams per loaf
        "bun": 100,  # grams per bun
        "tartar": 30,  # grams per tablespoon
        "hoisin": 30,  # grams per tablespoon
        "goose": 200,  # grams per goose
        "bok choy": 150,  # grams per bok choy
        "tarragon": 5,  # grams per tablespoon
        "cider": 240,  # grams per pint
        "pancetta": 20,  # grams per slice
        "gherkin": 10,  # grams per gherkin
        "tagliatelle": 100,  # grams per serving
        "chestnut": 50,  # grams per chestnut
        "spring green": 150,  # grams per serving
        "brussels sprout": 50,  # grams per brussels sprout
        "barbecue sauce": 30,  # grams per tablespoon
        "gnocchi": 100,  # grams per serving
        "shrimp": 100,  # grams per serving
        "icing": 30,  # grams per tablespoon
        "vegetable bouillon": 5,  # grams per cube
        "tequila": 40,  # grams per shot
        "marshmallow": 25,  # grams per marshmallow
        "duck": 170,  # grams per duck breast
        "clementine": 75,  # grams per clementine
        "gin": 40,  # grams per shot
        "colouring": 5,  # grams per teaspoon
        "coloring": 5,  # grams per teaspoon
        "dye": 5,  # grams per teaspoon
        "halloumi": 60,  # grams per slice
        "caper": 4,  # grams per tablespoon
        "pudding": 150,  # grams per serving
        "turnip": 150,  # grams per turnip
        "courgette": 200,  # grams per courgette
        "sumac": 2,  # grams per teaspoon
        "date": 20,  # grams per date
        "seasoning": 5,  # grams per tablespoon
        "tamarind": 20,  # grams per tablespoon
        "batter": 100,  # grams per serving
        "wrap": 60,  # grams per wrap
        "waffle": 100,  # grams per waffle
        "muffin": 100,  # grams per muffin
        "agar": 5,  # grams per tablespoon
        "herb": 5,  # grams per tablespoon
        "quail": 200,  # grams per quail
        "polenta": 250,  # grams per serving
        "prune": 30,  # grams per prune
        "margarine": 15,  # grams per tablespoon
        "piri-piri": 30,  # grams per tablespoon
        "lentil": 200,  # grams per cup
        "wrapper": 20,  # grams per wrapper
        "semolina": 120,  # grams per cup
        "gold": 1,  # grams per piece
        "silver": 1,  # grams per piece
        "sriracha": 15,  # grams per tablespoon
        "tamari": 15,  # grams per tablespoon
        "pigeon": 300,  # grams per pigeon
        "liqueur": 40,  # grams per shot
        "liquor": 40,  # grams per shot
        "yoghurt": 240,  # grams per cup
        "mackerel": 150,  # grams per fillet
        "currant": 40,  # grams per cup
        "coffee": 10,  # grams per tablespoon
        "hot sauce": 15,  # grams per tablespoon
        "taco shell": 50,  # grams per shell
        "pecorino": 30,  # grams per ounce
        "rocket": 25,  # grams per cup
        "arugula": 25,  # grams per cup
        "suet": 100,  # grams per serving
        "cleriac": 400,  # grams per celeriac
        "marsala": 150,  # grams per glass
        "quark": 250,  # grams per cup
        "sauce": 30,  # grams per tablespoon
        "gruyère": 30,  # grams per ounce
        "mace": 2,  # grams per teaspoon
        "espresso": 30,  # grams per shot
        "scallop": 50,  # grams per scallop
        "camembert": 30,  # grams per ounce
        "quince": 100,  # grams per quince
        "trout": 150,  # grams per fillet
        "anchovy": 20,  # grams per can
        "jalapeño": 15,  # grams per jalapeño
        "glitter": 5,  # grams per teaspoon
        "grape": 5,  # grams per grape
        "citric acid": 5,  # grams per teaspoon
        "chapati": 100,  # grams per chapati
        "okra": 30,  # grams per cup
        "tzatziki": 30,  # grams per tablespoon
        "vegetables": 150,  # grams per serving
        "chorizo": 50,  # grams per serving
        "granola": 50,  # grams per serving
        "pumpkin": 500,  # grams per pumpkin
        "bass": 150,  # grams per fillet
        "chipotle": 20,  # grams per pepper
        "liver": 150,  # grams per liver
        "scallion": 15,  # grams per scallion
        "wine": 150,  # grams per glass
        "relish": 30,  # grams per tablespoon
        "tilapia": 150,  # grams per fillet
        "mince": 100,  # grams per serving
        "crab": 100,  # grams per serving
        "tuna": 100,  # grams per serving
        "chili": 15,  # grams per tablespoon
        "pico de gallo": 15,  # grams per tablespoon
        "jicama": 150,  # grams per jicama
        "collard": 100,  # grams per serving
        "tongue": 150,  # grams per serving
        "malunggay": 50,  # grams per cup
        "clam": 20,  # grams per clam
        "lobster": 200,  # grams per lobster
        "chayote": 200,  # grams per chayote
        "pimiento": 30,  # grams per pimiento
        "sardine": 90,  # grams per can
        "mahi": 150,  # grams per fillet
        "taro": 150,  # grams per taro
        "bamboo": 150,  # grams per bamboo shoot
        "amaranth": 200,  # grams per cup
        "pig heart": 200,  # grams per pig heart
        "cognac": 40,  # grams per shot
        "paneer": 100,  # grams per serving
        "haddock": 150,  # grams per fillet
        "panko": 30,  # grams per cup
        "baking soda": 5,  # grams per tablespoon
        "agave": 30,  # grams per tablespoon
        "papaya": 200,  # grams per papaya
        "hotdog": 100,  # grams per hotdog
        "mirin": 40,  # grams per tablespoon
        "gourd": 200,  # grams per gourd
        "squash": 500,  # grams per squash
        "pig": 1000,  # grams per pig
        "crust": 100,  # grams per serving
        "croûtons": 15,  # grams per serving
        "naan": 100,  # grams per naan
        "fondant": 30,  # grams per tablespoon
        "guacamole": 30,  # grams per tablespoon
        "tortellini": 100,  # grams per serving
        "ciabatta": 100,  # grams per loaf
        "farfalle": 100,  # grams per serving
        "aquavit": 40,  # grams per shot
        "kipper": 100,  # grams per serving
        "glycerine": 30,  # grams per tablespoon
        "sesame": 5,  # grams per tablespoon
        "wood": 1000,  # grams per log
        "prosciutto": 30,  # grams per slice
        "guinness": 400,  # grams per pint
        "sponge fingers": 10,  # grams per finger
        "ladyfingers": 10,  # grams per finger
        "clove": 1,  # grams per clove
        "cacao": 5,  # grams per tablespoon
        "citrus": 200,  # grams per fruit
        "halibut": 150,  # grams per fillet
        "tonkatsu": 100,  # grams per serving
        "katsuobushi": 5,  # grams per tablespoon
        "konbu": 10,  # grams per piece
        "broth": 240,  # grams per cup
        "pita": 60,  # grams per pita
        "chile": 5,  # grams per teaspoon
        "sauerkraut": 150,  # grams per serving
        "bagel": 100,  # grams per bagel
        "campari": 40,  # grams per shot
        "orgeat": 30,  # grams per tablespoon
        "seltzer": 240,  # grams per cup
        "kimchi": 150,  # grams per serving
        "galangal": 30,  # grams per tablespoon
        "soda": 240,  # grams per can
        "fillet": 150,  # grams per serving
        "leaves": 5,  # grams per leaf
        "salsa": 30,  # grams per tablespoon
        "toffee": 30,  # grams per tablespoon
        "sultana": 30,  # grams per cup
        "rabbit": 1000,  # grams per rabbit
        "rutabaga": 200,  # grams per rutabaga
        "bitters": 5,  # grams per teaspoon
        "pickle": 30,  # grams per tablespoon
        "marmite": 30,  # grams per tablespoon
        "malteser": 10,  # grams per malteser
        "malt": 30,  # grams per tablespoon
        "brioche": 100,  # grams per serving
        "cannabis": 1,  # grams per joint
        "cola": 240,  # grams per can
        "ice": 30,  # grams per cube
    }
    if unit == "unit":
        return amount * mass_of_ingredients[ing] # Liters
    volume = amount * volume_of_units[unit] # Liters
    return volume * mass_density[ing_category] # L * g/L = grams
