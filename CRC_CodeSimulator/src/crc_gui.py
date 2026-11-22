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
        self.root.title("CRC Code Simulator // Developer Edition")
        self.root.geometry("1600x900")
        self.root.configure(bg='#e0f2fe')  # Light blue background like the image
        self.root.minsize(1400, 800)
        
        self.simulator = CRCSimulator(polynomial="10011")
        
        self.setup_styles()
        self.create_main_interface()
        self.center_window()
    
    def setup_styles(self):
        """Enhanced modern professional styling"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Light blue/white theme matching the image
        colors = {
            'primary': '#3b82f6',           # Light blue like header
            'primary_dark': '#2563eb',      # Darker blue
            'primary_light': '#60a5fa',     # Lighter blue
            'secondary': '#94a3b8',         # Light gray
            'secondary_dark': '#64748b',    # Medium gray
            'success': '#10b981',           # Green
            'success_dark': '#059669',      # Darker green
            'error': '#ef4444',             # Red
            'error_dark': '#dc2626',        # Darker red
            'warning': '#f59e0b',           # Amber
            'bg': '#e0f2fe',                # Light blue background
            'bg_alt': '#f0f9ff',            # Very light blue
            'bg_card': '#ffffff',           # White cards
            'bg_input': '#f0f9ff',          # Light blue input background
            'text': '#1e293b',              # Dark text
            'text_light': '#64748b',        # Medium gray text
            'border': '#bfdbfe',            # Light blue border
            'border_highlight': '#3b82f6',  # Blue highlight
            'shadow': '#93c5fd',            # Light blue shadow
            'accent': '#8b5cf6',            # Purple accent
            'code_bg': '#f0f9ff',           # Light blue code background
            'code_text': '#1e293b'          # Dark code text
        }
        
        # Enhanced card styling with subtle border
        self.style.configure('Card.TFrame',
                           background=colors['bg_card'],
                           relief='flat',
                           borderwidth=1)
        
        # Enhanced button styling with light blue theme
        self.style.configure('Primary.TButton',
                           font=('JetBrains Mono', 10, 'bold'),
                           padding=[20, 12],
                           background=colors['primary'],
                           foreground='#ffffff',
                           borderwidth=1,
                           relief='solid',
                           focuscolor='none')
        
        self.style.configure('Success.TButton',
                           font=('JetBrains Mono', 10, 'bold'),
                           padding=[20, 12],
                           background=colors['success'],
                           foreground='#ffffff',
                           borderwidth=1,
                           relief='solid',
                           focuscolor='none')
        
        self.style.configure('Secondary.TButton',
                           font=('JetBrains Mono', 10),
                           padding=[18, 10],
                           background=colors['secondary'],
                           foreground='#ffffff',
                           borderwidth=1,
                           relief='solid',
                           focuscolor='none')
        
        # Enhanced button hover and pressed states with professional feedback
        self.style.map('Primary.TButton',
                       background=[('active', colors['primary_light']),
                                  ('pressed', colors['primary_dark'])],
                       bordercolor=[('active', colors['primary_light']),
                                   ('pressed', colors['primary_dark'])])
        self.style.map('Success.TButton',
                       background=[('active', '#34d399'),
                                  ('pressed', colors['success_dark'])],
                       bordercolor=[('active', '#34d399'),
                                   ('pressed', colors['success_dark'])])
        self.style.map('Secondary.TButton',
                       background=[('active', colors['secondary_dark']),
                                  ('pressed', '#475569')],
                       bordercolor=[('active', colors['border_highlight']),
                                   ('pressed', colors['border'])])
        
        # Enhanced label styling with professional light theme
        self.style.configure('Title.TLabel',
                           font=('JetBrains Mono', 28, 'bold'),
                           background='#ffffff',
                           foreground=colors['text'])
        
        self.style.configure('Subtitle.TLabel',
                           font=('JetBrains Mono', 11),
                           background='#ffffff',
                           foreground=colors['text_light'])
        
        self.style.configure('Header.TLabel',
                           font=('JetBrains Mono', 14, 'bold'),
                           background=colors['bg_card'],
                           foreground=colors['text'])
        
        self.style.configure('Label.TLabel',
                           font=('JetBrains Mono', 10),
                           background=colors['bg_card'],
                           foreground=colors['text'])
        
        self.style.configure('Info.TLabel',
                           font=('JetBrains Mono', 9),
                           background=colors['bg_card'],
                           foreground=colors['text_light'])
        
        # Enhanced entry styling with professional light theme
        self.style.configure('Modern.TEntry',
                           font=('JetBrains Mono', 12),
                           fieldbackground=colors['bg_input'],
                           borderwidth=1,
                           relief='solid',
                           padding=10,
                           foreground=colors['text'],
                           insertbackground='#1e293b')  # Dark cursor for visibility
        
        self.style.map('Modern.TEntry',
                       bordercolor=[('focus', colors['border_highlight']),
                                  ('!focus', colors['border'])],
                       fieldbackground=[('focus', colors['bg_input']),
                                      ('!focus', colors['bg_input'])])
        
        # Enhanced notebook styling with light blue theme
        self.style.configure('Modern.TNotebook',
                           background=colors['bg_alt'],
                           borderwidth=0,
                           tabposition='n')
        
        self.style.configure('Modern.TNotebook.Tab',
                           font=('JetBrains Mono', 10, 'bold'),
                           padding=[25, 12],
                           background='#e5e7eb',
                           foreground=colors['text_light'],
                           borderwidth=0,
                           focuscolor='none')
        
        self.style.map('Modern.TNotebook.Tab',
                       background=[('selected', colors['bg_card']),
                                 ('active', '#d1d5db')],
                       foreground=[('selected', colors['primary']),
                                 ('active', colors['text'])])
    
    def create_main_interface(self):
        """Create complete interface with light blue theme matching image"""
        # Header
        self.create_header()
        
        # Main content - two column layout with light blue theme
        main_container = tk.Frame(self.root, bg='#e0f2fe')
        main_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        
        # Left panel - Notebook (tabs)
        left_panel = tk.Frame(main_container, bg='#e0f2fe')
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 8))
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(left_panel, style='Modern.TNotebook')
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.create_crc_overview_tab()
        self.create_custom_data_tab()
        self.create_random_data_tab()
        self.create_burst_error_tab()
        self.create_polynomial_test_tab()
        self.create_all_scenarios_tab()
        
        # Set default tab
        self.notebook.select(0)
        
        # Right panel - Results
        right_panel = tk.Frame(main_container, bg='#e0f2fe')
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(8, 0))
        
        # Results panel (right side)
        self.create_results_panel(right_panel)
    
    def create_crc_overview_tab(self):
        """CRC overview tab with educational content"""
        tab = tk.Frame(self.notebook, bg='#e0f2fe', padx=25, pady=25)
        self.notebook.add(tab, text="CRC_OVERVIEW")
        
        # Scrollable frame for content
        canvas = tk.Canvas(tab, bg='#e0f2fe', highlightthickness=0)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#e0f2fe')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Content sections
        self._add_overview_section(scrollable_frame, 
            "What is CRC?",
            "Cyclic Redundancy Check (CRC) is an error-detecting code used to detect accidental changes to digital data.",
            [
                "CRC is widely used in networks (Ethernet, WiFi), storage systems, and communication protocols",
                "It appends a fixed-length checksum to the data before transmission",
                "The receiver recalculates the checksum to verify data integrity",
                "CRC can detect both single-bit and multi-bit errors, including burst errors"
            ])
        
        self._add_overview_section(scrollable_frame,
            "How CRC Works",
            "CRC uses polynomial division to generate a checksum:",
            [
                "1. The data is treated as a binary number",
                "2. A generator polynomial (e.g., 1101) is chosen",
                "3. Zeros are appended to the data (length = polynomial degree)",
                "4. Modulo-2 division is performed on the data by the polynomial",
                "5. The remainder becomes the CRC checksum",
                "6. The checksum is appended to the original data for transmission",
                "7. The receiver performs the same division - remainder of 0 means valid data"
            ])
        
        self._add_overview_section(scrollable_frame,
            "Generator Polynomials",
            "Common CRC polynomials and their applications:",
            [
                "CRC-3 (1101): Simple error detection for small data",
                "CRC-4 (10011): Used in some telecom protocols",
                "CRC-8 (100000111): Standard in many embedded systems",
                "CRC-16 (10001000000100001): Used in USB, Modbus, and other protocols",
                "CRC-32: Used in Ethernet, ZIP files, and PNG images"
            ])
        
        self._add_overview_section(scrollable_frame,
            "Error Detection Capabilities",
            "CRC can detect various types of errors:",
            [
                "Single-bit errors: Always detected",
                "Double-bit errors: Always detected",
                "Odd number of bit errors: Always detected",
                "Burst errors: Detected if burst length ≤ polynomial degree",
                "Longer burst errors: High probability of detection (>99%)"
            ])
        
        self._add_overview_section(scrollable_frame,
            "Limitations",
            "What CRC cannot do:",
            [
                "Cannot correct errors - only detect them",
                "Cannot detect all possible error patterns",
                "Some rare error combinations may produce valid checksum",
                "Not suitable for malicious error detection (needs cryptographic hash)"
            ])
        
        self._add_overview_section(scrollable_frame,
            "Example",
            "Using CRC-3 with polynomial 1101:",
            [
                "Data: 1011",
                "Polynomial: 1101 (degree 3, so append 3 zeros)",
                "Appended data: 1011000",
                "Division: 1011000 ÷ 1101 = 1001 remainder 100",
                "CRC checksum: 100",
                "Transmitted: 1011100 (data + CRC)",
                "Receiver divides 1011100 by 1101",
                "If remainder = 0000: Data is valid",
                "If remainder ≠ 0000: Data has errors"
            ])
    
    def _add_overview_section(self, parent, title, description, points):
        """Helper to add overview sections"""
        section_frame = tk.Frame(parent, bg='#ffffff', relief='flat', borderwidth=1, padx=25, pady=20)
        section_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Title
        tk.Label(section_frame, text=title,
                font=('JetBrains Mono', 14, 'bold'),
                bg='#ffffff', fg='#2563eb').pack(anchor='w', pady=(0, 10))
        
        # Description
        tk.Label(section_frame, text=description,
                font=('JetBrains Mono', 10),
                bg='#ffffff', fg='#1e293b',
                wraplength=1200).pack(anchor='w', pady=(0, 15))
        
        # Points as paragraph
        paragraph_text = " ".join(points)
        point_label = tk.Label(section_frame, text=paragraph_text,
                font=('JetBrains Mono', 10),
                bg='#ffffff', fg='#64748b',
                wraplength=1200,
                justify=tk.LEFT)
        point_label.pack(anchor='w', pady=3)
    
    def create_header(self):
        """Create dark blue header matching the image design"""
        header = tk.Frame(self.root, bg='#1e3a8a', height=80)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        # Dark blue accent line
        accent_frame = tk.Frame(header, bg='#1e40af', height=3)
        accent_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        title_frame = tk.Frame(header, bg='#1e3a8a')
        title_frame.pack(expand=True, fill=tk.BOTH, padx=30)
        
        # Main title matching the image
        title_container = tk.Frame(title_frame, bg='#1e3a8a')
        title_container.pack(side=tk.LEFT, pady=(12, 8))
        
        tk.Label(title_container, text="CRC_CODE_SIMULATOR",
                font=('JetBrains Mono', 18, 'bold'),
                bg='#1e3a8a', fg='#ffffff').pack(anchor='w')
        
        # Right side - POLY and VALID indicators matching the image
        status_container = tk.Frame(title_frame, bg='#1e3a8a')
        status_container.pack(side=tk.RIGHT, pady=(12, 8))
        
        # POLY indicator
        self.poly_indicator = tk.Label(status_container, text="POLY: CRC-4",
                font=('JetBrains Mono', 10, 'bold'),
                bg='#1e3a8a', fg='#ffffff')
        self.poly_indicator.pack(anchor='e')
        
        # Status indicator
        self.header_status = tk.Label(status_container, text="[VALID]",
                font=('JetBrains Mono', 10, 'bold'),
                bg='#1e3a8a', fg='#10b981')
        self.header_status.pack(anchor='e', pady=(4, 0))
    
    def create_custom_data_tab(self):
        """Custom data testing tab with light blue theme"""
        tab = tk.Frame(self.notebook, bg='#e0f2fe', padx=25, pady=25)
        self.notebook.add(tab, text="CUSTOM_DATA")
        
        # White card with light blue theme
        card = tk.Frame(tab, bg='#ffffff', relief='flat', borderwidth=1, padx=30, pady=25)
        card.pack(fill=tk.BOTH, expand=True)
        
        # Section header with professional styling
        header_section = tk.Frame(card, bg='#ffffff')
        header_section.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(header_section, text="[CUSTOM_DATA_TEST]",
                font=('JetBrains Mono', 16, 'bold'),
                bg='#ffffff', fg='#2563eb').pack(side=tk.LEFT)
        
        tk.Label(header_section, text="// Test your own binary data",
                font=('JetBrains Mono', 9),
                bg='#ffffff', fg='#64748b').pack(side=tk.LEFT, padx=(15, 0))
        
        # Input fields
        self.create_input_field(card, "Binary Data:", "custom_data", "1011001")
        self.create_input_field(card, "Error Positions:", "custom_errors", "")
        
        # Polynomial selection with professional styling
        tk.Label(card, text="Generator Polynomial:",
                font=('JetBrains Mono', 10, 'bold'),
                bg='#ffffff', fg='#1e293b').pack(anchor='w', pady=(15, 6))
        
        # Radio buttons for preset vs custom
        self.custom_poly_mode = tk.StringVar(value="preset")
        poly_mode_frame = tk.Frame(card, bg='#ffffff')
        poly_mode_frame.pack(anchor='w', pady=(0, 10))
        
        tk.Radiobutton(poly_mode_frame, text="Select Preset", variable=self.custom_poly_mode,
                      value="preset", bg='#ffffff', fg='#1e293b',
                      font=('JetBrains Mono', 9),
                      command=lambda: self.toggle_poly_mode('custom')).pack(side=tk.LEFT, padx=(0, 20))
        tk.Radiobutton(poly_mode_frame, text="Enter Custom", variable=self.custom_poly_mode,
                      value="custom", bg='#ffffff', fg='#1e293b',
                      font=('JetBrains Mono', 9),
                      command=lambda: self.toggle_poly_mode('custom')).pack(side=tk.LEFT)
        
        # Preset dropdown
        self.custom_poly_preset_frame = tk.Frame(card, bg='#ffffff')
        self.custom_poly_preset_frame.pack(anchor='w', pady=(0, 10))
        
        self.custom_poly = tk.StringVar(value="CRC-4 (10011)")
        self.custom_poly_combo = ttk.Combobox(self.custom_poly_preset_frame, textvariable=self.custom_poly,
                                 values=["CRC-3 (1101)", "CRC-4 (10011)", 
                                        "CRC-8 (100000111)", "CRC-16 (10001000000100001)"],
                                 state='readonly', width=40)
        self.custom_poly_combo.pack()
        try:
            self.custom_poly_combo.configure(insertbackground='#1e293b')
        except:
            pass
        self.custom_poly_combo.bind('<<ComboboxSelected>>', lambda e: self.update_poly('custom'))
        
        # Custom polynomial entry (hidden by default)
        self.custom_poly_custom_frame = tk.Frame(card, bg='#ffffff')
        
        tk.Label(self.custom_poly_custom_frame, text="Custom Polynomial (binary):",
                font=('JetBrains Mono', 9),
                bg='#ffffff', fg='#64748b').pack(anchor='w')
        
        self.custom_poly_entry = tk.Entry(self.custom_poly_custom_frame,
                                         font=('JetBrains Mono', 12),
                                         bg='#f0f9ff',
                                         fg='#1e293b',
                                         insertbackground='#1e293b',
                                         relief='solid',
                                         borderwidth=1,
                                         width=40)
        self.custom_poly_entry.pack(pady=(5, 20))
        self.custom_poly_entry.insert(0, "10011")
        
        # Hide custom entry initially
        self.custom_poly_custom_frame.pack_forget()
        
        # Professional buttons
        btn_frame = tk.Frame(card, bg='#ffffff')
        btn_frame.pack(pady=15)
        
        ttk.Button(btn_frame, text="[RUN_SIMULATION]",
                 style='Primary.TButton',
                 command=lambda: self.run_custom_test()).pack(side=tk.LEFT, padx=8)
        
        ttk.Button(btn_frame, text="[CLEAR]",
                 style='Secondary.TButton',
                 command=lambda: self.clear_field('custom')).pack(side=tk.LEFT, padx=8)
    
    def create_random_data_tab(self):
        """Random data testing tab with light blue theme"""
        tab = tk.Frame(self.notebook, bg='#e0f2fe', padx=25, pady=25)
        self.notebook.add(tab, text="RANDOM_DATA")
        
        card = tk.Frame(tab, bg='#ffffff', relief='flat', borderwidth=1, padx=30, pady=25)
        card.pack(fill=tk.BOTH, expand=True)
        
        # Section header
        header_section = tk.Frame(card, bg='#ffffff')
        header_section.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(header_section, text="[RANDOM_DATA_TEST]",
                font=('JetBrains Mono', 16, 'bold'),
                bg='#ffffff', fg='#2563eb').pack(side=tk.LEFT)
        
        tk.Label(header_section, text="// Generate random binary data for testing",
                font=('JetBrains Mono', 9),
                bg='#ffffff', fg='#64748b').pack(side=tk.LEFT, padx=(15, 0))
        
        # Data length
        tk.Label(card, text="Data Length (8-32 recommended):",
                font=('JetBrains Mono', 10, 'bold'),
                bg='#ffffff', fg='#1e293b').pack(anchor='w', pady=(0, 6))
        
        self.random_length = tk.Entry(card, 
                                     font=('JetBrains Mono', 12),
                                     bg='#f0f9ff',
                                     fg='#1e293b',
                                     insertbackground='#1e293b',
                                     relief='solid',
                                     borderwidth=1,
                                     width=25)
        self.random_length.pack(pady=(0, 15))
        self.random_length.insert(0, "16")
        
        # Number of errors
        tk.Label(card, text="Number of Random Errors (0-5):",
                font=('JetBrains Mono', 10, 'bold'),
                bg='#ffffff', fg='#1e293b').pack(anchor='w', pady=(0, 6))
        
        self.random_errors = tk.Entry(card,
                                     font=('JetBrains Mono', 12),
                                     bg='#f0f9ff',
                                     fg='#1e293b',
                                     insertbackground='#1e293b',
                                     relief='solid',
                                     borderwidth=1,
                                     width=25)
        self.random_errors.pack(pady=(0, 15))
        self.random_errors.insert(0, "2")
        
        # Polynomial
        tk.Label(card, text="Generator Polynomial:",
                font=('JetBrains Mono', 10, 'bold'),
                bg='#ffffff', fg='#1e293b').pack(anchor='w', pady=(0, 6))
        
        # Radio buttons for preset vs custom
        self.random_poly_mode = tk.StringVar(value="preset")
        poly_mode_frame = tk.Frame(card, bg='#ffffff')
        poly_mode_frame.pack(anchor='w', pady=(0, 10))
        
        tk.Radiobutton(poly_mode_frame, text="Select Preset", variable=self.random_poly_mode,
                      value="preset", bg='#ffffff', fg='#1e293b',
                      font=('JetBrains Mono', 9),
                      command=lambda: self.toggle_poly_mode('random')).pack(side=tk.LEFT, padx=(0, 20))
        tk.Radiobutton(poly_mode_frame, text="Enter Custom", variable=self.random_poly_mode,
                      value="custom", bg='#ffffff', fg='#1e293b',
                      font=('JetBrains Mono', 9),
                      command=lambda: self.toggle_poly_mode('random')).pack(side=tk.LEFT)
        
        # Preset dropdown
        self.random_poly_preset_frame = tk.Frame(card, bg='#ffffff')
        self.random_poly_preset_frame.pack(anchor='w', pady=(0, 10))
        
        self.random_poly = tk.StringVar(value="CRC-3 (1101)")
        self.random_poly_combo = ttk.Combobox(self.random_poly_preset_frame, textvariable=self.random_poly,
                                 values=["CRC-3 (1101)", "CRC-4 (10011)", 
                                        "CRC-8 (100000111)", "CRC-16 (10001000000100001)"],
                                 state='readonly', width=40)
        self.random_poly_combo.pack()
        try:
            self.random_poly_combo.configure(insertbackground='#1e293b')
        except:
            pass
        self.random_poly_combo.bind('<<ComboboxSelected>>', lambda e: self.update_poly('random'))
        
        # Custom polynomial entry (hidden by default)
        self.random_poly_custom_frame = tk.Frame(card, bg='#ffffff')
        
        tk.Label(self.random_poly_custom_frame, text="Custom Polynomial (binary):",
                font=('JetBrains Mono', 9),
                bg='#ffffff', fg='#64748b').pack(anchor='w')
        
        self.random_poly_entry = tk.Entry(self.random_poly_custom_frame,
                                         font=('JetBrains Mono', 12),
                                         bg='#f0f9ff',
                                         fg='#1e293b',
                                         insertbackground='#1e293b',
                                         relief='solid',
                                         borderwidth=1,
                                         width=40)
        self.random_poly_entry.pack(pady=(5, 20))
        self.random_poly_entry.insert(0, "1101")
        
        # Hide custom entry initially
        self.random_poly_custom_frame.pack_forget()
        
        # Professional buttons
        btn_frame = tk.Frame(card, bg='#ffffff')
        btn_frame.pack(pady=15)
        
        ttk.Button(btn_frame, text="[GENERATE_TEST]",
                 style='Primary.TButton',
                 command=lambda: self.run_random_test()).pack(side=tk.LEFT, padx=8)
        
        ttk.Button(btn_frame, text="[CLEAR]",
                 style='Secondary.TButton',
                 command=lambda: self.clear_field('random')).pack(side=tk.LEFT, padx=8)
    
    def create_burst_error_tab(self):
        """Burst error testing tab with light blue theme"""
        tab = tk.Frame(self.notebook, bg='#e0f2fe', padx=25, pady=25)
        self.notebook.add(tab, text="BURST_ERROR")
        
        card = tk.Frame(tab, bg='#ffffff', relief='flat', borderwidth=1, padx=30, pady=25)
        card.pack(fill=tk.BOTH, expand=True)
        
        # Section header
        header_section = tk.Frame(card, bg='#ffffff')
        header_section.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(header_section, text="[BURST_ERROR_DETECTION]",
                font=('JetBrains Mono', 16, 'bold'),
                bg='#ffffff', fg='#2563eb').pack(side=tk.LEFT)
        
        tk.Label(header_section, text="// Test consecutive bit error detection",
                font=('JetBrains Mono', 9),
                bg='#ffffff', fg='#64748b').pack(side=tk.LEFT, padx=(15, 0))
        
        # Input data
        self.create_input_field(card, "Binary Data:", "burst_data", "1011001")
        
        # Burst length
        tk.Label(card, text="Burst Error Length:",
                font=('JetBrains Mono', 10, 'bold'),
                bg='#ffffff', fg='#1e293b').pack(anchor='w', pady=(15, 6))
        
        self.burst_length = tk.Entry(card,
                                    font=('JetBrains Mono', 12),
                                    bg='#f0f9ff',
                                    fg='#1e293b',
                                    insertbackground='#1e293b',
                                    relief='solid',
                                    borderwidth=1,
                                    width=25)
        self.burst_length.pack(pady=(0, 15))
        self.burst_length.insert(0, "3")
        
        # Polynomial
        tk.Label(card, text="Generator Polynomial:",
                font=('JetBrains Mono', 10, 'bold'),
                bg='#ffffff', fg='#1e293b').pack(anchor='w', pady=(0, 6))
        
        # Radio buttons for preset vs custom
        self.burst_poly_mode = tk.StringVar(value="preset")
        poly_mode_frame = tk.Frame(card, bg='#ffffff')
        poly_mode_frame.pack(anchor='w', pady=(0, 10))
        
        tk.Radiobutton(poly_mode_frame, text="Select Preset", variable=self.burst_poly_mode,
                      value="preset", bg='#ffffff', fg='#1e293b',
                      font=('JetBrains Mono', 9),
                      command=lambda: self.toggle_poly_mode('burst')).pack(side=tk.LEFT, padx=(0, 20))
        tk.Radiobutton(poly_mode_frame, text="Enter Custom", variable=self.burst_poly_mode,
                      value="custom", bg='#ffffff', fg='#1e293b',
                      font=('JetBrains Mono', 9),
                      command=lambda: self.toggle_poly_mode('burst')).pack(side=tk.LEFT)
        
        # Preset dropdown
        self.burst_poly_preset_frame = tk.Frame(card, bg='#ffffff')
        self.burst_poly_preset_frame.pack(anchor='w', pady=(0, 10))
        
        self.burst_poly = tk.StringVar(value="CRC-3 (1101)")
        self.burst_poly_combo = ttk.Combobox(self.burst_poly_preset_frame, textvariable=self.burst_poly,
                                 values=["CRC-3 (1101)", "CRC-4 (10011)", 
                                        "CRC-8 (100000111)", "CRC-16 (10001000000100001)"],
                                 state='readonly', width=40)
        self.burst_poly_combo.pack()
        try:
            self.burst_poly_combo.configure(insertbackground='#1e293b')
        except:
            pass
        self.burst_poly_combo.bind('<<ComboboxSelected>>', lambda e: self.update_poly('burst'))
        
        # Custom polynomial entry (hidden by default)
        self.burst_poly_custom_frame = tk.Frame(card, bg='#ffffff')
        
        tk.Label(self.burst_poly_custom_frame, text="Custom Polynomial (binary):",
                font=('JetBrains Mono', 9),
                bg='#ffffff', fg='#64748b').pack(anchor='w')
        
        self.burst_poly_entry = tk.Entry(self.burst_poly_custom_frame,
                                         font=('JetBrains Mono', 12),
                                         bg='#f0f9ff',
                                         fg='#1e293b',
                                         insertbackground='#1e293b',
                                         relief='solid',
                                         borderwidth=1,
                                         width=40)
        self.burst_poly_entry.pack(pady=(5, 20))
        self.burst_poly_entry.insert(0, "1101")
        
        # Hide custom entry initially
        self.burst_poly_custom_frame.pack_forget()
        
        # Professional buttons
        btn_frame = tk.Frame(card, bg='#ffffff')
        btn_frame.pack(pady=15)
        
        ttk.Button(btn_frame, text="[TEST_BURST]",
                 style='Primary.TButton',
                 command=lambda: self.run_burst_test()).pack(side=tk.LEFT, padx=8)
        
        ttk.Button(btn_frame, text="[CLEAR]",
                 style='Secondary.TButton',
                 command=lambda: self.clear_field('burst')).pack(side=tk.LEFT, padx=8)
    
    def create_polynomial_test_tab(self):
        """Different polynomial testing tab with light blue theme"""
        tab = tk.Frame(self.notebook, bg='#e0f2fe', padx=25, pady=25)
        self.notebook.add(tab, text="POLY_TEST")
        
        card = tk.Frame(tab, bg='#ffffff', relief='flat', borderwidth=1, padx=30, pady=25)
        card.pack(fill=tk.BOTH, expand=True)
        
        # Section header
        header_section = tk.Frame(card, bg='#ffffff')
        header_section.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(header_section, text="[POLYNOMIAL_COMPARISON]",
                font=('JetBrains Mono', 16, 'bold'),
                bg='#ffffff', fg='#2563eb').pack(side=tk.LEFT)
        
        tk.Label(header_section, text="// Compare different CRC polynomials",
                font=('JetBrains Mono', 9),
                bg='#ffffff', fg='#64748b').pack(side=tk.LEFT, padx=(15, 0))
        
        # Input data
        self.create_input_field(card, "Binary Data:", "poly_data", "1101011011")
        
        # Polynomial comparison
        tk.Label(card, text="Compare Different Polynomials:",
                font=('JetBrains Mono', 10, 'bold'),
                bg='#ffffff', fg='#1e293b').pack(anchor='w', pady=(15, 6))
        
        # Radio buttons for preset vs custom
        self.poly_test_mode = tk.StringVar(value="preset")
        poly_mode_frame = tk.Frame(card, bg='#ffffff')
        poly_mode_frame.pack(anchor='w', pady=(0, 10))
        
        tk.Radiobutton(poly_mode_frame, text="Select Preset", variable=self.poly_test_mode,
                      value="preset", bg='#ffffff', fg='#1e293b',
                      font=('JetBrains Mono', 9),
                      command=lambda: self.toggle_poly_mode('poly_test')).pack(side=tk.LEFT, padx=(0, 20))
        tk.Radiobutton(poly_mode_frame, text="Enter Custom", variable=self.poly_test_mode,
                      value="custom", bg='#ffffff', fg='#1e293b',
                      font=('JetBrains Mono', 9),
                      command=lambda: self.toggle_poly_mode('poly_test')).pack(side=tk.LEFT)
        
        # Preset dropdown
        self.poly_test_preset_frame = tk.Frame(card, bg='#ffffff')
        self.poly_test_preset_frame.pack(anchor='w', pady=(0, 10))
        
        self.poly_test_selection = tk.StringVar(value="CRC-3 vs CRC-4")
        self.poly_test_combo = ttk.Combobox(self.poly_test_preset_frame, textvariable=self.poly_test_selection,
                                 values=["CRC-3 vs CRC-4", "CRC-4 vs CRC-8", "CRC-8 vs CRC-16"],
                                 state='readonly', width=40)
        self.poly_test_combo.pack()
        try:
            self.poly_test_combo.configure(insertbackground='#1e293b')
        except:
            pass
        
        # Custom polynomial entry (hidden by default)
        self.poly_test_custom_frame = tk.Frame(card, bg='#ffffff')
        
        tk.Label(self.poly_test_custom_frame, text="First Polynomial (binary):",
                font=('JetBrains Mono', 9),
                bg='#ffffff', fg='#64748b').pack(anchor='w')
        
        self.poly_test_custom1_entry = tk.Entry(self.poly_test_custom_frame,
                                         font=('JetBrains Mono', 12),
                                         bg='#f0f9ff',
                                         fg='#1e293b',
                                         insertbackground='#1e293b',
                                         relief='solid',
                                         borderwidth=1,
                                         width=40)
        self.poly_test_custom1_entry.pack(pady=(5, 10))
        self.poly_test_custom1_entry.insert(0, "1101")
        
        tk.Label(self.poly_test_custom_frame, text="Second Polynomial (binary):",
                font=('JetBrains Mono', 9),
                bg='#ffffff', fg='#64748b').pack(anchor='w')
        
        self.poly_test_custom2_entry = tk.Entry(self.poly_test_custom_frame,
                                         font=('JetBrains Mono', 12),
                                         bg='#f0f9ff',
                                         fg='#1e293b',
                                         insertbackground='#1e293b',
                                         relief='solid',
                                         borderwidth=1,
                                         width=40)
        self.poly_test_custom2_entry.pack(pady=(5, 20))
        self.poly_test_custom2_entry.insert(0, "10011")
        
        # Hide custom entry initially
        self.poly_test_custom_frame.pack_forget()
        
        # Error injection
        tk.Label(card, text="Error Positions:",
                font=('JetBrains Mono', 10, 'bold'),
                bg='#ffffff', fg='#1e293b').pack(anchor='w', pady=(0, 6))
        
        self.poly_errors_entry = tk.Entry(card,
                                         font=('JetBrains Mono', 12),
                                         bg='#f0f9ff',
                                         fg='#1e293b',
                                         insertbackground='#1e293b',
                                         relief='solid',
                                         borderwidth=1,
                                         width=35)
        self.poly_errors_entry.pack(pady=(0, 20))
        self.poly_errors_entry.insert(0, "3 7")
        
        # Professional buttons
        btn_frame = tk.Frame(card, bg='#ffffff')
        btn_frame.pack(pady=15)
        
        ttk.Button(btn_frame, text="[COMPARE_POLY]",
                 style='Primary.TButton',
                 command=lambda: self.run_poly_test()).pack(side=tk.LEFT, padx=8)
        
        ttk.Button(btn_frame, text="[CLEAR]",
                 style='Secondary.TButton',
                 command=lambda: self.clear_field('poly')).pack(side=tk.LEFT, padx=8)
    
    def create_all_scenarios_tab(self):
        """All scenarios demo tab with light blue theme"""
        tab = tk.Frame(self.notebook, bg='#e0f2fe', padx=25, pady=25)
        self.notebook.add(tab, text="ALL_SCENARIOS")
        
        card = tk.Frame(tab, bg='#ffffff', relief='flat', borderwidth=1, padx=30, pady=25)
        card.pack(fill=tk.BOTH, expand=True)
        
        # Section header
        header_section = tk.Frame(card, bg='#ffffff')
        header_section.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(header_section, text="[COMPLETE_DEMONSTRATION]",
                font=('JetBrains Mono', 16, 'bold'),
                bg='#ffffff', fg='#2563eb').pack(side=tk.LEFT)
        
        tk.Label(header_section, text="// Run all predefined test scenarios",
                font=('JetBrains Mono', 9),
                bg='#ffffff', fg='#64748b').pack(side=tk.LEFT, padx=(15, 0))
        
        tk.Label(card, text="Comprehensive CRC error detection demonstration:",
                font=('JetBrains Mono', 10),
                bg='#ffffff', fg='#64748b').pack(anchor='w', pady=(0, 20))
        
        # Professional scenarios list with enhanced styling
        scenarios_frame = tk.Frame(card, bg='#f0f9ff', padx=20, pady=20)
        scenarios_frame.pack(fill=tk.X, pady=(0, 25))
        
        scenarios = [
            "[+] Error-free transmission",
            "[+] Single bit error detection",
            "[+] Double bit error detection",
            "[+] Multiple bit errors",
            "[+] Burst error detection",
            "[+] Different polynomial demonstration"
        ]
        
        for i, scenario in enumerate(scenarios):
            scenario_label = tk.Label(scenarios_frame, text=scenario,
                    font=('JetBrains Mono', 11),
                    bg='#f1f5f9', fg='#10b981')
            scenario_label.pack(anchor='w', pady=6)
        
        # Professional buttons
        btn_frame = tk.Frame(card, bg='#ffffff')
        btn_frame.pack(pady=15)
        
        ttk.Button(btn_frame, text="[RUN_ALL_SCENARIOS]",
                 style='Success.TButton',
                 command=lambda: self.run_all_scenarios()).pack(side=tk.LEFT, padx=8)
        
        ttk.Button(btn_frame, text="[CLEAR_RESULTS]",
                 style='Secondary.TButton',
                 command=self.clear_results).pack(side=tk.LEFT, padx=8)
    
    def create_input_field(self, parent, label_text, field_name, default_value):
        """Create enhanced labeled input field with professional light theme"""
        tk.Label(parent, text=label_text,
                font=('JetBrains Mono', 10, 'bold'),
                bg='#ffffff', fg='#1e293b').pack(anchor='w', pady=(12, 6))
        
        # Use standard Entry for cursor color control
        entry = tk.Entry(parent, 
                        font=('JetBrains Mono', 12),
                        bg='#f0f9ff',
                        fg='#1e293b',
                        insertbackground='#1e293b',
                        relief='solid',
                        borderwidth=1,
                        width=50)
        entry.pack(pady=(0, 12))
        entry.insert(0, default_value)
        
        # Store reference
        setattr(self, f"{field_name}_entry", entry)
    
    def create_results_panel(self, parent):
        """Create enhanced results display panel with light blue theme"""
        results_frame = tk.Frame(parent, bg='#ffffff', relief='flat', borderwidth=1, padx=25, pady=25)
        results_frame.pack(fill=tk.BOTH, expand=True, pady=(12, 0))
        
        # Professional header with light blue theme
        header_frame = tk.Frame(results_frame, bg='#f0f9ff', relief='flat', borderwidth=0)
        header_frame.pack(fill=tk.X, pady=(0, 12))
        
        # Title section with professional styling
        title_section = tk.Frame(header_frame, bg='#f0f9ff')
        title_section.pack(side=tk.LEFT, padx=15, pady=10)
        
        tk.Label(title_section, text="[SIMULATION_RESULTS]",
                font=('JetBrains Mono', 14, 'bold'),
                bg='#f0f9ff', fg='#3b82f6').pack(anchor='w')
        
        tk.Label(title_section, text="// Long division format with step-by-step analysis",
                font=('JetBrains Mono', 9),
                bg='#f0f9ff', fg='#64748b').pack(anchor='w', pady=(2, 0))
        
        # Professional status indicator
        self.results_status = tk.Label(header_frame, text="[READY]",
                                    font=('JetBrains Mono', 10, 'bold'),
                                    bg='#f0f9ff', fg='#64748b')
        self.results_status.pack(side=tk.RIGHT, padx=20, pady=10)
        
        # Professional results text with code-like appearance
        self.results_text = scrolledtext.ScrolledText(results_frame,
                                                     font=('JetBrains Mono', 10),
                                                     bg='#f0f9ff',
                                                     fg='#1e293b',
                                                     wrap=tk.WORD,
                                                     height=30,
                                                     padx=20,
                                                     pady=20,
                                                     relief='flat',
                                                     borderwidth=0)
        self.results_text.pack(fill=tk.BOTH, expand=True)
        
        # Professional text styling with code syntax highlighting colors
        self.results_text.tag_config('success', foreground='#10b981', font=('JetBrains Mono', 10, 'bold'))
        self.results_text.tag_config('error', foreground='#ef4444', font=('JetBrains Mono', 10, 'bold'))
        self.results_text.tag_config('header', font=('JetBrains Mono', 11, 'bold'), foreground='#3b82f6')
        self.results_text.tag_config('step', font=('JetBrains Mono', 10, 'bold'), foreground='#8b5cf6')
        self.results_text.tag_config('info', foreground='#64748b', font=('JetBrains Mono', 10))
        self.results_text.tag_config('warning', foreground='#f59e0b', font=('JetBrains Mono', 10, 'bold'))
        self.results_text.tag_config('division', foreground='#1e293b', font=('JetBrains Mono', 10))
    
    def center_window(self):
        """Center window on screen"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() - 1600) // 2
        y = (self.root.winfo_screenheight() - 900) // 2
        self.root.geometry(f'1600x900+{x}+{y}')
    
    def toggle_poly_mode(self, mode):
        """Toggle between preset and custom polynomial mode"""
        if mode == 'custom':
            if self.custom_poly_mode.get() == 'preset':
                self.custom_poly_preset_frame.pack_forget()
                self.custom_poly_custom_frame.pack(anchor='w')
            else:
                self.custom_poly_custom_frame.pack_forget()
                self.custom_poly_preset_frame.pack(anchor='w')
        elif mode == 'random':
            if self.random_poly_mode.get() == 'preset':
                self.random_poly_preset_frame.pack_forget()
                self.random_poly_custom_frame.pack(anchor='w')
            else:
                self.random_poly_custom_frame.pack_forget()
                self.random_poly_preset_frame.pack(anchor='w')
        elif mode == 'burst':
            if self.burst_poly_mode.get() == 'preset':
                self.burst_poly_preset_frame.pack_forget()
                self.burst_poly_custom_frame.pack(anchor='w')
            else:
                self.burst_poly_custom_frame.pack_forget()
                self.burst_poly_preset_frame.pack(anchor='w')
        elif mode == 'poly_test':
            if self.poly_test_mode.get() == 'preset':
                self.poly_test_preset_frame.pack_forget()
                self.poly_test_custom_frame.pack(anchor='w')
            else:
                self.poly_test_custom_frame.pack_forget()
                self.poly_test_preset_frame.pack(anchor='w')
    
    def validate_custom_polynomial(self, polynomial):
        """Validate custom polynomial"""
        if not polynomial:
            return False, "Polynomial cannot be empty"
        
        if not all(c in '01' for c in polynomial):
            return False, "Polynomial must be binary (0s and 1s only)"
        
        if polynomial[0] != '1':
            return False, "Polynomial must start with 1"
        
        if polynomial.count('1') < 2:
            return False, "Polynomial must have at least two 1s"
        
        return True, ""
    
    def update_poly(self, mode):
        """Update polynomial based on selection"""
        poly_map = {
            "CRC-3 (1101)": "1101",
            "CRC-4 (10011)": "10011",
            "CRC-8 (100000111)": "100000111",
            "CRC-16 (10001000000100001)": "10001000000100001"
        }
        
        if mode == 'custom':
            if self.custom_poly_mode.get() == 'preset':
                self.simulator.polynomial = poly_map[self.custom_poly.get()]
            else:
                custom_poly = self.custom_poly_entry.get().strip()
                is_valid, error_msg = self.validate_custom_polynomial(custom_poly)
                if not is_valid:
                    messagebox.showerror("Invalid Polynomial", error_msg)
                    return False
                self.simulator.polynomial = custom_poly
        elif mode == 'random':
            if self.random_poly_mode.get() == 'preset':
                self.simulator.polynomial = poly_map[self.random_poly.get()]
            else:
                custom_poly = self.random_poly_entry.get().strip()
                is_valid, error_msg = self.validate_custom_polynomial(custom_poly)
                if not is_valid:
                    messagebox.showerror("Invalid Polynomial", error_msg)
                    return False
                self.simulator.polynomial = custom_poly
        elif mode == 'burst':
            if self.burst_poly_mode.get() == 'preset':
                self.simulator.polynomial = poly_map[self.burst_poly.get()]
            else:
                custom_poly = self.burst_poly_entry.get().strip()
                is_valid, error_msg = self.validate_custom_polynomial(custom_poly)
                if not is_valid:
                    messagebox.showerror("Invalid Polynomial", error_msg)
                    return False
                self.simulator.polynomial = custom_poly
        
        self.simulator.polynomial_length = len(self.simulator.polynomial)
        
        # Update header indicator
        poly_display = f"CRC-{self.simulator.polynomial_length-1}" if self.simulator.polynomial_length <= 17 else "CUSTOM"
        self.poly_indicator.config(text=f"POLY: {poly_display}")
        
        return True
    
    def run_custom_test(self):
        """Run custom data test"""
        data = self.custom_data_entry.get().strip()
        
        if not data or not all(c in '01' for c in data):
            messagebox.showerror("Error", "Enter valid binary data")
            return
        
        if not self.update_poly('custom'):
            return
        
        error_input = self.custom_errors_entry.get().strip()
        errors = []
        if error_input:
            try:
                # Convert from 1-based to 0-based indexing
                errors = [int(x) - 1 for x in error_input.split()]
                # Validate positions are within bounds
                data_with_crc_length = len(data) + self.simulator.polynomial_length - 1
                errors = [pos for pos in errors if 0 <= pos < data_with_crc_length]
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
        
        if not self.update_poly('random'):
            return
        
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
        
        if not self.update_poly('burst'):
            return
        
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
        """Run polynomial comparison test with detailed output"""
        data = self.poly_data_entry.get().strip()
        
        if not data or not all(c in '01' for c in data):
            messagebox.showerror("Error", "Enter valid binary data")
            return
        
        error_input = self.poly_errors_entry.get().strip()
        errors = []
        if error_input:
            try:
                # Convert from 1-based to 0-based indexing
                errors = [int(x) - 1 for x in error_input.split()]
            except ValueError:
                messagebox.showerror("Error", "Invalid error positions")
                return
        
        # Check if using custom polynomials
        if self.poly_test_mode.get() == 'custom':
            poly1 = self.poly_test_custom1_entry.get().strip()
            poly2 = self.poly_test_custom2_entry.get().strip()
            
            # Validate both polynomials
            is_valid1, error_msg1 = self.validate_custom_polynomial(poly1)
            if not is_valid1:
                messagebox.showerror("Invalid Polynomial", f"First polynomial: {error_msg1}")
                return
            
            is_valid2, error_msg2 = self.validate_custom_polynomial(poly2)
            if not is_valid2:
                messagebox.showerror("Invalid Polynomial", f"Second polynomial: {error_msg2}")
                return
            
            polys = [
                ("Custom Polynomial 1", poly1, f"Custom {len(poly1)-1}-bit CRC", 
                 f"This is a user-defined custom polynomial with degree {len(poly1)-1}. The polynomial {poly1} can be used for specialized error detection requirements where standard polynomials may not be optimal."),
                ("Custom Polynomial 2", poly2, f"Custom {len(poly2)-1}-bit CRC",
                 f"This is a user-defined custom polynomial with degree {len(poly2)-1}. The polynomial {poly2} can be used for specialized error detection requirements where standard polynomials may not be optimal.")
            ]
        else:
            selection = self.poly_test_selection.get()
            
            if selection == "CRC-3 vs CRC-4":
                polys = [
                    ("CRC-3", "1101", "3-bit CRC - Good for simple error detection", 
                     "The CRC-3 polynomial is the simplest form of CRC, using a 3-bit remainder. It is suitable for small data packets where basic error detection is sufficient. The polynomial 1101 provides a good balance between simplicity and error detection capability for small-scale applications."),
                    ("CRC-4", "10011", "4-bit CRC - Better error detection capability",
                     "CRC-4 uses a 4-bit remainder, offering improved error detection compared to CRC-3. The polynomial 10011 is commonly used in telecommunications and small embedded systems where better error detection is required without significant overhead.")
                ]
            elif selection == "CRC-4 vs CRC-8":
                polys = [
                    ("CRC-4", "10011", "4-bit CRC - Suitable for small data",
                     "CRC-4 with polynomial 10011 provides a good compromise between overhead and error detection for small data sets. It is particularly useful in resource-constrained environments where computational resources are limited."),
                    ("CRC-8", "100000111", "8-bit CRC - Standard for many protocols",
                     "CRC-8 is widely adopted in many communication protocols and embedded systems. The polynomial 100000111 provides strong error detection capabilities for moderate-sized data packets and is the de facto standard for many industrial applications.")
                ]
            else:
                polys = [
                    ("CRC-8", "100000111", "8-bit CRC - Common in communication protocols",
                     "CRC-8 with polynomial 100000111 is extensively used in various communication protocols including SMBus, PMBus, and many proprietary protocols. It offers excellent error detection for 8-bit data systems and provides a good balance between performance and computational complexity."),
                    ("CRC-16", "10001000000100001", "16-bit CRC - High reliability for large data",
                     "CRC-16 is a robust error detection mechanism used in high-reliability systems such as USB, Modbus, and many industrial automation protocols. The polynomial 10001000000100001 (CRC-16-IBM) provides superior error detection for larger data packets and is essential for applications where data integrity is critical.")
                ]
        
        output = []
        output.append("="*70)
        output.append("POLYNOMIAL COMPARISON TEST - DETAILED ANALYSIS")
        output.append("="*70)
        output.append("")
        output.append(f"Test Configuration:")
        output.append(f"  Data: {data}")
        output.append(f"  Data Length: {len(data)} bits")
        output.append(f"  Error Positions: {[e+1 for e in errors] if errors else 'None'}")
        output.append(f"  Number of Errors: {len(errors)}")
        output.append("")
        output.append("-"*70)
        output.append("")
        
        for name, poly, description, detailed_desc in polys:
            self.simulator.polynomial = poly
            self.simulator.polynomial_length = len(poly)
            result = self.simulator.demonstrate_transmission(data, errors, show_steps=False)
            
            output.append(f"[{name.upper()}]")
            output.append(f"Polynomial: {poly}")
            output.append(f"Degree: {len(poly)-1} bits")
            output.append(f"Summary: {description}")
            output.append("")
            output.append(f"Detailed Description:")
            output.append(f"  {detailed_desc}")
            output.append("")
            output.append(f"Test Results:")
            output.append(f"  Original Data: {result['original_data']}")
            output.append(f"  CRC Checksum: {result['crc_checksum']}")
            output.append(f"  Transmitted Data: {result['transmitted_data']}")
            output.append(f"  Received Data: {result['received_data']}")
            output.append("")
            output.append(f"Verification:")
            output.append(f"  Remainder: {result['remainder']}")
            output.append(f"  Status: {'VALID - No errors detected' if result['is_valid'] else 'INVALID - Errors detected'}")
            if errors:
                output.append(f"  Error Detection: {'SUCCESSFUL' if not result['is_valid'] else 'FAILED (errors went undetected)'}")
            else:
                output.append(f"  Error Detection: N/A (no errors introduced)")
            output.append("")
            output.append("-"*70)
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
        """Display results with formatting matching the image"""
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
            elif line.startswith("STEP") or line.startswith("CRC") or line.startswith("TRANSMISSION") or line.startswith("BURST") or line.startswith("POLYNOMIAL") or line.startswith("ORIGINAL") or line.startswith("SIMULATION"):
                self.results_text.tag_add('header', f"{i}.0", f"{i}.end")
            elif "XOR" in line or "Step" in line or "dividend" in line.lower() or "bit" in line.lower():
                self.results_text.tag_add('step', f"{i}.0", f"{i}.end")
            elif "Remainder" in line or "Polynomial" in line or "Data" in line or "Quotient" in line or "Zeros" in line or "Length" in line or "Appended" in line:
                self.results_text.tag_add('info', f"{i}.0", f"{i}.end")
        
        # Update status
        if is_valid:
            self.results_status.config(text="[VALID]", fg='#10b981')
            self.header_status.config(text="[VALID]", fg='#10b981')
        else:
            self.results_status.config(text="[ERROR_DETECTED]", fg='#ef4444')
            self.header_status.config(text="[ERROR_DETECTED]", fg='#ef4444')
    
    def clear_field(self, mode):
        """Clear specific field"""
        if mode == 'custom':
            self.custom_data_entry.delete(0, tk.END)
            self.custom_data_entry.insert(0, "1011001")
            self.custom_errors_entry.delete(0, tk.END)
            self.custom_poly_entry.delete(0, tk.END)
            self.custom_poly_entry.insert(0, "10011")
            self.custom_poly_mode.set("preset")
            self.toggle_poly_mode('custom')
        elif mode == 'random':
            self.random_length.delete(0, tk.END)
            self.random_length.insert(0, "16")
            self.random_errors.delete(0, tk.END)
            self.random_errors.insert(0, "2")
            self.random_poly_entry.delete(0, tk.END)
            self.random_poly_entry.insert(0, "1101")
            self.random_poly_mode.set("preset")
            self.toggle_poly_mode('random')
        elif mode == 'burst':
            self.burst_data_entry.delete(0, tk.END)
            self.burst_data_entry.insert(0, "1011001")
            self.burst_length.delete(0, tk.END)
            self.burst_length.insert(0, "3")
            self.burst_poly_entry.delete(0, tk.END)
            self.burst_poly_entry.insert(0, "1101")
            self.burst_poly_mode.set("preset")
            self.toggle_poly_mode('burst')
        elif mode == 'poly':
            self.poly_data_entry.delete(0, tk.END)
            self.poly_data_entry.insert(0, "1101011011")
            self.poly_errors_entry.delete(0, tk.END)
            self.poly_errors_entry.insert(0, "3 7")
            self.poly_test_custom1_entry.delete(0, tk.END)
            self.poly_test_custom1_entry.insert(0, "1101")
            self.poly_test_custom2_entry.delete(0, tk.END)
            self.poly_test_custom2_entry.insert(0, "10011")
            self.poly_test_mode.set("preset")
            self.toggle_poly_mode('poly_test')
    
    def clear_results(self):
        """Clear results panel with technical format"""
        self.results_text.delete(1.0, tk.END)
        self.results_status.config(text="[READY]", fg='#64748b')
        self.header_status.config(text="[SYSTEM_READY]", fg='#10b981')


def main():
    root = tk.Tk()
    app = CompleteCRCGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
