
<script>

Date.prototype.getWeekNumber = function(){
  
var d = new Date(Date.UTC(this.getFullYear(), this.getMonth(), this.getDate()));
  
var dayNum = d.getUTCDay() || 7;
  
d.setUTCDate(d.getUTCDate() + 4 - dayNum);
  var yearStart = new Date(Date.UTC(d.getUTCFullYear(),0,1));
  return Math.ceil((((d - yearStart) / 86400000) + 1)/7)

};
function checkWeek() {
  
var s = document.getElementById('dString').value;
  
var m = moment(s, 'MM-DD-YYYY');
  
document.getElementById('momentWeek').value = m.format('W');
  
document.getElementById('answerWeek').value = m.toDate().getWeekNumber();      

}    

</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.18.1/moment.min.js"></script>

Enter Shop date MM-DD-YYYY:
<br> 
<input id="dString" value="" onchange= "checkWeek(this)"><br>
<hidden Moment:></hidden> 
<br>
<hidden input id="momentWeek" readonly>
Week #: 
<br>
<input id="answerWeek" readonly>
