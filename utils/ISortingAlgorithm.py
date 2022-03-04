from abc import ABC, abstractmethod

class ISortingAlgorithm(ABC):
  @abstractmethod
  def sort(self, data: list[int]) -> None:
    pass