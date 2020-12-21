from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

# Setting style for bar graphs
import matplotlib.pyplot as plt
#%matplotlib inline


# set font

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'
fig, ax = plt.subplots(figsize=(8.5, 11))

# Decorative Lines
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=300)
plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)

# set background color
#ax.set_facecolor('white')

# remove axes
plt.axis('off')

# Text Variables
Header = '>>>This resume was generated entirely in Python. For full sourcecode, view my Github \nhttps://github.com/piy72/ResumeBuilder.'
Name = 'PEEYUSH SHANKER TRIVEDI '
Title = 'Automation Engineer'
Contact = '568 kha/373,\nGeetapalli, Alambagh\nLucknow\nUttar Pradesh\nPin Code-226005\nPhone- 9653093751\nEmail-peeyusht612@gmail.com'
ProjectsHeader = 'PROJECTS'
ProjectOneTitle = 'Credit Suisse Infrastructure Automation'
ProjectOneDesc = '- Create CI/CD pipelines for Linux servers and Windows servers\n- Deploy those pipelines using Jenkins through Source code Management\n- Automate different scenarioes of internal web portals using Selenium and \n  Blueprism'
ProjectTwoTitle = 'Middleware Component Testing'
ProjectTwoDesc = '- Testing the functionalities of different middleware components of a vehicle.\n- Used Shell scripting for different middleware components like wifi etc.'
ProjectThreeTitle = 'Face detection system using Artficial neural networks'
ProjectThreeDesc = '- This was my major project in college.\n- Main aim of this project was to identify the faces from input picture.\n- Used Matlab as the coding language.'
ProjectFourTitle = 'Virtual Assistant'
ProjectFourDesc = '- This was a python based project.\n- This project was my personal project to impliment voice recognition through \n  python.'

WorkHeader = 'EXPERIENCE'
WorkOneTitle = 'Wipro Technologies / Automation Engineer'
WorkOneTime = '5/2018-Present'
WorkOneDesc = '- In the project with Credit suisse, decreased the manual effort in each tower by \n  50%\n- Convencing the customer to move from earlier framework to our \n  Java based framework which cut the execution time to almost half.\n- Got new Web portals for Automation which decreased the revenue loss from \n  10% to 3%'
WorkTwoTitle = 'Wipro Technologies / Automation Tester'
WorkTwoTime = '10/2017-3/2018'
WorkTwoDesc = '- Test various middleware componemts of vehicle using shell script.\n- Since it was my first project, I spent more time in learning about automation \nprocesses'

EduHeader = 'EDUCATION'
EduOneTitle = 'SRM University, B.Tech'
EduOneTime = '2013-2017'
EduOneDesc = '- Stream: Computer Science and Engineering\n- Major Project: Face detection System using Artficial neural networks'
EduTwoTitle = 'Lucknow Public Inter College, Intermediate'
EduTwoTime = '2011-12'
EduTwoDesc = '- Stream: Physics, Chemistry, Mathemetics and Computer Science'
SkillsHeader = 'Skills'
SkillsDesc = '- Java\n- Blueprism\n- Jenkins\n- Keyword Driven Approach\n- Command Line\n- Git and Version Control\n- SQL\n- Basic Shell Scripting\n- Excel\n- Python'
ExtrasTitle = 'Strengths'
ExtrasDesc = '- Fast Learner\n- Eager to learn new technologies\n- Innovator'

# add text
plt.annotate(Header, (.02,.98), weight='regular', fontsize=8, alpha=.75)
plt.annotate(Name, (.02,.94), weight='bold', fontsize=20)
plt.annotate(Title, (.02,.91), weight='regular', fontsize=14)
plt.annotate(Contact, (.7,.893), weight='regular', fontsize=8, color='#ffffff')
plt.annotate(ProjectsHeader, (.02,.86), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(ProjectOneTitle, (.02,.832), weight='bold', fontsize=10)
plt.annotate(ProjectOneDesc, (.04,.772), weight='regular', fontsize=9)
plt.annotate(ProjectTwoTitle, (.02,.745), weight='bold', fontsize=10)
plt.annotate(ProjectTwoDesc, (.04,.714), weight='regular', fontsize=9)
plt.annotate(ProjectThreeTitle, (.02,.685), weight='bold', fontsize=10)
plt.annotate(ProjectThreeDesc, (.04,.64), weight='regular', fontsize=9)
plt.annotate(ProjectFourTitle, (.02,.615), weight='bold', fontsize=10)
plt.annotate(ProjectFourDesc, (.04,.57), weight='regular', fontsize=9)

plt.annotate(WorkHeader, (.02,.52), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(WorkOneTitle, (.02,.491), weight='bold', fontsize=10)
plt.annotate(WorkOneTime, (.02,.473), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkOneDesc, (.04,.383), weight='regular', fontsize=9)
plt.annotate(WorkTwoTitle, (.02,.355), weight='bold', fontsize=10)
plt.annotate(WorkTwoTime, (.02,.337), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkTwoDesc, (.04,.287), weight='regular', fontsize=9)

plt.annotate(EduHeader, (.02,.230), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(EduOneTitle, (.02,.190), weight='bold', fontsize=10)
plt.annotate(EduOneTime, (.02,.170), weight='regular', fontsize=9, alpha=.6)
plt.annotate(EduOneDesc, (.04,.135), weight='regular', fontsize=9)
plt.annotate(EduTwoTitle, (.02,.10), weight='bold', fontsize=10)
plt.annotate(EduTwoTime, (.02,.085), weight='regular', fontsize=9, alpha=.6)

plt.annotate(SkillsHeader, (.7,.75), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(SkillsDesc, (.7,.56), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(ExtrasTitle, (.7,.403), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(ExtrasDesc, (.7,.345), weight='regular', fontsize=10, color='#ffffff')

#Save pdf
plt.savefig('resumeexample.pdf', dpi=300, bbox_inches='tight')

#add qr code
#arr_code = mpimg.imread('ekresumecode.png')
#imagebox = OffsetImage(arr_code, zoom=0.5)
#ab = AnnotationBbox(imagebox, (0.84, 0.12))
#ax.add_artist(ab)
