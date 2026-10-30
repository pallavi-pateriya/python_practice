import copy 

def copy_list(typ, lst):
  if typ == "Shallow" or typ == "shallow":
    new_lst = copy.copy(lst)
    new_lst[0][0] = 12
    print(lst)
    print(new_lst)

  elif typ == "Deep" or typ == "deep":
    new_lst = copy.deepcopy(lst)
    new_lst[0][0] = 12
    print(lst)
    print(new_lst)

copy_list("shallow", [[1,2],3,[4,5]])
copy_list("deep", [[1,2],3,[4,5]])