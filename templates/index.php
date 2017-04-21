
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Wiki Search</title>
    <!-- Bootstrap core CSS -->
    <!-- <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css"> -->
    <link rel="stylesheet" href="http://cdn.bootcss.com/twitter-bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="http://cdn.bootcss.com/twitter-bootstrap/3.3.7/css/bootstrap-theme.min.css">


    <style type="text/css">
      #searchbar{

        /*border-top:50px;*/
        padding-top: 50px;
      }
      body {
                /*padding-top: 50px;*/
            }
            .dropdown.dropdown-lg .dropdown-menu {
                margin-top: -1px;
                padding: 6px 20px;
            }
            .input-group-btn .btn-group {
                display: flex !important;
            }
            .btn-group .btn {
                border-radius: 0;
                margin-left: -1px;
            }
            .btn-group .btn:last-child {
                border-top-right-radius: 4px;
                border-bottom-right-radius: 4px;
            }
            .btn-group .form-horizontal .btn[type="submit"] {
              border-top-left-radius: 4px;
              border-bottom-left-radius: 4px;
            }
            .form-horizontal .form-group {
                margin-left: 0;
                margin-right: 0;
            }
            .form-group .form-control:last-child {
                border-top-left-radius: 4px;
                border-bottom-left-radius: 4px;
            }

            @media screen and (min-width: 768px) {
                #adv-search {
                    width: 500px;
                    margin: 0 auto;
                }
                .dropdown.dropdown-lg {
                    position: static !important;
                }
                .dropdown.dropdown-lg .dropdown-menu {
                    min-width: 500px;
                }
            }
            /* Style the tab */
            div.tab {
                overflow: hidden;
                border: 1px solid #ccc;
                background-color: #f1f1f1;
            }

            /* Style the buttons inside the tab */
            div.tab button {
                background-color: inherit;
                float: left;
                border: none;
                outline: none;
                cursor: pointer;
                padding: 14px 16px;
                transition: 0.3s;
            }

            /* Change background color of buttons on hover */
            div.tab button:hover {
                background-color: #ddd;
            }

            /* Create an active/current tablink class */
            div.tab button.active {
                background-color: #ccc;
            }

            /* Style the tab content */
            .tabcontent {
                display: none;
                padding: 6px 12px;
                border: 1px solid #ccc;
                border-top: none;
            }
            .navbar{
              position: fixed;
              width: 100%;
            }
            /*scroll to top*/
            #myBtn {
              display: none;
              position: fixed;
              bottom: 20px;
              right: 30px;
              z-index: 99;
              border: none;
              outline: none;
              background-color: red;
              color: white;
              cursor: pointer;
              padding: 15px;
              border-radius: 10px;
            }

            #myBtn:hover {
              background-color: #555;
            }

    </style>
    <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="http://cdn.bootcss.com/twitter-bootstrap/3.0.1/js/bootstrap.min.js"></script>

    <!-- <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" type='text/javascript'></script> -->
</head>

<body role="document" style="background-image: url(http://wallpapercave.com/wp/hFSZpWV.jpg)">
<!-- <div class="container theme-showcase" role="main"> -->
<!-- add tab -->
<section id="nav">
    <div class="tab navbar">
    <button class="tablinks" onclick="openCity(event, 'London')">Basic</button>
    <button class="tablinks" onclick="openCity(event, 'Paris')">Advanced</button>
    <button class="tablinks" onclick="openCity(event, 'Tokyo')">Custom</button>
    </div>
