SPEAKER 0
This material has been reproduced and communicated to you by or on behalf of the Australian National University, in accordance with Section 113% of the Copyright Act 1968. The material in this communication may be subject to copyright under the Act. Any further reproduction or communication of this material by you must be consistent with the provisions of the Act. Do not reproduce this material. Do not remove this notice.

SPEAKER 1
All right. Good afternoon, everyone. How is everyone? Getting uh Emptier, is it? Did you observe that in your other lectures this week as well? Yeah. Well, maybe it's the. In between long weeks I don't really know. Could be the the regular drop off towards the. Uh, last 3 of the semester, but in any case. Um, are there any questions before we continue? Is there any housekeeping that we need to talk about?

SPEAKER 2
Oh, is it not? No, no, no, don't, it's probably not.

SPEAKER 1
I can release it today. If I don't forget, um. I'll try to do it today. Let me set myself a reminder. There's no reason why it shouldn't be.

SPEAKER 2
Um, just a second.

SPEAKER 3
Also that, when would you recommend starting it?

SPEAKER 4
Yeah.

SPEAKER 3
Mm.

SPEAKER 1
I'll tell you in a second.

SPEAKER 2
I'm not good at multitasking.

SPEAKER 1
But I'll tell you in a second, um. This is how slow I am. So let's say at 6, you can remind me here, OK. All right. And that assignment, assignment 2, the last assignment, I will post hopefully today. And but it's based on what up to including lecture 9 or next week. Yeah, um, and it definitely plays with some of the

SPEAKER 2
concepts of next week. Uh, I think you can start working on it already,

SPEAKER 1
so it's gonna be multiple regression, but it's playing with

SPEAKER 2
functional forms as well, which is what we discuss next

SPEAKER 1
week. When is it due? Must be in week 11. So we can return it to you, or at least we can try to return it to you in week 12. Um, so again, you would have plenty of time, I

SPEAKER 2
think.

SPEAKER 1
So after we finish week 9. Uh, you, you'll be able to completely solve the assignment then you have.

SPEAKER 2
Basically, week 10 to work on it and even the first bit of week 11.

SPEAKER 1
And again, it should take you maybe 3 hours, 4 hours. Is that uh roughly what the first assignment took you? The second assignment is not so closely modelled on the computer lab as the 1st assignment. It's on purpose with the 1st assignment, you know, everyone was still learning Python coding and. And for that matter, how my assignments look like. So I made it very similar to the computer lab so everyone felt safe, which is not to say that the second assignment's going to be completely different, but it'll be more, more separated from the from the computer lab,

SPEAKER 2
but still you, you'll recognise concepts.

SPEAKER 1
But the workload is roughly the same, I think. Are there any other questions? So I'm trying to, to release that today. Um, what else? Then there's gonna be a quiz next week, I think. I'll remind everyone of that. We run it as per usual from. Was it Wednesday morning to Thursday afternoon? And it tests I don't know what it tastes.

SPEAKER 2
The last 4 weeks or whatever, I'll, I'll tell you,

SPEAKER 1
but um, yeah. Um, any other? Questions Cool. All right. Let's do more econometrics today. It's a kind of important lecture conceptually. It's not it's not going to be very technical, I hope, which is not to say there's no equations, but let's have a look. So the topic is bias from omitted variables, so that's quite. An important Concept. So let's, let's dive into it. So let's say an oracle tells us. So that is like an all knowing person or entity tells us that this is the regression that you should be running. Which is to say. X1 and X2. All you need to explain why that's roughly what I'm trying to say here. So Oracle says this is the model. So what you should do if you're given. Data on Y X1 and X2, you should run a regression of Y on X1 and X2. But You ignore the oracle and only regress why on X1.

SPEAKER 2
What happens?

SPEAKER 1
What's the danger of, of doing that? Let's see what happens. So it should be clear, first of all, um, first of all, what? Yeah, so instead of running this multiple regression, you're just running a simple regression of Y on X1. From what we did last week in the workshop session. Or maybe intuitively also it should be clear that If you compare the two regressions, the one that you should be running, which is here, the first one. And the one you, you run, the, the, that you actually end up running because you're stubborn, you run the

SPEAKER 2
11, where you just regress Y on X1, you go,

SPEAKER 1
I like what we did in the first half of the semester when we just did the simple regression. I just regressed Y on X1. The coefficient estimates here that you obtain for the coefficient that belongs to X1, will be numerically different. We saw that last week when, oops. Hello Why? Um, Cooling down, OK. Clearly. Now it's warming up again. Is it coming down? Um, what was I trying to say? The coefficient estimate, it doesn't let me do anything. The coefficient estimates are different. All right, what I wanted to say is we last week, We, we, we had the, the regression of. Test scores on the student-teacher ratio, the picture is still there. Oh right.

SPEAKER 2
So I just need, OK, now I can.

SPEAKER 1
Um Last week we regressed, sorry, test scores on student-teacher ratio. We obtained an estimate for the, for the coefficient on student-teacher ratio STR student-teacher ratio. Then we extended that in a multiple regression. Where we added what was it the English learner percentage in the school district and some other variable doesn't really matter but point being the coefficient estimate on the student teacher ratio changed. That's all I'm saying here. OK. The question is which one is better? Now, given that the Oracle told us you should really be regressing Y on both variables, we're guessing that the first one gives us a coefficient estimate for beta one that is better. But let's study this. What um Technically Um, so the question is if we do run the regression of Y on X1. What do we actually estimate? So here's how we find this out, where you write down the model that was. recommended to us by the Oracle, OK? And we are hiding, all that's happening here is a rewriting. We are hiding the second regressor. Inside an The error term A new era term called W here. OK. So, cause we are, in a way, we're ignoring that X2 is present and that we actually have data on X2. So this is just a rewriting exercise that makes it look like look like now a simple regression model. The last line, the 3rd line just looks like a simple regression model. Um, And it's obvious that the error term in the first line, which is called U, and the error term W in the third line are not the same because beta 2 is not zero most generally. So I haven't said this explicitly, but when the oracle tells us you should include two regressors here, it's just implicitly saying that beta 1 and beta 2 are non-zero. If the oracle told you now surprise, beta 2 is 0, then yeah, fine, then you're back into the in the simple regression world, but that's not what the oracle told us. Um So yeah, the last line here does look like just a simple regression model. So we can use knowledge from weeks, what is it, 3 and 4 and 5 of the semester to study what happens when you regress Y on X1 only, omitting X2. And this is what happens. First, we know from week 4 or 5 that the slope coefficient in the simpler regression is simply this formula here. Roughly speaking, the sample covariants of X1 and Y over the sample variants of X1. That's, that's it, right? But then we write out for X sorry, for Y I minus Y bar. We've seen this before, and you go, well, Yi minus Y bar is then just beta 1, X1 minus X1 bar plus the error minus its mean bar. This is sort of almost copy and paste from a few weeks ago where the error was not called W but U. Now the error is called W and hides X2 in it, but mechanically it's all the same here. OK. So we plug this in here in the equation above and we obtain this result here, which we have seen. Before as well, and you go, the slope estimate is equal to beta one, plus roughly speaking, the sample covariance between X1 and the error over the sample variance of X1. OK. The error here is called W. It's the same formula that we saw several weeks ago. Now, When we study the bias of the oils estimator, when we studied that in the past, our argument was like, so, you look at this formula, and you go, Take expected values on both sides and you ask yourself what's the expected value of beta one hat. Well, it's anchored at beta one. That's the good news. That's where we want it to be anchored on, plus the expected value of this big expression here which in a well behaved simple regression works out to zero. The expected value of this whole nuisance term here. In the past, was 0. That Led to the observation that the OS estimator is unbiased. But that was when the error term, which is called W here was well behaved. It satisfied the well that's assumption one. Here it doesn't. Let's make that visible. So typically the argument now would be that X1 and the error term W are uncorrelated so that the numerator here is almost 0. OK. But that is not the case here because this error term is not uncorrelated with X1, at least not in general. And what's the root of that? Because W contains X2 in it. OK. It, it includes you, the original error term, of which we're happy to assume that it doesn't cause any trouble, but it also includes X2 in it. X2 is the omitted regressor. So here it also contains so this error term W here contains X2. Because that that's the definition of W here, right? But so so W contains two components you, the original purely random error term of which we are happy to assume, it doesn't cause any problems. It's uncorrelated with X1. That is all assumption one really, as it refers to the original error, U. But X2 is also included is another component in the in the error term that is called W here. That is the omitted regressor, which could well be correlated with X1. OK. Generally speaking, We want it, or we want to account for the possibility that the emitted regressor could be correlated with X1. If that is the case, um, then the, the unbiasedness. Doesn't follow, which will, which I'll show you in the next slide. So if indeed. The included regressor X1 and the omitted regressor X2 are correlated with each other, then the error turn W will be correlated with X1, and now going to the previous slide, then the numerator here, Will not be zero. And I'll work that out now. On the next, next slide. So let's have a look at that one. Actually, not, not quite yet. Um, so. Taking you back and forth. Um, we're working out now. The correlation here. So this is the slide that I wanted to look at. So this is, this really looks like the Unbiasedness proof, unfortunately, here it is a proof of bias and it follows the steps from the proof that we saw several

