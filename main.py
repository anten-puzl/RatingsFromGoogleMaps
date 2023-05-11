import requests
import configparser
import os


def read_config():
    config = configparser.ConfigParser()
    if os.path.exists('config.ini'):
        config.read('config.ini')
        API_KEY = config['DEFAULT']['api_key']
    return {'API_KEY': API_KEY}

param = read_config()
API_KEY = param.get('API_KEY')

print(API_KEY)
exit()

museums = [
    "Muzeum Pałacu Króla Jana III w Wilanowie, ul. Stanisława Kostki Potockiego 10/16",
    "Muzeum Historii Żydów Polskich POLIN, ul. Mordechaja Anielewicza 6",
    "Muzeum Warszawy, Rynek Starego Miasta 28/42",
    "Centrum Interpretacji Zabytków, ul. Brzozowa 11/13",
    "Muzeum Warszawskiej Pragi, ul. Targowa 50/52",
    "Fotoplastikon Warszawski, Al. Jerozolimskie 51",  # Временно закрыт
    "Centrum Sztuki Współczesnej Zamek Ujazdowski, ul. Jazdów 2",
    "Państwowe Muzeum Etnograficzne, ul. Kredytowa 1",
    "Muzeum X Pawilonu Cytadeli Warszawskiej, ul. Skazańców 25",
    "Muzeum Wojska Polskiego, Al. Jerozolimskie 3",
    "Zachęta Narodowa Galeria Sztuki, pl. Małachowskiego 3",
    "Muzeum Rzeźby im. Xawerego Dunikowskiego, Puławska 113a",
    "Muzeum Legii Warszawa, ul. Łazienkowska 3",
    "Muzeum Katyńskie, ul. Jana Jeziorańskiego 4",
    "Centrum Pieniądza NBP, ul. Świętokrzyska 11/21",
    "Muzeum Jana Pawła II i Prymasa Wyszyńskiego",
    "Muzeum Ordynariatu Polowego",
    "Dom Spotkań z Historią, ul. Karowa 20",
    "Muzeum Geologiczne, ul. Rakowiecka 4",
    "Muzeum Azji i Pacyfiku, Solec 24",
    "Muzeum Farmacji, Piwna 31/33",
    "Muzeum Polskiej Techniki Wojskowej, Powsińska 13",
    "Muzeum Więzienia Pawiak, ul. Dzielna 24/26",
    "Muzeum Niepodległości, aleja 'Solidarności' 62",
    "Mauzoleum Walki i Męczeństwa, aleja Jana Chrystiana Szucha 25",
    "Muzeum Drukarstwa, Ząbkowska 23/25",
    "Muzeum Woli, Srebrna 12",
    "Centrum Sztuki Współczesnej Zamek Ujazdowski",
    "Centrum Sztuki Współczesnej Zamek Ujazdowski"
]


def get_place_rating(place):
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        "key": API_KEY,
        "input": place,
        "inputtype": "textquery",
        "fields": "rating"
    }
    response = requests.get(url, params=params)
    data = response.json()
    rating = data["candidates"][0]["rating"] if "rating" in data["candidates"][0] else None
    return rating

# Получить рейтинг каждого музея
museums_with_ratings = []
for museum in museums:
    rating = get_place_rating(museum)
    museums_with_ratings.append((museum, rating))

# Отсортировать список музеев по возрастанию рейтинга
sorted_museums = sorted(museums_with_ratings, key=lambda x: x[1])

# Вывести отсортированный список с рейтингами
for museum, rating in sorted_museums:
    print(f"{museum} - Рейтинг: {rating}")
