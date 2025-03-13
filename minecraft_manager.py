import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
import psutil
import threading
import time
from datetime import datetime

class MinecraftManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Minecraft Manager")
        self.root.geometry("600x400")
        
        # Configuration
        self.java_executable = "java"
        self.server_jar = "minecraft-server/spigot.jar"
        self.tlauncher_path = "TLauncher/TLauncher.jar"
        self.prism_path = "Prism Launcher.app/Contents/MacOS/PrismLauncher"
        self.server_memory = "-Xms1G -Xmx2G"
        self.tlauncher_memory = "-Xms512M -Xmx1G"
        self.prism_memory = "-Xms512M -Xmx1G"
        
        # Process tracking
        self.server_process = None
        self.tlauncher_process = None
        self.prism_process = None
        
        # Create logs directory
        os.makedirs("logs", exist_ok=True)
        
        self.setup_gui()
        self.setup_status_thread()
        
    def setup_gui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Minecraft Manager", font=('Helvetica', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Buttons frame
        buttons_frame = ttk.LabelFrame(main_frame, text="Controls", padding="5")
        buttons_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Server controls
        ttk.Button(buttons_frame, text="Start Server", command=self.start_server).grid(row=0, column=0, padx=5)
        ttk.Button(buttons_frame, text="Stop Server", command=self.stop_server).grid(row=0, column=1, padx=5)
        
        # TLauncher controls
        ttk.Button(buttons_frame, text="Start TLauncher", command=self.start_tlauncher).grid(row=1, column=0, padx=5)
        ttk.Button(buttons_frame, text="Stop TLauncher", command=self.stop_tlauncher).grid(row=1, column=1, padx=5)
        
        # PrismLauncher controls
        ttk.Button(buttons_frame, text="Start PrismLauncher", command=self.start_prism).grid(row=2, column=0, padx=5)
        ttk.Button(buttons_frame, text="Stop PrismLauncher", command=self.stop_prism).grid(row=2, column=1, padx=5)
        
        # Quick start buttons
        quick_start_frame = ttk.LabelFrame(main_frame, text="Quick Start", padding="5")
        quick_start_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(quick_start_frame, text="Start All", command=self.start_all).grid(row=0, column=0, padx=5)
        ttk.Button(quick_start_frame, text="Stop All", command=self.stop_all).grid(row=0, column=1, padx=5)
        
        # Status frame
        status_frame = ttk.LabelFrame(main_frame, text="Status", padding="5")
        status_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        self.server_status = ttk.Label(status_frame, text="Server: Stopped")
        self.server_status.grid(row=0, column=0, sticky=tk.W)
        
        self.tlauncher_status = ttk.Label(status_frame, text="TLauncher: Stopped")
        self.tlauncher_status.grid(row=1, column=0, sticky=tk.W)
        
        self.prism_status = ttk.Label(status_frame, text="PrismLauncher: Stopped")
        self.prism_status.grid(row=2, column=0, sticky=tk.W)
        
        # Log frame
        log_frame = ttk.LabelFrame(main_frame, text="Logs", padding="5")
        log_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        self.log_text = tk.Text(log_frame, height=10, width=60)
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        scrollbar = ttk.Scrollbar(log_frame, orient=tk.VERTICAL, command=self.log_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.log_text['yscrollcommand'] = scrollbar.set
        
    def setup_status_thread(self):
        self.status_thread = threading.Thread(target=self.update_status, daemon=True)
        self.status_thread.start()
        
    def update_status(self):
        while True:
            self.root.after(0, self.update_status_labels)
            time.sleep(1)
            
    def update_status_labels(self):
        self.server_status.config(text=f"Server: {'Running' if self.is_process_running(self.server_process) else 'Stopped'}")
        self.tlauncher_status.config(text=f"TLauncher: {'Running' if self.is_process_running(self.tlauncher_process) else 'Stopped'}")
        self.prism_status.config(text=f"PrismLauncher: {'Running' if self.is_process_running(self.prism_process) else 'Stopped'}")
        
    def is_process_running(self, process):
        if process is None:
            return False
        try:
            process.poll()
            return process.returncode is None
        except:
            return False
            
    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
        
    def start_server(self):
        if not os.path.exists(self.server_jar):
            messagebox.showerror("Error", f"Server JAR not found at {self.server_jar}")
            return
            
        try:
            with open("logs/server.log", "a") as f:
                self.server_process = subprocess.Popen(
                    [self.java_executable, self.server_memory, "-jar", self.server_jar, "nogui"],
                    stdout=f,
                    stderr=subprocess.STDOUT
                )
            self.log("Started Minecraft server")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start server: {str(e)}")
            
    def stop_server(self):
        if self.server_process:
            self.server_process.terminate()
            self.server_process = None
            self.log("Stopped Minecraft server")
            
    def start_tlauncher(self):
        if not os.path.exists(self.tlauncher_path):
            messagebox.showerror("Error", f"TLauncher JAR not found at {self.tlauncher_path}")
            return
            
        try:
            with open("logs/tlauncher.log", "a") as f:
                self.tlauncher_process = subprocess.Popen(
                    [self.java_executable, self.tlauncher_memory, "-jar", self.tlauncher_path],
                    stdout=f,
                    stderr=subprocess.STDOUT
                )
            self.log("Started TLauncher")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start TLauncher: {str(e)}")
            
    def stop_tlauncher(self):
        if self.tlauncher_process:
            self.tlauncher_process.terminate()
            self.tlauncher_process = None
            self.log("Stopped TLauncher")
            
    def start_prism(self):
        if not os.path.exists(self.prism_path):
            messagebox.showerror("Error", f"PrismLauncher not found at {self.prism_path}")
            return
            
        try:
            with open("logs/prism.log", "a") as f:
                self.prism_process = subprocess.Popen(
                    [self.prism_path],
                    stdout=f,
                    stderr=subprocess.STDOUT
                )
            self.log("Started PrismLauncher")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start PrismLauncher: {str(e)}")
            
    def stop_prism(self):
        if self.prism_process:
            self.prism_process.terminate()
            self.prism_process = None
            self.log("Stopped PrismLauncher")
            
    def start_all(self):
        self.start_server()
        time.sleep(2)  # Wait for server to initialize
        self.start_tlauncher()
        self.start_prism()
        
    def stop_all(self):
        self.stop_server()
        self.stop_tlauncher()
        self.stop_prism()

if __name__ == "__main__":
    root = tk.Tk()
    app = MinecraftManager(root)
    root.mainloop() 