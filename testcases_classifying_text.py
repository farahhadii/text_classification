import unittest
import classifying_text

class A2Tests(unittest.TestCase):
    
    def test_count_pairs_returns_2_from_file_example(self):
      self.assertEqual(classifying_text.count_pairs("file_count_pairs_example.txt"), 2)
        
    def test_count_pairs_returns_0_from_file_example(self):
      self.assertEqual(classifying_text.count_pairs("file_count_pairs_example2.txt"),0)
      
    def test_count_pairs_returns_exception_when_no_question_found(self):
        with self.assertRaises(Exception):
           classifying_text.count_pairs("file_count_pairs_exception.txt")
            
    def test_smaller_file_and_extract_all_questions(self):
        self.assertEqual(classifying_text.questions_and_answers("file_with_questions_and_answers.txt"),["question Who is Arya Stark's wife?\n", 'question Who escaped the persecution of House Stark?\n'])

    def test_empty_file_of_questions_and_answers(self): 
       self.assertEqual(classifying_text.questions_and_answers("file_with_empty_questions_and_answers.txt"), [])
     
    def test_smaller_list_of_answers_returning_string_of_answers(self):
      self.assertEqual(classifying_text.extracting_answers(['answer Jon Snow, King\n', 'answer Winterfell\n']),'Jon Snow, King\nWinterfell\n')
      
    def test_empty_list_of_answers_returns_empty_string_of_answers(self):
        self.assertEqual(classifying_text.extracting_answers([]),"")
         
    def test_smaller_list_of_questions_returning_string_of_questions(self):
       self.assertEqual(classifying_text.extracting_questions(['question What male line does Arya exterminate after returning to Westeros?\n', "question Who is the half-brother of Arya's half-brother?\n"]),"What male line does Arya exterminate after returning to Westeros?\nWho is the half-brother of Arya's half-brother?\n")
    
    def test_smaller_list_of_questions_returning_frequency_of_each_word(self):   
          self.assertIsNot(classifying_text.frequency(["Who is Arya Stark's wife?\n"]), [("wife", 3), ("house", 1)])
    
    def test_list_of_answers_returning_empty_frequency_for_each_word(self):
         self.assertIsNot(classifying_text.frequency_2(["Lady Catelyn Stark"]),[()])      

    def test_dictionary_of_words_returning_order_of_frequency_of_each_word(self):
        self.assertEqual(classifying_text.decreasing_frequency({'and': 509,'to': 301,'of': 396,'the': 747}), {'the': 747, 'and': 509, 'of': 396, 'to': 301})
        
    def test_dictionary_of_words_of_the_same_frequency_returning_the_same_order(self):
         self.assertEqual(classifying_text.decreasing_frequency({'virgin': 4, 'Giantsbane': 4, 'garrison': 4, 'tunnel': 4}),{'virgin': 4, 'Giantsbane': 4, 'garrison': 4, 'tunnel': 4})
            

if __name__ == '__main__':
  unittest.main(exit=True)
  
  
  
  
