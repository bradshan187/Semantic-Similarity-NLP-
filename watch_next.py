# importing spacy
import spacy

# specifying the model to use
nlp = spacy.load('en_core_web_md')

# creating a function to return the most similar film
def watch_next(description):

    # setting the max_similarity to 0 to return the film with the highest number since all are above 0
    max_similarity = 0

    # creating a variable to store the mosyt similar title
    max_title = ""

    # opening and reading the text file
    with open('movies.txt', 'r') as file:
        films = file.readlines()

    # for each film in the file, storing the title and description for each film in separate functions
    for film in films:
        film = film.strip()
        title_description = film.split(':')
        title, descript = title_description[0], title_description[1]
        
        # comparing the similarity between each film from the text file and the argument passed through the function
        model_sentence = nlp(description)
        similarity = nlp(descript).similarity(model_sentence)
        
        # finding the most similar film from the comparison just made
        if similarity > max_similarity:
            max_similarity = similarity
            max_title = title
            max_descript = descript
            
    # printing the title and the description of the most similar film
    print(max_title + ":", max_descript)

    # closing the file
    file.close()

# calling the function with the description to find the most similar film
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
(watch_next(description))
