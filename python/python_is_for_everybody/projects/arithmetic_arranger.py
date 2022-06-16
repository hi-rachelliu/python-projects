def arithmetic_arranger(problems, choice = None):
  # Imports libraries and defines global variables 
  
  import operator
  
  dividends = []
  first_val = []
  operators = []
  second_val = []
  first_leng = []
  results = []  
  lst = []
  full_leng = []
  s = ' '
  d = '-'
  length = ''

  # Determines the longer dividend
  for problem in problems:
    dividends.append(problem.split())
  length = (len(dividends))

  for problem in problems:
    things = problem.split()
    for thing in things:
      lst.append(len(thing))
      if len(thing) > 5:
        return ("Error: Numbers cannot be more than four digits.")
        quit()
    full_leng.append(max(lst) + 2)
    lst.clear()
    
  # Gets values into separate lists 
  for i in range(length):
    first_val.append(dividends[i][0]) 
    operators.append(dividends[i][1]) 
    second_val.append(dividends[i][2]) 
    first_leng.append(full_leng[i] - len(first_val[i]))
    if not first_val[i].isdigit() or not second_val[i].isdigit():
      return ("Error: Numbers must only contain digits.")
      quit()
    
  # Error situations! 
  if length > 5: 
    return ("Error: Too many problems.")
    quit()
  if ('*' in operators) or ('/' in operators):
    return ("Error: Operator must be '+' or '-'.")
    quit()

  # Prints output
  for i in range(length):
    print(s*(int(first_leng[i])) + first_val[i], end = ('    '))
  print('')
  for i in range(length):
    print(operators[i]+ s*(full_leng[i] - len(second_val[i]) -1), end = ('')) 
    print(second_val[i], end = ('    ')) 
  print('')
  for i in range(length):
    print(f"{d * (full_leng[i])}", end= ('    '))
  print('')

  # If choice == True, calculates and prints results
  ops = { "+": operator.add, "-": operator.sub }
  if choice == True:
    for i in range(length):
      results.append(str(ops[operators[i]](int(first_val[i]),int(second_val[i]))))
      print(s*(full_leng[i] - len(results[i])) + results[i], end = '    ')