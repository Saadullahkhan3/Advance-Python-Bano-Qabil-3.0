'''Find the Longest Consecutive Sequence in a List of Integers'''

class LongestConsecutiveList:
    def __init__(self) -> None:
        self.longest_sequence_lists = list()
        self.max_list_length = int()


    def take_input(self):
        _input = input("Enter words by space separated. \nEnter here : ").strip()
        num_list_str = _input.split() if _input else self.no_input_given()
        num_list_int = [int(i) for i in num_list_str]
        return num_list_int


    def no_input_given(self):
        raise ValueError(f"\n{"~"*50}\nEmpty Input Error: Input is empty! \n{"~"*50}")


    def calc_consecutive_numbers(self, list_of_int: list[int]):
        list_of_int.sort()
        dict_key = 1
        dict_of_consecutive_lists = {dict_key: []}
        try:
            for index, number in enumerate(list_of_int):
                n1, n2 = number, number + 1
                # Checking that current number +1 is equal to next number
                if (n2) == (list_of_int[index+1]):
                    dict_of_consecutive_lists[dict_key] += [n1, n2]
                # When consecutive sequence not found then creating a new dict_key for new list
                else:
                    dict_key += 1
                    dict_of_consecutive_lists[dict_key] = list()
        except:
            return dict_of_consecutive_lists


    def fetch_longest_consecutive_list(self, dict_of_consecutive_lists: dict[list[int]]):
        # Keys of that lists have maximum length
        max_len_list_keys = [k for k in dict_of_consecutive_lists if dict_of_consecutive_lists[k] != []]

        # Final list that contain maximum length lists, if there are multiple lists
        required_lists = [list(set(dict_of_consecutive_lists[k])) for k in max_len_list_keys]

        # Calculating maximum length
        self.max_list_length = max([len(e) for e in required_lists])

        # Filtering list and creating collection with thier length
        for lst in required_lists:
            lst_len = len(lst)
            if lst_len == self.max_list_length:
                self.longest_sequence_lists.append(lst)

        return self.longest_sequence_lists


    def show_output(self):
        print("\n" + "~"*50)
        print(f"Longest Length is : {self.max_list_length}")
        print("~"*50)
        for lst in self.longest_sequence_lists:
            print(f"List with longest length: {lst}")
            print("-"*50)



def main(Object: LongestConsecutiveList):
    _input = Object.take_input()
    dict_of_consecutive_lists = Object.calc_consecutive_numbers(_input)
    Object.fetch_longest_consecutive_list(dict_of_consecutive_lists)
    Object.show_output()
    

if __name__ == "__main__":
    obj = LongestConsecutiveList()
    main(obj)

# Output:
'''
Enter words by space separated. 
Enter here : 6 1 2 87 7 10 45 43 11

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Longest Length is : 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
List with longest length: [1, 2]
--------------------------------------------------
List with longest length: [6, 7]
--------------------------------------------------
List with longest length: [10, 11]
--------------------------------------------------
'''
