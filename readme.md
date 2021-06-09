# Summary of Key Lessons

## 0. Algorithms and Data Structures (ADS)
Continuing [Part 3 of ADS lectures by MIT[08:43]](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/lecture-videos/lecture-12-searching-and-sorting/). Irrelevant to ADS, [problem sets 4 and 5](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/) may be good practice if there is time.

Time Complexity Desirability: O(1) > O(logn) {reduce problem in half each time, bisection seach} > O(n) > O(nlogn) [{Timsort}](https://en.wikipedia.org/wiki/Timsort) > O(n^c) {nested loops} > O(c^n)

## 1. Brute Force Works, Just Not As Well On Big Problems.
Brute force methods are usually the easiest, first thing to think of. For an example, see two-sum.py. Beyond the initial solution, one should think of answers that help reduce computational time and/or space. This is related to the idea of **space and time complexity.** In the example of two-sum.py, we see that sacrificing some space by saving values into a **dictionary lookup** instead of double for-loops help reduce time complexity from O(n^2) to O(n), 4000ms to 40ms!

## 2. Binary Search Algorithm
By implementing the low = 0, high = len(array), n = (high - low)//2 and iterating over that, the search space effectively can be halved. This greatly reduces computational time.

## 3. Creativity
Check out the creative solutions on LeetCode discussion pages!


----------------------------------------------
# Explorations of DSAI/ML.
Today was a tiring day... just gonna copy-paste some job requirements I found on LinkedIn for DSAI.
Interestingly, **Team Lead** roles at Apple and a few other companies don't require **technical** skills at all! Got to seriously consider which path is more right for me.

(1. Bytedance)
- Major in computer science or a related technical discipline;
- Highly competent in algorithms and programming, prefer winners in ACMICPC, NOI/IOI, Top coder, and Kaggle;
- Good understanding of data structures and algorithms;
- Great communication and teamwork skills
- Publishing papers in top AI conferences or journals is a plus, including but not limited to CVPR, ICCV, ECCV, ICML, NeurIPS, ICLR, KDD, AAAI, IJCAI, etc.;
- Deep understanding in one of the following domains is a plus: image classification, object detection, and multi-modal learning.
(2. Google)
- Bachelor's degree in Statistics, Computer Science, Engineering, or Mathematics, related quantitative discipline, or equivalent practical experience.
- 8 years of experience in an analytical field.
- Experience in Python or R.
- Experience in data management systems.
+ PhD in Statistics, Computer Science, Engineering, or Mathematics.
+ Experience in data science with a focus on marketing analytics, statistical modeling, machine learning, forecasting and optimization.
+ Experience with big data and cloud platforms to deploy large-scale data science solutions.
+ Knowledge of media and the statistical algorithms typically used in marketing analytics.
(3. GovTech)
* Have experience working with data and machine learning to solve problems
* Have a demonstrated ability to build software
* Can write code to solve abstract problems
* Can talk and reason about code with other engineers
* Take the initiative to make things happen
* Want to work for the public good.
(4. ITE)
+ Suitable academic credentials in Data Science, Statistics, Computer Science, Information Systems, Analytics or related disciplines.
+ Knowledge and experience in :
+ implementing relational and non-relational databases
+ programming languages such as SQL, Python, R or Scala
+ data processing, visualisation
+ building and maintaining data/solution pipelines that feed machine learning models
+ building AI models in platforms such as Kera, TensorFlow or Theano
+ Strong interpersonal, communication and report writing skills.
(5. Agoda)
- Bachelor’s Degree or higher from top university in a quantitative subject (computer science, mathematics, engineering, statistics or science)
- Ability to communicate fluently in English
- Good numerical reasoning skills
- Proficiency in Excel
- Intellectual curiosity
+ Exposure to one or more data analysis packages or databases, e.g., SAS, R, SPSS, Python, VBA, SQL
+ Experience in digital marketing
+ Academic research experience
(6. IBM)
- For the research scientist role, a PhD in mathematics, computer science or related subject with experience in theory of algorithms, and publications in top tier conferences and journals.
- Python, C/C++, Java or other programming language
