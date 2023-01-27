import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorVals.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorVals.npy")
print(backLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues, label='back leg', linewidth=3)
matplotlib.pyplot.plot(frontLegSensorValues, label = 'front leg', linewidth = 1)

matplotlib.pyplot.legend()
matplotlib.pyplot.show()