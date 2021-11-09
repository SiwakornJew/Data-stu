def get_max_index(lst):
    max_index = len(lst)-1

    if lst[max_index] != max(lst) and max_index-1 >= 0: 
        return get_max_index(lst[:max_index])
    else:
        return max_index
def selection_sort(lst,right=None):
    if right is None:
        right = len(lst)-1
    if right < 0:
        return lst
    
    max_index = get_max_index(lst[:right+1])
    if max_index != right:
        lst[right], lst[max_index] = lst[max_index], lst[right]
        print(f'swap {lst[max_index]} <-> {lst[right]} : {lst}')
    return selection_sort(lst, right-1)

in_lst = list(map(int, input("Enter Input : ").split()))
ans = selection_sort(in_lst)
print(in_lst)