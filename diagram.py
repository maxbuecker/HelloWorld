import matplotlib as plt
import numpy as np
import time
import force
import limit

timelimit = 1000000 #in seconds

limits = np.array([[0, limit],
                   [timelimit, limit]])

plt.plot(time,force)
plt.plot(limits[:,0],limits[:,1]

plt.title('Gemessene Kraft')
plt.xlabel('Zeit in Sekunden')
plt.ylabel('Kraft in Newton')
plt.xlim([0,timelimit])
plt.ylim([np.min(force)-1000,np.max(force)+1000])
plt.legend(('Kraft','Schwellenwert')
