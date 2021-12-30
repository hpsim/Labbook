# OGL Labbook
A lab book for OGL benchmark data

This repository holds data from OGL benchmark and simulation runs and a set of post-processing scripts to analyse and visualise the data

## Goals
  1. Full documentation of a simulation project
  2. Automate recuirring tasks like plotting of results

## Requirements

 - Non intrusive work flow, comparable to git for example.
 - Human friendly file formats, eg. json

## CB/CS Aspects
Parts of this project can be seen as continuous benchmarking (CB), i.e. running a constant set of benchmark cases as the development of OGL progresses. However, a second part of this project could be seen as continuous simulation (CS), here simulation with setups different from the CB setup are performed. 

 - CB: Simulations with a set of fixed input parameters, with the aim to document changes in the performance of the simulation software for different versions of which;
 - CS: Simulations using a larger set of input parameters, to investigate changes in the simulation results for a fixed version of the simulation software.

## Terminology

 - **Project**
 - **Campaign**, a set of measurements
 - **Measurement**, one or multiple simulations with well defined input and results 
 - **Journal**, a log of measurements
 - **Input**
 - **Result**
 - **Pipeline** A set of program executions to get from the simulation input to a result


## Thoughts on Reproducibility
Reproducibility is one of the fundamental aspects of science. However, even if a deterministic pipeline is assumed, reaching full reproducibility is a major challenge for simulations. 

  - Setting up the same software or hardware enviroment might be impossible 
  - Reproducing a full project or even a measurement campaign might be too expensive
  - Requiring identical results might be overly restrictive, if results for example contain time stamps.


## Migration from OGL_DATA

## Structure
