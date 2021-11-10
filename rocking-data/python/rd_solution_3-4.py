import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=LAPTOP-46UVL3DK;"
    "Database=pythonDB;"
    "Trusted_Connection=yes;",
    autocommit=True,
)

cursor = conn.cursor()
print("**************Connected to localhost server****************")
cursor.execute("SELECT @@SERVERNAME")
for i in cursor:
    print(i)

### Load data into memory ###
athletes = pd.read_excel("data/Athletes.xlsx")
coaches = pd.read_excel("data/Coaches.xlsx")
entries_gender = pd.read_excel("data/EntriesGender.xlsx")
medals = pd.read_excel("data/Medals.xlsx")
teams = pd.read_excel("data/Teams.xlsx")

### Drop all tables ###

cursor.execute(
    """DROP TABLE IF EXISTS Countries;
DROP TABLE IF EXISTS Genders;
DROP TABLE IF EXISTS Medals;
DROP TABLE IF EXISTS Disciplines;
DROP TABLE IF EXISTS MedalCompetitions;
DROP TABLE IF EXISTS Athletes;
DROP TABLE IF EXISTS Coaches;
DROP TABLE IF EXISTS Teams;
DROP TABLE IF EXISTS GendersDisciplines;
"""
)

### Create and populate Countries ###
cursor.execute(
    """CREATE TABLE Countries (
	CountryID INT NOT NULL,
  CountryName VARCHAR(255),
  PRIMARY KEY (CountryName)
);
"""
)
for index, country in enumerate(athletes["NOC"].sort_values().unique()):
    cursor.execute(
        """INSERT INTO Countries (CountryID, CountryName)
                VALUES (?,?)
                """,
        index + 1,
        country,
    )

### Create and populate Genders ###
cursor.execute(
    """CREATE TABLE Genders (
	GenderID INT NOT NULL,
  GenderName VARCHAR(255),
  PRIMARY KEY (GenderName)
);
"""
)
cursor.execute(
    """INSERT INTO Genders (GenderID, GenderName)
                VALUES (1,'Female'),
                (2,'Male'),
                (3,'Other'),
                (4,'Not informed')
                """,
)

### Create and populate Medals ###
cursor.execute(
    """CREATE TABLE Medals (
	MedalID INT NOT NULL,
  MedalType VARCHAR(255),
  PRIMARY KEY (MedalType)
);
"""
)
cursor.execute(
    """INSERT INTO Medals (MedalID, MedalType)
                VALUES (1,'Gold'),
                (2,'Silver'),
                (3,'Bronze')
                """,
)

### Create and populate Disciplines ###
cursor.execute(
    """CREATE TABLE Disciplines (
	DisciplineID INT NOT NULL,
  DisciplineType VARCHAR(255),
  PRIMARY KEY (DisciplineType)
);
"""
)
for index, discipline in enumerate(
    pd.concat([coaches["Discipline"], athletes["Discipline"], teams["Discipline"]])
    .sort_values()
    .unique()
):
    cursor.execute(
        """INSERT INTO Disciplines (DisciplineID, DisciplineType)
                VALUES (?,?)
                """,
        index + 1,
        discipline,
    )

### Create and populate Athletes ###
cursor.execute(
    """CREATE TABLE Athletes (
	AthleteID INT NOT NULL,
    AthleteFullName VARCHAR(255),
	CountryName VARCHAR(255) NOT NULL,
    VARCHAR(255),
    PRIMARY KEY (AthleteID),
	FOREIGN KEY (DisciplineType) REFERENCES Disciplines(DisciplineType),
	FOREIGN KEY (CountryName) REFERENCES Countries(CountryName),
);
"""
)
for index, athlete in enumerate(athletes.itertuples()):
    cursor.execute(
        """INSERT INTO Athletes (AthleteID, AthleteFullName, CountryName, DisciplineType)
                VALUES (?,?,?,?)
                """,
        index + 1,
        athlete.Name,
        athlete.NOC,
        athlete.Discipline,
    )
