from dash import Dash, dcc, html, Input, Output, callback
import pandas as pd
from PIL import Image
from src.pattern import SweaterPattern
from flask import send_from_directory

df = pd.read_csv('data/knit_data.csv')

def run_app() -> None:
    app = Dash(__name__)
    app.title = 'Sweater Dashboard'

    @app.server.route("/downloads/<filename>")
    def serve_pdf(filename):
        return send_from_directory("downloads", filename, as_attachment=True)
    
    create_layout(app)
    app.run(debug=True, port=8051)
    return None

def create_layout(app: Dash) -> None:

    header = html.H1('Drop Shoulder Sweater Customization Dashboard',
                     style={'textAlign': 'center',
                            'fontFamily': 'American Typewriter',
                            'background-color': '#ffa6c3'}
                    )
    name_label = html.H4("Enter the name of your sweater (ex. My Sweater, The Kate, Alex's Sweater):",
                           style={'fontFamily': 'American Typewriter'}
                            )
    
    name_input = dcc.Input(id='name-input',
                            type='text',
                            placeholder='Enter name here',
                            style={'fontFamily': 'American Typewriter'}
                            )
    
    # COLUMN 1
    children = []
    # Neckline (second dropdown menu, select neckline type)
    neck_heading = html.H2('Neckline',
                            style={'fontFamily': 'American Typewriter',
                                'background-color': 'LavenderBlush',
                                'textAlign': 'center'}
                            )
    neck_label = html.H4('Select a neckline type:',
                        style={'fontFamily': 'American Typewriter'}
                        )
    neck_dd = dcc.Dropdown(id='neck-dd',
                           options=df['neck'].to_list(),
                           value = 'Boat neck',
                           style={'fontFamily': 'American Typewriter'}
                          )
    children += [neck_heading, neck_label, neck_dd]


    # Sleeves (first dropdown menu, select sleeve type)
    sleeve_heading = html.H2('Sleeve',
                           style={'fontFamily': 'American Typewriter',
                                  'background-color': 'LavenderBlush',
                                  'textAlign': 'center'}
                            )
    sleeve_label = html.H4('Select a sleeve type:',
                           style={'fontFamily': 'American Typewriter'}
                            )
    sleeve_dd = dcc.Dropdown(id='sleeve-dd',
                             options=df['sleeve'].to_list(),
                             value = 'Straight',
                             style={'fontFamily': 'American Typewriter'}
                            )
    children += [sleeve_heading, sleeve_label, sleeve_dd]
    

    # Embellishments
    # Dropdown menu for embellishments
    embellish_heading = html.H2('Embellishments',
                           style={'fontFamily': 'American Typewriter',
                                  'background-color': 'LavenderBlush',
                                  'textAlign': 'center'}
                            )
    embellish_label = html.H4('Select any optional embellishments:',
                              id='embellish-label',
                              style={'fontFamily': 'American Typewriter'}
                            )
    embellish_dd = dcc.Dropdown(id='embellish-dd',
                             options=df['embellish'].to_list(),
                             value='No embellishment',
                             style={'fontFamily': 'American Typewriter'}
                             )
    children += [embellish_heading, embellish_label, embellish_dd]
    
    # Ribbing pattern:
    ribbing_label = html.H4('Insert ribbing pattern (ex. 1x1, 1x2, 2x2):',
                            id='ribbing-label',
                            style={'fontFamily': 'American Typewriter'}
                            )
    ribbing_input1 = dcc.Input(id='rib-input1',
                                type='number',
                                placeholder='First number',
                                style={'fontFamily': 'American Typewriter'}
                                )
                            
    ribbing_input2 = dcc.Input(id='rib-input2',
                               type='number',
                               placeholder='Second number',
                               style={'fontFamily': 'American Typewriter'}
                                )
    
    children += [ribbing_label, ribbing_input1, ribbing_input2]
    
    # Cuff inputs:
    cuff_header = html.H4('Enter your desired ribbed cuff height (in inches):',
                            id='cuff-label',
                            style={'fontFamily': 'American Typewriter'}
                            )
    cuff_input = dcc.Input(id='cuff-input',
                            type='number',
                            placeholder='Cuff height (in inches)',
                            style={'display': 'block',
                                'verticalAlign': 'top',
                                'fontFamily': 'American Typewriter'}
                            )
    collar_header = html.H4('Enter your desired ribbed collar height (in inches):',
                            id='collar-label',
                            style={'fontFamily': 'American Typewriter'}
                            )
    collar_input = dcc.Input(id='collar-input',
                            type='number',
                            placeholder='Collar height (in inches)',
                            style={'fontFamily': 'American Typewriter'}
                            )
    children += [cuff_header, cuff_input, collar_header, collar_input]
    
    # Add all embellishment inputs to the children list
    
    # SIZING
    # Dropdown menu for sizing
    size_heading = html.H2('Sizing',
                           style={'fontFamily': 'American Typewriter',
                                  'background-color': 'LavenderBlush',
                                  'textAlign': 'center'}
                            )
    size_label = html.H4('Select the size of your sweater:',
                         id='size-label',
                         style = {'fontFamily': 'American Typewriter'}
                        )
    size_options = dcc.Dropdown(id='size-dd',
                             options=df['size'].to_list()+['Insert own measurements'],
                             value='Small',
                             style={'fontFamily': 'American Typewriter'}
                             )
    
    # Inputs for sizing
    sizing_label = html.H4('Insert your desired sweater measurements in inches:',
                            id='sizing-label',
                            style={'fontFamily': 'American Typewriter'}
                            )
    size_input1 = dcc.Input(id='size-input1',
                            type='number',
                            placeholder='Insert sleeve length',
                            style={'fontFamily': 'American Typewriter'}
                            )
    size_input2 = dcc.Input(id='size-input2',
                            type='number',
                            placeholder='Insert sleeve cuff width',
                            style={'fontFamily': 'American Typewriter'}
                            )
    size_input3 = dcc.Input(id='size-input3',
                            type='number',
                            placeholder='Insert shoulder width',
                            style={'fontFamily': 'American Typewriter'}
                            )
    size_input4 = dcc.Input(id='size-input4',
                            type='number',
                            placeholder='Insert body height',
                            style={'fontFamily': 'American Typewriter'}
                            )
    size_input5 = dcc.Input(id='size-input5',
                            type='number',
                            placeholder='Insert bottom width',
                            style={'fontFamily': 'American Typewriter'}
                            )
    size_input6 = dcc.Input(id='size-input6',
                            type='number',
                            placeholder='Insert neck opening width',
                            style={'fontFamily': 'American Typewriter'}
                            )
    children += [size_heading, size_label, size_options, sizing_label,
                 size_input1, size_input2, size_input3,
                 size_input4, size_input5, size_input6]
    
    # COLUMN 2
    # Image of the sweater
    children1 = []
    image = html.Img(id='image',
                    src=app.get_asset_url('assets/drop/drop_crew_straight.jpg'),
                    style={'width': '100%', 'height': 'auto',
                        'display': 'inline-block', 'verticalAlign': 'top'}
                    )
    
    # GAUGE
    gauge_heading = html.H2('Gauge',
                           style={'fontFamily': 'American Typewriter',
                                'background-color': 'LavenderBlush',
                                'textAlign': 'center'}
                            )
    gauge_label = html.H4('Enter the gauge of your chosen yarn in inches:',
                          id='gauge-label',
                          style={'fontFamily': 'American Typewriter'}
                        )
    length = html.Div([
        html.H4('Insert the length of your swatch:',
                id='length-label',
                style={'fontFamily': 'American Typewriter'}
                ),
        dcc.Input(id='length-input',
                type='number',
                placeholder='Insert length of swatch',
                style={'fontFamily': 'American Typewriter'}
                )
        ], style={'display': 'flex', 'alignItems': 'center'})
    
    stitch = html.Div([
        html.H4('Insert the number of stitches per inserted length:',
                id='stitch-label',
                style={'fontFamily': 'American Typewriter'}
                ),
        dcc.Input(id='stitch-input',
                type='number',
                placeholder='Insert number of stitches',
                style={'fontFamily': 'American Typewriter'}
                )
        ], style={'display': 'flex', 'alignItems': 'center'})
    
    height = html.Div([
        html.H4('Insert the height of your swatch:',
                id='height-label',
                style={'fontFamily': 'American Typewriter'}
                ),
        dcc.Input(id='height-input',
                type='number',
                placeholder='Insert height of swatch',
                style={'fontFamily': 'American Typewriter'}
                )
        ], style={'display': 'flex', 'alignItems': 'center'})
    
    row = html.Div([
        html.H4('Insert the number of rows per inserted height:',
                id='row-label',
                style={'fontFamily': 'American Typewriter'}
                ),
        dcc.Input(id='row-input',
                type='number',
                placeholder='Insert number of rows',
                style={'fontFamily': 'American Typewriter'}
                )
        ], style={'display': 'flex', 'alignItems': 'center'})
    
    button = html.Button('Generate Pattern', id='generate-btn', n_clicks=0)

    link = html.A('Download Pattern PDF',
                    id='download-link',
                    href='',
                    download='sweater_pattern.pdf',
                    target='_blank',
                    style={'display': 'none',
                           'marginTop': '20px',
                           'fontSize': '12px',
                           'fontFamily': 'Courier'})

    
    children1 += [image, gauge_heading, gauge_label, length, stitch, height, row, button, link]

    # LAYOUT
    app.layout = html.Div([
        header,
        name_label,
        name_input,
        html.Hr(),
        html.Div([
            html.Div(children=children, style={'flex': '1', 'padding': '10px'}),
            html.Div(children=children1, style={'flex': '1', 'padding': '10px', 'width': '100%'})
            ], style={'display': 'flex'})
        ])
       
    return

