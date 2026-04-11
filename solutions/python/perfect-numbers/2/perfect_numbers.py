def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if not isinstance(number, int) or isinstance(number,bool) or number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    divosors_sum = 0
    for divosor in range(1, number//2 + 1):
        if number % divosor == 0:
            divosors_sum+=divosor
    if divosors_sum == number:
        return "perfect"
    return "abundant" if divosors_sum > number else "deficient"
