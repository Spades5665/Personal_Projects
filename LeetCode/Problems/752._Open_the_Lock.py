# Problem: You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: 
#          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely 
#          and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each 
#          move consists of turning one wheel one slot.
#          The lock initially starts at '0000', a string representing the state of the 4 wheels.
#          You are given a list of deadends dead ends, meaning if the lock displays any of these 
#          codes, the wheels of the lock will stop turning and you will be unable to open it.
#          Given a target representing the value of the wheels that will unlock the lock, return 
#          the minimum total number of turns required to open the lock, or -1 if it is impossible.

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        # Check if the starting position is a deadend
        if "0000" in deadends:
            return -1
        
        # Queue for BFS traversal
        queue = deque()
        queue.append(["0000", 0])

        # A set of all locks that have been visited or are deadends
        visited = set(deadends)
        visited.add("0000")
        
        # Loop while there are still locks to check
        while len(queue):

            # Grab the current lock and how many turns it took to get to it
            lock, turns = queue.popleft()

            # Check if the current lock is the target
            if lock == target:
                return turns
            
            # Loop through each digit in the lock
            for i in range(4):
                
                # Add 1 to each digit 
                newLock = lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i + 1:]

                # Check if the new lock has been visited
                if not newLock in visited:
                    queue.append([newLock, turns + 1])
                    visited.add(newLock)

                # Sub 1 to each digit 
                newLock = lock[:i] + str((int(lock[i]) - 1) % 10) + lock[i + 1:]

                # Check if the new lock has been visited
                if not newLock in visited:
                    queue.append([newLock, turns + 1])
                    visited.add(newLock)
        
        # Target lock was not able to be found
        return -1
