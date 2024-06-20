import dataLayer as dl
import os
def menu():
     print("1.Add Products")
     print("2.Update Product")
     print("3.Delete Product")
     print("4.Get All Product")
     print("5.Exit")
     choice=int(input("Enter your Choice:"))
     return choice
def show_products():
     df=dl.getProducts()
     for i in df.index:
          product=df.loc[i]
          print("{0:<5} {1:<20} {2:<10} {3:<40} {4:<10}".format(product['PID'],product['Product Name'],product['Price'],product['Description'],product['Rating']))

def add_product():
     show_products()
     pid=int(input("Enter the product id:"))
     Product_Name=input("Enter the product Name:")
     price=float(input("Enter the price of product:"))
     Description=input("Enter the product description:")
     Rating=float(input("Enter the Rating:"))
     dl.add_Products(pid,Product_Name,price,Description,Rating)
     print("Product added Successfully!! ")
def press_any_key():
    input("Press any key to continue:")
def delete_Product():
    show_products()
    file = "project.csv"  # Replace with your actual file name
    key = int(input("Enter the product id to delete product: "))
    dl.delete(key, file)
    print("{0} deleted successfully!".format(key))

def update_products():
    show_products()
    file = "project.csv"  # Replace with your actual file name
    key = int(input("Enter the product id to update product: "))
    new_rating=float(input("Enter new Rating:"))
    dl.update(key,new_rating,file)
    print("{0} updated successfully!!".format(key))


Option=10
while(Option!=5):
  os.system("cls")
  Option=menu()
  if Option==1:

     add_product()
     press_any_key()
  if Option==2:
      update_products()
      press_any_key()
     
  if Option==3:
     delete_Product()
     press_any_key() 
     
  if Option==4:
     show_products()
     press_any_key()
     
     
     

