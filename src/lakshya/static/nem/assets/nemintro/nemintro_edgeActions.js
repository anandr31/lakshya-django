
(function($,Edge,compId){var Composition=Edge.Composition,Symbol=Edge.Symbol;
//Edge symbol: 'stage'
(function(symbolName){Symbol.bindElementAction(compId,symbolName,"${_Rectangle}","mouseenter",function(sym,e){var mySymbolObject=sym.getSymbol("left");mySymbolObject.play();var mySymbolObject=sym.getSymbol("circle");mySymbolObject.stop();});
//Edge binding end
Symbol.bindElementAction(compId,symbolName,"${_Rectangle}","mouseleave",function(sym,e){var mySymbolObject=sym.getSymbol("left");mySymbolObject.playReverse();var mySymbolObject=sym.getSymbol("circle");mySymbolObject.play();});
//Edge binding end
Symbol.bindElementAction(compId,symbolName,"${_top_hover}","mouseenter",function(sym,e){var mySymbolObject=sym.getSymbol("top_hover");mySymbolObject.play();var mySymbolObject=sym.getSymbol("anstop");mySymbolObject.play();});
//Edge binding end
Symbol.bindElementAction(compId,symbolName,"${_top_hover}","mouseleave",function(sym,e){var mySymbolObject=sym.getSymbol("top_hover");mySymbolObject.playReverse();var mySymbolObject=sym.getSymbol("anstop");mySymbolObject.playReverse();});
//Edge binding end
Symbol.bindElementAction(compId,symbolName,"${_Middle_hover}","mouseenter",function(sym,e){var mySymbolObject=sym.getSymbol("Middle_hover");mySymbolObject.play();var mySymbolObject=sym.getSymbol("ansmiddle2");mySymbolObject.play();});
//Edge binding end
Symbol.bindElementAction(compId,symbolName,"${_Middle_hover}","mouseleave",function(sym,e){var mySymbolObject=sym.getSymbol("Middle_hover");mySymbolObject.playReverse();var mySymbolObject=sym.getSymbol("ansmiddle2");mySymbolObject.playReverse();});
//Edge binding end
Symbol.bindElementAction(compId,symbolName,"${_low_hover}","mouseleave",function(sym,e){var mySymbolObject=sym.getSymbol("low_hover");mySymbolObject.playReverse();var mySymbolObject=sym.getSymbol("anslow");mySymbolObject.playReverse();});
//Edge binding end
Symbol.bindElementAction(compId,symbolName,"${_low_hover}","mouseenter",function(sym,e){var mySymbolObject=sym.getSymbol("low_hover");mySymbolObject.play();var mySymbolObject=sym.getSymbol("anslow");mySymbolObject.play();});
//Edge binding end
})("stage");
//Edge symbol end:'stage'

//=========================================================

//Edge symbol: 'left'
(function(symbolName){Symbol.bindElementAction(compId,symbolName,"${_RoundRect2}","mouseover",function(sym,e){sym.play("start1");});
//Edge binding end
})("left");
//Edge symbol end:'left'

//=========================================================

//Edge symbol: 'blink'
(function(symbolName){Symbol.bindTriggerAction(compId,symbolName,"Default Timeline",2000,function(sym,e){sym.play();});
//Edge binding end
})("blink");
//Edge symbol end:'blink'

//=========================================================

//Edge symbol: 'circle'
(function(symbolName){Symbol.bindElementAction(compId,symbolName,"${_circleplant3}","mouseover",function(sym,e){div
{opacity=1.0}});
//Edge binding end
Symbol.bindTriggerAction(compId,symbolName,"Default Timeline",2000,function(sym,e){sym.play();});
//Edge binding end
})("circle");
//Edge symbol end:'circle'

//=========================================================

//Edge symbol: 'staticircle'
(function(symbolName){})("staticircle");
//Edge symbol end:'staticircle'

//=========================================================

//Edge symbol: 'top_hover'
(function(symbolName){Symbol.bindElementAction(compId,symbolName,"${_RoundRect2Copy}","mouseenter",function(sym,e){});
//Edge binding end
Symbol.bindElementAction(compId,symbolName,"${_RoundRect2Copy}","mouseleave",function(sym,e){});
//Edge binding end
})("top_hover");
//Edge symbol end:'top_hover'

//=========================================================

//Edge symbol: 'anstop'
(function(symbolName){})("anstop");
//Edge symbol end:'anstop'

//=========================================================

//Edge symbol: 'ansmiddle'
(function(symbolName){})("ansmiddle");
//Edge symbol end:'ansmiddle'

//=========================================================

//Edge symbol: 'ansmiddle2'
(function(symbolName){})("ansmiddle2");
//Edge symbol end:'ansmiddle2'

//=========================================================

//Edge symbol: 'anslow'
(function(symbolName){})("anslow");
//Edge symbol end:'anslow'
})(jQuery,AdobeEdge,"EDGE-54667278");