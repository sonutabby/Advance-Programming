#Creating a dictionary with film details, I use the variable 'Movie'
Movie = {
    "Title": "Harry Potter",  #Film title
    "Author/Director": "J.K. Rowling", #Author's name
    "Year": 2001,  #Release year
    "Genre": "Action/Mystery", #Film genre
    "Rating": 9.6 #Film rating
}

#Displaying film details using a loop
for key, value in Movie.items(): #The key-value pairs in the Movie dictionary are iterated over using the for loop and Movie.items()
    print(f"{key}: {value}") #To display the movie's details, each key-value pair is printed inside the loop using string formatting (f"{key}: {value}")
