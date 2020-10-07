def file_read(fname):
        with open(fname) as f:     
                content_list = f.readlines()
                print(content_list)
file_read('D:/python assingment2/Q-2.txt')