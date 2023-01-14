import re
import ast
def lexical_analysis(input):
    operator = ['+', '-', '|', '^', '=', '*']
    special = ['!', '@', '_', '?', '<', '>', '#', '$', '%', '&']
    letters = []
    numbers = []
    operators = []
    specialCharacters = []
    datatype = []
    tokens = re.findall(r"\d|\D", input)
    print('\n',tokens,'\n')
    for i in range(len(tokens)):
        if tokens[i].isalpha() == True:
           letters.append(tokens[i])
        elif tokens[i].isnumeric() == True:
           numbers.append(tokens[i])
        elif tokens[i] in operator:
            operators.append(tokens[i])
        elif tokens[i] in special:
            specialCharacters.append(tokens[i])
            
    for i in range(len(tokens)):
        if tokens[i] in letters:
            datatype.append('Alphaphet')
        elif tokens[i] in numbers:
            datatype.append('Number')
        elif tokens[i] in operators:
            datatype.append('Operator')
        elif tokens[i] in specialCharacters:
            datatype.append('Special Character')

    for i in range(len(tokens)):
        print(" "+tokens[i]+" "+datatype[i]+" ")

def syntax_analysis(input):
    parsed_output = ast.parse(input)
    syntaxTree = ast.dump(parsed_output)
    print(syntaxTree)

if __name__ == "__main__":
 expression = str(input("Enter an expression: "))
 print("   _________________\n")
 print("   Lexical Analysis")
 print("   _________________\n")
 lexical_analysis(expression)
 print("   _________________\n")
 print("    Syntax Analysis")
 print("   _________________\n")
 syntax_analysis(expression)
