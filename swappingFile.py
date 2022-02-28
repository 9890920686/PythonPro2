### both text files are currently in stage 1. once you run the programme the data in files will swap.

def swapFile():
    file1 = input("Enter file 1 location: ")
    file2 = input("Enter file 2 location: ")

    with open(file1 , 'r') as a:
        data1 = a.read()

    with open(file2 , 'r') as a:
        data2 = a.read()

    with open(file1 , 'w') as a:
        a.write(data2)
        a.close()

    with open(file2 , 'w') as a:
        a.write(data1)
        a.close()

swapFile()

    

    
    