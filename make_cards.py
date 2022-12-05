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
        cat = "macht"
        vraag = r"""Bereken $\lognl[2] (2^3)$"""
        antw = ["3","2","4","128"]
        obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw}
        return obj

    in_obj_list = []
    for i in range(12):
        obj = _template()
        grondtal = np.random.randint(2,7)
        coinflip = np.random.randint(2)
        
        # macht = 10 if coinflip else np.random.randint(2,4)
        macht = np.random.randint(1,15)
        # while x == grondtarget:
        #     x = np.random.randint(2,4)
        # print(n,coinflip,grondtarget,x)
        obj['vraag'] = r"""Bereken $\lognl[%i] (%i^{%i})$"""%(grondtal,grondtal,macht)
        
        obj['antw'][0] = r"$%i$"%(macht)
        obj['antw'][1] = r"$%i$"%(grondtal*macht)
        obj['antw'][2] = r"$%i$"%(grondtal**macht)
        obj['antw'][3] = r"$\frac{%i}{%i}$"%(grondtal,macht)
        
        obj['antw_uitleg'] = ["Correct","definitie","definitie","definitie"]
    
        in_obj_list.append(obj)
    
    
    obj_list_to_document(loc,fname,in_obj_list)
    
    return loc+fname

def gen_lvl1_catmacht():

    def _typeset(grondtal,which,power):
        powers = ["sqrt","neg","nml"]
        if powers[which] == "sqrt":
            thetxt = r"\sqrt[%i]{%s}"%(power,grondtal)
            x = 1/power
        elif powers[which] == "neg":
            thetxt = r"\frac{1}{%s^{%i}}"%(grondtal,power)
            x = -power
        elif powers[which] == "nml":
            thetxt = r"%s^{%i}"%(grondtal,power)
            x = power
            
        return thetxt,x
    
    loc = "lvl1/lvl1_catmacht/"
    fname = "lvl1_catmacht"
    
    
    def _template():
        lvl = 0
        cat = "macht"
        vraag = r"""Bereken $\lognl[2] (2^3)$"""
        antw = ["3","2","4","128"]
        obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw}
        return obj

    in_obj_list = []
    for i in range(6):
        obj = _template()
        grondtal = np.random.randint(2,7)
        coinflip = np.random.randint(2)
        
            
        first,firstn = np.random.randint(3),np.random.randint(1,5)
        xstr,x = _typeset(str(grondtal),first,firstn)
        second,secondn = np.random.randint(3),np.random.randint(1,5)
        ystr,y = _typeset(str(grondtal),second,secondn)
       
        
        obj['vraag'] = r"""Bereken $\lognl[%i] (%s\cdot%s)$"""%(grondtal,xstr,ystr)
        
        obj['antw'][0] = r"$%f$"%(x+y)
        obj['antw'][1] = r"$%f$"%(x*y)
        obj['antw'][2] = r"$%f$"%(grondtal*(x+y))
        obj['antw'][3] = r"$%f$"%(grondtal**(x+y))
        
        obj['antw_uitleg'] = ["Correct","logxlog","definitie","definitie"]
    
        in_obj_list.append(obj)
    
    
    obj_list_to_document(loc,fname,in_obj_list)
    
    return loc+fname

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
    
    return loc+fname

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
    
    return loc+fname


def gen_lvl1_catkeer():
    
    loc = "lvl1/lvl1_catkeer/"
    fname = "lvl1_catkeer"
    
    
    def _template():
        lvl = 1
        cat = "keer"
        vraag = r"""Bereken $\lognl[2] (2\cdot 3) $"""
        antw = ["3","2","4","128"]
        obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw}
        return obj

    in_obj_list = []
    for i in range(6):
        obj = _template()
        b = np.random.randint(2,5)
        coinflip = np.random.randint(2)
        
        # first = 1 if coinflip else np.random.randint(2,4)
        
        second = b**(np.random.randint(1,4)) if coinflip else np.random.randint(2,28)
        
        obj['vraag'] = r"""Herleid $\lognl[%i] (%i\cdot x)$"""%(b,second)
        
        obj['antw'][0] = r"$%f+\lognl[%i](x)$"%(logb(b,second),b)
        obj['antw'][1] = r"$%f+\lognl[%i](x)$"%(b*second,b)
        obj['antw'][2] = r"$%f\lognl[%i](x)$"%(logb(b,second),b)
        
        obj['antw_uitleg'] = ["Correct","definitie","logxlog"]
    
        in_obj_list.append(obj)
        
        
    for i in range(6):
        obj = _template()
        b = np.random.randint(2,5)
        coinflip = np.random.randint(2)
        
        first = np.random.randint(2,8)
        
        second = np.random.randint(2,8)
        
        obj['vraag'] = r"""Herleid $\lognl[%i] (%i x) + \lognl[%i](%i) $ tot \'e\'en logaritme"""%(b,first,b,second)
        
        obj['antw'][0] = r"$\lognl[%i](%i x)$"%(b,first*second)
        obj['antw'][1] = r"$\lognl[%i](%i x)$"%(b,first+second)
        obj['antw'][2] = r"$\lognl[%i](%i x)$"%(b,first^second)
        obj['antw'][2] = r"$\lognl[%i](%i x + %i)$"%(b,first,second)
        
        obj['antw_uitleg'] = ["Correct","definitie","definitie","log+log"]
    
        in_obj_list.append(obj)
    
    
    obj_list_to_document(loc,fname,in_obj_list)
    
    return loc+fname

