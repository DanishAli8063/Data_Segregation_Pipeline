from preprocess import Preprocess
from fuzzywuzzy import fuzz

class SimilarityFinder:
    def __init__(self):
        self.threshold = 60
        self.bot_sentences = ["To qualify you for the plan are you between age of 40 & 80.So is your age above 65 years right.So is your age under 65 year right.To qualify you for the plan are you between age of 50 & 75.To qualify you for the plan are you between age of 50 & 92.So is your age between 40 & 92 right.",
"That’s pretty much all the information I needed now I will transfer this call really quick to my supervisor he is going to quickly verify this information just to make sure we are not making any clerical mistakes please stay on the line.",
"I believe that total mileage of your car is less than 150 thousand miles, is that correct? I believe that total mileage of your car is less than 175 thousand miles, is that correct?",
"The new Medicare plans are allowing for more coverage on things that were previously lacking.Things like dental vision hearing and over the counter drugs, it's only gonna take a minute or two to see if you qualify, and I just have to ask a few questions okay!",
"That’s pretty much all the information I needed, now I will transfer this call really quick to my supervisor. He is going to quickly verify this information just to make sure we are not making any clerical mistakes. Please stay on the line.",
"Thank you for your time, have a nice day.",
"Apologies",
"Say that Again.",
"Sorry to hear that.",
"Transfer Just give me a quick 10 more seconds and let's see what we can offer you, okay.",
"This call is about a new state regulated final expense insurance plan which covers 100% of burial funeral or cremation expenses its specially design for the people on fixed income or social security.",
"No, I am alive person.",
"So! I believe you are with your current provider for more than 6 months.",
"Say that again.",
"Well, I am calling you to tell you a little about the solar program, the benefits, tax rebates and grants from the government. Typically, it means going solar is absolutely free for most people.",
"Hi this is Tom I am calling you from Auto warrant processing center. How are you doing today?",
"I understand and its great you are thinking ahead but we will like to show you somethings just go ahead and see the information if you like otherwise there is no obligation on your part.",
"That’s pretty much all the information I needed from my side to check your eligibility and it does look like you may qualify. Now I am gonna quickly refer you to my licensed agent to get you some more details. Give me just a second, please.",
"I am doing good thanks for asking.",
"I understand I am not asking you to buy or change anything right now. Just listen to discounted prices, keep them in your mind for Future okay!",
"Can I confirm that you are the homeowner?",
"What will happen now is I will put this through the verification team they will contact you in next 15 to 30 minutes to verify the details I have taken down through you and to confirm the available appointment times if you got any further questions or check on anything else that pops into your head, they will answer for you in the meantime enjoy rest of your day.",
"To qualify you for the plan are you between age of 40 & 80.",
"Hi my name is Tod calling from American Solar, how are you doing today.",
"okay good",
"Alright, now your car has qualified for additional benefits, so I have one of my warranty specialists on the line who will assist you further. Just stay on the line for a few more seconds.",
"I understand but its not gone a take much time I have a product specialist on the line who can show you some options and you can take your time to take a decision.",
"Hmmm.",
"yes, yes, I am alive person.",
"Can you Hear me.",
"So! I believe I am speaking to the home owner, right?",
"Already In order to avail a discount I believe you have an active Bank Account.",
"Please What is your postal code.",
"It could be worth looking into it, its completely free to have technical surveyor around it, it takes about total 45 minutes to go through all the way through inspection there isn’t any obligation you know, you do what is your will but they can make your mind, showing how much a solar system would save you.",
"It could be worth looking into it, it’s completely free to have technical surveyor’s inspection there isn’t any obligation to you know, you do what is your will but they can change your mind,",
"The reason of the call is to let you know that rates of Auto warranty has been dropped on up to 30% We are providing you Auto warranty for five brand new years and also providing you free road side assistance as well.",
"Great. That’s everything I need; these things will be referred to our verification team and they gone a reach you in next 30min or so and answer your queries also if any and confirm appointment with you in the meantime enjoy rest of your day.",
"Ahan..",
"So would you like to learn more about this warranty.",
"I can bring my Product Specialist on the line and he can give you more information about it, Ok.",
"I will be transferring your call to a licensed insurance agent who would provide you with a quote. If you would like to get a quote, press 1, or stay on the line for the next 10 seconds. Press 2 to have your name removed from our list.",
"I understand but it's not gonna take much time. I have a product specialist on the line who can show you some options and you can take your time to take a decision.",
"So is your age between 40 & 92 right.",
"No no, like I said we are just providing free consultation about the solar program. We are just trying to get you a comparison between two options. If you think you are saving money you can go ahead, otherwise there is no cost or obligation on your part.",
"I understand, you are the home owner of a single family regular house, right!",
"That’s great.",
"Hi, my name is Holly, I’m one of the local energy advisers covering your area.",
"That’s Awesome.",
"Hi this is smantha with Medicare department health care benefits, how are you doing today.",
"Sad-Greeting Sorry to hear that.",
"I didn’t get that can you please repeat.",
"I completely understand that but these new affordable plans have just been approved in your state and everyone qualifies so our product specialist can give you more information right now if you like the prices, you can go on otherwise no obligation on your part OK.",
"Hi this is Mark from US Auto care. How are you doing today?",
"So, it’s less than 100 dollars, is it around seventy-five to ninety dollars on average between summers and winter.",
"I am calling because the updated plans for Medicare have been released and it may give you better access to things like dental vision hearing and over the counter benefits.Now these benefits aren’t automatically given so we are calling to make sure you are getting actually everything you are entitled to there is also addition benefit where you may qualify to get up to 100 dollar as cash back through your social security depending on your income.",
"OK, let me ask you this, given the current economic situation, somewhere down the line, if you want to increase your property value by simple renovation or remodeling work, would you think about it?",
"I understand but it's not gonna take much time. I have a product specialist on the line who can show you some options and you can take your time to make a decision.",
"Is your car model above 2013. Is your car model above 2007.",
"I understand I am not asking you to buy or change anything right now. Just go ahead and see the information if you like it ok, otherwise there is no obligation on your part.",
"Do you want to learn more about it.",
"I understand but given the current economic situation, we will like to show you somethings just go ahead and see the information if you like otherwise there is no obligation on your part.",
"Are you capable enough to make your own financial decisions.",
"I understand but its not gone a take much time. I have a product specialist on the line who can show you some options and you can take your time to take a decision.",
"Can you also confirm the First line of your address and Postal code.",
"Okay do you fit the age bracket between 45 and 79 years over of age.",
"Hi This is Tim from Home Improvement Services. How are you today?",
"Hello",
"Hi this is Ammy with American senior citizen care, how are you doing today.",
"The reason of the call is to let you know that We have recently drop down auto insurance rate up to 35% in market and right now I just wana give you the quotes its free of the cost you can just keep in your mind for future Okay.",
"I believe you do have Medicare Part A & B correct.",
"Are you still paying over 100 dollars on your electric bill.",
"So, we specialize in a wide range of home improvement services such as repair renovation and remodelling.",
"To qualify you for the plan are you between age of 50 & 92.",
"Perfect",
"I understand I am not asking you to buy or change anything right now just go ahead and see the information, if you like it's ok, otherwise there is no obligation on your part.",
"Alright.",
"I understand and its great you are thinking ahead but as you know cost of Funeral has increased over the years and we will like to show you some comparable options to assure you that you are getting best value of your dollar.",
"To qualify you for the plan are you between age of 50 & 75.",
"So is your age under 65 year right.",
"I can bring my Product Specialist on the line and he can give you more information about it Ok",
"So is your age above 65 years right.",
"So what if we are able to offer you something better and cheaper than what you are paying right now would you at least consider it as an option and think about it may be.",
"I understand and its great you are thinking ahead but we will like to show you some comparable options to assure you that you are getting best value.Just see the information.",
"A technical surveyor would check to see what you’re spending on your energy bills, to see if there are any savings you could benefit from, for example they’ll do is carry out a free roof survey to check the feasibility of Solar panels system for you and the solar panels and battery storage systems can help save up to 70% of your energy bills. can we well worth to look at it.",
"Hi, my name is Holly, I’m one of the local energy advisers covering your area. The reason for the call is to make you sure you’ve had your free energy saving assessment carried out at your property.",
"r u there",
"I understand I am not asking you to buy or change anything right now. Just listen to discounted prices, keep them in your mind for the future, okay.",
"Is that okay.",
"The reason for the call is to make you sure you’ve had your free energy saving assessment carried out at your property due to the energy crisis we’re going through at the moment.So by Using Solar panels and battery storage systems it can help save up to 70% of your energy bills So you’re entitled to a couple of services at no cost to yourself.",
"Hi",
"My name is Becky from Senior Benefits",
"This course allows you to spend a new low cost final expense license",
"Are you the one who makes your own decisions?",
"Great, I'm just gonna quickly connect you with a product specialist right away. Please hold on.",
"Hey, can you hear me? Are you still there?",
"Alright, I do understand your concern, but as you know the cost of funeral has increased over the years. So we're just here to show you some comparable options to give you an idea that if you're getting the best value of your dollar and I do have a product specialist with me on the line we can go ahead and show you some quotes right away. Okay.",
"I'm doing just fine, thanks for asking.",
"Well, I understand, but let me tell you this. These plans are specifically designed for the people on fixed income or social security and almost everyone qualifies for it.",
"And I do have a product specialist with me on the line who can simply provide information right away and you're under no obligation. If you like the plans, you can go on, otherwise you can stay where you are.",
"Oh come on... I wish I was, but I'm not actually.",
"Alright great, to qualify you for the plan are you between the age of 40 and 80?",
"Great, That sounds great.",
"Well, I'm just calling to let you know about a new state-approved final expense insurance plan, which covers the cost of your funeral, burial, or cremation expenses. And also you can leave some money for your loved ones. So would you like to learn more about it?",
"Awesome, awesome.",
"I understand but let me tell you it's not going to take much of your time. I have a product specialist with me on the line who will take only a few minutes of your precious time. I will show you some quotes right away and you can just take your time to make a decision. Alright.",
"Hello?",
"Hi, my name is Ethan. I'm calling you on behalf of Financial Solutions for Seniors. How are you doing today?",
"I beg your pardon, can you please repeat that?",
"Okay, sounds good.",
"and I hope so you do make your own financial decisions"
]



    def similarityFinder(self, bot_sentences, splitted_transcripts, threshold=81):
        preprocess = Preprocess()
        bot_indices = []

        #"bot_sentences" is a list of bot keywords/sentences
        for bot_sentence in bot_sentences:
            for index, transcript in enumerate(splitted_transcripts):
                #cleaning data
                b_sentence = preprocess.preprocess_text(bot_sentence)
                s_transcript = preprocess.preprocess_text(transcript)
                #finding similarity
                token_set_ratio = fuzz.token_set_ratio(b_sentence, s_transcript)

                if token_set_ratio>=threshold:
                    bot_indices.append(index)
        
        return bot_indices
    



