
# Art using Cellular Atomaton

This project uses a brach of maths Cyclic Cellular Atomaton to create patterns.

# Description
In this Cyclic Cellular Atomaton, each cell remains unchanged until some neighboring cell has a modular value exactly one unit larger than that of the cell itself.
It is a subset of Cellular Atomaton developed by **David Griffeath** and some others. In this project I mainly used **Codd's Cellular Automaton.**
### Rules
As with any cellular automaton, the cyclic cellular automaton consists of a regular grid of cells in one or more dimensions
- The cells can take on any of n states, ranging from 0 to n − 1.
- The first generation starts out with random states in each of the cells.
- In each subsequent generation, if a cell has a neighboring cell whose value is the successor of the cell's value, the cell is "consumed" and takes on the succeeding value. (Note that 0 is the successor of n-1; see also modular arithmetic.) More general forms of this type of rule also include a threshold parameter, and only allow a cell to be consumed when the number of neighbors with the successor value exceeds this threshold.
## Demo

![Image](https://github.com/Sarath191181208/Art_using_cellularAtomaton/blob/master/images/Screenshot%20.png?raw=True)

  
## References
Codd's Cellular Automaton Wikipedia : https://en.wikipedia.org/wiki/Codd's_cellular_automaton
Cyclic Cellular Automaton Wikipedia : https://en.wikipedia.org/wiki/Cyclic_cellular_automaton
## Run Locally

Clone the project

```bash
  git clone https://github.com/Sarath191181208/Art_using_cellularAtomaton.git
```

Go to the project directory

```bash
  cd Art_using_cellularAtomaton
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the project Locally

```bash
  python main.py
```

  
## Requirements

- python `make sure to add to path`
- pygame `pip install pygame`
- numpy `pip install numpy`
- numba `pip install numba`

  