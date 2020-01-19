import random
# Define data set
categories = ["Experience", "Career Goals", "Personality"]
interviewQuestions = [
"Experience":  ["Tell me about the last time a co-worker or customer got angry with you. What happened?", 
				"Can you give me a specific example of your leadership skills?",
				"Give me an example of a time when you faced a conflict while working on a team. How did you handle that?",
				"What specific skills did you get from your last job?",
				"What makes you more qualified than the other candidates?",
				"How does your experience qualify you for this job?",
				"What single project or task would you consider your most significant career accomplishment to date?"]
"Career Goals":["What professional achievement are you most proud of?",
				"Where do you aspire to be in five years?",
				"What have you done most recently to strengthen your career skills?",
				"What non-career goals are you most proud of reaching? Why does that particular goal stand out?",
				"Why do you want this job?"]
"Personality": ["What might you consider your biggest strengths?",
				"What might you consider you biggest weakness?",
				"Give an example of a project you worked on, in which you were dissatisfied with your own work, and what you would do differently.",
				"What is your definition of hard work?",
				"How do you personally define success?",
				"How do you handle stress?",
				"What are your passions outside of your career?",
				"Why did you choose this profession?",
				"What's the biggest decision you've had to make in the past year? Why was it so important?",
				"If you could relive tha last ten years of your life, what would you do differently?"]
				]

# Set up full question bank
questions = interviewQuestions.values 
questionBank = []
for question in questions:
	questionBank.extend(question)

# hype responses

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
	repromptMessage = "Would you like to chooose a new category?"
	cardText = "Please select a category"
	cardTitle = "Category Selection"
	return outputJsonBuildWithRepromptAndCard(launchMessage, cardText, cardTitle, repromptMessage, False)

def end():
	print("Session Ended")

# intent request handler
def intents(event):
	intentName = event["request"]["intent"]["name"]

	if intentName == "RequestSpecificCategory":
		return specificQuestion(event)
	elif intentName == "RequestRandom":
		return randomQuestion(event)
	elif  intentName == "HypeMe":
		return hype(event)
	elif intentName == "GeneralInterviewTips":
		return generalTips(event)
    elif intentName in ["AMAZON.NoIntent", "AMAZON.StopIntent", "AMAZON.CancelIntent"]:
        return stopSkill(event)
    elif intentName == "AMAZON.HelpIntent":
        return assistance(event)
    elif intentName == "AMAZON.FallbackIntent":
        return fallback(event)

# define intent handler functions
def specificQuestion(event):
	slotCategory = event["request"]["intent"]["slots"]["category"]["value"]
	if slotCategory in categories:
		specQuestion = random.choice(interviewQuestions["slotCategory"])
		repromptMessage = "Would you like to select another question?"
		cardText = specQuestion
		cardTitle = specQuestion
		return outputJsonBuildWithRepromptAndCard(specQuestion, cardText, cardTitle, repromptMessage, False)
	else:
		wrongNameMessage = "Sorry, we don't have support for that category yet. If you have forgotten the categories, please say help"
		repromptMessage = "Would you like to select another question?"
		cardText = "Please use a valid name"
		cardTitle = "Please use a valid name"
		return outputJsonBuildWithRepromptAndCard(wrongNameMessage, cardText, cardTitle, repromptMessage, False)

def randomQuestion(event):
	randQuestion = random.choice(questionBank)
	repromptMessage = "Would you like to select another question?"
	cardText = specQuestion
	cardTitle = specQuestion
	return outputJsonBuildWithRepromptAndCard(randQuestion, cardText, cardTitle, repromptMessage, False)

def hype(event):
	return

def generalTips(event):
	return

def stopSkill(event):
	stopMessage = "See you next time!"
	repromptMessage = ""
	cardText = "Bye!"
	cardTitle = "Bye!"
	return outputJsonBuildWithRepromptAndCard(stopMessage, cardText, cardTitle, repromptMessage, True)

def assistance(event):
	assistMessage = "You can select any of the following categories: experience, career goals, and personality. You can also ask for a" +
	" random question, a general interview tip or just a boost of encouragement. Try saying: Alexa, ask me a personality question."
	repromptMessage = "Would you like to select another question?"
	cardText = "You have asked for assistance."
	cardTitle = "Help"
	return outputJsonBuildWithRepromptAndCard(assistMessage, cardText, cardTitle, repromptMessage, False)

def fallback(event):
	fallbackMessage = "Sorry, I can't help with that yet."
	repromptMessage = "Would you like to select another question?"
	cardText = "You have asked an invalid question"
	cardTitle = "Invalid question"
	return  outputJsonBuildWithRepromptAndCard(fallbackMessage, cardText, cardTitle, repromptMessage, False)

# functions for building the output JSON
def plainTextBuild(text):
	textDict = {}
	textDict['type'] = 'PlainText'
	textDict['text'] = text
	return textDict

def repromptBuild(repromptText):
	repromptDict = {}
	repromptDict['outputSpeech'] = plainTextBuild(repromptText)
	return repromptDict

def cardBuild(cText, cTitle):
	cardDict = {}
	cardDict['type'] = "Simple"
	cardDict['title'] =  "cTitle"
	cardDict['content'] = "cText"
	return cardDict

def responseFieldBuildWithRepromptAndCard(outputText, cardText, cardTitle, reprompt_text, value):
    speechDict = {}
    speechDict['outputSpeech'] = plain_text_builder(outputText)
    speechDict['card'] = card_builder(cardText, cardTitle)
    speechDict['reprompt'] = reprompt_builder(repromptText)
    speechDict['shouldEndSession'] = value
    return speechDict

def outputJsonBuilderWithRepromptAndCard(outputText, cardText, cardTitle, repromptText, value):
    responseDict = {}
    responseDict['version'] = '1.0'
    responseDict['response'] = responseFieldBuildWithRepromptAndCard(outputText, cardText, cardTitle, repromptText, value)
    return responseDict




