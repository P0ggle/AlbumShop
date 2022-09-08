import matplotlib.pyplot as plt

def user_selection():
    print("-----------------ALBUM SHOP-----------------")
    print("1: Display List of records                |")
    print("2: Price threshold                        |")
    print("3: Amount of records in each genre type   |")
    print("4: Add new record                         |")
    print("5: Modify Stock                           |")
    print("6: Bar Chart for genre amount             |")
    print("-------------------------------------------")
#user selection options
#user selection input   
user_selection()       

def read_file():
    infile = open("record_data.txt")
        
    # optimised method using .split()
    for line in infile:
        if not line.startswith("#"): # ignore the header comment in the data file
            line = line.rstrip('\n').split(', ') 
            album.append(line) # each element now contains a 'line
    infile.close()
album = []    
    # ********************************************************************
    # ENTRY POINT TO PROGRAM
    # define an empty list with scope across the functions
    # read in data for processing within the menu
read_file()
#converting album data into a new list caleld datalist
data_list = album
#defining the keys for the upcoming dictionary 
keys = ['Artist','Title','Genre','PlayLength', 'Condition', 'Stock', 'Cost']
#creating a new empty list 
res = []
#looping through the datalist assigning each section a key from the keys list and zipping into a dictionary for future use
for d in data_list:
    res.append(dict(zip(keys, d)))
    

#Option 1
def print_summary():
#defined total cost to allow a addition to occur within loop  
    total_cost = 0
#printing out the dictionary with a seperating line by line 
  
    for item in range(len(album)):
        print(album[item][0],album[item][1], \
            album[item][2], album[item][3], album[item][4], album[item][5], album[item][6], sep=' -> ')
#multiply stock by the cost and then adds it to the total cost variable starting at 0               
        total_cost += float(res[item]['Stock']) * float(res[item]['Cost'])
#outputs the length of the album array  
        total_stock = len(album)    
#prints total stock and total cost and formatting it to 2 decimal places      
    print('\nTotal Titles:',format(total_stock,'.2f'))
    print('Total Cost:',format(total_cost,'.2f'))
     
     
#Option 2
def threshold():
#user input for threshold
    threshold_input = float(input("Input Threshold: "))
#will loop through the dictionary and if the threshold is met it will print that rows artist and cost with a seperator     
    print("---------------", "Records above", threshold_input, "---------------")
    for item in range(len(res)):
      if threshold_input < float(res[item]['Cost']):
        print(res[item]['Artist'], res[item]['Cost'], sep=' -> ')
    print("--------------------------------------------------")
                                    
#Option 3
def genre_count():
#get file object reference to the file
    file = open("record_data.txt", "r")
#read content of file to string
    album = file.read()
#get number of occurrences of the substring in the string
    Rock = album.count("Rock")
    Classical = album.count("Classical")
    Pop = album.count("Pop")
    Jazz = album.count("Jazz")
    Spoken_Word = album.count("Spoken Word")
#showing the user the amount of genres count and showing the occurrence of substring within the album list
    print("Total Genres Count")
    print("------------------")
    print("Rock:", Rock)
    print("Classical:", Classical)
    print("Pop:", Pop)
    print("Jazz:", Jazz)
    print("Spoken Word:", Spoken_Word)
    print("------------------")

#Option 4
def new_record():
#user input for the append
    artist_input = input("Artist Name?")
    title_input = input("Title Name?")
    genre_input = input("genre Name?")
    playlength_input = input("play length Name?")
    condition_input = input("condition Name?")
    stock_input = int(input("stock Name?"))
    cost_input = float(input("cost Name?"))
#appending the res dictionary with a new dictionary within the nested dictionary based on the above user input
    res.append({
                'Artist': artist_input,
                'Title': title_input,
                'Genre': genre_input,
                'PlayLength': playlength_input,
                'Condition': condition_input,
                'Stock':    stock_input,
                'Cost': cost_input,
            })
#defined total cost to allow a addition to occur within loop   
    total_cost = 0
#printing out the dictionary with a seperating line by line  
    for item in range(len(res)):
        print(res[item]['Artist' ], res[item]['Title' ],res[item]['Genre' ],res[item]['PlayLength' ], res[item]['Condition' ], \
            res[item]['Stock' ], res[item]['Cost'], sep=' -> ')
#multiply stock by the cost and then adds it to the total cost variable starting at 0   
        total_cost += float(res[item]['Stock']) * float(res[item]['Cost'])
#outputs the length of the dictionary called res       
        total_stock = len(res) 
#prints total stock and total cost and formatting it to 2 decimal places         
    print('\nTotal Stock:',format(total_stock,'.2f'))
    print('Total Cost:',format(total_cost,'.2f'))
    
#option 5
def modifyStock(): 
    titleinput = input("Enter Title You want to modify ")
    modify = [] 
    for item in range(len(res)):
        if titleinput == res[item]['Title']:
            modify.append({
            'Artist': res[item]['Artist'],
            'Title': res[item]['Title'],
            'Genre': res[item]['Genre' ],
            'PlayLength': res[item]['PlayLength'],
            'Condition': res[item]['Condition'],
            'Stock': res[item]['Stock'],
            'Cost': res[item]['Cost']
            })      
            # print(res[item]['Artist' ], res[item]['Title' ],res[item]['Genre' ],res[item]['PlayLength' ], res[item]['Condition' ], \
            # res[item]['Stock' ], res[item]['Cost'], sep=' -> ') 
    print(modify)
    stockinput = int(input("Change Increase or Decrease: "))
    
    for item in range(len(modify)):
        if (stockinput + int(modify[item]['Stock'])) < 0:
                #OutOfStockPrintMessage
                print("This album is not available anymore.")
                modify[item]['Stock'] = 0  #no negative numbers   
        else:
            #update album stock
                alteredStock = int(modify[item]['Stock']) + stockinput
                modify[item]['Stock'] = alteredStock
                print("The New Stock is: {0}".format(alteredStock))
         
#option 6                      
def barchart():
    file = open("record_data.txt", "r")
    #read content of file to string
    album = file.read()
        
    Rock = album.count("Rock")
    Classical = album.count("Classical")
    Pop = album.count("Pop")
    Jazz = album.count("Jazz")
    Spoken_Word = album.count("Spoken Word")
        
    left = ["rock", "classical", "pop", "jazz", "spoken word"]
    height = [Rock, Classical, Pop, Jazz, Spoken_Word]
        
    plt.bar(left, height)
        
    plt.show()
  
user_input = ""
while user_input != "7":
    #if user doesnt input 7 continue
    user_input = input("Option 1 - 6 | Enter 7 to quit: ")
    if user_input == "1":
        print_summary()
        user_selection()  
    elif user_input == "2":
        threshold()
        user_selection()  
    elif user_input == "3":
        genre_count()
        user_selection()
    elif user_input == "4":
        new_record()
        user_selection()
    elif user_input == "5":
        print_summary()
        modifyStock()
        user_selection()
    elif user_input == "6":
        barchart()
        user_selection()
    elif user_input == "7":
        break;
    else:
        user_selection()
print("Goodbye!")