# FUSion-Evaporation ReactiOn Calculator of Kinematics (Fuserock) #

Fuserock is a simple, terminal based calculator of fusion-evaporation nuclear reaction kinematics. It provides information on beam, target and compound nucleus total kinetic energies and velocities. It has the capability of scanning in energies as well as working for a single bombarding energy. 

## Setup
### Pre-requisites
The `fuserock` package is a python package. It requires Python3 to be installed and `pip` to be up to date. It also requires the `argparse` package to be installed.

### Install
You can clone the package's `git` repository:

>`$ git clone https://github.com/Yottaphy/fuserock.git`

and then enter the directory that was created and install

> `$ cd fuserock`\
> `$ pip install .`

## Usage
Once installed, fuserock can be used directly from the terminal. Some flags have to be included for the calculation to take place. 
> `$ fuserock -e bE -b bA bZ -t tA tZ`

or, equivalently:

> `$ fuserock --energy bE --beam bA bZ --target tA tZ`

will calculate the reaction of a `bE` MeV beam with mass number `bA` and proton number `bZ` impinging on a target with with mass number `tA` and proton number `tZ`.

For an energy scan, use: 
> `$ fuserock -s bEmin bEmax bEstep -b bA bZ -t tA tZ`

or, equivalently:

> `$ fuserock --scan bEmin bEmax bEstep --beam bA bZ --target tA tZ`

where the same calculations as above will happen, but for energies ranging from `bEmin` and `bEmax`, in steps of `bEstep`.

### Output

The output should show the reaction used and a table containing all of the energy and velocity data mentioned above. The formatting of the table may be displayed wrongly due to terminal size. To output the results into a txt file, simply do:

> `$ fuserock [...] > outputname.txt`

where `[...]` are the relevant flags and `outputname.txt` is the output file name, saved at the directory from which you launch Fuserock.