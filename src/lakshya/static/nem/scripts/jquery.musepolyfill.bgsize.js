/*
 ADOBE CONFIDENTIAL
 ___________________

 Copyright 2011 Adobe Systems Incorporated
 All Rights Reserved.

 NOTICE:  All information contained herein is, and remains
 the property of Adobe Systems Incorporated and its suppliers,
 if any.  The intellectual and technical concepts contained
 herein are proprietary to Adobe Systems Incorporated and its
 suppliers and may be covered by U.S. and Foreign Patents,
 patents in process, and are protected by trade secret or copyright law.
 Dissemination of this information or reproduction of this material
 is strictly forbidden unless prior written permission is obtained
 from Adobe Systems Incorporated.
*/
(function(a){function b(a){var b=a.css("background-image");a.css("background-image","");var c=a.css("background-image");b!=c&&a.css("background-image",b);return c.replace(/^\s*url\(\"?/,"").replace(/['"]?\)$/,"")}if(!Muse.Browser.Features.checkCSSFeature("background-size")){var c=function(c){var d=a(c),f=b(d),i=document.createElement("img"),k=document.createElement("div"),l=this,m=!1,o=!1,p=!0,r={};a(k).css({overflow:"hidden",position:"absolute",top:"0px",left:"0px",width:c.clientWidth+"px",height:c.clientHeight+
"px",marginBottom:"-"+c.clientHeight+"px",marginRight:"-"+c.clientWidth+"px",zIndex:"-1"}).addClass("museBgSizePolyfill");i.src=f;i.alt="";i.style.position="absolute";k.appendChild(i);c.children.length>0?c.insertBefore(k,c.children[0]):c.appendChild(k);if(c===document.body)d=a("html"),c=d.get(0),f=b(d),i.src=f,d.css("background-attachment")=="fixed"?(k.style.position="fixed",p=!1):k.style.position="absolute";else if(d.is("#page"))d.css("marginLeft").toLowerCase()=="auto"&&(o=!0),k.style.top=d.offset().top+
parseInt(d.css("borderTopWidth"))+"px",k.style.bottom=parseInt(d.parent().css("paddingBottom"))+parseInt(d.css("borderBottomWidth"))+"px",k.style.left=d.offset().left+parseInt(d.css("borderLeftWidth"))+"px",k.style.right=d.offset().left+parseInt(d.css("borderRightWidth"))+"px",k.style.zIndex=0;else if(d.css("position")=="static")c.style.position="relative";this.reloadImage=function(){var a=b(d),f=d.css("background-color");if(a!=i.src)i.src=a;c.style.backgroundImage="none";c.style.backgroundColor=
"transparent";k.style.backgroundColor=f;a=(d.css("background-position-x")+" "+d.css("background-position-y")).replace(/^\s+/,"").replace(/\s+$/,"").split(/\s+/);a.length==1&&a[0].indexOf("center")>=0&&a.push("center");for(var f=0,j=a.length;f<j;f++)switch(a[f]){case "center":case "50%":f==0?(i.style.right="",i.style.left="50%",i.style.marginLeft="-"+Math.ceil(i.offsetWidth/2)+"px"):(i.style.bottom="",i.style.top="50%",i.style.marginTop="-"+Math.ceil(i.offsetHeight/2)+"px");break;case "left":i.style.right=
"";i.style.left="0px";i.style.marginLeft="0px";break;case "right":i.style.left="";i.style.right="0px";i.style.marginLeft="0px";break;case "top":i.style.bottom="";i.style.top="0px";i.style.marginTop="0px";break;case "bottom":i.style.top="";i.style.bottom="0px";i.style.marginTop="0px";break;default:f==0?(i.style.left=a[f],i.style.marginLeft="-"+Math.ceil(i.offsetWidth/2)+"px"):(i.style.top=a[f],i.style.marginTop="-"+Math.ceil(i.offsetHeight/2)+"px")}};this.resizeImage=function(a){var b=c.getBoundingClientRect(),
f=c.scrollWidth-(Muse.Browser.Bugs.ScrollWidthHeightIncludesBorder?b.right-b.left-d.innerWidth():0),b=c.scrollHeight-(Muse.Browser.Bugs.ScrollWidthHeightIncludesBorder?b.bottom-b.top-d.innerHeight():0),f=!p?c.clientWidth:Math.max(f,c.clientWidth),b=!p?c.clientHeight:Math.max(b,c.clientHeight);!r[i.src]&&i.clientWidth&&(r[i.src]={width:i.clientWidth,height:i.clientHeight});var j=f/(r[i.src]?r[i.src].width:1),l=b/(r[i.src]?r[i.src].height:1);k.style.height=b+"px";k.style.marginBottom="-"+b+"px";k.style.width=
f+"px";k.style.marginRight="-"+f+"px";j<l==a?(i.style.height=b+1+"px",i.style.width="auto"):(i.style.width=f+1+"px",i.style.height="auto")};this.update=function(){if(m){c.style.backgroundImage="";d.css("background-color","");var a=d.css("background-image").toLowerCase(),b=(c.currentStyle||window.getComputedStyle(c,null))["background-size"];b&&b.toLowerCase();if(a!="none"&&(b=="cover"||b=="contain")){if(l.reloadImage(),k.style.display="block",k.style.width="0px",k.style.height="0px",l.resizeImage(b==
"cover"),o)k.style.left=d.offset().left+parseInt(d.css("borderLeftWidth"))+"px",k.style.right=d.offset().left+parseInt(d.css("borderRightWidth"))+"px"}else k.style.display="none"}};if(i.complete||f=="none")m=!0;else a(i).one("load",function(){m=!0;l.update()});this.update()},d=[];a(".museBGSize").each(function(){var b=new c(this);this!==document.body?d.push(b):(a(window).resize(function(){setTimeout(function(){b.update()},10)}),a(window).load(function(){setTimeout(function(){b.update()},10)}))});
var f=d.length;f>0&&setInterval(function(){for(var a=0;a<f;a++)d[a].update()},Math.max(120,16*f))}})(jQuery);