SPEAKER 2
weeks ago when we established that the OS estimator was

SPEAKER 1
unbiased. Here we show that there is a bias. So if you, if we just look at the left hand side and the very final outcome, the statement is the expected value of beta one hat is equal to beta one. Plus this stuff here that is non-zero in general. So, this stuff here, this um beta 2 plus the covariance over the variants, was not there. In week 4 or 5 whenever we established unbiasedness of the OS estimator. Um, so there is a bias here, and the bias term is this whole beta 2 times covariance of variance business. Now, let's discover where that all comes from. Let's go through, through this line by line. So the OLS estimator in the simple regression. Um beta one hat has this expected value here. So you take the previous results, so this result here, the right hand side, and you go apply expected value to these two components. Well, beta one is not a random variable, it's just a number. So that's this beta one there. And then expected value, this was all conditional on knowing X1 and X2. So we've got more taking several steps ahead because we have seen proofs like this before. We get the expected value now here inside the sun. And the brackets are around X1 minus X1 bar, WI minus W bar. This is all conditional X1 X2. And in the denominator we have sum of X1 minus X1 bar square we can take that out of the expected value because this is a conditional expectation, right? What else is happening in the next line, is it the third line here, 2 equality, we just plug in the definition of W I minus W bar, and that's this thing here, beta 2 X2 minus X2 plus U I minus U bar. Yeah. So then you have basically these two terms that stem from the, from W from the definition of W. And we take these two terms apart. So they have a part that belong, that takes care of the presence of X2, and another part that takes care of the presence of the original error you. So we've got in the 4th line, 3 equality, we get basically two terms. Um, so this term here. Results from the presence of beta 2 X2 minus X2 bar here. Um, and Pulling apart the components of the conditional expectation we get this guy here and the second term here

SPEAKER 2
takes care of the presence of U I minus your

SPEAKER 1
bar up here. That's this thing here, taking out X1 because we're conditioning on X1. So we have altogether beta 1 plus this term that that results from the presence of X2 in the error term and this term here, which results from the original error term that was present in the model, OK? This, what am I doing in the next slide. All right, and then for what happens as I move to the next line, who can tell me why this whole thing goes out, at least seemingly. As I move from This very long line to the next one. Why does this drop out? I might say it on the next slide.

SPEAKER 2
Yeah, because for this guy here.

SPEAKER 1
We assume Mean independence. So we could just quickly say that's 0. OK. So this here is the well-behaved error term U I minus U bar from the original model that the oracle told us, gave us. That error term. For that error term, or that's the assumption 1 applies. And so that cuts this off here straight away.

SPEAKER 2
So this here is 0.

SPEAKER 1
Because the expected value of the error term given the excess is 0, by assumption. Well behaved era But there's one component of the of the errorW that is not well behaved, and that's this component here that we carry with here. So we, we just basically copy and paste from the middle line to the next line. We divide by N, upstairs and downstairs, and then. It gets the flavour of a sample covariance over a sample variance. Then I'm just doing a population approximation, so when in the 3rd last equality, I have beta 1 plus beta 2, and what I have in the numerator is the sample covariance between the Xs over the sample variance of X1. Then I go, I want the population equivalent, so I'll do an approximate equality if my sample is large, then the sample covariance in the numerator becomes the population covariance and the denominator the population variance.

SPEAKER 2
And that's then this here. So bottom line.

