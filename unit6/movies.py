import csv

FILENAME = "movies.txt"

def write_movies(movies):
    with open(FILENAME, "w") as file: # write to txt file
        for movie in movies:
            file.write(movie + "\n")

def read_movies():
    movies = []
    with open(FILENAME) as file: # read from txt file
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
    return movies

def list_movies(movies):
    for i in range(len(movies)): # for every movie in however long the list is
        movie = movies[i]
        print(str(i+1) + ". " + movie)
    print()

def add_movie(movies):
    movie = input("Movie: ") # no need to append a new list as this is being applied directly to "movies" list
    movies.append(movie)
    write_movies(movies) # writing added movie to txt file
    print(movie + " was added.\n")

def delete_movie(movies):
    index = int(input("Number: "))
    movie = movies.pop(index - 1)
    write_movies(movies) # writing deleted movie to txt file
    print(movie + " was deleted.\n")

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
    while True: # forever unless loop is broken manually
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