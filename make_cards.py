from misc_func import *



def preamble(margin="0.5cm",landscape_or_portrait='landscape',one_or_twocolumn="onecolumn"):
    
    docclass = r"\documentclass[twocolumn]{article}" if one_or_twocolumn == "twocolumn" else r"\documentclass{article}"
    return r"""
"""+docclass+r"""
\usepackage[margin="""+margin+r""",centering,"""+landscape_or_portrait+r"""]{geometry}

\usepackage{graphicx}
\usepackage[table]{xcolor}

\usepackage{xparse}

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

%\setlength{\tabcolsep}{20pt}
\renewcommand{\arraystretch}{1}

\pagestyle{empty} % no page numbering
\setlength{\parindent}{0cm} % no indentation

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


def make_document_answers(loc,fname,lvl,cat,answers):
    
    
    
    
    thefile = manipulate_files(loc+fname+"_antwoord.tex")
    thefile.clearfile()
    
    
    
    writeline = r"""\begin{tabular}{ rr| c|c|c|c}\hline\hline
     & i & \textbf{A} & \textbf{B} & \textbf{C} & \textbf{D}\\\hline
"""
    thefile.write_appline(writeline)
    
    for i,antw in enumerate(answers):
        if i == 1:
            entry = "Level %s & "%(lvl+1)
        elif i == 2:
            entry = "%s &"%(cat)
        else:
            entry = "&"
        
        entry += str(i)
        
        for one_antw in antw:
            
            entry += "&"+one_antw
            if one_antw == "Correct":
                entry += r"""\cellcolor[gray]{0.6}"""
        entry += r"\\"

        thefile.write_appline(entry)
        
    
    writeline = r"""\hline\end{tabular}\par\ \newline
"""
    thefile.write_appline(writeline)
    
    


def make_document(loc,fname,pages):
    
    
    
    
    thefile = manipulate_files(loc+fname+".tex")
    thefile.clearfile()
    
    
    # Head # no header, combine all later with headerfooter
    # thefile.write_appline( preamble() )
    
    groups = [pages[i:i+6] for i in range(0, len(pages), 6)]
    
    for i,group in enumerate(groups):
        # Contents
        content = r""""""
        for p in group[:3]:
            content += r"%s"%(p)+r"""\hfill%
"""
        content += r"""
        \vfill
        """
        for p in group[3:]:
            content += r"%s"%(p)+r"""\hfill%
