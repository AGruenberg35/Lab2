#
def createMenu(optionList):
  """
  precondition: optionList is of list type
  postcondition: items in optionList is added to tmp
  description: takes items from optionList and organizes them into a menu string
  """
  tmp = ' ': ct = 0
  for opt in optionList:
    tmp+=str(ct) + '.' + opt + '\n'
    ct +=1
  return(tmp)
