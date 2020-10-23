#!/usr/bin/env python


# This is a Shopping Cart that lets the user create a cart and perform different actions to it.
# Action included are:
#   1. Create Cart for the Shopping Site
#   2. Add Items to Cart
#   3. Remove Items from the Cart
#   4. Get Items from the Cart
#   5. Update any values of the items in the Cart


from pymongo import MongoClient

# Create a MongoDB Client to connect to
client = MongoClient('localhost', 27017)

# Create a DB instance
db = client['mongo_db']

def create_cart():
    # Create a Collection with specified name 
    collection = db['cart']
    
    print('\nCart created Successfully!!\n')
    return True

def add_items(name, qty, price):
    
    '''
    Function to Add items to the shopping cart
    Params: 
        Product Name
        Product Qty
        Product Unit Price
    Returns: None
    '''

    coll = db.cart
    qry = {
        "prodName": name,
        "prodQty": qty,
        "prodUnitPrice": price
    }

    coll.insert_one(qry)
    print('\nItem Inserted successfully!!\n')

def get__specific_item(name):

    '''
    Function to Get Specified items from the shopping cart
    Params: 
        Product Name
    Return:
        Product Details from the Cart
    '''

    coll = db.cart
    
    print('\n')
    if coll.find({"prodName": name}):
        for rec in coll.find({"prodName": name}):
            for key, val in rec.items():
                if key != '_id':
                    print("{}: {}".format(key, val))
    else:
        print('\nNo such record present\n')

def show_items():

    '''
    Function to Get All the  items from the shopping cart
    Params: None
    Return:
        Product Details
    '''

    coll = db.cart
    print('\n')
    
    if coll.find():
        for rec in coll.find():
            print(list(rec.items())[1:])
    
    else:
        print('\nCart is Empty\n')


def remove_items(name):

    '''
    Function to Remove Specific items from the shopping cart
    Params: 
        Product Name
    Returns: None
    '''

    coll = db.cart
    rec = coll.find({"prodName": name})
    
    if rec:
        coll.delete_one({"prodName": name})
        print('\nItem deleted successfully!!\n')
    
    else:
        print('\nDeletion Failed, Not such Item present\n')

def update_items():

    '''
    Function to Update Specific items in the shopping cart
    Params: 
        Product Name
        Product Qty
        Product Unit Price
    Returns: None
    '''

    print('\n')
    prodName = input('Name of item: ')
    
    coll = db.cart
    rec = coll.find({"prodName": prodName})

    if rec:
        print('\nNew Values\n')
        new_prodName = input('Name of the item: ')
        new_prodQty = input('Number of items: ')
        new_unitPrice = input('Price per Unit: ')
    
        new_data = {}
        if len(new_prodName) != 0:
            new_data['prodName'] = new_prodName
        if len(new_prodQty) != 0 :
            new_data['prodQty'] = new_prodQty
        if len(new_unitPrice) != 0:
            new_data['prodUnitPrice'] = new_unitPrice

        qry = {"prodName": prodName}

        coll.update_one(qry, {'$set': new_data})

        print('\nItem Updated Succesfully\n')
    
    else:
        print('\nUpdation Failed, No such record present\n')


# Driver Code to setup

if __name__ == '__main__':
    print('\nWelcome to Shopping Center!!\nEnjoy Shopping!!\n')
    
    print('\nFirst Select the following before proceding\n')
    
    running = True

    while running:
        print('\n1. Create Cart\n2. Close Application\n')
        choice = int(input())
        
        if choice == 1:
            cart = create_cart()
            
            while cart:
                print('\n1. Add Items\n2. Remove Items\n3. Get Specific Item\n4. Show Items\n5. Update Items\n6. Log Out\n')
                action = int(input("\nEnter your choice: "))

                if action == 1:
                    print('\n')
                    prodName = input('Name of the item: ')
                    prodQty = input('Number of items: ')
                    unitPrice = input('Price per Unit: ')

                    add_items(prodName, prodQty, unitPrice)

                elif action == 2:
                    print('\n')
                    prodName = input('Name of the item: ')
                    remove_items(prodName)
                
                elif action == 3:
                    print('\n')
                    prodName = input('Enter the name of Item: ')
                    get__specific_item(prodName)

                elif action == 4:
                    show_items()
                
                elif action == 5:
                    update_items()
                
                elif action == 6:
                    cart = False

                else:
                    print('\nPlease choose appropriate action\n')
        
        if choice == 2:
            running = False

        else:
            print('\nCreate Cart before proceding\n')    