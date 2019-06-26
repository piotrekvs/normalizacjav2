roman=input("wprowadź liczba w systemie rzymskim:   ")

def rn_to_int(s):
    d = {'m': 1000, 'd': 500, 'c': 100, 'l': 50, 'x': 10, 'v': 5, 'i': 1}
    n = [d[i] for i in s.lower() if i in d]
    return sum([i if i>=n[min(j+1, len(n)-1)] else -i for j,i in enumerate(n)])

print(rn_to_int(roman))