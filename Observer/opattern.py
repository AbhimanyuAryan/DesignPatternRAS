# behavioural pattern

from abc import ABC, abstractmethod
from typing import List, Protocol

# Observer Protocol
class Observer(Protocol):
    @abstractmethod
    def update(self, source: "Observer", state: str) -> None:
        pass

# Subject
class Subject:
    def __init__(self):
        self._state: str = ""
        self._observers: List[Observer] = []

    def add_observer(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def set_state(self, new_state: str) -> None:
        for observer in self._observers:
            observer.update(self, new_state)

# Concrete Observer
class ConcreteObserver(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, source: Observer, state: str) -> None:
        if isinstance(source, ConcreteObserver):
            print(f"{self.name} received updated state from {source.name}: {state}")
        else:
            print(f"{self.name} received updated state: {state}")

# Usage
subject = Subject()

observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

subject.add_observer(observer1)
subject.add_observer(observer2)

subject.set_state("New state for observers!")
