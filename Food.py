import requests

def get_random_meal():
    r = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
    j = r.json()
    dish = dict(j['meals'][0])


    name = dish['strMeal']
    dishType = dish['strCategory']
    geoLocation = dish['strArea']
    instructions = dish['strInstructions']
    imageUrl = dish['strMealThumb']
    videoUrl = dish['strYoutube']
    ingredients = [{dish[f'strIngredient{i}']:dish[f'strMeasure{i}']}
               for i in range(1, 21) if dish[f'strIngredient{i}'] != ""]
    source = dish['strSource']
    meal = dict(name=name, dishType=dishType, geoLocation=geoLocation, ingredients=ingredients, instructions=instructions, imageUrl=imageUrl, videoUrl=videoUrl, source=source)
    return meal
