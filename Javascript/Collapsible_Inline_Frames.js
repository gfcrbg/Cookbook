/*
==========
JavaScript
==========
The user clicks on button.
The button triggers an event that expands an inline frame.

The user clicks on the same button.
The button triggers an event that collapses the expanded inline frame.
*/

<h2>Collapsible Inline Frames</h2>


<style>
#formA {
display: none;
}
#formB {
display: none;
}
</style>

<button type="button" onclick="showIssueTrackerA();">QA Issue Tracker A</button>
<br>
<br>
<iframe id="formA" src="https://docs.google.com/forms/d/e/1FAIpQLSf6mngBFYbMv1H5bbMmZUHtZMX6gZQjLjGaAcU7i71LNB37mQ/viewform?embedded=true" width="640" height="964" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
<br>
<button type="button" onclick="showIssueTrackerB();">QA Scoring Mailer Form</button>
<br>
<br>
<iframe id="formB" src="https://docs.google.com/forms/d/e/1FAIpQLScuShvq-etj7a_snl8IYcWRxfaFUE30CsG7jJ0OxxIxnHmOsQ/viewform?embedded=true" width="640" height="2200" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>



<script type="text/javascript">
function showIssueTrackerA() {
var x = document.getElementById('formA');
if (x.style.display === "none"){
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
function showIssueTrackerB() {
var y = document.getElementById('formB');
if (y.style.display === "none"){
    y.style.display = "block";
  } else {
    y.style.display = "none";
  }
}
</script>










