import requests
from pprint import pprint

edamam_app_key = 'b4bd766ee7762ee33c6758532257181c'

edamam_app_id = '753f0d79'


def one_dietary_restriction():
  results = requests.get(
    'https://api.edamam.com/search?q={}&app_id={}&app_key={}&health={}&excluded={}'.format(user_ingredient1, edamam_app_id, edamam_app_key, user_health_concern, user_aversion))

  data = results.json()

  print( 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(user_ingredient1, edamam_app_id, edamam_app_key))

  print('We found {} {} recipes without {} that use {}.'.format((data['count']), user_health_concern, user_aversion, user_ingredient1))

  print('See below for the top 10 results:')

  recipe_hits = (data['hits'])

  for each_recipe in recipe_hits:
    recipe = each_recipe['recipe']
    print(recipe['label'])
    print(recipe['shareAs'])


def two_dietary_restrictions():
    results = requests.get(
      'https://api.edamam.com/search?q={}&app_id={}&app_key={}&health={}&health={}&excluded={}'.format(user_ingredient1, edamam_app_id,
                                                                                 edamam_app_key, user_health_concern, user_health_concern2, user_aversion))

    data = results.json()

    print(
      'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(user_ingredient1, edamam_app_id, edamam_app_key))


    print('We found {} {}, {} recipes without {} that use {}.'.format((data['count']), user_health_concern, user_health_concern2, user_aversion, user_ingredient1))

    print('See below for the top 10 results:')

    recipe_hits = (data['hits'])

    for each_recipe in recipe_hits:
      recipe = each_recipe['recipe']
      print(recipe['label'])
      print(recipe['shareAs'])


user_ingredient1 = input("what is your first ingredient?")
user_aversion = input("which ingredient are you avoiding?")
user_health_concern = input('what is your dietary restriction?')

further_restrictions = input('Do you have further dietary restrictions?')

if further_restrictions == 'no':
  one_dietary_restriction()


elif further_restrictions == 'yes':
  user_health_concern2 = input('what other restriction do you have?')
  two_dietary_restrictions()








