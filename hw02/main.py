<html lang="en">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>Document</title>
<script type="text/javascript">
function getValue() {

var inputNum = document.getElementById("d1").value;
var d2 = document.getElementById("d2");
            
var tab = "<table border='1' >";
                
for (var i = 1; i <= inputNum; i++) {
tab += "<tr>";
                   
for (var j = 1; j <= inputNum; j++) {
tab +=
"<td style='background-color:rgb(86, 220, 30);width:80px;height:80px;margin:10px;'></td>";
}
tab += "</tr>";
}
tab += "</table>"
d2.innerHTML = tab;
            
}
</script>
</head>

<body>

<input type="text" id="d1" placeholder="输入数字1-9">
<input type="button" value="点击生成表格" onclick="getValue()">
<div id="d2" ></div>

</body>

</html>
