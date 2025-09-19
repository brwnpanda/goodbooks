"""
Data Visualization Module
Provides visualization tools for financial and business data.
"""

import matplotlib.pyplot as plt
import numpy as np


class FinancialVisualizer:
    """A class to create financial and business visualizations."""
    
    @staticmethod
    def plot_loan_amortization(principal, annual_rate, years, save_path=None):
        """
        Create a loan amortization chart showing principal vs interest over time.
        
        Args:
            principal (float): Loan amount
            annual_rate (float): Annual interest rate (as decimal)
            years (int): Loan term in years
            save_path (str, optional): Path to save the chart
        
        Returns:
            str: Success message or path where chart was saved
        """
        monthly_rate = annual_rate / 12
        num_payments = years * 12
        
        if monthly_rate == 0:
            monthly_payment = principal / num_payments
        else:
            monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / \
                            ((1 + monthly_rate) ** num_payments - 1)
        
        remaining_balance = principal
        principal_payments = []
        interest_payments = []
        months = []
        
        for month in range(1, num_payments + 1):
            interest_payment = remaining_balance * monthly_rate
            principal_payment = monthly_payment - interest_payment
            remaining_balance -= principal_payment
            
            principal_payments.append(principal_payment)
            interest_payments.append(interest_payment)
            months.append(month)
        
        plt.figure(figsize=(12, 8))
        plt.stackplot(months, principal_payments, interest_payments, 
                     labels=['Principal Payment', 'Interest Payment'],
                     alpha=0.7)
        plt.xlabel('Month')
        plt.ylabel('Payment Amount ($)')
        plt.title(f'Loan Amortization Schedule\n${principal:,.2f} at {annual_rate*100:.1f}% for {years} years')
        plt.legend(loc='upper right')
        plt.grid(True, alpha=0.3)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
            return f"Chart saved to {save_path}"
        else:
            plt.show()
            return "Chart displayed successfully"
    
    @staticmethod
    def plot_investment_growth(principal, annual_rate, years, save_path=None):
        """
        Create an investment growth chart showing compound interest over time.
        
        Args:
            principal (float): Initial investment
            annual_rate (float): Annual interest rate (as decimal)
            years (int): Investment period in years
            save_path (str, optional): Path to save the chart
        
        Returns:
            str: Success message or path where chart was saved
        """
        months = np.arange(0, years * 12 + 1)
        values = principal * (1 + annual_rate / 12) ** months
        
        plt.figure(figsize=(10, 6))
        plt.plot(months / 12, values, linewidth=2, color='green')
        plt.fill_between(months / 12, principal, values, alpha=0.3, color='lightgreen')
        plt.axhline(y=principal, color='red', linestyle='--', alpha=0.7, label='Initial Investment')
        
        plt.xlabel('Years')
        plt.ylabel('Investment Value ($)')
        plt.title(f'Investment Growth Over Time\n${principal:,.2f} at {annual_rate*100:.1f}% annual rate')
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        # Add annotations
        final_value = values[-1]
        plt.annotate(f'Final Value: ${final_value:,.2f}', 
                    xy=(years, final_value), xytext=(years*0.7, final_value*1.1),
                    arrowprops=dict(arrowstyle='->', color='black'),
                    fontsize=10, ha='center')
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
            return f"Chart saved to {save_path}"
        else:
            plt.show()
            return "Chart displayed successfully"
    
    @staticmethod
    def plot_break_even_analysis(fixed_costs, variable_cost_per_unit, price_per_unit, max_units=1000, save_path=None):
        """
        Create a break-even analysis chart.
        
        Args:
            fixed_costs (float): Total fixed costs
            variable_cost_per_unit (float): Variable cost per unit
            price_per_unit (float): Selling price per unit
            max_units (int): Maximum units to show on chart
            save_path (str, optional): Path to save the chart
        
        Returns:
            str: Success message or path where chart was saved
        """
        units = np.arange(0, max_units + 1, 10)
        total_costs = fixed_costs + (variable_cost_per_unit * units)
        total_revenue = price_per_unit * units
        
        # Calculate break-even point
        contribution_margin = price_per_unit - variable_cost_per_unit
        break_even_units = fixed_costs / contribution_margin
        break_even_revenue = break_even_units * price_per_unit
        
        plt.figure(figsize=(10, 6))
        plt.plot(units, total_costs, label='Total Costs', linewidth=2, color='red')
        plt.plot(units, total_revenue, label='Total Revenue', linewidth=2, color='blue')
        plt.axvline(x=break_even_units, color='green', linestyle='--', alpha=0.7, label='Break-Even Point')
        
        # Fill profit and loss areas
        plt.fill_between(units, total_costs, total_revenue, 
                        where=(total_revenue >= total_costs), 
                        alpha=0.3, color='green', label='Profit Area')
        plt.fill_between(units, total_costs, total_revenue, 
                        where=(total_revenue < total_costs), 
                        alpha=0.3, color='red', label='Loss Area')
        
        plt.xlabel('Units Sold')
        plt.ylabel('Amount ($)')
        plt.title('Break-Even Analysis')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Add break-even annotation
        plt.annotate(f'Break-Even: {break_even_units:.0f} units\n${break_even_revenue:,.2f}', 
                    xy=(break_even_units, break_even_revenue), 
                    xytext=(break_even_units + max_units*0.2, break_even_revenue),
                    arrowprops=dict(arrowstyle='->', color='black'),
                    fontsize=10, ha='left')
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
            return f"Chart saved to {save_path}"
        else:
            plt.show()
            return "Chart displayed successfully"