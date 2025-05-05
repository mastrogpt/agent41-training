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
# `Check Your Server`

![bg 100%](1-vibe/login-and-fixes.png)

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

 ###### Demo of tool creation

1. Clean the chat
2. Manual: Create a tool, a Demo Tool
3. Restore checkpoint
4. Ask: create a demo tool
6. Agent: create a demo tool
5. Test it
6. Deploy it

![bg right:60% 90%](1-vibe/create-a-demo.png)
---

- Demo Manual: create demo tool
  - Remove past chats
  - Create a demo tool in Manual mode
     -  The AI does not follow our rules
  - Restore Checkpoint
- Demo Ask: create demo tool
  - AI finds our rules
  - Note it needs the context to process

---
# Demo Agentic: create a demo tool
  - AI finds our rules
  - Agent **EXECUTES** our rules
  - Further decisions depends on the results
  - AI can make mistakes:
     - Not applying all the rules
     - Taking decions on unspecified behaviour
 


----

#### Demo Ollama:
  - Create a demo chat
  - Follows our rules
    - ollama.mdc
  - Makes a mistake on the API
    - Our rule does not specify which API to use
    - We need a manual fix

![bg left:50% 100%](1-vibe/build-an-ai-with-vibe.png)



