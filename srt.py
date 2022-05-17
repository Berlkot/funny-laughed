def merge_sort(mas: list):
    sor = []
    for i in range(len(mas)):
        sor.append([mas[i]])
    while len(sor) != 1:
        pod = []
        mas1, mas2 = sor.pop(0), sor.pop(0)
        for i in mas1:
            for j in mas2:
                s = j
                if i > s:
                    pod.append(s)
                else:
                    break
            pod.append(i)
            if mas1[-1] == i and i < s and s == mas2[-1]:
                pod.append(j)
        sor.append(pod)
        print(sor)
    return(sor)
