import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df.index = df['date']
df['date'] = pd.to_datetime(df['date'])


# Clean data
top_threshold = df['value'].quantile(.975)
bottom_threshold = df['value'].quantile(.025)

df = df[(df['value'] > bottom_threshold)  & (df['value'] < top_threshold)]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(10, 6))
    plt.plot(df['date'] , df['value'])
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')


    # Save image and return fig (don't change this part)
   
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

    # Extract the year and month from the date index
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Group by year and month, calculate the average page views
    avg_page_views = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot

    # Plot the bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    avg_page_views.plot(kind='bar', ax=ax)

    # Add labels and title
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.title('Average Daily Page Views by Month and Year')

    # Add legend
    plt.legend(title='Months')

    

    # Save image and return fig (don't change this part)
    
    return fig

# def draw_box_plot():
#     # Prepare data for box plots (this part is done!)
#     df_box = df.copy()
#     # df_box.reset_index(inplace=True)
#     df_box['year'] = [d.year for d in df_box.date]
#     df_box['month'] = [d.strftime('%b') for d in df_box.date]

#     # Draw box plots (using Seaborn)
#     fig, axes = plt.subplots(1, 2, figsize=(15, 6))
#     sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
#     sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
#     axes[0].set_xlabel('Year')
#     axes[0].set_ylabel('Page Views')
#     axes[0].set_title('Year-wise Box Plot (Trend)')
#     axes[1].set_xlabel('Month')
#     axes[1].set_ylabel('Page Views')
#     axes[1].set_title('Month-wise Box Plot (Seasonality)')
    




#     # Save image and return fig (don't change this part)
    
#     return fig

line_plot_fig = draw_line_plot()
bar_plot_fig = draw_bar_plot()


line_plot_fig.savefig('line_plot.png')
bar_plot_fig.savefig('bar_plot.png')

