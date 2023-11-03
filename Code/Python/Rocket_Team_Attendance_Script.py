def count_attendance(fname):
    full_dict = {}
    try:
        with open(fname) as file:
            full_file = file.readlines()
            for row in full_file:
                current_row = row.strip().split(',')
                #print(type(current_row))
                #print(current_row)
                for n in range(len(current_row)//5):
                    i=5*n+2
                    #print(current_row[i])
                    full_dict[current_row[i][0:8].lower()] = full_dict.setdefault(current_row[i][0:8].lower(), 0) + 1
        del full_dict['']
    except FileNotFoundError:
        print("File not found. Check your spelling.")
    
    for x500, attendance in full_dict.items():
        print(x500 + ': ' + str(attendance))
    
                
if __name__ == '__main__':
    count_attendance("./prop_attendance.csv")          




