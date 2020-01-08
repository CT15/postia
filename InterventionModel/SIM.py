import numpy as np

from .InterventionModel import InterventionModel

class SIM(InterventionModel):
    def __init__(self, user_df, post_df, instructor='Instructor', student='Student'):
        self.labels = None
        self.posts = None
        raise Exception('Not implemented.')

    @property
    def labels(self):
        return self.labels
    
    @property
    def posts(self):
        return self.posts
