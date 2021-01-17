<?php require_once 'connect.php';?>
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.1.6/Chart.bundle.min.js"></script>
<?php
  $sql="SELECT Q1,Q2,Q3,Q4,Q5,Q6 FROM  questionnaire_end limit 5";
  $result = mysqli_query($link, $sql);

  if ($result)
  {
    if (mysqli_num_rows($result) > 0)
    {
      while ($row = mysqli_fetch_assoc($result))
      {
        /*將查詢結果輪番存入陣列中*/
        $datas[] = $row;
      }
    }
    mysqli_free_result($result);
  }

  else
  {
    echo "{$sql} 語法執行失敗，錯誤訊息：" . mysqli_error($link);
  }

  /*檢視SQL查詢狀況*/
  if (!empty($datas))
  {
    foreach($datas as $key => $row)
      $Q1=$row['Q1'];
      $Q2=$row['Q2'];
      $Q3=$row['Q3'];
      $Q4=$row['Q4'];
      $Q5=$row['Q5'];
      $Q6=$row['Q6'];
  }
            
  else
  {
    echo "查無資料";
  }
?>
<style>
body {
  font-family: "Lato", sans-serif;
}

.sidenav {
  height: 100%;
  width: 220px;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: #111;
  overflow-x: hidden;
  padding-top: 20px;
}

.sidenav a {
  padding: 6px 8px 6px 16px;
  text-decoration: none;
  font-size: 25px;
  color: #818181;
  display: block;
}

.sidenav a:hover {
  color: #f1f1f1;
  cursor: pointer;
}

.main {
  margin-left: 220px; /* Same as the width of the sidenav */
  font-size: 28px; /* Increased text to enable scrolling */
  padding: 0px 10px;
}

.show{
  
  display:flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.show_wrap{
  display:flex;
  justify-content:center;
  align-items:center;
  border-bottom:2px solid
}

.show_wrap2{
  display:flex;
  justify-content:center;
  align-items:center;
}

.block{
  color:white;
  background:black;
  margin: 10px 55px 10px 55px;
  display: flex;
  padding:10px;
  justify-content:center;
  align-items:center;
  border-radius:10px;
}

.answer_wrap{
  display:flex;
  justify-content:center;
  align-items:center;
}

.answer{
  font-size:25px;
  width:700px;
  height:80px;
  background-color:#E0E0E0;
  margin:10px;
  border-radius:10px;
  padding:8px;
}

.range{
  font-weight:bold;
  font-size:24px;
}

.haha{
  margin: 10px 85px 10px 85px;
  display: flex;
  padding:10px;
  justify-content:center;
  align-items:center;
  border-radius:10px;
}


@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
</style>
</head>
<body>

<script>

</script>

<div class="sidenav">
  <a id="BTN1">客製化推薦紀錄</a>
  <a id="BTN2">問券反饋</a>
  <a id="BTN3">海外訂貨紀錄</a>
  <a id="BTN4">國內調貨紀錄</a>
  <a id="BTN5">推薦促銷門市</a>
  <a id="BTN6">廣告成效</a>
</div>

<div class="main">
  <h2>問券結果</h2>
    <div class="show">
      <canvas id="myChart" width="400" height="100"></canvas>
      <div class="show_wrap">
        <div class="block" style="position:absolute;left:275px;">質料</div>
        <div class="block" style="position:absolute;left:475px;">價格</div>
        <div class="block" style="position:absolute;left:675px;">設計感</div>
        <div class="block" style="position:absolute;left:865px;">修飾身材</div>
        <div class="block" style="position:absolute;left:1065px;">剪裁品質</div>
        <div class="block" style="position:absolute;left:1300px;">配色</div>
      </div>
</div>

   
</body>

</script>
<script>
    let BTN1 = document.getElementById('BTN1');
    BTN1.addEventListener('click', function() 
    {
      location.href="客製化推薦.php?page_count=1"
    });
    let BTN2 = document.getElementById('BTN2');
    BTN2.addEventListener('click', function() 
    {
      location.href="問卷結果.php"
    });
    let BTN3 = document.getElementById('BTN3');
    BTN3.addEventListener('click', function() 
    {
      location.href="海外訂貨.php"
    });
    let BTN4 = document.getElementById('BTN4');
    BTN4.addEventListener('click', function() 
    {
      location.href="國內調貨.php"
    });
    let BTN5 = document.getElementById('BTN5');
    BTN5.addEventListener('click', function() 
    {
      location.href="促銷推薦.php"
    });
    let BTN6 = document.getElementById('BTN6');
    BTN6.addEventListener('click', function() 
    {
      location.href="廣告成效.php"
    });

    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# 本問券結果已透過LTV加權',
            data: [<?php echo $Q1?>,<?php echo $Q2?>,<?php echo $Q3?>,<?php echo $Q4?>,<?php echo $Q5?>,<?php echo $Q6?>],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
      options: {
          scales: {
              yAxes: [{
                  ticks: {
                      beginAtZero: true
                  }
              }]
          }
      }
  });
</script>

</script>
</html> 
