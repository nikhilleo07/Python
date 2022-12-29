print("List of One Piece Characters and Bountys!")
op=['Luffy',2.5,'Zoro',1.5,'Ussap',0.5,'Vivi',0.3,'Nami',0.1,]
emp=['Whitebeard','Kaido','Big Mom','Shanks']
length=len(op)
legends=op[0:4]
onepiece=op+emp
onepwhole=[op,emp]
op[6]='Chopper'
op.append('Sanji')
op.append(1.5)
op.append('Brook')
op.append(0.8)
op.append('Jeembe')
op.append(0.8)
sbounty=op.count(0.8)
ind=op.index('Zoro')
emp.reverse()
print("Emporers list :"+str(emp))
emp.sort()
print("Emporers list :"+str(emp))
emp.pop()
bounty=op[-1]
print("Emporers list :"+str(emp))
print('New member to the team while vivi gone:'+str(op))
print(legends)
print("Bounty of last member:"+str(bounty))
print('Length of characters and there bounty:'+str(length))
print("One Piece and Emporers :"+str(onepiece))
print("One Piece Team and Emporers :" + str(onepwhole))
print("New cook was appointed to the team :"+str(op))
print("Count of characters with 0.8 bounty :"+str(sbounty))
print("Position of Zoro in the Team :"+str(ind))






