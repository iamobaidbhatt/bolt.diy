#!/usr/bin/env python3
"""
Hotstar Cookie Validator Tool
A comprehensive tool to validate Hotstar cookies from files or folders
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import re
import time
from datetime import datetime
from pathlib import Path
import json

class HotstarCookieValidator:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotstar Cookie Validator")
        self.root.geometry("1000x700")
        self.root.configure(bg='#1a1a1a')
        
        # Style configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure colors
        self.bg_color = '#1a1a1a'
        self.card_color = '#2d2d2d'
        self.accent_color = '#ff6b35'
        self.text_color = '#ffffff'
        self.success_color = '#00d084'
        self.error_color = '#ff4757'
        
        self.cookies_data = []
        self.valid_cookies = []
        self.invalid_cookies = []
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Main title
        title_label = tk.Label(
            self.root,
            text="🌟 Hotstar Cookie Validator",
            font=("Arial", 24, "bold"),
            bg=self.bg_color,
            fg=self.accent_color
        )
        title_label.pack(pady=20)
        
        # Input section
        input_frame = tk.Frame(self.root, bg=self.bg_color)
        input_frame.pack(pady=10, padx=20, fill='x')
        
        # File selection buttons
        btn_frame = tk.Frame(input_frame, bg=self.bg_color)
        btn_frame.pack(fill='x', pady=10)
        
        select_file_btn = tk.Button(
            btn_frame,
            text="📁 Select Cookie File",
            command=self.select_file,
            bg=self.accent_color,
            fg='white',
            font=("Arial", 12, "bold"),
            relief='flat',
            padx=20,
            pady=10
        )
        select_file_btn.pack(side='left', padx=5)
        
        select_folder_btn = tk.Button(
            btn_frame,
            text="📂 Select Folder",
            command=self.select_folder,
            bg=self.accent_color,
            fg='white',
            font=("Arial", 12, "bold"),
            relief='flat',
            padx=20,
            pady=10
        )
        select_folder_btn.pack(side='left', padx=5)
        
        validate_btn = tk.Button(
            btn_frame,
            text="✅ Validate Cookies",
            command=self.validate_cookies,
            bg=self.success_color,
            fg='white',
            font=("Arial", 12, "bold"),
            relief='flat',
            padx=20,
            pady=10
        )
        validate_btn.pack(side='left', padx=5)
        
        export_btn = tk.Button(
            btn_frame,
            text="💾 Export Valid Cookies",
            command=self.export_valid_cookies,
            bg='#3742fa',
            fg='white',
            font=("Arial", 12, "bold"),
            relief='flat',
            padx=20,
            pady=10
        )
        export_btn.pack(side='right', padx=5)
        
        # Selected files display
        self.selected_files_label = tk.Label(
            input_frame,
            text="No files selected",
            bg=self.bg_color,
            fg='#888888',
            font=("Arial", 10)
        )
        self.selected_files_label.pack(pady=5)
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            input_frame,
            variable=self.progress_var,
            maximum=100,
            length=400
        )
        self.progress_bar.pack(pady=10)
        
        # Results section
        results_frame = tk.Frame(self.root, bg=self.bg_color)
        results_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Statistics
        stats_frame = tk.Frame(results_frame, bg=self.card_color, relief='raised', bd=2)
        stats_frame.pack(fill='x', pady=5)
        
        self.stats_label = tk.Label(
            stats_frame,
            text="📊 Statistics: Total: 0 | Valid: 0 | Invalid: 0",
            bg=self.card_color,
            fg=self.text_color,
            font=("Arial", 12, "bold"),
            pady=10
        )
        self.stats_label.pack()
        
        # Results notebook (tabs)
        self.notebook = ttk.Notebook(results_frame)
        self.notebook.pack(fill='both', expand=True, pady=10)
        
        # Valid cookies tab
        valid_frame = tk.Frame(self.notebook, bg=self.bg_color)
        self.notebook.add(valid_frame, text="✅ Valid Cookies")
        
        self.valid_text = tk.Text(
            valid_frame,
            bg=self.card_color,
            fg=self.success_color,
            font=("Consolas", 10),
            wrap='word'
        )
        valid_scroll = tk.Scrollbar(valid_frame, command=self.valid_text.yview)
        self.valid_text.config(yscrollcommand=valid_scroll.set)
        self.valid_text.pack(side='left', fill='both', expand=True)
        valid_scroll.pack(side='right', fill='y')
        
        # Invalid cookies tab
        invalid_frame = tk.Frame(self.notebook, bg=self.bg_color)
        self.notebook.add(invalid_frame, text="❌ Invalid Cookies")
        
        self.invalid_text = tk.Text(
            invalid_frame,
            bg=self.card_color,
            fg=self.error_color,
            font=("Consolas", 10),
            wrap='word'
        )
        invalid_scroll = tk.Scrollbar(invalid_frame, command=self.invalid_text.yview)
        self.invalid_text.config(yscrollcommand=invalid_scroll.set)
        self.invalid_text.pack(side='left', fill='both', expand=True)
        invalid_scroll.pack(side='right', fill='y')
        
        # Status bar
        self.status_label = tk.Label(
            self.root,
            text="Ready to validate cookies",
            bg=self.card_color,
            fg=self.text_color,
            font=("Arial", 10),
            relief='sunken',
            anchor='w',
            padx=10
        )
        self.status_label.pack(side='bottom', fill='x')
    
    def select_file(self):
        """Select a single cookie file"""
        file_path = filedialog.askopenfilename(
            title="Select Cookie File",
            filetypes=[
                ("Text files", "*.txt"),
                ("Cookie files", "*.cookies"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self.selected_files = [file_path]
            self.selected_files_label.config(
                text=f"Selected: {os.path.basename(file_path)}",
                fg=self.success_color
            )
            self.status_label.config(text=f"File selected: {file_path}")
    
    def select_folder(self):
        """Select a folder to scan for cookie files"""
        folder_path = filedialog.askdirectory(title="Select Folder")
        
        if folder_path:
            # Find all potential cookie files
            cookie_files = []
            for ext in ['*.txt', '*.cookies', '*.dat']:
                cookie_files.extend(Path(folder_path).glob(f"**/{ext}"))
            
            self.selected_files = [str(f) for f in cookie_files]
            
            if cookie_files:
                self.selected_files_label.config(
                    text=f"Found {len(cookie_files)} files in folder",
                    fg=self.success_color
                )
                self.status_label.config(text=f"Folder selected: {folder_path}")
            else:
                self.selected_files_label.config(
                    text="No cookie files found in folder",
                    fg=self.error_color
                )
    
    def parse_cookie_line(self, line):
        """Parse a single cookie line in Netscape format"""
        line = line.strip()
        if not line or line.startswith('#'):
            return None
        
        parts = line.split('\t')
        if len(parts) < 6:
            return None
        
        try:
            return {
                'domain': parts[0],
                'domain_specified': parts[1].upper() == 'TRUE',
                'path': parts[2],
                'secure': parts[3].upper() == 'TRUE',
                'expires': int(parts[4]) if parts[4] != '0' and parts[4] != '-1' else 0,
                'name': parts[5],
                'value': parts[6] if len(parts) > 6 else '',
                'raw_line': line
            }
        except (ValueError, IndexError):
            return None
    
    def is_hotstar_cookie(self, cookie):
        """Check if cookie is related to Hotstar"""
        hotstar_domains = [
            'hotstar.com',
            '.hotstar.com',
            'www.hotstar.com',
            '.hses7-vod-cf-ace.cdn.hotstar.com'
        ]
        
        hotstar_names = [
            'deviceId', 'userHID', 'userPID', 'userUP', 'sessionUserUP',
            'CloudFront-Key-Pair-Id', 'CloudFront-Policy', 'CloudFront-Signature',
            'SELECTED__LANGUAGE', '_ga', '_gid', 'loc', 'geo', '_fbp'
        ]
        
        domain_match = any(domain in cookie['domain'] for domain in hotstar_domains)
        name_match = cookie['name'] in hotstar_names
        
        return domain_match or name_match
    
    def validate_cookie(self, cookie):
        """Validate a single cookie"""
        issues = []
        
        # Check if it's a Hotstar cookie
        if not self.is_hotstar_cookie(cookie):
            issues.append("Not a Hotstar cookie")
        
        # Check expiry
        if cookie['expires'] > 0:
            current_time = int(time.time())
            if cookie['expires'] < current_time:
                expires_date = datetime.fromtimestamp(cookie['expires'])
                issues.append(f"Expired on {expires_date.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Check domain format
        if not cookie['domain']:
            issues.append("Empty domain")
        
        # Check essential Hotstar cookies
        essential_cookies = ['userUP', 'userHID', 'userPID']
        if cookie['name'] in essential_cookies and not cookie['value']:
            issues.append("Essential cookie with empty value")
        
        # Check JWT tokens (userUP, sessionUserUP)
        if cookie['name'] in ['userUP', 'sessionUserUP']:
            if not self.validate_jwt_format(cookie['value']):
                issues.append("Invalid JWT token format")
        
        # Check CloudFront cookies
        if 'CloudFront' in cookie['name']:
            if not cookie['secure']:
                issues.append("CloudFront cookie should be secure")
        
        return len(issues) == 0, issues
    
    def validate_jwt_format(self, token):
        """Basic JWT format validation"""
        if not token:
            return False
        
        parts = token.split('.')
        if len(parts) != 3:
            return False
        
        # Check if each part is base64-like
        import string
        valid_chars = string.ascii_letters + string.digits + '-_='
        
        for part in parts:
            if not all(c in valid_chars for c in part):
                return False
        
        return True
    
    def validate_cookies(self):
        """Validate all cookies from selected files"""
        if not hasattr(self, 'selected_files') or not self.selected_files:
            messagebox.showwarning("No Files", "Please select files or folder first")
            return
        
        self.valid_cookies = []
        self.invalid_cookies = []
        all_cookies = []
        
        total_files = len(self.selected_files)
        
        for i, file_path in enumerate(self.selected_files):
            self.progress_var.set((i / total_files) * 100)
            self.root.update_idletasks()
            
            self.status_label.config(text=f"Processing: {os.path.basename(file_path)}")
            
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line_num, line in enumerate(f, 1):
                        cookie = self.parse_cookie_line(line)
                        if cookie:
                            cookie['file'] = file_path
                            cookie['line_number'] = line_num
                            all_cookies.append(cookie)
                            
                            is_valid, issues = self.validate_cookie(cookie)
                            
                            if is_valid:
                                self.valid_cookies.append(cookie)
                            else:
                                cookie['issues'] = issues
                                self.invalid_cookies.append(cookie)
            
            except Exception as e:
                messagebox.showerror("Error", f"Error reading {file_path}: {str(e)}")
        
        self.progress_var.set(100)
        self.display_results()
        self.status_label.config(text="Validation complete")
    
    def display_results(self):
        """Display validation results"""
        # Update statistics
        total = len(self.valid_cookies) + len(self.invalid_cookies)
        valid_count = len(self.valid_cookies)
        invalid_count = len(self.invalid_cookies)
        
        self.stats_label.config(
            text=f"📊 Statistics: Total: {total} | Valid: {valid_count} | Invalid: {invalid_count}"
        )
        
        # Clear previous results
        self.valid_text.delete(1.0, tk.END)
        self.invalid_text.delete(1.0, tk.END)
        
        # Display valid cookies
        if self.valid_cookies:
            self.valid_text.insert(tk.END, f"✅ VALID HOTSTAR COOKIES ({len(self.valid_cookies)})\n")
            self.valid_text.insert(tk.END, "=" * 60 + "\n\n")
            
            for cookie in self.valid_cookies:
                expires_str = "Session"
                if cookie['expires'] > 0:
                    expires_date = datetime.fromtimestamp(cookie['expires'])
                    expires_str = expires_date.strftime('%Y-%m-%d %H:%M:%S')
                
                cookie_info = (
                    f"Cookie: {cookie['name']}\n"
                    f"Domain: {cookie['domain']}\n"
                    f"Expires: {expires_str}\n"
                    f"File: {os.path.basename(cookie['file'])}\n"
                    f"Raw: {cookie['raw_line']}\n"
                    f"{'-' * 40}\n\n"
                )
                self.valid_text.insert(tk.END, cookie_info)
        else:
            self.valid_text.insert(tk.END, "No valid Hotstar cookies found.")
        
        # Display invalid cookies
        if self.invalid_cookies:
            self.invalid_text.insert(tk.END, f"❌ INVALID COOKIES ({len(self.invalid_cookies)})\n")
            self.invalid_text.insert(tk.END, "=" * 60 + "\n\n")
            
            for cookie in self.invalid_cookies:
                issues_str = ", ".join(cookie['issues'])
                cookie_info = (
                    f"Cookie: {cookie['name']}\n"
                    f"Domain: {cookie['domain']}\n"
                    f"Issues: {issues_str}\n"
                    f"File: {os.path.basename(cookie['file'])}\n"
                    f"Raw: {cookie['raw_line']}\n"
                    f"{'-' * 40}\n\n"
                )
                self.invalid_text.insert(tk.END, cookie_info)
        else:
            self.invalid_text.insert(tk.END, "No invalid cookies found.")
    
    def export_valid_cookies(self):
        """Export valid cookies to a file"""
        if not self.valid_cookies:
            messagebox.showwarning("No Valid Cookies", "No valid cookies to export")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Save Valid Cookies",
            defaultextension=".txt",
            filetypes=[
                ("Text files", "*.txt"),
                ("Cookie files", "*.cookies"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write("# Valid Hotstar Cookies\n")
                    f.write(f"# Exported on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write(f"# Total valid cookies: {len(self.valid_cookies)}\n\n")
                    
                    for cookie in self.valid_cookies:
                        f.write(cookie['raw_line'] + '\n')
                
                messagebox.showinfo("Export Successful", f"Valid cookies exported to {file_path}")
                self.status_label.config(text=f"Exported {len(self.valid_cookies)} valid cookies")
                
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export cookies: {str(e)}")

def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = HotstarCookieValidator(root)
    root.mainloop()

if __name__ == "__main__":
    main()