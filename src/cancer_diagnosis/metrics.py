import os
import sys

__dir__ = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(__dir__, "../../"))
sys.path.append(project_root)

import time

from tools.metrics import log_metrics, performance_calculation

def metrics_performance(classifier, X, y_true):
    start_time = time.time()
    y_pred = classifier.predict(X)
    end_time = time.time()
    elapsed_time = end_time - start_time
    accuracy, precision, recall, f1 = performance_calculation(y_true, y_pred)
    return accuracy, precision, recall, f1, elapsed_time


def evaluate_performance(classifier, X_train, y_train, X_test, y_test, log_file_path):
    train_metrics = metrics_performance(classifier, X_train, y_train)
    test_metrics = metrics_performance(classifier, X_test, y_test)
    log_metrics(train_metrics, test_metrics, log_file_path)
