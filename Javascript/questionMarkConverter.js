/*

Input (text1): text that contains '?'
Trigger (button): User clicks on button "Convert"
Output (text2): '?' is replaced with '"'

*/

<!DOCTYPE html>
<htmL>
    <font style= "color: white">
    <body style= "background-color:#000000">
<font style= "color: white">
                            <left>
                            <h1>Question Mark Converter</h1>
                            
                            <pre>1. PASTE affected text into A..</pre>
                            <pre>2. CLICK "Convert" button.</pre>
                            <pre>3. Modified text appears in B. </pre>
<pre>NOTE: This will turn ALL question marks into quotations.</pre>
                            <br>
                            <left>
                            <br>
                            <body>
                            A) Paste text:
                            <br>
                            <textarea rows= "7" cols= "50" id= "original"></textarea>
                            <br><br><br>
                            <button onclick="Pegasus()">Convert</button>
                            <br><br><br>
                            B) Modified text:
                            <br>
                            <textarea rows= "7" cols= "50" id= "conversion"></textarea>
                            </left>
                        
                        <br>
                        <br>
                
                <script>
                    function Pegasus() {
                        var text1 = document.getElementById("original").value;
                        var text2 = text1.replace(/\?/g, '"');
                        document.getElementById("conversion").value= text2;
                    }
                    </script>

        </font>
    </body>
</htmL> 
