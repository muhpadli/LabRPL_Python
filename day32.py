import random

print(78*"=","\n",29*" ","SELAMAT DATANG",
      "\n",23*" ","DI GAME GUNTING BATU KERTAS",
      "\n"+"="*78)
main = input("\nApakah anda sudah siap, main game ini (y/t) :").lower()

if(main == "y"):
    anda = input("\nMasukkan pilihan anda (gunting/batu/kertas) : ").lower()
    print(f"Pilihan anda adalah {anda}")
    bot = random.choice(["gunting","batu","kertas"])
    print(f"Pilihan bot komputer adalah {bot}")

    if(anda == bot ):
        print("\nAnda dan bot dinyatakan seri")
    elif(anda == "kertas" and bot == "batu")or(anda == "batu" and bot == "gunting") or (anda == "gunting" and bot == "batu"):
        print("\nAnda dinyatakan menang")
    else:
        print("\nAnda dinyatakan kalah")
else:
    print("silakan coba nanti yah!")

print(78*"=","\n",32*" ", "TERIMAKASIH \n"," "*15,
      "TELAH MAMPIR DI GAME GUNTING BATU KERTAS INI!",
      "\n"+"="*78)