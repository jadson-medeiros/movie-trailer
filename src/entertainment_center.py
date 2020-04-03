import fresh_tomatoes
from get_movie_list import get_movie_list


def main():
    
    # Read movies from a json file.
    movielist = get_movie_list("data\movies.json") 
    # Generate the html file and display in a browser window.
    fresh_tomatoes.open_movies_page(movielist) 
    
main()
