# CC = gcc


# # List of input files (1-0.txt to 2-9.txt)
# INPUT_FILES = $(shell seq -f "input-1-%g.txt" 0 9) $(shell seq -f "input-2-%g.txt" 0 9)

# # Rule to read the input file list
# print: 
# 	@echo $(INPUT_FILES)

# # Rule to build the executable
# pretest: pretest.c
# 	@$(CC) -g $< -o $@

# # Rule to execute and test the program
# compare: pretest $(INPUT_FILES)
# 	@for input_file in $(INPUT_FILES); do \
# 		expected_output="dataset/output/output$${input_file#input}"; \
# 		./pretest $$input_file; \
# 		if diff -s dataset/myoutput/output.txt $$expected_output >> diff_log.txt; then \
# 			echo "Test passed: $$input_file"; \
# 		else \
# 			echo "Test failed: $$input_file"; \
# 		fi; \
# 	done


# # Rule to clean up generated files
# clean:
# 	@rm -f pretest diff_log.txt dataset/myoutput/*

# .PHONY: compare clean $(INPUT_FILES)

PYTHON = python3

# List of input files (1-0.txt to 2-9.txt)
INPUT_FILES = $(shell seq -f "input-1-%g.txt" 0 9) $(shell seq -f "input-2-%g.txt" 0 9)

# Rule to read the input file list
print:
	@echo $(INPUT_FILES)

# Rule to execute and test the Python program
compare: winner.py $(INPUT_FILES)
	@for input_file in $(INPUT_FILES); do \
		expected_output="output/output$${input_file#input}"; \
		$(PYTHON) winner.py $$input_file; \
		if diff -s myoutput/output.txt $$expected_output >> diff_log.txt; then \
			echo "Test passed: $$input_file"; \
		else \
			echo "Test failed: $$input_file"; \
		fi; \
	done

# Rule to clean up generated files
clean:
	@rm -f diff_log.txt myoutput/*

.PHONY: compare clean print $(INPUT_FILES)



