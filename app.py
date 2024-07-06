import streamlit as st
import pickle
import pandas as pd
def predic(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10):
    '''
    -name:s1
     in:query
     type:number
     required:True
    -name:s4
     in:query
     type:number
     required:True
    -name:s5
     in:query
     type:number
     required:True
     DESCRIPTION:output varaibles
    '''
    if s2=='yes':
        s2=1
    else:
        s2=0
    if s3=='yes':
        s3=1
    else:
        s3=0
    if s6=='male':
        s6=1
    else :
        s6=0
    if s7=='yes':
        s7=1
    else:
        s7=0
    if s8=='never wroked':
        s8=1
    elif s8=='private':
        s8=2
    elif s8=='self employed':
        s8=3
    elif s8=='childern':
        s8=4
    else:
        s8=0
    if s9=='urban':
        s9=1
    else:
        s9=0
    if s10=='used to smoke':
        s10=1
    elif s10=='never smoked':
        s10=2
    elif s10=='smokes':
        s10=3
    else:
        s10=0
    out=cl.predict([[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]])
    return out
    
def stroke():
    html_temp="""
    <div style='background-color:grey;padding:13px'>
    <h1 style='color:black;text-align:center;'>Stroke predictor </h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    s1=st.text_input('Age')
    s2=st.selectbox('Do you have hypertension',['yes','no'])
    s3=st.selectbox('Do you have blood pressure',['yes','no'])
    s4=st.text_input('Glucose level')
    s5=st.text_input('BMI')
    s6=st.selectbox('Gender',['male','female'])
    s7=st.selectbox('married',['yes','no'])
    s8=st.selectbox('category',['never wroked','private','self employed','children','government job'])
    s9=st.selectbox('home location',['urban','rural'])
    s10=st.selectbox('smoking habit',['used smoke','never smoked','smokes'])
    result=" "
    if st.button('Predict'):
        result=predic(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10)
        
        if result==0:
            st.write(' # There is no chance of stroke in near future ')
        else:
            st.write(' # You might get  stroke consult Doctor Please......')
            st.write(' ')
            st.header('Symptoms')
            sy={'symptoms':['Trouble speaking and understanding what others are saying','Paralysis or numbness of the face, arm or leg','Problems seeing in one or both eyes','Headache','Trouble walking']}
            st.table(sy)
            st.title('Prevention')
            st.write(' ')
            pre={'prevention':['Controlling high blood pressure','Lowering the amount of cholesterol and saturated fat in your diet','Quitting tobacco use','Managing diabetes','Maintaining a healthy weight','Exercising regularly.','Avoiding Drugs']}
            st.table(pre)
            

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
            st.title('Symptoms')
            st.write(' ')
            data={'symptoms':['Increased thirst','Frequent urination','Extreme hunger','Unexplained weight loss',
                             'Fatigue','Blurred vision','Slow-healing sores','Frequent infections']}
            
            st.table(data)
            html_tem="""<div style='background-color:palegreen;padding:13px'>
            <h1 style='color:black;text-align:center;'>Diet</h1></div>"""
            st.markdown(html_tem,unsafe_allow_html=True)
            d={'Healthy carbohydrates':['Fruits','Vegetables','Whole grains','beans and peas','milk and cheese'],'Fiber rich foods':['Whole grains','nuts','fruits','vegetables','legumes'],'Foods to avoid':['Saturated fats','Trans fat','Cholesterol','Sodium','oils']}
            dat=pd.DataFrame.from_dict(d)
            st.table(dat)
            
    
    
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
            st.write(' ')
            st.title('Symptoms')
            swe={'Symptoms':['Pressure, tightness, pain, or a squeezing or aching sensation in your chest or arms that may spread to your neck, jaw or back','Nausea, indigestion, heartburn or abdominal pain','Shortness of breath','Cold sweat','Fatigue','Lightheadedness or sudden dizziness']}
            st.table(swe)
            st.write(' ')
            st.header('Risk Factors')
            ses={'Risk Factors':['High Blood Pressure','Tobacco','Age >45','High blood cholesterol','Obesity','Diabetes','Family history of heart attacks','Stress','drug use']}
            st.table(ses)
            
    
if __name__=='__main__':
    st.title('  Health care prediction using Machine Learning')
    st.text('\n')
    st.text('\n')
    #tex()
    #st.write('health care always been important to people , by machine learning and deep learning we have ease of access in health care.we truly belive prediction of diease at early stage and health care now at their hands we welcome our ml model predicto')
    check=st.sidebar.selectbox('what to predict',['Home','Diabetes','Heart','stroke'])
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
    elif check=='stroke':
        fi=open('stroke.pkl','rb')
        cl=pickle.load(fi)
        fi.close()
        stroke()
        #rep=st.sidebar.selectbox('home',['Home','about'])
    else:  
        #image=Image.open('h.png')
        #st.image(image)
        st.write('Machine Learning in health care revolutionized medicine. Machine learning brought health care at tips of hands to the people. Machine Learning and Deep Learning models helps docotors and radiologist to get the better understanding of diesae by gaining insights  and by predicting the diesases by taking symtops into consideration.')
        st.write("AI will effect Physicians and hosipitals,as it will play a key role in clinical decision support,enabling eariler indentification of diseases, and tailor treatment plans to optimal outcomes.")
        st.write('ML models are feeded with the appropriate data and trained to classify the result. ')
        st.write('Medical Imaging and  Diagnostics are used by pathologist, Raidologist to make quicker  and accurate  predictions')
       
        
#@st.cache()
