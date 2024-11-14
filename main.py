import openai
import requests

# (pomiędzy apostrofami wklej swój klucz dostępu do OpenAI API)
openai.api_key = ''

article_url = "https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt"

#pobranie artykułu
def fetch_article(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Błąd pobierania artykułu")
        return None

# Integracja API
def process_article_with_openai(article_text):
    prompt = f"""
    Przetwórz poniższy artykuł, używając odpowiednich znaczników HTML do uporządkowania treści.
    Określ miejsca, w których warto wstawić grafikę za pomocą znacznika <img> i atrybutu src="image_placeholder.jpg". Dodaj atrybut alt do
    każdego obrazu z precyzyjną podpowiedzią, którą możemy wykorzystać do wygenerowania grafiki.
    Umieść podpisy pod grafiką, korzystając z odpowiedniego tagu HTML.
    Nie używaj CSS ani JavaScript. Zwrócony kod powinien zawierać tylko treść polecenia do
    wstawki pomiędzy tagami <body> i </body>. Nie dołączaj tagów <html>,
    <head> lub <body>.
    
    Oto artykuł:
    {article_text}
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4", 
            messages=[
                {"role": "system", "content": "Jesteś asystentem AI do przetwarzania artykułów na kod HTML."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,  
            temperature=0.5 
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Błąd komunikacji z API: {e}")
        return None

# Tutaj zapisanie HTML do pliku
def save_html_to_file(html_content):
    try:
        with open("artykul.html", "w", encoding="utf-8") as file:
            file.write(html_content)
        print("HTML zapisany do pliku artykul.html")
    except Exception as e:
        print(f"Błąd zapisu pliku: {e}")

#Główna funkcja
def main():
    article_text = fetch_article(article_url)
    if article_text:
        html_content = process_article_with_openai(article_text)
        if html_content:
            save_html_to_file(html_content)

if __name__ == "__main__":
    main()
