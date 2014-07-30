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
(function(a){a.fn.museOverlay=function(b){var c=a.extend({autoOpen:!0,offsetLeft:0,offsetTop:0,$overlaySlice:a(),$overlayWedge:a(),duration:300,overlayExtraWidth:0,overlayExtraHeight:0},b);return this.each(function(){var d=a(this).data("museOverlay");if(d&&d[b]!==void 0)return d[b].apply(this,Array.prototype.slice.call(arguments,1));var f=a("<div></div>").appendTo("body").css({position:"absolute",top:0,left:0,zIndex:100001}).hide(),g=a("<div></div>").append(c.$overlaySlice).appendTo(f).css({position:"absolute",
top:0,left:0}),h=a(this).css({position:"absolute",left:0,top:0}).appendTo(f),i=a(window),j,k,l=null,m={isOpen:!1,open:function(){if(!m.isOpen)j=i.width(),k=i.height(),m.positionContent(j,k),f.show(),g.bind("click",m.close),g.css({opacity:0}).stop(!0),h.css({opacity:0}).stop(!0),g.bind("click",m.close).animate({opacity:0.99},{queue:!1,duration:c.duration,complete:function(){g.css({opacity:""});h.animate({opacity:1},{queue:!1,duration:c.duration,complete:function(){h.css({opacity:""})}})}}),a(document).bind("keydown",
m.onKeyDown),m.doLayout(),m.isOpen=!0,i.bind("resize",m.onWindowResize)},close:function(){a(".Container",h).each(function(){Muse.Utils.detachIframesAndObjectsToPauseMedia(a(this))});g.unbind("click",m.close);i.unbind("resize",m.onWindowResize);a(document).unbind("keydown",m.onKeyDown);if(c.onClose)c.onClose();g.css({opacity:0.99}).stop(!0);h.css({opacity:0.99}).stop(!0);h.animate({opacity:0},{queue:!1,duration:c.duration,complete:function(){g.animate({opacity:0},{queue:!1,duration:c.duration,complete:function(){f.hide();
h.css({opacity:""});g.css({opacity:""})}})}});m.isOpen=!1},onKeyDown:function(a){a.keyCode===27&&m.close()},onWindowResize:function(){var a=i.width(),b=i.height();(j!=a||k!=b)&&l==null&&(l=setTimeout(function(){j=i.width();k=i.height();m.positionContent(j,k);m.doLayout();l=null},10))},doLayout:function(){f.css({width:0,height:0});c.$overlayWedge.css({width:0,height:0});var b=a(document),d=b.width(),b=b.height(),g=document.documentElement||document.body;g.clientWidth!=g.offsetWidth&&(d=g.scrollWidth-
1);g.clientHeight!=g.offsetHeight&&(b=g.scrollHeight-1);f.css({width:d,height:b});c.$overlayWedge.css({width:d-c.overlayExtraWidth,height:b-c.overlayExtraHeight})},positionContent:function(a,b){var d=i.scrollLeft()+Math.max(0,a/2+c.offsetLeft),f=i.scrollTop()+Math.max(0,b/2+c.offsetTop);h.css({top:f,left:d})}};h.data("museOverlay",m);c.autoShow&&m.open()})}})(jQuery);
