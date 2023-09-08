def main():
    convert()

def convert():
    txt = input("Write a string whith a emoticon. ")
    new_txt = txt.replace(":)" , "🙂").replace(":(" , "🙁")
    print(new_txt)
main()