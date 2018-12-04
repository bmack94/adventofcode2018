from pprint import pprint
import sys
path='./claims.txt'
txt=open(path, 'r')

claims = []
multible_claims = []
for row in txt.readlines():
  #pprint(row)
  startX = int(row.split(' ')[2].split(',')[0])
  startY = int(row.split(' ')[2].split(',')[1].replace(':', ''))
  stepsX = int(row.split(' ')[3].split('x')[0])
  stepsY = int(row.split(' ')[3].split('x')[1].replace('\n', ''))
  # pprint(startX)
  # pprint(startY)
  # pprint(stepsX)
  # pprint(stepsY)
  for x in range(1, stepsX+1):
    stepX = int(startX+x)
    for y in range(1, stepsY+1):
      stepY = int(startY+y)
      location = str(stepX) + ' x ' + str(stepY)
      if location in claims:
        if location not in multible_claims:
          #pprint(location + 'is claimed')
          multible_claims.append(location)
      claims.append(location)

pprint(len(multible_claims))
