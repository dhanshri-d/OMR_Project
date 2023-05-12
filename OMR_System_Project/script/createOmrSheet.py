from PIL import Image, ImageDraw
import random

# Constants
QUESTION_COUNT = 10
OPTIONS_COUNT = 5
CIRCLE_RADIUS = 10
FILLED_CIRCLE_RADIUS = 30
CIRCLE_COLOR = "black"
FILLED_CIRCLE_COLOR = "black"
MARGIN = 200
QUESTION_SPACING = 120
OPTION_SPACING = 100
CIRCLE_SPACING = 60
QUESTION_NUMBER_PADDING = 30

# Calculate answer sheet dimensions with added background space
OMR_ANSWER_SHEET_WIDTH = 2 * MARGIN + (OPTIONS_COUNT - 1) * OPTION_SPACING + 2 * FILLED_CIRCLE_RADIUS
OMR_ANSWER_SHEET_HEIGHT = 2 * MARGIN + QUESTION_COUNT * QUESTION_SPACING

# Create blank answer sheet image with white background
omr_answer_sheet = Image.new("RGB", (OMR_ANSWER_SHEET_WIDTH, OMR_ANSWER_SHEET_HEIGHT), "white")
draw = ImageDraw.Draw(omr_answer_sheet)

# Draw questions and options
for i in range(QUESTION_COUNT):
    # Draw question number
    question_number = f"{i + 1}:"
    draw.text((MARGIN + QUESTION_NUMBER_PADDING, MARGIN + i * QUESTION_SPACING), question_number, fill="black")

    # Randomly choose an option to fill
    option_to_fill = random.randint(0, OPTIONS_COUNT - 1)

    # Draw options
    for j in range(OPTIONS_COUNT):
        # Calculate circle center coordinates
        circle_center_x = MARGIN + (j * OPTION_SPACING) + FILLED_CIRCLE_RADIUS
        circle_center_y = MARGIN + i * QUESTION_SPACING + FILLED_CIRCLE_RADIUS

        # Draw circle with clear edges
        draw.ellipse(
            [
                (circle_center_x - FILLED_CIRCLE_RADIUS, circle_center_y - FILLED_CIRCLE_RADIUS),
                (circle_center_x + FILLED_CIRCLE_RADIUS, circle_center_y + FILLED_CIRCLE_RADIUS),
            ],
            fill="white",
            outline=FILLED_CIRCLE_COLOR,
            width=3
        )

        # Fill the chosen option circle with black color
        if j == option_to_fill:
            draw.ellipse(
                [
                    (circle_center_x - FILLED_CIRCLE_RADIUS, circle_center_y - FILLED_CIRCLE_RADIUS),
                    (circle_center_x + FILLED_CIRCLE_RADIUS, circle_center_y + FILLED_CIRCLE_RADIUS),
                ],
                fill=CIRCLE_COLOR,
                outline=CIRCLE_COLOR,
            )

# Overlay the answer sheet on a different background color
background_color = "lightblue"  # Choose your desired background color
background_width = OMR_ANSWER_SHEET_WIDTH + 2 * MARGIN
background_height = OMR_ANSWER_SHEET_HEIGHT + 2 * MARGIN
background = Image.new("RGB", (background_width, background_height), background_color)
background.paste(omr_answer_sheet, (MARGIN, MARGIN))

# Save the composite image as a PNG file with optimization
omr_answer_sheet.show()
background.save("omr_answer_sheet10.png", optimize=True)

