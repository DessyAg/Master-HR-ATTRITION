import dash_html_components as html
import dash_table as dt

PAGE_SIZE = 15

def generate_table(dataframe) :
    return dt.DataTable(
        id='table-multicol-sorting',
        columns=[
            {"name": i, "id": i} for i in dataframe.columns
        ],
       
        style_cell_conditional=[{
        'if': {'row_index': 'odd'},
        'backgroundColor': 'rgb(248, 248, 248)'
         }],
        pagination_settings={
            'current_page': 0,
            'page_size': PAGE_SIZE
        },
        pagination_mode='be',

        sorting='be',
        sorting_type='multi',
        sorting_settings=[],
        style_table={'overflowX': 'scroll'}
    )

def renderTable(df) :
    return html.Div([
                html.H1('HR-Employee-Attrition', className='h1'),
                generate_table(df)
            ])