# import pickle as pkl
# import pandas as pd
# with open("svmClassifier.pkl", "rb") as f:
#     object = pkl.load(f)
    
# df = pd.DataFrame(object)
# df.to_csv(r'file.csv')

import pickle


with open('svmClassifier.pkl', 'rb') as f:
    data = pickle.load(f)