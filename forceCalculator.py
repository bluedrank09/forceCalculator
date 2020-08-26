import matplotlib.pyplot as plt
from matplotlib import legend

def drawGraph(xNumbers, yNumbers):
    figure = plt.figure()

    graph = figure.add_subplot(111)

    graph.plot(xNumbers, yNumbers, marker = 'o')
    graph.set_xlabel('Distance in meters')
    graph.set_ylabel('Gravitational force in newtons')

    graph.legend(['Force'])
    plt.show()

def generateForceList(massOne, massTwo):
    forceList = []
    gConstant = 6.674*(10**-11)
    
    rangeForForce = range(100,1001,50)

    for distance in rangeForForce:
        finalForce = gConstant * (massOne*massTwo) / (distance**2)
        forceList.append(finalForce)

    drawGraph(rangeForForce, forceList)

if __name__ == "__main__":
    try:
        massOne = int(input(f"Give me the mass of object one : "))
        massTwo = int(input(f"Give me the mass of object two : "))
        generateForceList(massOne, massTwo)

    except Exception as error:
        print(error)
    
    finally:
        print(f':)')