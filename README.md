# Auto Clicker Application

A fast left auto-clicking application that can be activated via keyboard shortcut and canceled instantly with right-click.

## Features

- **Fast Auto-Clicking**: Performs left clicks at 100 clicks per second
- **Keyboard Shortcut**: Press `F1` to start/stop auto-clicking
- **Instant Cancel**: Right-click anywhere to stop clicking immediately
- **Position Lock**: Clicks at the cursor position when activated
- **Simple GUI**: Easy-to-use interface with status display

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

3. **To start auto-clicking**:
   - Position your cursor where you want to click
   - Press `F1` to start auto-clicking at that position

4. **To stop auto-clicking**:
   - Press `F1` again, OR
   - Right-click anywhere on the screen

## Controls

- **F1**: Toggle auto-clicking on/off
- **Right-click**: Instantly stop auto-clicking
- **Exit button**: Close the application

## Important Notes

- Keep the GUI window open while using the auto-clicker
- The application will click at the cursor position when F1 is first pressed
- Right-click will stop clicking immediately, regardless of where you click
- The clicking rate is set to 100 clicks per second (very fast)

## Safety

- Always test in a safe environment first
- Use responsibly and in accordance with the terms of service of any applications you use it with
- The application includes instant stop functionality for safety

## Troubleshooting

- If the application doesn't respond to F1, make sure it has focus or try running as administrator
- If clicks aren't registering, ensure the target application accepts programmatic clicks
- On some systems, you may need to run the application with elevated privileges