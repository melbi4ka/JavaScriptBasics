countries = input().split(", ")
capitals = input().split(", ")
countries_dict = dict(zip(countries, capitals))

countries_for_print = {print(f"{country} -> {capital}") for country, capital in countries_dict.items()}




