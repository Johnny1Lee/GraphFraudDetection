import numpy as np
import pandas as pd

# reads the node_data, edge_data, node_features, edge_features


def get_features(node_feature_file_path):
    """
    get node features
    return: node feature matrix in order
    """
    for node_file in node_feature_file_path:
        is_1st_line = True
        with open(node_file, "r") as fh:
            for line in fh:
                if is_1st_line:
                    is_1st_line = False
                
                node_feats = line.strip().split(",")
                



