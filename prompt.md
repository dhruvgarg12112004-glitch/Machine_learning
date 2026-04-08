# Diagram Generation Prompts for Audio GUI Research Report

This file contains detailed prompts for generating each diagram used in the research report. Use these prompts with AI tools, design software, or copy them for manual creation.

---

## Figure 3.1: System Architecture Diagram

### Prompt for Diagram Generation Tools (Draw.io, Lucidchart, etc.):

```
Create a three-layered system architecture diagram for a web-based audio processing application with the following structure:

PRESENTATION LAYER (Top):
- Web Browser (Chrome/Firefox icon)
- HTML5 Interface
- JavaScript Event Handlers
- User Input Forms
- Visualization Containers

APPLICATION LAYER (Middle):
- Flask Server (Python icon)
- REST API Endpoints (GET/POST routes)
- Request Router
- Parameter Validator
- Business Logic Handler

PROCESSING LAYER (Bottom):
- Audio File Handler
- Librosa Library (Feature Extraction)
- NumPy (Numerical Computation)
- SciPy (Signal Processing)
- Database/Storage (SQLite)

CONNECTIONS:
- Arrows showing HTTP requests/responses between Presentation and Application layers
- Arrows showing function calls between Application and Processing layers
- Bidirectional data flow arrows

COLOR SCHEME:
- Presentation Layer: Light Blue background
- Application Layer: Light Green background
- Processing Layer: Light Orange background
- Use icons for each major component
- Add labels showing data types (JSON, Audio File, Features, etc.)

DIMENSIONS: 1200px × 800px
FILE FORMAT: PNG or PDF
```

---

## Figure 3.2: Audio Processing Workflow Flowchart

### Prompt for Flowchart Generation Tools (Lucidchart, Draw.io, Graphviz):

```
Create a detailed audio processing workflow flowchart with the following decision trees and processes:

START NODE: File Upload

PROCESS 1: File Validation
↓ (Success) | ↗ (Failure → Error Message → END)

PROCESS 2: Load Audio File
↓

PROCESS 3: Audio Preprocessing
- Normalize amplitude
- Handle stereo-to-mono conversion
- Apply anti-aliasing filters
↓

PROCESS 4: Preprocessing Quality Check
↓ (Pass) | ↗ (Fail → Reprocess)

PROCESS 5: Frame-based Audio Splitting
↓

PROCESS 6A: Time-Domain Feature Extraction (Parallel)
- RMS Energy
- Zero-Crossing Rate
- Amplitude Statistics
↓

PROCESS 6B: Frequency-Domain Feature Extraction (Parallel)
- Fast Fourier Transform
- Mel-Scale Mapping
- MFCC Computation
↓

PROCESS 7: Feature Aggregation
↓

PROCESS 8: Generate Visualizations
- Waveform Plot
- Spectrogram
- Frequency Domain Plot
↓

PROCESS 9: Store Results
↓

END NODE: Display to User

STYLING:
- Use rounded rectangles for start/end
- Use rectangles for processes
- Use diamonds for decisions
- Use blue arrows for main flow
- Use red arrows for error paths
- Use green arrows for success paths
- Add timing annotations (e.g., "2.3 sec average")

DIMENSIONS: 1000px × 1400px
FILE FORMAT: PNG or PDF
```

---

## Table 3.4: Computational Complexity Analysis

### Prompt for Table/Chart Generation:

```
Create a professional comparison table with the following specifications:

TABLE TITLE: "Computational Complexity Analysis of Processing Components"

COLUMNS:
1. Component
2. Description
3. Time Complexity
4. Space Complexity
5. Typical Throughput

DATA ROWS:
1. File I/O
   - Sequential audio file reading from disk
   - O(n) where n = file size
   - O(1) constant space
   - 50 MB/min

2. Audio Format Decoding
   - MP3/WAV/FLAC decoding
   - O(n) optimized decoding
   - O(n) buffer space
   - 45 MB/min

3. FFT (Fast Fourier Transform)
   - Frequency domain conversion in overlapping frames
   - O(n log n) per audio duration
   - O(n) for frequency bins
   - 40 MB/min

4. MFCC Feature Extraction
   - Mel-frequency cepstral coefficient computation per frame
   - O(n·m) where n=samples, m=features
   - O(m) for feature vectors
   - 30 MB/min

5. Feature Aggregation
   - Combining multiple feature sets
   - O(k) where k = features
   - O(k) minimal memory
   - 60 MB/min

6. Visualization Generation
   - Creating plots and spectrograms for display
   - O(k) where k = visualization points
   - O(k) image buffer
   - 55 MB/min

FORMATTING:
- Use alternating row colors (white/light gray)
- Bold column headers
- Right-align numeric values
- Add footnotes explaining Big-O notation
- Include legends for complexity notation
- Font: Arial, 11pt

DIMENSIONS: 1000px × 500px or as markdown table
FILE FORMAT: PNG or SVG (or CSV/Markdown table)
```

