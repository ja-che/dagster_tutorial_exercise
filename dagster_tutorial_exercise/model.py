'''Model dagster solid
'''
from sklearn.linear_model import RidgeCV
from sklearn.model_selection import train_test_split


def load_model(data):
    '''Load model'''

    model = RidgeCV()

    features = [
        'calories', 'protein', 'fat', 'sodium', 'fiber', 'carbo',
        'sugars', 'potass', 'vitamins', 'shelf', 'weight', 'cups']

    target = 'rating'

    return model, data[features], data[target]


def fit_model(model, features, target):
    '''Fit model'''

    data_train, data_test, target_train, target_test = train_test_split(
        features, target, random_state=42, test_size=0.3)

    model.fit(data_train, target_train)

    return model, data_test, target_test


# Write the `create_model` op function that wraps the two previous functions
# It takes `data` as input and return `model`, `data_test`, `target_test`
# Hint: it should be similar to the op of compute_kpi module
