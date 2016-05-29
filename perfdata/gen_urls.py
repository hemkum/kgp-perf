deps = ["AE", "AG", "AR", "BT", "CE", "CH", "CS", "CY", "EC", "EE", "EX", "GG", "HS", "ID", "IE", "IM", "IT", "MA", "ME", "MF", "MI", "MM", "MT", "NA", "PH", "QE", "QM", "RE"]
batches = ['10', '12', '13', '14', '15']
courses = ['1', '2', '3']
limits = [[51, 0, 51], [54, 0, 41], [65, 0, 0], [45, 0, 52], [77, 0, 40], [79, 0, 56], [79, 0, 69], [0, 70, 0], [79, 0, 32], [79, 0, 42], [0, 70, 0], [0, 70, 0], [0, 70, 0], [0, 70, 0], [57, 0, 0], [51, 0, 48], [0, 70, 0], [0, 70, 0], [78, 0, 39], [49, 0, 0], [60, 0, 0], [0, 70, 0], [64, 0, 46], [53, 0, 48], [0, 70, 0], [0, 0, 26], [0, 0, 26], [0, 70, 0]]

urls = []
for x, dep in enumerate(deps):
  for batch in batches:
    for y, course in enumerate(courses):
      for i in range(1, limits[x][y]):
        urls.append(batch + dep + course + '00' + str(i).zfill(2))

f = open('urls.txt', 'w')
for item in urls:
  f.write("%s\n" % item)