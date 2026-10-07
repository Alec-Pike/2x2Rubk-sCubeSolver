# 2x2 Rubik's Cube Solver

A small Python project for representing and solving a 2x2 Rubik's Cube. The repository is intended to model cube states, generate moves, and find a valid solution for scrambled configurations.

The project also includes a notebook report at `experiment.ipynb`, which documents the implementation and benchmark tests.

## Requirements

- Python 3.9 or newer
- pip
- Jupyter Notebook (if you want to run the report notebook)

there is no `requirements.txt`, so the only thing you need to install in Jupyter Notebook

```bash
pip install notebook
```

## Running the solver

From the project root, run the `main.py`. This script will run the three solution algorithms on whatever cube state you input. 

```bash
python main.py
```

`solver.py` and `pocketcube.py` also have brief test demonstrations if you run them directly.

```bash
python solver.py

python pocketcube.py
```

## Running the benchmark/report notebook

Open the notebook in Jupyter:

```bash
jupyter notebook experiment.ipynb
```

This notebook is contains the project report and benchmark results for evaluating the solver's performance.

## Project structure

Files in this project include:

- `main.py` — entry point for testing the cube solver
- `solver.py` — handling class for the cube and solving 
- `pocketcube.py` — cube representation and move logic
- `algorithms.py` — specific logic for search algorithms
- `experiment.ipynb` — report and benchmark tests

## Acknowledgements

The code for this project was directly based on a project by Tim, which can be found here:
https://tim.id.au/limejuice/generating-the-full-list-of-valid-states-of-a-2x2-rubiks-cube/

