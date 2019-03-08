import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

color_set = ['#80aaff','#cc0000']

def legendDiabetic(val) :
    if(val == 1) :
        return ''
    return ''

def renderScatterPlot(df) :
    return html.Div([
                html.H1('Scatter Plot HR ATTRITION', className='h1'),
                dcc.Graph(
                    id='scatterPlot',
                    figure={
                        'data': [
                            go.Scatter(
                                x=df[df['Attrition'] == col].head(500)['Age'],
                                y=df[df['Attrition'] == col].head(500)['MonthlyIncome'],
                                mode='markers',
                                marker=dict(color=color_set[i], size=10, line=dict(width=0.5, color='white')),
                                name=legendDiabetic(col)
                            ) for col, i in zip(df['Attrition'].unique(), range(2))
                        ],
                        'layout': go.Layout(
                            xaxis= dict(title='Age'),
                            yaxis={'title': 'Monthly Income'},
                            margin={ 'l': 40, 'b': 40, 't': 10, 'r': 10 },
                            hovermode='closest'
                        )
                    }
                )
            ])