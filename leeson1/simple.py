city= {"city": "Москва", "temperature": "20"}
print(city["city"])
city["temperature"]= int(city["temperature"]) - 5
print(city)
print(city.get('country'))
city['country']='Россия'
print(city)
city['data']="27.05.2019"
print(city)
print(len(city))
print(a=city["temperature"])