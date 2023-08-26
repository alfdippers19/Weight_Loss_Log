class User():
    def __init__ (self, user_data = [], user_current_data = 0):
        print('User Created')
        self.user_data = user_data
        self.user_current_data = user_current_data
        #user data will  be organised in 2d array, each data point in the list will contain a date and a weight

    def add_weight_data(self,user_data,user_current_data):

        print('Please input a weight in lbs')
        weight_input = int(input('Weight: '))

        self.user_data.append(weight_input)
        print(f'Your inputted weight is {self.user_data[user_current_data]}')
        self.user_current_data = self.user_current_data + 1
        main()

    def view_weight_data(self):

        for i in self.user_data:
            print(f'{i},')
        main()

def main_buffer():
    main()

def main():
    print('Would you like to add, remove, or view your weight data?')
    choice_0 = input('A / R / V: ')
    if choice_0 == 'A':
        current_user.add_weight_data(current_user.user_data,current_user.user_current_data)
    elif choice_0 == 'V':
        current_user.view_weight_data()
    else:
        print('Invalid input!')
        main_buffer()


print('Program started!')
current_user = User()
if __name__ == '__main__':
    main()