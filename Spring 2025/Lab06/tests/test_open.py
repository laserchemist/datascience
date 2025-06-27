def test_open(text,notebook,length):
    response_length = -10
    ntbk = nbf.read(notebook, nbf.NO_CONVERT):
    for index, obj in enumerate(ntbk.cells):
        if text in obj.source:
            next_item = ntbk.cells[index + 1]
            response_length = len(next_item.source) 
    return response_length