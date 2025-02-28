## Canned Command Sequences
define keyvaluecan
	if [ -z "$(1)" ]; then \
		echo; \
		$(call err,"keyvaluecan needs at leats one argument!!!") \	
		echo; \
		exit 0; \
	elif [ "$(2)" == "" ]; then \
		echo -e "$(BWhite)"$(1)"$(Color_Off)"; \
	else \
		echo -e "$(BWhite)"$(1)"$(White): $(BBlue)"$(2)"$(Color_Off)"; \
	fi
endef

define headercan
	echo -e "$(Yellow)"$(1)"$(Color_Off)"
	echo -e "$(White)----------------------------------------------$(Color_Off)"
endef

define COMMITFORMAT
$(BWhite)\1$(BIBlue)\2$(White)\3$(IWhite)\4$(Color_Off)
endef

define prompt
	echo -e -n "$(Yellow)"$(1)":$(Color_Off) " \
	&& read input
endef

define inform
	echo -e "$(BYellow)INFO: $(White)"$(1)"$(Color_Off)"
endef

define err
	echo -e "$(Red)ERROR: $(Yellow)"$(1)"$(Color_Off)"
endef