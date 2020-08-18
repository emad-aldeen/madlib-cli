def madlib(inp=None,inp2=None):
    """
    madlib():
        the main function to create the madlib story..
        inputs:
            the inputs can bee by user or made before
            inp = it can be only 'path for templte file' OR list contain the inputs..
            inp2 = only in case you insertd 'inp' as path you can insert 'inp2' as 'y', it will consider the inputs are list contain empty strings..
    GL & HF :)
    """
    a = '/home/emad/madlib-cli/madlib_cli/madlib_template.txt'
    b = False

    if inp:
        if inp.count('/') > 1:
            a = inp
        elif type(inp) == list:
            b = True
    
    a = a.split('.')
    
    with open(f'{a[0]}.txt','r') as f:
        lines = f.read()
        places = [[] for k in range(lines.count('{'))]
        j = 0
        for i in range(len(lines)):
            if lines[i] == '{' or lines[i] == '}':
                places[j].append(i)
                if len(places[j]) == 2:
                    j += 1
        if b:
            userInp = inp
        else:
            if inp2 == 'y':
                userInp = ['' for i in range(22)]
            else:
                userInp = [input(f'Please insert {lines[places[i][0]+1:places[i][1]]}: ') for i in range(len(places))]
        result = ''
        for x in range(len(places)):
            if x == 0:
                result += lines[:places[x][0]] + userInp[x] + lines[places[x][1]+1:places[x+1][0]]
            elif x == len(places)-1:
                result += userInp[x] + lines[places[x][1]+1:]
            else:
                result += userInp[x] + lines[places[x][1]+1:places[x+1][0]]  
    with open(a[0]+'_result.text','w+') as res:
        res.write(result)
    return result
    

if __name__ == '__main__':
    print("\n                Welcome to 'Madlib' Game :)\n\n- Rules:\n Simply we will ask you to insert knids of words..\n & finally we will present a cool story about your input..\n\n\n Type 'y' if you Are you Ready?")
    if input('>  ') == "y":
        print(madlib())
    else:
        print('Sory to see you leaveing.. :(')