SPEAKER 1
The expected value of the slope estimator for the included regressor is equal to beta one. Plus a nuisance term, a biassed term, and the biassed term is beta 2. Times the covariance between the Two regressors, the included one and the excluded one. Over the variants of the included regressor. X1 Now, OK, here this, I'm just repeating. What's the bias equal to? So the OS estimator is biassed here. If you ignore the presence of X2, you just run the simple regression. What you're estimating, roughly speaking, going back. You're estimating beta one plus this nuisance term. Now let's say the oracle tells you. But beta 2 was actually 0. And you go, OK, then that really means you're telling me that the original model was a simple regression, then there is no bias, then the bias goes away. Or alternatively, the oracle could tell you, OK, beta 2 is not zero, but the the covariance between these two guys is 0, and you go, then that collapses to the same thing. Those are all special cases, but in general that is not true, OK? When you include a uh exclude a regressor in general you want to account for the possibility that the the covariance between the included and the excluded or admitted regressor could be non-zero. OK, let me not um Freestyle too much. Let me just read through my slides. So the biassed term is what you're adding on to beta one. So what I'm trying to say here is this year is the biassed term. So beta 2 times the covariance over there over the variance is the bias. That's called the omitted variance bias. That's the bias that you get from omitting X2. That bias is proportional to the covariance between the two regresses and inversely proportional to the variance of X1. What's the sign of the bias? Well, it depends on the interplay of the sign of beta 2 and the covariance between these two guys. So the bias could be positive or negative. It really depends on the signs of these. Two things, beta 2 and the covariance. The the sign of the variants of the denominator is always positive, right? It's a variance. So the only two things that can have interesting or flexible signs are beta 2 and the covariance between the two regressors. So I don't think the maths is too tricky, but if you found it annoying, then there's some intuition here. If you emit X2 from the estimation, although it should have been included. Then the estimate for beta one would be biassed, and the bias results from Um, Results from, from this line of thought. The estimator beta 1 hat is, is doing two things at the same time. First, It captures the effect that you are after. The pure effect of X1 on Y. But the estimator soaks up the effect of X2 and Y as well. Why? Because X1 is correlated with X2. Does that make sense? Does that feel right? So Beta 1 hat, the well as estimator for X1 captures the indirect effect that X2 has on Y through its covariance with X1. OK. And that's, that creates the bias. Any questions? I'm gonna run through some examples with you. How that happens a lot in regressions. Because Ultimately, the question is always, what are you not including in your regression? And the stuff that you're not including. You usually write this down. Innocently or naively as you, the error. But the question is, It's what's hidden in the error still correlated? With the regressors that you're including in your regression. If so, then you're, then you're in trouble. Then, then your estimates of the included regressors or coefficients, I should say. are not capturing the pure effects. OK. Let's run through an example, the Mozart effect. I stole that from the textbook. Tweaked it a little bit, but the idea is the same. The, the question is, do kids. Who learn to play an instrument, become more successful later in life than kids who do not learn to play an instrument. You guys probably have your own priors on this, depending on whether or not you're playing an instrument. What you're after here is whether instrument playing itself. As a As a benefit for you later in life in the labour market, I'll make your brain more flexible. I, I really don't know. I'm not an expert. I'm not a psychologist. You do not want indirect instruments of facts that that sort of capture sort of. Social privilege or pushiness of parents or aptitude of kids, that's not what you want. You're after, and when I write down this equation here, the idea is And you could go, well, instrument playing, so I'm relating it to celery. Not instrument playing, it's like you're playing an instrument at work and your boss pays you more. That's, that's not, that's not the goal, but is there something that maybe happened in your brain that helps you then later in life? I know it's a bit of a stretch, but. That's, that's the rough idea, is that what I'm saying here? So you write down this model, which looks like a simple regression, and I'm calling this error term here W, not you, to, to highlight to you that I'm thinking stuff is hiding in this error term that could be correlated with instrument playing, and that, that is a problem. And I already told you my suspects. So An instrument here, I haven't told you this, but I'm saying saying this on the side, is a dummy variable which is equal to one, if a person learned to play an instrument as a kid. So what's wrong with this estimation and I've told you already, uh, and, and one another way of framing this is the regressor whose cause of the effect you're interested in, whether instrument playing has a positive effect on salary, on your, on your, on your earnings capacity later in life. It's a choice variable. And that's usually a problem, and that happens a lot in economics or in social sciences. It's not randomly assigned. So, what I'm And and you can sort of couch this in in omitted variables bias terminology. You're omitting a lot of stuff in this regression. So going back to that regression, in the error term W there's stuff hiding that could be correlated with instrument playing. What else would you want? On the right hand side to explain salary or earnings potential, am I saying this here? Yeah. Just a second. Yeah, clicker doesn't work. It's just technology randomly breaks. Um. So Ideally You, I'm, I'm offering a bunch of um explanatory variables that you might want to add here, so a person's aptitude, ability or intelligence, the person's education or socioeconomic status. So that's the parent socioeconomic status, but Let's go with education for example. If you look for an explanatory variable that explains salaries or earnings, education is an obvious one, OK? And then why would Um, So to my right to

SPEAKER 2
a cell here. I think I, yeah, so I'm going, I'm actually explicitly

SPEAKER 1
discussing this on the next slide. Let me Let me just read through this slide, so all of these here are likely correlated with instrument playing. So they would, according to our earlier discussion, bias the result. That you obtain for beta one. The estimate, so you cannot give the estimate of beta one a causal interpretation. Instead, you know, because you're omitting all of these things that you should be including but because they are correlated with instrument playing, you're you're estimating beta one hat and you understand that it's some sort of convolution or combination of the actual effect that you're after, but also the indirect effect that all these omitted variables here aptitude, intelligence, educations, and socioeconomic status have. On earnings potential through their covariance with instruments. So let's Select one of these and um make visible how this creates bias. So if, if this really should have been the regression, now I call my error to new, which suggests there's nothing else hidden. That that should be explaining salary, salary on the left hand side, which is a. Big assumption, but let's just go with this for a second and you go. This is the the regression that you maybe should have run. You control for a person's education as well, because people with more education tend to earn more, OK? Um What bias would you get if you only regressed salary on instrument playing? Well, this was the OVB formula. Here, I'm just offering this to you again. And then the question is, What bias do you get here if you don't regress salary on both instrument playing education, but only an instrument playing? Well, the bias. Is well given by this formula, and let's study the sign, beta 2 is probably positive, more education, higher earnings on average, OK. And then the next question, and this is all sort of conjecture, I think the covariance between By two variables, instrument playing education, I would guess it's positive. You could look this up if if you have data, right? And you could look at the sample covariances. You go maybe. People who end up with more education are also more likely to have played an instrument when they were kids. It's a conjecture. It doesn't have to be like that, but you can test this and you can actually bring this to the data. If we go with that story, then the omitted were bias here. It's positive. So consequently, when you just regress salary on instruments, you are overstating the effect of instrument playing on salary. So you make the wrong conclusion that instrument playing is very beneficial for for your earnings potential when really maybe all instrument playing did was cover for education. Does that make sense? And you want to sort of separate these two effects. Remember, this is sort of what happened last week when we added the English learner percentage to the regression. The coefficient estimate on the student-teacher ratio dropped a lot. Its role shrank or diminished. Um Yeah. So, an estimation like the one just describes confuses causation with correlation, OK. It's, it's always safe to say you estimated a correlation, that's never wrong, OK? But you can't say you estimated the causal effect of instrument playing on earnings potential salary if you haven't accounted for other omitted factors. Um, so here is a good way to To, to frame or how, how, how to think about. Uncovering a causal effect and this example shows you how How difficult it would be from um what's called observational data. To estimate a causal effect, what you would need for a regression of salary on instrument playing to uncover a causal effect, you would need a research design like this here. Let's read through it, it's quite entertaining. The only way of getting the uh causal effect here of estimating a causal effect would be through a randomised controlled trial, where let's say, You choose, I'm, I'm making this sound funny, but this, this would give you a causal effect. So 10,000 babies are born in Australia, uh, in which time span that happens, and then you randomly assign 5000 of them. To have, having to learn an instrument in their childhood, and 5000 of them are not allowed to do that. And this has to be random. So you're not picking, let's say 5, 5000 babies. I don't know you were born to wealthy parents and 5000 babies who are born to unwealthy parents, however you would define that. No, you randomly assign this. You don't look at the babies at at the parents, you just randomly assign. Half of them play an instrument, half of them don't. Of course you can't do this, but this is how you would have to design an experiment. And then 40 years later, uh, you watch what they earn. And you can just look at averages. You look at average earnings of, of the group that played an instrument, and compare that to average earnings of the group that didn't play an instrument. Because instrument playing was randomly assigned, you get The causal effect. Does that make sense? That's what you would want. I mean this is an analogy to randomised controlled trials in the medical sciences where people get a treatment or a placebo, OK, and the treatment here is you play an instrument and the placebo is you don't play an instrument. Um, in randomised controlled trials, oftentimes, um, you actually don't know what your treatment is. Here you would know what your treatment is, which is a problem, but let's ignore that for a second. Um, but that is, that brings you close to uncovering a causal effect. That's where a simple regression is sufficient. You do not need to control for education in this setting because you randomised babies, so the two groups, the non-instrument players and the instrument players are identical almost in distribution on these other characteristics. Probably, OK, unless of course the instrument playing somehow makes them. Choose more education or less education whatever but. So you, you want your regressor to be as randomly assigned as possible. And that's why I said earlier, this is not a good setting because our regressor is a choice. Choices are not randomly assigned. So take you guys for example, you guys are all university students, I assume. OK. That is your choice. That means you are better people. OK, we can say this safely here, I hope, but uh. It's a choice, OK? Um. You have selected yourself into it, and it makes you different in certain aspects to other people who have not made that choice. And we don't have to make it sounding judgmental or anything like that, but it just makes you different in certain dimensions that could bias conclusions that you draw from simple regression analysis. OK, I think I've made my point and here I'm saying if we want to uncover something that is called a causal effect, then we, we need to get as closely as possible to random assignment. Is that what I'm saying here? So here the idea of a causal effect is, it's the effect that that's measured in an ideal randomised controlled experiment. It's a very non-technical definition, but I think I make my point, and I'm gonna expose you to yet another example. Um, Of what's called an observational study where Um With the, the main regressor that we're interested in or explanatory variable that we're interested in is not randomly assigned. It happens a lot in social sciences. Having said that, the field has moved towards designing and running randomised controlled trials a lot, especially in development economics,

