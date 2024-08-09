from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)

messages = [
    "Это отличный пример использования библиотеки!",
    "Сегодня ужасная погода."
]

results = model.predict(messages, k=2)

for message, sentiment in zip(messages, results):
    print(message)
    for key, value in sentiment.items():
        print(f"    {key}: {value:.2f}")


def binary_search(arr_in, target):
    print(arr_in)
    print(target)