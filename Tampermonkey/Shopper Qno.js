// ==UserScript==
// @name           Shopper Qno
// @namespace      bbby.org
// @description    displays Qno next to shopper inputs
// @include        *ShopReview-Right.php*
// ==/UserScript==

var ins = document.getElementsByTagName('input');
var qno, last;
for(i=0;i<ins.length;i++)
{
	if(ins[i].type != 'hidden' && ins[i].type != 'button' && ins[i].type != 'submit')
	{
		qno = document.createElement('SPAN');
		qno.style.color='red';
		if(last!=ins[i].name)
		{
			last = qno.innerHTML = ins[i].name;
			ins[i].parentNode.insertBefore(qno , ins[i].parentNode.firstChild);
		}
	}
}


ins = document.getElementsByTagName('textarea');
for(i=0;i<ins.length;i++)
{
		qno = document.createElement('SPAN');
		qno.style.color='red';
		qno.innerHTML = ins[i].name;
		ins[i].parentNode.insertBefore(qno , ins[i].parentNode.firstChild);
}
