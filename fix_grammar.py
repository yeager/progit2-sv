#!/usr/bin/env python3
import os
import re
import glob

# Define the patterns that need fixing
# Patterns for definite form corrections after den här/det här/de här
patterns = [
    # det här + noun (needs -et or -t ending)
    (r'\bdet här kapitel\b', 'det här kapitlet'),
    (r'\bdet här avsnitt\b', 'det här avsnittet'),
    (r'\bdet här kommando\b', 'det här kommandot'),
    (r'\bdet här sätt\b', 'det här sättet'),
    (r'\bdet här skript\b', 'det här skriptet'),
    (r'\bdet här fall\b', 'det här fallet'),
    (r'\bdet här flöde\b', 'det här flödet'),
    (r'\bdet här projekt\b', 'det här projektet'),
    (r'\bdet här steg\b', 'det här steget'),
    (r'\bdet här meddelande\b', 'det här meddelandet'),
    
    # den här + noun (needs -en or -n ending) 
    (r'\bden här bok\b', 'den här boken'),
    (r'\bden här fil\b', 'den här filen'),
    (r'\bden här funktion\b', 'den här funktionen'),
    (r'\bden här krok\b', 'den här kroken'),
    
    # de här + noun (needs -na, -erna, -arna, -orna ending)
    (r'\bde här filer\b', 'de här filerna'),
    (r'\bde här verktyg\b', 'de här verktygen'),
    (r'\bde här incheckningar\b', 'de här incheckningarna'),
    (r'\bde här ändringar\b', 'de här ändringarna'),
    (r'\bde här kommandon\b', 'de här kommandona'),
    (r'\bde här system\b', 'de här systemen'),
]

def fix_file(filepath):
    """Fix grammatical errors in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes_made = []
    
    for pattern, replacement in patterns:
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            # Find what was changed
            matches = re.findall(pattern, content)
            for match in matches:
                changes_made.append(f"{match} → {replacement}")
            content = new_content
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filepath}:")
        for change in changes_made:
            print(f"  {change}")
        return True
    return False

def main():
    """Find and fix all .asc files in the book directory."""
    book_dir = 'book'
    if not os.path.exists(book_dir):
        print("Book directory not found!")
        return
    
    files_changed = 0
    total_changes = 0
    
    # Find all .asc files
    for filepath in glob.glob(f"{book_dir}/**/*.asc", recursive=True):
        if fix_file(filepath):
            files_changed += 1
    
    print(f"\nSummary: Modified {files_changed} files")

if __name__ == "__main__":
    main()