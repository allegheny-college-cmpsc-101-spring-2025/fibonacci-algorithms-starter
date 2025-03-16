# Fibonacci Algorithms

TODO: Make sure that you delete all of the TODO markers inside of this file and
either remove or rewrite the prompts. When you are finished with this reflection
it should contain professional writing that is suitable for publishing. That
includes removing this paragraph!


## Add Your Name Here

## 1. Program Output

TODO: This section will document program output, but it is also the data source for
an empirical timing experiment. Do not run the program with the `--display` option
because the display will impact the timing of the algorithms. Use the
`--pyinstrument` command-line argument to open up a web-based display
of the call profile from running your program. You can use this output to understand
the other profiling information that `fibonaccicreator` can produce. If an algorithm
does not work correctly and you can explain why it does not work, then please
provide that output in one of the fenced code blocks under the correct heading
below. Keep reading to see exactly what to run for your timing experiment.

### Two outputs from running the `iterativetuple`

TODO: Put the obtained outputs in fenced-code blocks. Choose small and large
inputs for a computer, perhaps separated by an order of magnitude. It is
essential that real, non-zero profile timings are obtained whenever possible. 

- Run 1: `iterativetuple` with a small input
- Run 2: `iterativetuple` with a large input


### Two outputs from running the `iterativelist`

TODO: Put the obtained outputs in fenced-code blocks. Use the same small and
large inputs as above. It is essential that real, non-zero profile timings are
obtained whenever possible. 

- Run 1: `iterativelist` with a small input
- Run 2: `iterativelist` with a large input

### Two outputs from running the `recursivetuple`

TODO: Put the obtained outputs in fenced-code blocks. Use the same small and
large inputs as above. It is essential that real, non-zero profile timings are
obtained whenever possible. 

- Run 1: `recursivetuple` with a small input
- Run 2: `recursivetuple` with a large input

### Two outputs from running the `recursivelist`

TODO: Put the obtained outputs in fenced-code blocks. Use the same small and
large inputs as above. It is essential that real, non-zero profile timings are
obtained whenever possible. 

- Run 1: `recursivelist` with a small input
- Run 2: `recursivelist` with a large input

### Justification of your choice for the large and small inputs

TODO: Document and justify your choice for the large and small inputs.
Describe any issues or compromises you had to make and why.


## 2. Performance Report

### Data

TODO: Fill in the table in markdown to summarize the profile timing data
gathered above. Abbreviation it stands for iterative tuple,
rl recursive list etc. Use one row for your small input and one
row for your large input. Add any rows as needed depending on your
unique situations.

| input | approach it | approach il | approach rt | approach rl|
|-------|-------------|-------------|-------------|------------|
| TODO  | TODO        | TODO        | TODO        | TODO       |
| TODO  | TODO        | TODO        | TODO        | TODO       |

### Analysis

TODO: Using the formula given in Prime Testing, show how you calculate which
algorithm is fastest and by how much it is faster. I.e., compute differences
while holding the denominator constant. Your calculations should use the data
in the data table above.

### Results and Discussion

TODO: Explain which algorithm is fastest, by how
much it is faster, and how you knew that it was faster referencing
the data analysis in the previously section. 

### Performance Report Conclusion

TODO: In conclusion, make sure that you can answer the following research
questions:

- RQ: Is `fibonaccicreator` faster with a list or a tuple?
- RQ: Is `fibonaccicreator` faster with recursion or iteration?
- RQ: Overall, what is the fastest approach when using `fibonaccicreator`?
- RQ: Overall, what is the most memory efficient approach when using `fibonaccicreator`?
- RQ: Overall, what are inappropriate approaches for computing Fibonacci numbers?

## 3. Source Code Review

TODO: Use a fenced code block to provide the requested source code.
Then describe in detail how the source code works.

### Function signature that defines the command-line interface for `fibonaccicreator`
### A code segment that calls a function based on its name in a string

## 4. Professional Development

TODO: Answer the questions below in your own words thinking about your
professional skills development.

- What was the greatest challenge that you faced when completing this assignment?
- How have your challenges or skills changed from assignment to assignment?
- Leveraging what you know from all experiments conducted this semester, what are "fast" ways to perform computations?
- Leveraging what you know from all experiments conducted this semester, what are "slow" ways to perform computations?
- What stumbling blocks did you encounter while using recursive algorithms?
- What resources did you consult when completing this project? How did they help you?
