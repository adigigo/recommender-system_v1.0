# This is thew data entry function used to enter data for new users into the recommender system database.
#Use with caution

def data_entry():
    
    flag = True
    data = {}
    
    movie_list = ['The Dark Knight','Thugs of Hindostan','Uri : The Surgical Strike','The Princess Switch','The Incredibles',
                 'The Avengers','Kaakha Kaakha','Parmaanu : The Story of Pokhran','Satyameva Jayathe','Irupathaam Nootandu',
                  'Devasuram','CID Moosa (Seena Thaana)','Geetha Govindam','The Prestige','Fidaa','Premam','Arjun Reddy','Student of the Year',
                  'Madrasapattinam','Manikarnika : The Queen of Jhansi','Spiderman : Homecoming','Jacobinte Swargarajyam','Harry Potter and the Chamber of Secrets',
                  'Kabhi Khushie Kabhi Gham','Chak De India']
                  
    
    while flag:
        
        name = input("Enter your name\n")
        data[name] = {}
        
        for movie in movie_list:
            print(f"Rating for {movie}\n")
            rating = input()
            
            if rating == '':
                continue
                
            else:
                data[name][movie] = float(rating)
                
        
        choice = input("Enter more data? Y/N\n")
        
        if choice == 'y' or choice == 'Y':
            continue
            
        if choice == 'n' or choice == 'N':
            flag = False
            
        
    return data
            
                
            
                
            
            
            

        
        
        
        
    
    
    