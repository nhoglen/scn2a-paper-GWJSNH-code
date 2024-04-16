import os
from boxsdk import OAuth2, Client
import re

def visit_all_dirs_files(usedir,full_list,curr_path,client):

    # get all the items in the current folder
    theseitems = client.folder(folder_id=usedir).get_items()

    for item in theseitems:     # loop over items
        tp = item.type # get key fields from directory items
        nm = item.name
        iid = item.id

        if tp == 'folder': # recursion if a folder is found
            curr_path.append(nm) # add directory to path
            full_list = visit_all_dirs_files(iid,full_list,curr_path,client) # look for more folders/files
            curr_path.pop() # clean the folder back off the path when going up a level
        else: # keep track of all the paths when there are files
            tpath = os.path.join(*curr_path)
            full_list.append(os.path.join(tpath,nm))

    return full_list

def find_in_list(lst, item, assaystr):
    result = []
    for i, x in enumerate(lst):
        if re.search(f'{item}[_|-|{assaystr}]',x,re.IGNORECASE):
            result.append(i)
    return result
