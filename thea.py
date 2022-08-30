import requests
from pprint import pprint

edamam_app_key = 'b4bd766ee7762ee33c6758532257181c'

edamam_app_id = '753f0d79'

print('Dish types are:  biscuits and cookies. Bread. Cereals. Condiments and sauces.')
print('Desserts. Drinks. Main course.  Pancake.  Preps.  Preserve.')
print('Salad. Sandwiches.  Side dish.  Soup.  Starter.  Sweets')

dish_type = input('What type of dish are you cooking today?')

def one_dietary_restriction():
  results = requests.get(
    'https://api.edamam.com/search?q={}&app_id={}&app_key={}&health={}&excluded={}&dishType={}'.format(user_ingredient1, edamam_app_id, edamam_app_key, user_health_concern, user_aversion, dish_type))

  data = results.json()


  if data['count'] == 0:
      print('Unfortunately your search returned no recipes.  Please check spelling and try again. Check that {} is a dish type listed in Edamame.'.format(dish_type))
  else:

        print('We found {} {} {} recipes without {} that use {}.'.format((data['count']), user_health_concern, dish_type, user_aversion, user_ingredient1))

        print('See below for the top 10 results:')

        recipe_hits = (data['hits'])


        for each_recipe in recipe_hits:
            recipe = each_recipe['recipe']
            pprint(recipe['label'])
            print(recipe['shareAs'])
        print('For more info, click here:')
        print( 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(user_ingredient1, edamam_app_id, edamam_app_key))


def two_dietary_restrictions():
    results = requests.get(
      'https://api.edamam.com/search?q={}&app_id={}&app_key={}&health={}&health={}&excluded={}&dishType={}'.format(user_ingredient1, edamam_app_id,
                                                                                 edamam_app_key, user_health_concern, further_restrictions, user_aversion, dish_type))

    data = results.json()

    if data['count'] == 0:
        print(
            'Unfortunately your search returned no recipes.  Please check spelling and try again. Check that {} is a dish type listed in Edamame.'.format(
                dish_type))
    else:

        print('We found {} {}, {} recipes without {} that use {}.'.format((data['count']), user_health_concern,
                                                                      further_restrictions, user_aversion,
                                                                      user_ingredient1, dish_type))

        print('See below for the top 10 results:')

    recipe_hits = (data['hits'])

    for each_recipe in recipe_hits:
      recipe = each_recipe['recipe']
      print(recipe['label'])
      print(recipe['shareAs'])

    print('For more info, see:')
    print(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(user_ingredient1, edamam_app_id,
                                                                         edamam_app_key))


user_ingredient1 = input("what is your first ingredient?")
user_aversion = input("which ingredient are you avoiding?")
user_health_concern = input('what is your dietary restriction?')

further_restrictions = input('Do you have a further dietary restriction? If so, what is it?')

if further_restrictions == 'no':
    try:
        one_dietary_restriction()
    except TypeError:
        print('{} is not a recognised dietary restriction in Edamame.  Check spelling and try running the search again.'.format(user_health_concern))

else:
    try:
        two_dietary_restrictions()
    except TypeError:
        print('Either {} or {} is not a recognised dietary restriction in Edamame.  Check spelling and try running the search again.'.format(user_health_concern, further_restrictions))








