import requests
from PIL import Image, ImageDraw, ImageFont
from transformers import pipeline

# Шаг 1: Получение новостей
def fetch_news(topic="school mathematics"):
    url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey=YOUR_API_KEY"
    response = requests.get(url)
    news = response.json()
    return news["articles"]

# Шаг 2: Фильтрация новостей
def filter_news(news):
    relevant_news = []
    for article in news:
        if "mathematics" in article["title"].lower() or "math" in article["title"].lower():
            relevant_news.append(article)
    return relevant_news

# Шаг 3: Генерация текста для блога
def generate_blog_text(news):
    pipe = pipeline("text-generation")
    prompt = ""
    for article in news:
        prompt += f"{article['title']}\n{article['description']}\n\n"
    generated_text = pipe(prompt, max_length=1024, num_return_sequences=1)[0]['generated_text']
    return generated_text

# Шаг 4: Генерация текста для изображения
def generate_image_text(blog_text):
    return "Увлекательная математика для школьников!"

# Шаг 5: Создание изображения
def create_image(text):
    img = Image.new('RGB', (800, 400), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 32)
    draw.text((10, 10), text, font=font, fill=(0, 0, 0))
    img.save('output_image.png')

# Шаг 6: Сохранение результатов
def save_results(blog_text, image_text):
    with open('blog_text.txt', 'w') as file:
        file.write(blog_text)
    create_image(image_text)

# Основная функция
def main():
    news = fetch_news()
    filtered_news = filter_news(news)
    blog_text = generate_blog_text(filtered_news)
    image_text = generate_image_text(blog_text)
    save_results(blog_text, image_text)

# Запуск программы
if __name__ == "__main__":
    main()