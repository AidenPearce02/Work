def namelist(args):
    result = ""
    if len(args) == 0:
        result = ""
    elif len(args) == 1:
        result = args[0].get('name')
    else:
        for i in args:
            if args.index(i) == len(args) - 1:
                result = result + " & " + i['name']
            elif args.index(i) == 0:
                result = i['name']
            else:
                result = result + " , " + i['name']

    return result

test = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
print(namelist(test))
