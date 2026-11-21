def common_club_members(club1, club2):
    set1 = set(club1)
    set2 = set(club2)   
    for member in set1:
        if member in set2:
            print(member)
arr1 = [9, 4, 9, 5, 12, 4]
arr2=[12, 9, 9, 8, 4, 12]
common_club_members(arr1, arr2)