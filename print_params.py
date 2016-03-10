import cPickle as pickle

import run_experiment
from stanza.unstable import config


def print_params(model):
    for param in model.params():
        print(param.name)
        print(param.get_value())


if __name__ == '__main__':
    options = config.options(read=True)
    with config.open('model.p', 'r') as infile:
        print_params(pickle.load(infile))