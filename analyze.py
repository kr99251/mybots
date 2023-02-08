import numpy
import matplotlib.pyplot

# backLegSensorValues = numpy.load("data/backLegSensorVals.npy")
# frontLegSensorValues = numpy.load("data/frontLegSensorVals.npy")
# print(backLegSensorValues)
# matplotlib.pyplot.plot(backLegSensorValues, label='back leg', linewidth=3)
# matplotlib.pyplot.plot(frontLegSensorValues, label = 'front leg', linewidth = 1)

targetAngles = numpy.load("data/targetAngles.npy")
targetAngles2 = numpy.load("data/targetAngles2.npy")
matplotlib.pyplot.plot(targetAngles, label = 'backLeg Target Angles', linewidth = 3)
matplotlib.pyplot.plot(targetAngles2, label = 'frontLeg Target Angles', linewidth = 1)

matplotlib.pyplot.legend()
matplotlib.pyplot.show()