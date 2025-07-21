# Problem: 
#   Given two arrays of strings list1 and list2, find the common strings with the least index sum.
#   A common string is a string that appeared in both list1 and list2.
#   A common string with the least index sum is a common string such that if it appeared at 
#   list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
#   Return all the common strings with the least index sum. Return the answer in any order.

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        # Create a hash table to keep track of lowest sum index values
        hash_table = dict()

        # Loop through each word in list1
        for i in range(len(list1)):

            # Check if current word is in list2
            if list1[i] in list2:

                # Find the sum of the indices
                index_sum = i + list2.index(list1[i])

                # Check if this sum has been found before and initialize if not
                if index_sum not in hash_table:
                    hash_table[index_sum] = [list1[i]]
                
                # Append the new word to the current list
                else:
                    new_list = hash_table[index_sum]
                    new_list.append(list1[i])
                    hash_table[index_sum] = new_list
                
        # Return the list at the minimum sum index found
        return hash_table[min(hash_table)]
