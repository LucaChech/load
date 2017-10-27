import pickle

with open('config/randomization.pik', 'r') as of:
    trials_raw = pickle.load(of)

trials = {}

cols = ['cat_1','cat_2','cat_3','cat_4','cat_5','TS','load','exemplar','question','present_absent','trial_type','tone_hz','tone_onset','image_name','block']

for k in trials_raw.keys():
    l = trials_raw[k]
    trial_dict = {}
    for i in range(len(l)):
        trial_dict[cols[i]] = l[i]
    trials[k] = trial_dict

