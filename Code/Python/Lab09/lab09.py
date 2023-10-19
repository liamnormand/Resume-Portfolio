import random
import statistics

def wordcount(fname):
    try:
        with open(fname) as file:
            full_file = file.read()
            full_file = full_file.split()
            return len(full_file)
    except FileNotFoundError:
        print("File does not exist")

    
def test_fun():
    try:
        x = int(input("Enter a number"))
        z = 2/x
        print("Good job, no errors")
    except ValueError:
        print("Input was not an integer, setting z to -1")
        z = -1
    except ZeroDivisionError:
        print("Can't divide by 0, setting z to -2")
        z = -2
    print(z)

def make_data(fname):
    with open(fname,'w') as csv:
        for i in range(1,1001):
            rand = random.randint(-1000,1000)
            csv.write(f'{i},{rand}\n')

def read_data(fname):
    try:
        with open(fname) as csv:
            abs_min = 1001
            abs_max = -1001
            for row in csv:
                current_val = int(row[row.find(',')+1:row.find('\n')])
                if abs_min > current_val:
                    abs_min = current_val
                if abs_max < current_val:
                    abs_max = current_val
        print(f"Absolute min is {abs_min}")
        print(f"Absolute max is {abs_max}")
    except FileNotFoundError:
        print("Bad file name")

def stock_reader(fname):
    try:
        with open(fname) as csv:
            close_list = []
            First = True
            for row in csv:
                if First:
                    First = False
                    continue
                current_row = row.strip().split(',')
                close_list.append(float(current_row[4]))
            
            mean = statistics.mean(close_list)
            median = statistics.median(close_list)
            minimum = min(close_list)
            maximum = max(close_list)

            print(f'Mean: {mean}')
            print(f'Median: {median}')
            print(f'Minimum: {minimum}')
            print(f'Maximum: {maximum}')
    except FileNotFoundError:
        print("Bad file name")


            

if __name__ == '__main__':
    print(wordcount("no.py"))
    #print(test_fun()) #"Hi", "0", "2"
    make_data("test_table.csv")
    read_data("test_table.csv")
    read_data("Bad_File.txt")
    stock_reader("MDT.csv")
    print()
    stock_reader("NVDA.csv")
    print()
    stock_reader("AMD.csv")
