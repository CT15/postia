import pandas as pd
import numpy as np
import enum

from InterventionModel import GIM, SIM, PIMM, NIM
from Flattener import TimestampFlattener, CommentFlattener


class FlattenerType(enum.Enum):
    COMMENT = 0
    TIMESTAMP = 1


class InterventionModelType(enum.Enum):
    NIM = 0
    GIM = 1
    PIMM = 2
    SIM = 3


class PostLabeller:
    def __init__(self, user_df, post_df, comment_df, flattener, intervention_model):
        self.user_df = user_df
        self.post_df = post_df
        self.comment_df = comment_df
        self.flattener = self.__get_flattener(flattener)
        self.flattened_df = self.flattener.flattened_df
        self.intervention_model = self.__get_intervention_model(intervention_model)

        self.posts = np.array(self.flattened_df.post_text)
        self.labels = np.array(self.intervention_model.labels)
        self.threadids = np.array(self.flattened_df.thread_id)


    def to_csv(self, path, mode='w'):
        data = {'thread_id':self.threadids, 'posts':self.posts, 'labels':self.labels}
        df = pd.DataFrame(data) 
        try:
            df.to_csv(path, mode=mode, index=False)
        except Exception as e:
            print(e)

    def __get_flattener(self, flattener):
        if flattener == FlattenerType.COMMENT:
            return CommentFlattener(self.post_df, self.comment_df)
        elif flattener == FlattenerType.TIMESTAMP:
            return TimestampFlattener(self.post_df, self.comment_df)
        else:
            raise Exception('Invalid flattener.')

    def __get_intervention_model(self, intervention_model):
        if intervention_model == InterventionModelType.GIM:
            return GIM(self.user_df, self.flattened_df)
        elif intervention_model == InterventionModelType.PIMM:
            return PIMM(self.user_df, self.flattened_df)
        elif intervention_model == InterventionModelType.SIM:
            return SIM(self.user_df, self.flattened_df)
        elif intervention_model == InterventionModelType.NIM:
            return NIM(self.user_df, self.flattened_df)
        else:
            raise Exception('Invalid intervention model.')
