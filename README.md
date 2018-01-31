The objective is to obtain some statistics about user behavior in an online forum.

1. Find for each student what is the hour during which the student has posted the most posts.
Files: StudentTimes-mapper.py and StudentTimes-reducer.py
       StudentTimes-part-00000 (output results file)

2. Process the forum data and output the length of the post and the average answer (just answer, not comment) length for each post.
Files: PostAnswerLength-mapper.py and PostAnswerLength-reducer.py
       PostAnswerLength-part-00000 (output results file)

3. Output Top 10 tags, ordered by the number of questions they appear in.
Files: TopTags-mapper.py and TopTags-reducer.py
       TopTags-part-00000 (output results file)

4. For each forum thread (that is a question node with all it's answers and comments) find a list of students that have posted there - either asked the question, answered a question or added a comment.
Files: StudyGroups-mapper.py and StudyGroups-reducer.py
       StudyGroups-part-00000 (output results file)

Test File: student_test_posts2.csv


