import os, sys
import pandas as pd

path = os.getcwd()
ap = pd.read_csv(path+"\\amazon_prime_titles.csv",sep = ",",low_memory=False)
dp = pd.read_csv(path + "\\disney_plus_titles.csv",sep = ",",low_memory=False)
hu = pd.read_csv(path + "\\hulu_titles.csv",sep = ",",low_memory=False)
nf = pd.read_csv(path + "\\netflix_titles.csv",sep = ",",low_memory=False)

ap['platform'] = "Amazon Prime"
dp['platform'] = "Disney Plus"
nf['platform']= "Netflix"
hu['platform']= "Hulu"

df = pd.concat([ap,dp,hu,nf],ignore_index=True)
df['release_year'] = df['release_year'].astype(str)
df.drop(["show_id","date_added","rating"],axis=1,inplace=True)

#Interface

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow) : 

    def __init__(self,*args,**kwargs) :
        super(MainWindow,self).__init__(*args,**kwargs)
        self.setWindowTitle("Search Engine")
        self.setFixedSize(QSize(800,850))
      
        main = QVBoxLayout()
        layout_type = QHBoxLayout()
        grid = QGridLayout()
        layout_plat = QHBoxLayout()
        grid2 = QHBoxLayout()
        grid3 = QGridLayout()
        grid3.setVerticalSpacing(20)

        self.setStyleSheet("background-color: white ;color: black;font-size: 14px")

        self.label = QLabel("Find films and series available on some of the best streaming platforms !")
        self.label.setAlignment(Qt.AlignCenter)

        self.label.setStyleSheet("font : Microsoft YaHei UI; font-size: 20px; font-style : bold; color : #40ADF9;")

        #Button : Movie & TV Show
        movie = QPushButton("Movie",self)
        serie = QPushButton("TV Show",self)
        types = [movie,serie]
        for x in types : 
            x.setStyleSheet("""QPushButton{font : Microsoft YaHei UI;font-size: 14px ; height: 32px ; max-width: 160px; font-weight: bold ; color: white;
                                   background-color:  #5EB4FA ; border : 2px ; border-style: solid ; border-radius:10px ; border-color : white }
                                   QPushButton::hover {color : #5EB4FA  ; border : 2px ; border-style: solid ; border-radius:10px ;  border-color : #5EB4FA ; background-color : white}
                                   QPushButton::checked{color : #5EB4FA  ; border : 2px ; border-style: solid ; border-radius:10px ;  border-color : #5EB4FA ; background-color : white}""")
            layout_type.addWidget(x)

        #Button - categories
        comedy = QPushButton('Comedy')
        drama = QPushButton('Drama')
        international = QPushButton('International')
        aa = QPushButton('Action && Adventure')
        family = QPushButton('Family')
        docu = QPushButton('Documentary')
        tsv = QPushButton('Talk Show && Variety')
        horror = QPushButton('Horror')
        suspense = QPushButton('Suspense')
        mvc = QPushButton("Music Videos && Concerts")
        SciFi = QPushButton("Science-Fiction")
        yaa = QPushButton('Young Adult')
        anime = QPushButton('Anime')
        sport = QPushButton("Sport")
        ls = QPushButton('Lifestyle')
        romance = QPushButton('Romance')
        latinos = QPushButton('Latino')

        #Button - Plateforme
        netflix = QPushButton('Netflix')
        disney = QPushButton('Disney Plus')
        amazon = QPushButton('Amazon Prime')
        hulu = QPushButton('Hulu')

        platforms = [hulu, disney, amazon, netflix]
        short_cat = [comedy,drama,family,docu,horror,suspense,SciFi,anime,sport,ls,romance,latinos,international,yaa]
        long_cat = [aa,tsv,mvc]
        
        for l in [platforms,types,short_cat,long_cat] :
            for x in l :
                x.setCheckable(True)
        for l in [platforms,types,short_cat] :
            for x in l :  
                x.setFixedSize(QSize(140,40))
        
        for x in short_cat :  
            x.setStyleSheet("""QPushButton{font : Microsoft YaHei UI;font-size: 14px ; font-weight: bold ; color: white;
                                   background-color: #8986F8 ; border : 2px ; border-style: solid ; border-radius:10px ; border-color : white }
                                   QPushButton::hover {color :  #8986F8 ; border : 2px ; border-style: solid ; border-radius:10px ;  border-color : #8986F8 ; background-color : white}
                                   QPushButton::checked{color :  #8986F8 ; border : 2px ; border-style: solid ; border-radius:10px ;  border-color : #8986F8 ; background-color : white}""")
        
        for x in long_cat : 
            x.setFixedSize(QSize(200,40))
            x.setStyleSheet("""QPushButton{font : Microsoft YaHei UI;font-size: 14px ;  font-weight: bold ; color: white;
                                   background-color: #8986F8 ; border : 2px ; border-style: solid ; border-radius:10px ; border-color : white }
                                   QPushButton::hover {color :  #8986F8 ; border : 2px ; border-style: solid ; border-radius:10px ;  border-color : #8986F8 ; background-color : white}
                                   QPushButton::checked{color :  #8986F8 ; border : 2px ; border-style: solid ; border-radius:10px ;  border-color : #8986F8 ; background-color : white}""")
            grid2.addWidget(x)

        for x in platforms : 
            x.setStyleSheet("""QPushButton{font : Microsoft YaHei UI;font-size: 14px ; height: 32px ; max-width: 160px; font-weight: bold ; color: white;
                                   background-color:  #A06CF8 ; border : 2px ; border-style: solid ; border-radius:10px ; border-color : white }
                                   QPushButton::hover {color :   #A06CF8 ; border : 2px ; border-style: solid ; border-radius:10px ;  border-color : #A06CF8 ; background-color : white}
                                   QPushButton::checked{color :  #A06CF8 ; border : 2px ; border-style: solid ; border-radius:10px ;  border-color : #A06CF8 ; background-color : white}""")
            layout_plat.addWidget(x)

        for i in range(0,3) :
            for j in range(0,4) :
                x = short_cat[j+(i*4)]
                grid.addWidget(x,i,j)
        
        main.addWidget(self.label)
        main.addLayout(layout_type)
        main.addSpacing(20)
        main.addLayout(grid)
        main.addLayout(grid2)
        main.addSpacing(20)
        main.addLayout(layout_plat)
        main.addSpacing(10)

        #Texte à saisir - title
        self.title = QLineEdit()
        self.title.setMaxLength(50)
        self.title.setPlaceholderText("Enter a title")
        self.title.setStyleSheet("height: 32px ; max-width: 375px; border : 2px ; border-style: solid ; border-radius:10px ; border-color : #B456F7")
        self.title.setAlignment(Qt.AlignCenter)
        grid3.addWidget(self.title,1,0)
        

        #Texte à saisir - actor
        self.actor = QLineEdit()
        self.actor.setMaxLength(30)
        self.actor.setPlaceholderText("Enter the name of an actor")
        self.actor.setStyleSheet("height: 32px ; max-width: 375px;border : 2px ; border-style: solid ; border-radius:10px ; border-color : #B950F7")
        self.actor.setAlignment(Qt.AlignCenter)
        grid3.addWidget(self.actor,3,0)
        
        #Texte à saisir - director
        self.director = QLineEdit(self)
        self.director.setMaxLength(30)
        self.director.setPlaceholderText("Enter the name of a director")
        self.director.setStyleSheet("height: 32px ; max-width: 375px;border : 2px ; border-style: solid ; border-radius:10px ; border-color : #CD3BF6")
        self.director.setAlignment(Qt.AlignCenter)
        grid3.addWidget(self.director,5,0)

        #Texte à saisir - country
        country1=df.country.unique()
        country2 = country1.tolist()
        liste_pays = []
        country2 = [x for x in country2 if type(x) != float]
        for elem in country2:
            if "," in elem:
                temp = elem.split(",")
                for elem in temp:
                    if ' ' in temp :
                        elem.strip()
                        if elem not in liste_pays:
                            liste_pays.append(elem)
            else:
                if elem not in liste_pays:
                    liste_pays.append(elem) 
        

        self.country = QLineEdit(self)
        self.country.setPlaceholderText("Enter a country")
        self.country.setStyleSheet("height: 32px ; max-width: 375px;border : 2px ; border-style: solid ; border-radius:10px ; border-color : #E520F5")
        self.country.setAlignment(Qt.AlignCenter)
        validator2 = QRegExpValidator(QRegExp("[a-zA-Z]*"))
        self.country.setValidator(validator2)
        completer = QCompleter(liste_pays)
        self.country.setCompleter(completer)
        grid3.addWidget(self.country,7,0)

        #Texte à saisir - dates (release_year)
        year = ['1920', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935',
        '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951',
        '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967',
        '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983',
        '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999',
        '2000', '2001', '2002', '2003', '2004', '2005','2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', 
        '2016', '2017', '2018', '2019', '2020', '2021']

        validator = QRegExpValidator(QRegExp('19[2-9][0-9]|20[0-2][0-9]'))
        self.years = QLineEdit(self)
        self.years.setValidator(validator)
        self.years.setPlaceholderText("Enter a release year")
        self.years.setStyleSheet("height: 32px ; max-width: 375px;border : 2px ; border-style: solid ; border-radius:10px ; border-color : #FE04F4")
        self.years.setAlignment(Qt.AlignCenter)
        completer2 = QCompleter(year)
        self.years.setCompleter(completer2)
        grid3.addWidget(self.years,9,0)


        def moteur():
            global df_filt

            title_ = self.title.text()
            actor_ = self.actor.text()
            director_ = self.director.text()
            country_ = self.country.text()
            release_ = self.years.text()
            movie_ = "Movie"
            serie_ = "Show"
            net = "Netflix"
            ama = "Amazon"
            dis = "Disney"
            hu = "Hulu"
            comedy_list = ['Comedy','Comedies','Parody','Stand Up']
            docu_list = ['Special Interest','Docuseries','Documentary','Documentaries','Arts','and Culture','Historical',
                      'History','Animals & Nature','Biographical','Anthology','Disaster']
            inter = 'International'
            latino = 'Latino'
            dramas = 'Drama'
            rom = 'Roman'
            horror_ = 'Horror'
            aa_list = ['Action','Action-Adventure','Adventure','Military and War','Western']
            fam_list = ['Kids','Animation','Cartoons']
            tsv_list = ['Talk Show and Variety','Entertainment','Variety','Talk Show','Reality','Game Shows','News']
            lifestyle_list = ['Fitness','Faith and Spirituality','LGBTQ','Arthouse','Food']
            suspens_list = ['Suspense','Crime','Policie/Cop','Thriller']
            sports = 'Sport'
            mvc_list = ['Music Videos and Concerts','Musical','Music','Concert Film']
            sf_list = ['Science Fiction','Sci-Fi','Fantasy','Superhero']
            yaa_list =  ['Coming of Age','Young Adult Audience']
            animes = 'Anime'
        
            c1 = False
            if movie.isChecked() == True :
                c1 = c1| df['type'].str.contains(movie_.title())if movie_ else True 
            if serie.isChecked() == True :
                c1 = c1 | df['type'].str.contains(serie_.title())if serie_ else True 
            if ((movie.isChecked() == False) & (serie.isChecked() == False)) :
                c1 = True

            c2 = False
            if comedy.isChecked() == True :
                for x in comedy_list :
                    c2 = c2 | df['listed_in'].str.contains(x.title()) if x else True
            if horror.isChecked() == True :
                c2 = c2 | df['listed_in'].str.contains(horror_.title()) if horror_ else True
            if international.isChecked() == True :
                c2 = c2 | df['listed_in'].str.contains(inter.title()) if inter else True
            if docu.isChecked() == True :
                for x in docu_list :
                    c2 = c2 | df['listed_in'].str.contains(x.title()) if x else True
            if latinos.isChecked() == True :
                c2 = c2 | df['listed_in'].str.contains(latino.title()) if latino else True
            if drama.isChecked() == True :
                c2 = c2 | df['listed_in'].str.contains(dramas.title()) if dramas else True
            if romance.isChecked() == True :
                c2 = c2 | df['listed_in'].str.contains(rom.title()) if rom else True
            if aa.isChecked() == True :
                for x in aa_list :
                    c2 = c2 | df['listed_in'].str.contains(x.title()) if x else True
            if family.isChecked() == True :
                for x in fam_list :
                    c2 = c2 | df['listed_in'].str.contains(x.title()) if x else True
            if tsv.isChecked() == True :
                for x in tsv_list :
                    c2 = c2 | df['listed_in'].str.contains(x.title()) if x else True
            if ls.isChecked() == True :
                for x in lifestyle_list :
                    c2 = c2 | df['listed_in'].str.contains(x.title()) if x else True
            if suspense.isChecked() == True :
                for x in suspens_list :
                    c2 = c2 | df['listed_in'].str.contains(x.title()) if x else True
            if mvc.isChecked() == True :
                for x in mvc_list :
                    c2 = c2 | df['listed_in'].str.contains(x.title()) if x else True
            if sport.isChecked() == True :
                c2 = c2 | df['listed_in'].str.contains(sports.title()) if sports else True
            if anime.isChecked() == True :
                c2 = c2 | df['listed_in'].str.contains(animes.title()) if animes else True
            if SciFi.isChecked() == True :
                for x in sf_list :
                    c2 = c2 | df['listed_in'].str.contains(x.title()) if x else True
            if yaa.isChecked() == True :
                for x in yaa_list :
                    c2 = c2 | df['listed_in'].str.contains(x.title()) if x else True
            else : c2 = True
             

            c3 = df['country'].str.contains(country_.title()) if country_ else True

            c4 = df['cast'].str.contains(actor_.title()) if actor_ else True

            c5 = df['title'].str.contains(title_.title()) if title_ else True

            c6 = df['release_year'].str.contains(release_) if release_ else True 

            c7 =  df['director'].str.contains(director_.title()) if director_ else True

            c8 = False
            if amazon.isChecked() == True :
                c8 = c8 | df['platform'].str.contains(ama.title()) if ama else True
            if netflix.isChecked() == True :
                c8 = c8 | df['platform'].str.contains(net.title()) if net else True
            if disney.isChecked() == True :
                c8 = c8 | df['platform'].str.contains(dis.title()) if dis else True
            if hulu.isChecked() == True :
                c8 = c8 | df['platform'].str.contains(hu.title()) if hu else True
            if ((amazon.isChecked() == False) & (netflix.isChecked() == False) & (disney.isChecked() == False) & (hulu.isChecked() == False)) :
                c8 = True
            
            df_filt = (df[c1 & c2 & c3 & c4 & c5 & c6 & c7 & c8])


            self.dialog = Second(self)
            self.dialog.show()

        
        self.search = QPushButton('SEARCH',self)
        self.search.clicked.connect(moteur)
        self.search.setFixedWidth(250)
        self.search.setStyleSheet("""font : Microsoft YaHei UI;font-size: 16px ; height: 32px ; max-width: 250px; font-weight: bold ; color: white;
                                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2CECFC, stop:1 #FF03F4);
                                    border-style: solid ; border-radius:10px ; """)

    
        grid3.addWidget(self.search,11,0,Qt.AlignHCenter)
        main.addLayout(grid3)
        main.addSpacing(20)
        windows = QWidget()
        windows.setLayout(main)
        self.setCentralWidget(windows)
        
        
class Second(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(Second,self).__init__(*args,**kwargs)
        main2 = QWidget()
        self.setWindowTitle("Results")
        self.setFixedSize(QSize(1500,1000))
        self.layout = QVBoxLayout()
        self.view = QTableView()
        self.model = PandasModel(df_filt)
        self.view.setModel(self.model)
        self.view.resizeRowsToContents()
        self.layout.addWidget(self.view)
        main2.setLayout(self.layout)
        self.setCentralWidget(main2)

class PandasModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self,parent=None):
        return self._data.shape[0]

    def columnCount(self,parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row()][index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
