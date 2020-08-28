import cleaner as dataStream
import plotly.graph_objects as go
import plotly.io as pio

#DONUT PLOT - CONDITIONS -----------------------------------------

labels = ['Diabetes','Hypertension','Coronary Heart(D)','Chronic Kidney(D)','No Conditions','Obstructive Pulmonary(D)']
values = dataStream.PIEList
fig_cond = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
#fig_cond.show()
pio.write_html(fig_cond, file="templates/cond.html")


#GROUP BAR PLOT - SYMPTOMS ---------------------------------------

symplabel=['Symptoms']
fig_symp = go.Figure(data=[
    go.Bar(name='Fever', x=symplabel, y=dataStream.Fever),
    go.Bar(name='Cough', x=symplabel, y=dataStream.Cough),
    go.Bar(name='Breathlessness', x=symplabel, y=dataStream.Breathlessness),
    go.Bar(name='Severe Acute Respiratory Syndrome', x=symplabel, y=dataStream.SARI),
    go.Bar(name='Influenza-like Illness', x=symplabel, y=dataStream.ILI),
    go.Bar(name='Asymptomatic', x=symplabel, y=dataStream.NONE_sym)
])
fig_symp.update_layout(barmode='group')
#fig_symp.show()
pio.write_html(fig_symp, file="templates/symp.html")

#STACK BAR PLOT - AGE DATA ------------------------------------------
fig_age = go.Figure()
fig_age.add_trace(go.Bar(
    y=['0 to 10', '10 to 20', '20 to 30','30 to 40', '40 to 50', '50 to 60','60 to 70', '70 to 80', '80 to 90','90 to 100'],
    x=dataStream.maleAgeList,
    name='Male Deaths',
    orientation='h',
    marker=dict(
        color='rgba(61, 112, 242, 0.6)',
        line=dict(color='rgba(61, 112, 242, 1.0)', width=2)
    )
))
fig_age.add_trace(go.Bar(
    y=['0 to 10', '10 to 20', '20 to 30','30 to 40', '40 to 50', '50 to 60','60 to 70', '70 to 80', '80 to 90','90 to 100'],
    x=dataStream.femaleAgeList,
    name='Female Deaths',
    orientation='h',
    marker=dict(
        color='rgba(242, 61, 221, 0.6)',
        line=dict(color='rgba(242, 61, 221, 1.0)', width=2)
    )
))
fig_age.update_layout(barmode='stack')
#fig_age.show()
pio.write_html(fig_age, file="templates/age.html")