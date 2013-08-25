#from mrbook.org/tutorials/make/
CC=gcc
CFLAGS=-c -Wall 
LDFLAGS= -lm
SOURCES=main.c
OBJECTS=$(SOURCES:.c=.o)
EXECUTABLE=a.out

all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(OBJECTS) -o $@ $(LDFLAGS) 

.c.o:
	$(CC) $(CFLAGS) $< -o $@

