from bs4 import BeautifulSoup
 
with open("index.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    flag = str(soup.li.a)

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

print("Привет, вот тебе послание : " + text_to_bits(flag))
print("Если расшифруешь, то получишь пиздюлей! Введи свой ответ!")

settings = None
while True:
	settings = input("Введи свой ответ : ")
	if settings == flag:
		print("Ты победил!")
		break
	else:
		print("Ты ввёл не правильный ответ! Попробуй снова!")