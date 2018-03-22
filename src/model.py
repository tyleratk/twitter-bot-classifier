import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, accuracy_score, recall_score, f1_score, classification_report
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
import numpy as np


class BotClassifier():

    def __init__(self, model_type):
        self.model_type = model_type


    def get_x_y(self, df=None, predict=False):
        if predict:
            values = []
            keep = ['followers_count','friends_count','listed_count',
                   'favourites_count','verified','statuses_count',
                   'default_profile','default_profile_image',
                   'has_extended_profile']
            for col in keep:
                values.append(df[col])
            return values

        else:
            df = pd.read_csv('../data/test.csv')
            df.drop(['location', 'id', 'id_str', 'screen_name', 'url', 'lang',
                     'created_at', 'status', 'name', 'description'], axis=1, inplace=True)
            df.bot = df.bot.map({1:True, 0:False})
            y = df.pop('bot').values
            X = df.values
            return X, y


    def fit(self, grid_search=False, score=False):
        X, y = self.get_x_y()
        X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)
        if self.model_type == 'rf':
            model = RandomForestClassifier(100)
        if score:
            model.fit(X_train, y_train)
            print('Score {}'.format(model.score(X_test, y_test)))
        else:
            model.fit(X, y)

        self.model = model


    def predict(self, user):
        X = self.get_x_y(user, predict=True)
        return self.model.predict([X])[0]


if __name__ == '__main__':
    clf = BotClassifier('rf')
    clf.fit()

    with open('../models/rf.pkl', 'wb') as outfile:
        pickle.dump(clf, outfile)
    print('Wrote model to pickle')


