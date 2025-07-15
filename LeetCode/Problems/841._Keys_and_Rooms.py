# Problem: 
#   There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. 
#   Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
#   When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, 
#   denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
#   Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, 
#   return true if you can visit all the rooms, or false otherwise.

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        # Holds the keys that have been found
        keys = {0}

        # Holds a queue of new keys to try
        queue = deque([0])

        # Loop until all keys have been tried
        while queue:

            # Get next key
            key = queue.popleft()

            # Loop through the room's keys
            for new_key in rooms[key]:

                # If it's a new key add to collection and queue
                if not new_key in keys:
                    keys.add(new_key)
                    queue.append(new_key)

                # Return if all keys have been found
                if len(keys) == len(rooms):
                    return True

        # At least one key was not found
        return False
