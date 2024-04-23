import pickle
import gzip

def main():
    workable_data = {}
    while True :
        user_choice = int(input('''
        1 - add data
        2 - remove data
        3 - search(passwords for logins)
        4 - edit
        5 - import data
        6 - save data
        7 - exit
        '''))

        if user_choice == 1 :
                new_login, new_password = input("Enter new login and password separated by space: ").split()
                workable_data[new_login] = new_password
        elif user_choice == 2:
            user_remove_choice = input('Enter login value to remove')
            if user_remove_choice in workable_data:
                workable_data.pop(user_remove_choice)
        elif user_choice == 3:
            user_password_search = input('Enter login to find out corresponding password')
            if user_password_search in workable_data:
                print(workable_data[user_password_search])
            else:
                print('such login doesnt exit')
        elif user_choice == 4:
            user_login,user_password_change = input('Enter your login and new password separated by space').split()
            workable_data[user_login] = user_password_change
        elif user_choice == 5:
            file_path = input('enter file path')
            with open(file_path, 'rb') as file:
                workable_data = pickle.load(file)
        elif user_choice == 6:
            file_path = input('Enter file path to save data: ')
            with gzip.open(file_path, 'wb') as file:
                pickle.dump(workable_data, file)
        else:
            print('exiting the program')
            break
