# Swimming Pool Shock Assistant CLI

#### Video Demo: https://youtu.be/Kz9LmwrTYGg

#### Description: Swimming Pool Shock Assistant is a CLI application written in Python that lets you calculate the amount of shock product needed to clean a swimming pool.

Most of the “heavy-lifting” in the project is done by the **pool** and **questions** modules inside the lib directory.

The **questions** modules leverages the Python **inquirer** module to generate the questionnaire and get the answers from the user. This module also includes all the validation needed to make sure the user enters the correct data type when answering the questionnaire (i.e. making sure you cannot enter a non-numeric value when typing the width, length, volume, etc of the pool)

The **pool** module contains the **Pool** Class, which is an Abstract Class. The **RectangularPool** and **RoundPool** classes inherit from this **Pool** Abstract Class and define their respective implementations for methods such as **generate** and **get_volume**. This particular design choice was made to facilitate the inclusion of other possible shapes in the future. For example,  a new Triangle Shaped Pool could be added as an option, just as long as the new TrianglePool Class conforms to the interface defined by the **Pool** Class.

In addition, the **pool** module also includes three **Enum** type files: water_color.py, shape.py and depth_type.py. These enums are used through the application to make sure we have a consistent set of values to reference when describing aspects of the pool such as its water color, depth type or shape.

The **project.py** file includes five functions besides the **main** function :

- The **generate_pool_with_answers** function accepts the questionnaire answers as an argument and makes sure we have all the required information to generate a new **Pool**. It then proceeds to determine which shape of pool to generate (i.e. Rectangular or Round) and after calling **map_answers_to_pool_init_args** to get the initial arguments needed to instantiate it, it generates a new Pool (with either the **RectangularPool** or the **RoundPool** class)

- The **map_answers_to_pool_init_args** function accepts a dictionary with the questionnaire answers as an argument and maps them to a new dictionary which contains all the values needed to instantiate a **Pool** , making sure all these new values have the correct data type.

- The **generate_pool_cleaning_instructions_message**  function accepts a **Pool** type value as an argument and calls the **get_required_shock_dose** method of **Pool** to generate the shocking instructions that will be ultimately displayed to the user.

- The **map_pool_data_to_table_data**  function also accepts a **Pool** type value as an argument, but in this case we  use it to generate a multi-dimensional *list* value which will be ultimately passed to the **tabulate** Python module in order to generate a table; this table contains all the summarized information about the swimming pool and the required amount of shock to clean it.

- Lastly we also have a **get_welcome_message** function which is used to generate a colorful welcome message to the user with the title and purpose of the application.

The project also includes two tests files:
- **test_pool.py** includes all the tests for both the **RectangularPool** and **RoundPool** classes.
- **test_project.py** includes all the tests for the five functions in the project.py file.

