text = """Romeo.  Why,  such  is  love's  transgression. 
Griefs  of  mine  own  lie  heavy  in  my  breast, 
Which  thou  wilt  propagate,  to  have  it  prest 
With  more  of  thine ;  this  love  that  thou  hast  shown 
Doth  add  more  grief  to  too  much  of  mine  own. 
Love  is  a  smoke  rais'd  with  the  fume  of  sighs : 
Being  purg'd,  a  fire  sparkling  in  lovers'  eyes ; 
Being  vex'd,  a  sea  nourish'd  with  lovers'  tears ; 
What  is  it  else  ?  a  madness  most  discreet, 
A  choking  gall,  and  a  preserving  sweet. 
Farewell,  my  coz."""



spl_chrs=[]
spl_words=[]


for everyword in text.split():
    if everyword == ';':
        spl_chrs.append(everyword)
    elif everyword == ':':
        spl_chrs.append(everyword)
    elif everyword == '?':
        spl_chrs.append(everyword)
    elif everyword == '.':
        spl_chrs.append(everyword)
    elif "'" in everyword:
        spl_words.append(everyword)

# alternate approach

for everyword in text.split():
    if everyword in [';',':','?','.']:
        spl_chrs.append(everyword)
    elif "'" in everyword:
        spl_words.append(everyword) 