def gen_lvl2_catomvorm():
    
    loc = "lvl2/lvl2_catomvorm/"
    fname = "lvl2_catomvorm"
    
    
    def _template():
        lvl = 2
        cat = "omvorm"
        vraag = r"""Bereken $\lognl[2] (2\cdot 3) $"""
        antw = ["3","2","4","128"]
        obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw}
        return obj

    in_obj_list = []
    for i in range(6):
        obj = _template()
        b = np.random.randint(2,5)
        coinflip = np.random.randint(2)
        
        a = 0 if coinflip else np.random.randint(15)
        c = np.random.randint(15)
        coinflip = np.random.randint(2)
        d = 0 if coinflip else np.random.randint(15)
        
        
        obj['vraag'] = r"""Herleid $y=%i+\lognl[%i] (%i\cdot x+%i)$"""%(a,b,c,d)
        
        obj['antw'][0] = r"$x=\frac{%i^{y-%i}-%i}{%i}$"%(b,a,d,c)
        obj['antw'][1] = r"$x=\frac{%i}{%i}%i^{y-%i}$"%(d,c,b,a)
        obj['antw'][2] = r"$x=\frac{%i^{%i y-%i}}{%i}$"%(b,c,d,a)
        obj['antw'][3] = r"$x=\lognl[%i](%i y - %i)-%i$"%(b,c,a,d)
        
        obj['antw_uitleg'] = ["Correct","definitie","definitie","definitie"]
    
        in_obj_list.append(obj)
        
        
    
    obj_list_to_document(loc,fname,in_obj_list)
    
    return loc+fname

def gen_lvl2_catvermeerder():
    
    loc = "lvl2/lvl2_catvermeerder/"
    fname = "lvl2_catvermeerder"
    
    
    def _template():
        lvl = 2
        cat = "vermeerder"
        vraag = r"""Bereken $\lognl[2] (2\cdot 3) $"""
        antw = ["3","2","4","128"]
        obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw}
        return obj

    in_obj_list = []
    for i in range(6):
        obj = _template()
        b = np.random.randint(2,5)
        coinflip = np.random.randint(2)
        
        a = 1 if coinflip else np.random.randint(1,15)
        c = 2 if coinflip else np.random.randint(2,5)
        
        
        obj['vraag'] = r"""Bereken met hoeveel $y=\lognl[%i](%i x)$ toeneemt als $x$ met %i wordt vermenigvuldigd"""%(b,a,c)
        
        obj['antw'][0] = r"plus $%f$"%(logb(b,c))
        obj['antw'][1] = r"keer $%f$"%(logb(b,c))
        obj['antw'][2] = r"plus $%f$"%(logb(b,a))
        obj['antw'][3] = r"keer $%f$"%(logb(b,a))
        
        obj['antw_uitleg'] = ["Correct","definitie","definitie","definitie"]
    
        in_obj_list.append(obj)
        
        
    
    obj_list_to_document(loc,fname,in_obj_list)
    
    return loc+fname

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
    
    fnames = []
    
    # Lvl 0
    fname = gen_lvl0_catkeer()
    fnames.append(fname)
    fname = gen_lvl0_catgrondtal()
    fnames.append(fname)
    fname = gen_lvl0_catmacht()
    fnames.append(fname)
    
    # Lvl 1
    fname = gen_lvl1_catkeer()
    fnames.append(fname)
    fname = gen_lvl1_catmacht()
    fnames.append(fname)
    
    # Lvl 2
    fname = gen_lvl2_catomvorm()
    fnames.append(fname)
    fname = gen_lvl2_catvermeerder()
    fnames.append(fname)
    
    # Watch out: all latex files have to be run by hand first before combine
    fnames = [f+'.pdf' for f in fnames]
    print(fnames)
    merge_pdfs(fnames,"all_combined.pdf")

if __name__ == "__main__":
    main()