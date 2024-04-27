import streamlit as st
import pickle
from PIL import Image

def main():
    st.title(":rainbow[LIFE EXPECTANCY PREDICTION]")
    image=Image.open('life_expectancy.jpg')
    st.image(image,width=850)
    Country=st.selectbox("Country",('Afghanistan', 'Albania', 'Algeria', 'Angola','Antigua and Barbuda',
       'Argentina', 'Armenia', 'Australia','Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
       'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan','Bolivia (Plurinational State of)', 'Bosnia and Herzegovina',
       'Botswana', 'Brazil', 'Brunei Darussalam', 'Bulgaria','Burkina Faso', 'Burundi', "Côte d'Ivoire", 'Cabo Verde',
       'Cambodia', 'Cameroon', 'Canada', 'Central African Republic','Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo',
       'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czechia',"Democratic People's Republic of Korea",
       'Democratic Republic of the Congo', 'Denmark', 'Djibouti','Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador',
       'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji','Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany',
       'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea','Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary',
       'Iceland', 'India', 'Indonesia', 'Iran (Islamic Republic of)','Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan',
       'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan',"Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho',
       'Liberia', 'Libya', 'Lithuania', 'Luxembourg', 'Madagascar','Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Mauritania',
       'Mauritius', 'Mexico', 'Micronesia (Federated States of)','Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar',
       'Namibia', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua','Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Panama',
       'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland','Portugal', 'Qatar', 'Republic of Korea', 'Republic of Moldova',
       'Romania', 'Russian Federation', 'Rwanda', 'Saint Lucia','Saint Vincent and the Grenadines', 'Samoa',
       'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia','Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
       'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan','Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden',
       'Switzerland', 'Syrian Arab Republic', 'Tajikistan', 'Thailand','The former Yugoslav republic of Macedonia', 'Timor-Leste', 'Togo',
       'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey','Turkmenistan', 'Uganda', 'Ukraine', 'United Arab Emirates',
       'United Kingdom of Great Britain and Northern Ireland','United Republic of Tanzania', 'United States of America',
       'Uruguay', 'Uzbekistan', 'Vanuatu','Venezuela (Bolivarian Republic of)', 'Viet Nam', 'Yemen','Zambia', 'Zimbabwe'))
    # org_ct=['Afghanistan', 'Albania', 'Algeria', 'Angola','Antigua and Barbuda',
    #    'Argentina', 'Armenia', 'Australia','Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
    #    'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan','Bolivia (Plurinational State of)', 'Bosnia and Herzegovina',
    #    'Botswana', 'Brazil', 'Brunei Darussalam', 'Bulgaria','Burkina Faso', 'Burundi', "Côte d'Ivoire", 'Cabo Verde',
    #    'Cambodia', 'Cameroon', 'Canada', 'Central African Republic','Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo',
    #    'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czechia',"Democratic People's Republic of Korea",
    #    'Democratic Republic of the Congo', 'Denmark', 'Djibouti','Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador',
    #    'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji','Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany',
    #    'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea','Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary',
    #    'Iceland', 'India', 'Indonesia', 'Iran (Islamic Republic of)','Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan',
    #    'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan',"Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho',
    #    'Liberia', 'Libya', 'Lithuania', 'Luxembourg', 'Madagascar','Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Mauritania',
    #    'Mauritius', 'Mexico', 'Micronesia (Federated States of)','Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar',
    #    'Namibia', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua','Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Panama',
    #    'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland','Portugal', 'Qatar', 'Republic of Korea', 'Republic of Moldova',
    #    'Romania', 'Russian Federation', 'Rwanda', 'Saint Lucia','Saint Vincent and the Grenadines', 'Samoa',
    #    'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia','Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
    #    'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan','Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden',
    #    'Switzerland', 'Syrian Arab Republic', 'Tajikistan', 'Thailand','The former Yugoslav republic of Macedonia', 'Timor-Leste', 'Togo',
    #    'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey','Turkmenistan', 'Uganda', 'Ukraine', 'United Arab Emirates',
    #    'United Kingdom of Great Britain and Northern Ireland','United Republic of Tanzania', 'United States of America',
    #    'Uruguay', 'Uzbekistan', 'Vanuatu','Venezuela (Bolivarian Republic of)', 'Viet Nam', 'Yemen','Zambia', 'Zimbabwe']
    # ct=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,
    #     46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,
    #     89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,
    #     124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,
    #     156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182]
    # for i in range(len(ct)):
    #     if Country==ct[i]:
    #         Country==org_ct[i]
    if Country=="Afghanistan":
        ct=0
    elif Country=="Albania":
        ct=1
    elif Country == "Algeria":
        ct = 2
    elif Country=="Angola":
        ct=3
    elif Country=="Antigua and Barbuda":
        ct=4
    elif Country=="Argentina":
        ct=5
    elif Country=="Armenia":
        ct=6
    elif Country=="Australia":
        ct=7
    elif Country=="Austria":
        ct=8
    elif Country=="Azerbaijan":
        ct=9
    elif Country=="Bahamas":
        ct=10
    elif Country=="Bahrain":
        ct=11
    elif Country=="Bangladesh":
        ct=12
    elif Country=="Barbados":
        ct=13
    elif Country=="Belarus":
        ct=14
    elif Country=="Belgium":
        ct=15
    elif Country=="Belize":
        ct=16
    elif Country=="Benin":
        ct=17
    elif Country=="Bhutan":
        ct=18
    elif Country=="Bolivia (Plurinational State of)":
        ct=19
    elif Country=="Bosnia and Herzegovina":
        ct=20
    elif Country=="Botswana":
        ct=21
    elif Country=="Brazil":
        ct=22
    elif Country=="Brunei Darussalam":
        ct=23
    elif Country=="Bulgaria":
        ct=24
    elif Country=="Burkina Faso":
        ct=25
    elif Country=="Burundi":
        ct=26
    elif Country=="Côte d'Ivoire":
        ct=27
    elif Country=="Cabo Verde":
        ct=28
    elif Country=="Cambodia":
        ct=29
    elif Country=="Cameroon":
        ct=30
    elif Country=="Canada":
        ct=31
    elif Country=="Central African Republic":
        ct=32
    elif Country=="Chad":
        ct=33
    elif Country=="Chile":
        ct=34
    elif Country=="China":
        ct=35
    elif Country=="Colombia":
        ct=36
    elif Country=="Comoros":
        ct=37
    elif Country=="Congo":
        ct=38
    elif Country=="Costa Rica":
        ct=39
    elif Country=="Croatia":
        ct=40
    elif Country=="Cuba":
        ct=41
    elif Country=="Cyprus":
        ct=42
    elif Country=="Czechia":
        ct=43
    elif Country=="Democratic People's Republic of Korea":
        ct=44
    elif Country=="Democratic Republic of the Congo":
        ct=45
    elif Country=="Denmark":
        ct=46
    elif Country=="Djibouti":
        ct=47
    elif Country=="Dominican Republic":
        ct=48
    elif Country=="Ecuador":
        ct=49
    elif Country=="Egypt":
        ct=50
    elif Country=="El Salvador":
        ct=51
    elif Country=="Equatorial Guinea":
        ct=52
    elif Country=="Burundi":
        ct=53
    elif Country=="Estonia":
        ct=54
    elif Country=="Ethiopia":
        ct=55
    elif Country=="Fiji":
        ct=56
    elif Country=="Finland":
        ct=57
    elif Country=="France":
        ct=58
    elif Country=="Gabon":
        ct=59
    elif Country=="Gambia":
        ct=60
    elif Country=="Georgia":
        ct=61
    elif Country=="Germany":
        ct=62
    elif Country=="Ghana":
        ct=63
    elif Country=="Greece":
        ct=64
    elif Country=="Grenada":
        ct=65
    elif Country=="Guatemala":
        ct=66
    elif Country=="Guinea":
        ct=67
    elif Country=="Guinea-Bissau":
        ct=68
    elif Country=="Guyana":
        ct=69
    elif Country=="Haiti":
        ct=70
    elif Country == "Honduras":
        ct=71
    elif Country == "Hungary":
        ct=72
    elif Country == "Iceland":
        ct = 73
    elif Country == "India":
        ct = 74
    elif Country == "Indonesia":
        ct = 75
    elif Country == "Iran (Islamic Republic of)":
        ct = 76
    elif Country == "Iraq":
        ct = 77
    elif Country == "Ireland":
        ct = 78
    elif Country=="Israel":
        ct=79
    elif Country=="Italy":
        ct=80
    elif Country=="Jamaica":
        ct=81
    elif Country=="Japan":
        ct=82
    elif Country=="Jordan":
        ct=83
    elif Country=="Kazakhstan":
        ct=84
    elif Country=="Kenya":
        ct=85
    elif Country=="Kiribati":
        ct=86
    elif Country=="Kuwait":
        ct=87
    elif Country=="Kyrgyzstan":
        ct=88
    elif Country=="Lao People's Democratic Republic":
        ct=89
    elif Country=="Latvia":
        ct=90
    elif Country=="Lebanon":
        ct=91
    elif Country=="Lesotho":
        ct=92
    elif Country=="Liberia":
        ct=93
    elif Country=="Libya":
        ct=94
    elif Country=="Lithuania":
        ct=95
    elif Country=="Luxembourg":
        ct=96
    elif Country=="Madagascar":
        ct=97
    elif Country=="Malawi":
        ct=98
    elif Country=="Malaysia":
        ct=99
    elif Country=="Maldives":
        ct=100
    elif Country=="Mali":
        ct=101
    elif Country=="Malta":
        ct=102
    elif Country=="Mauritania":
        ct=103
    elif Country=="Mauritius":
        ct=104
    elif Country=="Mexico":
        ct=105
    elif Country=="Micronesia (Federated States of)":
        ct=106
    elif Country=="Mongolia":
        ct=107
    elif Country=="Montenegro":
        ct=108
    elif Country=="Morocco":
        ct=109
    elif Country=="Mozambique":
        ct=110
    elif Country=="Myanmar":
        ct=111
    elif Country=="Namibia":
        ct=112
    elif Country=="Nepal":
        ct=113
    elif Country=="Netherlands":
        ct=114
    elif Country=="New Zealand":
        ct=115
    elif Country=="Nicaragua":
        ct=116
    elif Country=="Niger":
        ct=117
    elif Country=="Nigeria":
        ct=118
    elif Country=="Norway":
        ct=119
    elif Country=="Oman":
        ct=120
    elif Country=="Pakistan":
        ct=121
    elif Country=="Panama":
        ct=122
    elif Country=="Papua New Guinea":
        ct=123
    elif Country=="Paraguay":
        ct=124
    elif Country=="Peru":
        ct=125
    elif Country=="Philippines":
        ct=126
    elif Country=="Poland":
        ct=127
    elif Country=="Portugal":
        ct=128
    elif Country=="Qatar":
        ct=129
    elif Country=="Republic of Korea":
        ct=130
    elif Country=="Republic of Moldova":
        ct=131
    elif Country=="Romania":
        ct=132
    elif Country=="Russian Federation":
        ct=133
    elif Country=="Rwanda":
        ct=134
    elif Country=="Saint Lucia":
        ct=135
    elif Country=="Saint Vincent and the Grenadines":
        ct=136
    elif Country=="Samoa":
        ct=137
    elif Country=="Sao Tome and Principe":
        ct=138
    elif Country=="Saudi Arabia":
        ct=139
    elif Country=="Senegal":
        ct=140
    elif Country=="Serbia":
        ct=141
    elif Country=="Seychelles":
        ct=142
    elif Country=="Sierra Leone":
        ct=143
    elif Country=="Singapore":
        ct=144
    elif Country=="Slovakia":
        ct=145
    elif Country=="Slovenia":
        ct=146
    elif Country=="Solomon Islands":
        ct=147
    elif Country=="Somalia":
        ct=148
    elif Country=="South Africa":
        ct=149
    elif Country=="South Sudan":
        ct=150
    elif Country=="Spain":
        ct=151
    elif Country=="Sri Lanka":
        ct=152
    elif Country=="Sudan":
        ct=153
    elif Country=="Suriname":
        ct=154
    elif Country=="Swaziland":
        ct=155
    elif Country=="Sweden":
        ct=156
    elif Country=="Switzerland":
        ct=157
    elif Country=="Syrian Arab Republic":
        ct=158
    elif Country=="Tajikistan":
        ct=159
    elif Country=="Thailand":
        ct=160
    elif Country=="The former Yugoslav republic of Macedonia":
        ct=161
    elif Country=="Timor-Leste":
        ct=162
    elif Country=="Togo":
        ct=163
    elif Country=="Tonga":
        ct=164
    elif Country=="Trinidad and Tobago":
        ct=165
    elif Country=="Tunisia":
        ct=166
    elif Country=="Turkey":
        ct=167
    elif Country=="Turkmenistan":
        ct=168
    elif Country=="Uganda":
        ct=169
    elif Country=="Ukraine":
        ct=170
    elif Country=="United Arab Emirates":
        ct=171
    elif Country=="United Kingdom of Great Britain and Northern Ireland":
        ct=172
    elif Country=="United Republic of Tanzania":
        ct=173
    elif Country=="United States of America":
        ct=174
    elif Country=="Uruguay":
        ct=175
    elif Country=="Uzbekistan":
        ct=176
    elif Country=="Vanuatu":
        ct=177
    elif Country=="Venezuela (Bolivarian Republic of)":
        ct=178
    elif Country=="Viet Nam":
        ct=179
    elif Country=="Yemen":
        ct=180
    elif Country=="Zambia":
        ct=181
    else:
        ct=182
    year=st.text_input("Year", "Type here")
    Status=st.selectbox("Country Status",("Developed","Developing"),placeholder="Select any option",)
    if Status=="Developed":
        sts=0
    else:
        sts=1
    Population=st.text_input("Population rate", "Type here")
    HepatitisB=st.text_input("Hepatitis B rate", "Type here")
    Measles=st.text_input("Measles rate", "Type here")
    Polio=st.text_input("Polio rate","Type here")
    Diphtheria=st.text_input("Diphtheria rate", "Type here")
    HIV=st.text_input("HIV/AIDS rate", "Type here")
    infant_deaths=st.text_input("infant death rate", "Type here")
    uf_deaths=st.text_input("under-five death rate", "Type here")
    Total_exp=st.text_input("Average total expenditure","Type here")
    GDP=st.text_input("Average GDP", "Type here")
    BMI=st.text_input("Average BMI", "Type here")
    thinness= st.text_input("Average thinness among 1-19 year children", "Type here")
    Alcohol=st.text_input("Average Alcohol consumption", "Type here")
    Schooling=st.text_input("Average Schooling rate", "Type here")
    features=[ct,year,sts,Population,HepatitisB,Measles,Polio,Diphtheria,HIV,infant_deaths,uf_deaths,Total_exp,GDP,BMI,thinness,Alcohol,Schooling]
    scaler=pickle.load(open('minmaxscaler.sav','rb'))
    model=pickle.load(open('rfmodel.sav','rb'))
    pred=st.button('PREDICT')
    if pred:
        prediction=model.predict(scaler.transform([features]))
        st.write("# Life Expectancy :",round(prediction.item(),1))
main()
