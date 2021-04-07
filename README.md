# Perturbation experiments

## Introduction
This repository contains perturbation experiments done by the hardware security
lab of the ANSSI. It is meant to allow the hardware security community to have
access to the results published by the agency.

## Maintener
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

