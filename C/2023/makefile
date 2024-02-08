CC=gcc
CFLAGS=-Wall -g
INCLUDES=-Ilib

SOLUTIONS=solutions
UTIL_DIR=lib
BIN_DIR=bin

# Utility files
UTIL_SOURCES=$(wildcard $(UTIL_DIR)/*.c)

# Executable files
SOURCES=$(wildcard $(SOLUTIONS)/*.c)
EXECS=$(patsubst $(SOLUTIONS)/%.c,$(BIN_DIR)/%,$(SOURCES))

.PHONY: all clean setup

all: setup $(EXECS)

setup:
	@mkdir -p $(BIN_DIR)

$(BIN_DIR)/%: $(SOLUTIONS)/%.c $(UTIL_SOURCES)
	$(CC) $(CFLAGS) $(INCLUDES) -o $@ $^

clean:
	@rm -rf $(BIN_DIR)
