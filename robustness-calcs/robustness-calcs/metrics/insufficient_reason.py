def calc(performance):
    """Returns the maximax (optimistic) metric for a set of solutions

    Metric obtained from:
    Laplace, P. S. and Simon, P. (1951)
        'A philosophical essay on probabilities, translated from the 6th French edition by Frederick Wilson Truscott and Frederick Lincoln Emory'. Dover Publications (New York, 1951).

    'performance' is a 2D array of the performance metric used to
        evaluate each solution in each scenario
        dimension 1 is the solution index
        dimension 2 is the scenario index

    returns a 1D array of the robustness for each solution using the Principle of Insufficient Reason
    """

    # Calculate the average performance across scenarios
    robustness = [sum(solution)/len(solution) for solution in performance]
    
    return robustness