SPEAKER 2
but also in in labour economics.

SPEAKER 1
Um, For the reason that they allow you to back out causal effects. OK. I'm saying here OK. Right, yeah, so when, when we run regressions, we always ask ourselves. Is the main regressor that I'm interested in, is it a choice variable or is it randomly assigned? Usually it's not randomly assigned. Then you go, how far away from randomly assigned is it conceptually? The closer you can argue that it's ran random, the more of a causal interpretation you can give your estimate, OK? Um. And that basically has to do linking this to the OVB story, like, what is still in your error term? What are you leaving out of your regression and how is it correlated with the stuff that you're including in the regression? Typically, there's always something hidden in the error term. That causes trouble and that sort of removes you from perfect random assignment. Um, any questions on this before I take you through another? Example Now I'm giving you an example? As prototypical in education economics. Um, in the economics literature, there's 5000 research papers, maybe 50,000 written on what's called the return to education. This is a setting Which is non-random, non-random assignment. And so it's, it's observational data, but economists have tried to understand the causal effect of education on earnings. And the, the art of this or the science of this is how. Can you uncover causality from from choice data? Let's have a look. Uh, and it, it's not an issue that has been resolved, just to, to let you know already, um, it's, it's been an important research topic, um, and there's still, um, research developing and evolving in this direction. So labour economists are interested in the so-called return to education. So that is by how much does a university degree. Increase your expected earnings or for that matter, Um A a TAFE degree or a high school degree or. A year of education, but I've tailored it towards you

SPEAKER 2
guys because you guys are university students, so the question

SPEAKER 1
could be. What's the causal effect of a university degree? What's the return To a university degree. And it's not as easy as saying just compare the earnings between university students and non-university students because these two populations are very different from each other. Um, which is to say, university students, had they not obtained a university degree, would have probably earned more anyways, because they're better people. OK, this sounds terrible now, but, uh, for in the labour market, they have attributes that, uh, in fact, thinking about it, there might be worse people in the, in the practical labour market. Like if they give you tools and you have to fix something, maybe you're not so good at this, but if you're problem solving, maybe you're better at that. But in any case, the pro the problem stems from uh you having selected yourself into university and having certain attributes um that we can't control because we're not observing them. And, let me just run through the slides, otherwise I get too distracted. So, ideally, at age 18, so this is after Secondary school, you have a choice. Go get a job and this is simplified, right? Go get a job and earn money for the rest of your life. Don't take any interruptions. Um, Or go to university, increase your human capital. That's what happens here in this room. And After that, go get a job and work for the rest of your life. That, that's the model world. Um, so in this model, a university is like a bank. You take your human capital. Receive a positive annual rate of return here in this lecture, OK. And um you're right, and then after this lecture, you take your exams, whatever, you graduate and then you go into the labour market and receive. Whatever earnings you're getting. Estimating the return to education seems so easy. Just compare earnings of university graduates to those of high school graduates, and I've told you already that that's not the right idea. labour economists have been obsessing about this equation in various iterations versions quite a bit, but that's sort of the the main estimation. There is data on earnings. There is data on education and work experience that means. Have you worked for 5 years, 10 years, 20 years? Work experience gets rewarded in the labour market as well, OK? Um, to a point, so you, you could run this regression, but then you always ask yourself what's still in the error term that explains earnings that that is not covered by education and experience. But first of all, before we discuss that, let's run this regression. In Australia, a good data set to run this regression is the. Household income and labour dynamics in Australia, panel data set, Hilda, have you heard of this? Have you participated in it? I've got a colleague somewhere in Queensland who, who is, who was captured by Hilda. Captured really means captured because they re-interview every year. Maybe now it's every other year I forgot, but initially when they started in 2001, every year, they interview the same people and their offshoots, like. If you start a family, um, they'll ask you about your children's, whatever, every year, um, and you've got data sets like this in every major developed country, and Hilda's is a pretty good one, and it captures information on, well, on these variables. So you can run this regression, but much more as well. But for that matter. We take the Hilde data, run this regression, and this is what I get. And, and, and I should tell you what I'm actually regressing with, we'll cover this next week is log hourly wage, which is um a measure of earnings potential. OK? So As, as, as a worker, you don't have to be a worker. You could be an academic at university. You can report a wage, right?

SPEAKER 2
I don't know, or they would calculate this for you or whatever.

SPEAKER 1
And then you, but the point that I want to make here is not so much that it is about wage, but I'm logging this. I'm taking the logarithm, which allows me to interpret the right hand of the coefficient estimates as uh semi-elasticity. Let's have a look what I mean by that, and we'll, we'll cover that next week. Just as a preview, the regression that I'm running gives me a beta 1 hat of 0.0744, which means That an additional year of educational attainment increases. Hourly wage, which is a measure of earnings potential, by 7.4%. That's the interpretation. It's a percentage interpretation. That's what the logging of the dependent vehicle allows me to do. I like the percent interpretation because you then can compare that to what the capital market offers you. If you could take your human capital to the bank and say, grow my human capital, which you can't do, um, Westpac. Offers you 1% currently, OK? Um And even in high interest rate times, they don't

SPEAKER 2
offer near 7%.

