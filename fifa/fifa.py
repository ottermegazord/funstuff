import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.model_selection
import sklearn.neural_network
from sklearn.metrics import r2_score
from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE

"""Load Dataset"""

file_name = 'data.csv'
df = pd.read_csv(file_name, sep=',')
attributes = list(df.columns.values)
X = df.iloc[:, 11:46].copy()
y = df['Overall']
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.33, random_state=42)


"""Train Model"""

fifa = Ridge()
fifaLinear = LinearRegression()
rfe = RFE(fifaLinear, n_features_to_select = 2)


# fifa = sklearn.neural_network.MLPRegressor(verbose='True',
#                                            max_iter = 2000,
#                                            learning_rate_init=1,
#                                            learning_rate='adaptive')
# fifa = sklearn.neural_network.MLPRegressor(hidden_layer_sizes=(14, 14),
#                                            max_iter = 2000,
#                                            alpha=0.01,
#                                            solver='sgd',
#                                            activation = 'tanh',
#                                            verbose='True',
#                                            validation_fraction=0.1,
#                                            tol=1e-04
#                                            )


fifa.fit(X_train, y_train)
output = fifa.predict(X_test)
print(attributes)

x_axis = np.arange(0, output.shape[0])
#
r2_error = r2_score(y_test, output, multioutput="uniform_average")
print(r2_error)

fifaLinear.fit(X_train, y_train)
outputLinear = fifaLinear.predict(X_test)
r2_errorLinear = r2_score(y_test, outputLinear, multioutput="uniform_average")
print(r2_errorLinear)

rfe.fit(X_train, y_train)
outputRFE = rfe.predict(X_test)
# score_train = fifa.score(X_train, y_train)
# score_test = fifa.score(X_test, y_test)
# print(score_train)
# print(score_test)

plt.figure()
#plt.scatter(x_axis, y_test, label='test')
# plt.scatter(x_axis, output, label='output')
plt.scatter(x_axis, outputLinear, label='outputLinear')
plt.scatter(x_axis, outputRFE, label='RFE')
plt.legend()
plt.show()