import random

def Ws():
    weather=["Sunny", "Cloudy", "Rainy", "Windy", "Stormy", "Foggy"]
    wc=random.choice(weather)
    temp=random.randint(20,40)
    print(f"Weather : {wc} ,Temp : {temp}*C")
Ws()