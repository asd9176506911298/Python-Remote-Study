def s(name, *score, number = 2,**p):
    print('%-8s %s' % ('Name', name))
    print('%-8s %s' % ('Quantity', number))
    for key in sorted(p):
        print('%-8s %s' % (key, p[key]))
    
    print('%-8s %s' % ('Score', list(sorted(score))))
    print('- ' * 15)


s('Grace',59,98,72,number=3,Class='1A',Type='必修',
  Elective='Mandarin,English,Mathematics')

s("Edward",88,77,Class="1B",Type="選修",
  Elective="Computer,Python")