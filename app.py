import streamlit as st
import pickle
from PIL import Image
def predicto(d1,d2,d3,d4,d5,d6,d7,d8):
    '''
    -name:d1
       in:query
       type:number
        required=True
      -name:d2
       in:query
       type:number
       required:True
      -name:d3
       in:query
       type:number
       required:True
      -name:d4
       in:query
       type:number
       required:True
      -name:d5
       in:query
       type:number
       required:True
      -name:hd6
       in:query
       type:number
       required:True
      -name:d7
       in:query
       type:number
       required:True
      -name:d8
       in:query
       type:number

    '''
    re=model.predict([[d1,d2,d3,d4,d5,d6,d7,d8]])
    return re
def diabetes():
    st.write('diabetes')
    html_temp="""
    <div style='background-color:yellow;padding:13px'>
    <h1 style='color:black;text-align:center;'>Diabetes predictor </h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    d1=st.text_input("Pregancies")
    d2=st.text_input('Glucose')
    d3=st.text_input('bloodpressure')
    d4=st.text_input('skinthickness')
    d5=st.text_input('Insulin')
    d6=st.text_input('bmi')
    d7=st.text_input('diabetes pedrige ratio (0 to 1)')
    d8=st.text_input('age')
    result=" "
    if st.button('Predict'):
        result=predicto(d1,d2,d3,d4,d5,d6,d7,d8)
        if result==0:
            st.write(' # You dont have diabetes ')
        else:
            st.write(' # You might have diabetes consult Doctor Please......')
    
    
def predict_attack(h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13):
    """

    Parameters:

      -name:h1
       in:query
       type:number
        required=True
      -name:h5
       in:query
       type:number
       required:True
      -name:h4
       in:query
       type:number
       required:True
      -name:h8
       in:query
       type:number
       required:True
      -name:h9
       in:query
       type:number
       required:True
      -name:h10
       in:query
       type:number
       required:True
      -name:h11
       in:query
       type:number
       required:True
      -name:h12
       in:query
       type:number
       required:True
        DESCRIPTION:output varaibles
    """
    if h2=='male':
        h2=0
    else:
        h2=1
    if h3=='angina':
        h3=0
    elif h3=='atypical anigna':
       h3=1
    elif h3=='non-anignal pain':
       h3=2
    else:
        h3=3
    if h6=='greater than 120':
        h6=1
    else:
        h6=0
    if h7=='normal':
        h7=0
    elif h7=='ST-t normal':
        h7=1
    else:
        h7=2
    if h13=='yes':
        h13=1
    else:
        h13=0
    
    res=classifier.predict([[h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13]])
    return res
def heart():
    st.write('heart')
    html_temp="""
    <div style='background-color:yellow;padding:13px'>
    <h1 style='color:black;text-align:center;'>Heart attack predictor </h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    h1=st.text_input('Age')
    h2=st.selectbox('sex',['male','female'])
    h3=st.selectbox('type of chest pain',['angina','atypical anigna','non-anignal pain','asymptomatic'])
    h4=st.text_input('blood pressure')
    h5=st.text_input('cholesterol')
    h6=st.selectbox('blood sugar',['greater than 120',' less than120'])
    h7=st.selectbox('ecg results',['normal','ST-t normal','left ventricular hypertrophy'])
    h8=st.text_input('max heart rate')
    h9=st.text_input('old peak value ranges(0 to 4.5)')
    h10=st.text_input('slope value (0,1,2)')
    h11=st.text_input('no.of vessels (0,1,2,3)')
    h12=st.text_input('stress result (0,1,2)')
    h13=st.selectbox('excerise induced anigna',['yes','no'])
    result=" "
    if st.button('Predict'):
        result=predict_attack(h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13)
        
        if result==0:
            st.write(' # There is no chance of heart attack in near future ')
        else:
            st.write(' # You might get heart attack consult Doctor Please......')
    st.write('praneeth kanchanakuntla') 
if __name__=='__main__':
    st.title('  Health care prediction using Machine Learning')
    st.text('\n')
    st.text('\n')
    #tex()
    #st.write('health care always been important to people , by machine learning and deep learning we have ease of access in health care.we truly belive prediction of diease at early stage and health care now at their hands we welcome our ml model predicto')
    check=st.sidebar.selectbox('what to predict',['Home','Diabetes','Heart'])
    if check=='Heart':
        file=open("Heart.pkl","rb")
        classifier=pickle.load(file)
        file.close()
        heart()
    elif check=='Diabetes':
        fil=open("random_forest_regression_model.pkl","rb")
        model=pickle.load(fil)
        fil.close()
        diabetes()
    else:
        #rep=st.sidebar.selectbox('home',['Home','about'])
       
        st.write('Machine Learning in health care revolutionized medicine. Machine learning brought health care at tips of hands to the people. Machine Learning and Deep Learning models helps docotors and radiologist to get the better understanding of diesae by gaining insights  and by predicting the diesases by taking symtops into consideration.')
        st.write("AI will effect Physicians and hosipitals,as it will play a key role in clinical decision support,enabling eariler indentification of diseases, and tailor treatment plans to optimal outcomes.")
        st.write('ML models are feeded with the appropriate data and trained to classify the result. ')
        st.write('Medical Imaging and  Diagnostics are used by pathologist, Raidologist to make quicker  and accurate  predictions')
   
       
        
#@st.cache()
