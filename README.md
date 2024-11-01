# WhatsApp Chat Analyzer
## For 24 hour phone format only

The **WhatsApp Chat Analyzer** is a Streamlit application designed to analyze WhatsApp chat data. It provides insights into chat statistics, user activity, word frequency, and more, allowing users to gain valuable information from their chat history.

## Features

- **Upload Chat Data**: Users can upload their exported WhatsApp chat files for analysis.
- **User-Specific Analysis**: Select specific users or view overall statistics.
- **Key Statistics**: Displays total messages, words, media shared, links shared, and the most and least active users.
- **Visualizations**:
  - Most busy users bar chart.
  - Word cloud of frequently used words.
  - Bar charts for the most common words.
  - Activity maps for the busiest days and months.
  - Timelines showing daily and monthly message trends.


## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
```

### 2. Install required libraries

Install the necessary packages listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
streamlit run app.py
```

## File Structure

- `app.py`: Main file containing the Streamlit app code.
- `preprocessor.py`: Module for preprocessing chat data.
- `helper.py`: Module containing helper functions for analysis and visualization.
- `requirements.txt`: Lists all required Python libraries for the project.

## Project Details

The application processes exported WhatsApp chat data and provides various analyses:

- **Preprocessing**: The `preprocessor.py` module handles data cleaning and formatting.
- **Statistics Calculation**: The `helper.py` module calculates statistics such as message count, media shared, and links shared.
- **Visualizations**: Various plots are generated using Matplotlib to visualize user activity, word usage, and timelines.

## Usage

1. **Upload Chat Data**: Use the sidebar to upload your exported WhatsApp chat file.
2. **Select User**: Choose a specific user or "Overall" for collective statistics.
3. **View Analysis**: Click the "Show Analysis" button to display the statistics and visualizations.

## Example

After uploading a chat file and selecting a user, the application will show insights such as the total number of messages sent by the user, the most active days, and a word cloud representing frequently used words.

![Screenshot 2024-11-01 215134](https://github.com/user-attachments/assets/6887683b-940b-48a7-9d4b-3a10a04c1bcc)

![Screenshot 2024-11-01 215200](https://github.com/user-attachments/assets/af568865-daff-4f78-87ca-115ace5a70e1)

![Screenshot 2024-11-01 215250](https://github.com/user-attachments/assets/2cf06467-d9fc-4d48-b2bb-7557d8fc3f2e)


## IT WORKS FOR BOTH GROUP LEVEL and INDIVIDUAL LEVEL CHATS



## Future Improvements

- **Enhanced Visualizations**: Incorporate more advanced visualization techniques for better insights.
- **Sentiment Analysis**: Add features to analyze the sentiment of the messages.
- **Export Data**: Allow users to download the analysis report as a PDF or CSV.

