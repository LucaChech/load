import csv


import pickle
with open('../config/trials.pik', 'r') as of:
    trials = pickle.load(of)

blocks_final = []
with open('config/images.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        #print ', '.join(row)
        blocks_final.append(row)

low_one = blocks_final[0]
high_one = blocks_final[1]
high_two = blocks_final[2]
low_two = blocks_final[3]
high_three = blocks_final[4]
low_three = blocks_final[5]
low_four = blocks_final[6]
high_four = blocks_final[7]
low_five = blocks_final[8]
high_five = blocks_final[9]
high_six = blocks_final[10]
low_six = blocks_final[11]
high_seven = blocks_final[12]
low_seven = blocks_final[13]
low_eight = blocks_final[14]
high_eight = blocks_final[15]

low_one = [x.strip() for x in low_one[0].split(',')]
low_two = [x.strip() for x in low_two[0].split(',')]
low_three = [x.strip() for x in low_three[0].split(',')]
low_four = [x.strip() for x in low_four[0].split(',')]
low_five = [x.strip() for x in low_five[0].split(',')]
low_six = [x.strip() for x in low_six[0].split(',')]
low_seven = [x.strip() for x in low_seven[0].split(',')]
low_eight = [x.strip() for x in low_eight[0].split(',')]
high_one = [x.strip() for x in high_one[0].split(',')]
high_two = [x.strip() for x in high_two[0].split(',')]
high_three = [x.strip() for x in high_three[0].split(',')]
high_four = [x.strip() for x in high_four[0].split(',')]
high_five = [x.strip() for x in high_five[0].split(',')]
high_six = [x.strip() for x in high_six[0].split(',')]
high_seven = [x.strip() for x in high_seven[0].split(',')]
high_eight = [x.strip() for x in high_eight[0].split(',')]

blocks_final = [low_one, high_one, high_two, low_two, high_three, low_three, low_four, high_four, low_five, high_five, high_six, low_six, high_seven, low_seven, low_eight, high_eight]

#-----------------------------------------------------------------------------------------------------------------------------------------------------
probes_position_list = []
with open('config/probes.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        probes_position_list.append(row)

list_low_one = probes_position_list[0]
list_high_one = probes_position_list[1]
list_high_two = probes_position_list[2]
list_low_two = probes_position_list[3]
list_high_three = probes_position_list[4]
list_low_three = probes_position_list[5]
list_low_four = probes_position_list[6]
list_high_four = probes_position_list[7]
list_low_five = probes_position_list[8]
list_high_five = probes_position_list[9]
list_high_six = probes_position_list[10]
list_low_six = probes_position_list[11]
list_high_seven = probes_position_list[12]
list_low_seven = probes_position_list[13]
list_low_eight = probes_position_list[14]
list_high_eight = probes_position_list[15]



list_low_one = [x.strip() for x in list_low_one[0].split(',')]
list_low_two = [x.strip() for x in list_low_two[0].split(',')]
list_low_three = [x.strip() for x in list_low_three[0].split(',')]
list_low_four = [x.strip() for x in list_low_four[0].split(',')]
list_low_five = [x.strip() for x in list_low_five[0].split(',')]
list_low_six = [x.strip() for x in list_low_six[0].split(',')]
list_low_seven = [x.strip() for x in list_low_seven[0].split(',')]
list_low_eight = [x.strip() for x in list_low_eight[0].split(',')]
list_high_one = [x.strip() for x in list_high_one[0].split(',')]
list_high_two = [x.strip() for x in list_high_two[0].split(',')]
list_high_three = [x.strip() for x in list_high_three[0].split(',')]
list_high_four = [x.strip() for x in list_high_four[0].split(',')]
list_high_five = [x.strip() for x in list_high_five[0].split(',')]
list_high_six = [x.strip() for x in list_high_six[0].split(',')]
list_high_seven = [x.strip() for x in list_high_seven[0].split(',')]
list_high_eight = [x.strip() for x in list_high_eight[0].split(',')]

list_low_one = [int(n[1:-1]) for n in list_low_one ]
list_low_two = [int(n[1:-1]) for n in list_low_two]
list_low_three = [int(n[1:-1]) for n in list_low_three ]
list_low_four = [int(n[1:-1]) for n in list_low_four ]
list_low_five = [int(n[1:-1]) for n in list_low_five ]
list_low_six = [int(n[1:-1]) for n in list_low_six ]
list_low_seven = [int(n[1:-1]) for n in list_low_seven ]
list_low_eight = [int(n[1:-1]) for n in list_low_eight ]
list_high_one = [int(n[1:-1]) for n in list_high_one ]
list_high_two = [int(n[1:-1]) for n in list_high_two ]
list_high_three= [int(n[1:-1]) for n in list_high_three]
list_high_four = [int(n[1:-1]) for n in list_high_four ]
list_high_five = [int(n[1:-1]) for n in list_high_five ]
list_high_six = [int(n[1:-1]) for n in list_high_six ]
list_high_seven = [int(n[1:-1]) for n in list_high_seven ]
list_high_eight= [int(n[1:-1]) for n in list_high_eight ]

probes_position_list = [list_low_one, list_high_one, list_high_two, list_low_two, list_high_three, list_low_three, list_low_four, list_high_four, list_low_five, list_high_five, list_high_six, list_low_six, list_high_seven, list_low_seven, list_low_eight, list_high_eight]