"""
        print(content)
        thefile.write_appline( content )
        
        if i != len(groups):
            thefile.write_appline("\n\clearpage\n")
    
    # End file # no footer, combine all later with headerfooter
    # thefile.write_appline( foot() )


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

def gen_lvl0_catomvorm(loc,fname,lvl,cat):
    
    def _template():
        # lvl = lvl
        # cat = cat
        vraag = r"""Bereken $\lognl[2] (2^3)$"""
        antw = []
        antw_uitleg = []
        obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw,'antw_uitleg':antw_uitleg}
        return obj

    
    letters = ['x','t','q','p']
    
    in_obj_list = []
    for i in range(12):
        obj = _template()
        grondtal = np.random.randint(2,7)
        coinflip = np.random.randint(2)
        let = np.random.randint(len(letters)) if coinflip else 0
        let = letters[let]
        # macht = 10 if coinflip else np.random.randint(2,4)
        macht = np.random.randint(2,5)
        # while x == grondtarget:
        #     x = np.random.randint(2,4)
        # print(n,coinflip,grondtarget,x)
        obj['vraag'] = r"""Bereken $%s$ als $%i^{%s}=%i$"""%(let,grondtal,let,grondtal**macht)
        
        obj = obj_add_answer( obj,r"$%s=\lognl[%i](%i)=%i$"%(let,grondtal,grondtal**macht,macht) , "Correct")
        obj = obj_add_answer( obj,r"$%s=\lognl[%i](%i)=%i$"%(let,grondtal**macht,grondtal,macht) , "omgedraaid")
        obj = obj_add_answer( obj,r"$%s=\lognl[%i](%i)=%i$"%(let,grondtal,grondtal**(macht-1),macht) , "gedeeld")
        obj = obj_add_answer( obj,r"$%s=\lognl[%i](%i)=%i$"%(let,grondtal**(macht-1),grondtal,macht) , "beidefout")
        
    
        in_obj_list.append(obj)
    
    
    obj_list_to_document(loc,fname,in_obj_list)
    
    return loc+fname,len(in_obj_list)

def gen_lvl0_catmacht(loc,fname,lvl,cat):
    
    def _template():
        # lvl = lvl
        # cat = cat
        vraag = r"""Bereken $\lognl[2] (2^3)$"""
        antw = []
        antw_uitleg = []
        obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw,'antw_uitleg':antw_uitleg}
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
        
        obj = obj_add_answer( obj,r"$%i$"%(macht) , "Correct")
        obj = obj_add_answer( obj,r"$%i$"%(grondtal*macht) , "gxmacht")
        obj = obj_add_answer( obj,r"$%i$"%(grondtal**macht) , "gmachtmacht")
        obj = obj_add_answer( obj,r"$\frac{%i}{%i}$"%(grondtal,macht) , "gdeelmacht")
        
    
        in_obj_list.append(obj)
    
    
    obj_list_to_document(loc,fname,in_obj_list)
    
    return loc+fname,len(in_obj_list)


def gen_lvl1_cattotmacht(loc,fname,lvl,cat):
    
    def _template():
        # lvl = lvl
        # cat = cat
        vraag = r"""Bereken $\lognl[2] (2^3)$"""
        antw = []
        antw_uitleg = []
        obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw,'antw_uitleg':antw_uitleg}
        return obj

    
    letters = ['x','t','q','p']
    
    in_obj_list = []
    for i in range(12):
        obj = _template()
        macht = np.random.randint(1,5)
        grondtallist = ['x']+[np.random.randint(2,5) for x in range(5)]
        grondtal = str(grondtallist[np.random.randint(len(grondtallist))])
        
        grondtal = np.random.randint(2,7)
        coinflip = np.random.randint(2)
        base = np.random.randint(2,9)
        
        # print(n,coinflip,grondtarget,x)
        obj['vraag'] = r"""Herleid $y=\lognl[%i](%s^{%i})$"""%(base,grondtal,macht)
            
        
        obj = obj_add_answer( obj,r"$y=%i\cdot\lognl[%i](%s)$"%(macht,base,grondtal) , "Correct")
        obj = obj_add_answer( obj,r"$y=%i+\lognl[%i](%s)$"%(macht,base,grondtal) , "keer")
        obj = obj_add_answer( obj,r"$y=%s\cdot\lognl[%i](%i)$"%(grondtal,base,macht) , "macht")
        obj = obj_add_answer( obj,r"$y=%s+\lognl[%i](%i)$"%(grondtal,base,macht) , "macht")
        
    
        in_obj_list.append(obj)
    
    
    obj_list_to_document(loc,fname,in_obj_list)
    
    return loc+fname,len(in_obj_list)

def gen_lvl1_catherleid(loc,fname,lvl,cat):
    
    def _template():
        # lvl = lvl
        # cat = cat
        vraag = r"""Bereken $\lognl[2] (2^3)$"""
        antw = []
        antw_uitleg = []
        obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw,'antw_uitleg':antw_uitleg}
        return obj

    
    letters = ['x','t','q','p']
    
    in_obj_list = []
    for i in range(12):
        obj = _template()
        grondtal = 1000
        macht = 1
        while grondtal**macht > 300:
            macht = np.random.randint(1,5)
            grondtal2 = np.random.randint(2,7)
            macht1 = np.random.randint(2,5)
            grondtal = grondtal2**macht1
        coinflip = np.random.randint(2)
        # let = np.random.randint(len(letters)) if coinflip else 0
        # let = letters[let]
        # macht = 10 if coinflip else np.random.randint(2,4)
        # while x == grondtarget:
        #     x = np.random.randint(2,4)
        # print(n,coinflip,grondtarget,x)
        obj['vraag'] = r"""Herleid $y=\lognl[%i](%i x)$ tot de vorm $y=a+b\cdot \lognl[%i](x)$"""%(grondtal,grondtal**macht,grondtal2)
        
        obj = obj_add_answer( obj,r"$y=%i+\frac{1}{%i}\lognl[%i](x)$"%(macht,macht1,grondtal2) , "Correct")
        obj = obj_add_answer( obj,r"$y=%i+\frac{1}{%i}\lognl[%i](x)$"%(1+macht,macht1,grondtal2) , "macht")
        obj = obj_add_answer( obj,r"$y=%i+\frac{1}{%i}\lognl[%i](x)$"%(macht1,macht,grondtal2) , "grondtal")
        obj = obj_add_answer( obj,r"$y=%i+\frac{1}{%i}\lognl[%i](x)$"%(macht,grondtal,grondtal2) , "grondtal")
        
    
        in_obj_list.append(obj)
    
    
    obj_list_to_document(loc,fname,in_obj_list)
    
    return loc+fname,len(in_obj_list)

def gen_lvl2_catherleid(loc,fname,lvl,cat):
    
    def _template():
        # lvl = lvl
        # cat = cat
        vraag = r"""Bereken $\lognl[2] (2^3)$"""
        antw = []
        antw_uitleg = []
        obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw,'antw_uitleg':antw_uitleg}
        return obj

    
    letters = ['x','t','q','p']
    
    in_obj_list = []
    for i in range(12):
        obj = _template()
        grondtal = 1000
        macht = 1
        while grondtal**macht > 300:
            macht = np.random.randint(1,5)
            grondtal2 = np.random.randint(2,7)
            macht1 = np.random.randint(2,5)
            grondtal = grondtal2**macht1
        coinflip = np.random.randint(2)
        # let = np.random.randint(len(letters)) if coinflip else 0
        # let = letters[let]
        # macht = 10 if coinflip else np.random.randint(2,4)
        # while x == grondtarget:
        #     x = np.random.randint(2,4)
        # print(n,coinflip,grondtarget,x)
        obj['vraag'] = r"""Herleid $y=\lognl[%i](%i x)$ tot de vorm $y=a+b\cdot \lognl[%i](x)$"""%(grondtal,grondtal**macht,grondtal2)
        
        obj = obj_add_answer( obj,r"$y=%i+\frac{1}{%i}\lognl[%i](x)$"%(macht,macht1,grondtal2) , "Correct")
        obj = obj_add_answer( obj,r"$y=%i+\frac{1}{%i}\lognl[%i](x)$"%(1+macht,macht1,grondtal2) , "macht")
        obj = obj_add_answer( obj,r"$y=%i+\frac{1}{%i}\lognl[%i](x)$"%(macht1,macht,grondtal2) , "grondtal")
        obj = obj_add_answer( obj,r"$y=%i+\frac{1}{%i}\lognl[%i](x)$"%(macht,grondtal,grondtal2) , "grondtal")
        
    
        in_obj_list.append(obj)
    
    
    obj_list_to_document(loc,fname,in_obj_list)
    
    return loc+fname,len(in_obj_list)


def gen_lvl1_catmacht(loc,fname,lvl,cat):

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
    
    
    
    def _template():
        # lvl = lvl
        # cat = cat
        vraag = r"""Bereken $\lognl[2] (2^3)$"""
        antw = []
        antw_uitleg = []
        obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw,'antw_uitleg':antw_uitleg}
        return obj

    in_obj_list = []
    for i in range(12):
        obj = _template()
        grondtal = np.random.randint(2,7)
        coinflip = np.random.randint(2)
        
            
        first = np.random.randint(3)
        firstn = np.random.randint(1,5) if first == 1 else np.random.randint(2,5)
        xstr,x = _typeset(str(grondtal),first,firstn)
        second = np.random.randint(3)
        secondn = np.random.randint(1,5) if second == 1 else np.random.randint(2,5)
        ystr,y = _typeset(str(grondtal),second,secondn)
       
        
        obj['vraag'] = r"""Bereken $\lognl[%i] (%s\cdot%s)$"""%(grondtal,xstr,ystr)
        
        obj = obj_add_answer( obj,r"$%g$"%(x+y) , "Correct" )
        obj = obj_add_answer( obj,r"$%g$"%(x*y), "logxlog" )
        obj = obj_add_answer( obj,r"$%g$"%(grondtal*(x+y)), "grondtal*machten" )
        obj = obj_add_answer( obj,r"$%g$"%(grondtal**(x+y)), "definitie" )
        
    
        in_obj_list.append(obj)
    
    
    obj_list_to_document(loc,fname,in_obj_list)
    
    return loc+fname,len(in_obj_list)

def gen_lvl0_catgrondtal(loc,fname,lvl,cat):
    
    def _template():
        # lvl = lvl
        # cat = cat
        vraag = r"""Schrijf $\lognl[2] (3)$ als logaritme met grondtal 10"""
        antw = []
        antw_uitleg = []
        obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw,'antw_uitleg':antw_uitleg}
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
        
        obj = obj_add_answer( obj,r"$\frac{\lognl[%i](%i)}{\lognl[%i](%i)}$"%(grondtarget,x,grondtarget,n)  , "Correct" )
        obj = obj_add_answer( obj,r"$\frac{\lognl[%i](%i)}{\lognl[%i](%i)}$"%(grondtarget,x,n,x) , "swappen" )
        obj = obj_add_answer( obj,r"$\frac{\lognl[%i](%i)}{\lognl[%i](%i)}$"%(grondtarget,x,x,grondtarget) , "swappen" )
        obj = obj_add_answer( obj,r"$\frac{\lognl[%i](%i)}{%i}$"%(grondtarget,x,n) , "swappen" )
        
    
        in_obj_list.append(obj)
    
    
    obj_list_to_document(loc,fname,in_obj_list)
    
    return loc+fname,len(in_obj_list)

def gen_lvl0_catkeer(loc,fname,lvl,cat):
    
    def _template():
        # lvl = lvl
        # cat = cat
        vraag = r"""Bereken $\lognl[2] (2\cdot 3) $"""
        antw = []
        antw_uitleg = []
        obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw,'antw_uitleg':antw_uitleg}
        return obj

    in_obj_list = []
    for i in range(12): # KEER
        obj = _template()
        n = np.random.randint(2,5)
        coinflip = np.random.randint(2)
        
        first = 1 if coinflip else np.random.randint(2,4)
        second = np.random.randint(2,4)
        while second == first:
            second = np.random.randint(2,4)
        print(n,coinflip,first,second)
        obj['vraag'] = r"""Bereken $\lognl[%i] (%i\cdot %i) $"""%(n,n**first,n**second)
        
        obj = obj_add_answer( obj,str(first+second) , "Correct" )
        obj = obj_add_answer( obj,str(first*second) , "logxlog" )
        obj = obj_add_answer( obj,str((n**first)*(n**second)//n) , "definitie" )
        obj = obj_add_answer( obj,str(n**np.random.randint(5,7)) , "definitie" )
        
    
        in_obj_list.append(obj)
    
    for i in range(12): # DELEN
        obj = _template()
        n = np.random.randint(2,5)
        coinflip = np.random.randint(2)
        
        first = 1 if coinflip else np.random.randint(2,4)
        second = np.random.randint(2,4)
        while second == first:
            second = np.random.randint(2,4)
        print(n,coinflip,first,second)
        obj['vraag'] = r"""Bereken $\lognl[%i] (\frac{%i}{ %i}) $"""%(n,n**first,n**second)
        
        obj = obj_add_answer( obj,str(first-second) , "Correct" )
        obj = obj_add_answer( obj,str(-first*second) , "logxlog" )
        obj = obj_add_answer( obj,str(second-first) , "definitie" )
        obj = obj_add_answer( obj,str((-n)**np.random.randint(4)) , "definitie" )
        
    
        in_obj_list.append(obj)
    
    
    obj_list_to_document(loc,fname,in_obj_list)
    
    return loc+fname,len(in_obj_list)


def gen_lvl1_catkeer(loc,fname,lvl,cat):
    
    
    def _template():
        # lvl = lvl
        # cat = cat
        vraag = r"""Bereken $\lognl[2] (2\cdot 3) $"""
        antw = []
        antw_uitleg = []
        obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw,'antw_uitleg':antw_uitleg}
        return obj

    in_obj_list = []
    for i in range(6):# KEER
        obj = _template()
        b = np.random.randint(2,5)
        coinflip = np.random.randint(2)
        
        # first = 1 if coinflip else np.random.randint(2,4)
        
        second = b**(np.random.randint(1,5)) #if coinflip else np.random.randint(2,28)
        
        obj['vraag'] = r"""Herleid $\lognl[%i] (%i x)$"""%(b,second)
        
        obj = obj_add_answer( obj,r"$%g+\lognl[%i](x)$"%(logb(b,second),b) , "Correct" )
        obj = obj_add_answer( obj,r"$%g+\lognl[%i](x)$"%(b*second,b) , "macht" )
        if second != 1:
            obj = obj_add_answer( obj,r"$%g+\lognl[%i](x)$"%(second/b,b) , "macht" )
        else:
            obj = obj_add_answer( obj,r"$%g+\lognl[%i](x)$"%(second,b) , "macht" )
        obj = obj_add_answer( obj,r"$%g\cdot\lognl[%i](x)$"%(logb(b,second),b) , "keer" )
        
    
        in_obj_list.append(obj)
        
    for i in range(6): # DELEN
        obj = _template()
        b = np.random.randint(2,5)
        coinflip = np.random.randint(2)
        
        # first = 1 if coinflip else np.random.randint(2,4)
        
        second = b**(np.random.randint(1,5)) #if coinflip else np.random.randint(2,28)
        
        obj['vraag'] = r"""Herleid $\lognl[%i] (\frac{x}{%i})$"""%(b,second)
        
        obj = obj_add_answer( obj,r"$\lognl[%i](x)-%g$"%(b,logb(b,second)) , "Correct" )
        obj = obj_add_answer( obj,r"$\lognl[%i](x)-%g$"%(b,b*second) , "macht" )
        if second != 1:
            obj = obj_add_answer( obj,r"$\lognl[%i](x)+%g$"%(b,second/b) , "minfout" )
        else:
            obj = obj_add_answer( obj,r"$\lognl[%i](x)+%g$"%(b,second) , "minfout" )
        obj = obj_add_answer( obj,r"$-%g\cdot\lognl[%i](x)$"%(logb(b,second),b) , "keer" )
        
    
        in_obj_list.append(obj)
        
        
    for i in range(6): # KEER
        obj = _template()
        b = np.random.randint(2,5)
        coinflip = np.random.randint(2)
        
        first = np.random.randint(2,8)
        
        second = np.random.randint(2,8)
        
        obj['vraag'] = r"""Herleid $\lognl[%i] (%i x) + \lognl[%i](%i) $ tot \'e\'en logaritme"""%(b,first,b,second)
        
        obj = obj_add_answer( obj,r"$\lognl[%i](%i x)$"%(b,first*second) , "Correct" )
        obj = obj_add_answer( obj,r"$\lognl[%i](%i x)$"%(b,first+second) , "pluslogs" )
        obj = obj_add_answer( obj,r"$\lognl[%i](%i x)$"%(b,first^second) , "machten" )
        obj = obj_add_answer( obj,r"$\lognl[%i](%i x + %i)$"%(b,first,second) , "keer" )
        
    
        in_obj_list.append(obj)
    
        
    for i in range(6): # DELEN
        obj = _template()
        b = np.random.randint(2,5)
        coinflip = np.random.randint(2)
        
        first = np.random.randint(2,8)
        
        second = np.random.randint(2,8)
        
        obj['vraag'] = r"""Herleid $\lognl[%i] (%i x) - \lognl[%i](%i) $ tot \'e\'en logaritme"""%(b,first,b,second)
        
        obj = obj_add_answer( obj,r"$\lognl[%i](\frac{%i x}{%i})$"%(b,first,second) , "Correct" )
        obj = obj_add_answer( obj,r"$\lognl[%i](\frac{%i x}{%i})$"%(b,second,first) , "pluslogs" )
        obj = obj_add_answer( obj,r"$\lognl[%i](%i x)$"%(b,first*second) , "keeripvdeel" )
        obj = obj_add_answer( obj,r"$\lognl[%i](%i x - %i)$"%(b,first,second) , "delen" )
        
    
        in_obj_list.append(obj)
    
    
    obj_list_to_document(loc,fname,in_obj_list)
    
    return loc+fname,len(in_obj_list)

