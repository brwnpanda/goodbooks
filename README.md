# Finance & Consulting Analysis Tool

A comprehensive Python application demonstrating financial calculations and business consulting analysis. This project serves as a proof of work showcasing practical financial and business analysis capabilities in Python.

## Features

### Financial Calculations
- **Loan Payment Calculator**: Calculate monthly payments, total interest, and payment schedules
- **Compound Interest Calculator**: Analyze investment growth over time
- **Savings Goal Calculator**: Determine time needed to reach financial goals

### Business Consulting Analysis
- **ROI Analysis**: Calculate return on investment with annualized returns
- **Break-even Analysis**: Determine break-even points for business operations
- **Profit Margin Analysis**: Analyze business profitability
- **Payback Period Calculator**: Calculate investment recovery time
- **Financial Ratio Analysis**: Comprehensive business health metrics

### Data Visualization
- **Loan Amortization Charts**: Visual breakdown of principal vs interest payments
- **Investment Growth Charts**: Compound interest visualization over time
- **Break-even Analysis Charts**: Visual representation of profit/loss scenarios

## Installation

1. Clone the repository:
```bash
git clone https://github.com/brwnpanda/blabla.git
cd blabla
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Interactive Mode
Run the application in interactive mode:
```bash
python main.py
```

### Demo Mode
Run all demonstrations automatically:
```bash
python main.py --demo
```

## Project Structure

```
finance_consulting/
├── __init__.py              # Package initialization
├── financial_calculator.py # Financial calculation functions
├── business_analyzer.py    # Business analysis tools
└── visualizer.py           # Data visualization functions

main.py                     # Main application entry point
sample_data.py              # Sample data for testing
config.py                   # Configuration settings
requirements.txt            # Python dependencies
README.md                   # Project documentation
```

## Examples

### Financial Calculations

```python
from finance_consulting.financial_calculator import FinancialCalculator

# Calculate loan payment
loan_info = FinancialCalculator.calculate_loan_payment(250000, 0.045, 30)
print(f"Monthly payment: ${loan_info['monthly_payment']}")

# Calculate investment growth
investment = FinancialCalculator.calculate_compound_interest(10000, 0.07, 20)
print(f"Final amount: ${investment['final_amount']}")
```

### Business Analysis

```python
from finance_consulting.business_analyzer import BusinessAnalyzer

# Calculate ROI
roi = BusinessAnalyzer.calculate_roi(100000, 150000, 3)
print(f"ROI: {roi['roi_percentage']}%")

# Break-even analysis
breakeven = BusinessAnalyzer.calculate_break_even_point(50000, 20, 50)
print(f"Break-even units: {breakeven['break_even_units']}")
```

### Data Visualization

```python
from finance_consulting.visualizer import FinancialVisualizer

# Generate loan amortization chart
FinancialVisualizer.plot_loan_amortization(250000, 0.045, 30, "loan_chart.png")

# Generate investment growth chart
FinancialVisualizer.plot_investment_growth(10000, 0.07, 20, "investment_chart.png")
```

## Sample Outputs

The application generates various reports and visualizations:

### Financial Calculations Demo
```
LOAN PAYMENT CALCULATION
Scenario: $250,000 home loan at 4.5% for 30 years
Monthly Payment: $1,266.71
Total Payment: $456,017.35
Total Interest: $206,017.35
```

### Business Analysis Demo
```
BREAK-EVEN ANALYSIS
Scenario: Fixed costs $50,000, Variable cost $20/unit, Price $50/unit
Break Even Units: 1,666.67
Break Even Revenue: $83,333.33
Contribution Margin: $30.00
```

## Dependencies

- **Python 3.6+**
- **matplotlib**: For data visualization and chart generation
- **pandas**: For data manipulation and analysis
- **numpy**: For numerical calculations

## License

This project is open source and available under the MIT License.

## Contributing

This project demonstrates proof of work in financial and consulting analysis. Contributions are welcome to enhance the functionality and add new features.

## Contact

For questions or suggestions about this finance and consulting analysis tool, please open an issue on GitHub.