import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output, State
import pickle
from components.HRTable import renderTable
from components.scatterPlot import renderScatterPlot
from components.modelPredict import renderModelPredict

loadModel = pickle.load(open('dtree_attrition_final.sav', 'rb'))

app = dash.Dash(__name__)

server = app.server

dfHR = pd.read_csv('HRCSV.csv')

app.title = 'Dashboard HR-Employee Attrition'

app.layout = html.Div(children=[
    html.H1(children='Dashboard HR-Employee-Attrition ',className='titleDashboard'),
        dcc.Tabs(id="tabs", value='tab-1', children=[
            dcc.Tab(label=' HR-Employee-Attrition', value='tab-1',children=[
                renderTable(dfHR)
            ]),


        dcc.Tab(label='Scatter Plot', value='tab-2',children=[
            renderScatterPlot(dfHR)
        ]),

        dcc.Tab(label='Test Predict', value='tab-3',children=[
            renderModelPredict()
        ]),
        
    ], style={
        'fontFamily': 'system-ui'
    }, content_style={
        'fontFamily': 'Arial',
        'borderBottom': '1px solid #d6d6d6',
        'borderLeft': '1px solid #d6d6d6',
        'borderRight': '1px solid #d6d6d6',
        'padding': '44px'
    })


], style={
    'maxWidth': '1200px',
    'margin': '0 auto'
})

@app.callback(
    Output('table-multicol-sorting', "data"),
    [Input('table-multicol-sorting', "pagination_settings"),
     Input('table-multicol-sorting', "sorting_settings")])
def update_graph(pagination_settings, sorting_settings):
    # print(sorting_settings)
    if len(sorting_settings):
        dff = dfHR.head(500).sort_values(
            [col['column_id'] for col in sorting_settings],
            ascending=[
                col['direction'] == 'asc'
                for col in sorting_settings
            ],
            inplace=False
        )
    else:
        # No sort is applied
        dff = dfHR.head(500)

    return dff.iloc[
        pagination_settings['current_page']*pagination_settings['page_size']:
        (pagination_settings['current_page'] + 1)*pagination_settings['page_size']
    ].to_dict('rows')

@app.callback(
    Output('outputPredict', 'children'),
    [Input('buttonPredict', 'n_clicks')],
    [State('inputAge', 'value'), 
    State('inputDailyrate', 'value'),
    State('inputDistanceHome', 'value'),
    State('education', 'value'),
    State('inputenvironmentsatisfaction', 'value'),
    State('inputHourlyRate', 'value'),
    State('inputjobinvolvement', 'value'),
    State('inputjoblevel', 'value'),
    State('inputjobsatisfaction', 'value'),
    State('inputmonthlyincome', 'value'),
    State('inputmonthlyrate', 'value'),
    State('inputcompaniesworked', 'value'),
    State('inputsalaryhike', 'value'),
    State('inputperformancerating', 'value'),
    State('inputrelationshipsatisfaction', 'value'),
    State('inputstockoptionlevel', 'value'),
    State('inputworkingyears', 'value'),
    State('inputtimelastyear', 'value'),
    State('inputworkbalance', 'value'),
    State('inputyearsatcompany', 'value'),
    State('inputincurrentrole', 'value'),
    State('inputsincelastpromotion', 'value'),
    State('inputsincecurrmanager', 'value'),
    State('inputBusinessTravel', 'value'),
    State('inputDepartment', 'value'),
    State('educationfield', 'value'),
    State('inputgender', 'value'),
    State('inputjobrole', 'value'),
    State('inputmaritalstatus', 'value'),
    State('inputovertime', 'value')
    # State('inputincurrentrole', 'value'),
    # State('inputsincelastpromotion', 'value'),
    # State('inputsincecurrmanager', 'value'),

    ])



def update_output(n_clicks, Age,DailyRate,DistanceFromHome,Education,EnvironmentSatisfaction,HourlyRate,JobInvolvement,JobLevel,
                JobSatisfaction,MonthlyIncome,MonthlyRate,NumCompaniesWorked,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,
                StockOptionLevel,TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,
                YearsSinceLastPromotion,YearsWithCurrManager,BusinessTravel,Department,EducationField,Gender,JobRole,MaritalStatus,OverTime
               ):
    data = np.array([[Age,DailyRate,DistanceFromHome,Education,EnvironmentSatisfaction,HourlyRate,JobInvolvement,JobLevel,
                JobSatisfaction,MonthlyIncome,MonthlyRate,NumCompaniesWorked,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,
                StockOptionLevel,TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,
                YearsSinceLastPromotion,YearsWithCurrManager,BusinessTravel,Department,EducationField,Gender,JobRole,MaritalStatus,OverTime]])


    prediction = loadModel.predict(data)
    predictProba = loadModel.predict_proba(data)

    hasil = ''
    if(prediction[0] == 1) :
        hasil = 'Attriction'
    else :
        hasil = 'No Attriction'
    return 'Prediction : ' + hasil + ' | Probability : ' + str(predictProba[0,1])


if __name__ == '__main__':
    app.run_server(debug=True,port=1997)