"""
Plots behavior of jet power versus spin
Includes both the "disk model" and the Blandford-Znajek.
See Nemmen et al. 2007, MNRAS, 377 1652, "Models for jet power in
elliptical galaxies: evidence for rapidly spinning black holes".

Notation: 
  - variables named like M (uppercase) which conflict with preexisting 
    variables like m are represented as M_ .
  - the dimensionless spin (a/M) is given by "a" (not "j", as in the paper)

Author: Rodrigo Nemmen
E-mail: rodrigo.nemmen nasa.gov  

If you have any suggestions or find any bug in this code, please let me know.
"""
import numpy, pylab

# Input model parameters
f=1. 
m=1e9	# black hole mass [solar masses]
mdotbondi=0.001	# in Eddington units
alpha=0.3
eps=1.	# fraction of mass that reaches the jet formation region
f_adaf=1	# advection parameter

# Definition of constants in CGS units
c=2.99792458e10	# speed of light
G_=.6673e-7	# gravitational constant
Msun=.199e34	# solar mass

# General definitions
M_=m*Msun
RS=2*G_*M_/c**2	# Schwarzschild radius
mdot=eps*mdotbondi	# accr. rate that that reaches the jet formation region
lumedd=1.3e38*m	# Eddington luminosity
mdotedd=lumedd/(0.1*c**2)	# Eddington accretion rate in CGS units, assuming 10% radiative efficiency

# Hawley et al. (1995), determination of beta from alpha.
# See Narayan et al. (1998) (Sgr A* paper).
# Assumes P_mag = B^2/8*Pi
c_mri=0.55 
betaAdaf=1.-alpha/c_mri

# Calculation of gamma (adiabatic index) from Esin (1997)
gamma=(8.-3.*betaAdaf)/(6.-3.*betaAdaf)

# The quantities below come from Narayan & Yi (1995)
eps_=1./f_adaf*(5./3.-gamma)/(gamma-1.)	# epsilon'
gg=numpy.sqrt(1.+18.*alpha**2/(5.+2.*eps_)**2)-1.	# g(alpha,epsilon')
c1=(5.+2.*eps_)/(3.*alpha**2)*gg
c3=2.*(5.+2.*eps_)/(9.*alpha**2)*gg
c2=numpy.sqrt(eps_*c3)

points=100
a_i,a_f = 0.01, 1.	# initial and final spins
spin=numpy.linspace(a_i, a_f, points)	# array of black hole spins
a=spin	# pointer for spin
  
# radius of the event horizon
RH=G_/c**2*M_*(1+numpy.sqrt(1-a**2))
  
# ISCO (or marginally stable orbit)
A1=1+(1-a**2)**(1./3.)*((1+a)**(1./3.)+(1-a)**(1./3.))
A2=numpy.sqrt(3*a**2+A1**2)
Risco=G_/c**2*M_*(3+A2-numpy.sqrt((3-A1)*(3+A1+2*A2)))
R0_=1.0*Risco	# characteristic radius
r0=R0_/RS
  
# angular velocity of metric
omega=2*a*(G_/c**2*M_)**2/( (a*G_/c**2*M_)**2*(R0_+RS)+R0_**3  )*c
  
# Scale height (NY95)
H=numpy.sqrt(2.5*c3)*R0_
  
# angular velocity of the disk relative to the metric
Omega_disk=7.19e4*c2*1./m*r0**(-3./2.)
  
# magnetic field-enhancing shear in the Kerr metric
g=1+omega/Omega_disk  
  
# azimuthal magnetic field (NY95)
# Radial magnetic field threading the hole. Assumed to be
# the same as the one threading the ISCO, including the
# field-enhancing shear due to the Kerr metric.
B=6.55e8/numpy.sqrt(alpha)*numpy.sqrt(1-betaAdaf)/numpy.sqrt(c1)*c3**(1./4.)/numpy.sqrt(m)*numpy.sqrt(mdot)*r0**(-5./4.)
B=g*B	# field-enhancing
  
# jet power from the BZ effect
Pjet_bz=1./32.*1./4.*B**2*RH**2*c*a**2
  
# jet power from the "disk" model
Pjet=B**2*H**2*R0_**2*(omega+Omega_disk)**2/(32.*c)

# Plot ("disk" model - solid line, BZ model - dashed line)
pylab.clf()
pylab.plot(spin, numpy.log10(Pjet), linewidth=2, label='Hybrid')
pylab.plot(spin, numpy.log10(Pjet_bz),'--', linewidth=2, label='BZ')
pylab.xlabel('$j = a/M$')
pylab.ylabel('$\log (P_{\\rm jet} \ [{\\rm erg \ s}^{-1}])$')
pylab.legend(loc='lower right')
pylab.minorticks_on()

# Adds second Y axis
ax1=pylab.subplot(111)
ax2=pylab.twinx()
y=ax1.set_ylim()	# retrieves the lower and upper values of Pjet plotted in the left Y axis
ax2.set_ylim(10**y[0]/(mdot*mdotedd*c**2),10**y[-1]/(mdot*mdotedd*c**2))
ax2.set_yscale('log')
pylab.ylabel('$\eta_{\\rm jet}=P_{\\rm jet}/(\dot{M}_{\\rm ms} c^2)$')

pylab.show()
pylab.draw()

