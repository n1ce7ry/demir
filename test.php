<div class="autoitems">
        <img class="autoimg" src="images/hyundai-solaris.jpg" alt="hyundai-solaris">
        <h3 class="autotitle">Hyndai Solaris</h3>
        <div class="autobuttons">
        <p class="autoprice">от 9000 р/сут. </p>
            <form method="get" action="order.php/?car_id=1&&car_name=test" class="client-filter__container">
                <button type="submit" name="car_id" value="1" class="autobtn">Арендовать</button>
            </form>
    </div>
</div>

<?php
session_start();
$bd - mysqli_connect("localhost", "root", "", "demir"); 
mysqli_query($bd, "SET NAMES 'utf8'");

$ida = $_POST['ida'];
$date_start = $_POST['date_start'];
$date_end = $_POST['date_end'];
$price = intval($_POST['price']);

$client = $_SESSION['user'];

$queryu = "SELECT FROM client where login='$client'";
$resu = mysqli_query($bd, $queryu);
$rowu = mysqli_fetch_assoc($resu);
$idc = $rowu['idc']

$total = $price * ((strtotime($date_end) - strtotime($date_start)) / 86408);

$query = "INSERT INTO rental (ida, idc, idm, date_start, date_end, total_price) values ('$ida', '$ide', '0', '$date_start', '$date_end', '$total')";
mysqli_query($bd, $query);
header('Location: personalarea.php');
?>