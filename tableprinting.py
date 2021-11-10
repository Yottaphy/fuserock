from .reaction import Reaction

c = 299792458 #m/s

def PrintTableHead(projA, projZ, targA, targZ):
    print('######################################################################')
    print('             REACTION              ')
    print('Beam:\tA:', projA, '\tZ:', projZ)
    print('Target:\tA:', targA, '\tZ:', targZ)
    print('######################################################################')
    print('\n')
    print('\tBeam\t|\tScattered Target\t|\tCompound Nucleus\t|\tVelocity|\tGrazing  ')
    print('Energy [MeV]\tVelocity[m/s]\tVelocity[c]|\tEnergy [MeV]\tVelocity[m/s]\tVelocity[c]|Energy [MeV]\tVelocity[m/s]\tVelocity[c]|\tRatio|\tAngle')

def PrintTableContents(reaction):
    print(reaction.beamE, '\t', f'{reaction.beamV:.3e}', '\t', f'{reaction.beamV/c:.3e}', '\t', reaction.targE, '\t', f'{reaction.targV:.3e}', '\t', f'{reaction.targV/c:.3e}', '\t', reaction.compE, '\t', f'{reaction.compV:.3e}', '\t', f'{reaction.compV/c:.3e}', '\t',  f'{reaction.ratio:.3e}', '\t', f'{reaction.grazing:.3e}')
    