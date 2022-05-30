userInventory = ('Bag of Gold', 'Suitcase')

def inventoryValidator(x, y):
        x = userInventory
        while userInventory not in ('Business Card',):
            inventoryCheck = 'yes'
            return inventoryCheck
        else:
            inventoryCheck = 'no'
            return inventoryCheck
        
def inventoryDecider(inventoryCheck):
    if inventoryCheck == 'yes':
        return inventoryCheck
    elif inventoryCheck == 'no':
        return inventoryCheck

inventoryStatus = inventoryDecider(userInventory, inventoryValidator())

print("Checking inventory")
print(inventoryStatus)
blank = input("")

if inventoryStatus == 'yes':
    print("You have a business card!")

elif inventoryStatus == 'no':
    print ("You dont have a business card")

##
##
##userYesNo = yesNoDecider(yesNoValidator())
##
##if userYesNo == "yes":
##    print("YES!!")
##elif userYesNo == "no":
##    print("NO!!!")
##

#--------------------------------------

##
##def numberChoiceValidator():
##        userNumberChoice = input(':')
##        while userNumberChoice not in ['1', '2', '3']:
##            userNumberChoice = input("Please enter choices [1], [2], or [3]: ")
##        else:
##            return userNumberChoice
##        
##def numberChoiceDecider(userNumberChoice):
##    if userNumberChoice == '1':
##        return userNumberChoice
##    elif userNumberChoice == '2':
##        return userNumberChoice
##    elif userNumberChoice == '3':
##        return userNumberChoice
##
##
##userNumberChoice = numberChoiceDecider(numberChoiceValidator())
##
##if userYesNo == "1":
##    print("one!!")
##elif userYesNo == "2":
##    print("two!!!")
##elif userYesNo == "3":
##    print("three!!!")

#--------------------------------------
##
##class collections.ChainMap(*maps):
##
##import builtins
##import os, argparse
##
##c = ChainMap()        # Create root context
##d = c.new_child()     # Create nested child context
##e = c.new_child()     # Child of c, independent from d
##e.maps[0]             # Current context dictionary -- like Python's locals()
##e.maps[-1]            # Root context -- like Python's globals()
##e.parents             # Enclosing context chain -- like Python's nonlocals
##
##d['x'] = 1            # Set value in current context
##d['x']                # Get first key in the chain of contexts
##del d['x']            # Delete from current context
##list(d)               # All nested values
##k in d                # Check all nested values
##len(d)                # Number of nested values
##d.items()             # All nested items
##dict(d)               # Flatten into a regular dictionary
##
##pylookup = ChainMap(locals(), globals(), vars(builtins))
##
##class DeepChainMap(ChainMap):
##    'Variant of ChainMap that allows direct updates to inner scopes'
##
##    def __setitem__(self, key, value):
##        for mapping in self.maps:
##            if key in mapping:
##                mapping[key] = value
##                return
##        self.maps[0][key] = value
##
##    def __delitem__(self, key):
##        for mapping in self.maps:
##            if key in mapping:
##                del mapping[key]
##                return
##        raise KeyError(key)
##

#userGold = 500
##
##
##def add(a,b):
##    result = a + b
##    return result
##
##userInventory = ('Bag of Gold', 'Suitcase',)
##print(type(userInventory))
##print("--------------------------------------\n")
##userInventory = 'Wallet', 'Suitcase', 'Reference Letter'
##print(type(userInventory))
##
##updateInventory = ('Cardboard Box',)
##userInventory = add(userInventory, updateInventory)
##
##print("\n\n------------ List concatinated ----------\n")
##print(userInventory)
##print(type(userInventory))
##
