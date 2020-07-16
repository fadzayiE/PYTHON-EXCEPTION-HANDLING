Subject = ['Americans', 'Indians']
verb =['play', 'watch']
Object=['Baseball', 'Cricket']
All_sentences = [(sub +" "+ ver +" " + obj)
               for sub in Subject for ver in verb for obj in Object]
for sentence in All_sentences:
    print(sentence)
    