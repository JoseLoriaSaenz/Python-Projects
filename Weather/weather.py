temperature = int(input("Tell me the temperature: "))

if temperature > 80:
    print("It's too hot!")
elif temperature < 60:
    print("It's too cold!")


if temperature > 80 or temperature < 60:
    print("Stay inside!")
elif temperature < 80:
    print("Enjoy the outdoors!")
