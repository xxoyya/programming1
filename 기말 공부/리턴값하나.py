def std_dev(*args):
    def find_mean():
        mean = sum(args)/len(args)
        return mean

    def variance(mean):
        squared_deviation = 0
        for arg in args:
            squared_deviation += (arg - mean)**2
            var = squared_deviation / len(args)
            return var

    v = variance(find_mean())
    return v**0.5

print(std_dev(1,2,3,4,10,7,8,9))