@callback(
    Output('image','src'),
    Input('sleeve-dd', 'value'),
    Input('neck-dd', 'value'),
    Input('embellish-dd', 'value')
)
def update_image(sleeve: str,
                 neck: str,
                 embellish: str,
                 ):
    neck_opts = {
        'Boat neck': '_boat',
        'Crew neck': '_crew',
        'Mock neck': '_mock',
        'Turtleneck': '_turtle'
    }
    sleeve_opts = {
        'Straight': '_straight',
        'Tapered': '_tapered',
        'Flare': '_flare',
        'Balloon': '_balloon'
    }
    embellish_opts = {
        'Ribbed edges': '_cuff',
        'Ribbed collar': '_collar',
        'Ribbed edges and collar': '_cuff_collar',
        'No embellishment': ''
    }

    img = Image.open(f'assets/drop{neck_opts[neck]}{sleeve_opts[sleeve]}{embellish_opts[embellish]}.jpg')
    return img
    
@callback(
    Output('ribbing-label', 'style'),
    Output('rib-input1', 'style'),
    Output('rib-input2', 'style'),
    Output('cuff-label', 'style'),
    Output('cuff-input', 'style'),
    Input('embellish-dd', 'value'),
)
def update_embellish_input(embellish: str):
    if embellish != 'No embellishment':
        style = {'display': 'block',
                 'fontFamily': 'American Typewriter'
                 }
    else:
        style = {'display': 'none',
                 'fontFamily': 'American Typewriter',
                 }
    return style, style, style, style, style
    
