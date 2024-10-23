import nbformat as nbf
import glob
import os
from sentence_transformers import CrossEncoder
import torch

def test_open(text,notebook,length):
    response_length = -10
    notebooks = glob.glob('*.ipynb')
    notebook_new = max(notebooks, key=os.path.getmtime)
    if notebook_new != notebook:
        notebook = notebook_new
    ntbk = nbf.read(notebook, nbf.NO_CONVERT)
    for index, obj in enumerate(ntbk.cells):
        if text in obj.source:
            next_item = ntbk.cells[index + 1]
            #print(f'Your response: {next_item.source}')
            response_length = len(next_item.source) 
            break
    if response_length<length:
        #print(f'Your reponse to {text} is not sufficient ')
        score =0
    else:
        #print(f'Your reponse to {text} has been checked that you answered but not for content ')
        score =1
    return score
def test_open_score(text,notebook,length,file):
    print('+++++\n','Checking your response relative to key ideas\n++++')
    file = 'tests/'+file+'.txt'
    with open(file, "r") as f:
        answer=f.read()
    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-12-v2", default_activation_function=torch.nn.ReLU6())
    response_length = -10
    notebooks = glob.glob('*.ipynb')
    notebook_new = max(notebooks, key=os.path.getmtime)
    if notebook_new != notebook:
        notebook = notebook_new
    ntbk = nbf.read(notebook, nbf.NO_CONVERT)
    ascore = 0
    for index, obj in enumerate(ntbk.cells):
        if text in obj.source:
            next_item = ntbk.cells[index + 1]
            print(f'Your response: {next_item.source}')
            ascore = model.predict((answer, next_item.source))/6
            print(f'Similarity of your answer to expected ideas: {ascore:.2f}\n')
            response_length = len(next_item.source) 
            break
    score = ascore
    return score
def check_open(file,notebook):
    '''Read file with parameters'''
    data = [line.strip() for line in open(file, "r")]
    sc=test_open_score(data[1],notebook,60,data[-1])
    score = (sc > 0.6)*1
    return score