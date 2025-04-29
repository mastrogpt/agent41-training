---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.jpg')
color: 266089
html: true

---
![bg left:50% 90%](assets/logo-nuvolaris-agent41.png)

#### Agent41 Course
<center>
<img width="90%"src="assets/openserverless-logo.png">
</center>

### **Lesson 1**
####  Vibe Coding with Cursor

<center>
<img width="85%"src="assets/image-agent41.png">
</center>


---

<p>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
</p>

# <!--fit-->`Install Cursor: https://cursor.com`

![bg 100%](1-vibe/install-cursor.png)

---

## Setup

![bg left:50% 90%](1-vibe/launch-starter.png)


1. Clone repo
1. Clone from GitHub
1. Allow GitHub access
1. Copy Device Code
1. Paste Device Code
1. Authorize VSCode
1. Clone
`mastrogpt/agent41-starter`
1. Open Devcontainer

---
1. Open AI Chat 
2. Create a New Chat
3. Select the context
   - File & Folders
   - Code
   - More...
4. Select the Mode
   - Agent
   - Ask 
   - Manual

![bg right:50% 80%](1-vibe/overview.png)

---

## Modes
![bg right:50% 60%](1-vibe/modes.png)


- **Agent**: fully  automated
   - Find the context
   - Propose solution
   - Implements them
- **Ask**
   - As agent but do not act
- **Manual**
   - You have to provide the context


---
## Contexts
- Files and Folders
- Code (snipptets)
- Docs
- Past git revisions
- Past chats
- Terminal commands
- Errors
- Web
- **Cursor Rules** 


![bg right:50% 80%](1-vibe/contexts.png)

---

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

## `Cursor Rules`

![bg](1-vibe/rules.png)

---

![bg right:50% 50%](1-vibe/create-tool.png)

### Create Weather Tool

- `create a tool named weather`
  - **use a rule**
- `access to a service to get the wether in a location`
  - **asks a a question**
- `use openweather`

  - **my answer**


---

#### Implement Weather Tool

![bg right:50% 70%](1-vibe/weather.png)

- `read the api key`

- `make a request to openwhethermap and retrieve the wheather for a given location`

- `add to the index`

- test and deploy

--- 

# Use Ollama to Parse Time


- `write a function ask_ollama to ask using model llama3.1:8b  and return its anwser`

  - it should select or use the `ollama` rule
   

- `write parse_time_and_location invoking ask_ollama assuming it is a request for a wheather prediction at a given location and optionally a time. Return the answer as a tuple with 3 values: the location of the request, the time of the request as a number of in hours in advance from now,  and the number of days in advance. Default to 0 for both if not specified`

--- 
#  Parse Time fixes and tests

- LLM does not know the current day and time we have to specify it
  - `provide the current time and date to the prompt`

- Sometimes the output is not a json object but is is embedded:
  - `check the respnse and extract a json object if it is embedded in the answer`

- We need to add tests:
  - `write tests to check form London, London tomorrow moning, Paris next Week and Moscow in the night`

---

## Close the loop fixing the `weather` function

`Change the weather function to use the parse_and_time location and use always a forecast. In the result answer specify the date and time for the forecast in the local time.`

`write tests for London, London tomorrow, Paris next week`
