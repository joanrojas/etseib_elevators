# Optimisation and Simulation - Elevator's modelling

For optimisation&simulation class. It consists of an algorithm I designed together with a classmate to simulate 
the elevator system at my university. 

### 1. Brief files description

*_cua.py_* is stores the queue formed at the lowest floor. 

*_ascensor.py_* manages the itinierary of the elevator. For instance, it updates the route when a person comes in and also when the person goes off.

*_aleatori.py_* describes the entry of the system. A group of N people comes in, each of which wishes to go to floor K, where both N and K are uniformly distributed. It also returns time t, which is the time until the next income, typically exponentially distributed.

*_algorisme.py_* is the algorithm itself. It performs all necessary tasks such as _closing doors_, _opening doors_. It also prints the current state of the system.

The currently installed elevator system consists of 4 elevators working in pairs. 2 of them only go to even floors and the other 2 going to odd floors. 
We designed the algorithm so that we could test other systems, such as two working for top floors and the other 2 for lower floors. Depending on what you want to simulate, you state "mode1" or "mode" in *_algorisme.py_*.


