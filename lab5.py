
class AnalysisError(Exception):
    pass

class TextDataAnalyzer:
    
    def analyze(self, data):
        try:
            
            studio_info = {"title": "Movie Script", "length": "120 pages"}
            director = studio_info["director"]  
            
            word_count = len(data.split())
            print(f"The script contains {word_count} words.")
        
        except KeyError as e:
            print(f"KeyError: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

class NumericDataAnalyzer:
    
    def analyze(self, data):
        try:
    
            result = data / "string"  
            
            print(f"The result is {result}.")
        
        except TypeError as e:
            print(f"TypeError: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def analyze_positive_number(self, data):
        try:
        
            if data < 0:
                raise ValueError("Number must be positive")
            
            print(f"The number {data} is positive.")
        
        except ValueError as e:
            print(f"ValueError: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":

    text_analyzer = TextDataAnalyzer()
    numeric_analyzer = NumericDataAnalyzer()
    
    sample_text = "This is a studio script."
    sample_number = 1000
    negative_number = -500
    
    print("\nAnalyzing text data:")
    text_analyzer.analyze(sample_text)
    
    print("\nAnalyzing numeric data:")
    numeric_analyzer.analyze(sample_number)
    
    print("\nAnalyzing a positive number:")
    numeric_analyzer.analyze_positive_number(negative_number)
