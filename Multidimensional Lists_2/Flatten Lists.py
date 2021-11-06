#values = input().split('|')

#output_with_space = []
#output_without_space = []
#for i in values:
   # output_with_space.append(i)


#for v in output_with_space:
 #   new_list = v.split()
  #  output_without_space.append(new_list)

#for value in reversed(output_without_space):
 #   print(' '.join(x)[for x in value], end=' ')

numbers = input().split('|')

for el in reversed(numbers):
    tmp_list = el.split()
    tmp_string = " ".join(tmp_list)
    if tmp_string:
        print(tmp_string, end=' ')