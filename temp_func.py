def string_contain_all(texts, strings):
  
  return all(string in texts for string in strings)


def string_contain_any(texts, strings):
  
  return any(string in texts for string in strings)

def find_text_contain_all(texts, strings):
  
  return [text for text in texts if string_contain_all(text, strings)]
  
def save_to_text(file, *args):
  
  with open(file, "w", encoding = "utf-8") as handle:
    for string in args:
      print(string)
      handle.write(string + "\n")

  
