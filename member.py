from tabulate import tabulate
import math

class Member:
    data = {
        'Randy' : ['Gold',5_000_000,8_000_000],
        'Kirana' : ['Platinum', 8_000_000, 15_000_000],
        'Arkan' : ['Silver', 4_000_000, 9_000_000]
    }

    header_benefit = ['Membership', 'Discount', 'Another Benefit']
    table_benefit = [
        ['Platinum', 0.15, 'Benefit Gold + Silver + Cashback max. 30%'],
        ['Gold', 0.1, 'Benefit Silver + Voucher Ojek Online'],
        ['Silver', 0.08, 'Voucher Makanan']
    ]

    header_requirement = ['Membership', 'Monthly Expense', 'Monthly Income']
    table_requirement = [
        ['Platinum', 8_000_000, 15_000_000],
        ['Gold', 6_000_000, 10_000_000],
        ['Silver', 5_000_000, 7_000_000]
    ]

    def __init__ (self):
        self.username = None
        self.plan = None
        self.monthly_expense = None
        self.monthly_income = None

    def sign_up (self, username, monthly_expense, monthly_income):
        self.username = username
        self.monthly_expense = monthly_expense
        self.monthly_income = monthly_income
        self.plan = None

        baru = {username : [None, monthly_expense, monthly_income]}

        self.data.update(baru)
        print(self.data)
        return self.data

    def login (self, username):
        self.username = username

        for key, value in self.data.items():
            if key == username:
                self.username = username
                self.plan = value[0]
                self.monthly_expense = value[1]
                self.monthly_income = value[2]
                break
            else:
                self.username = None
                self.plan = None
                self.monthly_expense = None
                self.monthly_income = None

    def logout (self):

        self.username = None
        self.plan = None
        self.monthly_expense = None
        self.monthly_income = None

    def show_benefit(self):
        print ('Benefit Membership RanCommerce')
        print('')
        print(tabulate(self.table_benefit, self.header_benefit))

    def show_requirement(self):
        print ('Requirements Membership RanCommerce')
        print('')
        print(tabulate(self.table_requirement, self.header_requirement))

    def calculate_distance(self, point1, point2):
        '''
        Memakai euclidean distance 

        point1 = parameter requirement
        point2 = parameter user
        '''

        jarak = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5
        return jarak


    def predict_membership (self):
        distance = {}

        for req in self.table_requirement:
            type_req = req[0]
            point_req = req[1:3]

            dist = self.calculate_distance(point_req, [self.monthly_expense, self.monthly_income])
            distance[type_req] = dist
        print (distance)

        min_distance = min(distance, key = distance.get)
        self.plan = min_distance
        self.data[self.username][0] = min_distance

    def calculate_total (self, shopping):
        '''
        Fungsi untuk menghitung total belanja
        input belanja adalah list []
        '''
        
        self.shopping = shopping

        for jenis in self.table_benefit:
            if self.plan == jenis[0]:
                discount_percentage = jenis[1]
        
        total = sum(shopping) - (discount_percentage*sum(shopping))
        return total