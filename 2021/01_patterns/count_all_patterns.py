pegs = {
    1: {3:2, 7:4, 9:5},
    2: {8:5},
    3: {1:2, 7:5, 9:6},
    4: {6:5},
    5: {},
    6: {4:5},
    7: {1:4, 3:5, 9:8},
    8: {2:5},
    9: {1:5, 3:6, 7:8}
}

def next_steps(path):
    return (n for n in range(1,10) if (not path or n not in path and 
                                       (n not in pegs[path[-1]] 
                                        or pegs[path[-1]][n] in path)))

def patterns(path, steps):
    if steps == 0:
        
        return 1
    return sum(patterns(path+[n], steps-1) for n in next_steps(path))

print(patterns([], 9, verbose=True))