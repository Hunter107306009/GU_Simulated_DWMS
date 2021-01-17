<?php require_once 'connect.php';?>
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
<?php
  $sql="SELECT Transfer_ID,Transferred_ID,Item_ID,Trans_Quantity,Trans_Date,Arrive_Date FROM  trans_record";
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
  align-items:center;
}

.lala{
  height:50px;
  width:1000px;
  border-bottom-style:outset;
}

.haha{
  margin: 10px 55px 10px 55px;
  display: flex;
  padding:10px;
  justify-content:flex-start;
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
  <h2>國內調貨紀錄</h2>
    <div class="show">
      <table>
            <thead>
              <tr>
                <th class="block">訂貨方ID</th>
                <th class="block">收貨方ID</th>
                <th class="block">商品</th>
                <th class="block">訂購量</th>
                <th class="block">訂購日</th>
                <th class="block">收貨日</th>
              </tr>
            </thead>
            <?php if(!empty($datas)):?>
              <?php foreach($datas as $key => $row):?>
            <tbody>
              <tr>
                <td align="center"><?php echo $row['Transfer_ID']; ?></td>
                <td align="center"><?php echo $row['Transferred_ID']; ?></td>
                <td align="center"><?php echo $row['Item_ID']; ?></td>
                <td align="center"><?php echo $row['Trans_Quantity']; ?></td>
                <td align="center"><?php echo $row['Trans_Date']; ?></td>
                <td align="center"><?php echo $row['Arrive_Date']; ?></td>
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
</script>
</html>