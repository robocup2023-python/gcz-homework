import argparse
import pandas as pd
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path')
parser.add_argument('-n', '--number')
args=parser.parse_args()
myfile = pd.read_csv(args.path)
myfile.drop(["args.number"],axis=1)
