import maximin
import maximax

def calc(performance, alpha=0.5, maximise=True):
    """Returns the maximin (pessimistic) metric for a set of solutions

    Metric obtained from:
    Wald, A. (1950) Statistical decision functions. New York; Chapman & Hall: London.

    'performance' is a 2D array of the performance metric used to
        evaluate each solution in each scenario
        dimension 1 is the solution index
        dimension 2 is the scenario index

    'alpha' is a factor that shows what proportion of the optimism rule to use
        0 < alpha < 1

    'maximise' is a boolean value (assumed true) that is
        true  if the aim is to maximise the value of performance (e.g. profit)
        false if the aim is to minimise the value of performance (e.g. cost)

    returns a 1D array of the maximin robustness for each solution
    """

    # Get the optimistic robustness
    optimistic = maximax.calc(performance, maximise)
    
    # Get the pessimistic robustness
    pessimistic = maximin.calc(performance, maximise)

    # Combine the optimistic and pessimistic values
    robustness = []
    for solution in range(len(optimistic)):
        robustness.append(alpha * optimistic[solution] + (1 - alpha) * pessimistic[solution])

    return robustness