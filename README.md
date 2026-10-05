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

From the project root, run the `main.py`. This is a short test script demonstating the functionality of the solver. 

```bash
python main.py
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
