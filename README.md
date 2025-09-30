# Ex04 Places Around Me
# Date:
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



```
# OUTPUT
# RESULT
The program for implementing image maps using HTML is executed successfully.
