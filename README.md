# adafjet

## Overview

A Python script to estimate the jet power for advection-dominated accretion flows (ADAFs) around a spinning black hole.** 

The model incorporates relativistic effects in a pseudo-Newtonian fashion and is analytic. The model is described in the paper
> Nemmen, R. S., et al. 2007, Monthly Notices of the Royal Astronomical Society, 377, 1652
> [[published version here (paywall)](http://adsabs.harvard.edu/abs/2007MNRAS.377.1652N), [free version here](http://arxiv.org/abs/astro-ph/0612392)]


It reproduces approximately the jetpower vs spin dependency inferred from the GRMHD simulations of [McKinney (2005)](http://labs.adsabs.harvard.edu/ui/abs/2005ApJ...630L...5M), [Hawley & Krolik (2006)](http://labs.adsabs.harvard.edu/ui/abs/2006ApJ...641..103H) and [Tchekhovskoy et al. (2010)](http://labs.adsabs.harvard.edu/ui/abs/2010ApJ...711...50T). 

# Usage
 
Change the input parameters such as *m*, *eps* and *alpha* and run the script:

    run jetpower
(in IPython for example).

It should produce a plot of the jet power (and power efficiency) vs black hole spin.

# Credit

Copyright (c) 2012, [Rodrigo Nemmen](http://asd.gsfc.nasa.gov/Rodrigo.Nemmen/Rodrigo_Nemmens_Homepage/Home.html).
[All rights reserved](http://opensource.org/licenses/BSD-2-Clause).

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.