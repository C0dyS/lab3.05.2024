import pickle
import gzip

def main():
    while True :
        user_choice = int(input('''
        1 - export data
        2 - import data
        3 - add data
        4 - remove data
        5 - to exit
        '''))
        if user_choice == 1 :
            with gzip.open('task_file_2.gz','wb') as file:
                exported_data = list(input())
                pickle.dump(exported_data,file)
        elif user_choice == 2:
            with gzip.open('task_file_2.gz','rb') as file:
                imported_data = pickle.load(file)
        elif user_choice == 3:
            with gzip.open('task_file_2.gz', 'rb') as file:
                temporal_data = pickle.load(file)
            temporal_data.append(input())
            with gzip.open('task_file_2.gz', 'wb') as file:
                pickle.dump(temporal_data, file)
        elif user_choice == 4:
            with gzip.open('task_file_2.gz', 'rb') as file1:
                temporal_data = pickle.load(file1)
                user_remove_choice = int(input('select amount of elements to remove from the back: '))
                if user_remove_choice > 0 and user_remove_choice <= len(temporal_data):
                    temporal_data = temporal_data[:-user_remove_choice]
                    with gzip.open('task_file_2.gz', 'wb') as file:
                        pickle.dump(temporal_data, file)
                else:
                    print("Invalid choice. There are not enough elements to remove.")
        else:
            break
