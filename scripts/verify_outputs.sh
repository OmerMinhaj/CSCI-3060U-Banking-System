#!/bin/bash
# verify_outputs.sh: Compares actual transaction files to expected files

cd ../outputs || exit

for actual_file in *.atf; do
    echo "Checking outputs of test $actual_file"
    
    # Run diff against the expected directory
    if diff "$actual_file" "../expected/$actual_file"; then
        echo "[PASS] $actual_file matches expected output."
    else
        echo "[FAIL] Mismatch found in $actual_file!"
    fi
done