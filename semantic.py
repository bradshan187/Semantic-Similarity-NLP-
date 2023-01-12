import spacy

#------1------
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("head")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(word3.similarity(word4))
print(word4.similarity(word2))
print(word4.similarity(word1))

# what i found interesting from this piece of code is that when I added in the word "head", is beared very little similarity to the other words.
# although I expected little similarity between head and banana, I espected more between head and monkey and head and cat since both of these are animals with heads.
# head does have more similarity with monkey than it does with cat. 

#------2------
tokens = nlp('cat apple monkey banana head ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# what is interesting about these words is that it knows that 2 fruits are somewhat similar aswell as animals despite the actual words bearing no resemblance.

#------3------
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana",
"The black cat that comes onto the garden has come back and wants some food",
"I went for a walk today and managed to get to the next village before I realised I had to turn back",
"Por qué mi gato está en el coche"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# what is interesting about this piece of code is that the sentence that is most similar has 3 matching words, which is more than any of the others have.
# the least similar original sentence only has 1 matching word and has almost no relevance to the compared sentence apart from the one word and that a vehicle is mentioned in both, despite this the similariy is still over 0.5.
# I then added 2 more sentences in (one with some relevance to the sentence to compare and one without) to see if the length of the sentence made any difference in the similarity which it doesn't seem to.
# out of interest, I wanted to see how it compared the same sentence but in a different language, so I wrote the model sentence in spanish and it returned a negative figure which I found surprising.

# from running the example file with the simpler language model, what was interesting is how the similarity was much lower between the complaints and recipe and that the range was much higher.