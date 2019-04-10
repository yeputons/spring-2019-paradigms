APPS=$(sort $(basename $(wildcard *.cpp)))

.PHONY: all clean

all: $(APPS)

%: %.cpp
	g++ $^ -o $@ -Wall -Wextra -Werror -pthread

clean:
	rm $(APPS) >/dev/null 2>&1 || true
