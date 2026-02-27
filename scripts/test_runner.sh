#!/bin/bash
# test_runner.sh: Automates front-end execution

# Clear the old output files before running the new tests
rm -f ../outputs/*.atf ../outputs/*.out

cd ../inputs || exit

for i in *.txt; do
    echo "Running test $i"
    # Extracts filename without extension
    name=$(basename "$i" .txt)
    
    # Run the python script with command line arguments, piping input and redirecting terminal output
    python ../src/main.py ../current_accounts.txt ../outputs/"${name}.atf" < "$i" > ../outputs/"${name}.out"
done

echo "All tests executed."