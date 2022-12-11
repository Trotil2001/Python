
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
f_in_path = 'Task4_in.txt'
f_encod_path = 'Task4_encod_out.txt'
f_decod_path = 'Task4_decod_out.txt'

# str1='aaaabbbbbccccccccdeeeffff'




def read_f(path_f):
  with open(path_f, 'r',encoding='utf-8') as data_in:
    return data_in.read()

def write_f(path_f,str_f):
  with open(path_f, 'w',encoding='utf-8') as data_out:
    data_out.writelines(str_f)


str_in=read_f(f_in_path)
print(f'Исходная строка: {str_in}')

def encod(str_in):
  count=0
  str_enc=[]
  for i in range(0,len(str_in)):
    if str_in[i]==str_in[i-count]:
      count+=1
      item=str_in[i]
      if i == len(str_in)-1:
        str_enc.append(str(count)+str_in[i])    
    else:
      str_enc.append(str(count)+str_in[i-count])
      count=1
   
  str_enc="".join(str_enc)
  print(f'Сжатая строка: {str_enc}')
  return str_enc

write_f(f_encod_path,encod(str_in))

def dec(f_encod_path):
  str_dec=''
  count_d=''
  str_in_enc=read_f(f_encod_path)
  for item in str_in_enc:
    if item.isdigit():
      count_d+=item
    else:
      str_dec +=item * int(count_d)
      count_d=''
  print(f'Декодированная строка: {str_dec}')
  return str_dec

write_f(f_decod_path,dec(f_encod_path))