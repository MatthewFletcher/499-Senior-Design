# Statistical Analyzer: Test Data Files

Three test data files have been generated for testing the Statistical Analyzer.  One contains frequency data, one contains ordinal data, and one contains interval data.  A description of the contents of each is given below.

# Frequency Data

## File name: FrequencyDataTest.csv
## Data description: The data represents the results of counting the frequency of occurrence of seven sample events (labeled Sample 1 through Sample 7).  An expected frequency and an actual measured frequency are given for each sample.
## File format: Comma separated.  Line 1 gives the column headers as “Sample #”, “Expected Freq.”, and “Actual Freq.”  Each line contains three columns giving in order: (1) a string naming the sample, i.e. “Sample 1”, (2) an integer giving the expected frequency, and (3) an integer giving the actual measured frequency.


# Ordinal Data

## File name: OrdinalDataTest.csv
## Data description: The data represents the results of a 50-item questionnaire given to 100 respondents.  Each question can have one of 5 possible answers: 1=Strongly disagree, 2=Disagree, 3=Neutral, 4=Agree, 5=Strongly agree.  The data show the compilation of the number of respondants answering each question with each answer.
## File format: Comma separated.  Line 1 gives the column headers as “Question #”, “SD”, “D”, “N”, “A”, and “SA”  Each line contains six columns. The first column contains a string giving the question number, i.e. “Question 1”. The remaining columns (2-6) give respectively the number of respondents answering Strongly disagree, Disagree, Neutral, Agree, or Strongly agree for that question.


# Interval Data

## File name: IntervalDataTest.csv
## Data description: The data represents the results of a pre- and post-test experiment conducted with 100 subjects.  The data give the scored made on a standardized test before participating in the experimental training session and after the training.
## File format: Comma separated.  Line 1 gives the column headers as “Subject ID”, “Pretest”, and “Posttest”  Each line contains three columns. Column 1 contains a string identifying the subject, i.e. “Subject000”.  Column 2 contains an integer giving the subject’s pretest score.  Column 3 contains an integer giving the subject’s posttest score.


