import matplotlib.pyplot as plt


def generate_numberpics(loc='numberpics/'):
    
    
    for i in range(50):
        
        for j in range(2):
            fig = plt.figure(figsize=(2,2),frameon=True) # (8.26772,11.6929)
            ax =  fig.add_axes((0, 0, 1, 1))#fig.add_subplot(111)
            
            fig.subplots_adjust(left=0,right=1.,bottom=0,top=1.,wspace=0.,hspace=0.)
            
            ax.spines['left'].set_color('none')
            ax.spines['left'].set_position('center')
            ax.spines['right'].set_color('none')
            ax.spines['right'].set_position('center')
            ax.spines['bottom'].set_color('none')
            ax.spines['bottom'].set_position('center')
            ax.spines['top'].set_color('none')
            ax.spines['top'].set_position('center')
            ax.set_xticks([], [])
            ax.set_yticks([], [])
            
            if j:
                the_text = "$%i$"%i
                fname = '%i.jpg'%i
            else:
                the_text = r"$\overline{%i}$"%i
                fname = 'ol_%i.jpg'%i
            ax.text(0.5,0.5,the_text, size=88, horizontalalignment='center', verticalalignment='center',transform =ax.transAxes)
            fig.savefig(loc+fname)#,bbox_inches='tight' )
            plt.close(fig)
        
def main():
    generate_numberpics()
    
if __name__ == "__main__":
    main()
