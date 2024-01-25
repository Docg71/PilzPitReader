import os,re

import libbed_temperature as bed
                                    


if __name__ == '__main__' :
    print("File main is run directly")
else:
    print("File can only be run directly")
    os.exit()




''' Main  '''

def main():

    beds = bed.get_all_beds()
    bed.list_beds(beds)
    
    
    
    
    
main()    
print("done")
