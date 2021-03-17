#importing the libraries
import pygame 
import random 
import time
import tkinter as tk
from tkinter import messagebox
import time
pygame.font.init() 
 
#set up the window 
win = pygame.display.set_mode((900, 650)) 

# Title and Icon 
pygame.display.set_caption("SORTING VISUALISER") 
run = True

# Window size and some initials
global RED, PINK, LIGHT_GREEN, TURQUOISE, BLUE, YELLOW,GREY,BLACK,title_font,button_font
RED=(255,0,0)
PINK=(255,182,193)
LIGHT_GREEN=(0,204,102)
TURQUOISE=(175,238,238)
LIGHT_BLUE=(0,0,153)
YELLOW=(255,255,0)
GREY=(128,128,128)
BLACK=(0,0,0)
WHITE=(255,255,255)
ORANGE=(255,102,0)

arr =[0]*151
arr_colors =[LIGHT_GREEN]*151
colors =[PINK ,RED, LIGHT_BLUE , LIGHT_GREEN,YELLOW,TURQUOISE] 
title_font = pygame.font.SysFont("comicsans", 70) 
button_font = pygame.font.SysFont("comicsans", 20)
prompt_font = pygame.font.SysFont("comicsans", 25)


def popup():
        root = tk.Tk()
        root.withdraw()
        messagebox.askokcancel("Completion","All the numbers have been sorted. Press Enter to get a new random input")

# Function to generate new arr 
def regenerate(): 
    for i in range(1, 151):  
        arr[i]= random.randrange(1, 75)
        arr_colors[i]= colors[0]
 
def replot_contents(): 
    win.fill((255, 255, 255)) 
    draw()
    create_buttons_and_title()
    pygame.display.update() 
    #pygame.time.delay(10) 

def bubble(arr):
    fixed_text()
    for i in range(0,len(arr) - 1,1): 
        for j in range(0,len(arr) - i - 1,1):
            pygame.event.pump()
            replot_contents()
            if arr[j]>=arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                replot_contents()
                arr_colors[j]=colors[1]
                arr_colors[j+1]=colors[1]
                replot_contents()
               # pygame.time.delay(10)
                arr_colors[j]=colors[0]
                arr_colors[j+1]=colors[0]
                replot_contents()
                    
            elif arr[j]<arr[j+1]:
                replot_contents()    
                arr_colors[j]=colors[4]
                arr_colors[j+1]=colors[4]
                replot_contents()
                #pygame.time.delay(10)
                arr_colors[j]=colors[0]
                arr_colors[j+1]=colors[0]
                replot_contents()
        arr_colors[j+1]=colors[3]    
    arr_colors[0]=colors[3]
    replot_contents()

def selection(arr):
        fixed_text()
        for i in range(0,len(arr),1):
            #replot_contents()    
            pygame.event.pump()
            replot_contents()
            minimum_value_index=i
            arr_colors[i]=colors[2]
            for j in range(i+1,len(arr),1):
                if arr[minimum_value_index] >arr[j]:
                    minimum_value_index=j
            arr_colors[minimum_value_index]=colors[5]
##            replot_contents()
##            pygame.time.delay(5)
            arr[i],arr[minimum_value_index]=arr[minimum_value_index],arr[i]
            replot_contents()
            arr_colors[minimum_value_index]=colors[0]
            pygame.time.delay(50)
            arr_colors[i]=colors[3]
            replot_contents()
                
        
        
def insertionSort(arr): 
    fixed_text()
    for i in range(1, len(arr)):    
        pygame.event.pump() 
        replot_contents() 
        key = arr[i] 
        arr_colors[i]= colors[2] 
        j = i-1
        while j>= 0 and key<arr[j]: 
            arr_colors[j]= colors[2] 
            arr[j + 1]= arr[j] 
            replot_contents() 
            arr_colors[j]= colors[3] 
            j = j-1
        arr[j + 1]= key 
        replot_contents() 
        arr_colors[i]= colors[0]
    arr_colors[len(arr)-1]=colors[3]
    replot_contents()

    
