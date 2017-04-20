
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
      body {
    padding-top: 50px;
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



    </style>
<script src="https://code.jquery.com/jquery-1.10.2.min.js"></script> 
    <script src="http://cdn.bootcss.com/twitter-bootstrap/3.0.1/js/bootstrap.min.js"></script>

    <!-- <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" type='text/javascript'></script> -->
</head>

<body role="document">



 




    <div class="container theme-showcase" role="main">
     

      <div class="jumbotron">
       <h1>Wiki Search!</h1>
       
         
       <div style="padding: 10px 100px 10px;">
  <form class="bs-example bs-example-form" role="form" action="results" method="post">
    <div class="input-group">
      <span class="input-group-addon">query</span>
      <input type="text" class="form-control" name="inputValue">
    </div>
    <br>
    <div class="input-group">
      <span class="input-group-addon">starring</span>
      <input type="text" class="form-control" name="starValue">
    </div>
    <br>
    <div class="input-group">
      <span class="input-group-addon">runtime</span>
      <div>
      <input type="text" class="form-control" name="runValue1">
      <input type="text" class="form-control" name="runValue2">
      </div>
    </div>
    <br>
    <div class="input-group">
      <select class="form-control" name="genreValue">
              <option value="default">default</option>
              <option value="comedy">comedy</option>
              <option value="romance">romance</option>
              <option value="thriller">thriller</option>
              <option value="mystery">mystery</option>
              <option value="crime">crime</option>
              <option value="drama">drama</option>
              <option value="musical">musical</option>
              <option value="documentary">documentary</option>
              <option value="western">western</option>
              <option value="animation">animation</option>
            </select>
    </div>
    <br>
    <button class="btn btn-primary" type="submit" >Search</button> 
  </form>
</div>
     
      <div class="container">
  <div class="row">
    <div class="col-md-12">
            <div class="input-group" id="adv-search">
                <input type="text" class="form-control" placeholder="Search for snippets" />
                <div class="input-group-btn">
                    <div class="btn-group" role="group">
                        <div class="dropdown dropdown-lg">
                            <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-expanded="false"><span class="caret"></span></button>
                            <div class="dropdown-menu dropdown-menu-right" role="menu">
                                <form class="form-horizontal" role="form">
                                  <div class="form-group">
                                    <label for="filter">Filter by</label>
                                    <select class="form-control">
                                        <option value="0" selected>All Snippets</option>
                                        <option value="1">Featured</option>
                                        <option value="2">Most popular</option>
                                        <option value="3">Top rated</option>
                                        <option value="4">Most commented</option>
                                    </select>
                                  </div>
                                  <div class="form-group">
                                    <label for="contain">Author</label>
                                    <input class="form-control" type="text" />
                                  </div>
                                  <div class="form-group">
                                    <label for="contain">Contains the words</label>
                                    <input class="form-control" type="text" />
                                  </div>
                                  <button type="submit" class="btn btn-primary"><span class="glyphicon glyphicon-search" aria-hidden="true"></span></button>
                                </form>
                            </div>
                        </div>
                        <button type="button" class="btn btn-primary"><span class="glyphicon glyphicon-search" aria-hidden="true"></span></button>
                    </div>
                </div>
            </div>
          </div>
        </div>
  </div>
</div>
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
       <form action="showarticle.php" method="get">
      <!-- <table class="table table-striped table-bordered table-hover result stop_word">
        <tbody>
        {% for res in result %}
        <tr><td>
        
            <p><strong>{{res[11]}}. {{res[0]}}({{res[12]}})</strong></p>

            <p>{{res[1]}}
            </p>

          <form name="mydetail" action="detail" method="post"><input name="inputDetail" type="hidden" value="{{ res[11] }}">
          <button class="btn btn-primary" type="submit" >See the details</button>
          </form>

          </td></tr>
          
          {% endfor %}
          
        </tbody>
      </table>
       </form> 
      
        <ul class="pager result_page">
        <li>
            <a>next</a>
            <form action="jump_next" name="search" method="post">
              <input type="hidden", value="Next">
              <button class="next" type="submit">sdf</button>
            </form>
        </li>
        <li>
        <a>previous</a>
            <form action="jump_prev" name="search" method="post">
              <input type="hidden", value="Prev">
              <button class="previous" type="submit">fds</button>
            </form>
            </li>
          </ul>
          <form action="jump_prev" name="PPrev" id="PPrev" method="post">
              <input type="hidden", value="Prev">
              
          </form>
          <form action="jump_next" name="NNext" id="NNext" method="post">
              <input type="hidden", value="Next">
             
            </form>

          <ul class="pager">
            <li class="previous">
            <a href='javascript:my_submit("PPrev")'>Prev</a>
            </li>
            <li class="next">
            <a href='javascript:my_submit("NNext")'>Next</a>
            </li>
        </ul>
      </div>        
    </div>   -->


    <!-- /container -->
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    
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
    </script>
</body>
</html>
