class Submarine:
    def __init__(self):
        self.heigth = 0
        self.latitude = 0
        self.longitude = 0
        self.direction = 'NORTE'
    
    def __str__(self) -> None:
        return f'\n\n({self.latitude}, {self.longitude}, {self.heigth}, {self.direction})'

    def update_direction(self, command: str) -> None:
        if (self.direction == 'NORTE' and command == 'L') or (self.direction == 'SUL' and command == 'R'):
            self.direction = 'OESTE'
        elif (self.direction == 'SUL' and command == 'L') or (self.direction == 'NORTE' and command == 'R'):
            self.direction = 'LESTE'
        elif (self.direction == 'LESTE' and command == 'R') or (self.direction == 'OESTE' and command == 'L'):
            self.direction = 'SUL'
        elif (self.direction == 'OESTE' and command == 'R') or (self.direction == 'LESTE' and command == 'L'):
            self.direction = 'NORTE'
        else:
            raise ValueError('Invalid command.')

    @property
    def heigth(self) -> int:
        return self.__heigth
    
    @property
    def latitude(self) -> int:
        return self.__latitude

    @property
    def longitude(self) -> int:
        return self.__longitude
    
    @property
    def direction(self) -> str:
        return self.__direction

    @heigth.setter
    def heigth(self, heigth: int) -> None:
        self.__heigth = heigth
    
    @latitude.setter
    def latitude(self, latitude: int) -> None:
        self.__latitude = latitude
    
    @longitude.setter
    def longitude(self, longitude: int) -> None:
        self.__longitude = longitude
    
    @direction.setter
    def direction(self, direction: str) -> None:
        self.__direction = direction
