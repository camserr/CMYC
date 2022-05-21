from fileinput import filename
import math
import sys



# to run: python3 time.py hc.txt 2 -> python3 time.py result sheet wind category

def calculate(arr, wind):
    final = []
    ftime = 0
    handicap = {'HGET' : [87.5, 87.5, 86.2, 86.2, 82.5],
     'FSCT' : [92.1, 92.1, 90.4, 90.4, 89.1], 
     'LASE' : [93.7, 93.7, 92.3, 92.3, 91.0], 
     'EN' : [98.2, 98.2, 96.9, 96.9, 95.7], 
     'BUT' : [110.1, 110.1, 109.4, 109.4, 106.9],
     'H16' : [81.5, 81.5, 78.7, 78.7, 74.1],
     'FD' : [81.5, 81.5, 78.4, 78.4, 75.9],
     'ALBA' : [94.5, 94.5, 92.5, 92.5, 88.7],
     'SF' : [103.0, 103.0, 100.4, 100.4, 97.8],
     'THISTLE' : [83.0, 83.0, 83.0, 83.0, 83.0],
     'NACRA' : [69.0, 69.0, 68.0, 68.0, 65.0],
     'HI' : [84.3, 84.3, 87.8, 87.8, 86.3],
     'HWAV' : [92.1, 92.1, 95.8, 95.8, 92.7]}

    for i in range(len(arr)):
        time = arr[i][-1]
        a1 = time.split(':')
        if len(a1) ==3:
            hrs = float(a1[0])
            mins = float(a1[1]) + (hrs * 60)
            secs = float(a1[2])
            
        else:
            mins = float(a1[0])
            secs = float(a1[1])
        
        kind = arr[i][1].strip()
        if kind in handicap.keys():
            h = handicap[kind][wind]
            f1 = mins + (secs / 60)
            ftime = (f1 / h) * 100
            ftime  = str(round(ftime, 2))
            #print(ftime)
            if int(ftime[:2]) > 59:
                hrs = int(ftime[:2])// 60
                mins = int(ftime[:2]) % 60
                if mins < 10:
                    ftime = str(hrs) + ':0' + str(mins) + ':' + str(int(float(ftime[-2: ])* 60))
                else:
                    ftime = str(hrs) + ':' + str(mins) + ':' + str(int(float(ftime[-2: ])* 60))
            else:
                ftime = ftime[:2] + ':' + str(int(float(ftime[-2:])* 60))
        ##########################################COMPLETE###########################################################

            tup = (ftime, arr[i])
            final.append(tup)
        else:
            final.append(('ERROR', arr[i]))
    

    return final #[(ftime, arr)]


if __name__ == "__main__":
    # Get the input
    filename = sys.argv[1]
    wind = sys.argv[2]
    wind_speed = int(wind)
    finalname = filename.split('.')[0] + '_results.txt'

    pre = []
    # Open the file
    with open(filename, 'r') as f:
        # Read the file
        lines = f.readlines()
        # Loop through the lines
        for line in lines:
            # Split the line into a list
            line = line.split(',')
            # Append the list to the pre list
            pre.append(line)
            # # Get the boat name
            # boat = line[0]
            # # Get the time
            # ctime = line[1]
            # time = float(line[1])
    final = calculate(pre, wind_speed) #[(time, [boat, handicap, time])]
    final1 = sorted(final, key=lambda x: x[0])

    # Open the file
    with open(finalname, 'w') as f:
        # Loop through the list
        for line in final1:
            # Write the line to the file
            f.write(line[0] + ' ' + str(line[1]) + '\n')
        


    pass