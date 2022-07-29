
import enchant      # english dictionary
import timeit

all_times = []

def main():
    

    # First of all, ask for the sequence of characters to filter
    word_to_work_on: str = input("Please enter a sequence of characters.\n> ")

    # Then perform the algorithm
    print("\nPerforming calculations...\n")
    all_combinations: list[str] = get_all_word_bits(word_to_work_on)
    print("\nFinished calculations! Here are the sorted results...\n")

    all_combinations.sort()

    for index, item in enumerate(all_combinations):
        converted_to_string = convert_char_array_to_string(item)

        # if is_word(converted_to_string):
            # print(f"{all_times[index]}: {converted_to_string}")
        print(converted_to_string)


def get_all_word_bits(word: str = "", char_array: list[str]=[], index_to_start_with: int=0, all_possible_combinations: list[str]=[], is_internal=False, recursion_depth=1) -> list[str]:
    
    # Begin timer
    start_time = timeit.default_timer()
    
    # End recursion when word is 1 character long
    if len(word) == 1:
        return all_possible_combinations

    # End recursion when char array is empty
    elif is_internal and len(char_array) == 1:
        if (char_array not in all_possible_combinations) and is_word(convert_char_array_to_string(char_array)):
            print(convert_char_array_to_string(char_array))
            all_possible_combinations.append(char_array)
        
        # end timer
        end_time = timeit.default_timer()
        total_time = end_time - start_time
        all_times.append(total_time)
        # print(str(end_time - start_time), end=' | ')

        return all_possible_combinations
    
    # Otherwise, perform algorithm
    elif word != "":        # Filter out empty string

        # Convert string to char array; typically only used on first iteration
        if len(char_array) == 0:
            word_copy: str = word        # copy word first
            char_array = convert_string_to_char_array(word_copy)        # convert string to char array

        if (char_array not in all_possible_combinations) and is_word(convert_char_array_to_string(char_array)):
            print(convert_char_array_to_string(char_array))
            all_possible_combinations.append(char_array)
        
        for index, character in enumerate(char_array):

            """
            Remove one character at a time, then run this function again with that word.
            """

            char_array_copy = list(char_array)      # wrap around in a list to create a copy rather than a reference

            char_array_copy.pop(index)       # remove char at index from word
            
            result = get_all_word_bits(word, char_array_copy, index+1, all_possible_combinations, True, recursion_depth+1)

            for item in result:
                if item not in all_possible_combinations and is_word(item):       # sloppy filter
                    print(item)
                    all_possible_combinations.append(item)

    # end timer
    end_time = timeit.default_timer()
    total_time = end_time - start_time
    all_times.append(total_time)
    # print(str(end_time - start_time), end=' | ')

    return all_possible_combinations


def convert_string_to_char_array(source: str) -> list[str]:
    final_array: list[chr] = []

    for character in source:
        final_array.append(character)

    return final_array


def convert_char_array_to_string(source: list[str]) -> str:
    final_string: str = ""
    
    for item in source:
        final_string += item
    
    return final_string


def is_word(word: str) -> bool:
    dictionary = enchant.Dict("en_US")
    return dictionary.check(word)

main()