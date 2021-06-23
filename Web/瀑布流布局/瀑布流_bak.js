window.onload=function()
{
	imgLocation("container","box");	
	var imgData={"data":[{"src":"1.jpg"},{"src":"2.jpg"},{"src":"3.jpg"},{"src":"4.jpg"},{"src":"5.jpg"}]}
	window.onscroll=function()
	{
		if(checkFlag())
		{
			var cparent=document.getElementById("container");
			for(var i=0;i<5;i++)
			{
				var ccontent=document.createElement("div");
				ccontent.className="box";
				cparent.appendChild(ccontent);
				var boximg=document.createElement("div");
				boximg.className="box_img";
				ccontent.appendChild(boximg);
				var img=document.createElement("img");
				img.src=imgData.data[i].src;
				boximg.appendChild(img);
			}
		}
		imgLocation("container","box");	
	}
}

function checkFlag()
{
	var cparent=document.getElementById("container");
	var ccontent=getChildElement(cparent,"box");
	var lastHeight=ccontent[ccontent.length-1].offsetTop;
	var scrollTop=document.documentElement.scrollTop||document.body.scrollTop;
	var pageHeight=document.documentElement.clientHeight||document.body.clientHeight;
	console.log(lastHeight+";"+scrollTop+";"+pageHeight+";");
	if(lastHeight<(scrollTop+pageHeight))
		return true;
}

function imgLocation(parent,content)
{
	var cparent=document.getElementById(parent);
	var ccontent=getChildElement(cparent,content);
	
	var imgWidth=ccontent[0].offsetWidth;
	
	
	
	var cols=Math.floor(document.documentElement.clientWidth/imgWidth);
	cparent.style.cssText="width:"+imgWidth*cols+"px;margin:0 auto;"
	var boxHeightArr=[];
	for(var i=0;i<ccontent.length;i++)
		{
			if(i<cols)
			{
				boxHeightArr[i]=ccontent[i].offsetHeight;
			}
			else
			{
				var minBoxHeight=Math.min.apply(null,boxHeightArr);
				
				var index=getMinIndex(boxHeightArr,minBoxHeight);
				
				ccontent[i].style.cssText="position:absolute;top:"+minBoxHeight+"px";
				ccontent[i].style.left=ccontent[index].offsetLeft+"px";
				boxHeightArr[index]+=ccontent[i].offsetHeight; 
			}
		}
}

function getMinIndex(boxHeightArr,minBoxHeight)
{
	for(var i=0;i<boxHeightArr.length;i++)
	{
		if(boxHeightArr[i]==minBoxHeight)
			return i;
	}
}

function getChildElement(parent,content)
{
	var contentArr=[];
	var contentAll=parent.getElementsByTagName("*");
	for(var i=0;i<contentAll.length;i++)
	{
		if(contentAll[i].className==content)
			contentArr.push(contentAll[i]);
	}
	return contentArr;
}