---

## Table 4.1: Hardware/Software Requirements Summary

### Prompt for Requirements Table Generation:

```
Create a comprehensive hardware and software requirements table with the following structure:

TABLE TITLE: "Hardware/Software Requirements for Audio GUI System"

PART A: HARDWARE REQUIREMENTS

COLUMNS: Component | Minimum Specification | Recommended Specification | Notes

ROWS:
1. Processor
   Minimum: Intel Core i5 (6th gen) or equivalent, 2.5 GHz quad-core
   Recommended: Intel Core i7 (8th gen) or higher, 3.5 GHz
   Notes: Supports multi-threaded processing

2. RAM (Memory)
   Minimum: 8 GB DDR4
   Recommended: 16 GB DDR4 or higher
   Notes: Handles simultaneous multi-file processing

3. Storage
   Minimum: 50 GB SSD for application and cache
   Recommended: 100+ GB SSD for large batch operations
   Notes: Fast I/O recommended for audio processing

4. Network
   Minimum: 5 Mbps stable connection
   Recommended: 10+ Mbps for cloud deployment
   Notes: Required for web server access only

PART B: SOFTWARE REQUIREMENTS

COLUMNS: Component | Requirement | Notes

ROWS:
1. Operating System
   Windows 10/11, macOS 10.15+, Linux (Ubuntu 20.04+)
   Cross-platform support

2. Python
   Version 3.8 or higher
   Compatibility with scientific packages

3. Web Server
   Flask 2.0+
   Lightweight production deployment

4. Database
   SQLite (local) or PostgreSQL (production)
   User data and cache storage

5. Web Browser
   Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
   HTML5, CSS3, ES6 JavaScript support

6. Audio Libraries
   librosa, numpy, scipy, matplotlib
   Audio processing and visualization

STYLING:
- Two-column headers (Minimum vs Recommended)
- Color code: Green for recommended, Yellow for minimum acceptable
- Use checkmarks (✓) for supported items
- Add system compatibility matrix showing OS compatibility
- Include version numbers with "+" notation

DIMENSIONS: 1100px × 600px
FILE FORMAT: PNG, SVG, or HTML table
```

---

## Table 4.2: Dataset Characteristics and Validation Set Distribution

### Prompt for Dataset Visualization:

```
Create a dataset overview table and distribution chart with the following information:

TABLE TITLE: "Dataset Characteristics and Validation Distribution"

TABLE COLUMNS: Dataset Name | Category Type | Number of Classes/Categories | Total Files | Duration per File | Total Hours | Format | Training Split | Validation Split

TABLE ROWS:
1. GTZAN Genre Classification
   - Music Genre Classification
   - 10 genres (Blues, Classical, Country, Disco, Electronic, Folk, Hip-Hop, Jazz, Metal, Pop, Reggae, Rock)
   - 1000 songs
   - 30 seconds
   - 8.3 hours
   - MP3
   - 800 files (80%)
   - 200 files (20%)

2. ESC-50 Environmental Sounds
   - Environmental Sound Classification
   - 50 environmental categories
   - 2000 recordings
   - 5 seconds
   - 2.8 hours
   - WAV
   - 1600 files (80%)
   - 400 files (20%)

3. Custom Audio Samples
   - Mixed (speech, music, noise)
   - 5 categories
   - 500 files
   - Variable (10-60 sec)
   - 4.2 hours
   - MP3/WAV/FLAC
   - 400 files (80%)
   - 100 files (20%)

ADDITIONAL VISUALIZATIONS:
1. Pie Chart: Distribution of files across datasets
2. Bar Chart: Duration comparison (hours per dataset)
3. Stacked Bar Chart: Training vs Validation split per dataset
4. Heatmap: File count distribution by category and dataset

COLOR SCHEME:
- GTZAN: Blue
- ESC-50: Orange
- Custom: Green

ANNOTATIONS:
- Add total dataset size (11.3 hours combined)
- Show cross-validation strategy
- Include data augmentation notes (3x expansion mentioned)

DIMENSIONS: Table 1200px × 400px, Charts 1000px × 600px
FILE FORMAT: PNG or interactive SVG
```

