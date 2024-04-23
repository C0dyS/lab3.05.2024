import pickle

def input_to_file():
    start_list = list(input())
    with open('task_file.txt','wb') as file:
        pickle.dump(start_list,file)

def file_to_code():
    with open('task_file.txt','rb') as file:
        imported_data = pickle.load(file)
    print(type(imported_data),imported_data)


input_to_file()
file_to_code()
