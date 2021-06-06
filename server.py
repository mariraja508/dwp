import os
from flask import Flask,render_template,url_for,redirect,request,flash

app=Flask(__name__)

data={
  'ActionDisplayName' : 'Submit',
  'Attributes' : [ 
    {
'Type' : 'Checkbox',
'Name' :'Course',
'CheckValues' : [{
  'DisplayValue' : 'B.E',
  'Value' : 'b.e'
},
{
'DisplayValue' : 'B.Sc',
'Value' : 'b.sc'
},
],
    },

    {
      'DropdownValues' : [{
       'DisplayValue' : 'Guest',
       'Value' : 'gust'
    },
  {
    'DisplayValue' : 'Admin',
    'Value' : 'admin'
  },
],
'Name' : 'UserType',
'Type' : 'Dropdown'
},
    
    {
        'Name' : 'Username',
        'Type' : 'TextBox',
        'Size' : 10,
      },
      {
        'Name' : 'Password',
        'Type' : 'SeceretTextBox',
        'Size' : 10,
      },    
     
      {
        'Name' : "Gender",
        "Options" : [
          {
            'DisplayValue' : "Male",
            "Value" : "male"
        },
        {
          'DisplayValue' : "Female",
          "Value" : "female"
      }
        ],
        'Type' : "RadioButton",
      },  
      
      {
        'Name' : 'Address',
        'Type' : 'TextBox',
        'Size' : 10,
      },
        {
        'Name' : 'UserTime',
        'Type' : 'TimeBox',
        'Size' : 10,
      },
      {
        'Name' : 'UserEmail',
        'Type' : 'EmailBox',
        'Size' : 10,
      },  
  ]
}
@app.route("/",methods=['GET','POST'])
def cntd():
    return render_template("index.html",datas=data)

os.system("git add .")
os.system("git status")
os.system("git commit -m 'first' " )
os.system("git log")
if(__name__=='__main__'):
    app.run(debug=True)
