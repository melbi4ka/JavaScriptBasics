class Town:

    def __init__(self, name: str):
        self.name = name
        self.latitude = ""
        self.longitude = ""

    def set_latitude(self, latitude):
        self.latitude = "".join(latitude)

    def set_longitude(self, longitude):
        self.longitude = "".join(longitude)

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)

# Town: Sofia | Latitude: 42° 41' 51.04" N | Longitude: 23° 19' 26.94" E