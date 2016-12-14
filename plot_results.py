import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

no_hopping_scores = pd.read_csv('test-results/No_Hopping_results_FINAL.csv')
no_hopping_times = pd.read_csv('test-results/No_Hopping_timings_FINAL.csv').diff().dropna()
hopping_scores = pd.read_csv('test-results/Hopping_results.csv')
hopping_times = pd.read_csv('test-results/Hopping_timings.csv').diff().dropna()
hopping_mod_scores = pd.read_csv('test-results/Hopping_adj_results.csv')
hopping_mod_times = pd.read_csv('test-results/Hopping_adj_timings.csv').diff().dropna()

print "No hopping time:", (no_hopping_times[no_hopping_times<1000]).sum()/(60*60.)
print "Hopping time:", (hopping_times[hopping_times<1000]).sum()/(60*60.)
print "Adjusted hopping time:", (hopping_mod_times[hopping_mod_times<30]).sum()/(60*60.)

win = 100
no_hop_line,  = plt.plot(no_hopping_scores.rolling(window=win,center=False).mean(), label='Baseline')
hop_line,  = plt.plot(hopping_scores.rolling(window=win,center=False).mean(), label='Time Hopping')
adjust_hop_line, = plt.plot(hopping_mod_scores.rolling(window=win,center=False).mean(), label='Adjusted Time Hopping')
plt.legend(handles=[no_hop_line,hop_line,adjust_hop_line],loc='lower right')
plt.xlabel('Number of Episodes')
plt.ylabel('Score')
plt.savefig('test-results/scores.jpg')
plt.close()

bins = np.arange(0,30,1)

fig = plt.figure()
ax = fig.add_subplot(111)


_ = ax.hist(no_hopping_times.values,alpha=0.4, bins=bins, label='Baseline',normed=True)
_ = ax.hist(hopping_times.values,alpha=0.4, bins=bins, label='Time Hopping',normed=True, color='green')
_ = ax.hist(hopping_mod_times.values,alpha=0.4, bins=bins, label='Adjusted Time Hopping',normed=True, color='red')

plt.legend(loc='upper right')
plt.xlabel('Time per step (sec)')
plt.ylabel('Fraction of steps')
plt.savefig('test-results/time-dists.jpg')
plt.close()