# 310 Project: Chatbot App

## Assigment 3 note

Project-Report.pdf is only up-to-date as of Assignment 2. For the required documentation, see either the Word doc you came from, or further down in this Readme, under the "Assignment 3 Project Report" section especially.

## Team 31 Members:

Mohammad Al-surkhi

Jordan Colledge

Gabriel McLachlan

Jordan Ribbink

Nathan Wright

## Project Repo:

https://github.com/cosc310-project/chatbot-app/tree/dev

## Project Description and Purpose

Description copied and pasted from the Project Plan:
The project consists of a chatbot built in Electron; the chatbot comes with a generic visual interface to ensure simplicity of use and understanding. (Apparently this is extra credit for the next assignment, which we weren’t aware of until it had been implemented.) The chatbot takes on the role of a doctor, who can be asked questions about different symptoms and describe the likely illness and remedy. Thus, the user takes on the role of a patient.

The purpose of the app is to make a simple diagnostic tool, so that the user can diagnose their possible illnesses without having to leave their home. A doctor will necessarily be a better diagnostic tool than this app, but it's meant to be functional just the same.

## Installation and Usage

### Requirements

- Node JS - https://nodejs.org/en/
- NVM (optional) - https://github.com/nvm-sh/nvm
- Python 3 - https://www.python.org/downloads/
- Pyenv (optional) - https://github.com/pyenv/pyenv
- Pyenv-virtualenv (optional) - https://github.com/pyenv/pyenv-virtualenv

Open terminal in the root of the project and run this command:

1.  Install NPM dependencies

    ```bash
    npm install
    ```

