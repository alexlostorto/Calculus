import matplotlib.pyplot as plt

# Input any x or y coordinates here
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [6, 18, 22, 18, 26, 22, 26, 24, 28, 26, 34]

# How many sections to split the graph into
splits = 5


def main():
    if not (len(x) == len(y)):
        print("Amount of x and y values is not equal")
        return

    if not (len(x) >= 2 and len(y) >= 2):
        print("Must have at least 2 coordinates")
        return

    # Gets gradient and y-intercept for each line
    def getEquations():
        # Using equation y=mx+c
        counter = 1
        m = []
        c = []
        while counter <= len(x)-1:
            yDif = y[counter] - y[counter - 1]
            xDif = x[counter] - x[counter - 1]
            grad = yDif / xDif
            yIntercept = y[counter] - x[counter] * grad

            m.append(grad)
            c.append(yIntercept)

            counter += 1

        return m, c

    # Gets x-coords for each split
    def getSplits():
        interval = (x[-1] - x[0]) / splits
        x1 = [x[0]]
        for i in range(splits):
            xCoord = x[0] + interval * (i+1)
            x1.append(xCoord)

        return x1

    # Gets y-coord of the intersection for each vertical line split
    def getIntersections():
        # Using equation y=mx+c
        counter = 1
        equation = 1
        y1 = [y[0]]
        while counter <= splits-1:
            while x1[counter] >= x[equation]:
                equation += 1
            gradient = m[equation-1]
            yIntercept = c[equation-1]
            xCoord = x1[counter]
            # print(gradient, yIntercept, xCoord)

            yCoord = gradient * xCoord + yIntercept
            y1.append(yCoord)

            counter += 1
        y1.append(y[-1])

        return y1

    m, c = getEquations()
    x1 = getSplits()
    y1 = getIntersections()

    # for i in range(len(m)):
    #     print(f"y = {m[i]}x + {c[i]}")

    def method1():
        # Using equation (y1+y2)*(x2-x1)/2
        area1 = 0
        for i in range(len(m)):
            area1 += (y[i]+y[i+1]) * (x[i+1]-x[i]) / 2

        return area1

    def method2():
        # Using equation x/2n(2Σy-(y[0]+y[-1]))
        area2 = ((x[-1]-x[0])/(2*splits)) * (2*sum(y1)-(y1[0]+y[-1]))

        return area2

    area1 = method1()
    area2 = method2()

    print(area1, area2)

    plt.plot(x, y, color='orange', linestyle='solid', label='Original')
    plt.vlines(x=x1, ymin=0, ymax=y1, color='black', linestyle='dashed',
               label='splits')
    plt.xlabel('Time')
    plt.ylabel('Velocity')
    plt.title('Velocity-Time Graph')

    plt.show()


if __name__ == '__main__':
    main()
