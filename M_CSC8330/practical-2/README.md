# Practical 2 Assessment

## Overview:
This application is designed to simulate a basic ecosystem containing a simple food chain. 

## Features:
First iteration of the application is meant to run wihtout input. 3 colours (green, blue, red) represent 
3 members of the chain (producer, herbivore, carnivour). *Producers* (green) are stationary and will multiply 
over time simulating population growth, *herbivores* (blue) move around and consume *producers* (green) when in 
contact, but will die out if no *producers* are available for comsumption. *Carnivores* (red) move around and 
consume *herbivores* (blue) when in contact, but will also die out if no *herbivores* are available for 
cunsumption.

## Running the application:
To run the simulation, run `P2_foodchain_main.py` from console.

## ToDo:
Add options to modify starting number of each organism.
Add options to change length of the food chain.
Add options to increase number of food chains.