from random import randint, choice

faces = ("I ", "you ", "he ", "she ", "it ", "we ", "they ")

face_verb = {"I ": "am", "you ": "are",
             "we ": "are", "they ": "are"}
# all the virbs (the is for the 3rd face and it will become "is")
verbs = ("i", "play", "sleep", "eat",
         "drink", "smell", "judge", "open", "drive", "cum", "come", "walk", "run", "jump", "sit", "break", "cut", "fuck", "anger", "fight", "hit", "shoot", "fix", "read", "use", "make", "imitate", "rob", "turn", "ride", "heal")
# pairing some virbs with a word so they make sense
verb_exc = {"cum": " on", "come": " to", "walk": " past",
            "run": " from", "jump": " over", "sit": " on", "sleep": " on", "play": " with", "turn": " on"}

nouns = ("car", "guitar", "mom", "dad", "man", "woman", "table", "butt", "floor", "teacher",
         "microwave", "ball", "mouse", "dog", "paper", "wall", "city", "hoe", "person", "floor", "truck", "pill", "pillow", "keyboard", "case", "house", "pencil", "feild", "camera", "lady", "monitor", "lock", "bike", "horse", "god", "blacksmith", "cowboy", "map", "doctor", "nurse", "professor", "plumber")

consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L",
              "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
end = False
while end == False:
    # choosing a face
    the_face = faces[randint(0, 6)]
    # cheching if the face is the 3rd face
    third_face = the_face == "he " or the_face == "she " or the_face == "it "
    # face, verb pair to seperate them from the other verbs

    # choosing which verb to use with which face
    def choose_verb():
        if third_face:
            verb = choice(verbs)
            return verb + "s"
        else:
            # choosing a verb from the verbs list and face verb
            verb = choice((choice(verbs), face_verb[the_face]))
            # choosing ramdomly between the "normal" verbs and the "default" verbs
            return verb

    chosen_verb = choose_verb()

    if third_face:
        verb_neg_interr = chosen_verb[0:-1]
    else:
        verb_neg_interr = chosen_verb

    # putting an "s" to the verb of the 3rd face if it's an "exception verb"
    def exc(verb=chosen_verb):
        result_verb = verb
        verb_neg = verb_neg_interr
        # checking if the verb belongs to the exception dict, if yes at the word
        for key in verb_exc:
            if key + "s" == verb:
                result_verb = verb + verb_exc[key]
                verb_neg += verb_exc[key]
                break
            # saving the verb without the "s" for the interrogative of a third face
            elif key == verb:
                result_verb = verb + verb_exc[key]
                verb_neg += verb_neg_interr + verb_exc[key]
                break

        return result_verb, verb_neg

    the_exc = exc()
    the_verb = the_exc[0]
    verb_neg_interr = the_exc[1]

    choose_noun = choice(nouns)

    # if it's plural put a space, if it's singular put an "a", if it's "you" choose randomly if it's plural or singular (because "you" is the same in both)
    def choose_letter_before_noun(face=the_face, verb=the_verb):
        return choice(("", "a "))

    the_letter = choose_letter_before_noun()

    # if it's plural add an "s" or "ies"
    def modify_noun(noun=choose_noun, letter=the_letter):
        if the_letter == "":
            if noun[-1] == "y" and noun[-2].upper() in consonants:
                return noun[:-1] + "ies"
            else:
                return noun + "s"
        else:
            return noun
    the_noun = modify_noun()

    print("affirmative: " + the_face +
          the_verb + " " + the_letter + the_noun)
    if third_face and the_verb != "is":
        print("interrogative: " + "does " + the_face +
              verb_neg_interr + " " + the_letter + the_noun + "?")
        print("negative: " + the_face + "does not " +
              verb_neg_interr + " " + the_letter + the_noun)
    elif the_verb == "am" or the_verb == "are" or the_verb == "is":
        print("interrogative: " + the_verb + " " + the_face +
              the_letter + the_noun + "?")
        print("negative: " + the_face +
              the_verb + " not" + " " + the_letter + the_noun)
    else:
        print("interrogative: " + "do " + the_face +
              the_verb + " " + the_letter + the_noun + "?")
        print("negative: " + the_face + "do not " +
              the_verb + " " + the_letter + the_noun)

    again = input("press X to exit: ")
    if again.upper() == "X":
        end = True
    else:
        end = False
