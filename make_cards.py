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

\newcommand\Block[2]{%
\setlength\fboxsep{0pt}\setlength\fboxrule{0.1pt}% delete
\fbox{% delete
\begin{minipage}[c][\dimexpr.5\textheight-2pt\relax][c]{\dimexpr0.3333333\textwidth-3pt\relax}
\centering
#1\par #2
\end{minipage}%
  }% delete
}

\begin{document}

    """
    
def foot():
    return r"""
\end{document}"""

def body():
    return r"""
\thispagestyle{empty}% optional: suppress page numbering
\noindent\Block{text}{caption}\hfill%
\Block{text}{\begin{enumerate}\item a \item b\end{enumerate}}\hfill%
\Block{text}{caption}%
\vfill
\noindent\Block{}{}\hfill%
\Block{}{}\hfill%
\Block{}{}"""



def make_document(pages):
    
    
    
    fname = "tex/out.tex"
    
    thefile = manipulate_files(fname)
    thefile.clearfile()
    
    
    # Head
    thefile.write_appline( preamble() )
    
    # Contents
    content = r"""\thispagestyle{empty}% optional: suppress page numbering
\noindent
"""
    for p in pages[:3]:
        content += r"%s"%(p)+r"""\hfill%
"""
    content += r"""
    \vfill
    \noindent
    """
    for p in pages[:3]:
        content += r"%s"%(p)+r"""\hfill%
"""
    print(content)
    thefile.write_appline( content )
    
    # End file
    thefile.write_appline( foot() )


def make_page(obj):
    
    lvl = obj.get('lvl')
    cat = obj.get('cat')
    vraag = obj.get('vraag')
    antw = obj.get('antw')
    
    antw_txt = r"""\begin{enumerate}"""
    
    for ant in antw:
        antw_txt += r"""\item %s"""%ant
    
    antw_txt += r"""\end{enumerate}"""
    
    page = r"""\Block{%s}{%s}"""%(vraag,antw_txt)
    
    print(page)
    
    
    return page

def main():
    print('vamonos')
    
    lvl = 0
    cat = "keer"
    vraag = r"""Bereken $\lognl[2] (2\cdot 3) $"""
    antw = ["3","2","4","128"]
    obj = {'lvl':lvl,'cat':cat,'vraag':vraag,'antw':antw}
    
    in_obj_list = [ obj for i in range(6) ]
    
    pages = [ make_page(obj) for obj in in_obj_list ]
    
    make_document(pages)
    

if __name__ == "__main__":
    main()