2.  Install Python dependencies

    - OPTIONAL. Install [Pyenv](https://github.com/pyenv/pyenv) & [Pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) to manage Python environment. Follow instructions provided within documentation

      Create a new virutalenv in Python 3.8.10 and activate it

      ```bash
      pyenv virtualenv 3.8.10 ${YOUR_VIRTUALENV_NAME}
      pyenv activate ${YOUR_VIRTUALENV_NAME}
      ```

    - Install requirements via pip by running the following command from the root folder of the project

      ```bash
      pip install -r requirements.txt
      ```

3.  Run this command to train the bot's neural network:

    ```bash
    npm run train
    ```

    If this gives an error, run this instead:

    ```bash
    python util/train.py
    ```

    This may take a bit of time, but after it's run once, it doesn't need to be run again.

4.  Launch development server using the following bash command in root of project

    ```bash
    npm run start
    ```

    The chatbot should launch.

## Simplified Project Structure

NEW TO A3:
./documentation
./src/agent
./util

Some files for A3 are not included for this list, as they're simply used by utilities such as TensorFlow or NLTK, or may be obsolete.

. &nbsp;<br />
├── ...&nbsp;<br />
├── config &nbsp;<br />
│ &nbsp; └── dataset.json &nbsp; -> Stores our dataset for NLP<br />
├── documentation &nbsp;<br />
│ &nbsp; ├── 30-Turn Convo.pdf &nbsp; -> Stores images of the thirty-turn conversation as stipulated in requirements. <br />
│ &nbsp; ├── DFD's.pdf &nbsp; -> Stores the Data Flow Diagrams and descriptions of them. <br />
│ &nbsp; └── Unit Test Descriptions.pdf &nbsp; -> Stores descriptions of the unit tests used.
├── Project Report.docx &nbsp; -> Our project report document<br />
├── src &nbsp;<br />
│ &nbsp; ├── agent &nbsp;<br />
│ &nbsp; │ &nbsp; ├── plugins &nbsp; <br />
│ &nbsp; │ &nbsp; ├── tests &nbsp;<br />
│ &nbsp; │ &nbsp; │ &nbsp; └── agent_test.py &nbsp; -> Unit tests as used by Pytest.
│ &nbsp; │ &nbsp; └── agent.py &nbsp; -> The Python agent. Essentially used to read a query, manipulate it, and return the results.<br />
│ &nbsp; │ &nbsp; └── chat.py &nbsp; -> The Python agent. Essentially used to read a query, manipulate it, and return the results.<br />
│ &nbsp; ├── main &nbsp;<br />
│ &nbsp; │ &nbsp; ├── nlp-service.ts &nbsp;&nbsp;&nbsp;&nbsp;<- &nbsp;Interfaces with Node NLP module and trains from dataset &nbsp;<br />
│ &nbsp; │ &nbsp; ├── main.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Electron entry point, also includes IPC module for communicating frontend<br />
│ &nbsp; ├── renderer &nbsp;<br />
│ &nbsp; │ &nbsp; ├── App.vue &nbsp;&nbsp;&nbsp;<- &nbsp;Vue entry point <br />
│ &nbsp; │ &nbsp; ├── components &nbsp;&nbsp;&nbsp;<- &nbsp;Component structure following atomic design principles<br />
│ &nbsp; │ &nbsp; │ &nbsp; ├── atoms &nbsp;&nbsp;&nbsp;<- &nbsp;Smallest component unit in atomic design<br />
│ &nbsp; │ &nbsp; │ &nbsp; │ &nbsp; ├── ChatMessage.vue &nbsp;&nbsp;&nbsp;<- &nbsp;Vue component for chat messages<br />
│ &nbsp; │ &nbsp; │ &nbsp; │ &nbsp; └── TypingMessage.vue &nbsp;&nbsp;&nbsp;<- &nbsp;Vue component for "user is typing..."<br />
│ &nbsp; │ &nbsp; │ &nbsp; ├── molecules &nbsp;&nbsp;&nbsp;<- &nbsp;Medium sized component unit<br />
│ &nbsp; │ &nbsp; │ &nbsp; │ &nbsp; ├── ChatBar.vue &nbsp;&nbsp;&nbsp;<- &nbsp;Vue component for chat bar<br />
│ &nbsp; │ &nbsp; │ &nbsp; │ &nbsp; ├── ChatBox.vue &nbsp;&nbsp;&nbsp;<- &nbsp;Vue component for chat box (where messages go)<br />
│ &nbsp; │ &nbsp; │ &nbsp; │ &nbsp; └── ChatHeader.vue &nbsp;&nbsp;&nbsp;<- &nbsp;Chat header component (recipient picture+name)<br />
│ &nbsp; │ &nbsp; │ &nbsp; └── organisms &nbsp;&nbsp;&nbsp;<- &nbsp;Largest component unit (full functioning features)<br />
│ &nbsp; │ &nbsp; │ &nbsp; &nbsp; &nbsp; └── ChatContainer.vue &nbsp;&nbsp;&nbsp;<- &nbsp;Chat container component (full chat feature)<br />
│ &nbsp; │ &nbsp; ├── index.ejs &nbsp;&nbsp;&nbsp;<- &nbsp;Main HTML template where Vue is injected<br />
│ &nbsp; │ &nbsp; ├── index.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Webpack entry point<br />
│ &nbsp; │ &nbsp; ├── models &nbsp;&nbsp;&nbsp;<- &nbsp;Stores reusable object models (i.e. classes/data structures)<br />
│ &nbsp; │ &nbsp; │ &nbsp; ├── message.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Class to identify a sent message<br />
│ &nbsp; │ &nbsp; │ &nbsp; ├── service.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Abstract class representing stateful services injected into Vue<br />
│ &nbsp; │ &nbsp; │ &nbsp; └── user.ts &nbsp;&nbsp;<-Class to identify users in chat<br />
│ &nbsp; │ &nbsp; ├── services &nbsp;<br />
│ &nbsp; │ &nbsp; │ &nbsp; ├── chat-service.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Service to manipulate chat state and provide responses from AI<br />
│ &nbsp; │ &nbsp; │ &nbsp; └── services.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Services initializer plugin which is installed into Vue (inits all services)<br />
│ &nbsp; │ &nbsp; ├── store &nbsp;&nbsp;&nbsp;<- &nbsp;Configuration for Vuex store (state management) <br />
│ &nbsp; │ &nbsp; │ &nbsp; ├── createStore.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Initializer for store (object factory)<br />
│ &nbsp; │ &nbsp; │ &nbsp; └── modules &nbsp;&nbsp;&nbsp;<- &nbsp;Stores all modules involved in store<br />
│ &nbsp; │ &nbsp; │ &nbsp; &nbsp; &nbsp; └── chat.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Chat module for store (manages chat state for chat service)<br />
│ &nbsp; │ &nbsp; └── util &nbsp;&nbsp;&nbsp;<- &nbsp;Misc utilities<br />
│ &nbsp; │ &nbsp; &nbsp; &nbsp; ├── createApp.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Factory to create Vue app with desired configuration<br />
│ &nbsp; │ &nbsp; &nbsp; &nbsp; └── inject-context.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Helper function for injecting key into Vue/components (for DI)<br />
│ &nbsp; └── ... &nbsp;<br />
├── util &nbsp; <br />
│ &nbsp; ├── train.py &nbsp; -> A script used to train TensorFlow. <br />
│ &nbsp; └── trainer.py &nbsp; -> Utility for configuration used in train.py. <br />

**NOTE:** Not all files are included. Configuration files and similar files of low relevance (added clutter) are removed.

**NOTE:** Summary of Python files is very simplified.

## Vue Components (pseudo classes)

### ChatMessage.vue &lt;ChatMessage&gt;

Props (arguments):

- message -> Message (represents message object containing content/date/sender)

### TypingMessage.vue &lt;TypingMessage&gt;

Props (arguments):

- user -> User (represents user typing)

### ChatBar.vue &lt;ChatBar&gt;

Props (arguments): N/A

### ChatBox.vue &lt;ChatBox&gt;

Props (arguments): N/A

### ChatHeader.vue &lt;ChatHeader&gt;

Props (arguments):

- name -> String (represents name of user in header)

### ChatContainer.vue &lt;ChatContainer&gt;

Props (arguments): N/A

**NOTE:** Prop typings are denoted by [propName] -> [type]. They correspond with native TypeScript types OR typings found in our src/models folder. HTML selectors (class names) are indicated by "[file].vue &lt;[selector]&gt;"

**NOTE**: While vue components are phyiscally represented as classes in code/memory and generally function like so, I don't necessarily know if it is the correct nomenclature. However , based upon the requirements, we can call them this.

Vue technically abides by the MVC (Model-View-Controller structure) where the View is connected two-way data bindding to the Controller (i.e. JS in Vue component). Models are represented as classes in our "src/models" folder

## Models

├── models &nbsp;&nbsp;&nbsp;<- &nbsp;Stores reusable object models (i.e. classes/data structures)<br />
│ &nbsp; ├── message.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Class to identify a sent message<br />
│ &nbsp; ├── service.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Abstract class representing stateful services injected into Vue<br />
│ &nbsp; └── user.ts &nbsp;&nbsp;<-Class to identify users in chat<br />

### Message.ts (Message)

Class members:

- date: Date (message date sent)
- sender: User (message sender object)
- message: string (message body)

### Service.ts (_abstract_&nbsp; Service)

Class members:

- protected app: Vue.App (pointer to Vue App instance)

### User.ts (User)

Class members:

- name: string (represents user name)
- typing: boolean (represents whether user is typing, default=false)
- photo?: string (represents user photo URL, default=undefined)

# Assignment 3 Project Report

## 30-Turn Feasible Dialogue:

The PDF was consistently corrupted on upload. It can be found under ./documentation/30-Turn_Convo in six parts.

## Features Added:

### TensorFlow:

TensorFlow wasn't listed in the toolkits, but we've included it because we believe that it will more than count as one of the "other toolkits" category named.
It essentially works as a toolkit to implement neural networks into the program.
TensorFlow has improved the AI's ability to recognize sentences, and has been heavily integrated into synonym recognition.

We have no example conversation for TensorFlow, since it's used in training the tool that recognizes the user's input. As such, the best example for it is the 30-turn scenario.

### Spell Checking (Toolkit: Pyspellchecker):

Spell checking isn't counted as a toolkit, but it's an important addition to the bot so we put it here to demonstrate its integration.
The addition of spell check means that if a user doesn't know how to spell a symptom or diagnosis, then as long as it's close to the actual word, the bot will understand

Here's a modified bot output that demonstrates the functionality of spell checking.
![Spelling](/assets/examples/Spell.PNG 'Spell Checking Example')

(The image can be found at ./assets/examples/Spell.PNG if there are any issues.)

### Synonym Recognition - NLTK:

This improves the bot through enabling the user to input synonyms for words, rather than the exact words that the bot has initially listed in its software.
This broadens the bot's recognition of user inputs.

![Synonym Recognition](/assets/examples/Syn.PNG 'Synonym Example')

(The image can be found at ./assets/examples/Syn.PNG if there are any issues.)

### POS Tagging - NLTK:

This isn't used directly in conversation by the bot, but it is used to increase the quality of other features, like synonym recognition.
Essentially, this ensures that synonyms are only considered when they are of the same part of speech.
For example: if "input" is used as a noun in a sentence, synonyms of "input" as a verb will not be included.

Here's a modified bot output that demonstrates the functionality of POS tagging.
![POS](/assets/examples/POS.PNG 'POS Tagging Example')

(The image can be found at ./assets/examples/POS.PNG if there are any issues.)

### Sentiment Analysis - NLTK:

This is the first feature that is directly viewable by the user. When the user inputs a sentence that is particularly negative -- so negative that a human themself could recognize that something is wrong -- the bot will pick up on this and show some sympathy.
This helps the conversation flow a bit more naturally and in a realistic deployment could put a distressed user more at ease, both major improvements

![SentimentAnalysis](/assets/examples/SA.PNG 'Sentiment Example')

(The image can be found at ./assets/examples/SA.PNG if there are any issues.)

### Named Entity Recognition - NLTK:

This is another feature that is viewable by the user. If the user inputs a proper greeting or information about someone else, the bot recognizes this and appends its response accordingly
This helps to make the conversation a bit more personal, and helps it sound less like a programmed entity and more like speaking to a real person

![NE1](/assets/examples/NE.PNG 'Named Entity Recognition Example')

(The image can be found at ./assets/examples/NE.PNG if there are any issues.)

## Data Flow Diagrams

The images and their descriptions can be found at:
chatbot-app\documentation\DFD's.pdf

## Limitations

The bot occasionally fails when the input contains incorrect small words. This is caused by spellcheck, as the number of short words that they could possibly correct to causes the bot not to understand the input properly.

Example:

![Smal](/assets/examples/Short.png 'Small input errors')

(The image can be found at ./assets/examples/Short.PNG if there are any issues.)

The bot also fails when inputs are especially long. This can drag down the bot's performance, as well as raising the likelihood of giving an inaccurate response by a significant amount.

Example:

![large](/assets/examples/Long.png 'Large input errors')

(The image can be found at ./assets/examples/Long.PNG if there are any issues.)

# Github Graph:

This is the entire Github tree, including all branches that were used for different features

![tre5](/assets/examples/Tree5.PNG 'Trees')
![tre4](/assets/examples/Tree4.PNG 'Trees')
![tre3](/assets/examples/Tree3.PNG 'Trees')
![tre2](/assets/examples/tree2.PNG 'Trees')
![tre1](/assets/examples/Tree1.PNG 'Trees')

(The images can be found at ./assets/examples/tree.PNG if there are any issues. Alternatively, in the terminal use "gitk --all")

## Possible API Elements

With a bot as complex as ours, there are a number of different functionalities that could be exposed or used to create our own API.

1. Extract the synonyms function (found in util/trainer.py and src/agents/agent.py) to find the synonyms for a specific word, occupying a specific part of speech.
2. Extract spellcheck.py to have a simple spellcheck function using Python's spellcheck library.
3. Extract get_synonymous_sentences (found in src/agents.py) to get sentences that are "one synonym away" from the input sentence.
4. Extract config/dataset.json for a basic map from symptoms to diagnoses to be used in a similar doctor-like or other healthcare-oriented program.
5. Extract the functions to train the neural network (from util/trainer.py) based on all the synonyms for a given word.

# Assignment 3 - Nathan Wright's Modifications:

All desribed modifications in this document from this point forward were developped and implemented by Nathan Wright for the individual assignment.

### Wikipedia Searching - Wikipedia API:

This new feature makes use of the wikipedia API. The user can ask the bot to search for and summarize a wikipedia page using the keywords:

```bash
...search for "query"
...look up "query"
...wikipedia for "query"
```

For the bot to work best the query should be the last part of the sentence. This feature allows the user to look up medical information
without the need for scrolling through a wikipedia page themselves. There's also a check to see if the query is health related or not. If the bot thinks the query is not health related it will ask for user confirmation. Unfortunately, wikipedia does not tag their meaning the bot must rely on page categories. Thus this aspect of the wikipedia search feature can be unreliable.

Here's a short example of the feature.

![wikiSearch](/assets/examples/SEARCH.PNG 'Wikipedia Search Example')

(The image can be found at ./assets/examples/SEARCH.PNG if there are any issues.)

### Directions to a location - Google Maps API (geolocation, geocoding, places, and directions):

This new feature makes use of Google's geolocation, and places API. This feature allows the user to ask for a direction to a specific location within 10km of their specified location. The bot will provide the user with directions to the closest location specified, much like a GPS. This allows the user to ask for directions to their closest clinic, hospital, or other medical facility should they need it. This feature isn't limited to giving directions to just hospitals either.

The user can ask the bot for directions using the keywords:

```bash
...directions to "location name/description"
...directions for "location name/description"
...where is "location name/description"
...location of "location name/description"
...the nearest "location name/description"
...the closest "location name/description"
```

Afterwards the bot will ask the user for their address. Once the address is entered the bot will provide the user directions to their (most likely) desired location. For simplicity's sake the bot assumes the user will be driving.

Here's a short example of the feature.

![wikiSearch](/assets/examples/DIRECT.PNG 'Google Maps Directions Example')

(The image can be found at ./assets/examples/DIRECT.PNG if there are any issues.)

### The Functions:

In agent.py two new functions were added:

```bash
wikiSearch(query, base)
direction(query, base)
```

Both wikiSearch and direction take in a query and a base parameter. The query parameter is the user's input while the base is the current response the bot believes is appropriate. wikiSearch and direction check to see if any modification is required to the current bots calculated output. If there is editing needed, wikiSearch and direction will modify the bots calculated response. wikiSearch will add any information extracted from wikipedia that the user has requested to search. directions handles calculating the directions the bot should reply with and handling address input as well as confirmation.
