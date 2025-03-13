# Python Learning Course with Minecraft

This repository contains a collection of Python programming lessons and projects, with a special focus on learning Python through Minecraft integration.

## Course Structure

### Minecraft Lessons
The course includes a series of lessons (`les*.py`) that teach Python programming concepts using Minecraft:
- Basic Python syntax and data types
- Functions and classes
- Control structures (if/else, loops)
- Object-oriented programming
- Game development concepts

### Projects
1. **Tic-tac-toe Game**
   - Command-line version (`tic_tac_toe.py`)
   - Graphical user interface version (`tic_tac_toe_gui.py`)
   - Demonstrates GUI programming with Tkinter

2. **Minecraft Manager**
   - Command-line version (`start.sh`)
   - Graphical user interface version (`minecraft_manager.py`)
   - Demonstrates advanced GUI programming and process management

## Prerequisites
- Python 3.x
- Minecraft Pi API or Minecraft with Pi mod
- Tkinter (usually comes with Python)
- Java Runtime Environment (JRE) for Minecraft launchers
- psutil package for process management

## Setup Instructions

1. Clone the repository:
```bash
git clone [your-repository-url]
```

2. Install required packages:
```bash
pip install mcpi psutil
```

3. For Minecraft integration:
   - Install Minecraft Pi mod
   - Start Minecraft
   - Enable the Pi API in Minecraft settings

4. For Minecraft Launchers and Server:
   - Ensure Java is installed on your system
   - Place TLauncher.jar in the `TLauncher/` directory
   - Place PrismLauncher in the `Prism Launcher.app/` directory
   - Place Spigot server JAR in the `minecraft-server/` directory

## Running the Programs

### Minecraft Lessons
1. Start Minecraft
2. Run any lesson file:
```bash
python les*.py
```

### Tic-tac-toe Game
1. For command-line version:
```bash
python tic_tac_toe.py
```

2. For GUI version:
```bash
python tic_tac_toe_gui.py
```

### Minecraft Launchers and Server
The project includes two ways to manage Minecraft launchers and server:

#### 1. Command-line Version (start.sh)
1. Make the script executable:
```bash
chmod +x start.sh
```

2. Run the script:
```bash
./start.sh
```

3. Choose from the available options:
   - 1: Start Server only
   - 2: Start TLauncher only
   - 3: Start PrismLauncher only
   - 4: Start Server and TLauncher
   - 5: Start Server and PrismLauncher
   - 6: Start All
   - 7: Exit

#### 2. Graphical User Interface (minecraft_manager.py)
1. Run the GUI manager:
```bash
python minecraft_manager.py
```

Features of the GUI version:
- Visual status indicators for each component
- Individual start/stop controls
- Quick start/stop all buttons
- Real-time log viewer
- Error handling with pop-up messages
- Process status monitoring
- Memory configuration options

Logs are stored in the `logs/` directory:
- `server.log`: Minecraft server logs
- `tlauncher.log`: TLauncher logs
- `prism.log`: PrismLauncher logs

## Course Content

### Minecraft Lessons
- `les1.py` - Introduction to Minecraft API
- `les2.py` - Basic block placement
- `les3.py` - Player interaction
- `les4.py` - Building structures
- `les5.py` - Loops and patterns
- `les6.py` - Functions and modular programming
- `les7.py` - Event handling
- `les8.py` - Advanced building techniques
- `les9.py` - Game mechanics
- `les10.py` - Complex structures
- And more...

### Projects
- Tic-tac-toe game with both CLI and GUI versions
- Minecraft Manager with both CLI and GUI versions
- Demonstrates:
  - Object-oriented programming
  - GUI development
  - Process management
  - Log handling
  - Error handling
  - User input handling

## Contributing
Feel free to contribute to this project by:
1. Forking the repository
2. Creating a new branch
3. Making your changes
4. Submitting a pull request

## License
This project is open source and available under the MIT License.

## Author
[Your Name]

## Acknowledgments
- Minecraft Pi API developers
- Python community
- Tkinter documentation
- TLauncher team
- PrismLauncher team
- Spigot team 