import re


class AbhinandanPlex:

    visits = False

    def __init__(self):
        try:
            self.row = int(input('Enter the rows: '))
            self.col = int(input('Enter the cols: '))
        except ValueError:
            print('\nPlease enter valid information.\n')
            self.__init__()

        self.booked = list()
        self.cusInfo = list()
        self.seat_booked = len(self.booked)
        self.total_seats = self.row*self.col


class Seats(AbhinandanPlex):
    def __init__(self):
        super().__init__()

    def startSeats(self):
        if AbhinandanPlex.visits == False:
            self.defaultSeats()
        else:
            self.showSeats()

    # this method is used to display the empty seats when no seat is being booked
    def defaultSeats(self):
        print('\nHere "S" shows the vacant seats.')
        print("Here 'B' shows booked seats\n")
        self.seat_count = 0  # used to count seats booked
        self.list1 = []  # dummy list created to display empty seats

        self.total_seats = self.row*self.col  # stores total number of seats booked
        self.dict1 = dict()

        self.list_col_name = list()
        for c in range(1, self.col+1):
            self.list_col_name.append(str(c))
        print(' ', ' '.join(self.list_col_name))
        for r in range(1, self.row+1):
            self.list1 = list()
            for c in range(1, self.col+1):
                self.list1.append('S')  # list changes for each row
            print(r, ' '.join(self.list1))
        print('\n')

    def showSeats(self):
        self.list_col_name = list()
        for c in range(1, self.col+1):
            # displaying numbering of columns
            self.list_col_name.append(str(c))
        print(' ', ' '.join(self.list_col_name))

        for r in range(1, self.row+1):  # iterating over number of rows
            str_list = []  # contains status of seats in a row
            itera = 0
            done = []  # list created to store the rows which are already iterated over
            for items in self.booked:  # iterating over seats booked
                # this section will show status of seats in rows which contain booked seats
                if r == items[0]:
                    if r not in done:
                        for c in range(1, self.col+1):
                            if c == items[1]:
                                str_list.append('B')
                                itera += 1
                                done.append(r)
                            else:
                                str_list.append('S')
                                itera += 1
                                done.append(r)
                    else:
                        for c in range(1, self.col+1):
                            if c == items[1]:
                                str_list[c-1] = 'B'
                        done.append(r)
            if itera < self.col:  # this will show status of seats in the rows which don't have any booked seat
                while itera < self.col:
                    str_list.append('S')
                    itera += 1
            # will print the seating arrangment row by row
            print(r, ' '.join(str_list))


class BuyTicket(AbhinandanPlex):
    def __init__(self):
        print('\nHere you can buy the ticket.\n')
        self.choose()

    def choose(self):
        try:
            self.row_choice = int(input('Enter your choice of row: '))  
            self.col_choice = int(input('Enter your choice of column: '))

            if self.row_choice <= self.row and self.col_choice <= self.col and self.row_choice > 0 and self.col_choice > 0:
                if [self.row_choice, self.col_choice] in self.booked:
                    print('\nThis seat is already booked.')
                    print('Please select another one.\n')
                    self.choose()
                else:
                    self.booked.append([self.row_choice, self.col_choice])
                    self.customerInfo(self.row_choice, self.col_choice)

            else:
                print('\nPlease make sure the seat number exists.\n')
                self.choose()
        except ValueError:
            print('\nEnter valid values.\n')
            self.choose()

    def customerInfo(self, booked_row, booked_col):
        current_cust = list()
        seat_no = [booked_row, booked_col]  # stores seat number

        def custNameValidate():  # taking customer info and simultaneously validating it
            cust_name = input('Enter your name: ')
            x = re.findall("[0-9]", cust_name)
            if len(x) != 0:
              print('\nInvalid character found in customer name.\n')
              custNameValidate()
            else:
                return cust_name

        def custNoValidate():  # phone number validation
            cust_no = input('\nEnter your phone number: \n')
            try:
                if int(int(cust_no)/1000000000) > 0 and int(int(cust_no)/1000000000) < 10:
                    return cust_no
                else:
                    print('\nPlease enter a valid phone number.\n')
                    custNoValidate()
            except ValueError:
                print('\nPlease enter a valid phone number.\n')
                custNoValidate()

        def custGenValidate():  # gender validation
            cust_gend = input('\nEnter your gender (M/F/O): \n')
            cust_gend = cust_gend.upper()
            if cust_gend not in ['M', 'F', 'O']:
                print('\nEnter a valid gender.\n')
                custGenValidate()
            else:
                return cust_gend

        def custAgeValidate():  # age validation
            try:
                cust_age = input('\nEnter your age: \n')
                if int(cust_age) < 1 or int(cust_age) > 110:
                    print('\nEnter a valid age.\n')
                    custAgeValidate()
                else:
                    return cust_age
            except ValueError:
                print('\nPlease enter a valid age.\n')
                custAgeValidate()

        cust_name = custNameValidate()
        cust_no = custNoValidate()
        cust_gend = custGenValidate()
        cust_age = custAgeValidate()

        current_cust.append(seat_no)
        current_cust.append(cust_name)
        current_cust.append(cust_no)
        current_cust.append(cust_gend)
        current_cust.append(cust_age)

        self.cusInfo.append(current_cust)
        AbhinandanPlex.visits = True
        print('\nInformation successfully added.\n')


