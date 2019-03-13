from math import*

#Sample Dataset [To be used if the user decides against adding data]
data = {'shankar dharshan': {'The Dark Knight': 8.0,
  'Uri : The Surgical Strike': 8.0,
  'The Avengers': 8.0,
  'Kaakha Kaakha': 7.0,
  'Parmaanu : The Story of Pokhran': 7.0,
  'Satyameva Jayathe': 7.0,
  'Geetha Govindam': 3.0,
  'The Prestige': 8.0,
  'Premam': 9.0,
  'Arjun Reddy': 8.0,
  'Student of the Year': 5.0,
  'Madrasapattinam': 8.0,
  'Spiderman : Homecoming': 5.0,
  'Jacobinte Swargarajyam': 7.0,
  'Chak De India': 9.0},
 'ashwin': {'The Dark Knight': 7.0,
  'Thugs of Hindostan': 5.0,
  'Uri : The Surgical Strike': 9.0,
  'The Incredibles': 8.0,
  'The Avengers': 9.5,
  'CID Moosa (Seena Thaana)': 8.5,
  'Geetha Govindam': 9.0,
  'Fidaa': 7.5,
  'Premam': 8.0,
  'Arjun Reddy': 6.0,
  'Student of the Year': 8.5,
  'Spiderman : Homecoming': 8.5,
  'Harry Potter and the Chamber of Secrets': 8.0,
  'Kabhi Khushie Kabhi Gham': 9.5,
  'Chak De India': 8.0},
 'nitya': {'Uri : The Surgical Strike': 9.0,
  'The Incredibles': 8.0,
  'The Avengers': 7.0,
  'Premam': 8.0,
  'Student of the Year': 3.0,
  'Jacobinte Swargarajyam': 7.0,
  'Harry Potter and the Chamber of Secrets': 9.0},
 'akash jayakumar': {'The Dark Knight': 10.0,
  'Thugs of Hindostan': 3.0,
  'Uri : The Surgical Strike': 10.0,
  'The Incredibles': 8.0,
  'The Avengers': 9.0,
  'Kaakha Kaakha': 8.0,
  'Geetha Govindam': 3.0,
  'The Prestige': 10.0,
  'Premam': 5.0,
  'Arjun Reddy': 5.0,
  'Student of the Year': 6.0,
  'Madrasapattinam': 9.0,
  'Manikarnika : The Queen of Jhansi': 6.0,
  'Spiderman : Homecoming': 8.0,
  'Harry Potter and the Chamber of Secrets': 8.0,
  'Kabhi Khushie Kabhi Gham': 8.0,
  'Chak De India': 9.0},
 'arun': {'Uri : The Surgical Strike': 7.0,
  'The Incredibles': 8.0,
  'The Avengers': 8.0,
  'Irupathaam Nootandu': 6.0,
  'CID Moosa (Seena Thaana)': 8.0,
  'Geetha Govindam': 9.0,
  'The Prestige': 8.0,
  'Premam': 9.0,
  'Arjun Reddy': 9.0,
  'Student of the Year': 9.0,
  'Madrasapattinam': 8.0,
  'Spiderman : Homecoming': 8.0,
  'Jacobinte Swargarajyam': 10.0,
  'Harry Potter and the Chamber of Secrets': 8.0},
 'abhishek': {'The Dark Knight': 7.5,
  'The Incredibles': 7.0,
  'The Avengers': 8.4,
  'CID Moosa (Seena Thaana)': 8.0,
  'Geetha Govindam': 7.6,
  'Premam': 6.0,
  'Student of the Year': 7.8,
  'Madrasapattinam': 8.0,
  'Spiderman : Homecoming': 9.0,
  'Jacobinte Swargarajyam': 9.0,
  'Harry Potter and the Chamber of Secrets': 9.1,
  'Kabhi Khushie Kabhi Gham': 9.4,
  'Chak De India': 6.0},
 'adarsh balakrishnan': {'The Dark Knight': 8.5,
  'Thugs of Hindostan': 3.0,
  'The Incredibles': 8.5,
  'The Avengers': 8.0,
  'Devasuram': 7.25,
  'CID Moosa (Seena Thaana)': 7.0,
  'Geetha Govindam': 6.5,
  'The Prestige': 7.75,
  'Premam': 7.5,
  'Student of the Year': 7.0,
  'Madrasapattinam': 7.0,
  'Spiderman : Homecoming': 7.5,
  'Jacobinte Swargarajyam': 7.75,
  'Harry Potter and the Chamber of Secrets': 7.0},
 'nikita menon': {'The Dark Knight': 10.0,
  'Thugs of Hindostan': 0.5,
  'Uri : The Surgical Strike': 9.0,
  'The Incredibles': 8.0,
  'The Avengers': 8.5,
  'CID Moosa (Seena Thaana)': 7.0,
  'Premam': 10.0,
  'Student of the Year': 3.0,
  'Spiderman : Homecoming': 8.7,
  'Harry Potter and the Chamber of Secrets': 6.0,
  'Kabhi Khushie Kabhi Gham': 7.0,
  'Chak De India': 9.0},
 'naveen balachandran': {'The Dark Knight': 9.0,
  'The Princess Switch': 5.0,
  'The Incredibles': 7.5,
  'The Avengers': 7.5,
  'Kaakha Kaakha': 6.5,
  'Irupathaam Nootandu': 6.5,
  'Devasuram': 8.5,
  'CID Moosa (Seena Thaana)': 7.0,
  'Premam': 7.5,
  'Arjun Reddy': 7.0,
  'Student of the Year': 5.5,
  'Spiderman : Homecoming': 8.0,
  'Jacobinte Swargarajyam': 6.8,
  'Harry Potter and the Chamber of Secrets': 7.5,
  'Kabhi Khushie Kabhi Gham': 6.0,
  'Chak De India': 7.5},
 'anand siva': {'The Dark Knight': 8.5,
  'Thugs of Hindostan': 5.5,
  'Uri : The Surgical Strike': 8.5,
  'The Incredibles': 7.0,
  'The Avengers': 8.5,
  'Devasuram': 9.0,
  'CID Moosa (Seena Thaana)': 9.5,
  'Premam': 9.9,
  'Arjun Reddy': 8.0,
  'Student of the Year': 7.0,
  'Madrasapattinam': 8.2,
  'Spiderman : Homecoming': 6.0,
  'Jacobinte Swargarajyam': 7.5,
  'Harry Potter and the Chamber of Secrets': 8.0,
  'Kabhi Khushie Kabhi Gham': 8.5,
  'Chak De India': 9.4},
 'sourav': {'The Dark Knight': 7.5,
  'Uri : The Surgical Strike': 7.5,
  'The Incredibles': 7.0,
  'The Avengers': 7.0,
  'Irupathaam Nootandu': 6.0,
  'Devasuram': 7.0,
  'CID Moosa (Seena Thaana)': 8.0,
  'The Prestige': 7.0,
  'Premam': 8.0,
  'Arjun Reddy': 6.5,
  'Student of the Year': 6.0,
  'Spiderman : Homecoming': 7.0,
  'Jacobinte Swargarajyam': 5.5,
  'Harry Potter and the Chamber of Secrets': 6.5,
  'Kabhi Khushie Kabhi Gham': 5.0,
  'Chak De India': 6.0},
 'krishna murali': {'The Dark Knight': 9.5,
  'The Princess Switch': 4.0,
  'The Incredibles': 8.8,
  'The Avengers': 8.8,
  'Kaakha Kaakha': 8.0,
  'Fidaa': 4.0,
  'Premam': 6.0,
  'Arjun Reddy': 0.0001,
  'Student of the Year': 1e-07,
  'Madrasapattinam': 7.5,
  'Spiderman : Homecoming': 8.0,
  'Jacobinte Swargarajyam': 6.0,
  'Harry Potter and the Chamber of Secrets': 7.0,
  'Kabhi Khushie Kabhi Gham': 0.0001,
  'Chak De India': 8.0},
 'sai praneeth': {'The Dark Knight': 10.0,
  'Uri : The Surgical Strike': 10.0,
  'The Princess Switch': 9.0,
  'The Incredibles': 10.0,
  'The Avengers': 9.0,
  'Parmaanu : The Story of Pokhran': 8.0,
  'Geetha Govindam': 9.0,
  'The Prestige': 9.0,
  'Fidaa': 9.0,
  'Premam': 9.0,
  'Arjun Reddy': 8.0,
  'Student of the Year': 7.0,
  'Jacobinte Swargarajyam': 9.0,
  'Harry Potter and the Chamber of Secrets': 10.0,
  'Kabhi Khushie Kabhi Gham': 10.0,
  'Chak De India': 9.0},
 'athira': {'Uri : The Surgical Strike': 10.0,
  'The Incredibles': 10.0,
  'The Avengers': 8.0,
  'CID Moosa (Seena Thaana)': 7.0,
  'The Prestige': 8.0,
  'Premam': 7.0,
  'Student of the Year': 5.0,
  'Jacobinte Swargarajyam': 8.0,
  'Harry Potter and the Chamber of Secrets': 7.0,
  'Kabhi Khushie Kabhi Gham': 4.0,
  'Chak De India': 9.0},
 'adarsh': {'The Dark Knight': 9.0,
  'Uri : The Surgical Strike': 10.0,
  'The Princess Switch': 7.0,
  'The Incredibles': 8.5,
  'The Avengers': 8.5,
  'Parmaanu : The Story of Pokhran': 7.5,
  'Devasuram': 7.0,
  'CID Moosa (Seena Thaana)': 8.5,
  'Geetha Govindam': 7.0,
  'The Prestige': 9.0,
  'Premam': 9.0,
  'Arjun Reddy': 8.0,
  'Student of the Year': 5.0,
  'Manikarnika : The Queen of Jhansi': 7.0,
  'Spiderman : Homecoming': 8.0,
  'Jacobinte Swargarajyam': 9.0,
  'Harry Potter and the Chamber of Secrets': 8.0,
  'Kabhi Khushie Kabhi Gham': 8.0,
  'Chak De India': 9.0},
 'aditya viswanath': {'The Dark Knight': 8.7,
  'Thugs of Hindostan': 2.1,
  'Uri : The Surgical Strike': 8.2,
  'The Incredibles': 7.0,
  'The Avengers': 9.0,
  'Kaakha Kaakha': 7.0,
  'Parmaanu : The Story of Pokhran': 7.0,
  'Irupathaam Nootandu': 7.0,
  'Devasuram': 8.7,
  'CID Moosa (Seena Thaana)': 8.3,
  'Geetha Govindam': 6.0,
  'The Prestige': 8.1,
  'Premam': 7.6,
  'Arjun Reddy': 7.8,
  'Student of the Year': 6.8,
  'Madrasapattinam': 8.0,
  'Spiderman : Homecoming': 8.3,
  'Jacobinte Swargarajyam': 8.0,
  'Harry Potter and the Chamber of Secrets': 8.4,
  'Kabhi Khushie Kabhi Gham': 7.6,
  'Chak De India': 7.9},
  'rohan aby':{'The Dark Knight': 9,
  'The Incredibles': 8.0,
  'The Avengers': 7.5,
  'Devasuram': 8.0,
  'CID Moosa (Seena Thaana)': 7,
  'The Prestige': 8.0,
  'Premam': 7.5,
   'Fidaa': 6.5,         
  'Student of the Year': 6,
  'Manikarnika : The Queen of Jhansi': 6.0,
  'Jacobinte Swargarajyam': 7.0,
  'Harry Potter and the Chamber of Secrets': 7.5,
  'Kabhi Khushie Kabhi Gham': 8.5,}}

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


