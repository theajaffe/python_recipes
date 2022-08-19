import requests

def recipe_search(ingredient):

  edamam_app_key = 'b4bd766ee7762ee33c6758532257181c'

  edamam_app_id = '753f0d79'

  user_ingredient1 = input("what is your first ingredient?")

  results = requests.get(
    'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(user_ingredient1, edamam_app_id, edamam_app_key))


  data = results.json()

  return data[hits]

  def run():
    ingredient = user_ingredient1
    results = data(ingredient)

    for result in results:
      recipe = result['recipe']
      print(recipe['label'])
      print(recipe['uri'])













