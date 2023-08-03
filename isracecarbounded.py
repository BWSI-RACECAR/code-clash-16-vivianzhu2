class Solution:
    def isracecarbounded(self, instructions):
            #type instructions: string
            #return type: boolean
            initial_pos=[0,0]
            cur_pos=[0,0]
            #direction= ['S':0,'W':1,'N':2,'E':3] Reference for cur_dir (current direction)
            cur_dir=2
            
            #TODO: Write code below to returnn a boolean value with the solution to the prompt.
            for x in range(4):
                 for i in instructions: 
                        if i == "G":
                            if cur_dir == 2:
                                cur_pos[1] = cur_pos[1] + 1
                            if cur_dir == 0: 
                                cur_pos[1] = cur_pos[1]-1
                            if cur_dir == 3:
                                 cur_pos[0] = cur_pos[0]+1
                            if cur_dir ==1:
                                 cur_pos[0] = cur_pos[0]-1
                        if i == "L":
                             if cur_dir == 0: 
                                  cur_dir =3
                             else: 
                                  cur_dir = cur_dir -1
                        if i == "R":
                             if cur_dir ==3: 
                                  cur_dir = 0
                             else: 
                                  cur_dir = cur_dir + 1
            if cur_pos == initial_pos:
                 return True 
            else: 
                 return False 
            # previousChar = previousChar = instructions[0]
            # answer = False
            # print("instructions: " + instructions)
            # for i in range(len(instructions)):
            #      if i == 0: 
            #           continue
                      
            #      else:
                      
            #           if ((previousChar == instructions[i] and instructions[i] == "L") or (previousChar == instructions[i] and instructions[i] == "R")):
                           
            #                answer = True
            #                previousChar = instructions[i]
            #                print("prev char: " + previousChar)
            #                break 
            
            # return answer
                      
            pass
        
def main():
    input1=input()
    tc1 = Solution()
    ans = tc1.isracecarbounded(input1)
    print(ans)

if __name__ == "__main__":
    main()