</section>
<button onclick="topFunction()" id="myBtn" title="Go to top">Top</button>
<section id="searchbar">
<div id="London" class="tabcontent" style=display:block>


    <h1>Wiki Search!</h1>
    <div style="padding: 10px 100px 10px;">
    <form class="bs-example bs-example-form" role="form" action="results" method="post">
      <div class="input-group">
      <span class="input-group-addon">Title</span>
      <input type="text" class="form-control" name="title" placeholder="Title">
      </div>
    <br>
      <div class="input-group">
      <span class="input-group-addon">Ingredient</span>
      <input type="text" class="form-control" name="ingredient" placeholder="Ingredient">
      </div>
    <br>
      <div class="input-group">
      <span class="input-group-addon">Procedure</span>
      <div>
      <input type="text" class="form-control" name="procedure" placeholder="Procedure">
      </div>
      </div>
    <br>
      <div class="input-group">
      <span class="input-group-addon">Category</span>
      <select class="form-control" name="category">
        <option value="default">default</option>
        <option value="comedy">comedy</option>
      </select>
      </div>
    <br>
      <button class="btn btn-primary" type="submit" >Search</button>
    </form>
    </div>




  <div id="Paris" class="tabcontent">
  <h3>Paris</h3>
  <p>Paris is the capital of France.</p>
  </div>

  <div id="Tokyo" class="tabcontent">
  <h3>Tokyo</h3>
  <p>Tokyo is the capital of Japan.</p>
  </div>

</section>
<!-- end of tab -->







     <div class="jumbotron result_num stop_word stop_flag unknown unknown_flag">

      <p><small>About {{result_num}} results</small>

      {% if stop_flag %}
      <small>Ignoring term:
      {% for s in stop_word %}
            {{s}}
      {% endfor %}

      </small>
      {%endif%}

      {% if unknown_flag %}
      <small>Unknown search term:
      {% for s in unknown %}
            {{s}}
      {% endfor %}

      </small>
      {%endif%}

      </p>

       </div>

<section id="footer">
  <p>Some text some text some text some text..</p>
  <p>Some text some text some text some text..</p>
  <p>Some text some text some text some text..</p>
  <p>Some text some text some text some text..</p>
  <p>Some text some text some text some text..</p>
  <p>Some text some text some text some text..</p>
  <p>Some text some text some text some text..</p>
  <p>Some text some text some text some text..</p>
  <p>Some text some text some text some text..</p>
  <p>Some text some text some text some text..</p>
  <p>Some text some text some text some text..</p>
  <p>Some text some text some text some text..</p>
  <p>Some text some text some text some text..</p>
  <p>Some text some text some text some text..</p>
  <p>Some text some text some text some text..</p>
  <p>Some text some text some text some text..</p>
  <p>Some text some text some text some text..</p>
  <p>Some text some text some text some text..</p>
  <p>Some text some text some text some text..</p>
  <p>Some text some text some text some text..</p>
  <span class="copyright" dir="ltr">© 2017 Ti Liang, Jiawen Liang, Hao Wang</span>
</section>


<script type="text/javascript">
      $(function() {
        $('.pagination li a').click(function() {
            dstpage = $(this).data('page');
            if (dstpage == 0)
                return;
            $('#idCurPage').val(dstpage);
            cur = $('#idCurPage').val();
            $('form').submit();
            return false;
        });
    });
    // tab function
    function openCity(evt, cityName) {
        // Declare all variables
        var i, tabcontent, tablinks;

        // Get all elements with class="tabcontent" and hide them
        tabcontent = document.getElementsByClassName("tabcontent");
        for (i = 0; i < tabcontent.length; i++) {
            tabcontent[i].style.display = "none";
        }

        // Get all elements with class="tablinks" and remove the class "active"
        tablinks = document.getElementsByClassName("tablinks");
        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }

        // Show the current tab, and add an "active" class to the button that opened the tab
        document.getElementById(cityName).style.display = "block";
        evt.currentTarget.className += " active";
    }

    // When the user scrolls down 20px from the top of the document, show the button
    window.onscroll = function() {scrollFunction()};

    function scrollFunction() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            document.getElementById("myBtn").style.display = "block";
        } else {
            document.getElementById("myBtn").style.display = "none";
        }
    }

    // When the user clicks on the button, scroll to the top of the document
    function topFunction() {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
    }
</script>
</body>
</html>
