#!/usr/bin/python
# -*- coding: UTF-8 -*-

import nltk
from textanalyzer import *
import readabilitytests

#print nltk.corpus.brown.words()

#text = """
#Welcome to Disney Channel, please explore the site to find out
#about the great shows on Disney Channel. Why not check out the
#TV guide to find out what's on, or see what great prizes can be
#won in competitions. You might also want to look at younger
#childrens programmes on Playhouse Disney, or see classic episodes
#on Toon Disney.
#"""

text = """Denne boken er en veiledning til og referanse for programmeringsspråket Ruby. Bruk Ruby og du vil skrive bedre kode, være mer produktiv og ha det mer moro når du programmerer.

Dette er vågale påstander, men vi mener at du vil si deg enig i dem, etter å ha lest denne boka. Vi kan nemlig støtte oss på erfaring når vi sier dette.

I vår rolle som Pragmatiske Programmerere har vi prøvd haugevis av språk i vår søken etter verktøy som gjør hverdagen enklere og hjelper oss til å gjøre en bedre jobb. Men inntill nå har vi alltid blitt frustrert av språkene vi brukte.

Vårt arbeid består i å løse problemer, ikke i å mate kompilatorer, så vi liker dynamiske språk som kan tilpasse seg til oss og ikke har vilkårlige, rigide regler. Vi trenger klarhet i koden slik at vi kan bruke den til å kommunisere med. Vi verdsetter kortfattethet og muligheten for å uttrykke et krav i kode på en nøyaktig og effektiv måte. Jo mindre kode vi trenger å skrive, jo mindre ting som kan gå galt. (Også blir det mindre belastning på håndledd og fingre.)

Vi ønsker å være så produktive som mulig, og derfor vil vi at koden skal kjøre med en gang; tid brukt inne i avlusingsverktøy (debugger) stjeles fra tiden vi har til å drive utvikling. En annen ting som hjelper er hvis vi kan prøve ut koden mens vi endrer den; for hvis du må vente for en to timer lang kompilerings- og lenkingssyklus, ja da kan du like godt bruke hullkort og levere arbeidet ditt i en bunke og vente på til neste kompilering kjøres.

Vi ønsker et språk med et høyt abstraksjonsnivå. Jo mer høynivå språket er, jo mindre tid trenger vi på å oversette våre krav til kode.

Da vi oppdaget Ruby innså vi at vår søken var over. I høyere grad enn noe annet språk vi har arbeidet med, så unngår Ruby å gå i veien for arbeidet. Du kan konsentere deg om å løse problemet foran deg, i stedet for å knote med kompilatoren eller språket. Det er dette som gjør at Ruby kan hjelpe deg med å bli en bedre programmerer: ved å gi deg mulighet til å bruke mer av tiden til å løse problemer for brukerne dine, og ikke kompilatoren."""


text2 = """This book is a tutorial and reference for the Ruby programming language. Use Ruby, and you'll write better code, be more productive, and enjoy programming more.

These are bold claims, but we think that after reading this book you'll agree with them. And we have the experience to back up this belief.

As Pragmatic Programmers we've tried many, many languages in our search for tools to make our lives easier, for tools to help us do our jobs better. Until now, though, we'd always been frustrated by the languages we were using.

Our job is to solve problems, not spoonfeed compilers, so we like dynamic languages that adapt to us, without arbitrary, rigid rules. We need clarity so we can communicate using our code. We value conciseness and the ability to express a requirement in code accurately and efficiently. The less code we write, the less that can go wrong. (And our wrists and fingers are thankful, too.)

We want to be as productive as possible, so we want our code to run the first time; time spent in the debugger is time stolen from the development clock. It also helps if we can try out code as we edit it; if you have to wait for a 2-hour make cycle, you may as well be using punch cards and submitting your work for batch compilation.

We want a language that works at a high level of abstraction. The higher level the language, the less time we spend translating our requirements into code.

When we discovered Ruby, we realized that we'd found what we'd been looking for. More than any other language with which we have worked, Ruby stays out of your way. You can concentrate on solving the problem at hand, instead of struggling with compiler and language issues. That's how it can help you become a better programmer: by giving you the chance to spend your time creating solutions for your users, not for the compiler."""
#t = textanalyzer("no")
#t.analyzeText(text)
readabilitytests.ReadabilityTool().getReportAll(text)
#lang = "eng"
#t.setLang("eng")
#t.analyzeText(text2)
readabilitytests.ReadabilityTool().getReportAll(text2)                                  