def gen_lvl2_catomvorm(loc,fname,lvl,cat):
    
    def _template():
        # lvl = lvl
        # cat = cat
        vraag = r"""Bereken $\lognl[2] (2\cdot 3) $"""
        antw = []
        antw_uitleg = []
        obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw,'antw_uitleg':antw_uitleg}
        return obj

    in_obj_list = []
    for i in range(12):
        obj = _template()
        b = np.random.randint(2,5)
        coinflip = np.random.randint(2)
        
        a = 0 if coinflip else np.random.randint(15)
        c = np.random.randint(15)
        coinflip = np.random.randint(2)
        d = 0 if coinflip else np.random.randint(15)
        
        
        obj['vraag'] = r"""Druk $x$ uit in $y$ bij $y=%i+\lognl[%i] (%i\cdot x+%i)$"""%(a,b,c,d)
        
        obj = obj_add_answer( obj,r"$x=\frac{%i^{y-%i}-%i}{%i}$"%(b,a,d,c) , "Correct" )
        obj = obj_add_answer( obj,r"$x=\frac{%i}{%i}%i^{y-%i}$"%(d,c,b,a) , "definitie" )
        obj = obj_add_answer( obj,r"$x=\frac{%i^{%i y-%i}}{%i}$"%(b,c,d,a) , "keer" )
        obj = obj_add_answer( obj,r"$x=\lognl[%i](%i y - %i)-%i$"%(b,c,a,d) , "definitie" )
        
    
        in_obj_list.append(obj)
        
        
    
    obj_list_to_document(loc,fname,in_obj_list)
    
    return loc+fname,len(in_obj_list)

    
