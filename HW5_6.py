subject_dict = {}
numbers = []
q = ''

with open('file5_6.txt', encoding='utf-8') as f:
    for el in f.readlines():
        subject = el.split()[0]

        for i in range(len(el)):
            if el[i].isdigit():
                q += el[i]

                try:
                    if not el[i + 1].isdigit():
                        numbers.append(q)
                        q = ''
                except:
                    numbers.append(q)

        quantity = sum(map(int, numbers))
        subject_dict[subject] = quantity
        numbers = []
        q = ''

    print(subject_dict)
