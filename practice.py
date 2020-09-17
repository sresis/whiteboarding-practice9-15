def pig_latin(phrase_1):
  # split into list of words
  word_list = phrase_1.split(' ')



  vowels = 'aeiou'
  updated_words = []

  if phrase_1 == '':
    return ''

  if phrase_1 == '    '




  # iterate through each word in the string & determine if starts with vowel
  for word in word_list:
    if word[0] not in vowels:
      adj_word = word[1:len(word)] + word[0] + 'ay'
      updated_words.append(adj_word)
    elif word == '':
      skip
    else:
      adj_word = word + 'yay'
      word_list[index] = adj_word

  # add updated word to list of adjusted words      
  
    
  final_string = (' ').join(words_list)
    
  return final_string

print(pig_latin('porcupines are cute') == 'orcupinespay areyay utecay')

print(pig_latin('give me an apple') =='ivegay emay anyay appleyay')