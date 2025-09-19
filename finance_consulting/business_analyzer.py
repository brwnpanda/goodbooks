"""
Business Consulting Module
Provides business analysis tools for consulting projects.
"""


class BusinessAnalyzer:
    """A class to handle various business analysis calculations."""
    
    @staticmethod
    def calculate_roi(initial_investment, final_value, investment_period_years=None):
        """
        Calculate Return on Investment (ROI).
        
        Args:
            initial_investment (float): Initial investment amount
            final_value (float): Final value of investment
            investment_period_years (float, optional): Investment period in years
        
        Returns:
            dict: ROI percentage and annualized ROI if period provided
        """
        roi = ((final_value - initial_investment) / initial_investment) * 100
        
        result = {'roi_percentage': round(roi, 2)}
        
        if investment_period_years:
            annualized_roi = ((final_value / initial_investment) ** (1 / investment_period_years) - 1) * 100
            result['annualized_roi_percentage'] = round(annualized_roi, 2)
        
        return result
    
    @staticmethod
    def calculate_break_even_point(fixed_costs, variable_cost_per_unit, price_per_unit):
        """
        Calculate break-even point in units and revenue.
        
        Args:
            fixed_costs (float): Total fixed costs
            variable_cost_per_unit (float): Variable cost per unit
            price_per_unit (float): Selling price per unit
        
        Returns:
            dict: Break-even units and revenue
        """
        contribution_margin = price_per_unit - variable_cost_per_unit
        
        if contribution_margin <= 0:
            return {'error': 'Price per unit must be greater than variable cost per unit'}
        
        break_even_units = fixed_costs / contribution_margin
        break_even_revenue = break_even_units * price_per_unit
        
        return {
            'break_even_units': round(break_even_units, 2),
            'break_even_revenue': round(break_even_revenue, 2),
            'contribution_margin': round(contribution_margin, 2)
        }
    
    @staticmethod
    def calculate_profit_margin(revenue, total_costs):
        """
        Calculate profit margin.
        
        Args:
            revenue (float): Total revenue
            total_costs (float): Total costs
        
        Returns:
            dict: Profit, profit margin percentage, and profit ratio
        """
        profit = revenue - total_costs
        profit_margin = (profit / revenue) * 100 if revenue > 0 else 0
        
        return {
            'profit': round(profit, 2),
            'profit_margin_percentage': round(profit_margin, 2),
            'profit_ratio': round(profit / revenue, 4) if revenue > 0 else 0
        }
    
    @staticmethod
    def calculate_payback_period(initial_investment, annual_cash_flows):
        """
        Calculate payback period for an investment.
        
        Args:
            initial_investment (float): Initial investment amount
            annual_cash_flows (list): List of annual cash flows
        
        Returns:
            dict: Payback period in years and months
        """
        cumulative_cash_flow = 0
        payback_years = 0
        
        for year, cash_flow in enumerate(annual_cash_flows, 1):
            cumulative_cash_flow += cash_flow
            if cumulative_cash_flow >= initial_investment:
                # Calculate the exact payback period
                excess = cumulative_cash_flow - initial_investment
                fraction_of_year = 1 - (excess / cash_flow)
                payback_years = year - 1 + fraction_of_year
                break
        else:
            return {'error': 'Investment not recovered within the given cash flow period'}
        
        payback_months = payback_years * 12
        
        return {
            'payback_years': round(payback_years, 2),
            'payback_months': round(payback_months, 1)
        }
    
    @staticmethod
    def financial_ratio_analysis(revenue, total_assets, current_assets, current_liabilities, net_income):
        """
        Calculate key financial ratios for business analysis.
        
        Args:
            revenue (float): Total revenue
            total_assets (float): Total assets
            current_assets (float): Current assets
            current_liabilities (float): Current liabilities
            net_income (float): Net income
        
        Returns:
            dict: Various financial ratios
        """
        # Asset turnover ratio
        asset_turnover = revenue / total_assets if total_assets > 0 else 0
        
        # Current ratio
        current_ratio = current_assets / current_liabilities if current_liabilities > 0 else 0
        
        # Return on assets
        roa = (net_income / total_assets) * 100 if total_assets > 0 else 0
        
        # Net profit margin
        net_profit_margin = (net_income / revenue) * 100 if revenue > 0 else 0
        
        return {
            'asset_turnover_ratio': round(asset_turnover, 2),
            'current_ratio': round(current_ratio, 2),
            'return_on_assets_percentage': round(roa, 2),
            'net_profit_margin_percentage': round(net_profit_margin, 2)
        }