def euclid_sim(p1,p2):
    
    common_data = [item for item in data[p1] if item in data[p2] ]
    common_rating = [(common_data[p1][item],common_data[p2][item]) for item in common_data]
    
    distance = [pow(rating[0]-rating[1],2) for rating in common_rating]
    euc_dist = sqrt(sum(distance))
    
    return (1/1+euc_dist)    #Euclidean Similarity computed.
          
    
def pearson_sim(p1,p2):
    
    common_data = [item for item in data[p1] if item in data[p2]] #Gets the common ratings of both people
    
    num = len(common_data)   #Number of common data points between the two users.
    
    r1 = sum([data[p1][item] for item in common_data])
    r2 = sum([data[p2][item] for item in common_data])  #Ratings Column
    
    sr1 = sum([pow(data[p1][item],2) for item in common_data])
    sr2 = sum([pow(data[p2][item],2) for item in common_data])
    
    rs = sum([data[p1][item]*data[p2][item] for item in common_data])
    
    
    numerator = num*rs - (r1*r2)
    denominator = sqrt(((num*sr1)-(pow(r1,2)))*((num*sr2-(pow(r2,2)))))
    
    
    if denominator != 0:
        pcc = numerator/denominator
        
    else: 
        pcc = 0
    
    return pcc    #Pearson Similarity computed


