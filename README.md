# FuzzingDriver

[FuzzingDriver: the Missing Dictionary to Increase Code Coverage in Fuzzers, SANER'22](https://arxiv.org/pdf/2201.04853.pdf)


We propose a tool, called FuzzingDriver, to generate dictionary tokens for coverage-based greybox fuzzers (CGF) from the codebase of any target program. FuzzingDriver does not add any overhead to the fuzzing job as it is run beforehand. We compared FuzzingDriver to Google dictionaries by fuzzing six open-source targets, and we found that FuzzingDriver consistently achieves higher code coverage in all tests. We also executed eight benchmarks on FuzzBench to demonstrate how utilizing FuzzingDriver's dictionaries can outperform six widely-used CGF fuzzers. In future work, investigating the impact of FuzzingDriver's dictionaries on improving bug coverage might prove important. 

[Video demonstration](https://www.youtube.com/watch?v=Y8j_KvfRrI8)
