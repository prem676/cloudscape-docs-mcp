---
title: "Progressive steps - Cloudscape Design System"
source: "https://cloudscape.design/patterns/genai/progressive-steps/"
created: 2025-10-07
description: "A hierarchical display of information to inform users of the tasks being performed."
---
## Building blocks

![](https://cloudscape.design/__images/yvlrib0vb3vb/6incbcjkhIP8hWxSwCZzl9/da0644bf98a3145211e2f7614fab92b5/patterns--genai--progressive-steps--building-blocks--vr-light.png) ![](https://cloudscape.design/__images/yvlrib0vb3vb/bwJ4qan3ZmuNM9kbYxH8h/31f43265c68016b90cafcd4476e706d1/patterns--genai--progressive-steps--building-blocks--vr-dark.png)

#### A. Header - optional

When displaying a list of steps, the header should succinctly describe the main task or workflow. In a chat interface, a header may not be necessary as the context is established through the conversation.

#### C. Sub-steps - optional

If the main step has sub-steps, display them in a [tree view](https://issues.amazon.com/issues/AWSDesignSystem-489) leveraging the [status indicators](https://cloudscape.design/components/status-indicator/) component.

#### D. Status hub - optional

If there is more than one status within sub-steps, display a status hub to the right of the step. The status hub uses the [status indicator](https://cloudscape.design/components/status-indicator/?tabId=playground&example=error) component.

#### E. Step details - optional

Step details can be indicated via popover or description text. Use a [popover](https://cloudscape.design/components/popover/?tabId=playground&example=medium) to provide supplemental information about the step. Use description text to display details that are necessary for the user’s context. For example, estimated completion time for a step, or additional details about a step status.

#### F. Input request - optional

When gathering additional information from users to generate an output, display the [input requests in a dialog](https://github.com/cloudscape-design/demos/blob/main/src/pages/chat/additional-info/dialog.tsx) with form fields. To avoid blocking the user, include the ability for them to skip the input if desired. However, if the input is required, exclude the skip button, and add form field error text if a user attempts to bypass the form.

Provide clear and informative [status indicator](https://cloudscape.design/components/status-indicator/?tabId=playground&example=error) updates throughout the process to maintain user transparency and trust. This helps users understand what the system is doing and builds confidence in the generative AI capabilities.

Adjust the visual indicators and level of detail based on the expected latency, as mentioned in the [feedback mechansims](https://cloudscape.design/patterns/general/user-feedback/#criteria) pattern. This allows the progressive loading of steps to appropriately respond to varying response times and frames expectations for long load times.

- For under 10 seconds, provide additional details if possible, such as a list of sub-steps.
- For above 10 seconds, show a time estimate for indeterminate wait times, and a [progress bar](https://cloudscape.design/components/progress-bar/) for determinate wait times.

Clear and contextual error or warning messages help users understand any issues that arise during the process, and enable them to take follow-up actions. This transparency helps build trust in the generative AI system's capabilities.

Status updates and loading indicators should be kept concise and unobtrusive. Provide users the ability to view more details about steps within the process through the use of popovers, links, or expandable sections. This allows users to control the level of information they receive.

### Request input

There are times when additional information is needed from the user to complete a task or provide a relevant response. In these cases, present clear input requests to gather the necessary details.

Generative AI can vary in response times. The progressive steps experience should adjust the loading states and indicators based on the expected latency, providing different visual cues for loading experiences above and below 10 seconds.

#### Under 10 seconds

**Default:** Display a loading status on the last [step](https://cloudscape.design/components/steps/?tabId=playground&example=with-loading). Avoid displaying a loading state for under one second as this can seem jarring to users and can cause flickering in the UI.

1. Evaluated
	---
2. ---
3. ---

**Sub-steps:** Display sub-steps with corresponding status to inform users of the overall progress when applicable. For example, display a list of nodes being checked when troubleshooting an EKS issue.

![](https://cloudscape.design/__images/yvlrib0vb3vb/31yAETEJqwKiPNFWFDL6xk/9bccf8aeac3ee8c7225d96097bb75399/patterns--genai--progressive-steps--latency--vr-light.png) ![](https://cloudscape.design/__images/yvlrib0vb3vb/1yy191Id0NlqMXzUmQlSHR/73e520a807121a8d3177c94d996499d8/patterns--genai--progressive-steps--latency--vr-dark.png)

#### Above 10 seconds

**Indeterminate loading state:** Display the current step in a loading state along with an estimated wait time. This helps communicate the anticipated timeline and set appropriate user expectations.

1. Evaluated
	---
2. ---
3. ---
	This step may take up to 15 seconds to complete.

**Determinate loading state:** If a wait time is determinate, display a [progress bar](https://cloudscape.design/components/progress-bar/?tabId=playground&example=within-flash-component) with the time remaining as suggested in [feedback mechanisms](https://cloudscape.design/patterns/general/user-feedback/#criteria). This helps keep users informed about the processes unfolding over a longer period of time and builds trust.

1. Evaluated
	---
2. ---
3. ---
	Less than 20 seconds remaining

### Error

![](https://cloudscape.design/__images/yvlrib0vb3vb/6YGy3dpYC7F5smFIoj4CSE/5da53145a7240a99d867bbcc3aaf8ba6/patterns--genai--progressive-steps--error--vr-light.png) ![](https://cloudscape.design/__images/yvlrib0vb3vb/3UfBQbxhIzQkRS2L9SILjj/9bc990fc674475bb805f1e01e0df0023/patterns--genai--progressive-steps--error--vr-dark.png)

#### A. Step error

When a step has an error, provide clear and concise error details along with the failed status. Offer a retry option whenever it's appropriate for the user to attempt the action again.

#### B. Sub-step error

If there is more than 1 error status within sub-steps, such as an error and warning, display the status hub to the right of the main step.

#### C. Error details

When an error or warning message has lots of details corresponding to it, provide them in a [popover](https://cloudscape.design/components/popover/). This will help prevent overwhelming users with information displayed at once.

### Output

When presenting the final output to the user, include an [expandable section](https://cloudscape.design/components/expandable-section/) detailing the steps taken to generate the output. This should be collapsed by default.

1. Evaluated
	---
2. ---
3. ---
4. Summarized output
	---

## General guidelines

### Do

- **Enable access to details**
	Enable users to view more details about each step of the process through popovers, links, sub-steps, or expandable sections. This gives users the ability to dig deeper into the troubleshooting details.
- **Limit input requests**
	Limit the number of input requests to 3, if possible. This helps avoid overwhelming the user and maintains a streamlined troubleshooting experience.
- **Change the status to pending when a sub-step is loading**
	When a sub-step is loading, change the status of the main step to *pending* to indicate that the step is in progress, and move the *loading* status to the sub-step rather than leaving it on the main step.
- **Prioritize the most urgent status**
	The status of the main step corresponds to the most critical status in the sub-step. For example, If there is an error, warning, and success status in the sub-steps, the main step will have an error status.

### Don't

- **Avoid displaying a loading state for under one second**
	Displaying a loading state for under one second can seem jarring to users and can cause flickering in the UI. For example, If the model supports streaming and has a rapid processing stage, don’t display the loading text in chat bubble, instead start streaming the response directly.
- **Don’t have more than 4 levels of sub-steps**
	Keeping the number of sub-steps limited to 4 levels or less helps maintain a manageable view for the user.

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

#### Error

- **Step error:** When a step has an error, provide clear and concise error details along with the failed status. Offer a retry option whenever it's appropriate for the user to attempt the action again.
- **Sub-step error:** If there is more than 1 status within a sub-steps, such as an error and warning, display the status hub to the right of the main step.
- **Error details:** When an error or warning message has lots of details corresponding to it, provide them in a [popover](https://cloudscape.design/components/popover/). This will help overwhelming users with information displayed at once.

#### Loading text

Follow the writing guidelines for [loading and refreshing](https://cloudscape.design/patterns/general/loading-and-refreshing/#writing-guidelines) pattern.

#### Status indicator

Follow guidelines for [status indicator](https://cloudscape.design/components/status-indicator/?tabId=usage#writing-guidelines) component.