---

## Table 4.3: Performance Metrics and Validation Results

### Prompt for Performance Metrics Visualization:

```
Create a comprehensive performance metrics dashboard/table with the following specifications:

TABLE TITLE: "Performance Metrics and Validation Results"

COLUMNS: Metric Name | Measured Value | Unit | Target/Goal | Status | Notes

ROWS:
1. Feature Extraction Accuracy
   95%
   Percentage
   ≥90%
   ✓ PASS
   Consistency across repeated processing of same file

2. Processing Latency
   2.3
   Seconds
   <5 sec
   ✓ PASS
   For 3-5 minute audio files on reference hardware

3. Peak Memory Consumption
   180
   MB
   <500 MB
   ✓ PASS
   Typical audio file, hybrid methodology

4. Batch Processing Throughput
   50
   MB/min
   >25 MB/min
   ✓ PASS
   Sustained rate for continuous processing

5. Visualization Response Time
   420
   Milliseconds
   <500 ms
   ✓ PASS
   User interface responsiveness

6. Cross-Format Compatibility
   100% (MP3/WAV/FLAC)
   Percentage
   80%+
   ✓ PASS
   Tested with major audio formats

7. User Interface Uptime
   99.8%
   Percentage
   ≥99%
   ✓ PASS
   Monthly availability measurement

8. Error Rate
   0.2%
   Percentage
   <1%
   ✓ PASS
   Failed processing attempts per total submissions

ADDITIONAL VISUALIZATIONS:
1. Gauge Charts: One for each metric showing performance against target
2. Progress Bars: Visual representation of metric achievement
3. Timeline Graph: Latency improvement over software versions
4. Comparison Bar Chart: All metrics vs targets

STYLING:
- ✓ Green background/checkmark for PASS
- ✗ Red background/X for FAIL
- Yellow for WARNING/CAUTION status
- Large numbers (font size 16+) for key metrics
- Smaller text for notes/details

DIMENSIONS: Table 1100px × 500px, Dashboard 1200px × 800px
FILE FORMAT: PNG, SVG, or interactive HTML dashboard
```

---

## Table 5.1: Comparative Analysis of Processing Methodologies

### Prompt for Methodology Comparison Chart:

```
Create a comprehensive methodology comparison table and visualization with the following data:

TABLE TITLE: "Comparative Analysis of Processing Methodologies and Performance Metrics"

COLUMNS: 
Metric Name | M1: Time-Domain Features | M2: Frequency-Domain (MFCC) | M3: Hybrid Multi-Feature | Winner

DATA ROWS:
1. Feature Extraction Accuracy
   82%
   94%
   95%
   M3 (Hybrid)
   
2. Processing Latency (per minute of audio)
   50 ms
   150-200 ms
   180-220 ms
   M1 (Time-Domain)

3. Memory Consumption
   50 MB
   150 MB
   180 MB
   M1 (Time-Domain)

4. Throughput (MB/minute)
   75
   35
   30
   M1 (Time-Domain)

5. Feature Discrimination Quality
   Low-Medium
   High
   Very High
   M3 (Hybrid)

6. Spectral Information Capture
   Limited
   Excellent
   Comprehensive
   M3 (Hybrid)

7. Temporal Dynamics Capture
   Good
   Medium
   Excellent
   M3 (Hybrid)

8. Computational Efficiency Score (1-10)
   9
   6
   5
   M1 (Time-Domain)

9. Overall Quality Score (1-10)
   6
   8
   9
   M3 (Hybrid)

DESCRIPTION OF METHODOLOGIES:

M1 - TIME-DOMAIN FEATURES:
- Zero-crossing rate, RMS energy, amplitude statistics
- Fastest computation, limited spectral information
- Best for real-time applications requiring speed

M2 - FREQUENCY-DOMAIN (MFCC):
- Mel-frequency cepstral coefficients, spectral characteristics
- Moderate speed, good spectral representation
- Suitable for feature-rich analysis

M3 - HYBRID MULTI-FEATURE:
- Combines time-domain AND frequency-domain features
- Balanced approach, best feature quality
- Recommended methodology for this project

VISUALIZATION RECOMMENDATIONS:
1. Radar/Spider Chart: Comparing all 9 metrics across 3 methodologies
2. Side-by-side Bar Chart: Accuracy comparison
3. Grouped Bar Chart: Latency and Memory comparison
4. Performance vs Speed Trade-off Scatter Plot
5. Overall Score Comparison (larger chart/graph)

COLOR SCHEME:
- M1 (Time-Domain): Blue
- M2 (Frequency-Domain): Orange
- M3 (Hybrid): Green (highlight as recommended)

ANNOTATIONS:
- Add "RECOMMENDED" badge to M3
- Include notes about trade-offs
- Show computational complexity annotations
- Highlight best performer in each metric category

DIMENSIONS: Table 1200px × 600px, Radar Chart 800px × 800px, Bar Charts 1000px × 500px
FILE FORMAT: PNG, SVG, or interactive dashboard
```

