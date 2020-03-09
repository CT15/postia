import numpy as np
import pandas as pd

from .Flattener import Flattener

class CommentFlattener(Flattener):
    def __init__(self, post_df, comment_df):
        self._post_df = post_df
        self._comment_df = comment_df
        self._flattened_df = self.__get_flattened_df()

        
    def __get_flattened_df(self):
        self.post_df['parent_id'] = np.full(len(self.post_df,), None)
        self.comment_df.rename(columns={'comment_text':'post_text', 'post_id':'parent_id'}, inplace=True)

        self.post_df = self.post_df.sort_values(['thread_id', 'post_time'])
        self.comment_df = self.comment_df.sort_values(['thread_id', 'post_time'])

        combined_df = self.post_df.copy()

        # go down the comment_df
        index = 0
        parent_id = None
        start_index = -1

        percentage_done = -1

        while index <= len(self.comment_df):
            if index == len(self.comment_df) or self.comment_df.iloc[index].parent_id != parent_id:
                if parent_id is not None:
                    parent_id_index = combined_df[combined_df.id == parent_id].index
                    assert len(parent_id_index) == 1
                    parent_id_index = parent_id_index[0]

                    combined_df = pd.concat([combined_df.iloc[:parent_id_index+1], 
                                            self.comment_df.iloc[start_index:index], 
                                            combined_df.iloc[parent_id_index+1:]], sort=True).reset_index(drop=True)

                if index < len(self.comment_df):
                    parent_id = self.comment_df.iloc[index].parent_id
                    start_index = index
            
            new_percentage_done = int(round(index / len(self.comment_df) * 100))
            if new_percentage_done > percentage_done:
                percentage_done = new_percentage_done
                print(f'Flattening df ... {percentage_done}%')

            index += 1

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