@callback(
    Output('collar-label', 'style'),
    Output('collar-input', 'style'),
    Input('neck-dd', 'value'),
    Input('embellish-dd', 'value')
)
def update_collar(neck: str, embellish: str):
    if (neck == 'Boat neck' or 'Crew neck') or (embellish == 'No embellishment'):
        style = {'display': 'none',
                 'fontFamily': 'American Typewriter'
                 }
    else:
        style = {'display': 'block',
                 'fontFamily': 'American Typewriter',
                 }
    return style, style

@callback(
    Output('sizing-label', 'style'),
    Output('size-input1', 'style'),
    Output('size-input2', 'style'),
    Output('size-input3', 'style'),
    Output('size-input4', 'style'),
    Output('size-input5', 'style'),
    Output('size-input6', 'style'),
    Input('size-dd', 'value')
)
def update_size_input(size: str):
    if size == 'Insert own measurements':
        style = {'display': 'block',
                 'fontFamily': 'American Typewriter'
                 }
    else:
        style = {'display': 'none',
                 'fontFamily': 'American Typewriter',
                 }
    return style, style, style, style, style, style, style
    

@callback(
    Output('download-link', 'href'),
    Output('download-link', 'style'),
    Input('generate-btn', 'n_clicks'),
    Input('name-input', 'value'),
    Input('neck-dd', 'value'),
    Input('sleeve-dd', 'value'),
    Input('embellish-dd', 'value'),
    Input('rib-input1', 'value'),
    Input('rib-input2', 'value'),
    Input('cuff-input', 'value'),
    Input('collar-input', 'value'),
    Input('size-dd', 'value'),
    Input('size-input1', 'value'),
    Input('size-input2', 'value'),
    Input('size-input3', 'value'),
    Input('size-input4', 'value'),
    Input('size-input5', 'value'),
    Input('size-input6', 'value'),
    Input('length-input', 'value'),
    Input('stitch-input', 'value'),
    Input('height-input', 'value'),
    Input('row-input', 'value')
    )
def generate_pattern(n_clicks, name,
                    neck, sleeve, embellishment,
                    rib1, rib2, cuff, collar, size,
                    sleeve_length, sleeve_cuff_width, shoulder_width,
                    body_height, bottom_width, neck_opening_width,
                    length, stitch, height, row):
    if n_clicks == 0:
        return '', {'display': 'none'}
    
    try:
        pattern = SweaterPattern(name, neck, sleeve, embellishment,
                            rib1, rib2, cuff, collar, size,
                            sleeve_length, sleeve_cuff_width, shoulder_width,
                            body_height, bottom_width, neck_opening_width,
                            length, stitch, height, row)
        filename = pattern.generate_pdf()
        href = f"/downloads/{filename}"
        return href, {'display': 'inline',
                      'fontFamily': 'American Typewriter'}
    except Exception as e:
        print(f"Error: {e}")
        return '', {'display': 'none',
                    'fontFamily': 'American Typewriter'}
