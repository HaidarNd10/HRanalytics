# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#imports
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

#Image ploting
IMAGE_URL = "https://www.digitalvidya.com/wp-content/uploads/2019/05/HR-Analytics.jpg"
st.image(IMAGE_URL)

#Title set
st.title('Studying different parameters of employee activity')

#Header set
#st.header("Deadd", anchor=None)

#Reading csv file
df= pd.read_csv(r'C:\Users\Haidar\Desktop\AUB\MSBA\MSBA325\Assignments\Assignment#2\HRDataset_v14.csv')

#k!p@s$@_S(Ho7ielD
#Showing plots    

st.header("Scatter Plot")
x1=px.scatter(df, x='PositionID', y='Salary', color='PerfScoreID', 
        title='Variation of Salary and Performance Score across Position Rank')
st.plotly_chart(x1)

st.header("Animated Scatter Plot")
x2=px.scatter(df, x='PositionID', y='Salary',animation_frame='PositionID', animation_group='Salary', color='Sex', 
           hover_name='Salary', 
           log_x=True,
           size_max=55,
           range_x=[1,30],
           range_y=[30000,70000],
        title='Salary vs Position Rank for Males and Females')
st.plotly_chart(x2)
with st.expander("See explanation"):
    st.write("""
        The plot above shows the change of Salary distribution per each PositionID, i.e: employee rank in company
        defferentiating also between males and females, showing male representation in Red and females in Blue.
    """)

st.header("Box Plot")
x3=px.box(df, x="Sex", y="Salary", color="MaritalDesc", title='Salary vs Sex across different Maritial Status')
st.plotly_chart(x3)
#adding question
change= st.radio("Which out of the following is the employee with the highest Salary?",
                 ('Male Married', 'Female Married', 'Male Single', 'Male divorced', 'Female widowed'))
if change=='Female Married':
    st.write('Correct!')
else:
    st.write("Try again.")

st.header("Bar Chart")
x4=px.histogram(df, x='RecruitmentSource',color='RecruitmentSource', histfunc="count", 
             title='Number of employees recruited per each Source')
st.plotly_chart(x4)

st.header("Animated Bar Chart")
x5=px.histogram(df, x='RecruitmentSource',y='Salary',color='RecruitmentSource', animation_frame='EmpSatisfaction',
            animation_group='Salary', histfunc="avg", 
             title='Average Salary of employees vs Recriutment source and employee Satisfaction')
st.plotly_chart(x5)
with st.expander("See explanation"):
    st.write("""
        The chart above shows the change in average Slary per each recruitment souce with each EmpSatisfaction, i.e: 
            Employee Satisfaction, which ranges from 1-5 and 5 being the best.
    """)

st.header("3D line Plot")
x6=px.line_3d(df, x='PerfScoreID', y='EmpSatisfaction', z='Salary',color='RaceDesc', symbol='Sex',
        title='3D representation of Performance Score vs Salary and Satisfaction for employees of different sex and race')
st.plotly_chart(x6)
with st.expander("See explanation"):
    st.write("""
        The chart above is a 3D representation showing the variation in Slary, Employee Satisfaction and Performance score. 
            PerfScorewhich ranges from 1-4 and 4 being the best.
    """)

st.header("Area Plot")
x7=px.area(df,x='Salary', y='Absences',
       color='RaceDesc',
       title='Absences vs Salary of employees from different race')
st.plotly_chart(x7)

#Side Bar Edit
st.sidebar.title("Contents:")
st.sidebar.markdown("[Scatter Plot](#scatter-plot)")
st.sidebar.markdown("[Animated Scatter Plot](#animated-scatter-plot)")
st.sidebar.markdown("[Box Plot](#box-plot)")
st.sidebar.markdown("[Bar Chart](#bar-chart)")
st.sidebar.markdown("[Animated Bar Chart](#animated-bar-chart)")
st.sidebar.markdown("[3D line Plot](#3d-line-plot)")
st.sidebar.markdown("[Area Plot](#area-plot)")

#Display edit: colors & font
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="serif"



#st.markdown("body", unsafe_allow_html=False)


#st.write("Done by Haidar Noureddine")