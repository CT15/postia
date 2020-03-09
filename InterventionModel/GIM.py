# Gratitude Intervention Model

# From the paper:
# Formally, a post or comment is defined as a gratitude 
# message if it contains less than or equal to 15 words, 
# and has the word “thank” or “thanks”, in upper or lower 
# case. The text must not contain any question marks.

import numpy as np
import os

from .InterventionModel import InterventionModel

class GIM(InterventionModel):
    def __init__(self, user_df, post_df, instructor='Instructor', student='Student', filename='found'):
        if filename is not None and os.path.exists(f'{filename}.csv'):
            os.remove(f'{filename}.txt')

        self.filename = filename
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
        if len(string.split()) > 15 or '?' in string:
            return False

        thank_words = set(['thank', 'Thank', 'thanks', 'Thanks'])
        
        for word in string.split():
            if word in thank_words:
                return True

        return False


    def __get_updated_labels(self):
        labels = []

        # to count gratitude message found
        count = 0
        # 0 => student
        # 1 => instructor
        prev_post = '---'
        prev_label = -1
        for index, (post, label) in enumerate(zip(self.posts, self.labels)):
            if label == 1:
                labels.append(1)
            elif label == 0:
                if self.__is_gratitude_message(post) and index > 0:
                    labels.pop()
                    labels.extend([1, 0])
                    
                    count += 1

                    if self.filename is not None:
                        filename = f'{self.filename}.csv'

                        if os.path.exists(filename):
                            append_write = 'a'
                        else:
                            append_write = 'w'

                        with open(filename, append_write) as myfile:
                            myfile.write(f'{index},{post},{int(prev_label)},{prev_post}\n')

                else:
                    labels.append(0)
            else:
                raise Exception(f'The label {label} at index {index} is unrecognized.')
            
            prev_post = post
            prev_label = label

        if self.filename is not None and os.path.exists(f'{self.filename}.csv'):
            with open(f'{self.filename}.csv', 'a') as myfile:
                myfile.write(f'# total = {count}')

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
