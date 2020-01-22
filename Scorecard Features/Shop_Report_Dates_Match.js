/*
==========
JavaScript
==========
Input A: The user enters the month of the report date. (integer)
Input B: The user enters the month of the shop date.  (integer)
Button: The user clicks on button "Compare".  Triggers event that compares integer values in Input A and Input B.
Output: (boolean logic)  
  If values are true, "Yes" is the auto-response. 
  If values are false, "No" is the auto-response. An alert() is triggered that declares "Months do NOT match!".
*/


<left>
                        <h1>Shop / Report Dates</h1>
                        <h3>Determines if the the shop and report dates are in the same month.</h3>
                        <left>
                        <br>
                        <body>
                        Enter MONTH of Report Date:
                        <br>
                        <input type= "number" id= "report" >
                        <br><br><br>
                        Enter MONTH of Shop Date:
                        <br>
                        <input type= "number" id= "shop" >
                        <br><br><br>
                        <input type= "button" value= "Compare" onclick= "comparison()">
                        <br><br><br>
                        Are the months the same?
                        <br>
                        <input type= "text" id= "resultB">
                        </left>
                    
                        
                <script>
                function comparison() {
                    var date1 = parseInt(document.getElementById("report").value);
                    var date2 = parseInt(document.getElementById("shop").value);
                    var msg;
                    if (date2 != date1) {
                        alert("Months do NOT match!");
                        msg = "No";
                    } else {
                        msg = "Yes";
                    }
                    document.getElementById("resultB").value = msg;

                }
                </script>
