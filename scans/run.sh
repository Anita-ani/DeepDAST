#!/bin/bash

# Create scans directory if it doesn't exist
if [ ! -d "scans" ]; then
  echo "Creating scans/ directory..."
  mkdir scans
fi

# Start FastAPI backend
echo "Starting FastAPI backend..."
cd backend
uvicorn main:app --reload &
BACKEND_PID=$!
cd ..

# Wait a few seconds to let backend start
sleep 2

# Open the frontend HTML page
FRONTEND_FILE="frontend/index.html"
if [ -f "$FRONTEND_FILE" ]; then
  echo "Opening frontend in browser..."
  if command -v xdg-open >/dev/null; then
    xdg-open "$FRONTEND_FILE"
  elif command -v open >/dev/null; then
    open "$FRONTEND_FILE"
  else
    echo "Could not detect a supported browser opener. Please open $FRONTEND_FILE manually."
  fi
else
  echo "Frontend file not found."
fi

# Wait for backend process to exit
trap "echo Stopping backend...; kill $BACKEND_PID" EXIT
wait $BACKEND_PID
