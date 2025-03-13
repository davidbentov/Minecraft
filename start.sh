#!/bin/bash

# Configuration
JAVA_EXECUTABLE="java"
SERVER_JAR="minecraft-server/spigot.jar"
TLAUNCHER_PATH="TLauncher/TLauncher.jar"
PRISM_LAUNCHER_PATH="Prism Launcher.app/Contents/MacOS/PrismLauncher"
SERVER_MEMORY="-Xms1G -Xmx2G"
TLAUNCHER_MEMORY="-Xms512M -Xmx1G"
PRISM_MEMORY="-Xms512M -Xmx1G"
SERVER_LOG="logs/server.log"
TLAUNCHER_LOG="logs/tlauncher.log"
PRISM_LOG="logs/prism.log"

# Create logs directory if it doesn't exist
mkdir -p logs

# Function to check if a process is running
check_process() {
    if pgrep -f "$1" > /dev/null; then
        return 0
    else
        return 1
    fi
}

# Function to start the server
start_server() {
    echo "Starting Minecraft server..."
    if [ ! -f "$SERVER_JAR" ]; then
        echo "Error: Server JAR not found at $SERVER_JAR"
        return 1
    fi
    
    nohup $JAVA_EXECUTABLE $SERVER_MEMORY -jar "$SERVER_JAR" nogui >> "$SERVER_LOG" 2>&1 &
    SERVER_PID=$!
    
    # Wait for server to start
    echo "Waiting for server to initialize..."
    sleep 10
    
    if check_process "$SERVER_JAR"; then
        echo "Minecraft server started successfully with PID $SERVER_PID"
        return 0
    else
        echo "Error: Failed to start Minecraft server"
        return 1
    fi
}

# Function to start TLauncher
start_tlauncher() {
    echo "Starting TLauncher..."
    if [ ! -f "$TLAUNCHER_PATH" ]; then
        echo "Error: TLauncher JAR not found at $TLAUNCHER_PATH"
        return 1
    fi
    
    nohup $JAVA_EXECUTABLE $TLAUNCHER_MEMORY -jar "$TLAUNCHER_PATH" >> "$TLAUNCHER_LOG" 2>&1 &
    TLAUNCHER_PID=$!
    
    if check_process "TLauncher"; then
        echo "TLauncher started successfully with PID $TLAUNCHER_PID"
        return 0
    else
        echo "Error: Failed to start TLauncher"
        return 1
    fi
}

# Function to start PrismLauncher
start_prism() {
    echo "Starting PrismLauncher..."
    if [ ! -f "$PRISM_LAUNCHER_PATH" ]; then
        echo "Error: PrismLauncher not found at $PRISM_LAUNCHER_PATH"
        return 1
    fi
    
    nohup "$PRISM_LAUNCHER_PATH" >> "$PRISM_LOG" 2>&1 &
    PRISM_PID=$!
    
    if check_process "PrismLauncher"; then
        echo "PrismLauncher started successfully with PID $PRISM_PID"
        return 0
    else
        echo "Error: Failed to start PrismLauncher"
        return 1
    fi
}

# Main execution
echo "=== Minecraft Launcher and Server Manager ==="
echo "1. Start Server only"
echo "2. Start TLauncher only"
echo "3. Start PrismLauncher only"
echo "4. Start Server and TLauncher"
echo "5. Start Server and PrismLauncher"
echo "6. Start All"
echo "7. Exit"
read -p "Choose an option (1-7): " choice

case $choice in
    1)
        start_server
        ;;
    2)
        start_tlauncher
        ;;
    3)
        start_prism
        ;;
    4)
        start_server && start_tlauncher
        ;;
    5)
        start_server && start_prism
        ;;
    6)
        start_server && start_tlauncher && start_prism
        ;;
    7)
        echo "Exiting..."
        exit 0
        ;;
    *)
        echo "Invalid option. Exiting..."
        exit 1
        ;;
esac

# Wait for processes to terminate if any were started
if [ -n "$SERVER_PID" ]; then
    wait $SERVER_PID
fi
if [ -n "$TLAUNCHER_PID" ]; then
    wait $TLAUNCHER_PID
fi
if [ -n "$PRISM_PID" ]; then
    wait $PRISM_PID
fi

echo "All started processes have terminated."

