# None / Normal Intervention Model

# Label intervention based on provided data.
# No additional modification to the data.

import numpy as np

from .InterventionModel import InterventionModel

class NIM(InterventionModel):
    def __init__(self, user_df, post_df, instructor='Instructor', student='Student'):
        self._posts = np.array(post_df.post_text)

        instructors = user_df[user_df.user_title == instructor].id
        students = user_df[user_df.user_title == student].id
        if len(instructors) + len(students) != len(user_df):
            raise Exception(f'user_df.user_title should only be either {instructor} or {student}.')
        
        instructors, students = set(instructors), set(students)

        # label 0 => student; label 1 => instructor
        self._labels = np.zeros(len(post_df))
        self._labels[post_df[post_df.user.isin(instructors)].index.tolist()] = 1

        labels = []
        for label in self._labels:
            if label == 1:
                labels.append(instructor)
            elif label == 0:
                labels.append(student)
        self._labels = labels
        
    @property
    def labels(self):
        return self._labels

    @labels.setter
    def labels(self, value):
        self._labels = value

    @property
    def posts(self):
        return self._posts

    @posts.setter
    def posts(self, value):
        self._posts = value