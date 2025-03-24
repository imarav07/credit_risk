import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import seaborn as sns
from scipy.stats import chi2_contingency

def stacked_bar_chart(data_: pd.DataFrame, groupby_cols : list) -> Axes:
    # Group by age group and risk, then normalize
    stacked_distribution = data_.groupby(groupby_cols).size().unstack().apply(lambda x: x / x.sum(), axis=1)
    
    # Define colors for the bars
    colors = {'bad': 'red', 'good': 'green'}
    
    # Plot the data with specified colors
    ax = stacked_distribution.plot(kind='bar', stacked=True, color=[colors.get(x, '#333333') for x in stacked_distribution.columns])
    
    # Add percentage labels
    for p in ax.patches:
        width = p.get_width()
        height = p.get_height()
        x, y = p.get_xy() 
        ax.annotate(f'{height:.1%}', (x + width / 2, y + height / 2), ha='center', va='center')
    
    return ax

def bar_chart(data_: pd.DataFrame, groupby_cols : list) -> Axes:
    # Group by age group and risk, then normalize
    stacked_distribution = data_.groupby(groupby_cols).size().unstack()
    
    # Define colors for the bars
    colors = {'bad': 'red', 'good': 'green'}
    
    # Plot the data with specified colors
    ax = stacked_distribution.plot(kind='bar', stacked=True, color=[colors.get(x, '#333333') for x in stacked_distribution.columns])
    
    # Add labels
    for p in ax.patches:
        width = p.get_width()
        height = p.get_height()
        x, y = p.get_xy() 
        absolute = int(height)
        ax.annotate(f'({absolute})', (x + width / 2, y + height / 2), ha='center', va='center')
    
    return ax

def custom_box_plot(data_: pd.DataFrame, x_col: str, y_col: str, hue_col: str = None) -> None:
    # Create a box plot
    colors = {'bad': 'red', 'good': 'green'}
    plt.figure(figsize=(10, 6))
    sns.boxplot(x= x_col, y = y_col, hue=hue_col, data=data_, palette=colors)
    plt.title(f'Box Plot of {y_col} by {x_col}')
    plt.xlabel(f'{x_col}')
    plt.ylabel(f'{y_col}')
    plt.show()

def custom_scatter_plot(data_: pd.DataFrame, x_col: str, y_col: str, hue_col: str = None) -> None:
    # Create a scatter plot
    colors = {'bad': 'red', 'good': 'green'}
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x= x_col, y = y_col, hue=hue_col, data=data_, palette=colors)
    plt.title(f'Scatter Plot of {y_col} by {x_col}')
    plt.xlabel(f'{x_col}')
    plt.ylabel(f'{y_col}')
    if hue_col != None:
        plt.legend(title=hue_col)
    plt.show()

def custom_chi_square_test(data_: pd.DataFrame, x_col: str, y_col: str) -> None:
    # Create a contingency table
    contingency_table = pd.crosstab(data_[x_col], data_[y_col])
    
    # Perform the chi-square test
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    
    print('contingency_table:')
    print(contingency_table)
    # Print the results
    print(f'Chi-Square Statistic: {chi2}')
    print(f'p-value: {p}')
    print(f'Degrees of Freedom: {dof}')
    print('Expected Frequencies: ')
    print(expected)

    # Step 4: Interpretation
    if p < 0.05:
        print("Reject Null Hypothesis → Both Groups are dependent.")
    else:
        print("Fail to Reject Null Hypothesis → Both Groups are independent.")