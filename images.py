import imagetools
import copy
import math
##### Generating images

def rainbow(): #output an image; x, y (0--255)
    # blue-128
    # red-equal to its x coordinate(column)
    # green-equal to its y coordinate(row)
    #[[[0,0,128],[0,1,128]],[[1,0,128],[1,1,128]],[[2,0,128],[2,1,128]],[[3,0,128],[3,1,128]]]
    result = []
    for column in range(256):
        sum = [[column, 0, 128]]
        for row in range(1,256):
            pixal = [column, row, 128]
            sum = sum + [pixal] #one list [[],[],[]...]
        if result == []:
            result = [sum]
        else:
            result = result + [sum]
    return result 



def formula_art():
    result = []
    for column in range(1000):
        sum = []
        for row in range(1000):
            pixal = [(column % (row + 1)) % 256, (row % (column + 1)) % 256, 128]
            if sum == []:
                sum = [pixal]
            else:
                sum = sum + [pixal] #one list [[],[],[]...]
        if result == []:
            result = [sum]
        else:
            result = result + [sum]
    return result 
    

def my_formula_art(): # what does fibonacci sequence(A.K.A: mathematical formula of nature) look like in RGB? 
    result = []      #only 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233 (first 13th number) satisfy 
    def fibonacci(number): # return the nth number in the sequence. If number > 13, count from beginning, repeat
        sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
        if number > 13:
            nth_number = number % 13 - 1
            return sequence[nth_number]
        else:
            return number 
    dict = {1:1,2:1,3:2,4:3,5:5,6:8,7:13,8:21,9:34,10:55,11:89,12:144,13:233}
    for column in range(500):
        sum = []
        R = fibonacci(column)
        nth_number_R = column % 13 #=key
        if nth_number_R == 0:
            nth_number_R = 13
        for row in range(500):
            G =fibonacci(row)
            nth_number_G = row % 13
            if nth_number_G == 0:
                nth_number_G = 13
                # now I want B to be the number that has the same distance as R to G in fibonacci sequence.
                # and I want the neighbors for RGB stay the same: R G B or B G R(corresponding number)
            distance = abs(nth_number_G - nth_number_R) 
            if nth_number_G > nth_number_R:
                if nth_number_G + distance > 13:
                    nth_number_B = (nth_number_G + distance) % 13
                else:
                    nth_number_B = nth_number_G + distance
                B = dict[nth_number_B]
            elif nth_number_G < nth_number_R:
                if nth_number_G - distance < 0:
                    left = -1 * (nth_number_G - distance)
                    if left > 13:
                        left_finalturn = left % 13
                        nth_number_B = 14 - left_finalturn
                    else:
                        nth_number_B = 14 - left
                else:
                    nth_number_B = nth_number_G - distance
            else:
                nth_number_B = nth_number_G
                B = dict[nth_number_B]
            pixal = [R, G, B]
            if sum == []:
                sum = [pixal]
            else:
                sum = sum + [pixal] #one list [[],[],[]...]
        if result == []:
            result = [sum]
        else:
            result = result + [sum]
    return result 
#pic[x][y]---pixal = [xth number in fibonacci, yth number in fibonacci, equal dictance's number in fibonacci]
# first 13 number in fibonacci 



##### Manipulating images


def width(array): #output the width of the image--column
    result = 0
    for _ in array:
        result += 1
    return result 

def height(array):
    result = 0
    for _ in array[0]:
        result += 1
    return result 

def grayscale(pic): # don't modify input list!!!
   # RGB equals to the average of original ; use round()
    result = []
    for column in pic:
        row = []
        for pixel in column:
            R, G, B = pixel[0], pixel[1], pixel[2]
            new_number = round((R + G + B) / 3) 
            new_pixel = [new_number, new_number, new_number] #gray
            if row == []:
                row = [new_pixel]
            else:
                row = row + [new_pixel]
        if result == []:
            result = [row]
        else:
            result = result + [row]
    return result 

def leave_purple(pic): #don't modify input list!! roughly...  keep tring.....!
    result = []
    for column in pic:
        row = []
        for pixel in column:
            R, G, B = pixel[0], pixel[1], pixel[2]
            if (100 <= R <= 256 and 3 <= G <= 80 and 150 <= B <= 256) or (180 <= R <= 256 and 150 <= G <= 180 and 180 <= B <= 256) or (100 <= R <= 130 and 30 <= G <= 50 and 100 <= B <= 140):
                new_pixel = pixel[ : ]
            else:
                new_number = round((R + G + B) / 3) 
                new_pixel = [new_number, new_number, new_number]
            if row == []:
                row = [new_pixel]
            else:
                row = row + [new_pixel]
        if result == []:
            result = [row]
        else:
            result = result + [row]
    return result 

