# The filename "QA_Pairs9.txt" contains questions and answers generated from the Game of Thrones TV series across eight seasons created by a research team. 
# The first task counted the questions and answer pairs in the "QA_Pairs9.txt" file. The second task included extracting all questions and answers from "QA_Pairs9.txt" and 
# outputting the results into two new files, 'extracting_questions.txt' and 'extracting_Answers.txt'.
# The third task consisted of finding the term frequency of each word found in 'extracting_questions.txt' and 'extracting_Answers.txt' and outputting the frequency results in 
# "frequency_of_answers.txt" and "frequency_of_questions.txt". 
# Finally, the final task ranked the decreasing order of the frequency of each word from the 'extracting_Answers.txt' file and
# produced the results in a new file called 'decreasing_frequency_of_answers.txt.' 

def count_pairs(file_name):
    
    with open(file_name, encoding='utf-8-sig') as nameHandle:
        lines = nameHandle.readlines() #readlines method returns the entire file as a list of strings 
      
    # if a file has all answers and no questions 
    lines_with_answers = True 
    
    if len(lines) == 0:
        lines_with_answers = False 
        
    for i in lines:
        if i.startswith("question"):
            lines_with_answers = False 
            
    if lines_with_answers == True:
        raise Exception("yikes")
        
    new_lines= str(lines)
    count_qa_pairs = new_lines.count('answer')

    return count_qa_pairs
  
def decreasing_frequency(new_questions):

  sortValues = {k:v for k,v in sorted(new_questions.items(), key = lambda v:v[1], reverse = True)}
  return sortValues 

def frequency(questions):

  questions_in_str = ''.join(questions)
  
  words = questions_in_str.split() 
  for w in words: # get rid of question mark in some words 
      if w[-1] == '?':
          words.append(w[:-1])
          words.remove(w)
           
  for w in words: # get rid of the word question 
      if w == 'question':
        words.remove(w)
         
  new_questions = {}

  for word in words:
     
    if word not in new_questions:
        new_questions[word] = 1 # initialize it to 1 
    else:
        new_questions[word] +=1 # if it was already put into new_s and it appears again then increment its value 
  
  return new_questions.items() # sets it as tuples in a list 


def frequency_2(answers):

  answers_in_str = ''.join(answers)
  
  words = answers_in_str.split() 
  for w in words: # get rid of question mark in some words 
      if w[-1] == '?':
          words.append(w[:-1])
          words.remove(w)
           
  for w in words: # get rid of the word question 
      if w == 'answer':
        words.remove(w)
         
  new_questions_1 = {}

  for word in words:
      
    if word not in new_questions_1:
        new_questions_1[word] = 1 # initialize it to 1 
    else:
        new_questions_1[word] +=1 # if it was already put into new_s and it appears again then increment its value 
  
    
  k = decreasing_frequency(new_questions_1)
  with open('decreasing_frequency_of_answers.txt', 'w') as nameHandle_5:
      for i,j in k.items():
            nameHandle_5.write('%s, %s\n' % (i,j))
      
  return new_questions_1.items() # sets it as tuples in a list 

def extracting_questions(questions):
    
    str_of_questions = ''.join(questions)
    str_of_questions_2 = str_of_questions.split('question')
      
    list_of_questions = []
    for i in str_of_questions_2:
        list_of_questions += i.lstrip()
        
    final_str_of_questions = ''.join(list_of_questions)  
    return final_str_of_questions 
 
def extracting_answers(answers):
    
    str_of_answers = ''.join(answers)
    str_of_answers_2 = str_of_answers.split("answer")
      
    list_of_answers = []
    for i in str_of_answers_2:
        list_of_answers += i.lstrip()
        
    final_str_of_answers = ''.join(list_of_answers)  
    
    return final_str_of_answers 
  

def questions_and_answers(file_name):
    
   with open(file_name, encoding='utf-8-sig' ) as nameHandle:
     lines = nameHandle.readlines() # returns a list of strings from each line 

   questions = []
   answers = []
   for i, line in enumerate(lines):
      if 'answer' in line:
          answers.append(lines[i])
          questions.append(lines[i+1])
    
   t = frequency(questions)
   with open("frequency_of_questions.txt", "w") as nameHandle_3:
        for x,y in t:
            nameHandle_3.write('%s, %s\n' % (x,y))
            # %s allows me to form a string after I add mod symbol  
            
   n = frequency_2(answers)
   with open("frequency_of_answers.txt", "w") as nameHandle_4:
        for i,j in n:
            nameHandle_4.write('%s, %s\n' % (i,j))
   
   z = extracting_questions(questions)
   with open('extracting_questions.txt', 'w') as nameHandle_1:
      nameHandle_1.write(z) 
     
   l = extracting_answers(answers)
   with open('extracting_Answers.txt', 'w') as nameHandle_2:
       nameHandle_2.write(l) 
       
   return questions 

          
if __name__ == "__main__":    
   print(count_pairs("QA_Pairs9.txt"))
   k =(questions_and_answers("QA_Pairs9.txt"))
 
  
   
