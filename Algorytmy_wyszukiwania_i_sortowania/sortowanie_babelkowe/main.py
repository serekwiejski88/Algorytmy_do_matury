def sortowanie():
   table = [123,22,33,44,543,1321,83,43,999,10232,9,123321123231,1,3223,4,4,21,4,312312123,333,222,444444,5555]
   for j in range(len(table)):
         for i in range(len(table)):
            if i < len(table)-1:
               x = table[i]
               y = table[i + 1]
               if x>y:
                  table[i+1] = x
                  table[i] = y
               else:
                  continue
            else:
               continue
   print(table)


sortowanie()