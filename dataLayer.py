import pandas as pd 
file="project.csv"

def add_Products(PID,productName,Price,description,rating):
    data=pd.read_csv(file)
    products=[PID,productName,Price,description,rating]
    data.loc[len(data.index)]=products ##last say jgah denay k liye
    data.to_csv(file,index=False)
    

def update(PID,new_rating,file):
     data=pd.read_csv(file)
     idx=data[data['PID']==PID].index
     data.loc[idx,'Rating']=new_rating
     data.to_csv(file,index=False)

def delete(PID,file):
     data=pd.read_csv(file)
     idx=data[data['PID']==PID].index
     data = data.drop(idx, axis=0)  # Drop rows with the specified index
     data.to_csv(file,index=False)

def getProducts():
     data=pd.read_csv(file)
     return data

def get_single_product(PID):
     data=pd.read_csv(file)
     ans=data[data['PID']==PID]
     return data[ans]

