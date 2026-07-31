import sys
import time

def animated_spinner(message="Analyzing code", duration=3):
    """Displays an animated spinning wheel in the terminal."""
    spinner_symbols = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    i = 0
      
    while time.time() < end_time:
        sys.stdout.write(f'\r[+] {message} {spinner_symbols[i % len(spinner_symbols)]}')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
          
    print(f'\r[✓] {message} Complete!   ')

 
def typewriter_text(text, speed=0.03):
    """Prints text letter-by-letter for a terminal UI effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def animated_progress_bar(task_label="Applying Patches", total_steps=40, delay=0.03):
    """Displays a dynamic progress bar that fills up in real-time."""
    print(f"\n{task_label}:")
    for i in range(total_steps + 1):
        percent = (i / total_steps) * 100
        bar = '█' * i + '-' * (total_steps - i)
        sys.stdout.write(f'\r[{bar}] {percent:.1f}%')
        sys.stdout.flush()
        time.sleep(delay)
    print("\n[✓] All steps successfully completed!")



if __name__ == "__main__":
    # 1. Typewriter Banner
    typewriter_text(">>> TeamDrag CodeScan Terminal Interface", speed=0.02)
    typewriter_text(">>> Initializing Self-Healing and Diagnostics Modules...", speed=0.02)
    print("-" * 55)
    
    # 2. Spinner Animation
    animated_spinner(message="Scanning workspace directory", duration=3)
    
    # 3. Progress Bar Animation
    animated_progress_bar(task_label="Injecting Code Patches", total_steps=35, delay=0.04)
    
    # 4. Final Typewriter Confirmation
    print("-" * 55)
    typewriter_text(">>> System Status: STABLE | 0 Critical Bugs Remaining.", speed=0.02)
