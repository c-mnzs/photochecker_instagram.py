import sys
from requests_html import HTMLSession
import time

def checker():
    if len(sys.argv) < 2:
        invalid_len_message()

    else:
        try:
            if sys.argv[1].lower() == "--hashtag":
                if sys.argv[2]:
                    if "#" in sys.argv[2]:
                        newarg = sys.argv[2].replace("#", "")

                        print(check_hashtags(newarg))
                    
                    else:
                        print(check_hashtags(sys.argv[2]))
            
            else:
                error_message(sys.argv[1])

        except IndexError:
            usage_message("photochecker.py --hashtag 'hashtag'")
                
def check_hashtags(hashtag):
    session = HTMLSession()

    url = f'https://www.hashatit.com/hashtags/{hashtag}'
    r = session.get(url)
    time.sleep(2)
    photo = r.html.find('.photo', first=True)

    if(photo):
        screen = photo.find('.screen', first=True)
        if "instagram" in screen.text.lower():
            links = photo.find('a.image-link', first=True)
            link = list(links.absolute_links)[0]

            name = photo.find('a.favicon', first=True)
            
            string = f"Author: {name.text} | Link: {link}"
            
            return string
        else:
            return f"""ERROR: Hashatit couldn't retrieve posts in Instagram with the hashtag '{hashtag}' in it."""

    else:
        return f"""ERROR: No photos with the hashtag '{hashtag}' found."""

def invalid_len_message():
    print("""ERROR: You must pass in an argument. Run photochecker.py --hashtag 'hashtag'.""")
    
def error_message(arg):
    print(f"""ERROR: Argument '{arg}' does not exist. Run photochecker.py --hashtag 'hashtag'.""")

def usage_message(msg):
    print(f"USAGE: {msg}")

if __name__ == "__main__":
    checker()