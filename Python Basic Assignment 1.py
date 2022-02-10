#!/usr/bin/env python
# coding: utf-8
Q 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
* 
'hello'
-87.8
- 
/ 
+
6 
## Solution 
Values- 'hello',-87.8,8
expression- *,-,/,+
Q 2.  What is the difference between string and variable?
Solition. 1. A Variable is a store of information, and a String is a type of information you would store in a Variable
          2. A String is usually words, enclosed with "" Eg String x ="Welcome to SoloLearn" X is the Variable, and we declared it as a String, use the single = to assign the text to it.Q. 3. Describe three different data types.
Solution: Data Type: Data type is a data storage format that can contain a specific type or range of values. Below are three Data types
1. String (or str or text). Used for a combination of any characters that appear on a keyboard, such as letters, numbers and symbols.
2. Character (or char). Used for single letters.
3. Integer (or int). Used for whole numbers.Q 4.  What is an expression made up of? What do all expressions do?
Sol. An expression is a combination of values, variables, operators, and calls to functions. Expressions need to be evaluated.
The evaluation of an expression produces a value, which is why expressions can appear on the right hand side of assignment statements. A value all by itself is a simple expression, and so is a variable. Evaluating a variable gives the value that the variable refers to.
Q What do all expressions do?
All expressions evaluate (that is, reduce) to a single value.Q 5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
Sol: A statement performs some action such as printing values, looping, or if statement. On the other hand, expressions also produce values and we can assign these values to new variables.
-If you can print it, or assign it to a variable, it’s an expression. If you can’t, it’s a statement.
 examples of expressions:
 2 + 2 
3 * 7 
1 + 2 + 3 * (8 ** 9) - sqrt(4.0) 
min(2, 22) 
examples of statements:
if CONDITION: 
elif CONDITION: 
else:
Q 6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1
Sol:23

# In[1]:


bacon = 22
bacon + 1

Q 7. What should the values of the following two terms be?
'spam' + 'spamspam'
'spam' * 3
Sol: 'spamspamspam'
# In[4]:


'spam' + 'spamspam'
'spam' * 3

Q. 8 Why is eggs a valid variable name while 100 is invalid?
Sol: Because variable names cannot begin with a number.

Q 9 What three functions can be used to get the integer, floating-point number, or string version of a value?
sol: The int(), float(), and str() functions will evaluate to the integer, floating-point number, and string versions of the value passed to them.
Q 10 Why does this expression cause an error? How can you fix it?
'I have eaten ' + 99 + ' burritos.'
Sol: ' The expression causes an error because 99 is an integer, and only strings can be concatenated to other strings with the + operator.
)
'I have eaten ' + '99' + ' burritos.'
'I have eaten ' + str(99) + ' burritos.'
# In[10]:


'I have eaten ' + str(99) + ' burritos.'


# In[11]:


'I have eaten ' + 99 + ' burritos.'


# In[ ]:




