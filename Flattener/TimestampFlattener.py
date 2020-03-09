import pandas as pd
import numpy as np

from .Flattener import Flattener

class TimestampFlattener(Flattener):
    def __init__(self, post_df, comment_df):
        self.post_df = post_df
        self.comment_df = comment_df
        self.flattened_df = self.__get_flattened_df()


    def __get_flattened_df(self):
        self.post_df['parent_id'] = np.full(len(self.post_df,), None)
        self.comment_df.rename(columns={'comment_text':'post_text', 'post_id':'parent_id'}, inplace=True)

        combined_df = pd.concat([self.post_df, self.comment_df], axis=0, sort=True, ignore_index=True)
        combined_df = combined_df.sort_values(['thread_id', 'post_time'])
        
        combined_df.reset_index(drop=True, inplace=True)
        return combined_df

    @property
    def post_df(self):
        return self._post_df
    
    @post_df.setter
    def post_df(self, value):
        self._post_df = value

    @property
    def comment_df(self):
        return self._comment_df

    @comment_df.setter
    def comment_df(self, value):
        self._comment_df = value

    @property
    def flattened_df(self):
        return self._flattened_df

    @flattened_df.setter
    def flattened_df(self, value):
        self._flattened_df = value
