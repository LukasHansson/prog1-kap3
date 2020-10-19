g = float(input('Hur mycket ringer du per månad i minuter? '))
if g < 33:
    print('Du bör ha kontant')
if g > 34 and  g< 66:
    print('Du borde ha normal')
if g > 67:
    print('Du borde ha extra plus')