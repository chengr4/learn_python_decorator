# 為想共通做的事再寫一個 function -> 例如加工修飾
def print_func_name(func):
  def wrap():
      print("Now use function '{}'".format(func.__name__))
      func()
  return wrap

@print_func_name
def dog_bark():
  print("Bark !!!")

@print_func_name
def cat_miaow():
  print("Miaow ~~~")

if __name__ == "__main__":
  ''' 未用 @ 語法糖
  # 後面記得多放()來 call wrap()
  print_func_name(dog_bark)()
  # > Now use function 'dog_bark'
  # > Bark !!!

  print_func_name(cat_miaow)()
  # > Now use function 'cat_miaow'
  # > Miaow ~~~
  '''
  # 用了語法糖
  dog_bark()
  # > Now use function 'dog_bark'
  # > Bark !!!

  cat_miaow()
  # > Now use function 'cat_miaow'
  # > Bark !!!