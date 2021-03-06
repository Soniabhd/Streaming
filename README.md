Project carried out as part of the M1 Econometrics-Statistics of the University of Paris 1 Panthéon Sorbonne

# Search engine for streaming platforms content

<p align="center">
  <img src="https://boutique.orange.fr/informations/amazon-prime-video/img/visuel-entete.png" width="235" height="125">
  <img src="https://cineuropa.org/imgCache/2018/09/19/1537358562024_0570x0400_0x0x0x0_1573370192897.png" width="235" height="125">
  <img src="http://watchama.fr/wp-content/uploads/2020/01/disney-plus-logo.png" width="235" height="125">
  <img src="https://assetshuluimcom-a.akamaihd.net/h3o/facebook_share_thumb_default_hulu.jpg" width="235" height="125">
</p>

### Here are the links to the datasets
Amazon Prime Video : https://www.kaggle.com/datasets/shivamb/amazon-prime-movies-and-tv-shows <br/>
Netflix : https://www.kaggle.com/datasets/shivamb/netflix-shows <br/>
Disney + : https://www.kaggle.com/datasets/shivamb/disney-movies-and-tv-shows <br/>
Hulu : https://www.kaggle.com/datasets/shivamb/hulu-movies-and-tv-shows <br/>


&nbsp;
### Install the necessary packages you need 

`pip install pyqt5`  <br/>
`pip install pandas`

&nbsp;
### Data cleaning 
1. Convert release_year column to string <br/>
2. Remove the following columns : show_id, date_added and rating (columns not needed)

&nbsp;
### Distribution of the content by platform and type

<p align="center">
  <img src="https://github.com/Soniabhd/Streaming/blob/main/graph_stream.png" width="700" height="300" >
</p>


&nbsp;
### The interface
Feel free to apply all the filters you want but pay attention to the spelling of names and titles.

<p align="center">
  <img src="https://github.com/Soniabhd/Streaming/blob/main/interface.png" width="600" height="700" >
</p>
