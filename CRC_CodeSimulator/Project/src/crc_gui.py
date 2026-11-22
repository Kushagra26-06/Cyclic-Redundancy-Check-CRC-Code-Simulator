"""
CRC Code Simulator - Professional Edition
Advanced GUI with enhanced visualization and detailed step-by-step analysis
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from crc_simulator import CRCSimulator
import random


class CompleteCRCGUI:
    """Professional CRC Simulator GUI with advanced features"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 CRC Code Simulator - Professional Edition")
        self.root.geometry("1400x850")
        self.root.configure(bg='#f1f5f9')
        
        self.simulator = CRCSimulator(polynomial="1101")
        
        self.setup_styles()
        self.create_main_interface()
        self.center_window()
    
    def setup_styles(self):
        """Modern professional styling"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Modern color scheme
        colors = {
            'primary': '#2563eb',
            'secondary': '#64748b',
            'success': '#10b981',
            'error': '#ef4444',
            'warning': '#f59e0b',
            'bg': '#ffffff',
            'bg_alt': '#f8fafc',
            'text': '#1e293b',
            'text_light': '#64748b'
        }
        
        # Card styling
        self.style.configure('Card.TFrame',
                           background='#ffffff',
                           relief='raised',
                           borderwidth=2)
        
        # Button styling
        self.style.configure('Primary.TButton',
                           font=('Segoe UI', 11, 'bold'),
                           padding=15,
                           background=colors['primary'],
                           foreground='white',
                           borderwidth=0,
                           relief='flat')
        
        self.style.configure('Success.TButton',
                           font=('Segoe UI', 11, 'bold'),
                           padding=15,
                           background=colors['success'],
                           foreground='white',
                           borderwidth=0,
                           relief='flat')
        
        self.style.configure('Secondary.TButton',
                           font=('Segoe UI', 11),
                           padding=12,
                           background=colors['secondary'],
                           foreground='white',
                           borderwidth=0,
                           relief='flat')
        
        self.style.map('Primary.TButton',
                       background=[('active', '#1d4ed8'),
                                  ('pressed', '#1e40af')])
        self.style.map('Success.TButton',
                       background=[('active', '#059669'),
                                  ('pressed', '#047857')])
        self.style.map('Secondary.TButton',
                       background=[('active', '#475569'),
                                  ('pressed', '#334155')])
        
        # Label styling
        self.style.configure('Title.TLabel',
                           font=('Segoe UI', 32, 'bold'),
                           background='#0f172a',
                           foreground='#ffffff')
        
        self.style.configure('Subtitle.TLabel',
                           font=('Segoe UI', 11),
                           background='#0f172a',
                           foreground='#94a3b8')
        
        self.style.configure('Header.TLabel',
                           font=('Segoe UI', 14, 'bold'),
                           background='#ffffff',
                           foreground='#1e293b')
        
        self.style.configure('Label.TLabel',
                           font=('Segoe UI', 10),
                           background='#ffffff',
                           foreground='#1e293b')
        
        self.style.configure('Info.TLabel',
                           font=('Segoe UI', 9),
                           background='#ffffff',
                           foreground='#64748b')
        
        # Entry styling
        self.style.configure('Modern.TEntry',
                           font=('Segoe UI', 11),
                           fieldbackground='#f8fafc',
                           borderwidth=2,
                           relief='solid')
        
        # Notebook styling
        self.style.configure('Modern.TNotebook',
                           background='#f1f5f9',
                           borderwidth=0,
                           tabposition='n')
        
        self.style.configure('Modern.TNotebook.Tab',
                           font=('Segoe UI', 11, 'bold'),
                           padding=[25, 12],
                           background='#e2e8f0',
                           foreground='#475569',
                           borderwidth=0)
        
        self.style.map('Modern.TNotebook.Tab',
                       background=[('selected', '#ffffff'),
                                 ('active', '#f1f5f9')],
                       foreground=[('selected', colors['primary']),
                                 ('active', '#1e293b')])
    
    def create_main_interface(self):
        """Create complete interface with tabs"""
        # Header
        self.create_header()
        
        # Main content - two column layout
        main_container = tk.Frame(self.root, bg='#f1f5f9')
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Left panel - Notebook (tabs)
        left_panel = tk.Frame(main_container, bg='#f1f5f9')
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(left_panel, style='Modern.TNotebook')
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.create_custom_data_tab()
        self.create_random_data_tab()
        self.create_burst_error_tab()
        self.create_polynomial_test_tab()
        self.create_all_scenarios_tab()
        
        # Set default tab
        self.notebook.select(0)
        
        # Right panel - Results
        right_panel = tk.Frame(main_container, bg='#f1f5f9')
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Results panel (right side)
        self.create_results_panel(right_panel)
    
    def create_header(self):
        """Create modern header"""
        header = tk.Frame(self.root, bg='#0f172a', height=100)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title_frame = tk.Frame(header, bg='#0f172a')
        title_frame.pack(expand=True)
        
        tk.Label(title_frame, text="🔐 CRC Code Simulator",
                font=('Segoe UI', 28, 'bold'),
                bg='#0f172a', fg='#ffffff').pack(pady=(20, 5))
        
        tk.Label(title_frame, text="Advanced Error Detection & Correction Tool",
                font=('Segoe UI', 12),
                bg='#0f172a', fg='#94a3b8').pack()
        
        # Add status bar in header
        status_frame = tk.Frame(header, bg='#0f172a')
        status_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=(5, 0))
        
        tk.Label(status_frame, text="● System Ready",
                font=('Segoe UI', 9),
                bg='#0f172a', fg='#10b981').pack(side=tk.LEFT)
    
    def create_custom_data_tab(self):
        """Custom data testing tab"""
        tab = tk.Frame(self.notebook, bg='#f1f5f9', padx=35, pady=25)
        self.notebook.add(tab, text="Custom Data")
        
        # Card
        card = tk.Frame(tab, bg='#ffffff', relief='raised', borderwidth=2, padx=30, pady=25)
        card.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(card, text="🎯 Custom Data Testing",
                font=('Segoe UI', 18, 'bold'),
                bg='#ffffff', fg='#2563eb').pack(pady=(0, 25))
        
        # Input fields
        self.create_input_field(card, "Binary Data:", "custom_data", "1011001")
        self.create_input_field(card, "Error Positions (space-separated):", "custom_errors", "")
        
        # Polynomial selection
        tk.Label(card, text="Generator Polynomial:",
                font=('Segoe UI', 10, 'bold'),
                bg='white', fg='#1e293b').pack(anchor='w', pady=(15, 5))
        
        self.custom_poly = tk.StringVar(value="CRC-3 (1101)")
        poly_combo = ttk.Combobox(card, textvariable=self.custom_poly,
                                 values=["CRC-3 (1101)", "CRC-4 (10011)", 
                                        "CRC-8 (100000111)", "CRC-16 (10001000000100001)"],
                                 state='readonly', width=40)
        poly_combo.pack(pady=(0, 20))
        poly_combo.bind('<<ComboboxSelected>>', lambda e: self.update_poly('custom'))
        
        # Buttons
        btn_frame = tk.Frame(card, bg='#ffffff')
        btn_frame.pack(pady=15)
        
        ttk.Button(btn_frame, text="▶ Run Simulation",
                 style='Primary.TButton',
                 command=lambda: self.run_custom_test()).pack(side=tk.LEFT, padx=8)
        
        ttk.Button(btn_frame, text="🗑 Clear",
                 style='Secondary.TButton',
                 command=lambda: self.clear_field('custom')).pack(side=tk.LEFT, padx=8)
    
    def create_random_data_tab(self):
        """Random data testing tab"""
        tab = tk.Frame(self.notebook, bg='#f1f5f9', padx=35, pady=25)
        self.notebook.add(tab, text="Random Data")
        
        card = tk.Frame(tab, bg='#ffffff', relief='raised', borderwidth=2, padx=30, pady=25)
        card.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(card, text="🎲 Random Data Testing",
                font=('Segoe UI', 18, 'bold'),
                bg='#ffffff', fg='#2563eb').pack(pady=(0, 25))
        
        # Data length
        tk.Label(card, text="Data Length (8-32 recommended):",
                font=('Segoe UI', 10, 'bold'),
                bg='white', fg='#1e293b').pack(anchor='w', pady=(0, 5))
        
        self.random_length = ttk.Entry(card, style='Modern.TEntry', width=20)
        self.random_length.pack(pady=(0, 15))
        self.random_length.insert(0, "16")
        
        # Number of errors
        tk.Label(card, text="Number of Random Errors (0-5):",
                font=('Segoe UI', 10, 'bold'),
                bg='white', fg='#1e293b').pack(anchor='w', pady=(0, 5))
        
        self.random_errors = ttk.Entry(card, style='Modern.TEntry', width=20)
        self.random_errors.pack(pady=(0, 15))
        self.random_errors.insert(0, "2")
        
        # Polynomial
        tk.Label(card, text="Generator Polynomial:",
                font=('Segoe UI', 10, 'bold'),
                bg='white', fg='#1e293b').pack(anchor='w', pady=(0, 5))
        
        self.random_poly = tk.StringVar(value="CRC-3 (1101)")
        poly_combo = ttk.Combobox(card, textvariable=self.random_poly,
                                 values=["CRC-3 (1101)", "CRC-4 (10011)", 
                                        "CRC-8 (100000111)", "CRC-16 (10001000000100001)"],
                                 state='readonly', width=40)
        poly_combo.pack(pady=(0, 20))
        poly_combo.bind('<<ComboboxSelected>>', lambda e: self.update_poly('random'))
        
        # Buttons
        btn_frame = tk.Frame(card, bg='#ffffff')
        btn_frame.pack(pady=15)
        
        ttk.Button(btn_frame, text="🎲 Generate & Test",
                 style='Primary.TButton',
                 command=lambda: self.run_random_test()).pack(side=tk.LEFT, padx=8)
        
        ttk.Button(btn_frame, text="🗑 Clear",
                 style='Secondary.TButton',
                 command=lambda: self.clear_field('random')).pack(side=tk.LEFT, padx=8)
    
    def create_burst_error_tab(self):
        """Burst error testing tab"""
        tab = tk.Frame(self.notebook, bg='#f1f5f9', padx=35, pady=25)
        self.notebook.add(tab, text="Burst Error")
        
        card = tk.Frame(tab, bg='#ffffff', relief='raised', borderwidth=2, padx=30, pady=25)
        card.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(card, text="⚡ Burst Error Detection",
                font=('Segoe UI', 18, 'bold'),
                bg='#ffffff', fg='#2563eb').pack(pady=(0, 25))
        
        # Input data
        self.create_input_field(card, "Binary Data:", "burst_data", "1011001")
        
        # Burst length
        tk.Label(card, text="Burst Error Length:",
                font=('Segoe UI', 10, 'bold'),
                bg='white', fg='#1e293b').pack(anchor='w', pady=(15, 5))
        
        self.burst_length = ttk.Entry(card, style='Modern.TEntry', width=20)
        self.burst_length.pack(pady=(0, 15))
        self.burst_length.insert(0, "3")
        
        # Polynomial
        tk.Label(card, text="Generator Polynomial:",
                font=('Segoe UI', 10, 'bold'),
                bg='white', fg='#1e293b').pack(anchor='w', pady=(0, 5))
        
        self.burst_poly = tk.StringVar(value="CRC-3 (1101)")
        poly_combo = ttk.Combobox(card, textvariable=self.burst_poly,
                                 values=["CRC-3 (1101)", "CRC-4 (10011)", 
                                        "CRC-8 (100000111)", "CRC-16 (10001000000100001)"],
                                 state='readonly', width=40)
        poly_combo.pack(pady=(0, 20))
        poly_combo.bind('<<ComboboxSelected>>', lambda e: self.update_poly('burst'))
        
        # Buttons
        btn_frame = tk.Frame(card, bg='#ffffff')
        btn_frame.pack(pady=15)
        
        ttk.Button(btn_frame, text="⚡ Test Burst Error",
                 style='Primary.TButton',
                 command=lambda: self.run_burst_test()).pack(side=tk.LEFT, padx=8)
        
        ttk.Button(btn_frame, text="🗑 Clear",
                 style='Secondary.TButton',
                 command=lambda: self.clear_field('burst')).pack(side=tk.LEFT, padx=8)
    
    def create_polynomial_test_tab(self):
        """Different polynomial testing tab"""
        tab = tk.Frame(self.notebook, bg='#f1f5f9', padx=35, pady=25)
        self.notebook.add(tab, text="Polynomial Test")
        
        card = tk.Frame(tab, bg='#ffffff', relief='raised', borderwidth=2, padx=30, pady=25)
        card.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(card, text="🔬 Polynomial Comparison",
                font=('Segoe UI', 18, 'bold'),
                bg='#ffffff', fg='#2563eb').pack(pady=(0, 25))
        
        # Input data
        self.create_input_field(card, "Binary Data:", "poly_data", "1101011011")
        
        # Polynomial comparison
        tk.Label(card, text="Compare Different Polynomials:",
                font=('Segoe UI', 10, 'bold'),
                bg='white', fg='#1e293b').pack(anchor='w', pady=(15, 5))
        
        self.poly_test_selection = tk.StringVar(value="CRC-3 vs CRC-4")
        poly_combo = ttk.Combobox(card, textvariable=self.poly_test_selection,
                                 values=["CRC-3 vs CRC-4", "CRC-4 vs CRC-8", "CRC-8 vs CRC-16"],
                                 state='readonly', width=40)
        poly_combo.pack(pady=(0, 15))
        
        # Error injection
        tk.Label(card, text="Error Positions (for testing):",
                font=('Segoe UI', 10, 'bold'),
                bg='#ffffff', fg='#1e293b').pack(anchor='w', pady=(0, 5))
        
        self.poly_errors_entry = ttk.Entry(card, style='Modern.TEntry', width=30)
        self.poly_errors_entry.pack(pady=(0, 20))
        self.poly_errors_entry.insert(0, "3 7")
        
        # Buttons
        btn_frame = tk.Frame(card, bg='#ffffff')
        btn_frame.pack(pady=15)
        
        ttk.Button(btn_frame, text="🔬 Compare Polynomials",
                 style='Primary.TButton',
                 command=lambda: self.run_poly_test()).pack(side=tk.LEFT, padx=8)
        
        ttk.Button(btn_frame, text="🗑 Clear",
                 style='Secondary.TButton',
                 command=lambda: self.clear_field('poly')).pack(side=tk.LEFT, padx=8)
    
    def create_all_scenarios_tab(self):
        """All scenarios demo tab"""
        tab = tk.Frame(self.notebook, bg='#f1f5f9', padx=35, pady=25)
        self.notebook.add(tab, text="All Scenarios")
        
        card = tk.Frame(tab, bg='#ffffff', relief='raised', borderwidth=2, padx=30, pady=25)
        card.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(card, text="🚀 Complete Demonstration",
                font=('Segoe UI', 18, 'bold'),
                bg='#ffffff', fg='#2563eb').pack(pady=(0, 25))
        
        tk.Label(card, text="Run all predefined test scenarios to see CRC capabilities:",
                font=('Segoe UI', 10),
                bg='white', fg='#64748b').pack(pady=(0, 20))
        
        # Scenarios list
        scenarios = [
            "✓ Error-free transmission",
            "✓ Single bit error detection",
            "✓ Double bit error detection",
            "✓ Multiple bit errors",
            "✓ Burst error detection",
            "✓ Different polynomial demonstration"
        ]
        
        for scenario in scenarios:
            tk.Label(card, text=scenario,
                    font=('Segoe UI', 11),
                    bg='white', fg='#1e293b').pack(anchor='w', pady=5)
        
        # Buttons
        btn_frame = tk.Frame(card, bg='#ffffff')
        btn_frame.pack(pady=30)
        
        ttk.Button(btn_frame, text="🚀 Run All Scenarios",
                 style='Success.TButton',
                 command=lambda: self.run_all_scenarios()).pack(side=tk.LEFT, padx=8)
        
        ttk.Button(btn_frame, text="🗑 Clear Results",
                 style='Secondary.TButton',
                 command=self.clear_results).pack(side=tk.LEFT, padx=8)
    
    def create_input_field(self, parent, label_text, field_name, default_value):
        """Create labeled input field"""
        tk.Label(parent, text=label_text,
                font=('Segoe UI', 10, 'bold'),
                bg='#ffffff', fg='#1e293b').pack(anchor='w', pady=(10, 5))
        
        entry = ttk.Entry(parent, style='Modern.TEntry', width=50)
        entry.pack(pady=(0, 10))
        entry.insert(0, default_value)
        
        # Store reference
        setattr(self, f"{field_name}_entry", entry)
    
    def create_results_panel(self, parent):
        """Create results display panel"""
        results_frame = tk.Frame(parent, bg='#ffffff', relief='raised', borderwidth=2, padx=20, pady=20)
        results_frame.pack(fill=tk.BOTH, expand=True, pady=(15, 0))
        
        # Header with gradient effect
        header_frame = tk.Frame(results_frame, bg='#f1f5f9', relief='raised', borderwidth=1)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(header_frame, text="📊 Simulation Results",
                font=('Segoe UI', 15, 'bold'),
                bg='#f1f5f9', fg='#1e293b').pack(side=tk.LEFT, padx=15, pady=10)
        
        self.status_label = tk.Label(header_frame, text="● Ready",
                                    font=('Segoe UI', 11, 'bold'),
                                    bg='#f1f5f9', fg='#64748b')
        self.status_label.pack(side=tk.RIGHT, padx=15, pady=10)
        
        # Results text
        self.results_text = scrolledtext.ScrolledText(results_frame,
                                                     font=('Consolas', 10),
                                                     bg='#f8fafc',
                                                     fg='#1e293b',
                                                     wrap=tk.WORD,
                                                     height=30,
                                                     padx=15,
                                                     pady=15,
                                                     relief='flat')
        self.results_text.pack(fill=tk.BOTH, expand=True)
        
        # Text styling
        self.results_text.tag_config('success', foreground='#10b981', font=('Consolas', 10, 'bold'))
        self.results_text.tag_config('error', foreground='#ef4444', font=('Consolas', 10, 'bold'))
        self.results_text.tag_config('header', font=('Consolas', 11, 'bold'), foreground='#2563eb')
        self.results_text.tag_config('step', font=('Consolas', 10, 'bold'), foreground='#64748b')
        self.results_text.tag_config('info', foreground='#64748b', font=('Consolas', 10))
        self.results_text.tag_config('warning', foreground='#f59e0b', font=('Consolas', 10, 'bold'))
    
    def center_window(self):
        """Center window on screen"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() - 1400) // 2
        y = (self.root.winfo_screenheight() - 850) // 2
        self.root.geometry(f'1400x850+{x}+{y}')
    
    def update_poly(self, mode):
        """Update polynomial based on selection"""
        poly_map = {
            "CRC-3 (1101)": "1101",
            "CRC-4 (10011)": "10011",
            "CRC-8 (100000111)": "100000111",
            "CRC-16 (10001000000100001)": "10001000000100001"
        }
        
        if mode == 'custom':
            self.simulator.polynomial = poly_map[self.custom_poly.get()]
        elif mode == 'random':
            self.simulator.polynomial = poly_map[self.random_poly.get()]
        elif mode == 'burst':
            self.simulator.polynomial = poly_map[self.burst_poly.get()]
        
        self.simulator.polynomial_length = len(self.simulator.polynomial)
    
    def run_custom_test(self):
        """Run custom data test"""
        data = self.custom_data_entry.get().strip()
        
        if not data or not all(c in '01' for c in data):
            messagebox.showerror("Error", "Enter valid binary data")
            return
        
        self.update_poly('custom')
        
        error_input = self.custom_errors_entry.get().strip()
        errors = []
        if error_input:
            try:
                errors = [int(x) for x in error_input.split()]
            except ValueError:
                messagebox.showerror("Error", "Invalid error positions")
                return
        
        self.run_simulation(data, errors, "Custom Data Test")
    
    def run_random_test(self):
        """Run random data test"""
        try:
            length = int(self.random_length.get())
            num_errors = int(self.random_errors.get())
        except ValueError:
            messagebox.showerror("Error", "Enter valid numbers")
            return
        
        self.update_poly('random')
        
        data = ''.join(random.choice('01') for _ in range(length))
        data_with_crc_length = length + self.simulator.polynomial_length - 1
        
        if num_errors > 0:
            errors = random.sample(range(data_with_crc_length), min(num_errors, data_with_crc_length))
        else:
            errors = []
        
        self.run_simulation(data, errors, f"Random Data Test (Length: {length}, Errors: {num_errors})")
    
    def run_burst_test(self):
        """Run burst error test"""
        data = self.burst_data_entry.get().strip()
        
        if not data or not all(c in '01' for c in data):
            messagebox.showerror("Error", "Enter valid binary data")
            return
        
        try:
            burst_len = int(self.burst_length.get())
        except ValueError:
            messagebox.showerror("Error", "Enter valid burst length")
            return
        
        self.update_poly('burst')
        
        result = self.simulator.burst_error_detection(data, burst_len)
        
        output = []
        output.append("BURST ERROR DETECTION TEST")
        output.append(f"Original Data: {data}")
        output.append(f"Burst Length: {burst_len}")
        output.append(f"Error Positions: {result['error_positions']}")
        output.append(f"Detected: {'Yes' if result['is_detected'] else 'No'}")
        output.append(f"Remainder: {result['remainder']}")
        
        self.display_results(output, result['is_detected'])
    
    def run_poly_test(self):
        """Run polynomial comparison test"""
        data = self.poly_data_entry.get().strip()
        
        if not data or not all(c in '01' for c in data):
            messagebox.showerror("Error", "Enter valid binary data")
            return
        
        error_input = self.poly_errors_entry.get().strip()
        errors = []
        if error_input:
            try:
                errors = [int(x) for x in error_input.split()]
            except ValueError:
                messagebox.showerror("Error", "Invalid error positions")
                return
        
        selection = self.poly_test_selection.get()
        
        if selection == "CRC-3 vs CRC-4":
            polys = [("CRC-3", "1101"), ("CRC-4", "10011")]
        elif selection == "CRC-4 vs CRC-8":
            polys = [("CRC-4", "10011"), ("CRC-8", "100000111")]
        else:
            polys = [("CRC-8", "100000111"), ("CRC-16", "10001000000100001")]
        
        output = []
        output.append("POLYNOMIAL COMPARISON TEST")
        output.append(f"Data: {data}")
        output.append(f"Errors at: {errors}")
        output.append("")
        
        for name, poly in polys:
            self.simulator.polynomial = poly
            self.simulator.polynomial_length = len(poly)
            result = self.simulator.demonstrate_transmission(data, errors, show_steps=False)
            
            output.append(f"{name} ({poly}):")
            output.append(f"  CRC: {result['crc_checksum']}")
            output.append(f"  Valid: {'Yes' if result['is_valid'] else 'No'}")
            output.append(f"  Remainder: {result['remainder']}")
            output.append("")
        
        self.display_results(output, True)
    
    def run_all_scenarios(self):
        """Run all predefined scenarios"""
        scenarios = [
            ("Error-free transmission", "1011001", None),
            ("Single bit error", "1011001", [2]),
            ("Double bit error", "1011001", [1, 4]),
            ("Multiple bit errors", "1011001", [1, 4, 6]),
        ]
        
        self.simulator.polynomial = "1101"
        self.simulator.polynomial_length = 4
        
        for name, data, errors in scenarios:
            result = self.simulator.demonstrate_transmission(data, errors, show_steps=True)
            self.display_results(result['steps'], result['is_valid'], append=True)
    
    def run_simulation(self, data, errors, test_name):
        """Run simulation with detailed steps"""
        result = self.simulator.demonstrate_transmission(data, errors, show_steps=True)
        
        output = [f"{test_name}"]
        output.extend(result['steps'])
        
        self.display_results(output, result['is_valid'])
    
    def display_results(self, content, is_valid, append=False):
        """Display results with formatting"""
        if not append:
            self.results_text.delete(1.0, tk.END)
        
        if isinstance(content, list):
            text = "\n".join(content)
        else:
            text = content
        
        self.results_text.insert(tk.END, text + "\n")
        
        # Apply formatting
        content_lines = self.results_text.get(1.0, tk.END).split('\n')
        for i, line in enumerate(content_lines, 1):
            if "[OK]" in line or "VALID" in line or "Yes" in line or "detected" in line.lower():
                self.results_text.tag_add('success', f"{i}.0", f"{i}.end")
            elif "[ERROR]" in line or "CORRUPTED" in line or "No" in line:
                self.results_text.tag_add('error', f"{i}.0", f"{i}.end")
            elif line.startswith("STEP") or line.startswith("CRC") or line.startswith("TRANSMISSION") or line.startswith("BURST") or line.startswith("POLYNOMIAL"):
                self.results_text.tag_add('header', f"{i}.0", f"{i}.end")
            elif "XOR" in line or "Step" in line or "dividend" in line.lower() or "bit" in line.lower():
                self.results_text.tag_add('step', f"{i}.0", f"{i}.end")
            elif "Remainder" in line or "Polynomial" in line or "Data" in line:
                self.results_text.tag_add('info', f"{i}.0", f"{i}.end")
        
        # Update status
        if is_valid:
            self.status_label.config(text="● ✓ Valid", fg='#10b981')
        else:
            self.status_label.config(text="● ✗ Error Detected", fg='#ef4444')
    
    def clear_field(self, mode):
        """Clear specific field"""
        if mode == 'custom':
            self.custom_data_entry.delete(0, tk.END)
            self.custom_data_entry.insert(0, "1011001")
            self.custom_errors_entry.delete(0, tk.END)
        elif mode == 'random':
            self.random_length.delete(0, tk.END)
            self.random_length.insert(0, "16")
            self.random_errors.delete(0, tk.END)
            self.random_errors.insert(0, "2")
        elif mode == 'burst':
            self.burst_data_entry.delete(0, tk.END)
            self.burst_data_entry.insert(0, "1011001")
            self.burst_length.delete(0, tk.END)
            self.burst_length.insert(0, "3")
        elif mode == 'poly':
            self.poly_data_entry.delete(0, tk.END)
            self.poly_data_entry.insert(0, "1101011011")
            self.poly_errors_entry.delete(0, tk.END)
            self.poly_errors_entry.insert(0, "3 7")
    
    def clear_results(self):
        """Clear results panel"""
        self.results_text.delete(1.0, tk.END)
        self.status_label.config(text="Ready", fg='#64748b')


def main():
    root = tk.Tk()
    app = CompleteCRCGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
