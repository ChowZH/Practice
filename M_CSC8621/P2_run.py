run_times = open('run_times.in', "r")

times = []
times_sec = []
sum_total = 0

for x in run_times:
    times.append(x.rstrip('\n'))
    h = ''.join(x[0] + x[1])
    m = ''.join(x[3] + x[4])
    s = ''.join(x[6] + x[7])
    total_time = ((int (h))*60*60) + ((int (m))*60) + (int (s))
    times_sec.append(total_time)

    sum_total += total_time

run_times.close()

if __name__ == "__main__":
    print ("The length of list 'times' is : {}" .format(len(times)))

    top_ten = []
    times_sorted = sorted(times)
    for i in range(10):
        top_ten.append(times_sorted[i])
    print ("Top 10 times are : {}" .format(top_ten))

    print ("All times in seconds are : {}". format(times_sec))

    # Assignment Task 3
    S = sum_total%60
    Prod = (sum_total-S)/60
    M = Prod%60
    Prod = (Prod-M)/60
    H = Prod%24
    Prod = (Prod-H)/24
    D = Prod
    print ("Cumulative time spent by runners is {}D:{}H:{}M:{}S".format(int (D), int (H), int (M), int (S)))

    # Assignment Task 4
    mean = sum_total/100
    S = mean%60
    Prod = (mean-S)/60
    M = Prod%60
    Prod = (Prod-M)/60
    H = Prod%24
    print ("Mean time spent by runners is {}H:{}M:{}S".format(int (H), int (M), int (S)))
