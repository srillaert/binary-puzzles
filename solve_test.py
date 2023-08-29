from solve import *
from pathlib import Path

def test_matrix_empty_count():
	matrix = [["0", "."], [".", "0"]]
	assert(matrix_empty_count(matrix) == 2)

def test_solve_puzzle():
	directory = Path('./puzzles/')
	for file_path in directory.iterdir():
		if file_path.is_file():
			solution = solve_puzzle(file_path.absolute())
			assert(is_solved_puzzle(solution))
