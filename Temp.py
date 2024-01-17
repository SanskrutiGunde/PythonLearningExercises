from urllib.request import urlopen

def get_condition(city):
    url = "http://wttr.in/" + city + "?format=%C"
    page = urlopen(url)
    raw = page.read()
    condition = raw.decode("utf-8")
    return condition

city = input("City: ")
condition = get_condition(city)
if condition == "Clear":
    print("🌞 No umbrella ☂️ needed")
else:
    print("⛈️ Umbrella ☔ needed")