# Define data set
categories = ["Experience", "Career Goals", "Personality"]
InterviewQuestions = [
"Experience":   "Tell me about the last time a co-worker or customer got angry with you. What happened?", 
				"Can you give me a specific example of your leadership skills?",
				"Give me an example of a time when you faced a conflict while working on a team. How did you handle that?",
				"What specific skills did you get from your last job?",
				"What makes you more qualified than the other candidates?",
				"How does your experience qualify you for this job?",
				"What single project or task would you consider your most significant career accomplishment to date?"
				]

# configure what to do when launch/intent/session end request
def request_handler(event, context):
	if event["session"]["new"]: # what to do when new session has started
		start()
	if event["request"]["type"] == "LaunchRequest": # what to do when launchRequest
		return launch(event)
	elif event["request"]["type"] == "IntentRequest":
		return intents(event)
	elif event["request"]["type"] == "SessionEndedRequest":
		return end()

# request handlers except for intents
def start():
	print("Session has started")

def launch(event):
	launchMessage = "Hi and welcome to the interview me Alexa skill. You can request a question related to" + ', '.join(map(str, categories)) +
	"or a random question. Or, you can ask for a boost of confidence! Try saying Alexa, hype me up."
	repromtMessage = "Would you like to chooose a new category?"
	cardText = "Please select a category"
	cardTitle = "Category Selection"
	return outputJsonBuildWithRepromptAndCard(launchMessage, cardText, cardTitle, repromptMessage, False)
def end():
	print("Session Ended")

# intent request handler
def intents(event):
	intentName = event["request"]["intent"]["name"]

	if intentName == "RequestSpecificCategory":
		slotCategory = event["request"]["intent"]["slots"]["category"]["value"]
		return specificQuestion(event)
	elif intentName == "RequestRandom":
		



p1='What might you consider your biggest strength?'
p2=' What might you consider your biggest weakness?'
p3='Give an example of a project you worked on, in which you were dissatisfied with your own work, and what you would do differently.'
p4='What is your definition of hard work?'
p5='How do you personally define success?'
p6='How do you handle stress?'
p7='What are your passions outside of your career'
p8='Why did you choose this profession?'

print(p1)