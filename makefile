.PHONY: run test

# Run the simulation program
run:
	@echo "Running Simulation..."
	python3 main.py
 
# Run the unit tests
test:
	@echo "Running Tests..."
	python3 -m unittest test_simulation.py