from fpdf import FPDF
import re
from pathlib import Path

class SweaterPattern:
    def __init__(self, name, neck, sleeve, embellishment,
                    rib1, rib2, edge, collar, size,
                    sleeve_length, sleeve_cuff_width, shoulder_width,
                    body_height, bottom_width, neck_opening_width,
                    length, stitch, height, row):
        self.sleeve = sleeve
        self.neck = neck
        self.embellishment = embellishment
        self.size = size
        self.length = length
        self.stitch = stitch
        self.height = height
        self.row = row
        self.sleeve_length = sleeve_length
        self.sleeve_cuff_width = sleeve_cuff_width
        self.shoulder_width = shoulder_width
        self.body_height = body_height
        self.bottom_width = bottom_width
        self.neck_opening_width = neck_opening_width
        self.name = name
        self.rib1 = rib1
        self.rib2 = rib2
        self.edge = edge
        self.collar = collar
        self.pattern = ''

        self.stitch_gauge = round(stitch/length)
        self.row_gauge = round(row/height)

        size_chart = {
            "Small": {'sleeve_length': 19, 'sleeve_cuff_width': 3.5, 'shoulder_width': 23, "body_height": 24.5,
                      "bottom_width": 21, "neck_opening_width": 14, "sleeve_opening_width": 7.5, "mock_height": 2, 'turtle_height': 6},
            "Medium": {"sleeve_length": 19.5, "sleeve_cuff_width": 3.75, "shoulder_width": 23, "body_height": 25.5,
                       "bottom_width": 22, "neck_opening_width": 15, "sleeve_opening_width": 8, 'mock_height': 2, 'turtle_height': 6},
            "Large": {"sleeve_length": 20, "sleeve_cuff_width": 4, "shoulder_width": 25, "body_height": 26.5,
                      "bottom_width": 23, "neck_opening_width": 16, "sleeve_opening_width": 8.5, 'mock_height': 2.5, 'turtle_height': 6},
            "X-Large": {"sleeve_length": 21, "sleeve_cuff_width": 4.25, "shoulder_width": 26, "body_height": 27.5,
                        "bottom_width": 24, "neck_opening_width": 17, "sleeve_opening_width": 9, 'mock_height': 2.5, 'turtle_height': 6}
        }
        if self.size != "Insert own measurements":
            self.sleeve_length = size_chart[self.size]["sleeve_length"]
            self.sleeve_cuff_width = size_chart[self.size]["sleeve_cuff_width"]
            self.shoulder_width = size_chart[self.size]["shoulder_width"]
            self.body_height = size_chart[self.size]["body_height"]
            self.bottom_width = size_chart[self.size]["bottom_width"]
            self.neck_opening_width = size_chart[self.size]["neck_opening_width"]
            self.sleeve_opening_width = size_chart[self.size]["sleeve_opening_width"]
            if self.neck == 'Mock neck':
                self.collar = size_chart[self.size]['mock_height']
            if self.neck == 'Turtleneck':
                self.collar = size_chart[self.size]['turtle_height']
        if self.size == 'Insert own measurements':
            self.size == 'custom'
        
        if self.sleeve == 'Tapered' or 'Balloon':
            self.num_decreases = round(((self.sleeve_opening_width*2) - (self.sleeve_cuff_width*2))*self.stitch_gauge/2)
            num_rounds = self.sleeve_length * self.row_gauge
            self.decrease = round(num_rounds/self.num_decreases)
        if self.sleeve == 'Flare':
            self.num_increases = round(((self.sleeve_cuff_width*2) - (self.sleeve_opening_width*2))*self.stitch_gauge/2)
            num_rounds = self.sleeve_length * self.row_gauge
            self.increase = round(num_rounds/self.num_increases)
        

    def layout(self):
        """
        Contructs the text of the pattern.        
        """
        # Variables for repeated sentences:
        if self.edge != None:
            edge = f"Knit a {self.rib1}x{self.rib2} rib until your rib measures {self.edge} inches."
        else:
            edge = ''
        if self.collar != None:
            collar = f"Knit a {self.rib1}x{self.rib2} rib until your rib measures {self.collar} inches."
        else:
            collar = ''

        # Pattern
        self.pattern = [
            # Intro
            ('h1', f'{self.name} Sweater Pattern'),
            ('text', f'This is the pattern for your {self.size.lower()}, {self.sleeve.lower()}, {self.neck.lower()}, drop shoulder sweater. This pattern is written using knitting jargon so please look up any terms you are unfamiliar with. Please keep in mind that yarn types may alter some measurements. Consistently test your work against your desired measurements throughout your project to ensure accuracy. Make adjustments if needed. Enjoy!'),
            ('text', ''),
            ('h2', f'Materials Needed'),
            ('text', f'- 1200 to 1800 yards of yarn'),
            ('text', f'- 9 inch and 32 inch circular needles'),
            ('text', f'- 1 tapestry needle'),
            ('text', f'- 1 stitch marker'),
            ('text', ''),

            # Sweater Body
            ('h2', f'Knit the Body'),
            ('text', f'1. Cast on {self.bottom_width*self.stitch_gauge*2} stitches to 32 inch circular needles. Place a stitch marker on your right needle and conenct your stitches in the round. {edge}'),
            ('text', f'2. Knit stockinette until your work measures {round(self.body_height-self.sleeve_opening_width)} inches and you have reached your stitch marker.'),
            ('text', f'3. Split for sleeves by putting {self.bottom_width*self.stitch_gauge} stitches onto a separate set of needles or scrap string and remove the stitch marker.')
        ]
        if self.neck == 'Boat neck':
            self.pattern += [
                ('text', f'4. Knit the front half by to knitting stockinette flat until your work measures {self.sleeve_opening_width} inches from the underarm to the top. {collar}'),
                ('text', f'5. If you used scrap string, put the back half stitches onto your needles. If you used a separate set of needles for the back half, switch to those.'),
                ('text', f'6. Knit stockinette on the back half until the front and back heights are equal. Use stitch markers to count rows if you wish to be precise in their heights. {collar}')
                ]
        else:
            self.pattern += [
                ('text', f'4. Knit the front half by continuing to knit stockinette until your work measures {self.sleeve_opening_width} inches from the underarm to the top.'),
                ('text', f'5. If you used scrap string, put the back half stitches onto your needles. If you used a separate set of needles for the back half, switch to those.'),
                ('text', f'6. Knit stockinette until the front and back heights are equal.')
                ]
        self.pattern += [
            ('text', f'7. Use a mattress stitch and a tapestry needle to sew the front and back of the top of your work together. Sew {(self.shoulder_width-self.neck_opening_width)/2} inches of stitches together from the left shoulder towards the center. Repeat for the right edge.')
            ]
        if self.neck != 'Boat neck':
            if self.collar != None:
                self.pattern += [('text', f'8. Pick up the neckline stitches and knit a {self.rib1}x{self.rib2} rib until your rib measures {self.collar} inches.')]
            else:
                self.pattern += [('text', f'8. Pick up the neckline stitches and knit stockinette until your collar measures {self.collar} inches.')]
        # Sleeves
        self.pattern += [
            ('text', ''),
            ('h2', f'Knit the {self.sleeve} Sleeves'),
            ('text', f'1. Pick up every third stitch on the left arm hole. Place a stitch marker on your right needle to mark the beginning of the row.')
            ]
        if self.sleeve == 'Straight':
            self.pattern += [
                ('text', f'2. Knit stockinette until your sleeves measure {self.sleeve_length} inches. {edge}'),
                ('text', f'3. Cast off.'),
                ('text', f'4. Repeat steps 1-3 for the right sleeve.')
                ]
        if self.sleeve == 'Tapered':
            self.pattern += [
                ('text', f'2. Knit {self.decrease-1} rounds of stockinette. Knit another round and K2Tog the last two stitches before the stitch marker. Knit one stitch after the stitch marker then K2Tog the next two stitches. Use stitch markers to mark your decrease rounds if you wish to do so. {edge}'),
                ('text', f'3. Repeat Step 2 {self.num_decreases} times.'),
                ('text', f'4. Cast off.'),
                ('text', f'5. Repeat steps 1-3 for the right sleeve.'),
                ]
        if self.sleeve == 'Flare':
            self.pattern += [
                ('text', f'2. Knit {self.increase-1} rounds of stockinette. Knit another round and M1R before the stitch marker. Knit one stitch after the stitch marker then M1L. Use stitch markers to mark your increase rounds if you wish to do so. {edge}'),
                ('text', f'3. Repeat Step 2 {self.num_increases} times.'),
                ('text', f'4. Cast off.'),
                ('text', f'5. Repeat steps 1-3 for the right sleeve.'),
                ]
        if self.sleeve == 'Balloon':
            self.pattern += [
                ('text', f'2. Knit stockinette until your sleeves measure {self.sleeve_length}. Knit two more rounds and K2Tog every {round(self.sleeve_opening_width*2/self.num_decreases*2)} stitches. {edge}'),
                ('text', f'3. Cast off.'),
                ('text', f'4. Repeat steps 1-3 for the right sleeve.')
                ]


    def generate_pdf(self):
        self.layout()

        Path("downloads").mkdir(exist_ok=True)
        safe_name = re.sub(r'[^\w\s-]', '', self.name).strip().replace(' ', '_')
        filename = f"downloads/{safe_name}_sweater_pattern.pdf"

        pdf = FPDF()
        pdf.add_page()

        for kind, text in self.pattern:
            if kind == 'h1':
                pdf.set_fill_color(255, 166, 195)
                pdf.set_font('Courier', 'BU', 16)
                pdf.cell(0, 10, text, ln=True, fill=True, align='C')
            elif kind == 'h2':
                pdf.cell(0, 3, '', ln=True)
                pdf.set_fill_color(255, 240, 245)
                pdf.set_font('Courier', 'B', 14)
                pdf.cell(0, 10, text, ln=True, fill=True)
            else:  # default paragraph
                pdf.set_font('Courier', '', 12)
                pdf.multi_cell(0, 10, text)
        
        pdf.output(filename)
        return filename