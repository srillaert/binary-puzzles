#!/bin/bash -e
gcc -o solve_test solve_test.c -lm
./solve_test
gcc -o solve solve.c -lm