SPEAKER 1
Even the stock market, currently, definitely not the stock market. OK. But uh in the 2010s, the stock market didn't offer this to you. This is a very cheap back of the envelope argument here. Which, which uh university lecturer should be making is you're doing a good investment if only I could interpret this. In a causal way we haven't discussed the non-causality yet, right? But let's say, let's believe this for a second, then you have made a great decision sitting in this class because your human capital increases continuously at 7.4% every second, OK. That's not right, quite true. But uh, you know, it's the annual rate of return, so you have to divide this by. How many seconds there are in a year, but, but you, your human capital increases very smoothly. Um, at an annual rate of 7.4%, this is what this regression says. And by the way, a year of work experience offers a very small return, and I'm, I'm so everything seems highly significant here, so that's, that's good, but I'm more interested in in interpreting the point estimate. OK. So congratulations. Good job going to university here. But, of course, this is a discussion on omitted variables bias. What are we, oops, it's 2:55. Let me just uh wrap up this slide. Um, what are we omitting here? Um, labour economists think that there's A lot omitted here. And the main culprit, the, the way it's framed in like 5000 different research papers and 500 different textbooks. is ability or intelligence or aptitude. OK, so earnings depend on, let's just call it ability, whatever that means. Earnings depend on your education, on your work experience, but also maybe on your ability. OK, but at the same time, if it's some measure of aptitude or skill or did I say intelligence depends on is correlated with education as well. A more intelligent people also tend to choose higher education levels. So then with that story you would probably be overestimating beta one unless you. Can account for unobserved factors. I'll continue with this thought um after a little break.

SPEAKER 2
So let's continue at what time do we continue at

SPEAKER 1
50.

SPEAKER 4
A little bit confused saying this method is problematic, you just simply compare the earning of uh graduates from university and the earning of.

SPEAKER 1
Sorry, so. Just comparing the. Average earnings between these two groups.

SPEAKER 2
Ignore the fact that these groups don't just differ in the university or in the education levels, but also in

SPEAKER 1
unobserved factors. And so this is like exactly the omitted variables argument.

SPEAKER 2
So, uh, to connect this to this here, the The

SPEAKER 1
group of university graduates on average includes Cleverer people maybe let's go with that story right so then. These people would earn more even if they didn't.

SPEAKER 2
Go to university. So then you're sort of overstating the effect of the university. Do you, does that make sense?

SPEAKER 1
So this is exactly the, the problem of the simple

SPEAKER 2
regression is that it doesn't separate out other unobserved effects. So here we would hope, think that university graduates.

SPEAKER 1
Would have higher earnings. Even had they, if they hadn't gone to university, and there's a big if, right, but that's how labour economists

SPEAKER 2
frame this?

SPEAKER 1
Does it sort of makes sense.

SPEAKER 3
Just a question about um.

SPEAKER 5
Whether or not things like aggregation in subgroups that affect buyers because the thing I'm. If we could say that education is causally effective. Is it fair to say that because we're not including the type of education that the education major is biassed or um years or just like? An economist That was the scientist or. Would it be fair to say that the beta one is biassed or is it just that it's aggregated?

SPEAKER 3
Yeah, that's the the retation I would go with. It's Yeah, it is an average return for The population You can then you can look closer. competition on this guy. He studies of physics, engineering, economist, history, you can with rich data, you can.

SPEAKER 2
All you On the sub sample of university graduate.

SPEAKER 3
But aggression Subject I don't not You could, but that's

SPEAKER 5
my, yeah, I mean.

SPEAKER 3
Let's do that. If the research question is And the question is. What's the value of particular discipline or degree subject? I think we are positioning our head. If you want to richer study I wanted to go back to that idea. I just instructed the university graduate to go let's turn to a science degree. The RCB or even the closer distinction, but they still If we just go with the binary. Science No What type of person it's a choice again, right. wanted it to be The first so. Just pass and go on. of earnings on Degree And the original data. Then use the a zone. Is there something systematic of things. The choice sons your journalists would have probably been better. So but I, I know. But OK, we're back.

SPEAKER 1
Any questions so far? Uh Now Um, in this, in this regression, again, this is a regression that labour economists have obsessed about since

SPEAKER 2
the 1950s, and this is the 1950s, 1960s or 1970s,

SPEAKER 1
still. struggling with it. And why is that generically we think there's stuff hidden in the error term that's correlated with education and a non-judgmental way of putting this is there's something people who have obtained or chosen a higher education level would have earned. Differently, uh, how is it, yeah, it's not a good

SPEAKER 2
way of saying this.

SPEAKER 1
Yeah, I would say it. In a way that puts people who choose a higher education level in a better light. If you had chosen not to go to university, your earnings would have been higher anyways. That's that's the the line of thought here. You would have had better outcomes anyways, OK. Or this is to say, if I could randomly allocate people to a university degree and to a high school degree. And what do I want to say? Um, and yes, I would expect, I would hope that the university degree has a positive effect, but in the data people are not randomly allocated, um, and they are sort of, um, it's called counterfactual, the counterfactual, had they not chosen the university degree, would have still been a better outcome. Relative to people who choose not to go to university.

SPEAKER 2
Does that make sense?

SPEAKER 1
Um. At least you want to account for that possibility. If you go with the story and the way that's framed, if you read your standard mainstream textbook, is what's hiding in here is this weird abstract term ability which could capture your skill level, your effort level, your intelligence. Your ability, and that is positively correlated with earnings. OK, higher ability, higher earnings, hopefully that's rewarded in the labour market, but higher ability also means you're probably more able to go to university or to obtain more education. OK. If you and at the same time, I should say data sets such as HILDA do not contain measures of ability. Because it's such a weird, opaque, abstract notion. Like, you can't ask a person, what's your ability? They won't say. Is that a question? Say that again. Yeah, yeah, um, proxies have been used like IQ, but they come with their own problems. Interestingly, you'd go, oh this sounds like a simple solution. I just proxy it with something. Um, but turns out the proxies can make the story worse if the proxies are bad, like what the person's ability, uh, IQ, um, but they could mitigate. These impacts, but proxy solutions are available and it's like

SPEAKER 2
a whole separate discussion that we could have, and it's definitely one direction one could go to, but here if

SPEAKER 1
we if we go with my story that there's something hiding in the error term that positively influences earnings, that means its beta is positive. But it's also positively correlated with education. That's like in the previous example, we are overstating the effect of education on earnings, unless we could control for this unobserved stuff. So here education has to do two jobs. I do believe that education does have a positive effect. The direct sort of positive causal effect that education has on earnings, but there's also They could increase the human capital. They, education is also a positive effect, because it's correlated with unobserved ability and you want to sort of philtre that out. OK. All right. Now, there is um. Econometric methods to deal with this. One is proxy variables. Um, another one, I'm not naming this series called Instrumental Variables, which you would learn about, excuse me. In subsequent econometrics courses. Which, uh, a paper by Andrew Lee and Chris Ryan. Published and using Hilda published in the Economics of Education Review in 2008, have have done, I say slightly more sophisticated econometric analysis is quite a lot more sophisticated, and what they do is, let me think, yeah, they, they run a multiple regression model and estimate a return to education of 13%. So they're basically taking this one here, this regression here. And throwing in more regressors. Interestingly, they obtained a point estimate of 13% so it pulls the regressor up and we said that if we could control for for ability for unobserved factors, I would guess my effect estimate should go down. That was we're thinking that this one here overstates the effect of educational earnings. So that that also shows you why this is such a, not a minefield, but why, why is there such a puzzle in in education economics to uncover the causal effect. Like you throw in more regressors, the effect, the estimate actually goes up. It's a bit weird. Then they go, OK, maybe just adding regressors and running or less is not the best. Way of dealing with OVB because there's still stuff that is unobserved. They use other um statistical econometric techniques, um, and they end up with an estimate of 10%. So I'm not giving you sort of a Clear solution or clear answer to what really is the cause and effect of education on earnings. I would say education economists would say anything between 0 and 15%, but the question is what is the number? It's it's positive, but is it non-zero and is it competitive relative to the capital market, for example, and it's still an open research question OK and. Ideally, you would randomly allocate education, but you can't um. Do that, yeah, here, here I'm saying, so what, what you would have to do is randomly allocate education obviously you can't do that, OK. Any questions? Then I've got two very dry topics now to run through, but we'll have to do it quickly, and then

