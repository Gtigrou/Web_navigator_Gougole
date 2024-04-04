import requests
import webview

def display_html(html_code):
    webview.create_window("Viewer", html=html_code, width=800, height=600, resizable=True)
    webview.start()

def search_by_url(url):
    response = requests.get(url)
    if response.status_code == 200:  # Vérification de la réussite de la requête
        display_html(response.text)  # Affiche le contenu de la page
    else:
        print("La requête a échoué. Statut code :", response.status_code)

def search_():
    search = input("Your research =>> ")
    search = search.split()
    new = []
    for i in range(len(search)):
        if i != len(search) - 1:  # Corrigé l'indice utilisé dans la condition
            new.append(search[i] + "+")
        else:
            new.append(search[i])

    search = "".join(new)
    search = ("https://www.google.com/search?q=" + search)
    response = requests.get(search)

    if response.status_code == 200:  # Vérification de la réussite de la requête
        display_html(response.text)  # Affiche le contenu de la page
    else:
        print("La requête a échoué. Statut code :", response.status_code)


def main():
    search = ""
    while True:
        search = input(">>> ").lower()
        if search == "./help":
            print("""   
            ./Exit  ==> exit programs.
            ./URL   ==> search by URL.
            ./help  ==> show this panel.
            ./search ==> for searching something on Gougole.
            """)
            main()
        if search == "./exit":
            break
        if search == "./url":
            url = input("Url >>> ")
            search_by_url(url)
        if search == "./search":
            search_()
        print(f"Command Unknow:[{search}] type ./help for some tips ! error:001")
if __name__ == '__main__':
    main()