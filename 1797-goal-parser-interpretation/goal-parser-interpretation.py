class Solution:
    def interpret(self, command: str) -> str:
        goal = ''
        for i in range(len(command)):
            if i < len(command)-1:
                if command[i]+command[i+1]=="()":
                    goal += 'o'
                elif command[i]+command[i+1]=="(a":
                    goal += 'al'
                elif command[i]=='G':
                    goal += 'G'
            elif command[i]=='G':
                goal+='G'
        return goal
        