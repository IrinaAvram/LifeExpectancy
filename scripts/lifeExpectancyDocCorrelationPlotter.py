
# coding: utf-8

# ### Parsing and processing of file 1

# In[1]:


import csv
import numpy

with open('../input/vie_005.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    ct = 0
    data1 = [[0]*3 for i in range(55)]
    plotdata1 = [[0]*55 for i in range(3)]
    gapFM = [0 for i in range(55)]
    for row in spamreader:
        if ct != 0:
            data1[ct - 1][0] = row[20]
            data1[ct - 1][1] = row[11].replace(",", ".")
            data1[ct - 1][2] = row[12].replace(",", ".")
            plotdata1[0][ct - 1] = row[20]
            plotdata1[1][ct - 1] = row[11].replace(",", ".")
            plotdata1[2][ct - 1] = row[12].replace(",", ".")
            if ct > 1:
                gapFMFloat = float(plotdata1[2][ct - 1]) - float(plotdata1[1][ct - 1])
                gapFM[ct - 1] = str(gapFMFloat)
            else:
                gapFM[ct - 1] = "Gap between Females and Males"
        ct = ct + 1


# ### Parsing and processing of file 2

# In[2]:


import csv
with open('../input/DP_LIVE_24032018181437189.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    data2 = [[0]*2 for i in range(56)]
    plotdata2 = [[0]*56 for i in range(2)]
    ct = 0
    ect = 0
    data2[0][0] = "REF_YEAR"
    data2[0][1] = "NR OF DOCTORS / 1000 INH"
    plotdata2[0][0] = "REF_YEAR"
    plotdata2[1][0] = "NR OF DOCTORS / 1000 INH"
    fullData2 = [[0]*8 for i in range(56)]
    fullData2[0] = ["LOCATION","INDICATOR","SUBJECT","MEASURE","FREQUENCY","REF_YEAR","NR OF DOCTORS / 1000 INH","FLAG CODES"]
    
    for row in spamreader:
        if row[0].replace('"', '') == "AUT":
            for elem in row:
                fullData2[ct + 1][ect] = row[ect].replace('"', '')
                ect = ect + 1
            data2[ct + 1][0] = row[5].replace('"', '')
            data2[ct + 1][1] = row[6]
            plotdata2[0][ct + 1] = row[5].replace('"', '')
            plotdata2[1][ct + 1] = row[6]
            ct = ct + 1
            ect = 0


# ### Complete data for file 1 as table

# In[3]:


import plotly.plotly as py
import plotly.figure_factory as ff
import pandas as pd
import plotly.tools as pt

pt.set_credentials_file(username='<INSERT USERNAME HERE>', api_key='<INSERT API KEY HERE>')
df = pd.read_csv("vie_005.csv", sep=';', skiprows=0)
table = ff.create_table(df)
py.iplot(table, filename='leAustriaInputRestricted')


# ### Only the necessary data from file 1 as table

# In[4]:


import plotly.plotly as py
import plotly.figure_factory as ff
import pandas as pd

table = ff.create_table(data1)
py.iplot(table, filename='leAustriaInputRestricted')


# ### Complete data for file 2 as table (only for Austria)

# In[5]:


import plotly.plotly as py
import plotly.figure_factory as ff
import pandas as pd

table = ff.create_table(fullData2)
py.iplot(table, filename='doctorsAustriaInput')


# ### Only the necessary data from file 2 as table

# In[6]:


import plotly.plotly as py
import plotly.figure_factory as ff
import pandas as pd

table = ff.create_table(data2)
py.iplot(table, filename='doctorsAustriaInputRestricted')


# ### Bar chart of male life expectancy

# In[7]:


import plotly.plotly as py
import plotly.tools as pt
from plotly.graph_objs import *

data = [Bar(x=plotdata1[0],
            y=plotdata1[1], name='Male Life Expectancy')]

layout = Layout(
    barmode='group'
)

annotations = []
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Source: Stadt Wien – data.wien.gv.at - Demographic indicators in Vienna since 1961',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False))
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Male Life Expectancy',
                              font=dict(family='Arial',
                                        size=24,
                                        color='rgb(37,37,37)'),
                              showarrow=False))
layout['annotations'] = annotations

fig = Figure(data=data, layout=layout)
py.iplot(fig, filename='leMale')


# ### Bar chart of female life expectancy

# In[8]:


import plotly.plotly as py
import plotly.tools as pt
from plotly.graph_objs import *

data = [Bar(x=plotdata1[0],
            y=plotdata1[2], name='Female Life Expectancy',
            marker=dict(
                color='rgba(222,45,38,0.8)',
        ))]

layout = Layout(
    barmode='group'
)

annotations = []
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Source: Stadt Wien – data.wien.gv.at - Demographic indicators in Vienna since 1961',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False))
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Female Life Expectancy',
                              font=dict(family='Arial',
                                        size=24,
                                        color='rgb(37,37,37)'),
                              showarrow=False))
layout['annotations'] = annotations

fig = Figure(data=data, layout=layout)
py.iplot(fig, filename='leFemale')


# ### Bar chart comparison of female and male life expectancy

# In[9]:


