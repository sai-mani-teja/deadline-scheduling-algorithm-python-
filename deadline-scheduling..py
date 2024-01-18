num = int(input("Enter the number of CPU's: "))
for k in range(0, num):
    n = int(input("Enter the number of Process: "))
    b = {}
    a = {}
    d = {}
    for i in range(0, n):
        pid = input("Enter the Process Id: ")
        at = int(input(f"Enter the Arrival time for Process{i}: "))
        a[pid] = at
        bt = int(input(f"Enter the Burst time for Process{i}: "))
        b[pid] = bt
        dt = int(input(f"Enter the Deadline time for Process{i}: "))
        d[pid] = dt
    print(f"The Arrival Times of CPU{k} Processes are: ")
    print(a)
    print(f"The Burst Times of CPU{k} Processes are: ")
    print(b)
    print(f"The Deadline Times of CPU{k} Processes are: ")
    print(d)
    ct1 = []
    c = {}
    ct = 0
    a1 = {}
    b1 = {}
    d1 = {}
    temp = min(d.values())
    for id,deadline in d.items():
        if deadline == temp:
            res = id
            d1[res] = d[res]
    for id,arrival in a.items():
        if id == res:
            flag = 1
            at1 = a[res]
            a1[res] = at1
    for id,burst in b.items():
        if id == res:
            if flag == 1: 
                if (at1 >= 0 and at1 <= ct):
                    ct += b[res]
                    c[res] = ct
                    b1[res] = b[res]
                    ct1.append(ct)
                else:
                    ct += at1 + b[res]
                    c[res] = ct
                    b1[res] = b[res]
                    ct1.append(ct)
            else:
                print("Invalid Process Id")
    a.pop(res)
    b.pop(res)
    d.pop(res)
    for i in range(1, n):
        temp = min(d.values())
        for id,deadline in d.items():
            if deadline == temp:
                res = id
                d1[res] = d[res]
        for id,arrival in a.items():
            if id == res:
                flag = 1
                at1 = a[res]
                a1[res] = at1
        for id,burst in b.items():
            if id == res:
                if flag == 1: 
                    if (at1 >= 0 and at1 <= ct):
                        ct += b[res]
                        c[res] = ct
                        b1[res] = b[res]
                        ct1.append(ct)
                    else:
                        ct += (at1 - ct1[i-1]) + b[res]
                        c[res] = ct
                        ct1.append(ct)
                        b1[res] = b[res]
                        
                else:
                    print("Invalid Process Id")
        a.pop(res)
        b.pop(res)
        d.pop(res)
    print(f"The Completion Times of CPU{k} Processes are: ")
    print(c)
    tat = {}
    for i in c:
        if i in a1:
            tat[i] = c[i] - a1[i]
    print(f"The Turn Around Times of CPU{k} Processes are: ")
    print(tat)
    wt = {}
    for i in tat:
        if i in b1:
            wt[i] = tat[i] - b1[i]
    print(f"The Waiting Times of CPU{k} Processes are: ")
    print(wt)
    tat_sum = 0
    for i in tat.values():
        tat_sum += i
    avg_tat = tat_sum/n
    wt_sum = 0
    for i in wt.values():
        wt_sum += i
    avg_wt = wt_sum/n
    print(f"The Average Turn Around Time of CPU{k} is: {avg_tat}")
    print(f"The Average Waiting Time of CPU{k} is: {avg_wt}")
