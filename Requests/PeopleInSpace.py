import pip._vendor.requests as req

response = req.get('http://api.open-notify.org/astros.json')
json = response.json()

astronauts = json['people']

for astronaut in astronauts:
    print(astronaut['name'], 'in', astronaut['craft'])