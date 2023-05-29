
import requests

api_key = "API_Yandex_Maps"
query = "Магазин"
region = "37.618754,55.751283"

x = requests.get(f"https://search-maps.yandex.ru/v1/?text={query}&type=biz&ll={region}&lang=ru_RU&apikey={api_key}").json()
for i in x["features"]:
    print(i)

