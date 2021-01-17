<?php require_once 'connect.php';?>
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
<?php
  $page_count=$_GET['page_count'];
  $page=($page_count-1)*10+1;
  $sql="SELECT USER_Name,Recommendation_Content,Customized_Time FROM customized_recommendation limit ".strval($page). ",10";
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
  {/*不做出反應*/}
            
  else
  {
    echo "查無資料";
  }
?>
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

.block{
  color:white;
  background:black;
  padding:10px;
  border-radius:10px;
}

.show_wrap2{
  display:flex;
  justify-content:center;
  align-items:center;
}

.haha{
  margin: 10px 55px 10px 55px;
  display: flex;
  padding:10px;
  justify-content:center;
  align-items:center;
  border-radius:10px;
}

table{
    padding:10px;
    background-color:#eee;
    border:1px solid black;
    width:1100px;
}

td{
    border:50px;
}

.T_wrap{
  display:flex;
  justify-content: flex-end;
  margin-right:130px;
}

#T2 {
border-top: 15px solid white;
border-bottom: 15px solid white;
border-left: 25px solid black;
display:inline-block;
margin-right:10px;
}

#T4 {
  border-top: 15px solid white;
  border-bottom: 15px solid white;
  border-right: 25px solid black;
  display:inline-block;
  margin-left:10px;
}

#T2:hover {
  cursor: pointer;
}

#T4:hover {
  cursor: pointer;
}

.page_id{
  margin-right:30px;
  margin-left:30px;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
</style>
</head>
<body>

<div class="sidenav">
  <a id="BTN1">客製化推薦紀錄</a>
  <a id="BTN2">問券反饋</a>
  <a id="BTN3">海外訂貨紀錄</a>
  <a id="BTN4">國內調貨紀錄</a>
  <a id="BTN5">推薦促銷門市</a>
  <a id="BTN6">廣告成效</a>
</div>

<div class="main">
  <h2>客製化推薦紀錄</h2>
  <div class="T_wrap">
    <div id="T2"></div>
    <div class="page_id">第<?php echo $page_count;?>頁</div>
    <div id="T4"></div>
  </div>
    <div class="show">

          <table>
            <thead>
              <tr>
                <th class="block">會員姓名</th>
                <th class="block">推薦優惠</th>
                <th class="block">推薦時間</th>
              </tr>
            </thead>
            <?php if(!empty($datas)):?>
              <?php foreach($datas as $key => $row):?>
            <tbody>
              <tr>
                <td align="center"><?php echo $row['USER_Name'];?></td>
                <td align="center"><?php echo $row['Recommendation_Content'];?></td>
                <td align="center"><?php echo $row['Customized_Time'];?></td>
              </tr>
            </tbody>
            <?php endforeach; ?></br>
        <?php else: ?>
        查無資料
        <?php endif; ?>
          </table>

          
      </div>
</div>
   
</body>
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
    let right = document.getElementById('T2');
    right.addEventListener('click', function() 
    {
      let page_count = <?php echo $page_count ?>;
      if(page_count<400)
      {
        location.href="客製化推薦.php?page_count="+String(page_count+1);
      }
      else
      {
        alert("這是最後一頁");
      }
    });
    let left = document.getElementById('T4');
    left.addEventListener('click', function() 
    {
      let page_count = <?php echo $page_count ?>;
      if(page_count>1)
      {
        location.href="客製化推薦.php?page_count="+String(page_count-1);
      }
      else
      {
        alert("這已經是第一頁了");
       }
    });
</script>
</html>