animals = input().split(", ")

if "wolf" in animals:
    if "wolf" == animals[-1]:
        print("Please go away and stop eating my sheep")
    else:
        index_wolf = animals.index("wolf")
        count_sheep = abs(index_wolf+1 - (len(animals)))
        print(f"Oi! Sheep number {count_sheep}! You are about to be eaten by a wolf!")
