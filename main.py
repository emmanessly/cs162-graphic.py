import matplotlib.pyplot as plot
# set up your lists
#decided to have some fun with this...so set this up as a pie chart calculating the sizes of 3 planets and one moon:
#earth, mars, europa, and venus
numlist = [37.7, 10, 2.3, 50] #diameter of one object divided by sum of diameter of other objects in miles
namelist = ['earth', 'mars', 'europa', 'venus']
colorlist = ['#D1E2E8', '#DED4F3', '#C0C8CF', '#FFF0F5' ] #googled how to add specific colors in pycharm and found the hex codes on color-name.com
explodelist = [0.01, 0.01, 0.01, 0.01]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist,
    	explode = explodelist, startangle = 360) #changed the start angle to the best visually accurate representation of the sizes
plot.axis('equal')
plot.savefig('piechart.png')

