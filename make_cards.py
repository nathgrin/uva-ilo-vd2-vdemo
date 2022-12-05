import numpy as np
import matplotlib.pyplot as plt
import json
import random

from misc_func import *

def format_graph(ax):
    
    thelim = list(ax.get_xlim())
    if thelim[0] > -0.5:
        thelim[0] = -0.5
    if thelim[1] < 0.5:
        thelim[1] = 0.5
    ax.set_xlim(thelim)
    thelim = list(ax.get_ylim())
    if thelim[0] > -0.5:
        thelim[0] = -0.5
    if thelim[1] < 0.5:
        thelim[1] = 0.5
    ax.set_ylim(thelim)
    
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['right'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.spines['top'].set_position('zero')

    # remove the ticks from the top and right edges
    ax.xaxis.set_ticks_position('both')
    ax.yaxis.set_ticks_position('both')
    
    ax.grid()
    

def format_formulatable(ax):
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

def make_figures(loc,obj):
    
    
    name = obj.get('name', "noname")
    
    def _inifig():
        fig = plt.figure(figsize=(3,3),frameon=True) # (8.26772,11.6929)
        ax =  fig.add_axes((0, 0, 1, 1))#fig.add_subplot(111)
        
        fig.subplots_adjust(left=0,right=1.,bottom=0,top=1.,wspace=0.,hspace=0.)
        return fig,ax

    ## Formula
    fig,ax = _inifig()
    arratxt =""
    for antw in obj['antw']:
        arraytxt += r"\mathbf{%s}& %s \\"%('a)',antw)
        
    thetext = """%s
    $\begin{array}
    %s
    \end{array}$""".format(obj['vraag'],arraytxt)
    
    ax.text(0.5, 0.5, thetext, fontsize=24, horizontalalignment='left',verticalalignment='center', transform=ax.transAxes)
    
    format_formulatable(ax)
    
    
    fname = "lvl%s_cat%s_%i"%(obj['lvl'],obj['cat'],0)
    plt.savefig(loc+fname+'.png', bbox_inches='tight')
    plt.close(fig)
    
    

def make_pages(loc,fname_list,out_fname=None,
               code_settings={},
               repeat=1,random_order = False):
    if out_fname is None: out_fname = "pages"
    
    # Make code
    code_res = make_code(code_settings)
    code_list = code_res.get('code_list',[])
    print("CODE: a=%i, b=%i, n=%i"%(code_res['a'],code_res['b'],len(code_list)))
    
    # print(code_res)
    
    ## fname_list to page
    from PIL import Image,ImageDraw,ImageFont

    width, height = int(11.693 * 300),int(8.268 * 300) # A4 at 300dpi
    cellw,cellh = width//5,height//4
    imagew,imageh = int(1.9*300),int(1.9*300)
    # imagew,imageh = int(1.8*300),int(1.8*300)
    padw,padh = (cellw-imagew)//2,(cellh-imageh)//2
    codeImw,codeImh = int(0.2*300),int(0.2*300)
    
    if random_order:
        random.shuffle(fname_list)
        random.shuffle(code_list)
    
    if repeat > 1:
        old_code_list = code_list[:]
        old_fname_list = fname_list[:]

        for i in range(repeat-1):
            code_list.extend(old_code_list)
            fname_list.extend(old_fname_list)
        
    
    
    groups = [fname_list[i:i+10] for i in range(0, len(fname_list), 10)]
    groups_code = [code_list[i:i+10] for i in range(0, len(code_list), 10)]
    
    page_list = []
    
    # For each page
    for ind_group, group in enumerate(groups):
        group_code = groups_code[ind_group]
        print(ind_group,group,group_code)
        page = Image.new('RGB', (width, height), 'white')
        draw = ImageDraw.Draw(page)
            
        xi,yrow = 0,0
        order = range(len(group))
        for ind_card in order:
            card = group[ind_card]
            code = group_code[ind_card]
            
            for toggle in range(2):
                fname = card[toggle]
                # print(xi,ytoggle,yrow)
                xcoord = padw + xi*cellw
                ycoord = padh + (yrow+toggle)*cellh
                # print(xcoord,ycoord)
                with Image.open(fname) as Im:
                    if toggle == 0:
                        Im = Im.rotate(180)
                    Im = Im.resize((imagew,int(Im.height*imagew/Im.width)))
                    page.paste(Im, box=(xcoord, ycoord))
                
                code_x,code_y = xcoord-padw+codeImw//2,ycoord-padh//2
                with Image.open(code) as codeIm:
                    if toggle == 0:
                        codeIm = codeIm.rotate(180)
                        code_x = -1*code_x + (2*xi+1)*cellw
                        code_y = -1*code_y + (2*yrow+1)*cellh
                        code_x += -codeImw
                        code_y += -codeImh
                    codeIm = codeIm.resize((codeImw,int(codeIm.height*codeImw/codeIm.width)))
                    page.paste(codeIm, box=(code_x,code_y))
                # draw.text((xcoord-padw//2,ycoord),code,font=font, fill=(0, 0, 0, 255))

            if xi != 4:
                xi += 1
            else:
                xi = 0
                yrow += 2
            
        
        lw = 20
        # draw.line( (0, page.size[1], page.size[0], 0) ,width=lw, fill=128)
        for i in range(6):
            draw.line( [(i*cellw,0),(i*cellw,height)] ,width=lw, fill=256)
        for i in range(5):
            draw.line( [(0,i*cellh),(width,i*cellh)] ,width=lw, fill=256)
        
        save_fname = loc+out_fname+'_{}.pdf'.format(ind_group)
        page.save(save_fname)
        page_list.append(save_fname)
    
    merge_pdfs(page_list,loc+out_fname+".pdf")


def lognl(x):
    return  r"{}^{\scalebox{0.5}{%i}}\!}\log"%(x)
    

def main():
    
    loc = ""
    
    obj = {'lvl':0,'cat':"keer",'vraag':"Bereken %s, kies uit:",'antw':['3','2','4','8']}
    in_obj_list = [obj for x in range(2)]
    
    # Make figures per object
    print("> Make figures")
    if True:
        for i in range(len(in_obj_list)):
            obj = in_obj_list[i]
            
            make_figures(loc+'figures/',obj)
    
    input("a")
    
    # Combine figures to page
    print("> Make Pages")
    out_fname = name
    fnames = make_fname_list(loc+"figures/",in_obj_list)
    
    input("b")
    
    make_pages(loc,fnames,out_fname=out_fname,
               code_settings={},random_order=True)#,repeat=2)
    
    
if __name__ == "__main__":
    main()