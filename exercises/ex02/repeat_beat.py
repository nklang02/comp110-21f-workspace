"""Repeating a beat in a loop."""

__author__ = "730418254"


# Begin your solution here...
beat: str = (input("What beat do you want to repeat? "))
maximum: int = int(input("How many times do you want to repeat it? "))
i: int = 0
while i < maximum:
    print((beat + " ") * (maximum - 1) + beat)
    i = i + maximum + maximum
if maximum <= 0:
    print("No beat...")
    maximum = (maximum + 1) ** 2

            

        
        
    

