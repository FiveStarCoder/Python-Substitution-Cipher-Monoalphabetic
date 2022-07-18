import sys
import time
import keyboard

class MonoAlphabetic_Substituion:


    def __init__(self,text = "Hello", jumps = 1):
        self.text = text
        self.jumps = jumps

    def get_text(self):
        return self.text

    def encipher(self,case_sensitive=False):





        if case_sensitive:
            self.encoded_text = ""
            # run the for loop
            for char in self.text:
                # get the ascii integer value of the character
                value = ord(char)
                if value > 90:
                    # it is lower
                    # increment the value with the jumps
                    value += self.jumps
                    while value > 122:
                        value = 97 + (value - 122) - 1

                    # convert integer to character
                    self.encoded_text += chr(value)

                else:
                    # it is Upper
                    # increment the value with the jumps
                    value += self.jumps
                    while value > 90:
                        value = 65 + (value - 90) - 1

                    # convert integer to character
                    self.encoded_text += chr(value)

        else:
            self.encoded_text = ""
            # run the for loop
            for char in self.text.upper():
                # get the ascii integer value of the character
                value = ord(char)
                # increment the value with the jumps
                value += self.jumps
                while value > 90:
                    value = 65 + (value - 90) - 1

                # convert integer to character
                self.encoded_text += chr(value)

        return self.encoded_text

    def decipher(self,case_sensitive=False):
        if case_sensitive:
            self.decoded_text = ""
            # run the for loop
            for char in self.text:
                # get the ascii integer value of the character
                value = ord(char)
                if value > 90:
                    # it is lower
                    # increment the value with the jumps
                    value -= self.jumps

                    while value < 97:
                     value = 122 - (97 - value) + 1

                    # convert integer to character
                    self.decoded_text += chr(value)
                else:

                    # it is upper
                    # increment the value with the jumps
                    value -= self.jumps

                    while value < 65:
                        value = 90 - (65 - value) + 1

                    # convert integer to character
                    self.decoded_text += chr(value)


        else:
            self.decoded_text = ""
            # run the for loop
            for char in self.text.upper():
                # get the ascii integer value of the character
                value = ord(char)
                # increment the value with the jumps
                value -= self.jumps
                while value < 65:
                    value = 90 - (65 - value) + 1

                # convert integer to character
                self.decoded_text += chr(value)



        return self.decoded_text

    def loading(self):
        loop_time = 2
        loading_speed = 4  # number of characters to print out per second
        loading_string = "Loading" + "." * 5  # characters to print out one by one (6 dots in this example)

        for x in range(loop_time):
            #  track both the current character and its index for easier backtracking later
            for index, char in enumerate(loading_string):
                # you can check your loading status here
                # if the loading is done set `loading` to false and break

                sys.stdout.write(char)  # write the next char to STDOUT
                sys.stdout.flush()  # flush the output
                time.sleep(1.0 / loading_speed)  # wait to match our speed
            index += 1  # lists are zero indexed, we need to increase by one for the accurate count
            # backtrack the written characters, overwrite them with space, backtrack again:

            sys.stdout.write("\b" * index + " " * index + "\b" * index)
            sys.stdout.flush()  # flush the output



if __name__ == '__main__':
    try:

        print('*' * 20, 'MONOALPHABETIC SUBSTITUTION','*' * 20)
        # text = input("ENTER THE INPUT TEXT:\t").strip().upper()
        # jumps = int(input("ENTER THE JUMPS:\t").strip())
        #
        # # create method object
        # method = MonoAlphabetic_Substituion(text = text, jumps=jumps)
        #
        # method.loading()
        #
        #
        #
        #
        # print("Your Original Text is ::\t" + method.get_text())
        # print("Your Cipher Text is ::\t" + method.encipher())





        # print("Your Decoded Text is ::\t" + method.decipher("KHOoR",3))

    except Exception as e:
       e.with_traceback()


