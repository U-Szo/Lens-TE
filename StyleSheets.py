main_window_stylesheet = ("    background-color: rgb(38,49,51);\n"
"    border-radius:10px;\n")
title_bar_frame_stylesheet_window_normal = ("    background-color: rgb(17, 18, 17);\n"
"    border: 2px solid rgb(38,49,51);\n"
"    border-bottom: 0px;\n"
"    border-top-left-radius:10px;\n"
"    border-top-right-radius:10px;\n"
"    border-style:solid;\n")
title_bar_frame_stylesheet_window_maximized = ("    background-color: rgb(17, 18, 17);\n"
"    border: 2px solid rgb(38,49,51);\n"
"    border-bottom: 0px;\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:10px;\n"
"    border-style:solid;\n")
title_bar_move_frame_stylesheet =("    background-color: transparent;\n"
"    border:0px;\n")
title_label_stylesheet = ("background-color: qlineargradient(spread:reflect, x1:0, y1:0.0170455, x2:1, y2:0, stop:0 rgba(32, 33, 32, 255), stop:1 rgba(17, 18, 17, 255));\n"
"border: 0px;\n"
"border-bottom-left-radius:0px;\n")
minimize_button_stylesheet = ("QPushButton {\n"
"    background-color: rgb(17, 18, 17);\n"
"    border: 0px;\n"
"    border-radius:0px;\n"
"    margin:0px;   \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 51, 50);\n"
"    border-radius:0px;\n"
"    border-color:none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(37, 38, 37);\n"
"    border-radius:0px;\n"
"}\n"
"")
maximize_button_stylesheet = minimize_button_stylesheet
exit_button_stylesheet_window_normal = ("QPushButton {\n"
"    background-color: rgb(17, 18, 17);\n"
"    border: 0px;\n"
"    border-radius:0px;\n"
"    border-top-right-radius:10px;\n"
"    margin:0px;   \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(232, 17, 35);\n"
"    border-radius:0px;\n"
"    border-top-right-radius:10px;\n"
"    border-color:none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(149, 20, 30);\n"
"    border-radius:0px;\n"
"    border-top-right-radius:10px;\n"
"}\n"
"")
exit_button_stylesheet_window_maximized = ("QPushButton {\n"
"    background-color: rgb(17, 18, 17);\n"
"    border: 0px;\n"
"    border-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    margin:0px;   \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(232, 17, 35);\n"
"    border-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    border-color:none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(149, 20, 30);\n"
"    border-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"}\n"
"")
tool_bar_frame_stylesheet = ("background-color: rgb(17,18,17);\n"
"    border: 2px solid rgb(38,49,51);\n"
"    border-bottom: 0px;\n"
"    border-top: 0px;\n"
"border-radius:0px;\n")
tool_bar_buttons_stylesheet = ("QPushButton {\n"
"    background-color:rgb(192,192,192);\n"
"    border:0px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:rgb(132,132,132);\n"
"}")
input_output_splitter_stylesheet = ("    background-color: rgb(17, 18, 17);\n"
"    border: 2px solid rgb(38,49,51);\n"
"    border-top: 0px;\n"
"    border-radius: 0px;\n"
"    border-bottom-left-radius:10px;\n"
"    border-bottom-right-radius:10px;")
files_tab_widget_layout_widget_stylesheet = ("    border: 0px;\n")
files_tab_widget_stylesheet = ("QTabWidget::pane{\n"
"    border:0px;\n"
"}\n"
"QTabBar::tab {\n"
"    font: 10pt \"Consolas\";\n"
"    color: rgb(236, 236, 236);\n"
"    border-radius: 0px;\n"
"    border-bottom: 1px;\n"
"    border-top: 0px;\n"
"    border-left: 0px;\n"
"    border-right: 0px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-style: solid;\n"
"    border-bottom-color:  rgb(25, 26, 25);\n"
"}\n"
 "QTabBar::close-button {\n"
 "    image: url(main_window_icons/TabCloseButtonicon.png);\n"
 "    subcontrol-position: right;\n"
 "}\n"
 "QTabBar::close-button:hover {\n"
 "    image: url(main_window_icons/TabCloseButtonhovericon.png);\n"
 "    subcontrol-position: right;\n"
 "}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: None;\n"
"    background-color: rgb(29, 30, 29);\n"
"    color: rgb(236, 236, 236);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background-color: rgb(15, 16, 15);\n"
"    color: rgb(130, 130, 130);\n"
"}\n"
"QTabBar::tab:!selected:hover {\n"
"    background-color: rgb(32,33,32);\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8px;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: qlineargradient(spread:reflect, x1:0.488636, y1:0, x2:0, y2:0.00495455, stop:0 rgba(52, 52, 52, 255), stop:1 rgba(32, 33, 32, 255));\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8px;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}")
output_plain_text_edit_stylesheet = ("color: rgb(236, 236, 236);\n"
"font: 11pt \"Consolas\";"
"border: 0px;\n")
tab_code_editor_stylesheet = ("QCodeEditor {\n"
"    background-color: rgb(25, 26, 25);\n"
"    border-radius:0px;\n"
"    color: rgb(236, 236, 236);\n"
"    font: 11pt \"Consolas\";\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(5, 6, 5);\n"
"    width: 10px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(72, 73, 72);\n"
"    min-height: 30px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(72, 73, 72);\n"
"    height: 15px;\n"
"    border-top-left-radius: 5px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {  \n"
"    border: none;\n"
"    background-color: rgb(72, 73, 72);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 5px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* HORIZONTAL     */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(5, 6, 5);\n"
"    height: 10px;\n"
"    margin: 0px 15px 0px 15px ;\n"
"    border-radius: 0px;\n"
" }\n"
"/*  HANDLE BAR horizontal */\n"
"QScrollBar::handle:horizontal {    \n"
"    background-color: rgb(72, 73, 72);\n"
"    min-width: 30px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover{    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(72, 73, 72);\n"
"    width: 15px;\n"
"    border-top-left-radius: 5px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(72, 73, 72);\n"
"    width: 15px;\n"
"    border-top-right-radius: 5px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"")