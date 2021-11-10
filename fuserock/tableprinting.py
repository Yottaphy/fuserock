from .reaction import Reaction
from math import pi

c = 299792458 #m/s

def PrintTableHead(projA, projZ, targA, targZ):
    print('###################################')
    print('             REACTION              ')
    print('Beam:\tA:', projA, '\tZ:', projZ)
    print('Target:\tA:', targA, '\tZ:', targZ)
    print('###################################')
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('Beam\t\tBeam\t\tBeam       |\tScattered\tScattered\tScattered  |\tCompound\tCompound\tCompound   |\tVelocity   |\tGrazing')
    print('Energy [MeV]\tVelocity[m/s]\tVelocity[c]|\tEnergy [MeV]\tVelocity[m/s]\tVelocity[c]|\tEnergy [MeV]\tVelocity[m/s]\tVelocity[c]|\tRatio      |\tAngle [deg]')
    print('-------------------------------------------+-----------------------------------------------+-----------------------------------------------+---------------+-----------------')

def PrintTableContents(reaction):
    print(reaction.beamE, '\t\t', f'{reaction.beamV:.3e}', '\t', '{:.3f}'.format(round(reaction.beamV/c,3)), '    |\t  ', f'{reaction.targE:.3e}', '\t', f'{reaction.targV:.3e}', '\t', '{:.3f}'.format(round(reaction.targV/c,3)), '\t   |\t', f'{reaction.compE:.3e}', '\t', f'{reaction.compV:.3e}', '\t', '{:.3f}'.format(round(reaction.compV/c,3)), '    |\t',  '{:.3f}'.format(round(reaction.ratio,3)), '    |\t', round((reaction.grazing*180/pi)%360,2))
    #print(reaction.beamE, '\t', reaction.beamV, '\t', reaction.beamV/c, '|\t', reaction.targE, '\t', reaction.targV, '\t', reaction.targV/c, '|\t', reaction.compE, '\t', reaction.compV, '\t', reaction.compV/c, '|\t',  reaction.ratio, '|\t', reaction.grazing)
  