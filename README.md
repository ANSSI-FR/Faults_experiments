# Perturbation experiments

## Archiving

This project is not maintained anymore and has been archived on September 18th, 2023. No further work is expected to happen here.

## Introduction
This repository contains perturbation experiments done by the hardware security
lab of the ANSSI. It is meant to allow the hardware security community to have
access to the results published by the agency.

## Maintainer
- Thomas Trouchkine (thomas.trouchkine@ssi.gouv.fr)

## Copyright and license

Copyright ANSSI (2017-2021)

This software is licensed under MIT license. See LICENSE file in the root folder of the project.

## Authors
- Thomas Trouchkine (thomas.trouchkine@ssi.gouv.fr)

## Organization
The results are stored in two directories:
- the `manips` directory contains the data as gathered after a perturbation
  campaign. It consists in `.csv` files, each line of these files represents a
  perturbation and stores all the relevant parameters used to set up the
  perturbation.
- the `parameters` directory contains the parameters needed for doing the
  analysis of the experiments. It consits in Python files instantiating a
  dictionary with the parameters.

The name of the manips files and their associated parameters are matching and
follow this nomenclature:
```sh
$COMPONENT_$TARGET_$IV
```
where:
- `$COMPONENT` refers to the tested component
- `$TARGET` refers to the test program, in the case of an algorithm, the name of
  the algorithm is given (for instance AES). In the case it refers to an
  instruction the test program is the repetition of this instruction as defined
  in [this article](https://thomas.trouchkine.com/assets/pdf/wistp_2019.pdf).
  The target `movallreg` refers to a test program composed of `mov` instruction
  alternating in all registers such as:
  ```asm
  mov r0,r0
  mov r1,r1
  mov r2,r2
  ```
- `$IV` refers to the initial values used for the registers. They may differ
  regarding the target, for instance, `iv1` does not refers to the same values
  if it is associated with an AES algorithm or a single instruction test
  program. The initial values are all defined in the parameters files.
  
## Analyzing the experiments
You can either used your own tools to parse the `.csv` files with the given
parameters or you can used the ANSSI fault analyzer tool which purpose is to
analyze these results.

### Using the ANSSI tool for analyzing the results

1. Clone the fault experiments and fault analyzer repositories:
``` sh
git clone git@github.com:ANSSI-FR/Faults_experiments.git
git clone git@github.com:ANSSI-FR/Faults_analyzer.git
```

2. Go to the fault analyzer directory and change the `"main_dir"` parameter of
   the `config.py` file to `../Faults_experiments`:
``` sh
cd Faults_analyzer
# Edit config.py
```

``` python
CONFIG = {
    "main_dir": "../Faults_experiments/", # <- edit this line
    "results_dir": "results/",
    "manips_dir": "manips/",
    "parameters_dir": "parameters/",
    "tikz_dir": "tikz/"
}
```

3. Initialize the fault analyzer

``` sh
# In Faults_analyzer/
make init
```

4. Run the fault analyzer

``` sh
# In Faults_analyzer/
make run
```

Here you are ! You can now analyze the experiments !

For more information on how to use the fault analyzer, see [its
documentation](https://anssi-fr.github.io/Faults_analyzer/).

## Available experiments
- `bcm2711b0_orrR5_iv5_laser_20x_4v_20ns_carto_core`: in this experiment we used
  a laser to perturb a bcm2711b0 die. We tested several positions over the cores
  of the circuit.
- `bcm2837_AES_iv1_em`: in these experiments, we used EMFIs to perturb the
  execution of the OpenSSL AES running on a bcm2837 (on a Raspberry Pi 3 board).
- `bcm2837_[andR8,movallreg,orrR5]_iv[1,3,4]`:in these experiments, we used EMFI
  to perturb the execution of simple test programs over Linux on a bcm2837 with
  various initial values for the registers.
- `bcm2837_orrx3x3_iv1_EM_fix`: in this experiment, we used EMFI to perturb the
  execution of a simple test program bare metal on a bcm2837.
- `intelcorei3_mov/orRbx_iv1_em_fix`: in these experiments, we used EMFI to
  perturb the execution of simple test programs over Linux on an Intel Core i3
  processor.
