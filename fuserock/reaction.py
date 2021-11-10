from math import pi, sqrt


e_charge = 1.6021773E-19 #C
u        = 1.6605402E-27 #kg
c        = 2.99792458    #m/s
epsilon0 = 8.85419E-12   #F/m
r0       = 1.40          #fm

class Reaction:
    
    def __init__(self, E, beamA, beamZ, targA, targZ):
        self.beamE      = E                                                                                          #Beam Energy (lab) in MeV

        self.beamA      = beamA                                                                                      #beam A
        self.beamZ      = beamZ                                                                                      #beam Z

        self.targA      = targA                                                                                      #target A
        self.targZ      = targZ                                                                                      #target Z        
                                                                                          
        self.compA      = self.beamA + self.targA                                                                    #compound A
        self.compZ      = self.beamZ + self.targZ                                                                    #compound Z

        self.beamR      = r0*self.beamA**(-1/3)                                                                      #beam radius in fm                        
        self.targR      = r0*self.targA**(-1/3)                                                                      #target radius in fm
        self.compR      = r0*self.compA**(-1/3)                                                                      #compound radius in fm
                        
        self.coulombB   = ((1E9*e_charge)/(4*pi*epsilon0))*(self.targZ*self.beamZ)/(self.targR + self.beamR)         #Coulomb Barrier in MeV
        self.projCoul   = self.coulombB*self.compA/self.targA                                                        #Projectile K to surpass Coulomb Barrier in MeV
                        
        self.targE      = 4*self.beamE*self.targA*self.beamA/(self.compA)**2                                         #scattered target energy in MeV
        self.compE      = self.beamE*self.beamA/(self.compA)                                                         #compound energy in MeV
                        
        self.beamV      = sqrt(2E6*e_charge*self.beamE/(self.beamA*u))                                               #beam velocity in m/s
        self.targV      = sqrt(2E6*e_charge*self.targE/(self.targA*u))                                               #scattered target velocity in m/s
        self.compV      = self.beamV*beamA/(self.compA)                                                              #compound nucleus velocity in m/s

        self.ratio      = 0
        if self.compV != 0:
            self.ratio      = self.targV/self.compV                                                                  #ratio of scattered target to compound velocities
        self.grazing    = self.Grazing(self.beamE, self.beamA, self.beamZ, self.targA, self.targZ)                   #grazing angle

    def Grazing(_, beamE, beamA, beamZ, targA, targZ):
        #outputs grazing angle in degrees
        T            = beamE/beamA
        Rb           = 1.28*beamA**(1/3) -0.76+0.8*beamA**(-1/3)
        Rt           = 1.28*targA**(1/3) -0.76+0.8*targA**(-1/3)
        
        Cb           = Rb*(1-1/(Rb**2))
        Ct           = Rt*(1-1/(Rt**2))
        Rint         = Cb + Ct +4.49 - (Cb + Ct)/6.35
        grazing      = 2.88*targZ*beamZ*(931.5 + T)/Rint * 1/beamA * 1/(T**2 + 1863*T)

        return grazing