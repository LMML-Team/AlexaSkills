# Alexa Skills
This is a student project for our Cognitive Assistant in Beaver Works 2017.
By [Anthony Cavallaro](https://github.com/QuantitativeFinancier), [Amanda Wang](https://github.com/CandyMandy28), [Michael Lai](https://github.com/impostercafe), and [Petar Griggs](https://github.com/Anonymission)
## Setup

### Setup.py
Clone this repository into your desired repository.

Install everything at once by running:
```shell
python FaceRecognition\setup.py
```

### Ngrok
We have provided you ngrok from https://ngrok.com/download.
Run ngrok.exe.

**To run Ngrok**, go to the directory of the cloned repository and run the command:
```shell
./ngrok.exe http 5000
```
or
```shell
./ngrok http 5000
```

### Alexa (Echo)
To run the skills, you need to create an amazon developer account in order to access the (Alexa Skills Kit)[https://developer.amazon.com/alexa-skills-kit].

Once you have an account, sign into (Amazon Developer)[https://developer.amazon.com/] and go to Alexa > Alexa Skills Kit.
Click on `Add a New Skill`.
Create a name and invocation name, click save, and move onto the next part, Interaction Model.

**For Intent Schema**, fill in the parameters that the skill will need.
```
{
   "intents":
   [
   {"intent": "YesIntent"},
   {"intent": "NoIntent"},
   {"intent":"AMAZON.PauseIntent"},
   {"intent":"AMAZON.ResumeIntent"}
   ]
}
```

Next, for Sample Utterances, fill in the text box with example words that you may say to continue or discontinue an action.
```
YesIntent yes
YesIntent yeah
YesIntent ok
YesIntent sure

NoIntent no
NoIntent no thanks
NoIntent nope
```

**For Configuration**, select HTTPS for the Service Endpoint type and select the continent you are planning to use this in. A textbox will appear, and you need to have ngrok running and copy the HTTPS URL. It should be `https://(random_hash).ngrok.io`
