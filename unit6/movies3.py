import pickle  # Using binary, so use pickle module

FILENAME = "movies.bin"

def write_movies(movies):
    with open(FILENAME, "wb") as file: # write to binary
        pickle.dump(movies, file)

def read_movies():
    movies = []
    with open(FILENAME, "rb") as file: # read from binary
        movies = pickle.load(file)
    return movies

def list_movies(movies):
    for i in range(len(movies)): # for every movie in however long the list is
        movie = movies[i]
        print(str(i+1) + ". " + movie[0] + " (" + str(movie[1]) + ")")
    print()

def add_movie(movies):
    name = input("Name: ")
    year = (input("Year: "))
    movie = [] # need to initialize the list before appending
    movie.append(name)
    movie.append(year) # year must be appended seperately
    movies.append(movie)
    write_movies(movies) # writing added movie to binary file
    print(name + " was added.\n")

def delete_movie(movies):
    index = int(input("Number: "))
    movie = movies.pop(index - 1)
    write_movies(movies) # writing deleted movie to binary file
    print(movie[0] + " was deleted.\n")

def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exits the program")

def main():
    display_menu()
    movies = read_movies()
    while True:# forever unless loop is broken manually
        command = input("Command: ")
        if    command == "list":
            list_movies(movies)
        elif command == "add":
            add_movie(movies)
        elif command == "del":
            delete_movie(movies)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")

if __name__ == "__main__":
    main()