window.onload=function()
{
	imgLocation("content","box");
	
}

function imgLocation(parent,content)
{
	var cparent=document.getElementById(parent);
	var ccontent=getChildElement(cparent,content);
	var imgWidth=ccontent[0].offsetWidth;
	var cols=Math.floor(document.documentElement.clientWidth/imgWidth);
	cparent.style.cssText="width:"+cols*imgWidth+"px";
	var boxHeightArr=[];
	for(var i=0;i<ccontent.length;i++)
	{	
		if(i<cols)
		{
			boxHeightArr[i]=ccontent[i].offsetHeight;
		}
		else
		{
			var minHeight=Math.min.apply(null,boxHeightArr);
			console.log(minHeight);
			var index=getminHeightIndex(boxHeightArr,minHeight);
			ccontent[i].style.cssText="position:absolute;top:"+minHeight+"px";
			ccontent[i].style.left=ccontent[index].offsetLeft+"px";
			boxHeightArr[index]+=ccontent[i].offsetHeight;
			console.log(index);
		}	
	}
}
function getminHeightIndex(boxHeightArr,minHeight)
{
	for(var i=0;i<boxHeightArr.length;i++)
	{
		if(boxHeightArr[i]==minHeight)
		{
			return i;
		}
	}	
}
function getChildElement(parent,content)
{
	var contentArr=[];
	var allcontent=parent.getElementsByTagName("*");
	for(var i=0;i<allcontent.length;i++)
	{
		if(allcontent[i].className==content)
			contentArr.push(allcontent[i]);
	}
	return contentArr;
}