def gen_lvl2_catvermeerder(loc,fname,lvl,cat):
    
    def _template():
        # lvl = lvl
        # cat = cat
        vraag = r"""Bereken $\lognl[2] (2\cdot 3) $"""
        antw = []
        antw_uitleg = []
        obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw,'antw_uitleg':antw_uitleg}
        return obj

    in_obj_list = []
    for i in range(12):
        obj = _template()
        b = np.random.randint(2,5)
        coinflip = np.random.randint(2)
        
        a = 1 if coinflip else b**np.random.randint(1,6)
        c = 2 if coinflip else np.random.randint(2,5)
        
        
        obj['vraag'] = r"""Bereken met hoeveel $y=\lognl[%i](%i x)$ toeneemt als $x$ met %i wordt vermenigvuldigd"""%(b,a,c)
        
        obj = obj_add_answer( obj,r"plus $%g$"%(logb(b,c)) , "Correct" )
        obj = obj_add_answer( obj,r"keer $%g$"%(logb(b,c)), "keer" )
        obj = obj_add_answer( obj,r"plus $%g$"%(logb(b,a)), "definitie" )
        obj = obj_add_answer( obj,r"keer $%g$"%(logb(b,a)), "keer" )
        
    
        in_obj_list.append(obj)
        
    obj_list_to_document(loc,fname,in_obj_list)
    
    return loc+fname,len(in_obj_list)

