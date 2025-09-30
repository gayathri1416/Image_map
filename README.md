# Ex04 Places Around Me
# Date:30.09.2025
# AIM
To develop a website to display details about the places around my house.

# DESIGN STEPS
## STEP 1
Create a Django admin interface.

## STEP 2
Download your city map from Google.

## STEP 3
Using <map> tag name the map.

## STEP 4
Create clickable regions in the image using <area> tag.

## STEP 5
Write HTML programs for all the regions identified.

## STEP 6
Execute the programs and publish them.

# CODE
```
urls.py:
from django.contrib import admin
from django.urls import path
from mapapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.p1),
    path('new/',views.p2,name='manali'),
    path('file/',views.p3,name='park'),
    path('new1/',views.p4,name='oil'),
    path('file1/',views.p5,name='petrol'),
    path('new2/',views.p6,name='lake'),
    ]

viwes.py:

from django.shortcuts import render
from django.http import HttpResponse
def p1(request):
    return render (request,'map.html')
def p2(request):
    return render(request,'webpage5.html')
def p3(request):
     return render(request,'webpage1.html')
def p4(request):
     return render(request,'webpage2.html')
def p5(request):
     return render(request,'webpage3.html')
def p6(request):
     return render(request,'webpage4.html')

map.html : 

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
     
        {% load static %} 
        <img src="{% static 'map.png' %}" usemap="#mymap" height="50%" width="100%" >
        <map name="mymap">
        <area shape="rect" coords="838,347,1207,250" href="{% url 'manali' %}" title=" MANALI CLICK HERE" >
        <area shape="rect" coords="170,750,2,450" href="{% url 'park' %}" title="PARK CLICK HERE">
        <area shape="circle" coords="552,0,200" href="{% url 'oil' %}" title="INDIAN OIL CLICK HERE">
        <area shape="rect" coords="1393,573,1023,436" href="{% url 'petrol' %}" title="PLANT-1 CLICK HERE">
        <area shape="rect" coords="443,800,200,400" href="{% url 'lake' %}" title="LAKE CLICK HERE">
</body>
</html>

webpage1.html:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    body{
        background: #d791e6;
    }
    .Title{
        font-family: Georgia, 'Times New Roman', Times, serif;
        align-items: center;
        letter-spacing: 0.2cm;
    }
    .content{
        width: 100%;
        line-height: 1cm;
        font-size: larger;
        font-family:cursive;
        color:moccasin;
        text-shadow: 1px 1px 0px black;
        text-indent: 2cm;
        
        
    }
    .picture{
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 35%;
        height: 35%;
       
    }
    
</style>
<body>
    <h1 align="center" class="Title">MATHUR MMDA PARK</h1>
        {% load static %}
       <img src="{% static 'park.jpg' %}"alt="park image" class="picture">
       <p class="content">
        MMDA Park is a well-known urban park located in the <B>Mathur MMDA area of North Chennai</B>. It spans around 2.5 acres and provides a green space for recreation and relaxation.
The park features a skating rink, children’s play area with slides and swings, walking paths, and a meditation hall. It was inaugurated on ,<B>September 21, 2016 </B>, by the <I><B> Chief Minister, J. Jayalalithaa</I></B>, and transformed from a former dump yard into a community space.
The park has morning and evening visiting hours and entry is free of charge. Its walking paths, including pebble-filled and 8-shaped tracks, are popular with joggers. 
A warm-up arena is also available for exercise routines. The Greater Chennai Corporation is currently adding a “sponge park” to prevent urban flooding. This will include rainwater harvesting, a kabaddi court, football pitch, jogging track, and tiered grass seating.</p>
        
</body>
</html>

webpage2.html:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    body{
        background: #7bfbfd;
    }
    .Title{
        font-family:Arial, Helvetica, sans-serif;
        align-items: center;
        letter-spacing: 0.1cm;
    }
    .content{
        width: 100%;
        line-height: 1cm;
        font-size: x-large;
        font-weight:600;
        font-family:serif;
        color:rgba(58, 45, 114, 0.788);
        text-shadow: 1px 1px 0px whitesmoke;
        text-indent: 2cm;
        
    }
    .picture{
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 35%;
        height: 35%;
       
    }
</style>
<body>
        <h1  align="center" class="Title">INDIAN OIL CORPORATION LIMITED Integrated Lube Complex Chennai,Manali</h1>
        {% load static %}
        <img src="{% static 'oil.jpg' %}" alt="image"  class="picture">
        

       <p class="content">
            Indian Oil Corporation Limited’s Integrated Lube Complex in Manali, Chennai, is one of India’s largest and most advanced lubricant production facilities.
            It manufactures a wide range of automotive and industrial lubricants, including greases, base oils, and specialty products, catering to both domestic and international markets.
            The complex is equipped with modern blending, filling, packaging, and quality control systems to ensure high standards. It operates under strict safety and environmental regulations, emphasizing sustainable industrial practices.
            The facility employs skilled professionals across production, engineering, and quality management. Strategically located in North Chennai, it benefits from excellent road and rail connectivity for raw material supply and product distribution.</p>
</body>
</html>
  
webpage3.html:
 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    body{
        background-color:darkmagenta;
    }
    .Title{
        font-family:fantasy;
        align-items: center;
        letter-spacing: 0.2cm;
    }
    .content{
        width: 100%;
        line-height: 1cm;
        font-size: larger;
        font-family:serif;
        color:rgb(45, 228, 238);
        text-shadow: 1px 1px 0px black;
        text-indent: 2cm;
        
    }
    .picture{
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 35%;
        height: 35%;
       
    }
</style>
<body>
     <h1  align="center" class="Title">MANALI PETROCHEMICALS LTD PLANT-1</h1>
        {% load static %}
        <img src="{% static 'petrol1.png' %}"alt="image"  class="picture">
         <p class="content">
            Manali Petrochemicals Ltd (MPL), established in 1986 and located in the Manali Industrial Area of Chennai, operates Plant-I as one of its key production units.
            The plant mainly manufactures propylene oxide and its derivatives such as polyols and propylene glycol. These products are widely used in industries for making polyurethane foams, adhesives, coatings, paints, pharmaceuticals, cosmetics, food products, and insulation materials. 
            By supplying these vital petrochemicals, Plant-I supports major sectors like automotive, construction, furnishing, textiles, and healthcare, making it an important contributor to India’s chemical and industrial growth.</p>
</body>
</html>
  
webpage4.html:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <style>
    body{
        background-color: crimson;
    }
    .Title{
        font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        align-items: center;
        letter-spacing: 0.2cm;
        text-shadow: 1px 1px 4px white;
    }
    .content{
        width: 100%;
        line-height: 1cm;
        font-size: x-large;
        font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
        color:antiquewhite;
        text-indent: 2cm;
        
    }
    .picture{
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 35%;
        height: 35%;
       
    }
</style>
<body>
<h1 align="center" class="Title">PERIYATHOPPU LAKE AND VIEW </h1>
        {% load static %}
        <img src="{% static 'lake.jpg' %}"alt=" image" class="picture">
       <p class="content">
            Periya Thoppu Lake, spread over about 139 acres across the Manali and Madhavaram regions of North Chennai, was once an important waterbody supporting drinking water needs, fishing, and local biodiversity. 
            Over the years, however, it has suffered from severe neglect, with water hyacinth infestation, sewage inflow, and urban encroachments reducing its capacity and ecological health.
             The construction of a road has further split the lake into parts, weakening its flood-holding function. During Cyclone Michaung, this loss of capacity caused heavy flooding in surrounding neighborhoods. Recognizing its importance, the Greater Chennai Corporation and other agencies have proposed restoration projects, including deepening the lake, intercepting sewage, and improving storm-water management, aiming to revive it as a vital ecological and flood-mitigation resource for the city.</p>
</body>
</html>
        
webpage5.html:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>    <style>
    body{
        background-color: rgb(200, 97, 118);
    }
    .Title{
        font-family:'Times New Roman', Times, serif;
        font-weight: bolder; 
        align-items: center;
        letter-spacing: 0.2cm;
        text-shadow: 2px 2px 2px white;
    }
    .content{
        width: 100%;
        line-height: 1cm;
        font-size: x-large;
        font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
        color:rgb(75, 230, 251);
        text-indent: 2cm;
        
    }
    .picture{
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 35%;
        height: 35%;
       
    }
</style>
<body>
    <h1 align="center" class="Title">MANALI, CHENNAI</h1>
        {% load static %}
        <img src="{% static 'manali.jpg' %}"alt=" image"  class="picture">
        

       <p class="content">
            Manali is a northern suburb and industrial township of Chennai, Tamil Nadu, located along the banks of the Kosasthalaiyar River. It is well known as an industrial hub, housing major facilities such as Manali Petrochemicals Ltd, Chennai Petroleum Corporation Ltd (CPCL), and several small and medium chemical industries. The area also has residential neighborhoods, markets, schools, and religious places, making it both an industrial and urban zone. Due to its concentration of industries, Manali plays an important role in Chennai’s economy, but it also faces challenges such as air and water pollution, traffic congestion, and flooding during heavy rains. In recent years, efforts have been taken to improve infrastructure, restore local lakes, and balance industrial growth with environmental and community well-being.</p>
    
</body>
</html>

```
# OUTPUT
![alt text](<Screenshot 2025-09-30 192943.png>)
![alt text](<Screenshot 2025-09-30 192957.png>)
![alt text](<Screenshot 2025-09-30 193032.png>)
![alt text](<Screenshot 2025-09-30 193220.png>)
![alt text](<Screenshot 2025-09-30 193242.png>)
![alt text](<Screenshot 2025-09-30 195835.png>)

# RESULT
The program for implementing image maps using HTML is executed successfully.
