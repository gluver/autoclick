# Auto Clicker Application

A fast left auto-clicking application that can be activated via keyboard shortcut and canceled instantly with right-click.

## Features

- **Adjustable Speed**: Configurable click speed from 1-100 clicks per second
- **Keyboard Shortcut**: Press `Ctrl+Alt+K` to start/stop auto-clicking
- **Instant Cancel**: Right-click anywhere to stop clicking immediately
- **Position Lock**: Clicks at the cursor position when activated
- **Simple GUI**: Easy-to-use interface with speed control and status display
- **Standalone Executable**: Available as a self-contained .exe file

## Installation

1. Make sure you have Python 3.6+ installed
2. Create and activate a virtual environment:
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\Activate.ps1
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python autoclick.py
   ```

2. A GUI window will appear with instructions

3. **To adjust click speed**:
   - Use the speed slider in the GUI to set clicks per second (1-100)
   - Default speed is 20 clicks per second

4. **To start auto-clicking**:
   - Position your cursor where you want to click
   - Press `Ctrl+Alt+K` to start auto-clicking at that position
   - OR click the "Start Auto-Click" button in the GUI

5. **To stop auto-clicking**:
   - Press `Ctrl+Alt+K` again, OR
   - Click the "Stop" button in the GUI, OR
   - Right-click anywhere on the screen

## Controls

- **Ctrl+Alt+K**: Toggle auto-clicking on/off
- **Start Auto-Click button**: Begin auto-clicking (GUI)
- **Stop button**: Stop auto-clicking (GUI)
- **Speed slider**: Adjust click speed (1-100 clicks/sec)
- **Right-click**: Instantly stop auto-clicking
- **Exit button**: Close the application

## Important Notes

- Keep the GUI window open while using the auto-clicker
- The application will click at the cursor position when Ctrl+Alt+K is first pressed
- Right-click will stop clicking immediately, regardless of where you click
- The clicking rate is adjustable from 1-1000 clicks per second (default: 20)
- Higher speeds may cause system instability - use with caution

## Safety

- Always test in a safe environment first
- Use responsibly and in accordance with the terms of service of any applications you use it with
- The application includes instant stop functionality for safety

## Troubleshooting

- If the application doesn't respond to Ctrl+Alt+K, make sure it has focus or try running as administrator
- If clicks aren't registering, ensure the target application accepts programmatic clicks
- On some systems, you may need to run the application with elevated privileges
- For the standalone executable (autoclick.exe), no Python installation is required

## Compilation

To create a standalone executable:
```bash
pip install nuitka
python -m nuitka --standalone --onefile --windows-console-mode=disable --enable-plugin=tk-inter autoclick.py
```

This will create `autoclick.exe` - a self-contained executable that runs without Python installation.