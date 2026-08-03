from abc import ABC, abstractmethod


class PrimitiveBase(ABC):
    """
    Base class for all robot primitives.
    """

    def __init__(self, planner_client):
        self._planner = planner_client

    @abstractmethod
    def execute(self):
        """
        Execute the primitive.
        """
        raise NotImplementedError