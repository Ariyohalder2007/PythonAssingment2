def file_read(fname):
        my_array = []
        with open(fname) as f:   
                for i in f:
                        my_array.append(i)
                print(my_array)

file_read('D:/python assingment2/Q-2.txt')