def quicksort(arr, l, r): 
    if l<r: 
        pi = partition(arr, l, r) 
        quicksort(arr, l, pi-1) 
        replot_contents() 
        for i in range(0, pi + 1): 
            arr_colors[i]= colors[3] 
        quicksort(arr, pi + 1, r)
        
    elif l==r==len(arr)-1:
        arr_colors[l:r]=colors[3]
        arr_colors[r]=colors[3]
        replot_contents()
    
# Function to partition the arr 
def partition(arr, low, high): 
    pygame.event.pump()  
    pivot = arr[high] 
    arr_colors[high]= colors[2] 
    i = low-1
    for j in range(low, high): 
        arr_colors[j]= colors[1] 
        replot_contents() 
        arr_colors[high]= colors[2] 
        arr_colors[j]= colors[0] 
        arr_colors[i]= colors[0] 
        if arr[j]<pivot: 
            i = i + 1
            arr_colors[i]= colors[1] 
            arr[i], arr[j]= arr[j], arr[i] 
    replot_contents() 
    arr_colors[i]= colors[0] 
    arr_colors[high]= colors[0] 
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  
    return ( i + 1 ) 

def create_buttons_and_title():
        pygame.draw.rect(win, (255,165,0), (290, 60, 100, 30))
        pygame.draw.rect(win, (255,165,0), (415, 60, 100, 30))
        pygame.draw.rect(win, (255,165,0), (540, 60, 100, 30))
        pygame.draw.rect(win, (255,165,0), (665, 60, 100, 30))
        pygame.draw.rect(win, (255,165,0), (790, 60, 100, 30))

        title=title_font.render(f"Sorting Algorithm Visualizer", 1, (0,0,255))
        prompt=prompt_font.render(f"Select the Algorithm to Visualize", 1, (0,0,0))
        randomize=button_font.render(f"New Array", 1, (0,0,0))
        bubble=button_font.render(f"Bubble Sort", 1, (0,0,0))
        insertion=button_font.render(f"Insertion Sort", 1, (0,0,0))
        selection=button_font.render(f"Selection Sort", 1, (0,0,0))
        quick=button_font.render(f"Quick Sort", 1, (0,0,0))

        
        win.blit(title, (120, 0))
        win.blit(prompt, (5, 65))
        win.blit(randomize, (306, 68))
        win.blit(bubble, (426, 68))
        win.blit(insertion, (549, 68))
        win.blit(selection, (671, 68))
        win.blit(quick, (805, 68))
        pygame.display.update()

            
def make_blank(win):
        win.fill((255,255,255))
        create_buttons_and_title()
        
# Function to Draw the arr values 
def draw(): 
    element_width =(width-150)//150
    pygame.draw.line(win, (0, 0, 0), (0, 95),(900, 95), 6) 
    
    # Drawing the arr values as lines 
    for i in range(1, 151): 
        pygame.draw.line(win, arr_colors[i], (boundry_arr * i-3, 100),(boundry_arr * i-3, arr[i]*boundry_grp + 100), element_width) 

def fixed_text():
    pass
# Program should be run 
# continuously to keep the window open


regenerate()
global boundary_arr,boundary_grp
global width, length

boundry_arr = 900 // 150
boundry_grp = 600 // 100
width = 900
length = 600

area_1 = pygame.Rect(290, 60, 100, 30)
area_2 = pygame.Rect(415, 60, 100, 30)
area_3 = pygame.Rect(540, 60, 100, 30)
area_4 = pygame.Rect(665, 60, 100, 30)
area_5 = pygame.Rect(790, 60, 100, 30)

win.fill((255,255,255))
create_buttons_and_title()
#fixed_text()   
while run: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                                if area_1.collidepoint(event.pos):
                                    make_blank(win)
                                    regenerate()
                                elif area_2.collidepoint(event.pos):
                                    bubble(arr)
                                    popup()
                                    make_blank(win)
                                    regenerate()
                                elif area_3.collidepoint(event.pos):
                                    insertionSort(arr)
                                    popup()
                                    make_blank(win)
                                    regenerate()
                                elif area_4.collidepoint(event.pos):
                                    selection(arr)
                                    popup()
                                    make_blank(win)
                                    regenerate()
                                elif area_5.collidepoint(event.pos):
                                    quicksort(arr,0,len(arr)-1)
                                    popup()
                                    make_blank(win)
                                    regenerate()    
                        
                        
    draw() 
    pygame.display.update() 
    
pygame.quit() 
