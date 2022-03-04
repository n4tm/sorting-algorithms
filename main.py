from utils.ISortingAlgorithm import ISortingAlgorithm
from algorithms.SortingAlgorithms import *
from random import shuffle

test_data = [3, 6, 2, 23, 93, -2, -6, 2, 0, 2, 5, 0, 65, -234, 123, 24, 54]

def test_sorting_algorithm(algorithm: ISortingAlgorithm) -> None:
  print(f'--- {algorithm.__class__.__name__} ---')
  shuffle(test_data)
  print(f'shuffled data: {test_data}')
  algorithm.sort(test_data)
  print(f'sorted data: {test_data}\n')

if __name__ == '__main__':
  for algorithm in [bubbleSort, selectionSort, insertionSort, mergeSort, quickSort]: 
    test_sorting_algorithm(algorithm)