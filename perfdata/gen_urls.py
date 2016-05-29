deps = ["AE", "AG", "AR", "BT", "CE", "CH", "CS", "CY", "EC", "EE", "EX", "GG", "HS", "ID", "IE", "IM", "IT", "MA", "ME", "MF", "MI", "MM", "MT", "NA", "PH", "QE", "QM", "RE"]
batches = ['11']
courses = ['1', '2', '3']
lowlimits = [[31, 0, 31], [34, 0, 21], [45, 0, 0], [25, 0, 32], [57, 0, 20], [59, 0, 36], [59, 0, 49], [0, 60, 0], [59, 0, 12], [59, 0, 22], [0, 60, 0], [0, 60, 0], [0, 60, 0], [0, 60, 0], [37, 0, 0], [31, 0, 28], [0, 60, 0], [0, 60, 0], [58, 0, 19], [29, 0, 0], [40, 0, 0], [0, 60, 0], [44, 0, 26], [33, 0, 28], [0, 60, 0], [0, 0, 6], [0, 0, 6], [0, 60, 0]]

urls = []
for dep in deps:
  for batch in batches:
    for course in courses:
      for i in range(1, lowlimits[[int(course)-1]):
        urls.append(batch + dep + course + '00' + str(i).zfill(2))

f = open('urls.txt', 'w')
for item in urls:
  f.write("%s\n" % item)