---

## General Guidelines for All Diagrams

### For Using with AI Image Generation Tools (DALL-E, Midjourney, etc.):

```
Use a more natural language prompt like:

"Create a professional research-quality [DIAGRAM_TYPE] showing [DESCRIPTION]. 
The diagram should include [SPECIFIC_ELEMENTS]. 
Use a [COLOR_SCHEME] color scheme. 
The style should be [STYLE]. 
Include labels and legends. 
The image should be suitable for academic publication."

Example for Figure 3.1:
"Create a professional system architecture diagram for a web-based audio processing 
application showing three layers: presentation (web browser), application (Flask server), 
and processing (libraries). Use light blue, green, and orange backgrounds for each layer. 
Include component icons and data flow arrows. Professional technical illustration style, 
suitable for academic publication."
```

### For Using with Design Tools (Figma, Adobe XD, etc.):

```
1. Create new project/canvas
2. Set artboard size as specified in DIMENSIONS
3. Use the element descriptions to build components
4. Apply colors from COLOR SCHEME
5. Add text labels and annotations
6. Export as PNG (300 DPI for publication) or PDF (vector format)
```

### For Using with Code-Based Diagram Tools (PlantUML, Mermaid, Graphviz):

```
PlantUML Example for Architecture:
@startlayout
title System Architecture

rectangle "Presentation Layer" {
    component [Web Browser]
    component [HTML5 Interface]
    component [JavaScript Handler]
}

rectangle "Application Layer" {
    component [Flask Server]
    component [REST API]
}

rectangle "Processing Layer" {
    component [Librosa]
    component [NumPy]
}

@endlayout
```

---

## File Organization

Suggested folder structure for saving generated diagrams:

```
Audio GUI/
├── diagrams/
│   ├── Figure_3_1_System_Architecture.png
│   ├── Figure_3_2_Audio_Processing_Flowchart.png
│   ├── Table_3_4_Complexity_Analysis.png
│   ├── Table_4_1_Hardware_Software_Requirements.png
│   ├── Table_4_2_Dataset_Characteristics.png
│   ├── Table_4_3_Performance_Metrics.png
│   ├── Table_5_1_Methodology_Comparison.png
│   └── prompt.md (this file)
├── research_report.md
├── app.py
└── templates/
```

---

## Tools Recommended for Each Diagram Type

| Diagram Type | Best Tools | Alternative Tools |
|---|---|---|
| System Architecture | Draw.io, Lucidchart, Visio | OmniGraffle, Miro |
| Flowchart | Lucidchart, Draw.io, Graphviz | Visio, Miro |
| Tables & Charts | Excel, Google Sheets, Tableau | Python (Matplotlib), Plotly |
| Complex Diagrams | Adobe Illustrator, Figma | Sketch, CorelDRAW |
| Code Diagrams | PlantUML, Mermaid, Graphviz | ASCII diagram tools |

---

## Tips for Publication-Quality Diagrams

1. **Resolution**: Use 300 DPI for printed materials, 96 DPI for web
2. **Format**: PNG for final images, SVG for editable versions
3. **Fonts**: Use professional fonts (Arial, Helvetica, Times New Roman)
4. **Colors**: Ensure colorblind-friendly palette
5. **Labels**: Clear, readable text with consistent sizing
6. **Consistency**: Match styling across all diagrams
7. **Captions**: Include descriptive figure captions
8. **Legends**: Add legends for complex diagrams

---

**Last Updated**: April 1, 2026
**Project**: Audio GUI - Web-Based Audio Processing Application
**Report**: Research Report with Comprehensive Diagrams
