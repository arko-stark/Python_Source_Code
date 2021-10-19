def old_macdonald(name):
    if len(name)== 0 :
        return 'Empty String'
    elif 0 < len(name) < 4 :
        return name[0].upper()+name[1:]
    else :
        return name[0].upper()+name[1:3]+name[3].upper()+name[5:]

print(old_macdonald('nameiskhan'))