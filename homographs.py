print ("==========================================")
print ("            HOMOGRAPH CHECKER")
print ("==========================================")

# In situations where filename 2 is longer, trim filename2
def getstart(filename1, filename2):
    if (len(filename1) > len(filename2) ):
        return (0) # Start at 0
    return (len(filename2) - len(filename1))

# Turn file paths into hex code
def gethex(filename1, filename2, start):
    # hexed  = []
    # hexed2 = []
    # # Turn strings into hex code for comparison (and later homograph comparisons)
    # for i in range(start, len(filename2)):
    #     hexed.append(filename2[i].encode('utf-8').hex())
    # for i in range(0, len(filename1)):
    #     hexed2.append(filename1[i].encode('utf-8').hex())

    return getsequence(filename1, filename2)
    

def getsequence(fn1, fn2): # ['2e', '2e', '2f']
    # file structure and protected file structure
    filestructure = ['home','user','cse453','week05','test.txt']
    protectedstructure = ['home','user','secret','password.txt']

    # Turn file strings into objects
    path1 = (''.join([str(elem) for elem in fn1])).split('/')
    path2 = (''.join([str(elem) for elem in fn2])).split('/')

    # reverse strings to work backwards across directories
    sq1 = path1[::-1] 
    sq2 = path2[::-1] 

    # reverse comparative file structures for comparisons
    filestructure = filestructure[::-1] 
    protectedstructure = protectedstructure[::-1] 

    # search for folder placeholders and replace with appropriate file structure
    for i in range(0, len(sq1)):
        if(sq1[i] == '..'):
            sq1[i] = filestructure[i]
    
    # search for folder placeholders and replace with appropriate file structure
    for i in range(0, len(sq2)):
        if(sq2[i] == '..'):
            sq2[i] = filestructure[i]

    # make sure file path is not the same as the protected structure
    if(sq1 == protectedstructure or sq2 == protectedstructure):
        return "The paths are not homographs"

    # If sq1 is shorter, trim sq2 for comparison
    if (len(sq1) < len(sq2) ):
        end = len(sq2)
        for i in range(len(sq1), end):
            sq2.pop(len(sq1))

    # compare strings 
    if(sq1 == sq2):
        return "The paths are homographs"
    return "The paths are not homographs"


hg1 = input("Specify the first filename:  ")
hg2 = input("Specify the second filename:  ")

print(gethex(hg1, hg2, getstart(hg1, hg2)))

