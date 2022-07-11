import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
from typing import List

DATA_DIR = './data/movielens'


def rmse(y_true: float, y_pred: float) -> float:
    """rmse
    """
    return np.sqrt(mean_squared_error(y_true, y_pred))


def main():
    """_summary_
    """ 
    u_cols: List[str] = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
    user_df = pd.read_csv(os.path.join(DATA_DIR, 'u.user'),
                          sep='|',
                          encoding='latin-1',
                          names=u_cols)

    i_cols: List[str] = [
            'movie_id', 'title', 'release_date', 'video_release_date',
            'IMDb_URL', 'unknonw', 'Action', 'Adventure', 'Animaton',
            'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama',
            'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery',
            'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western'
            ]

    item_df = pd.read_csv(os.path.join(DATA_DIR, 'u.item'),
                          sep='|',
                          encoding='latin-1',
                          names=i_cols)

    r_cols: List[str] = ['user_id', 'movie_id', 'rating', 'timestamp']
    ratings_df = pd.read_csv(os.path.join(DATA_DIR, 'u.data'),
                             sep='\t',
                             encoding='latin-1',
                             names=r_cols).drop('timestamp', axis=1)

#    print(ratings_df.head())

    movies: pd.DataFrame = item_df[['movie_id', 'title']]
#    print(movies.head())
    X: pd.DataFrame = ratings_df.copy()
    y: pd.DataFrame = ratings_df['user_id']

    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.25,
                                                        stratify=y,
                                                        random_state=42)

    print(y_train[:4])


if __name__ == '__main__':
    main()
