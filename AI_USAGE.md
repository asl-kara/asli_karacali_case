# AI Usage

## 1. Explain the terms *context*, *prompt*, *skill*, and *agent* as they relate to AI coding assistants.

**Context** can be the pages, files, and conversation history that you are working on, or an error in the terminal. Context is all the data that the AI looks at when generating a solution or response in other words, it is the background information the AI needs in order to produce a useful answer. In this project, context included the page object files, real HTML from insiderone.com, and field names extracted from the browser console.

**Prompt** is the command we give to the AI. We either assign it a task like "do this" or "do that" or we ask it a question. A well-written prompt is specific, includes relevant context, and states the expected output format.

**Skill** is a predefined, reusable, and saved instruction set invoked with a slash command (e.g. `/code-review`, `/write-test`); it is an ability we teach and add to the AI. When working on something similar in the future, instead of writing a detailed prompt from scratch, we simply call the skill reducing time and increasing the quality of the output. A skill defines how the AI should approach a specific type of task consistently, the same way every time.

**Agent** works differently from standard AI. In standard AI, the flow goes: ask a question → get an answer → ask again. With an agent, you simply give a task and the agent completes it on its own. An agent is an autonomous AI instance that can use tools such as reading files, running commands, and searching the web to complete multi-step tasks independently. Unlike a skill, which runs within the current conversation, an agent operates in isolation with its own context.

---

## 2. How did you validate the AI output? Which parts did you reject and why?

I reviewed all the generated tests using the `/code-review` skill, which allowed me to validate the AI output one more time. Beyond that, I applied an "ask permission before" approach throughout the project because I wanted to stay in control of every change and intervene immediately when needed. When I asked the AI to suggest UI test scenarios, I rejected the ones I did not find suitable for example, it suggested a language switcher scenario, but I rejected it because testing the demo page form made more sense for the case study. It also suggested navigating to the careers page via a direct link, but I rejected that as well since I wanted it to behave like a real user scrolling down and clicking the "We Are Hiring" button. My own background also allowed me to judge whether the outputs were reasonable and make informed decisions along the way.

---

## 3. Describe one point where the AI was weak in this task and how you solved it manually.

The AI could not access the form field structure of the demo page because the form is rendered dynamically by HubSpot's JavaScript, fetching the static HTML returned no field data at all. The AI guided me to manually solve this by running a one-line snippet in the browser console (`document.querySelectorAll('input, select, textarea').forEach(el => console.log(el.name, el.type, el.id, el.placeholder))`) which instantly returned all field names, types, and placeholders needed to write stable locators.

Another thing I noticed was that when the AI started implementing the UI test suggestion, it began directly from the demo form page instead of navigating from insiderone.com. I found this completely normal since I had not provided any test steps beforehand. I corrected it by re-explaining the test steps in the chat, so it is fair to say that I wrote the test step details manually.

---

## 4. In which situations would you prefer to write code manually instead of using AI?

In situations where despite a sufficient prompt I still cannot get the solution I need, or when I find the AI's suggested solutions inadequate, insufficient, or not aligned with proper standards, I investigate and analyze the problem myself firsthand and write the fix manually, then continue with AI afterwards.
