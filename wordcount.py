" " " This program counts the number of times each unique word appears in a text file. The result  \
 are output to the command line, and the user is given the option of printing the results to a new file"""
'''providing unique value'''
import os

COMMON_WORDS = {"the", "be", "are", "is", "were", "was", "am",
                "been", "being", "to", "of", "and", "a", "in",
                "that", "have", "had", "has", "having", "for",
                "not", "on", "with", "as", "do", "does", "did",
                "doing", "done", "at", "but", "by", "from"}


class WordProcess:
    """This class returns the number of times each word appears in a text"""

    def __init__(self, file):
        """Construct class instance with file attribute."""
        self.file = file

    def sort_by_value(items):
        """Create a key to be used to sort wordlist"""
        return items[-1]

    def words_dict(self):
        """compare user input text file to english wordlist and return matches,"""
        if os.path.getsize(self.file):
            return False
        else:
            open_input_file = open(self.file, "r")
            wordlist_path = os.path.expanduser("~/Desktop/MyProject/python code")
            open_wordlist_file = open(wordlist_path, "r")

            read_input = open_input_file.read().split()
            read_wordlist = open_wordlist_file.read().split()

            count = 0
            for word in read_input:
                word = word.lower()
                # removing common punctuation so it's not part of the word.
                read_input[count] = word.strip(".,?!-_:;\/()")
                count += 1

            word_count = {}
            for word in read_input:
                word = word.lower()
                if word in read_wordlist:
                    if word not in word_count:
                        word_count[word] = 1
                    else:
                        word_count[word] += 1
                else:
                    continue
            open_input_file.close()
            open_wordlist_file.close()

            return word_count

    def print_top_words(self, choice):
        """ sort and print each unique word with its frequency to the console.
          Return the results as a list to use in file output
         """
        word_count = self.words_dict()
        # uses reverse order to sort (most frequent first).
        items = sorted(word_count.items(), key=WordProcess.sort_by_value, reverse=True)

        results_list = []

        # Truncates output if user wants to suppress common words.

        for word in items[:50]:
            if choice == "y" and word[0] not in COMMON_WORDS:
                result = word[0] + ": " + str(word[1]) + "times"
                results_list.append(result)
                print(result)
            elif choice == "n":
                result = word[0] + ": " + str(word[1]) + "times"
                results_list.append(result)
                print(result)
            return results_list


print('welcome to the broker text analysis program.\n')

'''asking user to provide information '''
while True:
    user_input = input("please enter the path and name of the text file you want"
                       " to analyze. (E.g.: C:/user/monthy/Desktop/file.txt):"
                       "\n")

    print("Reading file, one moment...")

    class_init = WordProcess(user_input)

    if os.path.isfile(user_input) is False:
        print("The file you specified does not exist")
        continue
    else:
        common_word = ""
        print("file read sucessfully!")

        while common_word != "y" or common_word != "n":
            common_word = input("Would you like to strip common words from the results? "
                                "(Y/N) ").lower()
            if common_word == "y" or common_word == "n":
                break
            print("compiling results, one moment...\n")

        new_result = WordProcess.print_top_words(class_init, common_word)
        break

        user_output = ""
        while user_output != "y" or user_output != "n":
            user_output = input("\n" "would you like to output these results to a file? "
                                "(Y/N) ").lower()

            if user_output == "y":
                # Relative path to current user's desktop.
                user_desktop = os.path.expanduser("~/Desktop")
                output_folder = "/Wordcount Output"
                # Removes path from file name.
                file_name = user_input.split("/")[-1]
                # Removes file extension from name.
                no_ext = file_name.rstrip(".", 1)[0]

                write_file = open(no_ext + "_results.txt", "w")
                write_file.write("Results for {}:\n\n".format(file_name))

                for line in new_result:
                    write_file.write(line + "\n")
                write_file.close()

                print('success!')
                break
            elif user_output == "n":
                print("Exiting...")
                break
        break

# def fizzbuzz():
#  for i in range (1,100):
#     if i % 3 == 0 and i%5 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0:
#         print("Buzz")
#     elif i % 5 == 0:
#         print("Fizz")
#     else:
#         print(str(i))
#
# fizzbuzz()
#  def __init__(self, num):
#         self.num = num
#     def check_parity(self):
#         if self.num % 2 == 0:
#             print("{} is even.".format(self.num))
#         else:
#             print("{} is odd.".format(self.num))
# x = Parity(12345)
# x.check_parity()
