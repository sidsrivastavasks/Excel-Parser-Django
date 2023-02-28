# Excel-Parser-Django

## Run the Deployed App

Click here to see the hosted URL [https://my-django-project.onrender.com/excel](https://my-django-project.onrender.com/excel)

<hr>
<br>

### It is a Django based Application.

<br>

### It accepts an Excel(.xls and xlsx) Files from user in this format

| Product Name | Variation  | Stock |
| ------------ | ---------- | ----- |
| iPhone       | Blue-64 GB | 50    |
| Oneplus      | Nord       | 10    |

<br>
<br>

### After Proving the user Input, It gets added to the database, and User can see in this way

| SL.No | Name   | Lowest Price | Variations & Stocks                                                                                                                  | Last Updated              |
| ----- | ------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------- |
| 1     | iPhone | 49000        | <table> <thead> <tr> <th>Variation</th> <th>Stock</th> </tr> </thead> <tbody> <tr> <td>Blue-64 GB</td> <td>50</td> </tbody> </table> | 21st May 2021 8:06 PM UTC |

<br>

## Database Models

<hr>

## For our Database I'm using PostgreSql. Our database includes Product and Product Variation Model.

### Product

```
Name,
lowest_price,
last_updated
```

<hr>

### ProductVariation

```
product,
variation_text,
stock,
last_updated
```

## Endpoints

#### First Endpoint

```
1 - I'm using `/excel` for my base url.
```

### The above endpoint is used to render the Django template to show the data to the user. It also have a form that accepts the File from user.

<br>

### The template includes -

```
Search by Product Name
Sorting based on - SL.NO, Name, Lowest Price, and Last_updated Columns
Pagination
```

<br>

#### Second Endpoint

```
2- /excel/add-product
```

#### This endpoint is a POST request that accepts a File input from the user and add the data to the database.

### Here are some screen shots of the website

![image](https://user-images.githubusercontent.com/55981532/221781328-ce2833b7-8bb1-49e1-94e5-dfda35262a45.png)
![image](https://user-images.githubusercontent.com/55981532/221781391-01ee79d8-8aa8-4c1a-951c-4c12b4fb9f50.png)
![image](https://user-images.githubusercontent.com/55981532/221781562-772dd664-86c9-4cc1-a631-63178996dfa3.png)
![image](https://user-images.githubusercontent.com/55981532/221781703-dd2d6e84-7cad-4921-9fa8-dc5ff85856fe.png)




