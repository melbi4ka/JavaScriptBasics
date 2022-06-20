class Town:
    latitude = ""
    longitude = ""

    def __init__(self, name: str):
        self.name = name

    def set_latitude(self, latitude):
        Town.latitude = "".join(latitude)

    def set_longitude(self, longitude):
        Town.longitude = "".join(longitude)

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {Town.latitude} | Longitude: {Town.longitude}"


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)

