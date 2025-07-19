# Problem: 
#   Given a list of folders folder, return the folders after removing all sub-folders
#   in those folders. You may return the answer in any order.
#   If a folder[i] is located within another folder[j], it is called a sub-folder of it. 
#   A sub-folder of folder[j] must start with folder[j], followed by a "/". For example, 
#   "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".
#   The format of a path is one or more concatenated strings of the form: '/' followed 
#   by one or more lowercase English letters.
#   For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        # Sort the folders so the main folders are in front
        folder = sorted(folder)

        # Hold only the main folders
        main_folders = []
        
        # Next index to check
        index = 0

        # Loop through each index in folder
        while index < len(folder):

            # Get the next main folder and add it to main_folders
            new_folder = folder[index]
            main_folders.append(new_folder)

            # Loop through each folder that has the new main folder
            while index < len(folder) - 1 and folder[index + 1][0:len(new_folder) + 1] == new_folder + "/":
                index += 1 

            # Go to next main_folder
            index += 1
        
        # Return main_folders
        return main_folders
