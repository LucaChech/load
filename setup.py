import pickle

with open('config/randomization.pik', 'r') as of:
    trials_raw = pickle.load(of)


 trials = {}

cols = ['','']

for k in trials_raw.keys():
    l = trials_raw[k]
    trial_dict = {}
    for i in range(len(l)):
        trial_dict[cols[i]] = l[i]
    trials[k] = trial_dict

