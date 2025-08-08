CXX = g++
CXXFLAGS = -O2 -std=c++17

TARGET = pretest

# List of input files 
INPUT_FILES = $(wildcard input/*.txt)

TEST_INPUT = input/input-1-0.txt


# Rule to build the executable
$(TARGET): $(TARGET).cpp
	@$(CXX) $(CXXFLAGS) $< -o $@

# Rule to read the input file list
print: 
	@echo $(INPUT_FILES)


# Rule to execute and test the program
compare: $(TARGET) $(INPUT_FILES)
	@> diff_log.txt
	@for input_file in $(INPUT_FILES); do \
		input_base=$$(basename $$input_file); \
		prefix=$$(echo $$input_base | sed -n 's/^\(.*\)input-.*\.txt/\1/p'); \
		rest=$$(echo $$input_base | sed -n 's/^.*input-\(.*\.txt\)/\1/p'); \
		expected_output="output/$${prefix}output-$${rest}"; \
		./$(TARGET) $$input_file; \
		if diff -s myoutput/output.txt $$expected_output >> diff_log.txt; then \
			echo "Test passed: $$input_file"; \
		else \
			echo "Test failed: $$input_file"; \
		fi; \
	done

test: $(TARGET)
	./$(TARGET) $(TEST_INPUT)

# Rule to clean up generated files
clean:
	@rm -rf $(TARGET) diff_log.txt myoutput/

.PHONY: compare clean print

# PYTHON = python3

# # List of input files (1-0.txt to 2-9.txt)
# INPUT_FILES = $(shell seq -f "input-1-%g.txt" 0 9) $(shell seq -f "input-2-%g.txt" 0 9)

# # Rule to read the input file list
# print:
# 	@echo $(INPUT_FILES)

# # Rule to execute and test the Python program
# compare: pretest.py $(INPUT_FILES)
# 	@for input_file in $(INPUT_FILES); do \
# 		expected_output="dataset/output/output$${input_file#input}"; \
# 		$(PYTHON) pretest.py $$input_file; \
# 		if diff -s dataset/myoutput/output.txt $$expected_output >> diff_log.txt; then \
# 			echo "Test passed: $$input_file"; \
# 		else \
# 			echo "Test failed: $$input_file"; \
# 		fi; \
# 	done

# # Rule to clean up generated files
# clean:
# 	@rm -f diff_log.txt dataset/myoutput/*

# .PHONY: compare clean print $(INPUT_FILES)