### Create and populate GendersDisciplines ###
cursor.execute(
    """CREATE TABLE GendersDisciplines (
	GendersDisciplinesID INT NOT NULL,
    DisciplineType VARCHAR(255),
    GenderName VARCHAR(255),
    FOREIGN KEY (GenderName) REFERENCES Genders(GenderName),
	FOREIGN KEY (DisciplineType) REFERENCES Disciplines(DisciplineType)
);
"""
)
temp_index = 0
for gender in entries_gender.itertuples():
    for female in range(gender.Female):
        cursor.execute(
            """INSERT INTO GendersDisciplines (GendersDisciplinesID, DisciplineType, GenderName)
                  VALUES (?,?,?)
                  """,
            temp_index + 1,
            gender.Discipline,
            "Female",
        )
        temp_index += 1
    for male in range(gender.Male):
        cursor.execute(
            """INSERT INTO GendersDisciplines (GendersDisciplinesID, DisciplineType, GenderName)
                  VALUES (?,?,?)
                  """,
            temp_index + 1,
            gender.Discipline,
            "Male",
        )
        temp_index += 1

### Create and populate Coaches ###
cursor.execute(
    """CREATE TABLE Coaches (
	CoachID INT NOT NULL,
  CoachFullName VARCHAR(255),
	CountryName VARCHAR(255) NOT NULL,
  DisciplineType VARCHAR(255),
	Event VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (CoachID),
	FOREIGN KEY (DisciplineType) REFERENCES Disciplines(DisciplineType),
	FOREIGN KEY (CountryName) REFERENCES Countries(CountryName),
);
"""
)
for index, coach in enumerate(coaches.itertuples()):
    cursor.execute(
        """INSERT INTO Coaches (CoachID, CoachFullName, CountryName, DisciplineType)
                VALUES (?,?,?,?)
                """,
        index + 1,
        coach.Name,
        coach.NOC,
        coach.Discipline,
    )

### Create and populate MedalCompetitions ###
cursor.execute(
    """CREATE TABLE MedalCompetitions (
	MedalCompetitionsID INT NOT NULL,
	CountryName VARCHAR(255) NOT NULL,
	MedalType VARCHAR(255),
  PRIMARY KEY (MedalCompetitionsID),
	FOREIGN KEY (CountryName) REFERENCES Countries(CountryName),
	FOREIGN KEY (MedalType) REFERENCES Medals(MedalType)
);
"""
)
temp_index = 0
for medals in medals.itertuples():
    for gold in range(medals.Gold):
        cursor.execute(
            """INSERT INTO MedalCompetitions (MedalCompetitionsID, CountryName, MedalType)
                  VALUES (?,?,?)
                  """,
            temp_index + 1,
            medals[2],
            "Gold",
        )
        temp_index += 1
    for silver in range(medals.Silver):
        cursor.execute(
            """INSERT INTO MedalCompetitions (MedalCompetitionsID, CountryName, MedalType)
                  VALUES (?,?,?)
                  """,
            temp_index + 1,
            medals[2],
            "Silver",
        )
        temp_index += 1
    for bronze in range(medals.Bronze):
        cursor.execute(
            """INSERT INTO MedalCompetitions (MedalCompetitionsID, CountryName, MedalType)
                  VALUES (?,?,?)
                  """,
            temp_index + 1,
            medals[2],
            "Bronze",
        )
        temp_index += 1

### Create and populate MedalCompetitions ###
cursor.execute(
    """CREATE TABLE Teams (
	TeamID INT NOT NULL,
	CountryName VARCHAR(255) NOT NULL,
  DisciplineType VARCHAR(255),
	Event VARCHAR(255),
  PRIMARY KEY (TeamID),
	FOREIGN KEY (DisciplineType) REFERENCES Disciplines(DisciplineType),
	FOREIGN KEY (CountryName) REFERENCES Countries(CountryName),
);
"""
)
for index, team in enumerate(teams.itertuples()):
    cursor.execute(
        """INSERT INTO Teams (TeamID, CountryName, DisciplineType)
                VALUES (?,?,?)
                """,
        index + 1,
        team.NOC,
        team.Discipline,
    )
