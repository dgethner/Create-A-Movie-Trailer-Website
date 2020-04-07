#When we import fresh_tomatoes we are giving access to reference the file for use in this document.
#This is important as fresh_tomatoes is our code to be able to format our webpage.
import fresh_tomatoes
#When we import media we are giving access to reference the file for use in this document.
#This is important as media contains our class movie which is how we are able to create a blueprint for our objects.
import media

def getMoviesList():
    '''
    This function is used to generate data for each of the movies instances
    '''
    the_core = media.Movie("The Core",
                            "The story of a group adventuring to the center of the Earth.",
                            "https://upload.wikimedia.org/wikipedia/en/f/f4/The_Core_poster.jpg",
                            "https://www.youtube.com/watch?v=foAyvN6mVwQ",
                            "Jon Amiel",
                            "March 28, 2003",
                            "2h 15min",
                            "PG-13")

    a_night_at_the_roxbury = media.Movie("A Night At The Roxbury",
                            "Two borthers take the club by storm.",
                            "https://upload.wikimedia.org/wikipedia/en/0/02/A_night_at_the_roxbury.jpg",
                            "https://www.youtube.com/watch?v=BuqeN2FjrRQ",
                            "John Fortenberry",
                            "October 2, 1998",
                            "1h 22min",
                            "PG-13")

    corky_romano = media.Movie("Corky Romano",
                            "A dyfunctional Mafia family against the FBI.",
                            "https://upload.wikimedia.org/wikipedia/en/1/18/Corky_Romano_DVD_box_cover.jpg",
                            "https://www.youtube.com/watch?v=nidmVOLy0ZI",
                            "Rob Pritts",
                            "October 12, 2001",
                            "1h 26min",
                            "PG-13")

    oceans_thirteen = media.Movie("Ocean's Thirteen",
                            "A group of professional criminals trying to rob a casino.",
                            "https://upload.wikimedia.org/wikipedia/en/c/c1/Oceans13Poster1.jpg",
                            "https://www.youtube.com/watch?v=QdCFxe-ottI",
                            "Steven Soderbergh",
                            "June 8, 2007",
                            "2h 2min",
                            "PG-13")

    casino = media.Movie("Casino",
                            "Two best friends compete over a gambling empire.",
                            "https://upload.wikimedia.org/wikipedia/en/d/d8/Casino_poster.jpg",
                            "https://www.youtube.com/watch?v=EJXDMwGWhoA",
                            "Martin Scorsese",
                            "November 22, 1995",
                            "2h 58min",
                            "R")

    gran_torino = media.Movie("Gran Torino",
                            "A Vet sticks up for what he believes in, protecting his neighborhood.",
                            "https://upload.wikimedia.org/wikipedia/en/c/c6/Gran_Torino_poster.jpg",
                            "https://www.youtube.com/watch?v=AUiU42iOi4M",
                            "Clint Eastwood",
                            "January 9, 2009",
                            "1h 56min",
                            "R")


    movies = [the_core, a_night_at_the_roxbury, corky_romano, oceans_thirteen, casino, gran_torino]
    return movies

mList = getMoviesList()

def validateMovieData(mList):
    '''
    This function will check if each movie listed has any missing information
    '''
    valid = True
    for item in mList:
        if (item.title == '' or item.storyline == '' or item.poster_image_url == '' or item.trailer_youtube_url == '' or
            item.director == '' or item.launch_date == '' or item.duration == '' or item.rating == ''): 
            valid = False
            print item.title
            break
    return valid

validateMovieData(mList)

fresh_tomatoes.open_movies_page(getMoviesList())
