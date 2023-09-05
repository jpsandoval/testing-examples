from datetime import date
# clases copy from internet


class WrongPinException(Exception):
    pass


class DebtNotAllowed(Exception):
    pass


class QuickSort:
    def sort(array):
        """ Método que ejecuta quicksort sobre un array """
        print("sorting")


class Client:
    def __init__(self, pesel, surname, firstName, expiryDate, plec, birthDate, address):
        if len(pesel) == 11:  # Tiene que ser de 11 digitos
            self.pesel = pesel  # Número nacional de polonia
            self.surname = surname
            self.plec = plec  # Genero
            self.firstName = firstName
            self.expiryDate = expiryDate
            self.birthDate = birthDate
            self.address = address
        else:
            print("Niepoprawny pesel")  # PESEL incorrecto
            print("\n")

    def surname_change(self, new_surname):
        """ Cambia el surname """
        self.surname = new_surname

    def print_data(self):
        """ Imprime todos los datos """
        print("Imie: "+self.firstName)
        print("Nazwisko: " + self.surname)
        print("PESEL: " + self.pesel)
        print("Data waznosci: " + self.expiryDate)
        print("Plec: " + self.plec)
        print("Data urodzenia: " + self.birthDate)
        print("Adres: " + self.address)

    def expiry_check(self):
        print("Dzisiaj jest " + str(date.today()) + ", a dowód wygasa " + self.expiryDate)


class Address:
    def __init__(self, street, houseNumber, city, postalCode):
        self.__street = street
        self.__houseNumber = houseNumber
        self.__city = city
        self.__postalCode = postalCode

    @property
    def street(self):
        return self.__street
    
    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def houseNumber(self):
        return self.__houseNumber
    
    @houseNumber.setter
    def houseNumber(self,value):
        self.__houseNumber = value

    @property
    def city(self):
        return self.__city
    
    @city.setter
    def city(self, value):
        self.__city = value
        print("Value has been set")
    
    @property
    def postalCode(self):
        return self.__postalCode

    @postalCode.setter
    def postalCode(self, value):
        self.__postalCode = value


class Account:
    def __init__(self, client, address, pin):
        if len(pin) == 4 and pin.isnumeric():
            self.client = client
            self.address = address
            self.pin = pin
            self.saldo = 0
        else:
            raise WrongPinException

    def CheckPin(self, pin):
        if pin != self.pin:
            raise WrongPinException

    def CheckIfWithdrawalPossible(self, amount):
        if amount > self.saldo:
            raise DebtNotAllowed

    def deposit(self, amount, pin):
        self.CheckPin(pin)
        self.saldo += amount

    def withdrawal(self, amount, pin):
        self.CheckPin(pin)
        self.CheckIfWithdrawalPossible(amount)
        self.saldo -= amount
    
    def accountStatus(self, pin):
        self.CheckPin(pin)
        print(self.saldo)
        print(self.client.print_data())


class OutOffPowerError(Exception):
    def __str__(self):
        return "Out off power"


class Robot:
    def __init__(self, name, start=(0, 0), power=9, board_dim=8):
        self.name = name
        self.start = start
        self.board_dim = board_dim
        self.power = power
        self.place = list(start)

    @property
    def name(self):
        
        return self.__dict__['name']

    @name.setter
    def name(self, value):
        if type(value) != str:
            raise TypeError("Name must be string type.")
        self.__dict__['name'] = value

    @property
    def start(self):
        return self.__dict__['start']

    @start.setter
    def start(self, value):
        if type(value) not in (list, tuple) or len(value) != 2:
            raise TypeError("Place must be 2 elements list.")
        self.__dict__['start'] = value

    @property
    def board_dim(self):
        return self.__dict__['board_dim']

    @board_dim.setter
    def board_dim(self, value):
        if type(value) != int or value <= 0:
            raise TypeError("Board dimention must be positive integer type.")
        self.__dict__['board_dim'] = value

    @property
    def place(self):
        return self.__dict__['place']

    @place.setter
    def place(self, value):
        if type(value) not in (list, tuple) or len(value) != 2:
            raise TypeError("Place must be 2 elements list.")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("Place values should be int")
        self.__dict__['place'] = value
        self.__dict__['place'][0] = self.__dict__['place'][0] % self.board_dim
        self.__dict__['place'][1] = self.__dict__['place'][1] % self.board_dim

    @property
    def power(self):
        return self.__dict__['power']

    @power.setter
    def power(self, value):
        if type(value) != int:
            raise TypeError("Power must be integer type.")
        self.__dict__['power'] = value

    def __move(self, vector, value):
        if type(value) != int:
            raise TypeError("You can only move with integer intervals.")
        try:
            self.Check_power()
            new_position = [self.place[0] +
                            vector[0], self.place[1] + vector[1]]
            self.place = new_position
            self.power = self.power - abs(value)

            if self.place[0] == 0:  # jeśli pierwszy wiersz
                self.power = self.power + 5
        except OutOffPowerError as e:
            print(e)

    def up(self, value):
        self.__move([-value, 0], value)

    def left(self, value):
        self.__move([0, -value], value)

    def __str__(self):
        return f"Name:{self.name},\nPlace: {self.place},\nPower: {self.power}"

    def __repr__(self):
        return f"{self.name}, {self.place}, {self.power}"

    def Check_power(self):
        if self.power <= 0:
            raise OutOffPowerError