def gen_lvl3_catbereken(loc,fname,lvl,cat):
    
    def _template():
        # lvl = lvl
        # cat = cat
        vraag = r"""Gegeven is dat $\lognl[10] = 8$ Bereken $\lognl[2] (2\cdot 3) $"""
        antw = []
        antw_uitleg = []
        obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw,'antw_uitleg':antw_uitleg}
        return obj

    in_obj_list = []
    ####
    obj = _template()
    grondtal = np.random.randint(2,11)
    
    obj['vraag'] = r"""Gegeven is dat $\lognl[](a) = 6$. Bereken $\lognl[] (\sqrt{a^4}) $"""
    
    obj = obj_add_answer( obj,r"12" , "Correct" )
    obj = obj_add_answer( obj,r"24" , "machten" )
    obj = obj_add_answer( obj,r"8" , "totmacht" )
    obj = obj_add_answer( obj,r"3" , "machten" )
    in_obj_list.append(obj)
    ####
    obj = _template()
    grondtal = np.random.randint(2,11)
    
    obj['vraag'] = r"""Gegeven is dat $\lognl[](a) = 6$. Bereken $\lognl[] (\sqrt{a \sqrt{a}}) $"""
    
    obj = obj_add_answer( obj,r"9" , "Correct" )
    obj = obj_add_answer( obj,r"18" , "machten" )
    obj = obj_add_answer( obj,r"7.5" , "totmacht" )
    obj = obj_add_answer( obj,r"3.5" , "machten" )
    in_obj_list.append(obj)
    ####
    obj = _template()
    grondtal = np.random.randint(2,11)
    
    obj['vraag'] = r"""Gegeven is dat $\lognl[](a) = 6$. Bereken $\lognl[] (\sqrt{100a \sqrt{a}}) $"""
    
    obj = obj_add_answer( obj,r"11" , "Correct" )
    obj = obj_add_answer( obj,r"18" , "keer" )
    obj = obj_add_answer( obj,r"9" , "keer" )
    obj = obj_add_answer( obj,r"7" , "machten" )
    in_obj_list.append(obj)
    ####
    obj = _template()
    grondtal = np.random.randint(2,11)
    
    obj['vraag'] = r"""Gegeven is dat $\lognl[](a) = 6$. Bereken $\lognl[] (0.001a^2) $"""
    
    obj = obj_add_answer( obj,r"3" , "Correct" )
    obj = obj_add_answer( obj,r"-18" , "keer" )
    obj = obj_add_answer( obj,r"18" , "keer" )
    obj = obj_add_answer( obj,r"6" , "machten" )
    in_obj_list.append(obj)
    ####
    obj = _template()
    grondtal = np.random.randint(2,11)
    
    obj['vraag'] = r"""Gegeven is dat $\lognl[](a) = 6$. Bereken $\lognl[] (\frac{1}{\sqrt{a}}) $"""
    
    obj = obj_add_answer( obj,r"-3" , "Correct" )
    obj = obj_add_answer( obj,r"-12" , "totmacht" )
    obj = obj_add_answer( obj,r"12" , "totmacht" )
    obj = obj_add_answer( obj,r"3" , "fout" )
    in_obj_list.append(obj)
    ####
    for getal in [(r'\sqrt{2000}',np.sqrt(2000)),('8',8),(r"\frac{15}{28}",15/28),('2',2),('5',5)]:
        obj = _template()
        
        obj['vraag'] = r"""Schrijf als macht van 10: $%s$"""%(getal[0])
        
        obj = obj_add_answer( obj,r"$10^{%.2f}$"%(np.log10(getal[1])) , "Correct" )
        obj = obj_add_answer( obj,r"$10^{%.2f}$"%(1.5*np.log10(getal[1])) , "definitie" )
        obj = obj_add_answer( obj,r"$10^{%.2f}$"%(0.5*np.log10(getal[1])) , "definitie" )
        obj = obj_add_answer( obj,r"$10^{%.2f}$"%(2*np.log10(getal[1])) , "definitie" )
        in_obj_list.append(obj)
        
    ####
    obj = _template()
    grondtal = np.random.randint(2,11)
    
    obj['vraag'] = r"""Bereken $N$ als $\lognl[](\lognl[](\lognl[](N)))=0$"""
    
    obj = obj_add_answer( obj,r"" , "Correct" )
    obj = obj_add_answer( obj,r"" , "--" )
    obj = obj_add_answer( obj,r"" , "--" )
    obj = obj_add_answer( obj,r"" , "--" )
    in_obj_list.append(obj)
    ####
    obj = _template()
    grondtal = np.random.randint(2,11)
    
    obj['vraag'] = r"""Bewijs met behulp van de regel $\lognl[](ab)=\lognl[](a)+\lognl[](b)$ dat $\lognl[](1)=0$"""
    
    obj = obj_add_answer( obj,r"" , "Correct" )
    obj = obj_add_answer( obj,r"" , "--" )
    obj = obj_add_answer( obj,r"" , "--" )
    obj = obj_add_answer( obj,r"" , "--" )
    in_obj_list.append(obj)
        
    
    obj_list_to_document(loc,fname,in_obj_list)
    
    return loc+fname,len(in_obj_list)

