subj = {}
with open('file_6.txt', 'r', encoding='utf-8') as init_f:
    for line in init_f:
        #subject, lecture, practice, lab = line.split()
        line = line.replace('-', '0').replace('(л)', '').replace('(пр)', '').replace('(лаб)', '')
        subj[line.split()[0]] = sum(map(int, line.split()[1:]))
        #subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n{subj}')
