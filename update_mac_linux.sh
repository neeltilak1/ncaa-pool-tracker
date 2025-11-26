#!/bin/bash
# NCAA Basketball Pool Data Updater - Mac/Linux Shell Script
# Make executable: chmod +x update_mac_linux.sh
# Run: ./update_mac_linux.sh

echo "======================================================================"
echo "NCAA BASKETBALL POOL DATA UPDATER"
echo "======================================================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo ""
    echo "Install Python 3:"
    echo "  Mac: brew install python3"
    echo "  Ubuntu/Debian: sudo apt-get install python3"
    echo "  Fedora: sudo dnf install python3"
    echo ""
    exit 1
fi

echo "Running update script..."
echo ""

# Run the Python script
python3 update_pool_data.py

# Check exit code
if [ $? -eq 0 ]; then
    echo ""
    echo "======================================================================"
    echo "SUCCESS! Your pool_data.json has been updated."
    echo "======================================================================"
    echo ""
    echo "Next steps:"
    echo "1. Upload the updated pool_data.json to GitHub"
    echo "2. Or refresh your local tracker page in the browser"
else
    echo ""
    echo "======================================================================"
    echo "UPDATE FAILED. Please check the error messages above."
    echo "======================================================================"
    echo ""
    echo "If auto-fetch doesn't work, use the Manual Edit feature instead."
fi

echo ""
read -p "Press Enter to continue..."
