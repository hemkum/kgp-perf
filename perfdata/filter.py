import os
deps = ["AE", "AG", "AR", "BT", "CE", "CH", "CS", "CY", "EC", "EE", "EX", "GG", "HS", "ID", "IE", "IM", "IT", "MA", "ME", "MF", "MI", "MM", "MT", "NA", "PH", "QE", "QM", "RE"]
for dep in deps:
  files = [dep + '/' + file for file in os.listdir(dep)]
  for file in files:
    if 'Semester' not in open(file, 'r').read():
      os.remove(file)