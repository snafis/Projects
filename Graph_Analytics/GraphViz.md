# GraphViz

* Install graphviz for Mac from graphviz.org.

* To check the installation, open a Terminal and type : dot -h

```
dot -h
dot: option -h unrecognized
 
Usage: dot [-Vv?] [-(GNE)name=val] [-(KTlso)<val>] <dot files>
```

OK, so dot was installed and added to your $PATH.

* Next, create a dot source file and launch dot : `dot -T png -O my1st.dot`

For example :
```
digraph finite_state_machine {
	rankdir=LR;
	size="8,5"
	node [shape = doublecircle]; LR_0 LR_3 LR_4 LR_8;
	node [shape = circle];
	LR_0 -> LR_2 [ label = "SS(B)" ];
	LR_0 -> LR_1 [ label = "SS(S)" ];
	LR_1 -> LR_3 [ label = "S($end)" ];
	LR_2 -> LR_6 [ label = "SS(b)" ];
	LR_2 -> LR_5 [ label = "SS(a)" ];
	LR_2 -> LR_4 [ label = "S(A)" ];
	LR_5 -> LR_7 [ label = "S(b)" ];
	LR_5 -> LR_5 [ label = "S(a)" ];
	LR_6 -> LR_6 [ label = "S(b)" ];
	LR_6 -> LR_5 [ label = "S(a)" ];
	LR_7 -> LR_8 [ label = "S(b)" ];
	LR_7 -> LR_5 [ label = "S(a)" ];
	LR_8 -> LR_6 [ label = "S(b)" ];
	LR_8 -> LR_5 [ label = "S(a)" ];
}
```
This will create a new file my1st.dot.png that looks like this :
![](http://www.graphviz.org/Gallery/directed/fsm.png)

* Reference: [dotguide](http://www.graphviz.org/pdf/dotguide.pdf)
