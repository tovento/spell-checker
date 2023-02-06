class UI:
    def __init__(self):
        pass

    def start(self):
        """TODO"""
        print("Write 'q' to quit.")
        print("Write a word for spellchecker.")

        while True:
            command = input("word: ")

            if command == "q":
                break
            else:
                print("great!")
