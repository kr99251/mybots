import numpy

amplitudeBackLeg = numpy.pi
frequencyBackLeg = 10
phaseOffsetBackLeg = 0

amplitudeFrontLeg = numpy.pi
frequencyFrontLeg = 10
phaseOffsetFrontLeg = 0

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

targetAngles = numpy.linspace(0, 2*numpy.pi, 1000)