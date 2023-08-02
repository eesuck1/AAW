import datetime
import os.path

import numpy
import pandas

from Source.constants import SIZE, MODELS_FOLDER
from Source.ML import leaky_relu, softmax, mean_squared_difference

from xgboost import XGBRegressor


class Model:
    def __init__(self, train: bool = True, load_weights: str = None):
        self._data_ = None
        self._labels_ = None
        self._train_ = None
        self._model_ = XGBRegressor()

        if train:
            self.train()

    # def __del__(self):
    #     index = len(os.listdir(MODELS_FOLDER)) + 1
    #     self._model_.save_model(os.path.join(MODELS_FOLDER, f"model_{index}.model"))

    def preprocess_data(self) -> None:
        self._train_ = self._data_[["plane_x", "plane_y", "plane_direction"]]
        self._labels_ = self._data_[["mouse_x", "mouse_y"]]

        # self._train_.loc[:, "plane_x"] = self._train_["plane_x"].astype(float) / SIZE[0]
        # self._train_.loc[:, "plane_y"] = self._train_["plane_y"].astype(float) / SIZE[1]
        # self._labels_.loc[:, "mouse_x"] = self._labels_["mouse_x"].astype(float) / SIZE[0]
        # self._labels_.loc[:, "mouse_y"] = self._labels_["mouse_y"].astype(float) / SIZE[1]

    def fit(self) -> None:
        self._model_.fit(self._train_.values, self._labels_.values)

    def predict(self, coordinates: numpy.ndarray) -> tuple[int, int]:
        prediction = self._model_.predict(coordinates)

        return prediction[0]

    def train(self) -> None:
        self._data_ = pandas.read_csv("C:\Git\AAW\labels.txt")
        self._train_ = None
        self._labels_ = None

        self.preprocess_data()
        self.fit()

    def print_data(self) -> None:
        print(self._data_.head())
