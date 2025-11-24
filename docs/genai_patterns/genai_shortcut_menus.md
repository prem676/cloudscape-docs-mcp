---
title: "Shortcut menus - Cloudscape Design System"
source: "https://cloudscape.design/patterns/genai/shortctut-menus/"
created: 2025-10-13
description: "Use shortcut menus to help users modify behavior, add context, and execute quick actions."
---
#### Invoke a shortcut menu

Shortcut menus can be invoked through typing special characters or selecting icon buttons.Providing shortcut menu access through both keystrokes and buttons supports both discoverability for new users through visible buttons and efficiency for power users through keystrokes. For example, the prompt input secondary actions slot can display a group of buttons that, when clicked, invoke a menu. Additionally, typing special characters like *@* or */* in the text area can trigger menus.

#### Enhance natural language prompts

Users interact with generative AI tools like code assistants or content generators through natural language prompts. Shortcut menus can enhance these prompts by allowing users to complete actions like specifying a mode and inserting references to provide additional context while maintaining the flow of their text input. For example, a developer might activate */code* mode when asking for code analysis, or a content creator might reference specific documentation while requesting a text summary.

#### Actions

Actions help users modify system behavior or execute common tasks. By typing */* or using an icon button, users can access different types of actions like setting modes ( which sets the framework for how the system should process and respond to user input) or using quick commands (like clearing context or getting help). For example, a user might set a mode to specify how their prompts should be interpreted, or execute a quick action to start a new conversation.

#### References

References are interactive shortcuts that let users add context to their prompts. Users can select files, code snippets, and other data sources without manually copying file paths. This functionality creates a more efficient way to enhance prompts without disrupting the natural flow of conversation or requiring technical knowledge of file systems and paths.

#### Contextual relevance

Shortcuts open specific menu types. This helps users by showing only relevant options like modes when they need to change behavior, or references when they need to add context. For example, typing */* opens a menu of modes or quick actions, while typing *@* opens a menu for items that can be referenced within a prompt.

## Common symbols

| **Symbol** | **Use** | **Example** |
| --- | --- | --- |
| / | Performing quick actions | In a prompt input, a user enacts a quick action through a forward slash like /clear to remove all references, files and context currently in the prompt input. |
| @ | References for inserting files, usernames, or other resources | In a prompt input, a user requests a cost analysis and provides the system with additional context by referencing a.csv file in their prompt via a shortcut menu. |

Quick actions provide users with access to helpful commands. They reduce the need to manually type out common commands like *help* or *clear*. Quick actions appear alongside modes in the shortcut menu when using the */* command or button, making them easy to discover and execute. Common quick actions include clearing the conversation or prompt input, accessing help documentation, or starting a new chat.

<video xmlns="http://www.w3.org/1999/xhtml" width="100%" controls="" title="[mute]

A video demonstration showing how to access system help using a shortcut command. The user types '/help' in the prompt, which automatically opens a shortcut menu with autosuggest options. As they type, the menu filters and suggests relevant help topics."><source src="/__images/yvlrib0vb3vb/6RV2jWtwGo6tUUczNzNAH3/ff03f34101eb1aa8896ca2d1ef77202b/quick-actions.mp4" type="video/mp4"></video>

Setting a mode tells the system how to interpret user input entered in a [prompt input](https://cloudscape.design/components/prompt-input/). For example, selecting */dev* for technical, development-related prompts. Users can set a mode with the prompt input with keystrokes or icon buttons. Typing / at the beginning of a prompt will invoke a shortcut menu for setting modes. Alternatively a user can set a mode at any time through an icon button.

<video xmlns="http://www.w3.org/1999/xhtml" width="100%" controls="" title="

A video demonstration showing how to set a mode in a prompt input. When the user clicks to open a shortcut menu and selects a mode, an inline token automatically appears in the text area to indicate the selected mode is active."><source src="/__images/yvlrib0vb3vb/4VXo5J6MJTQGc5wwBvBFwh/e2a17072ba43323e3fad8093ae17a145/set-a-mode.mp4" type="video/mp4"></video>

