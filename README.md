# Disjoint-Sets Implementation Comparison

This repository contains the code and report for comparing two different methods for implementing data structures for disjoint sets: 
- Implementation based on linked lists
- Implementation based on rooted trees

## Introduction

In this project, I compare the efficiency of the above implementations by testing disjoint sets based algorithms for finding connected components in non-oriented graphs with different sizes and densities.

## Contents

- [Code](#code)
- [Report](#report)
- [Test Cases and Results](#test-cases-and-results)
- [Conclusion](#conclusion)

## Code

The code is organized into the following modules:
- `linked_list_disjoint_set.py`: Handles the linked list representation of disjoint sets.
- `disjoint_set_forest.py`: Handles the rooted trees representation of disjoint sets.
- `graph.py`: Manages the graph data structure and provides methods for generating graphs.
- `test.py`: Provides methods for testing the efficiency of different implementations of the connected-components algorithm.
- `main.py`: The main executable program where tests are run.

## Report

The report provides a theoretical analysis of the problem, documentation of the code, details of the tests conducted, and analysis of the results. The report is available in the root directory as `report.pdf`.

## Test Cases and Results

I conducted a total of six tests, three of which compared all implementations and the other three compared only linked lists with weighted union to rooted trees. Each test case evaluated the efficiency of the implementations on graphs with varying sizes and densities. Detailed test cases and results can be found in the report.

## Conclusion

The conclusion section of the report summarizes the findings of the project and provides insights into the efficiency of different disjoint-set implementations in solving the problem of finding connected components in non-oriented graphs.

