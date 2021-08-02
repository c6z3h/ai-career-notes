# Updates at a glance / what I did today:
- Alternate-day Leetcode practice
- More Ontology work.
## Next:
- AWS Udacity ML course quiz, PettingZoo multi-agent RL..
- [AlphaZERO Paper: Methods](https://www.nature.com/articles/nature24270): What is MCTS??
- Apply to the evergreen "Talent Incubators", Stay connected on StartupSG Network.
- Continue Book: Think and Grow Rich self-questionnaire
- Study some anthropology to know how to create better RL models, especially how to model the ever-changing subgoals of living things. Perhaps too, what cause the successful predictive modelling of "Limits to Growth"..
----------------------------------------------
# My Coding Tests
## 1. AI Singapore: AI Apprentice Test
## 2. Grab: (1) DevOps, (2) DSAI Test
## 3. GovTech: Technological Associate Programme Test
## 4. Shopee: ML Engineer (Fresh Grad) Test, 14 July 2021
- 2 questions in 60 min, proctored with camera, microphone, screen_share (Glider.AI).
- Similar to Leetcode Easy / medium.
- (1) Strings: Substring matching (2) Sort and search: k-th largest integer in array.
## 5. ByteDance: SWE - HBase, tbc
----------------------------------------------
# Career Explorations
Target of Artificial General Intelligence (AGI). Why? If done well, it may offer a prediction of our future, and solve problems ahead of our time. We may be able to leap forward eons to reach the stable equilibria that awaits Earthlings at last. NLP, CV are smart, but they are specific to the domain -- [RL may be the backbone](https://venturebeat.com/2021/06/09/deepmind-says-reinforcement-learning-is-enough-to-reach-general-ai/). Printed the DeepMind paper, ["Reward is enough"](https://www.sciencedirect.com/science/article/pii/S0004370221000862),

[He’s not alone. Part of the problem is that AGI is a catchall for the hopes and fears surrounding an entire technology. Contrary to popular belief, it’s not really about machine consciousness or thinking robots (though many AGI folk dream about that too). But it is about thinking big. Many of the challenges we face today, from climate change to failing democracies to public health crises, are vastly complex. If we had machines that could think like us or better—more quickly and without tiring—then maybe we’d stand a better chance of solving these problems. As the computer scientist I.J. Good put it in 1965: “the first ultraintelligent machine is the last invention that man need ever make.” - MIT Technology Review](https://www.technologyreview.com/2020/10/15/1010461/artificial-general-intelligence-robots-ai-agi-deepmind-google-openai/)
"OpenAI has said that it wants to be the first to build a machine with human-like reasoning abilities."
http://raysolomonoff.com/dartmouth/boxa/dart564props.pdf
https://link.springer.com/article/10.1007/s11023-007-9079-x
https://www.wired.com/2015/01/the-deep-mind-of-demis-hassabis/
HYPOTHESIS: IF we create a RL model of Earth and tune parameters such that events play out as it has been recorded in History, then we can be sure that the predictions of future will be of higher accuracy too.

PHILOSOPHICALLY: What is the best good for man? To alleviate suffering?
Job Requirements copy-pasted from LinkedIN for DSAI.
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


----------------------------------------------
# Lessons from the Udacity: AWS ML Course 2021
## 1. Object-Oriented Programming (Python)
* class, `__init__`, and self are the basic building blocks of a class.
* Magic Methods ( `def __add__(self, other):` , `return "mean {}, standard deviation {}".format(self.mean, self.stdev)` )
* Inheritance (method and attributes for the parent, children inherit attributes)
* Making a Package, Upload to PyPi
## 2. Software Engineering Best Practices
* Docstrings, Refactoring
* Test-Driven Development
* Code Review / Logging
## 3. Machine Learning Theory
* ML Steps: (1) Define problem (2) Build dataset (3) Train model, minimize loss function (4) Evaluate model (5) Use model / infer
## 4. Machine Learning in AWS (Practical)
*By 2023, spending on AI systems will reach $98B, up 2.5x from 2019. - IDC, By end of 2024, 75% of enterprises will shift from piloting to operationalizing AI. - Gartner, ML is now part of mainstream DevOps process, not isolated projects. - Gartner*
* AWS pre-trained AI services, just apply without needing knowledge in machine learning (Computer Vision (CV), Reinforcement Learning(RL), Generative Adversarial Networks (GAN)).
### CV - DeepLens
* Uses -- in identification of polar bears, manual hard-coding of rules is limited as the polar bear may not always face the camera.
* Tasks -- image classification (classify the whole image), object detection (detect object(s) in a image), semantic segmentation (detect position of objects), activity recognition (video)
### RL - DeepRacer (free trial)
* Uses -- games frustration-boredom balancer, wind turbine farm downstream airflow optimization.
* Delete the model to not incur charges!
### GAN - DeepComposer (free trial)
* Generator (create new music; with feedback from Discriminator)
* Discriminator (validate if generated music sounds like real music)
----------------------------------------------
# Lessons from LeetCode
## 0. Algorithms and Data Structures (ADS)
Continuing [Part 3 of ADS lectures by MIT[08:43]](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/lecture-videos/lecture-12-searching-and-sorting/). Irrelevant to ADS, [problem sets 4 and 5](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/) may be good practice if there is time.

Time Complexity Desirability: O(1) > O(logn) {reduce problem in half each time, bisection seach} > O(n) > O(nlogn) [{Timsort}](https://en.wikipedia.org/wiki/Timsort) > O(n^c) {nested loops} > O(c^n)

## 1. Brute Force Works, Just Not As Well On Big Problems.
Brute force methods are usually the easiest, first thing to think of. For an example, see two-sum.py. Beyond the initial solution, one should think of answers that help reduce computational time and/or space. This is related to the idea of **space and time complexity.** In the example of two-sum.py, we see that sacrificing some space by saving values into a **dictionary lookup** instead of double for-loops help reduce time complexity from O(n^2) to O(n), 4000ms to 40ms!

## 2. Binary Search Algorithm
By implementing the low = 0, high = len(array), n = (high - low)//2 and iterating over that, the search space effectively can be halved. This greatly reduces computational time.

## 3. Creativity
Check out the creative solutions on LeetCode discussion pages!
