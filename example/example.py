import pandas as pd

from PostLabeller import PostLabeller
from PostLabeller import FlattenerType as ft
from PostLabeller import InterventionModelType as imt

# Replace paths with appropriate paths to csv files
user_df = pd.read_csv('./user.csv', comment='#')
post_df = pd.read_csv('./post.csv', comment='#')
comment_df = pd.read_csv('./comment.csv', comment='#')

# Can use any combinations of FlattenerType and InterventionModelType
pl = PostLabeller(user_df, post_df, comment_df,
                  ft.TIMESTAMP, imt.GIM)

# Replace path with desired path
pl.to_csv('./result.csv')
