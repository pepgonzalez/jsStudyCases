import urllib

def read_text():
    #open es una built-in function de python, siempre disponible
    file = open("C:\Users\joseg\Desktop\Udacity\quotes.txt")
    text = file.read()
    print(text)
    file.close()
    check_profanity(text)

    #wdyl.com -> sitio que te dice si un texto dice una blasfemia (profanity)
def check_profanity(string):
    url = "http://isithackday.com/arrpi.php?text=" + string
    #urllib no es una built-in funtion de python, se debe importar
    connection = urllib.urlopen(url)
    
read_text()
