import numpy as np

industry_names = np.array(['Software Development', 'Hardware Manufacturing', 'Cybersecurity', 'Cloud Computing',
                           'Artificial Intelligence (AI) and Machine Learning',
                           'Data Analytics and Business Intelligence', 'Internet of Things (IoT)',
                           'Telecommunications',
                           'E-commerce and Online Retail', 'Digital Marketing and Advertising', 'Fintech',
                           'Healthcare IT', 'Gaming and Entertainment Technology', 'EdTech', 'Robotics',
                           'CleanTech',
                           'Big Data', 'Blockchain and Cryptocurrency', 'Mobile App Development',
                           'Cyber Forensics'])
industry_vacancies = np.array([['Senior Software Engineer', 'Frontend Developer', 'Quality Assurance Analyst'],
                               ['Hardware Design Engineer', 'Product Assembly Technician', 'Quality Control Inspector'],
                               ['Cybersecurity Analyst', 'Ethical Hacker', 'Information Security Manager'],
                               ['Cloud Solutions Architect', 'DevOps Engineer', 'Cloud Security Specialist'],
                               ['Machine Learning Engineer', 'AI Research Scientist', 'Data Scientist'],
                               ['Business Intelligence Analyst', 'Data Visualization Specialist', 'Big Data Engineer'],
                               ['IoT Solutions Architect', 'Embedded Systems Engineer', 'IoT Security Consultant'],
                               ['Network Engineer', 'Telecommunications Specialist', 'VoIP Engineer'],
                               ['E-commerce Manager', 'Online Marketing Specialist', 'Fulfillment Coordinator'],
                               ['Digital Marketing Manager', 'SEO Specialist', 'Social Media Strategist'],
                               ['Financial Analyst', 'Blockchain Developer', 'Payments Solutions Architect'],
                               ['Health IT Project Manager', 'Clinical Informatics Specialist',
                                'Telemedicine Specialist'],
                               ['Game Developer', 'UX/UI Designer for Gaming', '3D Animator'],
                               ['EdTech Product Manager', 'Online Learning Content Creator',
                                'Educational Software Developer'],
                               ['Robotics Engineer', 'Automation Specialist', 'Robotics Software Developer'],
                               ['Renewable Energy Engineer', 'Sustainability Analyst', 'Environmental Data Analyst'],
                               ['Big Data Architect', 'Data Engineer', 'Hadoop Administrator'],
                               ['Cryptocurrency Analyst', 'Smart Contract Developer',
                                'Blockchain Solutions Consultant'],
                               ['Mobile App Developer', 'iOS/Android Developer', 'Mobile App UI/UX Designer'],
                               ['Digital Forensics Investigator', 'Cybersecurity Forensics Analyst',
                                'Incident Response Specialist']
                               ])

skills = np.array([
    'Python', 'JavaScript', 'Java', 'C/C++', 'Ruby', 'PHP', 'Swift', 'Kotlin', 'Objective-C', 'TypeScript',
    'HTML/CSS', 'SQL', 'Shell Scripting', 'MATLAB', 'R', 'Scala', 'Go', 'Perl', 'Rust', 'Assembly Language',
    'Bash Scripting', 'PowerShell', 'Node.js', 'React', 'Angular', 'Vue.js', 'Django', 'Flask', 'Spring Framework',
    'Hibernate', 'Android SDK', 'iOS SDK', 'Xamarin', 'Unity', 'Unreal Engine', 'Selenium', 'Appium', 'JMeter',
    'Gatling',
    'Docker', 'Kubernetes', 'Git', 'SVN', 'CI/CD', 'AWS', 'Azure', 'GCP', 'Linux/Unix Administration',
    'Windows Server Administration',
    'TCP/IP', 'HTTP/HTTPS', 'DNS', 'Firewall Configuration', 'IDS', 'VPNs', 'OWASP Top 10',
    'Data Structures and Algorithms',
    'OOP Concepts', 'Functional Programming', 'Concurrent Programming', 'Reactive Programming', 'RESTful API Design',
    'GraphQL',
    'Microservices Architecture', 'MongoDB', 'Cassandra', 'MySQL', 'PostgreSQL', 'Distributed Computing',
    'Parallel Computing',
    'AWS', 'Azure', 'GCP', 'Solidity', 'Truffle', 'Payment Gateway Integration', 'Telehealth Technologies', 'Unity',
    'Unreal Engine',
    'Educational Technology Tools', 'ROS - Robot Operating System', 'Renewable Energy Systems', 'Hadoop', 'Spark',
    'Snowflake', 'Redshift',
    'D3.js', 'Matplotlib', 'NLTK', 'SpaCy', 'OpenCV', 'TensorFlow', 'Scikit-learn', 'Keras', 'Tableau', 'Power BI',
    'Flutter', 'React Native',
    'Digital Forensics Tools', 'Incident Response Tools', 'NIST', 'ISO 27001', 'Secure Coding Guidelines', 'Scrum',
    'Kanban',
    'SDLC Models', 'Cloud Security Best Practices', 'Threat Modeling Techniques', 'Ethical Hacking Methodologies',
    'Burp Suite', 'Metasploit',
    'Cross-platform Development Strategies', 'Secure Mobile Development Practices', 'Wireless Security Protocols',
    'Cybersecurity Incident Response Planning',
    'Malware Analysis Tools', 'Interpreters and Compilers', 'Software Design Patterns',
    'Mobile App Performance Optimization', 'System Design Principles',
    'Real-time Systems Development', 'Fault-Tolerant Systems Design', 'DevSecOps Principles',
    'Cloud Migration Strategies', 'Cryptography Libraries'
])

industry_vacancies_dict = {}

for idx, industry in enumerate(industry_names):
    industry_vacancies_dict[industry] = list(industry_vacancies[idx])

