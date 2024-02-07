import queue 

class Anagram:
    def heuristic(self, state, goal):
        cnt = 0
        for letter in state:
            if letter not in goal:
                cnt +=1
        return cnt

    num_iterations = 0
    def anagram_expand(self, state, goal):
        node_list = []

        for pos in range(1, len(state)):  # Create each possible state that can be created from the current one in a single step
            new_state = state[1:pos + 1] + state[0] + state[pos + 1:]

            # TO DO: c. Very simple h' function - please improve!
            if new_state == goal:
                score = 0
            else:
                score = self.heuristic(new_state, goal)

            node_list.append((new_state, score))

        return node_list


    # TO DO: b. Return either the solution as a list of states from start to goal or [] if there is no solution. 
     #The a_star function needs to know the problem’s  start state, the  desired goal state, and  an expand function that expands a given node
    def a_star(self, start, goal, expand):
        list = []
        q = queue.PriorityQueue()
        q.put((self.heuristic(start, goal), start, []))

        while not q.empty():
            score, state, plc = q.get()
            
            if state in list:
                continue
            list.append(state)
            
            if state == goal:
                return plc + [state]
        
            #new_state, h_score = v
            for (new_state, h_score) in expand(state, goal):
                if new_state in list:   
                    continue
                f_score = (len(plc) + 1) + h_score
                q.put((f_score, new_state, plc + [state]))
                
        return []


    # Finds a solution, i.e., the set of steps from one word to its anagram.
    def solve(self,start, goal):

        self.num_iterations = 0

        # TO DO: a. Add code below to check in advance whether the problem is solvable
        #start_check = []
        start_check = {}
        goal_check = {}

        for letter in start:
          start_check[letter] = start_check.get(letter, 0) 
        for letter in goal:
         goal_check[letter] = goal_check.get(letter, 0) 

    # comparing each letter in start and goal
        for letter in goal_check:
            if letter not in start_check or goal_check[letter] > start_check[letter]:
               print('This is clearly impossible. I am not even trying to solve this.')
            return "IMPOSSIBLE"
        # if ...
        #    print('This is clearly impossible. I am not even trying to solve this.')
        #    return "IMPOSSIBLE"

        self.solution = self.a_star(start, goal, self.anagram_expand)

        if not self.solution:
            print('No solution found. This is weird, I should have caught this before even trying A*.')
            return "NONE"

        print(str(len(self.solution) - 1) + ' steps from start to goal:')

        for step in self.solution:
            print(step)

        print(str(self.num_iterations) + ' A* iterations were performed to find this solution.')

        return str(self.num_iterations)



if __name__ == '__main__':
    anagram = Anagram()
    anagram.solve('TRACE', 'CRATE')
    anagram.solve('TEARDROP', 'PREDATOR')