def obj_list_to_document(loc,fname,in_obj_list):
    # print(in_obj_list)
    lvl = in_obj_list[0]['lvl']
    cat = in_obj_list[0]['cat']
    
    pages = [ ]
    answers = [ ]
    for i,obj in enumerate(in_obj_list):
        order = np.random.permutation(len(obj['antw'])) # random order
        page = make_page(obj,str(i),order) 
        pages.append(page)
        print(obj)
        print(order)
        print(obj['antw'])
        print(obj['antw_uitleg'])
        answers.append([obj['antw_uitleg'][ind] for ind in order]) # Comply to random order
        
        # TODO: log right answer and uitleg
    
    make_document(loc,fname,pages)
    
    make_document_answers(loc,fname,lvl,cat,answers)
    
    
    
    

def make_scoresheet(loc,fname,data):
    
    width = 12
    empties = width*r"&\phantom{XXX}"
    
    thefile = manipulate_files(loc+fname+".tex") 
    thefile.clearfile()
    
    
    # Head
    thefile.write_appline( preamble(margin="2.5cm") )
    
    # tabel
    
    for twice in range(2): # Repeat
        for twice in range(2): # Repeat
            
            toggle = 0
            
            thefile.write_appline("\n"+r"\Large"+"\n\n")
            csstring = width*"|c"
            writeline = r"""\rowcolors{1}{gray!25}{white}\begin{tabular}{ rr"""+csstring+r"""}\hline\hline
    """
            thefile.write_appline(writeline)
            
            for lvl in data:
                # print("LEVEL",lvl)
                
                for i,cat in enumerate(data[lvl]):
                    # print(data[lvl][cat])
                    # input()
                    # if toggle:
                    #     entry = r"\rowcolor[gray]{.95}"
                    # else:
                    #     entry = ""
                    entry = ""
                    
                    if i == 0:
                        entry += "Level %s & "%(lvl+1)
                    else:
                        entry += "& "
                    entry += cat + " "
                    entry += empties 
                    
                    entry += r"\\"

                    thefile.write_appline(entry)
                    toggle = 1-toggle
                
                thefile.write_appline("\hline")
            
            writeline = r"""\hline\end{tabular}\par\ \newline
        """
            thefile.write_appline(writeline)
            
            thefile.write_appline("\n\n\n")
            thefile.write_appline(r"\vfill")
            
        thefile.write_appline(r"\clearpage")
            
    # End file
    thefile.write_appline( foot() )
    
