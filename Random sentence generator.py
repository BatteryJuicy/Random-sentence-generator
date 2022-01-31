from random import randint

end = False
while end == False:
    count = 0
    while count <= 100:
        # choosing a face
        faces = ("I ", "you ", "he ", "she ", "it ", "we ", "they ")
        the_face = faces[randint(0, 6)]
        # face, verb pair to seperate them from the other verbs
        face_verb = {"I ": "am", "you ": "are", "we ": "are", "they ": "are"}
        # all the virbs (the is for the 3rd face and it will become "is")
        verbs = ("i", "play", "sleep", "eat",
                 "drink", "smell", "judge", "open", "drive", "cum", "come", "walk", "run", "jump", "sit", "break", "cut", "fuck", "anger", "fight", "hit", "shoot", "fix", "read", "use", "make", "imitate", "rob", "turn", "ride", "heal")
        # pairing some virbs with a word so they make sense
        verb_exc = {"cum": " on", "come": " to", "walk": " past",
                    "run": " from", "jump": " over", "sit": " on", "sleep": " on", "play": " with", "turn": " on"}

        # choosing which verb to use with which face
        def choose_verb(face=the_face):
            # putting an "s" at the end the verb if it is 3d face
            if face == "he " or face == "she " or face == "it ":
                return verbs[randint(0, len(verbs) - 1)] + "s"
            else:
                # choosing the verb from the verbs list for the rest of the faces(not including the "i")
                verb = (verbs[randint(1, len(verbs) - 1)], face_verb[face])
            # choosing ramdomly between the "normal" verbs and the "default" virbs
            return verb[randint(0, 1)]

        chosen_verb = choose_verb()

        # putting an "s" to the virb of the 3rd face if it's an "exception virb"
        def exc(verb=chosen_verb):
            result_verb = verb
            # checking if the verb belongs to the exception dict, if yes at the word
            for key in verb_exc:
                if key == verb or key + "s" == verb:
                    result_verb = verb + verb_exc[key]
                    break
            return result_verb

        the_verb = exc()
        # the list with all the nouns
        nouns = ("car", "guitar", "mom", "dad", "man", "woman", "table", "butt", "floor", "teacher",
                 "microwave", "ball", "mouse", "dog", "paper", "wall", "city", "hoe", "person", "floor", "truck", "pill", "pillow", "keyboard", "case", "house", "pencil", "feild", "camera", "lady", "monitor", "lock", "bike", "horse", "god", "map", "doctor", "nurse", "professor", "plumber")
        choose_noun = nouns[randint(0, len(nouns) - 1)]

        # if it's plural put a space, if it's singular put an "a", if it's "you" choose randomly if it's plural or singular (because "you" is the same in both)
        def choose_letter_before_noun(face=the_face, verb=the_verb):
            if the_face == "we " or the_face == "they ":
                return " "
            elif the_face == "you ":
                return (" ", " a ")[randint(0, 1)]
            else:
                return " a "
        the_letter = choose_letter_before_noun()

        def modify_noun(noun=choose_noun, letter=the_letter):
            if the_letter == " ":
                return noun + "s"
            else:
                return noun
        the_noun = modify_noun()

        print(the_face + the_verb + the_letter + the_noun)
        count += 1
    count = 0
    end = True
    again = input("again? Press A. Else press anything: ")
    if again.upper() == "A":
        end = False
