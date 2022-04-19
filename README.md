# coding-exercise-b2b-swe

Hi!

In this coding excercise you'll be presented with a (very) basic "todo" application - which is poorly written, and has several bugs in it.

You're task is to refactor it so that it works as requested below, and the bugs are all fixed.
Don't forget to commit your work, you can do it while working on the exercise or at the end, whichever you prefer.

## Functional Requirements

- The app will allow the user to create new todos _(a "Todo" has "\_id", "name", "description", and "completed" fields)_
- When creating a "Todo", you must provide a "name" 

- The app will allow the user to get a todo by it's "_id"  
- The app will allow the user to get all todos  
- The app will allow the user to toggle the "completed" field


## Running the Server

1. Simply run `uvicorn main:app --reload`.  

2. You can test and play with your API by opening the GitPod's Preview URL (preview on the right, or copy the URL to a new tab)
