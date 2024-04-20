import matplotlib.pyplot as plt

def main():
    x_coords=[0,1,2,3,4]
    y_coords=[0,3,1,5,2]

    plt.title("Sales by Year")
    plt.xlabel("Year")
    plt.ylabel("Sales")

    plt.grid(True)

    plt.xlim(xmin=0,xmax=5) # x eksenindeki limitleri belirler.
    plt.ylim(ymin=0,ymax=6) # y eksenindeki limitleri belirler.

    plt.xticks([0,1,2,3,4],['2016','2017','2018','2019','2020'])
    plt.yticks([0,1,2,3,5],['$0m','$1m','$2m','$3m','$5m'])

    #çizgi grafiği oluşturur.
    plt.plot(x_coords,y_coords,marker="o") #(x,y) koordinatlarına nokta koyar. 

    plt.show() #çizgi grafiği görüntüler.

# main()    


def main0():
    left_edges=[0,10,20,30,40]
    heights= [100,200,300,400,500]
    bar_width=5 #normalde varsayılan  genişlik 0.8'dir.


    #Renk kodları:
    # 'b' = blue
    # 'g' = green
    # 'r' = red
    # 'c' = cyan
    # 'm' = magenta
    # 'y' = yellow
    # 'k' = black
    # 'w' = white

    plt.bar(left_edges,heights,bar_width,color= ('y','g','b','c','k'))
    plt.show()

# main0()


def main1():
    values= [12,80,70,40]
    slices_labels= ["12","80","70","40"]
    plt.title("Sales by Quarter")
    plt.pie(values,labels=slices_labels,colors=("r","g","b","c"))
    plt.show()

main1()

