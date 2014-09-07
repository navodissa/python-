__author__ = 'navodissa'


class Flight:
    age = 20

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))

        if not (number[2:].isdigit() and 9999 >= int(number[2:]) >= 1000):
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seat_arragment()
        self._seating = [{letter: None for letter in seats} for _ in rows]

        print("Parent instructor")

    def _parse_seat(self, seat):
        """ Parse a seat designator into a valid row and letter.

        Args:
            Seat: A seat designator such as 12F

        Returns:
            A tuple containing an integer and a string for row and seat.
        """
        row_numbers, seat_letters = self._aircraft.seat_arragment()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))
        if len(seat) != 3:
            print("Please type a valid length")
        else:
            row_text = seat[:2]
            try:
                row = int(row_text)
            except ValueError:
                raise ValueError("Invalid seat row {}".format(row_text))

            if row not in row_numbers:
                raise ValueError("Invalid row number {}".format(row))

            return row, letter

    def allocate_seat(self, seat, passenger):
        """ Allocate a seat to a passenger.

        :type self: object
        Args:
            Seat: A seat designator such as '12C or '21F.
            Passenger: The passenger name.

        Raises:
            ValueError: If the seat is unavilable.
        '"""
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} is already occupied.".format(seat))

        self._seating[row][letter] = passenger


    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())


    def _passenger_seats(self):
        """ An iterable series of passenger seating allocation."""
        row_numbers, seat_letters = self._aircraft.seat_arragment()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}:{}".format(row, letter))


def relocate_passenger(self, from_seat, to_seat):
    """ Relocate a passenger to a different seat.

        Args:
            from_seat: The existing seat designator for the passenger to be moved.

            to_seat: The new seat designator.
        """

    from_row, from_letter = self._parse_seat(from_seat)
    if self._seating[from_row][from_letter] is None:
        raise ValueError("No passenger to relocate in seat {}".format(from_seat))

    to_row, to_letter = self._parse_seat(to_seat)
    if self._seating[to_row][to_letter] is not None:
        raise ValueError("Seat {} already occupied".format(to_seat))

    self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
    self._seating[from_row][from_letter] = None


def numbers(self):
    return self._number


__doc__ = "Any doc"


def dates(self):
    print("Parent Method", Flight.age)


class Child(Flight):
    # def __init__(self):
    # print("Child instructor")

    def child_method(self):
        print("Child Method")

    def dates(self):
        print("Child Method", Flight.age)


class Aircraft():
    def __init__(self, name, model, rows, seat_per_row):
        self._name = name
        self._model = model
        self._rows = rows
        self._seat_per_row = seat_per_row

    def Registration(self):
        return self._name

    def Plane(self):
        return self._model

    def seat_arragment(self):
        return range(1, self._rows + 1), "ABCDEFGHJ"[:self._seat_per_row]


def make_flight():
    f = Flight("BS2354", Aircraft("G-EURP", "Airbus A748", 15, 6))
    f.allocate_seat("12A", "Navoda")
    f.allocate_seat("11C", "Sunil")
    f.allocate_seat("04D", "Kamal")
    f.allocate_seat("01F", "Nimal")
    return f


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}" \
             "  Flight: {1}" \
             "  Seat: {2}" \
             "  Aircraft: {3}" \
             "|".format(passenger, flight_number, seat, aircraft)
    banner = '+' + '_' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()
