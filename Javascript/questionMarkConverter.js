/*

Input (text1): text that contains '?'
Trigger (button): User clicks on button "Convert"
Output (text2): '?' is replaced with '"'

*/

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
