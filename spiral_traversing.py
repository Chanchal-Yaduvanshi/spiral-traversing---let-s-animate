#Print First row, Last column, Last row in reverse order, First column in reverse order
import random
import turtle
turtle.bgcolor("black")
tur = turtle.Turtle()
width = 5
height = 7
dot_distance = 25

tur.penup()
list_color = ["white", "yellow", "brown", "red", "blue", "green", "orange", "pink", "violet", "grey", "cyan"]
tur.setpos(-250,250)



def spiral(m,n) :         #m-no of rows, n=no of columns
    i=0                     #starting index of row
    j=0                     #starting index of column
    flag = 0

    # tur.color("White")
    col = random.randint(0,10)
    tur.color(list_color[col])

    while(i<m and j<n) :
        
        if(flag==1) :
            tur.right(90)
        
        #Printing first row from the remaining rows
        for index in range(j, n) :
            tur.dot()
            tur.forward(dot_distance)
        i += 1
        flag = 1
        

        #Printing last column from the remaining columns
        tur.right(90)
        col = random.randint(0,10)
        tur.color(list_color[col])
        for index in range(i, m) :
            tur.dot()
            tur.forward(dot_distance)
        n = n-1
        

        #Printing last row from the remaining rows in reverse order
        tur.right(90)
        col = random.randint(0,10)
        tur.color(list_color[col])
        if(i<m) :
            for index in range(n-1, j-1, -1) :
                tur.dot()
                tur.forward(dot_distance)
            m = m-1
        

        #Printing first column from the remaining columns in reverse order
        tur.right(90)
        col = random.randint(0,10)
        tur.color(list_color[col])
        if(j<n) :
            for index in range(m-1, i-1, -1) :
                tur.dot()
                tur.forward(dot_distance)
            j = j+1


# spiral(20,20)
R = 20 
C = 20
spiral(R,C)
turtle.done()