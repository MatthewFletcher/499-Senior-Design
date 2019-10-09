import pandas as pd
import matplotlib.pyplot as plt
import CSV_Wizard

# This function will graph the frequency or interval data as a normal x/y line graph.
def freqorint_xy(df):
    headers = list(df.columns.values)

    x = df[headers[1]]
    y = df[headers[2]]
    plt.xlabel(headers[1])
    plt.ylabel(headers[2])

    # Plot the points using matplotlib
    plt.plot(x, y)
    plt.show()

# This function will graph the frequency or interval data as a horizontal bar graph
def freqorint_hbar(df):
    headers = list(df.columns.values)
    headers.pop(0)
    x = headers
    y = []
    for header in headers:
        y.append(df[header].sum())

    plt.barh(x,y)
    plt.show()

# This function will graph frequency or interval data as a vertical bar graph
def freqorint_vbar(df):
    headers = list(df.columns.values)
    headers.pop(0)
    x = headers
    y = []
    for header in headers:
        y.append(df[header].sum())

    plt.bar(x,y)
    plt.show()

# This function will graph the frequency or interval data as a pie chart
def frequency_pie(df):
    headers = list(df.columns.values)
    # Remove the Question # column
    headers.pop(0)
    x = headers
    y = []
    explode = []
    for header in headers:
        y.append(df[header].sum())
        explode.append(0)

    # Data to plot
    colors = ['gold', 'yellowgreen']

    # Plot
    plt.pie(y, explode=explode, labels=x, colors=colors,
            autopct='%1.1f%%', shadow=False, startangle=0)
    plt.axis('equal')
    plt.show()

# This function will graph the ordinal data as a vertical bar graph
def ordinal_vbar(df):
    headers = list(df.columns.values)
    # Remove the Question # column
    headers.pop(0)
    x = headers
    y = []

    for header in headers:
        y.append(df[header].sum())

    plt.bar(x, y)
    plt.show()

# This function will graph the ordinal data as a horizontal bar graph
def ordinal_hbar(df):
    headers = list(df.columns.values)
    # Remove the Question # column
    headers.pop(0)
    x = headers
    y = []
    for header in headers:
        y.append(df[header].sum())

    plt.barh(x, y)
    plt.show()

# This function will graph ordinal data as a pie chart
def ordinal_pie(df):
    headers = list(df.columns.values)
    # Remove the Question # column
    headers.pop(0)
    x = headers
    y = []
    explode = []
    for header in headers:
        y.append(df[header].sum())
        explode.append(0)

    # Data to plot
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lavender']

    # Plot
    plt.pie(y, explode=explode, labels=x, colors=colors,
            autopct='%1.1f%%', shadow=False, startangle=0)
    plt.axis('equal')
    plt.show()

# Testing purposes
if __name__ == '__main__':
    myinfo = CSV_Wizard.openFile("../../TestData/IntervalDataTest.csv")
    #contains numpy array
    d = myinfo[0]
    frequency_pie(d)