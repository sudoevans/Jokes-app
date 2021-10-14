import requests
from tkinter import *
from threading import Thread


api='https://geek-jokes.sameerkumar.website/api'

jokes=[]
joke_number=0


def preload_jokes():
    print('**Loading Jokes**')
    for i in range(10):
        noris_joke=requests.get(api).json()
        jokes.append(noris_joke)
    print(jokes)
    


preload_jokes()
print('Jokes Done Loading!')



def get_joke():
    btn.configure(text="Loading...")
    global joke_label
    global jokes
    global joke_number

    joke_label.configure(text=jokes[joke_number])
    joke_number=joke_number+1
    print(joke_number)

    if joke_number>5:
        thread=Thread(target=preload_jokes)
        thread.start()

    # if  [joke_number]==jokes[-3]:
    #     thread=Thread(target=preload_jokes)
    #     thread.start()


root=Tk()
root.configure(width=900, height=300)
root.title("Dummy Old Jokes")

# root.resizable(0,0)
joke_label=Label(text="Click the Button to get a joke!",font=("lucida"), width=50, height=10)

joke_label.grid(row=0, column=1,padx=20, pady=20)

btn=Button(text="Fetch Joke",command=get_joke,
    activebackground='#fa8107',fg='#ffffff',bg='#54300b', font=('lucida', 15,'bold'),width=40,height=4)
btn.grid(row=1, column=1, columnspan=2,padx=15, pady=20
               
)
root.mainloop()

