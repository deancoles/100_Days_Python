# You are given a list of exam scores, and you have to print out the highest score from the list.

# List of scores
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# Declare a global variable to contain the highest score
max_score = 0

# Loop through all scores, updating max_score when required
for score in student_scores:
    if score > max_score:
        max_score = score

# Print the highest exam score
print(max_score)