# The White Room
> An all-in-one Self Management Framework

Live Demo: http://46.101.90.169:5000/dashboard

<!--
Has features for calories and macro tracking, water tracking, kitchen inventory tracking (Product details including calories and macros per serving and per 100g and price and purchase location and price per item and servings per item and whether it is a tool or not also it generates a shopping list based on what you have in your inventory and saved products), recipe saving using saved products (not very good yet but it's not done), task management with name, description, and due dates as well as marking as complete or incomplete, self reward system with rewards, punishments, and log entries that don't affect coin balance, interval timers page that allow you to add multiple timers for different breaks, multi user chore management system with steps for the chores and RRULEs for repetition of the chores (work in progress, needs a GUI for generating the RRULEs behind the scene for you), settings page to change saved user data from initial setup page. 


# Mathmagician
Makes practice questions for you and tests you on them.
Maths is magic ∴ anyone can be a magician.
![mathmagician_demo](./demos/mathmagician_demo.png)
## Features  
- Matrix Multiplication questions and answers  
- Easy Quadratic Equation Differentiation questions and answers  
- Save stats (attempts, successes) and reset stats buttons  
- Separate stats for each exercise  
- Spellbook design, with index page for different maths  
- User gains Mana for completing questions and can Rank up to different levels  
- Flash notifications when completing questions or when ranking up which also shows current mana progress  
- Different "player models" for different ranks (apprentice.png, etc)  
### Possible Updates/TODO:  
- Daily streak bonus xp, logarithmic increase  
- Rank up animations  
- Gamified Experience with story telling and RPG elements  
- Show XP bar increasing animation when completing questions  
- Graph tracking progres over time  
- KaTeX rendering https://katex.org/  
- Hint levels up to the fully explained working out with the numbers used in the question  
- Speed arithmetic questions for rapid incantation-less casting  
- Flash mental arithmetic questions  
- Scratch pad area for notes and drawing  
- On screen calculators (different types depending on the questions/level/grade basic->scientific->graphing->idk all based on Casio recommended in England)  

- Think of more features and integrate with "Routes" to add a custom route learn maths from the foundations up to A-Level (high school) level)
- Check if mathmagician_base and base html templates can be merged in some way to not have two base templates or any missing features.
- Make real art for the different ranks and make rank ups based on quizzes to prove you learnt all pre requisites and can move up (also linked with route)
-->


# Features
## Week 14
Actually done:
- Update README <-- most important fr
- Add Mathmagician with updated theming

Goals:
- Improve Kitchen Inventory so that you can add an item to inventory without saving it's product details just add it once, you might've bought something just to try it once or got it as a gift from someone else.
- Add Kirinify with updated theming (and think about how twr would listen to music)


## Week 13 - Winter Theme:
What I actually managed to implement:
Meditation frontend incomplete with placeholder data in Python not actually added to sqlite3 database.  

Ideas:
### Meditation
A timer that supports playing custom audios at the start, end, and at **customisable** time intervals. Can also be used to make things like custom couch to 5k routines with custom voices such as TTS or anything else the user can imagine. However the namesake of the feature meditation fits the winter theme as some people suffer from seasonal affective depression and meditation can help with that, and so can the other features I am aiming to implement this week: weightlifting tracking and run tracking (using GPS data such as from a smartwatch).

### Weightlifting
Support for linear progression routines (like starting strength and routines inspired by it) as well as custom exercises and workout templates.

### Running
Support for GPS data from smart watches.
If possible, this is just the readme with my ideas, it will:
- Shows where you ran assuming GPS data can do that, 
- Your pace (km/h and min/km no option for miles), 
- Heart rate if that is included in the file format
- Step count
- Distance (km only)



## Week 12 - Framework Theme:
The White Room is
> An all-in-one Self Management Framework
and the following feature is a framework to plan and do **anything** such as learn languages or instruments or even the correct watch order for a series you are watching:
### Routes
A tree of tasks, habits, routines and resources that guide the user on a self guided mastery of certain skills. The user can make any custom tree but the primary use case is for people to progressively overload skills much in the same way they would with weights in a gym. For example a "mindfulness" tree might start with a habit of 1 minute a day of meditation and a resource such as a link to a YouTube video of why you should practice meditating. This can be expanded for anything such as musical instruments, languages or chess/go/shogi, anything the user can imagine to create a plan for themselves.

![routes_demo](./demos/routes_demo.gif)

What I actually managed to implement so far:
- Add route (name and description)
- Add nodes ("steps") to the routes (name, type(doesn't do anything yet), content)
- Display routes and their steps
- Delete steps
- Delete routes
As well as:
- Placeholder pages for meditation, runs and weightlifting





## Older
### Food Diary
![Food Diary Demo 1](./demos/food_diary_demo.gif)

### Kitchen Inventory
![Kitchen Inventory Demo](./demos/kitchen_inventory_demo.gif)

#### Food Diary Demo 2
Now that there is items in kitchen inventory you can add them to food diary
![Food Diary Demo 2](./demos/food_diary_demo2.gif)
Adding it to your inventory decrements the quantity added from the amount left in your inventory.

### Recipes
![Recipes Demo](./demos/recipes_demo.gif)
Work in progress, in the future it will be able to calculate an estimation for the calories and macros of the recipe based on the details saved about the ingredients in kitchen inventory. It will also be able to just add an instance of the recipe to your inventory and from there to your food diary with those calculated calories and macros, and if you made multiple servings then you can easily add it to food diary once you eat the other serving in 3 clicks. 

### Tasks
![Tasks Demo](./demos/tasks_demo.gif)

### Self Reward System
![Self Reward System Demo](./demos/rewards_demo.gif)
  
Need to update logic to change "-5 coins spent" to "added 5 coins".
Not shown: Reward images

### Interval Timers
Not fully working, requires updates

### Chores
![chores demo](./demos/chores_demo.png)

### Settings
Change data from initial setup page
![settings demo](demos/settings_demo.png)
<!--
## Planned
-->

## Self-Hosting Guide
install python if you don't have it  

```sh
git clone https://github.com/shania-codes/thewhiteroom  
cd thewhiteroom  

Windows: python -m venv venv  
macOS/Linux: python3 -m venv venv  


Windows: 
venv\Scripts\activate  
macOS/Linux:
source venv/bin/activate  


pip install flask python-dateutil  

flask run  
```
Visit: http://YourServerIP:5000/  
