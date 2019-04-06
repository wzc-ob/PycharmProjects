def line(a,b):
    def aline(x):
        return  a*x +b
    return  aline
if __name__ == '__main__':

    line23 = line(2,3)
    line50 = line(5,0)
    print(line23(4))
    print(line50(2))