def rec_engine(person,limit):
    
    ratings = [(pearson_sim(person,other),other) for other in data if other != person]  #ratings list contains the list of similarity coefficients of the person wrt all other persons in the data set.
    
    ratings.sort(reverse=True)            #Sorts the ratings in descending order
    
    
    ratings = ratings[0:limit]
    
    recomms = {}
    
    for similarity, other in ratings:
        rankings = data[other]
        
        for item in rankings:
            if item not in data[person]:
                weight = similarity * rankings[item]
                
                if item in recomms:
                    sim,weights = recomms[item]
                    
                    recomms[item] = (sim+similarity,weights + [weight])    #asding similarity and weight of one item per comparison to one different eprson.
                    
                    
                else:
                    
                    recomms[item] = similarity,[weight]

    
    print("Recommended for you ->\n")
    for item in recomms:
        
        s,weight = recomms[item]
        recomms[item] = sum(weight)/s
        
        print(f"{item} -> {recomms[item]}")
        
    
    return recomms      
            
    

def find_similar_users(person):
    
    l1 = [(pearson_sim(person,other),other) for other in data if other != person]
    
    l1.sort(reverse=True)
    
    print(f"{l1[0][1]} is the most similar user to {person}\n")
    
    
 #End of function find_similar_users


print("Welcome to the Recommendation Engine\n")

print("Do you wan to add data? Y/N\nIf you choose N, sample dataset will be used")
choice = input()


if choice == 'y' or choice == 'Y':
     data = data_entry()
               
if choice == 'n' or choice == 'N':
    name = input('Who do you want to find recommendations for?\n')

    print("\n")

    find_similar_users(name)

    rec_engine(name,10)

            





