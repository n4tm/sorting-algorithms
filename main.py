from utils.ComparisonChart import ComparisonChart
from utils.SortingAlgorithm import SortingAlgorithm
from SortingAlgorithms import *
from random import randint

if __name__ == '__main__':
  # Generates a list of size x filled with random integers between -y and y
  random_data_with_size: list[int] = lambda x, y : [randint(-y, y) for _ in range(x)]

  # Generates a list of 6 lists of sizes 10, 10², 10³, 10⁴, 10⁵, 10⁶, respectively. 
  # Each one filled with random integers between -1000 and 1000.
  data_list: list[list[int]] = [random_data_with_size(pow(10, x), 1000) for x in range(1, 4)]

  algorithms: list[SortingAlgorithm] = [bubbleSort, selectionSort, insertionSort, mergeSort]

  ComparisonChart.sort_data_and_plot_comparisons(data_list, algorithms)
  ComparisonChart.show()