import pandas as pd
import matplotlib.pyplot as plt
url = 'https://content-media-cdn.codefinity.com/courses/47339f29-4722-4e72-a0d4-6112c70ff738/weather_data.csv'
weather_df = pd.read_csv(url, index_col=0)
plt.figure(figsize=(8, 6))
plt.plot(weather_df['Boston'])
plt.plot(weather_df['Seattle'])
# Set the title of the plot
plt.title('Boston and Seattle average yearly temperatures', fontsize=15, loc='right')
plt.show()
#Here’s what each line of your script does:

#import pandas as pd
#– Imports the pandas library under the alias pd for data manipulation.

#import matplotlib.pyplot as plt
#– Imports matplotlib’s plotting interface as plt.

#url = 'https://…/weather_data.csv'
#– Stores the CSV file’s web address in the variable url.

#weather_df = pd.read_csv(url, index_col=0)
#– Reads the CSV from url into a DataFrame named weather_df, using the first column as the row index.

#plt.figure(figsize=(8, 6))
#– Creates a new figure for plotting, sized 8×6 inches.

#plt.plot(weather_df['Boston'])
#– Plots the “Boston” column (average yearly temperatures) as a line on the current figure.

#plt.plot(weather_df['Seattle'])
#– Plots the “Seattle” column on the same axes, allowing comparison.

# Set the title of the plot
#– A comment noting that the next line customizes the plot title.

#plt.title('Boston and Seattle average yearly temperatures', fontsize=15, loc='right')
#– Sets the plot’s title text, increases its font size to 15, and aligns it to the right.

#plt.show()
#– Renders and displays the figure with both lines and the customized title.
###