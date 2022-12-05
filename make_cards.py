from misc_func import *



def preamble():
    return r"""
\documentclass{article}
\usepackage[margin=2cm,centering,landscape]{geometry}

\usepackage{graphicx}


\usepackage{enumitem}
\setenumerate[0]{label=\textbf{\alph*)},leftmargin=2cm,rightmargin=2cm}
%\renewcommand{\theenumi}{\textbf{\alph{enumi})}}


\NewDocumentCommand{\lognl}{o}{%
  \IfNoValueTF{#1}{}{{}^{\scalebox{0.5}{#1}}\!}\log}%

\newcommand\Block[5]{%
\setlength\fboxsep{0pt}\setlength\fboxrule{0.1pt}% delete
\fbox{% delete
\begin{minipage}[c][\dimexpr.5\textheight-2pt\relax][t]{\dimexpr0.3333333\textwidth-3pt\relax}
\vspace{\baselineskip}\hspace{1cm}#1\hfill#2\phantom{\hspace{1cm}}\par
\vspace{1.5cm}
\centering
#3\par #4\par
\vfill
\hfill#5\phantom{\hspace{1cm}}
\vspace{\baselineskip}
\end{minipage}%
  }% delete
}

\begin{document}

    """
    
def foot():
    return r"""
\end{document}"""

def body(): # not used atm
    return r"""
\thispagestyle{empty}% optional: suppress page numbering
\noindent\Block{text}{caption}\hfill%
\Block{text}{\begin{enumerate}\item a \item b\end{enumerate}}\hfill%
\Block{text}{caption}%
\vfill
\noindent\Block{}{}{}{}\hfill%
\Block{}{}{}{}\hfill%
\Block{}{}{}{}"""



def make_document(loc,fname,pages):
    
    
    
    
    thefile = manipulate_files(loc+fname+".tex")
    thefile.clearfile()
    
    
    # Head
    thefile.write_appline( preamble() )
    
    groups = [pages[i:i+6] for i in range(0, len(pages), 6)]
    
    for i,group in enumerate(groups):
        # Contents
        content = r"""\thispagestyle{empty}% optional: suppress page numbering
    \noindent
"""
        for p in group[:3]:
            content += r"%s"%(p)+r"""\hfill%
"""
        content += r"""
        \vfill
        \noindent
        """
        for p in group[3:]:
            content += r"%s"%(p)+r"""\hfill%
"""
        print(content)
        thefile.write_appline( content )
        
        if i != len(groups):
            thefile.write_appline("\n\clearpage\n")
    
    # End file
    thefile.write_appline( foot() )


def make_page(obj,index,order):
    
    lvl = str(obj.get('lvl')+1)
    cat = obj.get('cat')
    vraag = obj.get('vraag')
    antw = obj.get('antw')
    
    antw_txt = r"""\begin{enumerate}"""
    
    for i in order:
        ant = antw[i]
        antw_txt += r"""\item %s"""%ant
    
    antw_txt += r"""\end{enumerate}"""
    
    page = r"""\Block{%s}{%s}{%s}{%s}{%s}"""%(lvl,cat,vraag,antw_txt,index)
    
    print(page)
    
    
    return page

def gen_lvl0_catmacht():
    
    loc = "lvl0/lvl0_catmacht/"
    fname = "lvl0_catmacht"
    
    
    def _template():
        lvl = 0
        cat = "grondtal"
        vraag = r"""Bereken $\lognl[2] (2^3)$ als logaritme met grondtal 10"""
        antw = ["3","2","4","128"]
        obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw}
        return obj

    in_obj_list = []
    for i in range(12):
        obj = _template()
        n = np.random.randint(2,15)
        coinflip = np.random.randint(2)
        
        grondtarget = 10 if coinflip else np.random.randint(2,4)
        x = np.random.randint(2,32)
        while x == grondtarget:
            x = np.random.randint(2,4)
        print(n,coinflip,grondtarget,x)
        obj['vraag'] = r"""Schrijf $\lognl[%i] (%i)$ als logaritme met grondtal %i"""%(n,x,grondtarget)
        
        obj['antw'][0] = r"$\frac{\lognl[%i](%i)}{\lognl[%i](%i)}$"%(grondtarget,x,grondtarget,n)
        obj['antw'][1] = r"$\lognl[%i](%i)$"%(grondtarget,x)
        obj['antw'][2] = r"$\frac{\lognl[%i](%i)}{\lognl[%i](%i)}$"%(grondtarget,x,x,grondtarget)
        obj['antw'][3] = r"$\frac{1}{%i}\lognl[%i](%i)$"%(n,grondtarget,x)
        
        obj['antw_uitleg'] = ["Correct","definitie_swappen","definitie_swappen","definitie_swappen"]
    
        in_obj_list.append(obj)
    
    
    obj_list_to_document(loc,fname,in_obj_list)
    
    return in_obj_list

