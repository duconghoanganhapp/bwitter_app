<?php
if(isset($_POST['signup']))
{
$servername = "localhost";
$username = "root";
$password = "root";
$database = "facebook_project";
// Create connection
$connect = new mysqli($servername, $username, $password, $database, 8889);
// Check connection
if ($connect->connect_error) {
    die("Connection failed: " . $connect->connect_error);
}
	
	$Email=$_POST['email'];

	$que1=$connect->query("select * from users where Email='$Email'");
	$count1 = $que1->num_rows;

	if($count1>0)
	{
		echo "<script>
				alert('There is an existing account associated with this email.');
			</script>";
	}
	else
	{
		$Name=$_POST['first_name'].' '.$_POST['last_name'];
		$Password=$_POST['password'];
		$Gender=$_POST['sex'];
		$Birthday_Date=$_POST['day'].'-'.$_POST['month'].'-'.$_POST['year'];
		$FB_Join_Date=$_POST['fb_join_time'];
		
		$day=intval($_POST['day']);
		$month=intval($_POST['month']);
		$year=intval($_POST['year']);
		if(checkdate($month,$day,$year))
		{
			$que2=$connect->query("insert into users(Name,Email,Password,Gender,Birthday_Date,FB_Join_Date) values('$Name','$Email','$Password','$Gender','$Birthday_Date','$FB_Join_Date')");

			session_start();
			$_SESSION['tempfbuser']=$Email;
		
		
			if($Gender=="Male")
			{
				header("location:fb_files/fb_step/fb_step1/Step1_Male.php");
			}
			else
			{
				header("location:fb_files/fb_step/fb_step1/Step1_Female.php");
			}
		}
		else
		{
			echo "<script>
				alert('The selected date is not valid.');
			</script>";
		}
	}
}
?>
