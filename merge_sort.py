
def merge(left_arr, right_arr):
    merged = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] <= right_arr[right_idx]:
            merged.append(left_arr[left_idx])
            left_idx += 1
        else:
            merged.append(right_arr[right_idx])
            right_idx += 1

    while left_idx < len(left_arr):
        merged.append(left_arr[left_idx])
        left_idx += 1

    while right_idx < len(right_arr):
        merged.append(right_arr[right_idx])
        right_idx += 1

    return merged

def merge_sort(arr):
	if len(arr) <= 1:
		return arr
		
	mid = len(arr) // 2
	left_half = arr[:mid]
	right_half = arr[mid:]
	
	left_merged = merge_sort(left_half)
	right_merged = merge_sort(right_half)
	
	return merge(left_merged, right_merged)
