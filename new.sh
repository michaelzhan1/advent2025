#!/bin/sh

# Check for required arguments
if [ $# -lt 1 ]; then
    echo "Usage: $0 <day>"
    exit 1
fi

# Pad number to 2 digits
padded=$(printf "%02d" "$1")

# File paths
src="$padded.py"
txt="$padded.in"

# Exit if file already exists
if [ -f "$src" ]; then
    exit 0
fi

# Create directory and files
touch "$txt"

cat > "$src" << EOF
def parse():
    with open("$padded.in") as f:
        return f.read()

def main():
    pass

if __name__ == "__main__":
    main()
EOF
