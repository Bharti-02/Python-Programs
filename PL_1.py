# search name in list print found if name in list 
def name_search(name,target):
    for i in range(len(name)):
        if name[i]==target:
            return "Found"
    return "Not Found"


name=input("Enter names:").split()
target=input("Enter name :")
print(name_search(name,target))
                