def gen_lvl0_catgrondtal():
    
    loc = "lvl0/lvl0_catgrondtal/"
    fname = "lvl0_catgrondtal"
    
    
    def _template():
        lvl = 0
        cat = "grondtal"
        vraag = r"""Schrijf $\lognl[2] (3)$ als logaritme met grondtal 10"""
        antw = ["3","2","4","128"]
        obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw}
        return obj

    in_obj_list = []
    for i in range(12):
        obj = _template()
        n = np.random.randint(2,15)
        coinflip = np.random.randint(2)
        
        grondtarget = 10 if coinflip else np.random.randint(2,4)
        x = np.random.randint(2,32)
        while x == grondtarget:
            x = np.random.randint(2,4)
        print(n,coinflip,grondtarget,x)
        obj['vraag'] = r"""Schrijf $\lognl[%i] (%i)$ als logaritme met grondtal %i"""%(n,x,grondtarget)
        
        obj['antw'][0] = r"$\frac{\lognl[%i](%i)}{\lognl[%i](%i)}$"%(grondtarget,x,grondtarget,n)
        obj['antw'][1] = r"$\lognl[%i](%i)$"%(grondtarget,x)
        obj['antw'][2] = r"$\frac{\lognl[%i](%i)}{\lognl[%i](%i)}$"%(grondtarget,x,x,grondtarget)
        obj['antw'][3] = r"$\frac{1}{%i}\lognl[%i](%i)$"%(n,grondtarget,x)
        
        obj['antw_uitleg'] = ["Correct","definitie_swappen","definitie_swappen","definitie_swappen"]
    
        in_obj_list.append(obj)
    
    
    obj_list_to_document(loc,fname,in_obj_list)
    
    return in_obj_list

def gen_lvl0_catkeer():
    
    loc = "lvl0/lvl0_catkeer/"
    fname = "lvl0_catkeer"
    
    
    def _template():
        lvl = 0
        cat = "keer"
        vraag = r"""Bereken $\lognl[2] (2\cdot 3) $"""
        antw = ["3","2","4","128"]
        obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw}
        return obj

    in_obj_list = []
    for i in range(12):
        obj = _template()
        n = np.random.randint(2,5)
        coinflip = np.random.randint(2)
        
        first = 1 if coinflip else np.random.randint(2,4)
        second = np.random.randint(2,4)
        while second == first:
            second = np.random.randint(2,4)
        print(n,coinflip,first,second)
        obj['vraag'] = r"""Bereken $\lognl[%i] (%i\cdot %i) $"""%(n,n**first,n**second)
        
        obj['antw'][0] = str(first+second)
        obj['antw'][1] = str(first*second)
        obj['antw'][2] = str((n**first)*(n**second)//n)
        obj['antw'][3] = str(n**np.random.randint(5,7))
        
        obj['antw_uitleg'] = ["Correct","logxlog","definitie","definitie"]
    
        in_obj_list.append(obj)
    
    
    obj_list_to_document(loc,fname,in_obj_list)
    
    return in_obj_list

def obj_list_to_document(loc,fname,in_obj_list):

    pages = [ ]
    for i,obj in enumerate(in_obj_list):
        order = np.random.permutation(len(obj['antw'])) # random order
        page = make_page(obj,str(i),order) 
        pages.append(page)
        
        # TODO: log right answer and uitleg
    
    make_document(loc,fname,pages)
    

def main():
    print('vamonos')
    
    
    # gen_lvl0_catkeer()
    gen_lvl0_catgrondtal()

if __name__ == "__main__":
    main()