from Planet import Planet

print("search a planet in our solar system (dont capitalize, also search exit to stop)")
x = 0
search = ""
earth = Planet("5.9 x 10^24","9.8 m/s^2", 365)
saturn = Planet("5.68 x 10^26","10.44 m/s^2",1058)
mars = Planet("6.4 x 10^23","3.711 m/s^2", 687)
pluto = Planet("1.3 x 10^22","0.62 m/s^2", 90600)
neptune = Planet("1.024 x 10^26","1.024 m/s^2", 60200)
jupiter = Planet("1.9 x 10^27","24.79 m/s^2", 4300)
mercury = Planet("3.3 x 10^23","3.7 m/s^2", 88)
venus = Planet("4.87 x 10^24","8.87 m/s^2", 225)
uranus = Planet("8.6 x 10^24","8.87 m/s^2", 31000)

while x == 0:
    search = input()
    if search == "earth":
        print(str(earth))
    elif search == "saturn":
        print(str(saturn))
    elif search == "mars":
        print(str(mars))
    elif search == "pluto":
        print(str(pluto))
    elif search == "neptune":
        print(str(neptune))
    elif search == "jupiter":
         print(str(jupiter))
    elif search == "mercury":
        print(str(mercury))
    elif search == "venus":
        print(str(venus))
    elif search == "exit":
        x = 1
    elif search == "your mom":
        print("should be lol")
    else:
        print("planet not found")
