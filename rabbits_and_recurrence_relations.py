def fib(n: int, k:int) -> int:
    """fibonacci sequence that computes the 
    total number of rabbits present after n months

    fn = fn - 1 + fn-2 * k

    where fn - 1 is all rabbits a month prior
    fn - 2 is all rabbits two months prior (able to reproduce)

    :param k: each pair produce k number of pairs per month
    :param n: number of months in the simulation
    :return: number of pairs at the end of the simulation
    """
    
    # Base case
    if n == 2 or n == 1:
        return 1
    
    # Recursive case
    return fib(n - 1, k) + fib(n-2, k) * k

print(fib(5, 3))
with open('rosalind_fib (1).txt', 'r') as f:

    data = f.readline()

    list_of_data = data.strip().split(' ')
    print(fib(int(list_of_data[0]), int(list_of_data[1])))
