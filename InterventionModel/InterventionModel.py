from abc import ABCMeta, abstractmethod, abstractproperty

class InterventionModel(metaclass=ABCMeta):
    @abstractproperty
    def labels(self):
        pass

    @abstractproperty
    def posts(self):
        pass

    @abstractmethod
    def __init__(self, user_df, post_df, instructor='Instructor', student='Student'):
        pass
