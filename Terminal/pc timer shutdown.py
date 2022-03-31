import subprocess
#v1
print("PC Shutdown timer v1")

seconds = input("Введите через сколько секунд выключить компьютер: ")

if input("Вы уверенны? (y/n)") == "n":
    print("Действие отменено")
else:
    subprocess.call(["shutdown", "/s", "/t", seconds])


#["shutdown", "/s", "/t", seconds]
#(["shutdown", "/l"])v1

