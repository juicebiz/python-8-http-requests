import requests
API_TOKEN = '2619421814940190'

def get_hero_by_name(name: str):
    url = f'https://superheroapi.com/api/{API_TOKEN}/search/{name}'
    response = requests.get(url)
    json = response.json()
    if(json['response'] == 'success'):
        for hero in json['results']:
            if(hero['name'] == name):
                return hero
    else:
        return 'Ошибка'

def who_is_smartest():
    heroes = ('Thanos', 'Hulk', 'Captain America')
    max_intelligence = 0
    smartest_hero = ''
    for hero in heroes:
        result_hero = get_hero_by_name(hero)
        intelligence = int(result_hero['powerstats']['intelligence'])
        if(intelligence > max_intelligence):
            smartest_hero = hero
            max_intelligence = intelligence
    print(f"Самый умный герой - {smartest_hero}")

who_is_smartest()
