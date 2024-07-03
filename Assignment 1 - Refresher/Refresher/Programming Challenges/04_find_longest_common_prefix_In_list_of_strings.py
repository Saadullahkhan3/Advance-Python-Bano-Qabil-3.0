
class FindPrefix:
    def __init__(self) -> None:
        self.a_to_z = [chr(i) for i in range(97, 123)]
        

    def longest_occurences_words(self, list_of_str: list[str], start: int=0):
        
        dict_no_of_occurnce = {key:[list(), list()] for key in self.a_to_z}

        for alphabet in self.a_to_z:
            for word in list_of_str:
                current_alphabet_dict = dict_no_of_occurnce[alphabet]
                
                if word[start] == alphabet:
                    current_alphabet_dict[1] += [word]
                
                # When same prefix word ends, due to sorting all same prefix words are together
                if not word[start] == alphabet and len(current_alphabet_dict[1]) != 0:
                    break

            current_alphabet_dict[0] = len(current_alphabet_dict[1])

        max_length = max([dict_no_of_occurnce[v][0] for v in self.a_to_z])
 
        return (dict_no_of_occurnce, max_length)


    def extract_values(self, dict_no_of_occurnce, max_length):
        extracted_values = list()
        
        for i in [max_length]:
            for key in dict_no_of_occurnce:
                _length = dict_no_of_occurnce[key][0]
                _word_list = dict_no_of_occurnce[key][1]

                if _length == i:
                    extracted_values.append(_word_list)
                    
        return extracted_values


    def join_list(self, list_of_list: list[list[str]]):
        joined_lst = list()
        try:
            for lst in list_of_list:
                joined_lst += lst
            return joined_lst
        except:
               return list_of_list


    def find_longest_common_prefix_In_list_of_str(self, list_of_str: list[str]):
        list_of_str = [i.lower() for i in list_of_str]
        list_of_str.sort()
        
        dict_no_of_occurnce, max_length = self.longest_occurences_words(list_of_str=list_of_str)

        extracted_values = self.extract_values(dict_no_of_occurnce=dict_no_of_occurnce, max_length=max_length)

        joined_list =  self.join_list(extracted_values)

        new_list = list()
        index = int()   # Used for Prefix indexing

        for i in range(1, 10000):
            index = i
            new_list = self.extract_values(*self.longest_occurences_words(joined_list, i))            

            if len(new_list) == len(extracted_values):
                continue

            else:
                if len(new_list[0]) == len(extracted_values[0]):
                    extracted_values = new_list
                    continue

                else:
                    break
        
        prefix = [i[0][0:index] for i in extracted_values]
        
        return prefix, extracted_values


    def show_output(self, prefixs: list[str], words_list: list[str]):
        print("\n" + "-"*50)
        for prefix in prefixs:
            print(f"Prefix: {prefix}")
            lst = [w_lst for w_lst in words_list if w_lst.lower().startswith(prefix)]
            print(f"list of Words: {lst}")
            print("-"*50 + "\n")


    def take_input(self):
        _input = input("Enter words by space separated. \nEnter here : ")
        list_input = _input.split() if _input else self.no_input_given()
        return list_input


    def no_input_given(self):
        raise ValueError(f"\n{"~"*50}\nEmpty Input Error: Input is empty! \n{"~"*50}")



obj = FindPrefix()
lst_of_input = obj.take_input()
prefixs, lst_of_prefixed_words = obj.find_longest_common_prefix_In_list_of_str(lst_of_input)

# Here should be pass selected words but..
# Passing original words so it can be more nice!
obj.show_output(prefixs=prefixs, words_list=lst_of_input)


# Output:
'''
Enter words by space separated. 
Enter here : Flower flu Saad Saif Sajjad flag

--------------------------------------------------
Prefix: fl
list of Words: ['Flower', 'flu', 'flag']
--------------------------------------------------

Prefix: sa
list of Words: ['Saad', 'Saif', 'Sajjad']
--------------------------------------------------

'''
