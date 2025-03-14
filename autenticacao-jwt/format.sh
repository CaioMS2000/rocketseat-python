echo "Removing __pycache__ directories..."
find . -type d -name "__pycache__" -exec rm -rf {} +

echo "Adding __init__.py files..."
python add_init.py

echo "Formatting code..."
ruff format src/

echo "Final cleanup..."
find . -type d -name "__pycache__" -exec rm -rf {} +

echo "Done!"
