from typing import Dict, List
import language_tool_python
import os
from dotenv import load_dotenv

class GrammarChecker:
    def __init__(self):
        # Initialize LanguageTool with English (US) language
        self.lt = language_tool_python.LanguageTool('en-US')

    def analyze_text(self, text: str) -> Dict:
        """Analyze text using LanguageTool with detailed categorization."""
        matches = self.lt.check(text)
        
        # Categorize issues
        categories = {
            'Grammar': [],
            'Spelling': [],
            'Punctuation': [],
            'Style': [],
            'Other': []
        }
        
        for match in matches:
            category = self._categorize_issue(match.ruleId)
            categories[category].append({
                'message': match.message,
                'replacements': match.replacements,
                'context': match.context,
                'rule_id': match.ruleId,
                'category': category,
                'offset': match.offset,
                'length': match.errorLength
            })
        
        # Get corrected text
        corrected_text = self._apply_corrections(text, matches)
        
        return {
            'total_issues': len(matches),
            'categories': {
                cat: len(issues) for cat, issues in categories.items()
            },
            'suggestions': categories,
            'original_text': text,
            'corrected_text': corrected_text
        }
    
    def _categorize_issue(self, rule_id: str) -> str:
        """Categorize the issue based on LanguageTool's rule ID."""
        rule_id = rule_id.lower()
        
        if any(x in rule_id for x in ['grammar', 'verb', 'tense']):
            return 'Grammar'
        elif any(x in rule_id for x in ['spell', 'typo']):
            return 'Spelling'
        elif any(x in rule_id for x in ['punct', 'comma', 'apos']):
            return 'Punctuation'
        elif any(x in rule_id for x in ['style', 'word_choice']):
            return 'Style'
        else:
            return 'Other'
    
    def _apply_corrections(self, text: str, matches: List) -> str:
        """Apply all corrections to the text."""
        # Sort matches by offset in reverse order to avoid index issues
        sorted_matches = sorted(matches, key=lambda x: x.offset, reverse=True)
        
        corrected_text = text
        for match in sorted_matches:
            if match.replacements:
                # Apply the first suggested replacement
                start = match.offset
                end = start + match.errorLength
                corrected_text = corrected_text[:start] + match.replacements[0] + corrected_text[end:]
        
        return corrected_text

def print_results(results: Dict):
    """Print the analysis results in a clear, well-formatted way."""
    print("\n" + "="*60)
    print(" "*20 + "GRAMMAR CHECK RESULTS")
    print("="*60 + "\n")
    
    # Print text comparison in a box
    print("📝 TEXT COMPARISON")
    print("-"*60)
    print(f"Original:  {results['original_text']}")
    print(f"Corrected: {results['corrected_text']}")
    print("-"*60 + "\n")
    
    # Print summary in a clean format
    print("📊 SUMMARY")
    print("-"*60)
    print(f"Total issues found: {results['total_issues']}")
    
    # Only show categories with issues
    if results['total_issues'] > 0:
        print("\nIssues breakdown:")
        for category, count in results['categories'].items():
            if count > 0:
                print(f"  • {category}: {count}")
        print("-"*60 + "\n")
        
        # Print detailed analysis in a table format
        print("🔍 DETAILED ANALYSIS")
        print("-"*60)
        print(f"{'Type':<15}{'Error':<30}{'Suggestion':<25}")
        print("-"*60)
        
        for category, issues in results['suggestions'].items():
            if issues:
                for issue in issues:
                    error_type = category
                    error_msg = issue['message'][:27] + "..." if len(issue['message']) > 30 else issue['message']
                    suggestion = issue['replacements'][0] if issue['replacements'] else "No suggestion"
                    print(f"{error_type:<15}{error_msg:<30}{suggestion:<25}")
        
        print("-"*60)
        print("\n💡 DETAILED EXPLANATIONS")
        print("-"*60)
        for category, issues in results['suggestions'].items():
            if issues:
                for issue in issues:
                    print(f"\nIssue Type: {category}")
                    print(f"Problem: {issue['message']}")
                    if issue['replacements']:
                        print(f"Solution: Use '{issue['replacements'][0]}' instead")
                    print(f"Context: \"{issue['context']}\"")
        print("-"*60)
    
    print("\n✨ Done! Your text has been checked for grammar issues.\n")

def main():
    print("Welcome to the Grammar Checker!")
    print("Using LanguageTool - Free and Open Source Grammar Checker")
    print("\nPlease enter the text you want to analyze:")
    
    # Read a single line of text
    text = input("> ")
    
    if not text.strip():
        print("No text provided. Exiting...")
        return
    
    checker = GrammarChecker()
    results = checker.analyze_text(text)
    print_results(results)

if __name__ == "__main__":
    main() 