from textblob import TextBlob

words = input("Enter Any Words to CHECK spelling:")

print("incorrect Word:", words)

correct=TextBlob(words)

print("Correct Words:", correct.correct())





