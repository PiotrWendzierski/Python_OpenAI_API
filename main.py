import openai
import requests

# (pomiędzy apostrofami wklej swój klucz dostępu do OpenAI API)
openai.api_key = ''

article_url = "https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt"

# pobranie artykułu
def fetch_article(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Podnosi wyjątek dla kodów błędów HTTP (np. 404, 500)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Błąd pobierania artykułu: {e}")
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
        # Sprawdzamy, czy odpowiedź zawiera wymagane dane
        html_content = response.get('choices', [{}])[0].get('message', {}).get('content', '').strip()
        if not html_content:
            raise ValueError("Odpowiedź od OpenAI nie zawiera przetworzonego artykułu.")
        return html_content
    except Exception as e:
        print(f"Błąd komunikacji z API: {e}")
        return None

# Tutaj zapisanie do pliku
def save_html_to_file(html_content):
    try:
        with open("artykul.html", "w", encoding="utf-8") as file:
            file.write(html_content)
        print("HTML zapisany do pliku artykul.html")
    except IOError as e:
        print(f"Błąd zapisu pliku: {e}")
    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}")

# Główna funkcja
def main():
    article_text = fetch_article(article_url)
    if article_text is None:
        print("Nie udało się pobrać artykułu. Program zostanie zakończony.")
        return  # Zakończ program, jeśli nie udało się pobrać artykułu

    html_content = process_article_with_openai(article_text)
    if html_content is None:
        print("Nie udało się przetworzyć artykułu. Program zostanie zakończony.")
        return  # Zakończ program, jeśli nie udało się przetworzyć artykułu

    save_html_to_file(html_content)

if __name__ == "__main__":
    main()