SPEAKER 2
we have a very short discussion workshop section.

SPEAKER 1
So Two topics that that are very separate from what we've just discussed. Let's have a look. The French war theorem, whoa, war, I don't know how to say it, um. And that's this. It's a bit odd. And if you don't like it, just ignore it. I you can't. I think it's part of the assignment. But the assignment, I think talks you through it, and I'm not 100% sure anymore if it's really part of

SPEAKER 2
the assignment. I might have taken it out.

SPEAKER 1
Um, And this is how it goes. I struggle With it's just justifying why I'm including it in the lecture, but I, let's see. You, you tell me if it, it helps, helps you understand or less estimation or not, or if it just makes things worse. It's like this. Let's just read through this together. Let's say the model is just this multiple regression with K regressors. And, and so what you would do is to, to estimate your betas is apply OLS. We've defined the estimator. In Python, you run the regression of Y on the K regressors. Now, Comes this funny theorem that. That, that, that we read through regression in 3 steps. Let's follow the 3 steps and see what it gets us. Regress Regressor one On all the other regressors. It's a bit odd, you're regressing regressors against each other. But you can, right? You're using X1 as the dependent variable, and you regress it on all the other regressors, X23 XK. In step 2, you regress, oh sorry, step 1 wasn't finished. In that regression where X1 is a dependent variable, so I'm back to step one, you regress X1 on all the other regressors and you obtain the residual of that regression. And call that residual X1 tilda. You can do that. The question is, why would you do that? And we, we talked through this. Step 2. In step 2, you request your dependent variable and all the regressors but X1. And obtain the residual from that regression. And step 3, you regress the two residuals against each other. Mechanically you can do that and what this thing says, what this theorem says. You're running a simple regression of These two residuals, white tilde against X1 tilde, and this is a simple regression now. You should include a constant. By saying that The, the OLS estimate in that simple regression that you obtain for the slope. Core insights. With the coefficient estimate that you would have obtained. Had you run the regression as you would have done it before you have seen this theorem, just in Python, just run the regression of Y on the whole set of regressors and obtain and single out your beta one hat. That numerically is identical to the slope coefficient that you obtain in this weird regression where you run the two residuals against against each other. So first, this is not a theorem that gives you a new way of running regressions. That's not the point of it. You will always run your multiple regression like we have done it today and last week. You just regress why on the full set of regressess. This here may offer you an additional insight conceptually, theoretically what multiple regression does. So this is not. A recipe for how you can alternatively run your aggression or this is just For some of you an insight in, in what multiple regression does. And I'm trying to offer you that insight now, and I struggle with it historically, but let's, let's see, I, I try to do my best job. So what's happening here is If I run this regression here and I obtain my K+1 OLS estimates and I write down the OLS estimate for beta one, that number is exactly the same as the one that I'm getting out of this complicated procedure. Why is that? Why is this complicated procedure obtaining the same? What's happening in this complicated procedure is this. In the first step, you're creating a version of X1 that is separated or removed from all the influence of the other regressors. That guy is called X1 Tilda. In the second step, you create a version of X2 that is completely removed. Netted out, partialed out from the effects of all the other regressors X2 through XK. So in a way, All that's left is variation in X1, and that's what you're regressing on, on each other there. The part of the part of Y that's related to X1, and the part of X1, that's not related to the other regressors. You you relate these two, you obtain. The same coefficient estimate. So that's sort of one short way of explaining this. Let me read through my slides and hope for the best that it makes things clear or not. In the first two steps, you generate versions of X1 and Y that are purged or free from any correlation with the covariants X2 through XK. X1 tilda, that weird residual in the first stage. Except captures all the variation in X1 that is uncorrelated with X2 through XK. So you can view Xtilda 1 as a version of X1, from which the effects of X2 through XA have been partialed or netted out. And likewise for white, white children. So when you then regress Y tilt against X1 till then step 3, you therefore obtain an estimate that captures the true effect of X1 and Y in which any of the correlation to the other aggressors is shut off.

SPEAKER 2
Or fixed This gives you sort of another angle of

SPEAKER 1
how How we think of a coefficient estimate and the holding everything constant is um. As sort of explained by this procedure, it's like. You're really isolating the effect of a variable in this case X1, on the dependent variable, shutting off any weird correlations that X1 could have on the dependent variable through its relationship with the other regressors. And this is Symmetric to I mean I could have shown you this previous slide, singling out X7, for example, or any of the other Xs. OK. So instead of focusing here on X1, I could have said regress X7 on all the other regressors. Regress why on all the other regressors except X7 and what you're getting is an estimate of beta 7. That numerically is identical to the one that you obtain, would obtain in the multiple regression for beta 7, OK? And not only for the 7th 1, for all the other ones. So all this is to say that multiple regression is successful in shutting down the effects of the other regressors. And that's just another perspective on this. I'm not giving you a mathematical derivation. I will never ask you for one, so don't worry about that. The only case where you will see this is possibly in the assignment where you can basically convince yourself that that actually works. And like I said, I don't even remember if I'm throwing this into the assignment, so let me look when I post it, OK. And then, um, as, as a random piece of, of knowledge, let's say if it's a true false question in the, in the exam, I asked you. Something along these lines, is it true or false, then you can say yes, it's true by the Fri war theorem, but no deeper than that. Other than that, my only hope is that it sort of gives you slightly a different angle on what multiple regression does. Any questions on this?

SPEAKER 3
Why is like With regression Here.