Users can add additional context to a prompt by inserting references to relevant data sources that the system is connected to, either by using a keystroke like @ or by clicking an icon button.

<video xmlns="http://www.w3.org/1999/xhtml" width="100%" controls="" title="[mute]

A video demonstration showing how to add a reference using a shortcut menu. The user opens a menu, selects a reference from the available options, and an inline token representing the selected reference is automatically inserted into the prompt text."><source src="/__images/yvlrib0vb3vb/4lTzfOWJBH0FIoa0eVOnkG/d9eaad24c3952bfecfa343f4d389e41c/add-context.mp4" type="video/mp4"></video>

Users can highlight the placeholder variable in their inserted prompt template and use *@* to replace them with actual references. For example, when a template contains <dataset>, users can swap it with a specific data reference through the reference menu, customizing the template while maintaining the inserted template’s structure.

<video xmlns="http://www.w3.org/1999/xhtml" width="100%" controls="" title="[mute]

A video demonstration showing how to use a prompt template and replace variables. The user enters a template containing placeholder variables, then replaces each text variable by typing '@' to open a menu, selecting appropriate references from the suggestions, and inserting them as inline tokens."><source src="/__images/yvlrib0vb3vb/60UwkwsDBGfP9TsH7DeWUh/3d485ce5215d21533b5069e3e745cdaf/replacing-placeholders.mp4" type="video/mp4"></video>

## General guidelines

### Do

- Use [groups](https://cloudscape.design/components/autosuggest/?tabId=playground&example=with-suggestions-groups) and descriptive labels to separate different kinds of menu items.
- Use constraint text below the prompt input to increase visibility of available shortcut menus and their functionality.
- Use one symbol per menu type.
- Persist modes when users are likely to continue similar prompts. For example, maintain a mode like / *dev* across multiple turns so users don't need to reapply it each time they ask a question or give a command.
- Keep active modes visible and display them as an inline token so users always know which mode they've configured. Users need to see their currently applied mode to understand how the system will interpret and process their input.

## Writing guidelines

- Use sentence case, but continue to capitalize proper nouns and brand names correctly in context.
- Use end punctuation, except in [headers](https://cloudscape.design/components/header/?tabId=usage) and [buttons](https://cloudscape.design/components/button/?tabId=usage). Don’t use exclamation points.
- Use present-tense verbs and active voice.
- Don't use *please*, *thank you*, ellipsis (*...*), ampersand (*&*), *e.g.*, *i.e.*, or *etc.* in writing.
- Avoid directional language.
	- For example: use *previous* not *above*, use *following* not *below*.
- Use device-independent language.
	- For example: use *choose* or *select* not *click*.

### Component-specific guidelines

#### Reference item groups

- Use descriptive names for categories of reference types within suggestion groups to help users select relevant items within shortcut menus.
	- For example: a shortcut menu triggered by a */* may have both quick actions and modes labeled as *Modes* and *Quick actions*.

#### Constraint text

- Describe the special characters and the shortcut menus they invoke separated by commas.
	- For example: Use */* to set a mode and quick actions, *@* to add context.

#### Menu button labels

- Match the label to the keyboard character that triggers the same menu.
	- For example: */* button for modes and actions menu, *@* button for references menu.
- Follow [writing guidelines for icon button](https://cloudscape.design/components/button/?tabId=usage#component-specific-guidelines).

## Accessibility guidelines

- Follow the guidelines on alternative text and Accessible Rich Internet Applications (ARIA) regions for each component.
- Make sure to define ARIA labels aligned with the language context of your application.
- Don't add unnecessary markup for roles and landmarks. Follow the guidelines for each component.
- Provide keyboard functionality to all available content in a logical and predictable order. The flow of information should make sense.

### Generative AI chat

Generative AI chat is a conversation between a user and a generative AI assistant.

### Prompt input

Enables users to provide a prompt or command.

### Variables

A pattern for using variables within structured content such as prompt templates, code snippets, and text with predefined formats.