class Stats(AbhinandanPlex):
    def __init__(self):
        super().__init__()

    def statistics(self):
        print('Number of purchased tickets:', self.seat_booked)

        if self.total_seats > 60:
            # hall_size = 'Large'
            if self.row % 2 == 0:
                mid = self.row/2
            else:
                mid = (self.row//2)+1
            total_sale = 0
            for current_seat in self.booked:
                if current_seat[0] < mid:
                    current_price = 10
                    total_sale += current_price
                elif current_seat[0] >= mid:
                    current_price = 8
                    total_sale += current_price

            print('Current Income is $', total_sale)

        else:
            # hall_size = 'Small'
            total_sale = 0
            for current_seat in self.booked:
                current_price = 10
                total_sale += current_price
            print('Current Income is $', total_sale)

        if self.total_seats > 60:
            if self.row % 2 == 0:
                mid = self.row/2
                first_half = (mid*self.col)*10
                second_half = (mid*self.col)*8
                total_income = first_half+second_half
                print('Total income is: $', int(total_income))
            else:
                mid = (self.row//2)+1
                first_half = ((mid-1)*self.col)*10
                second_half = ((mid)*self.col)*8
                total_income = first_half+second_half
                print('Total income is: $', int(total_income))
        else:
            total_income = self.row*self.col*10
            print('Total income is: $', int(total_income))


class CustInfo(AbhinandanPlex):
    def __init__(self):
        super().__init__()

    def getInfo(self):
        print('\nNote: Enter "0" in either row or column to leave the menu.')
        try:
            self.get_row = int(input('\nEnter the row number.\n'))
            self.get_col = int(input('Enter the column number.\n'))

            if self.get_row == 0 or self.get_col == 0:
                pass
            else:

                if [self.get_row, self.get_col] in self.booked:
                    print('Here is the information for the customer.')

                    for group in self.cusInfo:
                        print(group)
                        for seat_no in group:
                            if seat_no == [self.get_row, self.get_col]:
                                print('Name:', group[1])
                                print('Phone No.:', group[2])
                                print('Gender:', group[3])

                                if self.total_seats > 60:
                                    if self.row % 2 == 0:
                                        mid = self.row/2
                                        if self.get_row <= mid:
                                            print('Ticket Price: $10.')
                                        elif self.get_row > mid:
                                            print('Ticket Price: $8.')
                                    else:
                                        mid = (self.row//2)+1
                                        if self.get_row <= mid:
                                            print('Ticket Price: $10.')
                                        elif self.get_row > mid:
                                            print('Ticket Price: $8.')
                                else:
                                    print('Ticket Price: $10.')

                                print('Age:', group[4])

                    self.getInfo()

                else:
                    print('This seat is vacant.')
                    self.getInfo()
        except ValueError:
            print('\nPlease enter vaid info.\n')
            self.getInfo()


class Finale(Seats, BuyTicket, Stats, CustInfo, AbhinandanPlex):
    def __init__(self):
        AbhinandanPlex.__init__(self)
        print('\nWelcome to AbhinandanPlex!\n')
        print('\nWe are having the World Premiere of "Star Wars: The Last Jedi".\n')
        print('\nBook your tickets fast!!!\n')
        self.showMenu()

    def showMenu(self):
        print('1. Show the seats')
        print('2. Buy a ticket')
        print('3. Statistics')
        print('4. Show booked Tickets User Info')
        print('0. Exit')
        try:
            self.option = int(input('Choose from the options mentioned above. '))
            if self.option == 1:
                super().startSeats()
                self.showMenu()
            elif self.option == 2:
                BuyTicket.__init__(self)
                self.showMenu()
            elif self.option == 3:
                Stats.statistics(self)
                self.showMenu()
            elif self.option == 4:
                print('\nEnter the seat number to get the customer info.\n')
                CustInfo.getInfo(self)
                self.showMenu()
            elif self.option == 0:
                print('\nThanks for using AbhinandanPlex.\n')
            else:
                print("\nInvalid Option.\n")
        except ValueError:
            print('\nInvalid Option.\n')
            self.showMenu()


obj = Finale()


