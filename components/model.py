import dash_core_components as dcc
import dash_html_components as html

def renderModelPredict() :
    return html.Div([
                html.H1('Test Predict Diabetes', className='h1'),
                html.Div(children=[

                    html.Div([
                        html.P('Age : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputAge', type='number', value='0')
                    ],className='col-4'),


                    html.Div([
                        html.P('Daily rate: ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputDailyrate', type='number', value='0')
                    ],className='col-4'),

                    html.Div([
                        html.P('Distance From Home : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputDistanceHome', type='number', value='0')
                    ],className='col-4'),


                    html.Div([
                        html.P('Education : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='education', type='number', value='0')
                    ],className='col-4'),

                    html.Div([
                        html.P('EnvironmentSatisfaction : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputenvironmentsatisfaction', type='number', value='0')
                    ],className='col-4'),

                     html.Div([
                        html.P('HourlyRate : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputHourlyRate', type='number', value='0')
                    ],className='col-4'),

                    html.Div([
                        html.P('JobInvolvement : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputjobinvolvement', type='number', value='0')
                    ],className='col-4'),

                    html.Div([
                        html.P('JobLevel : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputjoblevel', type='number', value='0')
                    ],className='col-4'),

                     html.Div([
                        html.P('Job Satisfaction : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputjobsatisfaction', type='number', value='0')
                    ],className='col-4'),


                    
                     html.Div([
                        html.P('Monthly Income : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputmonthlyincome', type='number', value='0')
                    ],className='col-4'),

                    html.Div([
                        html.P('Monthly Rate : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputmonthlyrate', type='number', value='0')
                    ],className='col-4'),

                    html.Div([
                        html.P('NumCompaniesWorked : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputcompaniesworked', type='number', value='0')
                    ],className='col-4'),

                     html.Div([
                        html.P('Percent Salary Hike : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputsalaryhike', type='number', value='0')
                    ],className='col-4'),

                    html.Div([
                        html.P('Performance Rating: ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputperformancerating', type='number', value='0')
                    ],className='col-4'),


                    html.Div([
                        html.P('Relationship Satisfaction: ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputrelationshipsatisfaction', type='number', value='0')
                    ],className='col-4'),

                    html.Div([
                        html.P('StockOptionLevel: ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputstockoptionlevel', type='number', value='0')
                    ],className='col-4'),

                    html.Div([
                        html.P('Total Working Years: ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputworkingyears', type='number', value='0')
                    ],className='col-4'),

                    html.Div([
                        html.P('Training Time Last Years: ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputtimelastyear', type='number', value='0')
                    ],className='col-4'),

                    html.Div([
                        html.P('Work Life Balance: ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputworkbalance', type='number', value='0')
                    ],className='col-4'),

                    html.Div([
                        html.P('Years At Company: ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputyearsatcompany', type='number', value='0')
                    ],className='col-4'),

                    html.Div([
                        html.P('Years In Current Role: ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputincurrentrole', type='number', value='0')
                    ],className='col-4'),

                    html.Div([
                        html.P('Years Since Last Promotion: ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputsincelastpromotion', type='number', value='0')
                    ],className='col-4'),

                    html.Div([
                        html.P('Years with Curr Manager: ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputsincecurrmanager', type='number', value='0')
                    ],className='col-4'),


                    html.Div([
                        html.P('Business Travel : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(id='inputBusinessTravel',
                        options=[{'label': i.capitalize(),
                        'value': i} for i in ['Travel_Rarely','Travel_Frequently','Non-Travel']],
                        value='Travel_Rarely')
                    ],className='col-4'),

                
                    html.Div([
                        html.P('Department : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(id='inputDepartment',
                        options=[{'label': i.capitalize(),
                        'value': i} for i in ['Sales','Research & Development','Human Resources']],
                        value='Sales')
                    ],className='col-4'),


                    html.Div([
                        html.P('Education Field : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(id='educationfield',
                        options=[{'label': i.capitalize(),
                        'value': i} for i in ['Life Sciences','Medical','Marketing','Technical Degree'
                        'Human Resources','Other']],
                        value='Medical')
                    ],className='col-4'),

                    html.Div([
                        html.P('Gender : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(id='inputgender',
                        options=[{'label': i.capitalize(),
                        'value': i} for i in ['Female','Male']],
                        value='Female')
                    ],className='col-4'),

                    html.Div([
                        html.P('Job Role : ')
                    ],className='col-2'),
                     html.Div([
                        dcc.Dropdown(id='inputjobrole',
                        options=[{'label': i.capitalize(),
                        'value': i} for i in ['Sales Executive','Research Scientist','Laboratory Technician'
                        'Manufacturing Director','Healthcare Representative','Manager','Sales Representative',
                        'Research Director','Human Resources']],
                        value='Sales Executive')
                    ],className='col-4'),

                    html.Div([
                        html.P('Marital Status : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(id='inputmaritalstatus',
                        options=[{'label': i.capitalize(),
                        'value': i} for i in ['Single','Married','Divorced']],
                        value='Single')
                    ],className='col-4'),


                    html.Div([
                        html.P('Over Time : ')
                    ],className='col-2'),
                     html.Div([
                        dcc.Dropdown(id='inputovertime',
                        options=[{'label': i.capitalize(),
                        'value': i} for i in ['Yes','No']],
                        value='Yes')
                    ],className='col-4'),

                    
                    html.Div([
                        html.Button('Predict', id='buttonPredict', className='btn btn-primary')
                    ],className='mx-auto', style={ 'paddingTop': '20px', 'paddingBottom': '20px' })
                ],className='row'),
                html.Div([
                    html.H2('', id='outputPredict', className='mx-auto')
                ], className='row')
            ])