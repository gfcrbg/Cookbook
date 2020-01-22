/*

Input (text1): text that contains '?'
Trigger (button): User clicks on button "Convert"
Output (text2): '?' is replaced with '"'

*/

----------------------------------------
Scorecard version
----------------------------------------


<left>
<h1>Question Mark Converter</h1>
<br>                            
<b>1.</b> PASTE affected text into textbox.
<br>
<b>2.</b> CLICK "Convert" button.
<br>
<b>3.</b> Converted text appears in textbox. 
<br><br>
<b>NOTE:</b> This will turn ALL question marks into quotations.
<br>
<left>
<br>
Paste text:
<br>
<textarea rows= "7" cols= "50" id= "original"></textarea>
<br><br><br>
<button type="button" onclick="Pegasus()">Convert</button>
<br><br>
</left>
<br><br>
<script>
function Pegasus() {
var text1 = document.getElementById("original").value;
var text2 = text1.replace(/\?/g, '"');
document.getElementById("original").value= text2;
}
</script>


----------------------------------------
Browser version
----------------------------------------


<!DOCTYPE html>
<htmL>
    <font style= "color: white">
    <body style= "background-color:#000000">
<font style= "color: white">
                            <left>
                            <h1>Question Mark Converter</h1>
                            
                            <pre>1. PASTE affected text into textbox.</pre>
                            <pre>2. CLICK "Convert" button.</pre>
                            <pre>3. Converted text appears in textbox. </pre>
<pre>NOTE: This will turn ALL question marks into quotations.</pre>
                            <br>
                            <left>
                            <br>
                            <body>
                            Paste text:
                            <br>
                            <textarea rows= "7" cols= "50" id= "original"></textarea>
                            <br><br><br>
                            <button type="button" onclick="Pegasus()">Convert</button>
                            <br><br>
                            </left>
                        
                            <br>
                            <br>
                
                    <script>
                    function Pegasus() {
                        var text1 = document.getElementById("original").value;
                        var text2 = text1.replace(/\?/g, '"');
                        document.getElementById("original").value= text2;
                    }
                    </script>

        </font>
    </body>
</htmL> 