def combine_to_single_tex(loc,fname,fnames,loc_relative="../"):
    
    
    def _questions():
        thefile = manipulate_files(loc+fname+".tex") 
        thefile.clearfile()
        
        
        # Head
        thefile.write_appline( preamble() )
        
        thefile.write_appline("\n\n\n")
        
        for fn in fnames:
            
            writeline = r"\input{%s}"%(loc_relative+fn+".tex")
            thefile.write_appline(writeline)
        
        thefile.write_appline("\n\n\n")
        
        # End file
        thefile.write_appline( foot() )
    
    def _answers():
        thefile = manipulate_files(loc+fname+"_antwoord.tex")
        thefile.clearfile()
        
        
        # Head
        thefile.write_appline( preamble(landscape_or_portrait='landscape',one_or_twocolumn="twocolumn") )
        
        thefile.write_appline("\n\centering\n\n")
        
        lvls = ['0','0']
        for fn in fnames:
            curlvl = fn.split("_")[0].split('/')[1].replace('lvl','')
            # print(curlvl)
            lvls.append(curlvl)
            if lvls[-1] != lvls[-2] and curlvl != '3':
                writeline = r"\clearpage"
                thefile.write_appline(writeline)
            # input()
            
            writeline = r"\input{%s}"%(loc_relative+fn+"_antwoord.tex")
            thefile.write_appline(writeline)
            thefile.write_appline("\n")
            thefile.write_appline("\n")
            
            
        
        thefile.write_appline("\n\n\n")
        
        # End file
        thefile.write_appline( foot() )

    
    _questions()
    _answers()

def obj_add_answer(obj,antw,antw_uitleg):
    obj['antw'].append(antw)
    obj['antw_uitleg'].append(antw_uitleg)
    return obj

