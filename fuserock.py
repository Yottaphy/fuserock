import argparse
from .reaction import Reaction
from .tableprinting import PrintTableHead, PrintTableContents

E_Bi = [391.15, 342.26, 325.96, 309.66]
E_U  = [410.15, 358.88, 341.79, 324.70]

def get_parser():

    parser = argparse.ArgumentParser(description = 'FUSion-Evaporation ReactiOn Calculator of Kinematics')

    parser.add_argument('-E',
                        dest='energy',
                        type=float,
                        help='Beam energy in MeV')

    parser.add_argument('-Escan', '--scan',
                        nargs=3,
                        metavar=('energyMin','energyMax', 'energyStep'),
                        type=int,
                        help='Minimum, maximum and scan step beam energy in MeV for an energy scan. Is overriden by -E')
    
    parser.add_argument('-b', '--beam', '-p', '--projectile',
                        nargs=2,
                        metavar=('beamA','beamZ'),
                        type=int,
                        required=True,
                        help='A and Z of the beam particle')

    parser.add_argument('-t', '--target',
                        nargs=2,
                        metavar=('targA','targZ'),
                        type=int,
                        required=True,
                        help='A and Z of the target particle')

    
    args = parser.parse_args()
    return args, parser

def main():
    args, parser = get_parser()
    if args.energy is None and args.energyMin*args.energyMax*args.energyStep is None:
        print('Error. No single energy or scan range has been defined. Try again.')
        exit()
    
    PrintTableHead(args.beamA, args.beamZ, args.targA, args.targZ)
    if args.energy is not None:
        reac = Reaction(args.energy, args.beamA, args.beamZ, args.targA, args.targZ)
        PrintTableContents(reac)
    else:
        for energy in range(args.energyMin, args.energyMax, args.energyStep):
            reac = Reaction(energy, args.beamA, args.beamZ, args.targA, args.targZ)
            PrintTableContents(reac)

if __name__ == '__main__':
    main()