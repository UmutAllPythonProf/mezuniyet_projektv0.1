# #Gerekli Kütüphane(ler)
# import openai

# #API Anahtarı
# openai.api_key = "sk-**************************************"#Şu An Güncel

# while True:
#     soru = input("Sizin Sorunuz (Çıkış Yapmak İstiyorsanız \"q\" Tıklatın) : ")

#     if soru.lower() == "q":
#         print("Pekala Çıkış Yapılıyor, Görüşmek Üzere")
#         break

#     else:
#         algoritma = openai.Completion.create(
#             engine = "gpt-3.5-turbo-0125",
#             prompt = soru,
#             max_tokens = 16385,
#             n=1,
#             stop=None,
#         )

#         bot_cevabi = algoritma.choices[0].text

#         print("{} \n\nBunun Dışında Yardım Edebileceğim Bir Konu Varsa Yardımcı Olmaktan Zevk Duyarım...\n\n")

import tkinter as tk
from tkinter import scrolledtext, END
import openai
from threading import Thread

# OpenAI API Key'inizi girin
openai.api_key = "YOUR_API_KEY"

# Sohbet geçmişini saklamak için bir değişken
chat_history = ""

def get_response(message):
  """
  OpenAI'ya bir mesaj gönderir ve yanıtı döndürür.
  """
  global chat_history
  
  # Sohbet geçmişini ve yeni mesajı birleştirin
  prompt = chat_history + "\n" + message

  # OpenAI'ya bir istek gönderin
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=100,
  )

  # Yanıtı ayıklayın
  answer = response["choices"][0]["text"]

  # Sohbet geçmişini güncelleyin
  chat_history += "\nAI: " + answer

  return answer

def update_chat(message):
  """
  Sohbet penceresini günceller.
  """
  chat_box.insert(END, message + "\n")

def on_send():
  """
  "Gönder" düğmesine tıklandığında tetiklenir.
  """
  msgbx = "1.0", "end-1c"
  start_index = msgbx.get()  # Eğer msgbx bir Entry veya bir değer döndüren başka bir nesne ise
  message = input_box.get(start_index, "end-1c")

  input_box.delete("1.0", "end")

  # Kullanıcı mesajını sohbet penceresine ekleyin
  update_chat("Ben: " + message)

  # Arka planda bir iş parçacığı kullanarak OpenAI'ya bir istek gönderin
  thread = Thread(target=get_response, args=[message])
  thread.start()

def main():
  """
  Chatbot penceresini oluşturur ve çalıştırır.
  """
  global chat_box, input_box

  # Pencereyi oluşturun
  root = tk.Tk()
  root.title("Chatbot")

  # Sohbet metin kutusunu oluşturun
  chat_box = scrolledtext.ScrolledText(root, width=50, height=20)
  chat_box.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

  # Giriş metin kutusunu oluşturun
  input_box = tk.Entry(root, width=50)
  input_box.grid(row=1, column=0, padx=10, pady=5)

  # Gönder düğmesini oluşturun
  send_button = tk.Button(root, text="Gönder", command=on_send)
  send_button.grid(row=1, column=1, padx=5, pady=5)

  # Pencereyi çalıştırın
  root.mainloop()

if __name__ == "__main__":
  main()

