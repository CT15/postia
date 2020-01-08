# Gratitude Intervention Model

# From the paper:
# Formally, a post or comment is defined as a gratitude 
# message if it contains less than or equal to 15 words, 
# and has the word “thank” or “thanks”, in upper or lower 
# case. The text must not contain any question marks.

import numpy as np

from .InterventionModel import InterventionModel

class GIM(InterventionModel):
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

        self._labels = self.__get_updated_labels()

        labels = []
        for label in self._labels:
            if label == 1:
                labels.append(instructor)
            elif label == 0:
                labels.append(student)
        self._labels = labels


    def __is_gratitude_message(self, string):
        if len(string) > 15 or '?' in string:
            return False

        thank_words = set(['thank', 'Thank', 'thanks', 'Thanks'])
        
        for word in string:
            if word in thank_words:
                return True

        return False


    def __get_updated_labels(self):
        labels = []
        
        # 0 => student
        # 1 => instructor
        for index, (post, label) in enumerate(zip(self.posts, self.labels)):
            if label == 1:
                labels.append(1)
            elif label == 0:
                if self.__is_gratitude_message(post) and index > 0:
                    labels.pop()
                    labels.extend([1, 0])
                else:
                    labels.append(0)
            else:
                raise Exception(f'The label {label} at index {index} is unrecognized.')
        
        return np.array(labels)

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