import plotly.plotly as py
import plotly.tools as pt
import plotly.graph_objs as go

tracef = go.Bar(x=plotdata1[0],
            y=plotdata1[1], name='Male Life Expectancy')
tracem = go.Bar(x=plotdata1[0],
            y=plotdata1[2], name='Female Life Expectancy',
               marker=dict(
                color='rgba(222,45,38,0.8)',
        ))

data = [tracef, tracem]
layout = go.Layout(
    barmode='group'
)

annotations = []
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Source: Stadt Wien – data.wien.gv.at - Demographic indicators in Vienna since 1961',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False))
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Female and male Life Expectancy',
                              font=dict(family='Arial',
                                        size=24,
                                        color='rgb(37,37,37)'),
                              showarrow=False))
layout['annotations'] = annotations

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='leMF')


# ### Scatter chart of gap between female and male life expectancy

# In[10]:


import plotly.plotly as py
import plotly.tools as pt
import plotly.graph_objs as go

traceg = go.Scatter(x=plotdata1[0], y=gapFM, 
                    mode='lines+markers', name='Gap between female and male LE',
                    line=dict(
                        color='rgba(67,67,67,1)',
                        shape='spline'
                    ))

annotations = []
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Source: Stadt Wien – data.wien.gv.at - Demographic indicators in Vienna since 1961',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False))
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Gap between female and male Life Expectancy',
                              font=dict(family='Arial',
                                        size=24,
                                        color='rgb(37,37,37)'),
                              showarrow=False))
layout['annotations'] = annotations
fig = go.Figure(data=[traceg], layout=layout)

py.iplot(fig, filename='leFMGap')


# ### Scatter chart of doctors per 1000 inhabitants in Austria

# In[11]:


import plotly.plotly as py
import plotly.tools as pt
import plotly.graph_objs as go


traced = go.Scatter(x=plotdata2[0], y=plotdata2[1], 
                    mode='lines+markers', name='Number of doctors per 1000 inhabitants',
                    line=dict(
                        color='rgba(204,204,204,1)',
                        shape='spline'
                    ))
annotations = []
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Source: OECD (2018), Doctors (indicator). doi: 10.1787/4355e1ec-en (Accessed on 26 March 2018)',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False))
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Number of doctors per 1000 inhabitants',
                              font=dict(family='Arial',
                                        size=24,
                                        color='rgb(37,37,37)'),
                              showarrow=False))
layout['annotations'] = annotations
fig = go.Figure(data=[traced], layout=layout)
py.iplot(fig, filename='doctors')


# ### Charts illustrating the comparison of life expectancy and nr of doctors increase

# In[12]:


tracef = go.Bar(x=plotdata1[0],
            y=plotdata1[1], name='Male Life Expectancy')
tracem = go.Bar(x=plotdata1[0],
            y=plotdata1[2], name='Female Life Expectancy',
               marker=dict(
                color='rgba(222,45,38,0.8)',
        ))

traced = go.Scatter(x=plotdata2[0], y=plotdata2[1], 
                    mode='lines+markers', name='Number of doctors per 1000 inhabitants',
                    line=dict(
                        color='rgba(204,204,204,1)',
                        shape='spline'
                    ))

data = [tracef, tracem, traced]
layout = go.Layout(barmode='group', yaxis =go.YAxis(tickvals=[0,1,2,60,70,80]))

annotations = []
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Source 1: Stadt Wien – data.wien.gv.at - Demographic indicators in Vienna since 1961<br>Source 2: OECD (2018), Doctors (indicator). doi: 10.1787/4355e1ec-en (Accessed on 26 March 2018)',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False))
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Female and male Life Expectancy',
                              font=dict(family='Arial',
                                        size=24,
                                        color='rgb(37,37,37)'),
                              showarrow=False))
layout['annotations'] = annotations

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='leMFAndDocs')


# In[13]:


tracef = go.Scatter(x=plotdata1[0],
            y=plotdata1[1], name='Male Life Expectancy')
tracem = go.Scatter(x=plotdata1[0],
            y=plotdata1[2], name='Female Life Expectancy',
               marker=dict(
                color='rgba(222,45,38,0.8)',
        ))

traced = go.Scatter(x=plotdata2[0], y=plotdata2[1], 
                    mode='lines+markers', name='Number of doctors per 1000 inhabitants',
                    line=dict(
                        color='rgba(204,204,204,1)',
                        shape='spline'
                    ),
                   yaxis='y2')

data = [tracef, tracem, traced]
layout = go.Layout(barmode='group', yaxis=dict(
        title='Life expectancy in years'
    ),
    yaxis2=dict(
        title='Doctors per 1000 inhabitants',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    ))

annotations = []
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Source 1: Stadt Wien – data.wien.gv.at - Demographic indicators in Vienna since 1961<br>Source 2: OECD (2018), Doctors (indicator). doi: 10.1787/4355e1ec-en (Accessed on 26 March 2018)',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False))
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Female and male life expectancy correlated with ammount of doctors',
                              font=dict(family='Arial',
                                        size=24,
                                        color='rgb(37,37,37)'),
                              showarrow=False))
layout['annotations'] = annotations

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='leMFAndDocsScatter')

