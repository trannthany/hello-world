#Learn Tkinter in 20 minutes
#https://www.youtube.com/watch?v=_lSNIrR1nZU

from tkinter import * 

#key down function
def click():
    entered_text = text_entry.get() #this will collect the text from the next entry box
    output.delete(0.0, END)#0.0 means everthing before the first character
    try:
        definition = comp_dictionary[entered_text]
    except:
        definition = "Sorry there is no word like that please try again"
    output.insert(END, definition)

#exit function
def close_window():
    window.destroy()
    exit()
### main:
window = Tk()
window.title("My computer Science Glossary")
window.configure(background="black")
## My photo
photo1 = PhotoImage(file="working_with_xml/images.gif")
Label(window, image=photo1, bg = "black").grid(row=0, column=0, sticky=W)
#Create label
Label(window, text="Enter the word you would like a definition for: ", bg="black", fg="white", font="none 12 bold").grid(row=1, column=0, sticky=W)
#create a text entry box
text_entry = Entry(window, width=20, bg="white")
text_entry.grid(row=2, column=0, sticky=W)
#add a submit button
Button(window, text="SUBMIT", width=6, command=click).grid(row=3, column=0, sticky=W) #Command calls a function click()
#create another label
Label(window, text="\nDefinition:", bg="black", fg="white", font="none 12 bold").grid(row=4, column=0, sticky=W)
#create a text box
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)
#the dictionary
comp_dictionary = {
    'algorithm': 'Step by step instructions to complete a task', 'bug': 'Piece of code that causes a program to fail'
}
#exit label
Label(window, text="Click to exit:", bg="black", fg="white", font="none 12 bold").grid(row=6, column=0, sticky=W)
#exit button
Button(window, text="EXIT", width=14, command=close_window).grid(row=7, column=0, sticky=W) #Command calls a function click()
### run the main loop
window.mainloop()