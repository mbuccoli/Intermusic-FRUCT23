'''
From the Fruct23 guidelines:

    Please check before submission
    Please put ticks besides all items and click "SUBMIT":
    Have you use proper template (MS Word and LaTeX)?
    
    If you target is Full Paper it shall be at least 6 pages and max 12 pages!
    
    If you target is Full Paper it shall have at least 6 references to other authors!
    
    Are all figures in White and Black?
    
    Have all tables and figures titles?
    
    Are authors titled by full first name and second name?
    
    Have you prepared PDF for submission according to the provided templates? (please note that later we might ask you for source files)
    
    For TeX source articles - all sections and references shall be done in one TeX file? 
    
    For TeX source articles - do you have all figures in EPS format and all of them are in archive?

This script reads the main.tex files and converts it to OneTexFile.tex .
Note that the PDF should be generated from OneTexFile

Please note that ALL THE FIGURES MUST BE IN BN

'''

if __name__=='__main__':
    IN_FILE='main.tex'
    OUT_FILE='OneTexFile.tex'
    with open(IN_FILE,'r') as fp:
        content=fp.read()
    '''
    the real algorith, which is basically a while with a replace:
    while "\include " in content:
        replace(content)
    '''
    with open(OUT_FILE,'w') as fp:
        fp.write(content)
    

