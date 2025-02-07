'''
Base Functions for implementation
'''
class Latex(object):
    '''
    Single line of output to desmos
    '''

    def __init__(self,text):
        self.text = text
    
    def __str__(self):
        return self.text

def expression(text) -> Latex:
    '''
    Returns a Latex object
    '''
    return Latex(text)
