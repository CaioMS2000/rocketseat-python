#!/bin/bash

# --- Setup and Safety Checks ---

# 1. Check if .git/hooks/pre-commit exists.  Exit if it doesn't.
if [ ! -f .git/hooks/pre-commit ]; then
  echo "Error: .git/hooks/pre-commit does not exist.  Cannot proceed." >&2
  exit 1
fi

# 2. Check if .git/hooks/pre-commit.original *already* exists.
#    If it does, warn and ask before overwriting.
if [ -f .git/hooks/pre-commit.original ]; then
  read -r -p ".git/hooks/pre-commit.original already exists. Overwrite? (y/N) " response
  if [[ ! "$response" =~ ^[Yy]$ ]]; then
    echo "Aborted.  .git/hooks/pre-commit.original not overwritten." >&2
    exit 1
  fi
fi

# --- Move and Create the New Hook ---

# 3. Rename the original pre-commit hook.
mv .git/hooks/pre-commit .git/hooks/pre-commit.original

# 4. Create the new pre-commit hook and write the script content.
#    Using a "here document" is the cleanest way to do this.
cat > .git/hooks/pre-commit <<EOF
#!/bin/sh
git add -A
.git/hooks/pre-commit.original
RESULT=\$?
if [ \$RESULT -ne 0 ]; then
  git add -A
fi
exit 0
EOF

# 5. Make both scripts executable.
chmod +x .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit.original

echo "pre-commit hook modified successfully."

exit 0