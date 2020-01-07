/*
==========
JavaScript
==========
The user clicks on button.  
The button triggers an event that scrolls the user to a configured location on the page.
*/


Test scrollIntoView
<br>
<br>
<button type="button" onclick="wootA()">Narrative / Text</button>
<br>
<br>
<button type="button" onclick="wootB()">Mulitcheck</button>
<br>
<br>

<script>
function wootA() {
  var meh = document.getElementById("bleh");
  meh.scrollIntoView();
}
function wootB() {
  var meh = document.getElementById("boo");
  meh.scrollIntoView();
}
</script>