SPEAKER 1
So when you, when you regress, um, what do you do in the first step, you, you regress, regress X1 on X2 through XK. We're looking at the residual. The residual is the power of X1 that has nothing to do with X2 through XK. That's what I mean. You, you You're creating a version of X1. That is really just X1. With all the influence of the X2, 34, and K removed. That's what I mean by that. And um if you read in the book, textbook, I think they call it partialing out the influence of the other regressors or netting it out, purging it, removing it. That's, that's what happens here technically, um, and so, all, all this is saying in a way is that implicitly. Multiple regression does this for you. Which is quite cool and does it for you, for all the regressors. So the, when you get a coefficient estimate for one of your K regressors. Or coefficients, the interpretation really is the pure unencumbered effect that that regressor has on the dependent variable. It's not the effect that this regressor has on the dependent variable through its correlation with the other regressors. Now that's, that's removed. That's exactly what this says here. OK. And that's also what you want. By And, and maybe this was obvious to you, OK, but I, I thought I'll mention it yet again. I do acknowledge that this can be confusing, but I. Um, I think I Um Race this as an issue, you are aware of it that it could be confusing. I try my best, but um, have a read in the, in the book if if that helps you at all. And it can be shown technically, but you can show it on the computer by just following these steps and convincing yourself that's actually the case. And then a quick one here, measures of fit. Just a quick run through, we have to tweak our R squared here when we do multiple regression analysis. And this is how it works. So mostly the next 3 slides are copy and paste from several weeks ago. And I'll point out to you where I made changes. So here we still talk about R squared and the standard error of the regression. We've seen exactly this slide before, no changes because the symbols. general enough they also apply to multiple regressions. So for example, if we talk about the ESS, the explained sum of squared, it's still the same formula from several weeks ago when we did simple regression analysis. The hat, of course, is based on the multiple regression model now, but the formula is the same. So then my R squared is the same. Same formula And so this slide is almost the same. So we do have the extreme case, R squared is 0. If the ESS is 0, if you're not explaining anything. In this case, with your regresses, which is even more unlikely. But that's, that's the corner case when your regressors are completely useless. Um, and R squad is one, when your regressors explain all the variation in the dependent variable. Um, so we're still bounded by 0 and 1 with our R square. Now, the last bullet point is new. As a mechanical fact or feature. I think this sounds persuasive and we're not proving it. Next statement is, if you add a regressor, To your model, the ESS. Can not go down. You can't explain less by throwing in more. Does that make sense? Would everyone believe that? I think it's almost trivial, almost, OK. So, if you move from a simpler regression model to a model where you add another regressor, the ESS cannot go down. You cannot explain less because you still have your original regressor in the model. Or conversely, the RSS goes down. Therefore, this is econometrics. But Um, The ice as it goes down. So, on that formula here, yeah, I, uh, 1 minus RSS over TSS goes up. OK. Should I, should I tell him about the rate of return? Was it 7.4%. Um, Well, maybe he's not an economist. Um, OK, so technically you can game the R squared. You just throw in regresses. That's not good. We don't want this to be possible. OK. So we tweak the concept of Rsquared and how do we tweak it? We put in a cost or a price for throwing in additional regresses. Where do we do this on this slide? Down here, it's hiding in K. I'm, I'm making it costly. To add a regressor. Why? So we said the ISS goes down. If you, if your UK increases, but the whole thing in front of it goes up. And then you don't really know what's the net effect. There's the potential. For the R squared, sorry, this thing is called the adjusted Rsquared to go up or down now. That's good. So, at least the possibility of gaining the R2d measure is not Um, so easy anymore. Having said that, most, most econ economicticians won't allow you

SPEAKER 2
to game anyways, but, uh, from experience.

SPEAKER 1
Also, I should say the R square plays a much

SPEAKER 2
smaller role in econometrics than it does in statistics.

SPEAKER 1
Never mention never that never mind I'm mentioning it here. So this thing is called adjusted as. So it's, it has a bar on top of it, it, I don't know if you see this. Um, so when we run multiple regressions, This is what you want to report if someone asks you what's your R squared. They might not say what's your adjusted R squared, but it's implicit, you tell them your um adjusted R squared. So this, this thing doesn't necessarily increase when you add regressors, and interestingly, it could also be negative, but it's just a theoretical possibility. Um, and then the standard error of the regression, I don't remember actually how we defined it. Last time, but this is the, the extension, it's just

SPEAKER 2
the sum of great residuals, and then you, you put

SPEAKER 1
in a K here. Um, Yeah Not too. Oh, it's not just the sum of square residuals, it's the square root of it.

SPEAKER 2
OK.

SPEAKER 1
All right. Any questions? So the R squared or the adjusted R squared, it's, it's the more important. Um Measure. Just a second, uh, more important measure, but um, I'm telling you this year anyways, because you find it in in textbooks. But uh I'm much more familiar with people telling you what they are squares are. Yeah, your question? What Say that. What, what are N and K? Oh, sorry about that. Let's go to R square. I should have told you, right? N is the sample size, and K.

SPEAKER 2
Is the number of Slope coefficients that you have.

SPEAKER 1
Is this, we've got X1, X2 all the way through XK. It's that K. It's the number of regressors that you're including. Sorry about that. Yeah. So that's what I mean by by K. Changing K has two effects. Let's say increasing K has two effects. Increasing K, meaning you throw in additional regressors, has two effects. This whole factor here goes up. Because this goes, K goes up, but it's negative and it's in the denominator, OK? And RSS goes down. So opposing directions and then. You don't know which direction it goes depends on your N and your K and what does happen to your RSS. It's not that it will wildly fluctuate from experience, OK, but um. This has this property that You can game it. That Any other questions?

SPEAKER 2
Yeah. I, I wouldn't, uh.

SPEAKER 1
It's that, uh, is when you're literally not explaining much, and the, the interplay between RSS and the sort of the punishment factor that that you're plugging in the the the the vision by K there at the bottom, um, happens to drive it down into the negative range. I think it literally means. It, it is sort of means zero. OK. Cool So, the next week, we'll wrap up. Uh, multiple regression. I've got a few other topics to cover. And then in week 10, we start with um auto regressions and time series analysis. So that's the direction that we're going in the lecture. Um, anything else of interest? Any other housekeeping things that you want to discuss, then we have a relatively Um What's this Easy workshop session today. I didn't even bring my iPad because I don't plan

SPEAKER 2
to write anything. I just want to talk.

SPEAKER 1
I updated the workshop session this morning. I didn't like the one that was there before. Can you guys read this? Should I zoom in? You can read That I it's, it's big enough. It's just a A discussion And, and then we can all go our many ways. So this is an omitted variables bias during this, so many like this, like every day in the news or whatever you can read stuff like that. Is the Mediterranean diet good for you? Should you have a glass of wine every day? Um, ideally in the mornings, I don't know. Um, should you eat chocolate? Should you should you smoke, that's not a good one. But um. Is daily exercise good for you? Well, of course it is, but the people who choose to daily exercise are better people, OK. It's not me, not me. OK. But this is, this, it's always the same story, right? And you see how this has to do with causality, or many variables bias, and whether OS assumption one is satisfied or not. So that's the whole interplay here. So another one is this one that I, I think is inspired by true events. I think I saw a study like this before and I sort of. Made it into sort of a course. I gave it a course representation and made it sort

SPEAKER 2
of a discussion section for today's workshop.

SPEAKER 1
And here's how the story goes. In a recent study, a recent study found that the death rate for people who typically sleep fewer than 7 hours per night is 5% points higher than for people who sleep more than 7 hours, so you split the

SPEAKER 2
population into these two subgroups.

