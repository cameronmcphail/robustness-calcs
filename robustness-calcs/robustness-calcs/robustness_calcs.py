import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path + '/metrics')

import maximin
import maximax
import optimism_pessimism
import insufficient_reason
import starrs_domain

def calc_all(performance):
    """Returns the robustness values for a variety of metrics

    'performance' is a 2D array of the performance metric used to
        evaluate each solution in each scenario
        dimension 1 is the solution index
        dimension 2 is the scenario index

    returns an array of class instances which include the name of the metric
     and the value of the robustness metric for each solution:
    [
        .name = "Metric 1 name"
        .robustness = [<1D array>],

        .name = "Metric 2 name"
        .robustness = [<1D array>]
    ]
    """

    class robustnessMetric:
        """Contains the name and values or a robustness metric"""
        def __init__(self, name, robustness):
            self.name = name
            self.robustness = robustness

    robustness = []
    robustness.append(robustnessMetric("Maximin", maximin.calc(performance)))
    robustness.append(robustnessMetric("Maximax", maximax.calc(performance)))
    robustness.append(robustnessMetric("Optimism-Pessimism", optimism_pessimism.calc(performance)))
    robustness.append(robustnessMetric("Principle of Insufficient Reason", insufficient_reason.calc(performance)))
    robustness.append(robustnessMetric("Starr's Domain Criterion", starrs_domain.calc(performance, 0.95)))
    
    return robustness

if __name__ == "__main__":
    performance = [[0.7, 0.8, 0.9], [0.8, 0.9, 1.0]]
    robustness = calc_all(performance)
    for metric in robustness:
        print(metric.name, metric.robustness)