def main():
    print('vamonos')
    def _locfname(lvl,cat):
        fname = "lvl%i_cat%s"%(lvl,cat)
        # loc = "lvl%i/%s/"%(lvl,fname)
        loc = "content/"
        return loc,fname
    
    def _make_entry(loc,fname):
        out = {}
        out['loc'] = loc
        out['fname'] = fname
        
        return out
    
    data = {}
    
    fnames = []
    
    # Lvl 0
    lvl = 0
    data[lvl] = {}
    
    cat = "keer"
    loc,fname = _locfname(lvl,cat)
    data[lvl][cat] = _make_entry(loc,fname)
    fname_tex,n = gen_lvl0_catkeer(loc,fname,lvl,cat)
    data[lvl][cat]['n'] = n
    data[lvl][cat]['fname_tex'] = fname_tex
    
    
    cat = "grondtal"
    loc,fname = _locfname(lvl,cat)
    data[lvl][cat] = _make_entry(loc,fname)
    fname_tex,n = gen_lvl0_catgrondtal(loc,fname,lvl,cat)
    data[lvl][cat]['n'] = n
    data[lvl][cat]['fname_tex'] = fname_tex
    
    cat = "macht"
    loc,fname = _locfname(lvl,cat)
    data[lvl][cat] = _make_entry(loc,fname)
    fname_tex,n = gen_lvl0_catmacht(loc,fname,lvl,cat)
    data[lvl][cat]['n'] = n
    data[lvl][cat]['fname_tex'] = fname_tex
    
    cat = "omvorm"
    loc,fname = _locfname(lvl,cat)
    data[lvl][cat] = _make_entry(loc,fname)
    fname_tex,n = gen_lvl0_catomvorm(loc,fname,lvl,cat)
    data[lvl][cat]['n'] = n
    data[lvl][cat]['fname_tex'] = fname_tex
    
    # Lvl 1
    lvl = 1
    data[lvl] = {}
    
    cat = "keer"
    loc,fname = _locfname(lvl,cat)
    data[lvl][cat] = _make_entry(loc,fname)
    fname_tex,n = gen_lvl1_catkeer(loc,fname,lvl,cat)
    data[lvl][cat]['n'] = n
    data[lvl][cat]['fname_tex'] = fname_tex
    
    cat = "macht"
    loc,fname = _locfname(lvl,cat)
    data[lvl][cat] = _make_entry(loc,fname)
    fname_tex,n = gen_lvl1_catmacht(loc,fname,lvl,cat)
    data[lvl][cat]['n'] = n
    data[lvl][cat]['fname_tex'] = fname_tex
    
    cat = "herleid"
    loc,fname = _locfname(lvl,cat)
    data[lvl][cat] = _make_entry(loc,fname)
    fname_tex,n = gen_lvl1_catherleid(loc,fname,lvl,cat)
    data[lvl][cat]['n'] = n
    data[lvl][cat]['fname_tex'] = fname_tex
    
    cat = "totmacht"
    loc,fname = _locfname(lvl,cat)
    data[lvl][cat] = _make_entry(loc,fname)
    fname_tex,n = gen_lvl1_cattotmacht(loc,fname,lvl,cat)
    data[lvl][cat]['n'] = n
    data[lvl][cat]['fname_tex'] = fname_tex
    
    # Lvl 2
    lvl = 2
    data[lvl] = {}
    
    cat = "omvorm"
    loc,fname = _locfname(lvl,cat)
    data[lvl][cat] = _make_entry(loc,fname)
    fname_tex,n = gen_lvl2_catomvorm(loc,fname,lvl,cat)
    data[lvl][cat]['n'] = n
    data[lvl][cat]['fname_tex'] = fname_tex
    
    cat = "vermeerder"
    loc,fname = _locfname(lvl,cat)
    data[lvl][cat] = _make_entry(loc,fname)
    fname_tex,n = gen_lvl2_catvermeerder(loc,fname,lvl,cat)
    data[lvl][cat]['n'] = n
    data[lvl][cat]['fname_tex'] = fname_tex
    
    cat = "herleid"
    loc,fname = _locfname(lvl,cat)
    data[lvl][cat] = _make_entry(loc,fname)
    fname_tex,n = gen_lvl2_catherleid(loc,fname,lvl,cat)
    data[lvl][cat]['n'] = n
    data[lvl][cat]['fname_tex'] = fname_tex
    
    # Lvl 3
    lvl = 3
    data[lvl] = {}
    
    cat = "bereken"
    loc,fname = _locfname(lvl,cat)
    data[lvl][cat] = _make_entry(loc,fname)
    fname_tex,n = gen_lvl3_catbereken(loc,fname,lvl,cat)
    data[lvl][cat]['n'] = n
    data[lvl][cat]['fname_tex'] = fname_tex
    
    # Combine all tex to 1 tex
    fname_out = "combined_questions"
    loc_out =  "combined/"
    fnames = [ data[lvl][cat]['fname_tex'] for lvl in data  for cat in data[lvl]]
    combine_to_single_tex(loc_out,fname_out,fnames)
    
    loc_scoresheet = loc_out
    fname_scoresheet = "scoresheet"
    make_scoresheet(loc_scoresheet,fname_scoresheet,data)
    
    # Watch out: all latex files have to be run by hand first before combine
    # fnames = [f+'.pdf' for f in fnames]
    # print(fnames)
    # merge_pdfs(fnames,"all_combined.pdf")

if __name__ == "__main__":
    main()