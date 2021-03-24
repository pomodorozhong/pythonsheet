import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math
from . import major as pm
from . import utility as pu
from sklearn import linear_model
from scipy.optimize import minimize


def _fit_poly_through_origin(x, y, n=1):
    a = x[:, np.newaxis] ** np.arange(1, n+1)
    coeff = np.linalg.lstsq(a, y)[0]
    return np.concatenate(([0], coeff))


def fit(x: 'series', y: 'series', deg: int,
        plot_file="",
        x_upper_bound=None,
        x_lower_bound=None,
        y_upper_bound=None,
        y_lower_bound=None,
        pass_zero=False):

    df = pu.combine_series_to_dataframe([x, y])

    # remove rows that contains non-numeric
    df = df[pd.to_numeric(df[x.name], errors='coerce').notnull()]
    df = df[pd.to_numeric(df[y.name], errors='coerce').notnull()]
    df[x.name] = pd.to_numeric(df[x.name])
    df[y.name] = pd.to_numeric(df[y.name])

    # remove outliers
    if y_upper_bound:
        df = df[df[y.name] < y_upper_bound]
    if y_lower_bound:
        df = df[df[y.name] > y_lower_bound]
    if x_upper_bound:
        df = df[df[x.name] < x_upper_bound]
    if x_lower_bound:
        df = df[df[x.name] > x_lower_bound]
    df = df[(np.abs(stats.zscore(df)) < 4).all(axis=1)]

    x = getattr(df, x.name)
    y = getattr(df, y.name)
    if pass_zero:
        model = _fit_poly_through_origin(x, y, deg)
    else:
        model = np.polynomial.polynomial.polyfit(x, y, deg)
    predict = np.polynomial.Polynomial(model)

    if plot_file != "":
        # clear plot
        plt.clf()

        # plotting
        x_min = pm.min(x)
        x_max = pm.max(x)
        x_diff = x_max - x_min
        plot_x_min = math.floor(x_min - x_diff * 0.1)
        plot_x_max = math.ceil(x_max + x_diff * 0.1)

        x_lin_reg = range(plot_x_min, plot_x_max)
        y_lin_reg = predict(x_lin_reg)
        plt.plot(x, y, 'kx')
        plt.plot(x_lin_reg, y_lin_reg, c='r')
        plt.title(predict)

        # save plot
        plt.savefig(plot_file)

    return predict


def multiple_linear_fit(features: 'list_of_series', target: 'series'):
    target_name = target.name
    if target_name is None:
        target_name = 'target'
        target.name = target_name

    features_names = []
    for i in range(len(features)):
        feature_name = features[i].name
        if feature_name is None:
            feature_name = f'feature{i}'
            features[i].name = feature_name

        features_names.append(feature_name)

    serieses = features
    serieses.append(target)
    df = pu.combine_series_to_dataframe(features)

    # remove rows that contains non-numeric
    for features_name in features_names:
        df = df[pd.to_numeric(df[features_name], errors='coerce').notnull()]
        df[features_name] = pd.to_numeric(df[features_name])
    df = df[pd.to_numeric(df[target_name], errors='coerce').notnull()]
    df[target_name] = pd.to_numeric(df[target_name])

    # data preparation
    X = df[features_names].values.reshape((-1, len(features_names)))
    Y = df[target_name]

    # regression
    ols = linear_model.LinearRegression()
    model = ols.fit(X, Y)

    coefficients = model.coef_.tolist()
    coefficients.append(model.intercept_)

    # Evaluate
    r2 = model.score(X, Y)

    return coefficients, r2


# Reference: https://apmonitor.com/me575/index.php/Main/NonlinearRegression
def multiple_polynomial_fit(degree: int, features: 'list_of_series', target: 'series', minimize_method=None, plot_dir=None):

    def calc_y(x):
        coeffs = []
        coeffs.append(x[0])
        for i in range(len(features)):
            index = 1 + i*degree
            for d in range(degree):
                coeffs.append(x[index+d])

        y = 0
        y += coeffs[0]
        for x_i in range(len(features)):
            coeff_i = 1 + x_i*degree
            for d in range(degree, 0, -1):
                y += coeffs[coeff_i+d-1] * features[x_i] ** d

        return y

    def objective(x):
        y = calc_y(x)
        obj = 0.0
        for i in range(len(target)):
            obj += ((y[i]-target[i]))**2

        return obj

    # initial guesses
    coeff_guesses = np.zeros(len(features)*degree+1)

    # optimize
    solution = minimize(objective, coeff_guesses, method=minimize_method)
    x = solution.x
    y = calc_y(x)

    # target measured outcome
    # y  predicted outcome
    from scipy import stats
    slope, intercept, r_value, p_value, std_err = stats.linregress(target, y)

    coefficients = x
    r2 = r_value**2

    # plotting
    if plot_dir != None:
        if target.name == None:
            target_name = '[target_name]'
        else:
            target_name = target.name

        # actual vs predicted
        plt.clf()
        plt.figure(1)
        plt.title(
            f'Actual versus Predicted Outcomes\nfor multiple {degree} degree polynomial regression')
        plt.plot(target, y, '1')
        plt.xlabel('Measured Outcome')
        plt.ylabel('Predicted Outcome')
        plt.grid(True)
        plt.savefig(f'{plot_dir}/{target_name}_actual_vs_predicted.png')

        # actual vs prediction error
        plt.clf()
        prediction_error = y - target
        plt.figure(1)
        plt.title(
            f'Actual versus Error of Prediction\nfor multiple {degree} degree polynomial regression')
        plt.plot(target, prediction_error, '1')
        plt.xlabel('Measured Outcome')
        plt.ylabel('Error of Predicted Outcome')
        plt.grid(True)
        plt.savefig(f'{plot_dir}/{target_name}_vs_prediction_error.png')

        for i in range(len(features)):
            # actual vs each feature
            if features[i].name == None:
                feature_name = f'[feature{i}_name]'
            else:
                feature_name = features[i].name
            plt.clf()
            plt.figure(1)
            plt.title(
                f'Actual versus {feature_name}\nfor multiple {degree} degree polynomial regression')
            plt.plot(target, features[i], '1')
            plt.xlabel('Measured Outcome')
            plt.ylabel(feature_name)
            plt.grid(True)
            plt.savefig(f'{plot_dir}/{target_name}_vs_{feature_name}.png')

            # prediction error vs each feature
            plt.clf()
            plt.figure(1)
            plt.title(
                f'Actual versus {feature_name}\nfor multiple {degree} degree polynomial regression')
            plt.plot(prediction_error, features[i], '1')
            plt.xlabel('Error of Predicted Outcome')
            plt.ylabel(feature_name)
            plt.grid(True)
            plt.savefig(
                f'{plot_dir}/{target_name}_prediction_error_vs_{feature_name}.png')

    return coefficients, r2
