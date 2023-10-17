__author__ = 'nonthakon jitchiranant'
class account(): #define a class for account
    def __init__(self,name='user'):
        self.name = name
        self.account = {}
        self.transaction_num = 0
        self.net = 0
        
    def add_transaction(self, time_create, type, value, purpose='unknown', comment='unknown'):
        self.account[self.transaction_num] = (time_create, type, value, purpose, comment)
        if type == 'income':
            self.net += value
            self.transaction_num += 1
        elif type == 'expense':
            self.net -= value
            self.transaction_num += 1
        else:
            print('error : transaction {} can\'t be add.'.format(self.account[self.transaction_num]))
            del self.account[self.transaction_num]
        
    def show_income(self):
        print(self.all_income())
        
    def show_expense(self):
        print(self.all_expense())
        
    def show_all(self):
        print(self.account)
        
    def show_by_day(self, day):
        print(self.transaction_by_day(day))
        
    def transaction_by_day(self, day):
        return_dict = {}
        for key, value in self.account.items():
            if value[0] == day:
                return_dict[key] = value
        return return_dict
    
    def all_income(self):
        return_dict = {}
        for key, value in self.account.items():
            if value[1] == 'income':
                return_dict[key] = value
        return return_dict
    
    def all_expense(self):
        return_dict = {}
        for key, value in self.account.items():
            if value[1] == 'expense':
                return_dict[key] = value
        return return_dict
    
    def income_by_day(self, day):
        return_dict = {}
        for key, value in self.account.items():
            if value[1] == 'income' and value[0] == day:
                return_dict[key] = value
        return return_dict

    def expense_by_day(self, day):
        return_dict = {}
        for key, value in self.account.items():
            if value[1] == 'expense' and value[0] == day:
                return_dict[key] = value
        return return_dict
    
    def net_by_day(self, day):
        cur_net = 0
        for key, value in self.account.items():
            if value[1] == 'income' and value[0] == day:
                cur_net += value[2]
        for key, value in self.account.items():
            if value[1] == 'expense' and value[0] == day:
                cur_net -= value[2]
        return cur_net