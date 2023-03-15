import os

fnames = os.listdir('data')
del_ls = ['Applejack-12A-2-4-2023_Applejack-12A-2-4-2023.csv']

aug_fnames = [i for i in fnames if i not in del_ls]

print('TESTING FNAMES, length: ' + str(len(fnames)))
print(fnames)
print('\n \n')
print('TESTING APPLICATION OF DEL_LS, length: ' + str(len(aug_fnames)))
print(aug_fnames)