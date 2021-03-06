import re

class Seats:
    total_itera = 0
    part_itera = 0
    def __init__(self):
        if Seats.part_itera==0:
            print('Welcome to AbhinandanPlex')
            print("\nTonight's special is 'Star Wars: Empire Strikes Back'.")
            print('\nBook Your tickets fast.')
            Seats.part_itera+=1
        
        if Seats.total_itera==0:
            self.row = int(input('Enter the rows: '))
            self.col = int(input('Enter the cols: '))
            Seats.part_itera+=1

        
        self.booked = list()  # used to store seats info
        self.cusInfo = list()  # used to store customer info
        

    def defaultSeats(self):     #this method is used to display the empty seats when no seat is being booked
        print('\nHere "S" shows the vacant seats.')
        print("Here 'B' shows booked seats\n")
        self.seat_count = 0 #used to count seats booked
        self.list1 = [] #dummy list created to display empty seats

        self.total_seats = self.row*self.col    #stores total number of seats booked
        self.dict1 = dict()

        self.list_col_name = list()
        for c in range(1, self.col+1):
            self.list_col_name.append(str(c))
        print(' ', ' '.join(self.list_col_name))
        for r in range(1, self.row+1):
            self.list1 = list()
            for c in range(1, self.col+1):
                self.list1.append('S')  #list changes for each row
            print(r, ' '.join(self.list1))
        print('\n')

    def seatsInfo(self, booked_row, booked_col):    #method used to store customer info
        current_cust = list()
        seat_no = [booked_row, booked_col]  # stores seat number

        def custNameValidate():     #taking customer info and simultaneously validating it
            cust_name = input('Enter your name: ')
            x = re.findall("[0-9]", cust_name)
            if len(x) != 0:
              print('Invalid character found in customer name.')
              custNameValidate()
            else:
                return cust_name
        

        def custNoValidate():   #phone number validation
            cust_no = input('Enter your phone number: ')
            try:
                if int(int(cust_no)/1000000000)>0 and int(int(cust_no)/1000000000)<10:
                    return cust_no
                else:
                    print('Please enter a valid phone number.\n')
                    custNoValidate()
            except ValueError:
                print('Please enter a valid phone number.\n')
                custNoValidate()

        def custGenValidate():  #gender validation
            cust_gend = input('Enter your gender (M/F/O): ')
            cust_gend = cust_gend.upper()
            if cust_gend not in ['M','F','O']:
                print('Enter a valid gender.\n')
                custGenValidate()
            else:
                return cust_gend
        
        def custAgeValidate():  #age validation
            try:
                cust_age = input('Enter your age: ')
                if int(cust_age)<1 or int(cust_age)>110:
                    print('Enter a valid age.\n')
                    custAgeValidate()
                else:
                    return cust_age
            except ValueError:
                print('Please enter a valid age.\n')
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
        

    def show_seats(self):
        self.list_col_name = list()
        for c in range(1, self.col+1):
            self.list_col_name.append(str(c))   #displaying numbering of columns
        print(' ', ' '.join(self.list_col_name))

        for r in range(1,self.row+1):   #iterating over number of rows
            str_list = []   #contains status of seats in a row
            itera = 0
            done=[] #list created to store the rows which are already iterated over
            for items in self.booked:   #iterating over seats booked
                if r == items[0]:       #this section will show status of seats in rows which contain booked seats
                    if r not in done:
                        for c in range(1,self.col+1):
                            if c==items[1]:
                                str_list.append('B')
                                itera+=1
                                done.append(r)
                            else:
                                str_list.append('S')
                                itera+=1
                                done.append(r)
                    else:
                        for c in range(1,self.col+1):
                            if c==items[1]:
                                str_list[c-1] = 'B'
                        done.append(r)
            if itera<self.col:  #this will show status of seats in the rows which don't have any booked seat
                while itera<self.col:
                    str_list.append('S')
                    itera+=1
            print(r,' '.join(str_list)) #will print the seating arrangment row by row
        self.show_menu()


