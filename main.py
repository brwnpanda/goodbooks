#!/usr/bin/env python3
"""
Finance and Consulting Application
A complete demonstration of financial calculations and business consulting tools.
"""

import os
import sys
from finance_consulting.financial_calculator import FinancialCalculator
from finance_consulting.business_analyzer import BusinessAnalyzer
from finance_consulting.visualizer import FinancialVisualizer


def print_header(title):
    """Print a formatted header."""
    print("\n" + "="*60)
    print(f" {title}")
    print("="*60)


def print_results(results, title="Results"):
    """Print formatted results."""
    print(f"\n{title}:")
    print("-" * 40)
    for key, value in results.items():
        if isinstance(value, (int, float)):
            if 'percentage' in key or 'rate' in key:
                print(f"{key.replace('_', ' ').title()}: {value}%")
            elif 'ratio' in key:
                print(f"{key.replace('_', ' ').title()}: {value}")
            else:
                print(f"{key.replace('_', ' ').title()}: ${value:,.2f}")
        else:
            print(f"{key.replace('_', ' ').title()}: {value}")


def demonstrate_financial_calculations():
    """Demonstrate financial calculation capabilities."""
    print_header("FINANCIAL CALCULATIONS DEMO")
    
    # Loan calculation example
    print("\n1. LOAN PAYMENT CALCULATION")
    print("Scenario: $250,000 home loan at 4.5% for 30 years")
    loan_results = FinancialCalculator.calculate_loan_payment(250000, 0.045, 30)
    print_results(loan_results)
    
    # Investment calculation example
    print("\n2. COMPOUND INTEREST CALCULATION")
    print("Scenario: $10,000 invested at 7% annually for 20 years")
    investment_results = FinancialCalculator.calculate_compound_interest(10000, 0.07, 20)
    print_results(investment_results)
    
    # Savings goal example
    print("\n3. SAVINGS GOAL CALCULATION")
    print("Scenario: Save $50,000 with $500 monthly at 3% annual interest")
    savings_results = FinancialCalculator.calculate_savings_goal(50000, 500, 0.03)
    print_results(savings_results)


def demonstrate_business_analysis():
    """Demonstrate business analysis capabilities."""
    print_header("BUSINESS CONSULTING ANALYSIS DEMO")
    
    # ROI calculation example
    print("\n1. RETURN ON INVESTMENT (ROI) ANALYSIS")
    print("Scenario: $100,000 investment returning $150,000 over 3 years")
    roi_results = BusinessAnalyzer.calculate_roi(100000, 150000, 3)
    print_results(roi_results)
    
    # Break-even analysis example
    print("\n2. BREAK-EVEN ANALYSIS")
    print("Scenario: Fixed costs $50,000, Variable cost $20/unit, Price $50/unit")
    breakeven_results = BusinessAnalyzer.calculate_break_even_point(50000, 20, 50)
    print_results(breakeven_results)
    
    # Profit margin analysis
    print("\n3. PROFIT MARGIN ANALYSIS")
    print("Scenario: Revenue $500,000, Total costs $350,000")
    profit_results = BusinessAnalyzer.calculate_profit_margin(500000, 350000)
    print_results(profit_results)
    
    # Payback period analysis
    print("\n4. PAYBACK PERIOD ANALYSIS")
    print("Scenario: $100,000 investment with annual cash flows")
    annual_cash_flows = [25000, 30000, 35000, 40000, 45000]
    print(f"Annual cash flows: {annual_cash_flows}")
    payback_results = BusinessAnalyzer.calculate_payback_period(100000, annual_cash_flows)
    print_results(payback_results)
    
    # Financial ratio analysis
    print("\n5. FINANCIAL RATIO ANALYSIS")
    print("Scenario: Company financial data analysis")
    ratio_results = BusinessAnalyzer.financial_ratio_analysis(
        revenue=1000000,
        total_assets=800000,
        current_assets=300000,
        current_liabilities=150000,
        net_income=120000
    )
    print_results(ratio_results)


def create_sample_reports():
    """Create sample visual reports."""
    print_header("GENERATING SAMPLE REPORTS")
    
    # Create reports directory
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
        print(f"Created {reports_dir} directory")
    
    try:
        # Generate loan amortization chart
        print("\n1. Generating Loan Amortization Chart...")
        loan_chart_path = os.path.join(reports_dir, "loan_amortization.png")
        result1 = FinancialVisualizer.plot_loan_amortization(250000, 0.045, 30, loan_chart_path)
        print(result1)
        
        # Generate investment growth chart
        print("\n2. Generating Investment Growth Chart...")
        investment_chart_path = os.path.join(reports_dir, "investment_growth.png")
        result2 = FinancialVisualizer.plot_investment_growth(10000, 0.07, 20, investment_chart_path)
        print(result2)
        
        # Generate break-even analysis chart
        print("\n3. Generating Break-Even Analysis Chart...")
        breakeven_chart_path = os.path.join(reports_dir, "breakeven_analysis.png")
        result3 = FinancialVisualizer.plot_break_even_analysis(50000, 20, 50, 2000, breakeven_chart_path)
        print(result3)
        
        print(f"\nAll reports saved in the '{reports_dir}' directory!")
        
    except ImportError as e:
        print(f"Note: Visualization requires matplotlib. Install with: pip install matplotlib")
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error generating charts: {e}")


def run_interactive_demo():
    """Run an interactive demo of the application."""
    print_header("FINANCE & CONSULTING PROJECT DEMONSTRATION")
    print("Welcome to the Finance and Consulting Analysis Tool!")
    print("This project demonstrates proof of work in financial calculations")
    print("and business consulting analysis using Python.")
    
    while True:
        print("\n" + "-"*50)
        print("MENU OPTIONS:")
        print("1. Financial Calculations Demo")
        print("2. Business Analysis Demo") 
        print("3. Generate Sample Reports")
        print("4. Run All Demos")
        print("5. Exit")
        print("-"*50)
        
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":
                demonstrate_financial_calculations()
            elif choice == "2":
                demonstrate_business_analysis()
            elif choice == "3":
                create_sample_reports()
            elif choice == "4":
                demonstrate_financial_calculations()
                demonstrate_business_analysis()
                create_sample_reports()
            elif choice == "5":
                print("\nThank you for using the Finance & Consulting Tool!")
                print("This demonstrates a complete proof of work in Python for")
                print("financial calculations and business consulting analysis.")
                break
            else:
                print("Invalid choice. Please enter 1-5.")
                
        except KeyboardInterrupt:
            print("\n\nExiting application...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


def main():
    """Main application entry point."""
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        # Run all demos automatically
        demonstrate_financial_calculations()
        demonstrate_business_analysis()
        create_sample_reports()
        print_header("DEMONSTRATION COMPLETE")
        print("This Finance & Consulting project demonstrates:")
        print("• Financial calculations (loans, investments, savings)")
        print("• Business analysis (ROI, break-even, profit margins)")
        print("• Data visualization and reporting")
        print("• Clean, modular Python code structure")
        print("• Practical proof of work in finance/consulting domain")
    else:
        # Run interactive demo
        run_interactive_demo()


if __name__ == "__main__":
    main()