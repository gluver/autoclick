import threading
import time
from pynput import mouse, keyboard
from pynput.mouse import Button, Listener as MouseListener
from pynput.keyboard import Key, Listener as KeyboardListener, GlobalHotKeys
import tkinter as tk
from tkinter import messagebox
import sys

class AutoClicker:
    def __init__(self):
        self.clicking = False
        self.click_thread = None
        self.mouse_listener = None
        self.keyboard_listener = None
        self.current_pos = (0, 0)
        self.mouse_controller = mouse.Controller()
        self.click_speed = 20  # Default 20 clicks per second
        
        # Create GUI
        self.root = tk.Tk()
        self.root.title("Auto Clicker")
        self.root.geometry("300x280")
        self.root.resizable(False, False)
        
        # Status label
        self.status_label = tk.Label(self.root, text="Status: Ready", font=("Arial", 12))
        self.status_label.pack(pady=10)
        
        # Control buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        self.start_btn = tk.Button(button_frame, text="Start Auto-Click", 
                                  command=self.start_clicking, 
                                  bg="green", fg="white", width=15)
        self.start_btn.pack(side=tk.LEFT, padx=5)
        
        self.stop_btn = tk.Button(button_frame, text="Stop", 
                                 command=self.stop_clicking, 
                                 bg="red", fg="white", width=10)
        self.stop_btn.pack(side=tk.LEFT, padx=5)
        self.stop_btn.config(state="disabled")  # Initially disabled
        
        # Speed control
        speed_frame = tk.Frame(self.root)
        speed_frame.pack(pady=10)
        
        speed_label = tk.Label(speed_frame, text="Click Speed (clicks/sec):", font=("Arial", 10))
        speed_label.pack()
        
        self.speed_var = tk.IntVar(value=self.click_speed)
        self.speed_scale = tk.Scale(speed_frame, from_=1, to=1000, orient=tk.HORIZONTAL, 
                                   variable=self.speed_var, command=self.update_speed,
                                   length=300)
        self.speed_scale.pack(pady=5)
        
        self.speed_display = tk.Label(speed_frame, text=f"Current: {self.click_speed} clicks/sec", 
                                     font=("Arial", 9), fg="blue")
        self.speed_display.pack()
        
        # Instructions
        instructions = [
            "Press Ctrl+Alt+K or 'Start Auto-Click' button",
            "Right-click anywhere to stop instantly",
            "Auto-clicks at current cursor position"
        ]
        
        for instruction in instructions:
            label = tk.Label(self.root, text=instruction, font=("Arial", 9))
            label.pack(pady=2)
        
        # Exit button
        exit_btn = tk.Button(self.root, text="Exit", command=self.exit_app, bg="red", fg="white")
        exit_btn.pack(pady=10)
        
        # Setup hotkeys and listeners
        self.setup_listeners()
    
    def update_speed(self, value):
        """Update click speed when slider changes"""
        self.click_speed = int(value)
        self.speed_display.config(text=f"Current: {self.click_speed} clicks/sec")
        
    def setup_listeners(self):
        try:
            # Global hotkey for Ctrl+Alt+K
            self.hotkeys = GlobalHotKeys({
                '<ctrl>+<alt>+k': self.toggle_clicking
            })
            self.hotkeys.start()
            print("Global hotkey Ctrl+Alt+K registered successfully")
        except Exception as e:
            print(f"Failed to register global hotkey: {e}")
            messagebox.showwarning("Hotkey Warning", 
                                 f"Failed to register Ctrl+Alt+K hotkey: {e}\n\n" +
                                 "You may need to run as administrator or use the GUI buttons.")
        
        try:
            # Mouse listener for right-click detection
            self.mouse_listener = MouseListener(on_click=self.on_mouse_click)
            self.mouse_listener.start()
            print("Mouse listener started successfully")
        except Exception as e:
            print(f"Failed to start mouse listener: {e}")
            messagebox.showerror("Error", f"Failed to start mouse listener: {e}")
    
    def toggle_clicking(self):
        # This method is only used by Ctrl+Alt+K hotkey
        print("Ctrl+Alt+K hotkey pressed!")
        if self.clicking:
            print("Ctrl+Alt+K: Stopping auto-clicker")
            self.stop_clicking()
        else:
            print("Ctrl+Alt+K: Starting auto-clicker")
            self.start_clicking()
    
    def start_clicking(self):
        if not self.clicking:
            # Get current cursor position
            self.current_pos = self.mouse_controller.position
            self.clicking = True
            print(f"Starting auto-clicker at position: {self.current_pos}")
            self.status_label.config(text=f"Status: Clicking at {self.current_pos}")
            
            # Update button states
            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")
            
            # Start clicking thread
            self.click_thread = threading.Thread(target=self.click_loop, daemon=True)
            self.click_thread.start()
            print("Click thread started")
        else:
            print("Auto-clicker is already running")
    
    def stop_clicking(self):
        if self.clicking:
            self.clicking = False
            self.status_label.config(text="Status: Stopped")
            
            # Update button states
            self.start_btn.config(state="normal")
            self.stop_btn.config(state="disabled")
            
            if self.click_thread:
                self.click_thread.join(timeout=0.1)
    
    def click_loop(self):
        click_count = 0
        while self.clicking:
            try:
                # Move to the saved position and click
                self.mouse_controller.position = self.current_pos
                self.mouse_controller.click(Button.left, 1)
                click_count += 1
                
                # Print status every 100 clicks for debugging
                if click_count % 100 == 0:
                    print(f"Auto-clicked {click_count} times, still running: {self.clicking}")
                
                # Calculate delay based on click speed (clicks per second)
                delay = 1.0 / self.click_speed
                time.sleep(delay)
            except Exception as e:
                print(f"Click error: {e}")
                self.clicking = False
                break
        
        print(f"Click loop ended. Total clicks: {click_count}")
    
    def on_mouse_click(self, x, y, button, pressed):
        # Stop clicking on right-click press only
        # Ignore left clicks to prevent interference with auto-clicking
        if button == Button.right and pressed:
            if self.clicking:
                print(f"Right-click detected at ({x}, {y}), stopping auto-clicker")
                self.stop_clicking()
    
    def exit_app(self):
        self.stop_clicking()
        
        # Stop all listeners
        if self.hotkeys:
            self.hotkeys.stop()
        if self.mouse_listener:
            self.mouse_listener.stop()
        
        self.root.quit()
        self.root.destroy()
        sys.exit()
    
    def run(self):
        try:
            # Handle window close event
            self.root.protocol("WM_DELETE_WINDOW", self.exit_app)
            
            # Show instructions on startup
            messagebox.showinfo("Auto Clicker", 
                              "Instructions:\n\n" +
                              "• Press Ctrl+Alt+K to start/stop auto-clicking\n" +
                              "• Right-click anywhere to stop instantly\n" +
                              "• Auto-clicks at cursor position when activated\n\n" +
                              "Keep this window open while using the auto-clicker.")
            
            self.root.mainloop()
        except KeyboardInterrupt:
            self.exit_app()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            self.exit_app()

if __name__ == "__main__":
    try:
        app = AutoClicker()
        app.run()
    except Exception as e:
        print(f"Failed to start auto-clicker: {e}")
        input("Press Enter to exit...")