def crop(pic, left, top, right, bottom): #left-small column; right-large column; top-large row; bottom-small row
    def width(array): 
        result = 0
        for _ in array:
            result += 1
        return result 
    def height(array):
        result = 0
        for _ in array[0]:
            result += 1
        return result 
    column_total = width(pic)
    row_total = height(pic)
    pic_remove_column = copy.deepcopy(pic[left : (column_total - right + 1)]) #the column after changes
    result = []
    for column in pic_remove_column:
            remove_row = copy.deepcopy(column[bottom : (row_total - top + 1)]) #the row after changes
            if result == []:
                result = [remove_row]
            else:
                result = result + [remove_row]
    return result 

def enlarge(pic, factor):
    result = []
    for column in pic:
        result_row = []
        for row in column:
            row1 = row[ : ] #copy
            row1 = [row1] * factor #enlarge row
            if result_row == []:
                result_row = row1
            else:
                result_row = result_row + row1
        column1 = [result_row] * factor  #enlarge column
        if result == []:
            result = column1
        else:
            result = result + column1
    return result

def blur(pic, radius):  #it takes a tiny liitle longer moment to load, but it worksss!!!
    def width(array): 
        result = 0
        for _ in array:
            result += 1
        return result 
    def height(array):
        result = 0
        for _ in array[0]:
            result += 1
        return result 
    total_column = width(pic) 
    total_row = height(pic)
    result_singlelist = []
    for a in range(total_column): #0,2,3...maximum column
        for b in range(total_row): 
            pixel_new = pic[a][b][ : ] #each target pixel [R,G,B], copy pixel 
            R_target, G_target, B_target = pixel_new[0], pixel_new[1], pixel_new[2]
            sum_R, sum_G, sum_B = [], [] ,[]
            number = 0
            for x in range(a - radius, a + radius + 1): #if x > a + radius, it won't be possible. so we just need to try pixels that have conditions like this..
                if x >= 0 and x <= (total_column - 1):
                    for y in range(b - radius, b + radius + 1): #each pixel in pic
                        if y >= 0 and y <= (total_row - 1):
                            pixel_other_new = pic[x][y][ : ]
                            if math.sqrt((x - a) ** 2 + (y - b) ** 2) <= radius:
                                number += 1
                                if sum_R == []:
                                    sum_R, sum_G, sum_B = pixel_other_new[0], pixel_other_new[1], pixel_other_new[2]
                                else:
                                    sum_R, sum_G, sum_B = sum_R + pixel_other_new[0], sum_G + pixel_other_new[1], sum_B + pixel_other_new[2]
            R_target, G_target, B_target = round(sum_R / number), round(sum_G / number), round(sum_B / number)
            pixel_new = [[R_target, G_target, B_target]]
            if result_singlelist == []:
                result_singlelist = [pixel_new]
            else:
                result_singlelist += [pixel_new] # it is a list like this: [[[R,G,B]],[[R,G,B]],[[R,G,B]]]. I want to add the number of row of [[R,G,B]] together and makes it a column, repeat the number of column times
    result = []
    times = 0  
    while times < total_column: #remove + append ; first add the ls from the original ls, then append the reuslt to the new ls, then remove them from the first ls
        new_ = []
        for i in range(total_row): #0,1,2,....row-1, number of row of number's sum
            if new_ == []:
                new_ = result_singlelist[i] 
            else:
                new_ += result_singlelist[i] # a complete row
        result.append(new_)
        result_singlelist = result_singlelist[total_row: ]
        times += 1
    return result    

def my_effect(pic): #switch R and B for each pixel (turn the morning to night...gets darker)
    result = []
    for column in pic:
        result_row = []
        for pixel in column:
            pixel_1 = pixel[ : ]
            pixel_1[0], pixel_1[2] = pixel_1[2], pixel_1[0]
            new_pixel = [pixel_1[0], pixel_1[1], pixel_1[2]]
            if result_row == []:
                result_row = [new_pixel]
            else:
                result_row += [new_pixel]
        column1 = [result_row] 
        if result == []:
            result = column1 
        else:
            result += column1 
    return result 