SPEAKER 1
The 1.1 million observations, which is to say you have a lot of observations which you go, Oh, that's good. But a lot of observations does not protect you from making the wrong inference. OK, that's unfortunately true. Just because you have more than a million observations doesn't mean that you're interpreting stuff all wrong, but let's see how we interpret stuff. The 1.1 million observations used for this study came from a random survey of Australians aged 30 to 102. So this is like almost census data, OK. Um, each survey respondent was tracked for 4 years. Sleeping patterns or mortality outcomes were observed over that 4 year period. So presumably, You were asked how much do you typically sleep? Never mind biassed responses. It's not as bad as saying how many, how much do you smoke? I, I don't smoke. Um when you do smoke here, maybe it's. Let's bite. Let's let's ignore, well, we, we can talk about anything here, but that's, that's not the main problem of this exercise. Um, but based on this brief summary, would you recommend that Australians who sleep fewer than 7 hours per night should try sleep more? Discuss who wants to go first? What's, what's the problem here? And anything goes. Any volunteers there.

SPEAKER 4
other things causing the deaths than just your sleep. You can't just.

SPEAKER 1
Yeah. Now, what are these other things and and anyone?

SPEAKER 3
I think I guess it's all Yeah, so this is

SPEAKER 1
this is exactly my main argument. So and we can discuss several other factors, but that is sort of, if I give this to you in the, in the final exam, I would go, and, and this is also how, if you see how this is phrased, 30 to 100 to year. All the people, and this is now not a controversial statement, tend to sleep less. They also tend to die more. It's true. So that, you're picking that up, right? And that's sort of end of the exercise. Um, but I would also go with you go now. If you, if you're in a group of people who sleep less than 7 hours. Um, uh, I guess the, the deeper question is, What, what do you want to uncover here with this exercise? It's like a deeper change in sort of what the cells of the body can do if they can recover from more sleep and sort of the quality, I don't, I'm not a biologist or what should I be a molecular, what is it called biologist who can say more sleep. Makes your cells recover or makes you healthy or whatever and and therefore live longer or reduces your probability to die. Or is this here? Well, if you sleep less, You're more accident prone, perhaps. OK. You don't check the road when you cross, when you cross the road, you get in accidents more. So the separating these, these effects. would be important right by just comparing these two. Two groups you are controlling for things uh that are correlated with sleep and with mortality outcomes and that you ideally want to separate and then the bigger question is, What's your, what's your research objective here anyways? What, what, what do you want? The causal effect of, of sleeping? What is it? That sleep has some sort of biological benefits or whether it has Benefits on How you can spend your everyday life, pay attention to, to the traffic when you cross the road or when you're driving.

SPEAKER 3
Also theoretically couldn't poor health cause poor sleep.

SPEAKER 1
That's true, so you could Of be of poor health, let's say you have chronic back pain. Um, you get 5 hours of sleep only. Um, OK, I don't know if you die from chronic back pain. Well, it's a, it's an indicator for, for poor health. I mean you've got other issues, maybe.

SPEAKER 2
OK. Yeah, so a lot goes, and this is a typical

SPEAKER 1
exercise that I could just dump on you in an exam and go discuss, and then we'd be looking for any reasonable explanation. We would not be looking for an exhaustive discussion because it's sort of never ending. But you really raised my main point, and that's also the way this question is structured is well. Yeah, older people sleepless and die more. But that's what you're picking up, OK? So the true effect of sleep. Um, or more than 7 hours sleep on mortality could be 0, could be 0, but you're picking up a positive effect. Um, because of the spurious correlation, OK. And like I said, You see stories like this all the time. Like, um, you take, um, what is it these, these diets, uh, where you don't eat for 14 hours or something, what are they called um time delayed, what are they called? Fasting, intermittent fasting, right. I'm not dismissing it, but I'm saying. People who choose to intermittently fast are systematically different to people who don't, so if you could just compare these two groups, that's not sufficient. Uh, you need to control the underlying, uh, you need to control for the systematic differences, um, which oftentimes you don't observe. OK. Anyway, I think I've made my point, I don't want to keep you any longer. Do you have any other questions? I think that's sort of what makes regression interesting. It can be such a mechanical and Mathematical topic, but the, the art of interpreting your regression is actually quite

SPEAKER 2
important to and understanding the limitations of it, and that's

SPEAKER 1
sort of what we're learning today. All right, let me stop talking. It's another long weekend, ANZAC Day, so I shouldn't say enjoy. Um, have a, have a solemn Anzac Day weekend, and I, I see you next week.

SPEAKER 6
not related to the course but to you is that more just like like an econometrics.

SPEAKER 3
Do you know what?

SPEAKER 2
I think yeah.

SPEAKER 1
So he's more of a theorist but.

SPEAKER 2
It should run.

SPEAKER 3
In a little bit of a consumer friendly way.

SPEAKER 2
Which I would guess he's doing.

SPEAKER 1
Um, if, if I see him he's in my corridor, I'll ask him how he runs so far.

SPEAKER 2
I'm pretty sure he's got computer labs as well, and the idea is to make it sort of the add on to this course.

SPEAKER 3
This used to be called 2008 is 2007, so it's

SPEAKER 2
just signalling to you that they belong together, but over

SPEAKER 1
time can always separate, but I don't think it's a

SPEAKER 6
very theoretical course and it takes the stuff you instrumental variables dealing with causality and stuff like that and it was like one of the applied.

SPEAKER 2
Yeah, right, that's 31 that while the applied micro is applied for for sure, right, um, I can't say yeah I would just recommend. If you can at the beginning of the semester attend both lectures, the tutorials. I know it's a bit of a nuisance. See what It Um, but I, I would think that

SPEAKER 3
34 is also relatively applied, but it doesn't strictly speaking,

SPEAKER 1
have to be because it's not in its in it.

SPEAKER 2
So let's have a look.

SPEAKER 1
OK, and last thing for um like like the econometrics

SPEAKER 6
courses, do they just like if you've done this, you don't need to do like the basic like introductory one, do you? Yeah.

SPEAKER 2
But you would have taken to the.

SPEAKER 3
it's not a prerequisite.

SPEAKER 1
2007. I mean, but it's a pre-re for for the BX,

SPEAKER 3
right? I'm not. I see, so.

SPEAKER 2
Well. So I, I do have in my graduate course this one here.

SPEAKER 3
I have two other students and I've had honours students

SPEAKER 2
in the past difficult course here um and we would expect that any of our honour students has at least taken this one here. Well, all the other econometrics courses are not compulsory.

SPEAKER 1
As an econometrician, I would like them to have more. I think most of them will actually have more, but

SPEAKER 2
it's not expected if you're asking about that. Um, it's also not they will not force you into

SPEAKER 1
this course.

SPEAKER 2
want to take. I think they build and Schedule with you which courses to take. I do know many other students who do not take my my graduate degrees.

SPEAKER 6
Is it a theory? Yeah, OK.

SPEAKER 1
You can have a look at not easy.

SPEAKER 2
Um, it's, it's at the high level, yeah, it's mostly for PhD students.

SPEAKER 1
But from experience, the few honour students that I get

SPEAKER 2
are usually at the top.

SPEAKER 1
Are you playing with the idea of doing honours? You have to, it's. How does that work? What's your degree?

SPEAKER 2
And honours in what?

SPEAKER 1
Oh cool.

SPEAKER 2
OK, well that makes, I don't know how it works.

SPEAKER 1
So when would that be next year or next year, but it's good that you ask. Cool have a good week.
