import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path + '/metrics')

import maximin
import maximax
import optimism_pessimism
import insufficient_reason

if __name__ == "__main__":
    performance = [[0.7, 0.8, 0.9], [0.8, 0.9, 1.0]]
    robustness = maximin.calc(performance)
    print(robustness)
    robustness = maximax.calc(performance)
    print(robustness)
    robustness = optimism_pessimism.calc(performance)
    print(robustness)
    robustness = insufficient_reason.calc(performance)
    print(robustness)