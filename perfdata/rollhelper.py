import os
deps = ["AE", "AG", "AR", "BT", "CE", "CH", "CS", "CY", "EC", "EE", "EX", "GG", "HS", "ID", "IE", "IM", "IT", "MA", "ME", "MF", "MI", "MM", "MT", "NA", "PH", "QE", "QM", "RE"]
Ms = []
for dep in deps:
  files = [dep + '/' + file for file in os.listdir(dep)]
  types = ['1', '2', '3']
  M = [0, 0, 0]
  m = [100, 100, 100]
  for file in files:
    tp = int(file[-10])-1
    num = int(file[-7:-5])
    M[tp] = max(M[tp], num)
    m[tp] = min(m[tp], num)
  if M[0] == 0 and M[2] == 0:
    M[1] = 60
  Ms.append(M)
  # print (dep, M)
print Ms