class BuyTicket (Seats):
    def __init__(self):
        if Seats.total_itera==0 and Seats.part_itera == 0:
            super().__init__()
            print("You can now choose your seat: ")
            try:
                Seats.part_itera += 1
                self.row_choice = int(input('Enter your choice of row: '))
                self.col_choice = int(input('Enter your choice of column: '))
                
            except ValueError:
                print('Enter valid values.\n')
                self.__init__()
        else:
            print("You can now choose your seat: ")
            try:
                self.row_choice = int(input('Enter your choice of row: '))
                self.col_choice = int(input('Enter your choice of column: '))
                self.book()
            except ValueError:
                print('Please enter valid values.\n')
                self.checkAvailability()
    def book(self):     #method used for booking seats
        self.booked.append([self.row_choice, self.col_choice])  #stores the booked seat in 'booked'
        super().seatsInfo(self.row_choice, self.col_choice)     #accessing seatsInfo method from 'Seats' class
        self.seat_count += 1
        for i in range(1, self.row+1):
            if i == self.row_choice:
                for j in range(1, self.col+1):
                    if j == self.col_choice:
                        self.list1[j-1] = self.dict1[i, j]
                        self.list1[j-1].replace('S', 'B',)
        print('Congratulations... Your seat is booked.\n')
        Seats.total_itera+=1
        self.show_seats()


    def checkAvailability(self):
        if Seats.total_itera==0:
            if self.row_choice<=self.row and self.col_choice<=self.col:
                print('The seat is available')
                self.dict1[self.row_choice, self.col_choice] = 'B'
                self.book()
            else:
                print('Entered seat number is invalid.')
                print('Please try again.')
                self.row_choice=int(input('Enter your choice of row: '))
                self.col_choice=int(input('Enter your choice of column: '))
                print('\n')
                self.checkAvailability()
                Seats.total_itera+=1

        else:
            if [self.row_choice, self.col_choice] in self.booked:
                print('Sorry, requested seat is not available.')
                
                for level1 in self.cusInfo:
                    
                    for requested in level1:
                        
                        if requested == [self.row_choice,self.col_choice]:
                            
                            print('Here is the information of the current customer.')
                            index=1
                            while index<=4:
                                print(level1[index])
                                index+=1
                self.show_menu()
            else:
                if self.row_choice <= self.row and self.col_choice <= self.col:
                    print('The seat is available')
                    self.dict1[self.row_choice, self.col_choice] = 'B'
                    self.book()
                else:
                    print('Entered seat number is invalid.')
                    print('Please try again.')
                    self.row_choice = int(input('Enter your choice of row: '))
                    self.col_choice = int(input('Enter your choice of column: '))
                    print('\n')
                    self.checkAvailability()

class Statistics(BuyTicket,Seats):
    def __init__(self):
        super().__init__()
    def NumPurTic(self):
        print('Total tickets sold are: ',self.seat_count)
        self.show_menu()
    def PerTicBoo(self):
        print('Percentage of seats booked is: ',round((self.seat_count/self.total_seats)*100,2))
        self.show_menu()
    def CurInc(self):
        if self.total_seats >60:
            # hall_size = 'Large'
            if self.row%2==0:
                mid = self.row/2
            else:
                mid = (self.row//2)+1
            total_sale = 0
            for current_seat in self.booked:
                if current_seat[0]<mid:
                    current_price = 10
                    total_sale+=current_price
                elif current_seat[0]>=mid:
                    current_price = 8
                    total_sale+=current_price

            print('Current Income is',total_sale)
            self.show_menu()
        else:
            # hall_size = 'Small'
            total_sale = 0
            for current_seat in self.booked:
                current_price = 10
                total_sale+=current_price
            print('Current Income is',total_sale)
            self.show_menu()
        
    def TotInc(self):
        if self.total_seats>60:
            if self.row%2==0:
                mid = self.row/2
                first_half = (mid*self.col)*10
                second_half = (mid*self.col)*8
                total_income = first_half+second_half
                print('Total income is: ',int(total_income))
            else:
                mid = (self.row//2)+1
                first_half = ((mid-1)*self.col)*10
                second_half = ((mid)*self.col)*8
                total_income = first_half+second_half
                print('Total income is: ',int(total_income))
        else:
            total_income = self.row*self.col*8
            print('Total income is: ',int(total_income))
        self.show_menu()


    def show_menu(self):
        print('Choose the options from following menu')
        print('1. Number of purchased tickets')
        print('2. Percentage of tickets booked.')
        print('3. Current Income.')
        print('4. Total Income.')
        print('5. Book another seat.')
        print('Q. Quit')

        choose = input('\n')
        if choose=='1':
            self.NumPurTic()
        elif choose=='2':
            self.PerTicBoo()
        elif choose=='3':
            self.CurInc()
        elif choose=='4':
            self.TotInc()
        elif choose=='5':
            super().__init__()
        elif choose=='Q' or choose=='q':
            print('Thank you for Choosing AbhinandanPlex')
        else:
            print('Please select the values from the menu.')
            self.show_menu()


obj = Statistics()
obj.defaultSeats()
obj.checkAvailability()
