from abc import ABCMeta, abstractmethod

import matplotlib.pyplot as plt

class SortingAlgorithm(metaclass=ABCMeta):
  @abstractmethod
  def sort(self, data: list[int]) -> None:
    pass