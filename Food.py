import sys
import requests

# this doesn't need to be a whole class but it's here in case I want to expand its capabilities

# returns a meal dict from themealdb
def get_random_meal():
    r = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
    if not r.status_code == 200:
        print(f"Error: could not get random meal from TheMealDB, code {r.status_code}")
        sys.exit(1)

    j = r.json()
    dish = dict(j['meals'][0])

    name = dish['strMeal']
    dishType = dish['strCategory']
    geoLocation = dish['strArea']
    imageUrl = dish['strMealThumb']
    videoUrl = dish['strYoutube']
    source = dish['strSource']
    meal = dict(name=name, dishType=dishType, geoLocation=geoLocation, imageUrl=imageUrl, videoUrl=videoUrl, source=source)
    return meal
