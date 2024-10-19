import streamlit as st
import preprocessor ,helper
import matplotlib.pyplot as plt

st.sidebar.title('WhatsApp Chat Analyzer')

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
   
    bytes_data = uploaded_file.getvalue()
    data=bytes_data.decode('utf-8')
    
    df=preprocessor.preprocess(data)

    

    #fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")




    selected_user = st.sidebar.selectbox("Show analysis wrt",user_list)

    if st.sidebar.button("Show Analysis"):

        # Stats Area
        num_messages, words, num_media_messages,links,max_msg,min_msg = helper.fetch_stats(selected_user,df)
        st.title("Top Statistics")
        col1, col2, col3, col4 ,col5,col6= st.columns(6)

        with col1:
            st.subheader("Total Messages")
            st.text(num_messages)
        with col2:
            st.subheader("Total Words")
            st.text(words)
        with col3:
            st.subheader("Media Shared")
            st.text(num_media_messages)
        with col4:
            st.subheader("Links Shared")
            st.text(links)
        
        with col5:
            st.subheader('Max msg by')
            st.text(max_msg)

        with col6:
            st.subheader('Min msg by')
            st.text(min_msg)



        
        

        #ACTIVE USERS CHART
        if selected_user == 'Overall':
            st.title('Most Busy Users')
            x,new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values,color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)
        
        #WORDCLOUD
        st.title("WordCloud")
        df_wc=helper.create_wordcloud(selected_user,df)
        fig,ax=plt.subplots()

        ax.imshow(df_wc)
        st.pyplot(fig)

        #MOST COMMON WORDS
        most_common_df = helper.most_common_words(selected_user,df)

        fig,ax = plt.subplots()

        ax.barh(most_common_df[0],most_common_df[1])
        plt.xticks(rotation='vertical')

        st.title('Most commmon words')
        st.pyplot(fig)
# activity map
        st.title('Activity Map')
        col1,col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values,color='purple')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values,color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)



        # monthly timeline
        st.title(" Timelines")
        col1,col2 = st.columns(2)
        with col1:
            timeline = helper.monthly_timeline(selected_user,df)
            fig,ax = plt.subplots()
            ax.plot(timeline['time'], timeline['message'],color='green')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # daily timeline
        with col2:
            st.title("Daily Timeline")
            daily_timeline = helper.daily_timeline(selected_user, df)
            fig, ax = plt.subplots()
            ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
