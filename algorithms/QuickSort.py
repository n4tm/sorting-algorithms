from utils.SortingAlgorithm import SortingAlgorithm

class QuickSort(SortingAlgorithm):  
  pivot_index = 0

  def sort(self, data: list[int]) -> None:
    def _internal_sort(_data) -> list[int]:
      if not _data: return _data # empty sequence case
      pivot = _data[QuickSort.pivot_index]
      begin = _internal_sort([x for x in _data if x < pivot])
      end = _internal_sort([x for x in _data if x > pivot])
      return begin + [x for x in _data if x == pivot] + end
    data[:] = _internal_sort(data)
