import nbformat as nbf
def test_open(text,notebook,length):
    response_length = -10
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