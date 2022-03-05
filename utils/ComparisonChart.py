import matplotlib.pyplot as plt
from time import perf_counter
from utils.SortingAlgorithm import SortingAlgorithm

class ComparisonChart:
  plt.xlabel('List Length')
  plt.ylabel('Time Complexity')
  plt.xscale("log")
  plt.yscale("log")
  plt.grid()

  @staticmethod
  def sort_data_and_plot_comparisons(data: list[list[int]], algorithms: list[SortingAlgorithm]) -> None:
    plt.xlim(len(data[0]), len(data[len(data)-1]))
    for algorithm in algorithms:
      times: list[float] = list()
      data_sizes: list[int] = list()
      for d in data:
        start = perf_counter()
        algorithm.sort(d)
        end = perf_counter()
        data_sizes.append(len(d))
        times.append(end-start)
      plt.plot(data_sizes, times, label=''.join(map(lambda x: x if x.islower() else " " + x, algorithm.__class__.__name__)))
    plt.legend()

  @staticmethod
  def show() -> None:
    plt.show()
