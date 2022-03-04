from utils.ISortingAlgorithm import ISortingAlgorithm

class QuickSort(ISortingAlgorithm):  
  pivot_index = 0

  @staticmethod
  def internal_sort(data: list[int]):
    if not data: return data # empty sequence case
    pivot = data[QuickSort.pivot_index]
    begin = QuickSort.internal_sort([x for x in data if x < pivot])
    end = QuickSort.internal_sort([x for x in data if x > pivot])
    return begin + [x for x in data if x == pivot] + end

  def sort(self, data: list[int]) -> None:
    data[:] = QuickSort.internal_sort(data)
