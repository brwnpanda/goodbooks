"""
Financial Calculator Module
Provides basic financial calculations for loans, investments, and savings.
"""

import math


class FinancialCalculator:
    """A class to handle various financial calculations."""
    
    @staticmethod
    def calculate_loan_payment(principal, annual_rate, years):
        """
        Calculate monthly loan payment using the formula:
        M = P * [r(1+r)^n] / [(1+r)^n - 1]
        
        Args:
            principal (float): Loan amount
            annual_rate (float): Annual interest rate (as decimal, e.g., 0.05 for 5%)
            years (int): Loan term in years
        
        Returns:
            dict: Monthly payment, total payment, and total interest
        """
        monthly_rate = annual_rate / 12
        num_payments = years * 12
        
        if monthly_rate == 0:
            monthly_payment = principal / num_payments
        else:
            monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / \
                            ((1 + monthly_rate) ** num_payments - 1)
        
        total_payment = monthly_payment * num_payments
        total_interest = total_payment - principal
        
        return {
            'monthly_payment': round(monthly_payment, 2),
            'total_payment': round(total_payment, 2),
            'total_interest': round(total_interest, 2)
        }
    
    @staticmethod
    def calculate_compound_interest(principal, annual_rate, years, compounds_per_year=12):
        """
        Calculate compound interest using the formula:
        A = P(1 + r/n)^(nt)
        
        Args:
            principal (float): Initial investment
            annual_rate (float): Annual interest rate (as decimal)
            years (int): Investment period in years
            compounds_per_year (int): Number of times interest compounds per year
        
        Returns:
            dict: Final amount, interest earned, and growth percentage
        """
        final_amount = principal * (1 + annual_rate / compounds_per_year) ** (compounds_per_year * years)
        interest_earned = final_amount - principal
        growth_percentage = (interest_earned / principal) * 100
        
        return {
            'final_amount': round(final_amount, 2),
            'interest_earned': round(interest_earned, 2),
            'growth_percentage': round(growth_percentage, 2)
        }
    
    @staticmethod
    def calculate_savings_goal(target_amount, monthly_contribution, annual_rate):
        """
        Calculate how long it takes to reach a savings goal.
        
        Args:
            target_amount (float): Target savings amount
            monthly_contribution (float): Monthly savings contribution
            annual_rate (float): Annual interest rate (as decimal)
        
        Returns:
            dict: Time to reach goal in months and years
        """
        monthly_rate = annual_rate / 12
        
        if monthly_rate == 0:
            months = target_amount / monthly_contribution
        else:
            months = math.log(1 + (target_amount * monthly_rate) / monthly_contribution) / math.log(1 + monthly_rate)
        
        years = months / 12
        
        return {
            'months_to_goal': round(months, 1),
            'years_to_goal': round(years, 1)
        }