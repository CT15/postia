from abc import ABCMeta, abstractmethod, abstractproperty

class Flattener(metaclass=ABCMeta):
    @abstractproperty
    def post_df(self):
        pass

    @abstractproperty
    def comment_df(self):
        pass

    @abstractproperty
    def flattened_df(self):
        pass
