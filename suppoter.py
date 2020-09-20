kv = """
ScreenManager:
    Mainscreen:
    Secondscreen:
    Contactscreen:
    Infoscreen:
    Aboutscreen:
    Csescreen:
    Itscreen:
    Ecescreen:
    Mechscreen:
    Csesem1screen:
    Csesem2screen:
    Csesem3screen:
    Csesem4screen:
    Csesem5screen:
    Csesem6screen:
    Csesem7screen:
    Csesem8screen:
    Itsem1screen:
    Itsem2screen:
    Itsem3screen:
    Itsem4screen:
    Itsem5screen:
    Itsem6screen:
    Itsem7screen:
    Itsem8screen:
    Ecesem1screen:
    Ecesem2screen:
    Ecesem3screen:
    Ecesem4screen:
    Ecesem5screen:
    Ecesem6screen:
    Ecesem7screen:
    Ecesem8screen:
    Mechsem1screen:
    Mechsem2screen:
    Mechsem3screen:
    Mechsem4screen:
    Mechsem5screen:
    Mechsem6screen:
    Mechsem7screen:
    Mechsem8screen:
<Mainscreen>:
    name:"main"
    MDLabel:
        text:'Tap to Start'
        size_hint:.5,.4
        halign:'center'
        pos_hint:{'center_x':0.5,'center_y':0.06}
        theme_text_color:'Hint'
    ImageButton:
        source:"RMK_Engineering_College.png"
        on_press:
            app.goto()  


<Secondscreen>:
    name:"second" 
    MDRectangleFlatIconButton:
        icon: 'language-python'
        text: 'CSE'
        width: dp(70)
        pos_hint: {'center_x':0.5,'center_y':0.65}
        on_press:
            app.root.current="cse"
    MDRectangleFlatIconButton:
        icon: 'language-java'
        text: 'IT'
        width: dp(70)
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press:
            app.root.current="it"  
    MDRectangleFlatIconButton:
        icon: 'electric-switch-closed'
        text: 'ECE'
        width: dp(70)
        pos_hint: {'center_x':0.5,'center_y':0.35}
        on_press:
            app.root.current="ece"  
    MDRectangleFlatIconButton:
        icon: 'nut'
        text: 'MECHANICAL'
        width: dp(140)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            app.root.current="mech"            
    MDLabel:
        text:'Choose Departments'
        size_hint:.5,.4
        halign:'center'
        pos_hint:{'center_x':0.5,'center_y':0.8}
        theme_text_color:'Custom'
        text_color:(236/255.0,98/255.0,81/255.0,1)
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'RMK E-MATERIALS'
                        spacing:20
                        padding:1
                        elevation: 11
                        left_action_items: [["menu",lambda x: nav_drawer.set_state("open")]]
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '10dp'
                ScrollView:     
                    MDList:
                        OneLineListItem:
                            text: 'Home'
                            on_press:
                                nav_drawer.set_state("close")
                                app.root.current="second"
                                app.shho()
                        OneLineListItem:
                            text: 'Contact Us'
                            on_press:
                                nav_drawer.set_state("close")
                                app.root.current="contactscreen"
                                app.show_popup()
                        OneLineListItem:
                            text: 'College Info'
                            on_press:
                                nav_drawer.set_state("close")
                                app.root.current="info"
                                app.show()
                        OneLineListItem:
                            text: 'App Makers'
                            on_press:
                                nav_drawer.set_state("close")
                                app.root.current="aboutscreen"
                                app.shoo()        
                        MDRaisedButton:
                            text:'Change Theme'
                            on_press:
                                nav_drawer.set_state("close")
                                app.show_theme_picker()           
                                     

<Contactscreen>:
    name: 'contactscreen'
    RelativeLayout:
        Image:
            source:"chairman.png"
            pos_hint:{"center_x":.5,"center_y":.7}
            size_hint:.6,1
    MDRectangleFlatIconButton:
        text:"Mail"
        icon:'email'
        size:80,30
        pos_hint:{'center_x':0.5,'center_y':0.45}
        on_press:
            app.show_dai()
    MDRectangleFlatIconButton:
        text:"Contact No"
        icon:'cellphone'
        size:130,30
        pos_hint:{'center_x':0.5,'center_y':0.35}
        on_press:
            app.show_da()
    MDRectangleFlatIconButton:
        text:"Address"
        icon:'location-enter'
        size:120,30
        pos_hint:{'center_x':0.5,'center_y':0.25}
        on_press:
            app.show_dia() 
    MDLabel:
        text:'Follow Us'
        size_hint:.5,.4
        halign:'center'
        pos_hint:{'center_x':0.5,'center_y':0.16}
        theme_text_color:'Custom'
        text_color:(236/255.0,98/255.0,81/255.0,1)
    MDFloatingActionButton:
        icon:'facebook'
        elevation_normal:8
        md_bg_color: (59/255.0,89/255.0,152/255.0,1)
        pos_hint:{'center_x':0.21,'center_y':0.08}
        on_press:
            app.web()
    MDFloatingActionButton:
        icon:'instagram'
        elevation_normal:8
        md_bg_color: (255/255.0,99/255.0,71/255.0,1)
        pos_hint:{'center_x':0.51,'center_y':0.08} 
        on_press:
            app.bro() 
    MDFloatingActionButton:
        icon:'linkedin'
        elevation_normal:8
        md_bg_color: (14/255.0,118/255.0,168/255.0,1)
        pos_hint:{'center_x':0.81,'center_y':0.08}
        on_press:
            app.wb()                                    
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Contact College'
                        spacing:30
                        padding:1
                        elevation: 11
                        left_action_items: [["menu",lambda x: nav_drawer.set_state("open")]]
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '10dp'
                ScrollView:     
                    MDList:
                        OneLineListItem:
                            text: 'Home'
                            on_press:
                                nav_drawer.set_state("close")
                                app.root.current="second"
                                app.shho()      
                        OneLineListItem:
                            text: 'Contact Us'
                            on_press:
                                nav_drawer.set_state("close")
                                app.root.current="contactscreen"
                                app.show_popup()
                        OneLineListItem:
                            text: 'College Info'
                            on_press:
                                nav_drawer.set_state("close")
                                app.root.current="info"
                                app.show()
                        OneLineListItem:
                            text: 'App Makers'
                            on_press:
                                nav_drawer.set_state("close")
                                app.root.current="aboutscreen"
                                app.shoo()                      
                        MDRaisedButton:
                            text:'Change Theme'
                            on_press: 
                                nav_drawer.set_state("close")
                                app.show_theme_picker()        


<Aboutscreen>:
    name: 'aboutscreen'
    MDCard:
        size_hint: None, None
        size: "125dp", "110dp"
        pos_hint: {"center_x": .2, "center_y": .72}
        elevation:12
        Image:
            source:"naren.png"
            size_hint:.5,1
    MDCard:
        size_hint: None, None
        size: "115dp", "119dp"
        pos_hint: {"center_x": .2, "center_y": .43}
        elevation:12
        Image:
            source:"sumanth.png"
            size_hint:.5,1
    MDCard:
        size_hint: None, None
        size: "110dp", "110dp"
        pos_hint: {"center_x": .2, "center_y": .15}
        elevation:12
        Image:
            source:"siva.png"
            size_hint:.5,1


    MDRectangleFlatButton:
        text: "Details" 
        pos_hint: {"center_x": .7, "center_y": .72}
        on_press:
            app.naren()
    MDRectangleFlatButton:
        text: "Details"
        pos_hint: {"center_x": .7, "center_y": .42}
        on_press: 
            app.sumanth()
    MDRectangleFlatButton:
        text: "Details"
        pos_hint: {"center_x": .7, "center_y": .15}
        on_press:
            app.siva()
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'App Makers'
                        spacing:30
                        padding:1
                        elevation: 11
                        left_action_items: [["menu",lambda x: nav_drawer.set_state("open")]]
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '10dp'
                ScrollView:     
                    MDList:
                        OneLineListItem:
                            text: 'Home'
                            on_press:
                                nav_drawer.set_state("close")
                                app.root.current="second"
                                app.shho()
                        OneLineListItem:
                            text: 'Contact Us'
                            on_press:
                                nav_drawer.set_state("close")
                                app.root.current="contactscreen"
                                app.show_popup()
                        OneLineListItem:
                            text: 'College Info'
                            on_press:
                                nav_drawer.set_state("close")
                                app.root.current="info"
                                app.show()
                        OneLineListItem:
                            text: 'App Makers'
                            on_press:
                                nav_drawer.set_state("close")
                                app.root.current="aboutscreen"
                                app.shoo()
                        MDRaisedButton:
                            text:'Change Theme' 
                            on_press: 
                                nav_drawer.set_state("close")
                                app.show_theme_picker()        


<Infoscreen>:
    name:'info'
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "280dp", "200dp"
        pos_hint: {"center_x": .5, "center_y": .5}
        MDLabel:
            text:'Click  The  Logo'
            size_hint:.5,.4
            halign:'center'
            pos_hint:{'center_x':0.5,'center_y':0.1}
            theme_text_color:'Custom'
            text_color:(236/255.0,98/255.0,81/255.0,1)
        ImageButton:
            source:"RMK_Engineering_College.png"
            on_press:
                app.clg()  
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'College Achievements'
                        spacing:8
                        padding:1
                        elevation: 11
                        left_action_items: [["menu",lambda x: nav_drawer.set_state("open")]]
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '10dp'
                ScrollView:     
                    MDList:
                        OneLineListItem:
                            text: 'Home'
                            on_press:
                                nav_drawer.set_state("close")
                                app.root.current="second"
                                app.shho()
                        OneLineListItem:
                            text: 'Contact Us'
                            on_press:
                                nav_drawer.set_state("close")
                                app.root.current="contactscreen"
                                app.show_popup()
                        OneLineListItem:
                            text: 'College Info'
                            on_press:
                                nav_drawer.set_state("close")
                                app.root.current="info"
                                app.show()
                        OneLineListItem:
                            text: 'App Makers'
                            on_press:
                                nav_drawer.set_state("close")
                                app.root.current="aboutscreen"
                                app.shoo()  
                        MDRaisedButton:
                            text:'Change Theme'                           
                            on_press: 
                                nav_drawer.set_state("close")
                                app.show_theme_picker()  
                                
                                
<Csescreen>:
    name:'cse'
    MDLabel:
        text:'Choose Semester'
        size_hint:.5,.4
        halign:'center'
        pos_hint:{'center_x':0.5,'center_y':0.8}
        theme_text_color:'Custom'
        text_color:(236/255.0,98/255.0,81/255.0,1)
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-1'
        width: dp(100)
        pos_hint: {'center_x':0.3,'center_y':0.7}
        on_press:
            app.root.current="csesem1"  
            app.sub()
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-2'
        width: dp(100)
        pos_hint: {'center_x':0.7,'center_y':0.7}
        on_press:
            app.root.current="csesem2"  
            app.sub()
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-3'
        width: dp(100)
        pos_hint: {'center_x':0.3,'center_y':0.55}
        on_press:
            app.root.current="csesem3" 
            app.sub() 
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-4'
        width: dp(100)
        pos_hint: {'center_x':0.7,'center_y':0.55}
        on_press:
            app.root.current="csesem4"  
            app.sub()
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-5'
        width: dp(100)
        pos_hint: {'center_x':0.3,'center_y':0.4}
        on_press:
            app.root.current="csesem5"  
            app.sub()
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-6'
        width: dp(100)
        pos_hint: {'center_x':0.7,'center_y':0.4}
        on_press:
            app.root.current="csesem6"  
            app.sub()
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-7'
        width: dp(100)
        pos_hint: {'center_x':0.3,'center_y':0.25}
        on_press:
            app.root.current="csesem7"  
            app.sub()
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-8'
        width: dp(100)
        pos_hint: {'center_x':0.7,'center_y':0.25}
        on_press:
            app.avali()
            #app.root.current="csesem8"        
            #app.sub()  
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'CSE E-MATERIALS'
                        spacing:20
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change()]]
                    Widget:
        
    
<Itscreen>:
    name:'it'
    MDLabel:
        text:'Choose Semester'
        size_hint:.5,.4
        halign:'center'
        pos_hint:{'center_x':0.5,'center_y':0.8}
        theme_text_color:'Custom'
        text_color:(236/255.0,98/255.0,81/255.0,1)
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-1'
        width: dp(100)
        pos_hint: {'center_x':0.3,'center_y':0.7}
        on_press:
            app.root.current="itsem1" 
            app.sub() 
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-2'
        width: dp(100)
        pos_hint: {'center_x':0.7,'center_y':0.7}
        on_press:
            app.root.current="itsem2"  
            app.sub()
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-3'
        width: dp(100)
        pos_hint: {'center_x':0.3,'center_y':0.55}
        on_press:
            app.root.current="itsem3"  
            app.sub()
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-4'
        width: dp(100)
        pos_hint: {'center_x':0.7,'center_y':0.55}
        on_press:
            app.root.current="itsem4"  
            app.sub()
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-5'
        width: dp(100)
        pos_hint: {'center_x':0.3,'center_y':0.4}
        on_press:
            app.root.current="itsem5"
            app.sub()  
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-6'
        width: dp(100)
        pos_hint: {'center_x':0.7,'center_y':0.4}
        on_press:
            app.root.current="itsem6"  
            app.sub()
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-7'
        width: dp(100)
        pos_hint: {'center_x':0.3,'center_y':0.25}
        on_press:
            app.root.current="itsem7"  
            app.sub()
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-8'
        width: dp(100)
        pos_hint: {'center_x':0.7,'center_y':0.25}
        on_press:
            app.avali()
            #app.root.current="itsem8"  
            #app.sub()      
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'IT E-MATERIALS'
                        spacing:20
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change()]]
                    Widget:



<Ecescreen>:
    name:'ece'
    MDLabel:
        text:'Choose Semester'
        size_hint:.5,.4
        halign:'center'
        pos_hint:{'center_x':0.5,'center_y':0.8}
        theme_text_color:'Custom'
        text_color:(236/255.0,98/255.0,81/255.0,1)
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-1'
        width: dp(100)
        pos_hint: {'center_x':0.3,'center_y':0.7}
        on_press:
            app.root.current="ecesem1" 
            app.sub() 
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-2'
        width: dp(100)
        pos_hint: {'center_x':0.7,'center_y':0.7}
        on_press:
            app.root.current="ecesem2"  
            app.sub()
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-3'
        width: dp(100)
        pos_hint: {'center_x':0.3,'center_y':0.55}
        on_press:
            app.root.current="ecesem3"  
            app.sub()
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-4'
        width: dp(100)
        pos_hint: {'center_x':0.7,'center_y':0.55}
        on_press:
            app.root.current="ecesem4"  
            app.sub()
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-5'
        width: dp(100)
        pos_hint: {'center_x':0.3,'center_y':0.4}
        on_press:
            app.root.current="ecesem5"  
            app.sub()
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-6'
        width: dp(100)
        pos_hint: {'center_x':0.7,'center_y':0.4}
        on_press:
            app.root.current="ecesem6"  
            app.sub()
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-7'
        width: dp(100)
        pos_hint: {'center_x':0.3,'center_y':0.25}
        on_press:
            app.root.current="ecesem7"
            app.sub()  
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-8'
        width: dp(100)
        pos_hint: {'center_x':0.7,'center_y':0.25}
        on_press:
            app.avali()
            #app.root.current="ecesem8" 
            #app.sub()       
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'ECE E-MATERIALS'
                        spacing:20
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change()]]
                    Widget:
        

<Mechscreen>          
    name:'mech'
    MDLabel:
        text:'Choose Semester'
        size_hint:.5,.4
        halign:'center'
        pos_hint:{'center_x':0.5,'center_y':0.8}
        theme_text_color:'Custom'
        text_color:(236/255.0,98/255.0,81/255.0,1)
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-1'
        width: dp(100)
        pos_hint: {'center_x':0.3,'center_y':0.7}
        on_press:
            app.root.current="mechsem1"
            app.sub()  
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-2'
        width: dp(100)
        pos_hint: {'center_x':0.7,'center_y':0.7}
        on_press:
            app.root.current="mechsem2"  
            app.sub()
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-3'
        width: dp(100)
        pos_hint: {'center_x':0.3,'center_y':0.55}
        on_press:
            app.root.current="mechsem3"  
            app.sub()
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-4'
        width: dp(100)
        pos_hint: {'center_x':0.7,'center_y':0.55}
        on_press:
            app.root.current="mechsem4"
            app.sub()  
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-5'
        width: dp(100)
        pos_hint: {'center_x':0.3,'center_y':0.4}
        on_press:
            app.root.current="mechsem5"  
            app.sub()
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-6'
        width: dp(100)
        pos_hint: {'center_x':0.7,'center_y':0.4}
        on_press:
            app.root.current="mechsem6" 
            app.sub() 
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-7'
        width: dp(100)
        pos_hint: {'center_x':0.3,'center_y':0.25}
        on_press:
            app.root.current="mechsem7"  
            app.sub()
    MDRectangleFlatIconButton:
        icon: "cast-education"
        text: 'SEM-8'
        width: dp(100)
        pos_hint: {'center_x':0.7,'center_y':0.25}
        on_press:
            app.avali()
            #app.root.current="mechsem8"   
            #app.sub()     
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'MECH E-MATERIALS'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change()]]
                    Widget:
                    
                    
                                
<Csesem1screen>:        
    name:'csesem1'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        CSE SEM-1'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_screen()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                            ThreeLineListItem:
                                text:"Communicative English"
                                secondary_text: "HS8151"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shhs8151()
                                    
                            ThreeLineListItem:
                                text:"Engineering Mathematics I"
                                secondary_text: "MA8151"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shma8151()
                                    
                            ThreeLineListItem:
                                text:"Engineering Physics"
                                secondary_text: "PH8151"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shph8151()
                            
                            ThreeLineListItem:
                                text:"Engineering Chemistry"
                                secondary_text: "CY8151"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shcy8151()
                                    
                            ThreeLineListItem:
                                text:"Problem Solving and Python Programming"
                                secondary_text: "GE8151"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shge8151()
                                    
                            ThreeLineListItem:
                                text:"Engineering Graphics"
                                secondary_text: "GE8152"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shge8152()
       
<Csesem2screen>:         
    name:'csesem2'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        CSE SEM-2'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_screen()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                            ThreeLineListItem:
                                text:"Technical English"
                                secondary_text: "HS8251"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shhs8251()
                                    
                            ThreeLineListItem:
                                text:"Engineering Mathematics II"
                                secondary_text: "MA8251"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shma8251()
                    
                                    
                            ThreeLineListItem:
                                text:"Physics for Information Science"
                                secondary_text: "PH8252"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.shph8252u1()
                            ThreeLineListItem:
                                text:"Physics for Information Science"
                                secondary_text: "PH8252"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.shph8252u2()
                            ThreeLineListItem:
                                text:"Physics for Information Science"
                                secondary_text: "PH8252"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.shph8252u3()
                            ThreeLineListItem:
                                text:"Physics for Information Science"
                                secondary_text: "PH8252"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.shph8252u4()
                            ThreeLineListItem:
                                text:"Physics for Information Science"
                                secondary_text: "PH8252"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.shph8252u5()
                                    
                            ThreeLineListItem:
                                text:"Basic Electrical, Electronics and Measurement Engineering"
                                secondary_text: "BE8255"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.shbe8255u1()
                            ThreeLineListItem:
                                text:"Basic Electrical, Electronics and Measurement Engineering"
                                secondary_text: "BE8255"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.shbe8255u2()
                            ThreeLineListItem:
                                text:"Basic Electrical, Electronics and Measurement Engineering"
                                secondary_text: "BE8255"
                                tertiary_text: "Unit -3"
                                on_release:
                                    app.shbe8255u3()
                            ThreeLineListItem:
                                text:"Basic Electrical, Electronics and Measurement Engineering"
                                secondary_text: "BE8255"
                                tertiary_text: "Unit 4"
                                on_release:
                                    app.shbe8255u4()
                            ThreeLineListItem:
                                text:"Basic Electrical, Electronics and Measurement Engineering"
                                secondary_text: "BE8255"
                                tertiary_text: "Unit 5"
                                on_release:
                                    app.shbe8255u5()
                                    
                            ThreeLineListItem:
                                text:"Environmental Science and Engineering"
                                secondary_text: "GE8291"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shge8291()
                                
                            ThreeLineListItem:
                                text:"Programming in C"
                                secondary_text: "CS8251"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shcs8251()
      
                                                             
<Csesem3screen>:         
    name:'csesem3'
                    
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        CSE SEM-3'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_screen()]]    
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                            ThreeLineListItem:
                                text:"Discrete Mathematics"
                                secondary_text: "MA8351"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.cseMA8351u1()

                            ThreeLineListItem:
                                text: "Discrete Mathematics"
                                secondary_text: "MA8351"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.cseMA8351u2()
                            ThreeLineListItem:
                                text: "Discrete Mathematics"
                                secondary_text: "MA8351"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.cseMA8351u3()
                            ThreeLineListItem:
                                text: "Discrete Mathematics"
                                secondary_text: "MA8351"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.cseMA8351u4()
                            ThreeLineListItem:
                                text: "Discrete Mathematics"
                                secondary_text: "MA8351"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.cseMA8351u5()
                            ThreeLineListItem:
                                text: "Digital Principles and System Design"
                                secondary_text: "CS8351"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.cseCS8351u1()
                            ThreeLineListItem:
                                text: "Digital Principles and System Design"
                                secondary_text: "CS8351"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.cseCS8351u2()
                            ThreeLineListItem:
                                text: "Digital Principles and System Design"
                                secondary_text: "CS8351"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.cseCS8351u3()
                            ThreeLineListItem:
                                text: "Digital Principles and System Design"
                                secondary_text: "CS8351"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.cseCS8351u4()
                            ThreeLineListItem:
                                text: "Digital Principles and System Design"
                                secondary_text: "CS8351"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.cseCS8351u5()
                            ThreeLineListItem:
                                text: "Data Structures"
                                secondary_text: "CS8391"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.cseCS8391u1()
                            ThreeLineListItem:
                                text: "Data Structures"
                                secondary_text: "CS8391"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.cseCS8391u2()
                            ThreeLineListItem:
                                text: "Data Structures"
                                secondary_text: "CS8391"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.cseCS8391u3()
                            ThreeLineListItem:
                                text: "Data Structures"
                                secondary_text: "CS8391"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.cseCS8391u4()
                            ThreeLineListItem:
                                text: "Data Structures"
                                secondary_text: "CS8391"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.cseCS8391u5()
                            ThreeLineListItem:
                                text: "Object Oriented Programming"
                                secondary_text: "CS8392"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.cseCS8392u1()
                            ThreeLineListItem:
                                text: "Object Oriented Programming"
                                secondary_text: "CS8392"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.cseCS8392u2()
                            ThreeLineListItem:
                                text: "Object Oriented Programming"
                                secondary_text: "CS8392"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.cseCS8392u3()
                            ThreeLineListItem:
                                text: "Object Oriented Programming"
                                secondary_text: "CS8392"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.cseCS8392u4()
                            ThreeLineListItem:
                                text: "Object Oriented Programming"
                                secondary_text: "CS8392"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.cseCS8392u5()
                            ThreeLineListItem:
                                text: "Communication Engineering"
                                secondary_text: "EC8395"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.cseEC8395u1()
                            ThreeLineListItem:
                                text: "Communication Engineering"
                                secondary_text: "EC8395"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.cseEC8395u2()
                            ThreeLineListItem:
                                text: "Communication Engineering"
                                secondary_text: "EC8395"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.cseEC8395u3()
                            ThreeLineListItem:
                                text: "Communication Engineering"
                                secondary_text: "EC8395"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.cseEC83952u4()
                            ThreeLineListItem:
                                text: "Communication Engineering"
                                secondary_text: "EC8395"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.cseEC8395u5()
                    
                    
                                   

<Csesem4screen>:         
    name:'csesem4'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        CSE SEM-4'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_screen()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                            ThreeLineListItem:
                                text:"Probability and Queueing Theory"
                                secondary_text: "MA8402"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.cseMA8402u1()
                            ThreeLineListItem:
                                text:"Probability and Queueing Theory"
                                secondary_text: "MA8402"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.cseMA8402u2()
                            ThreeLineListItem:
                                text:"Probability and Queueing Theory"
                                secondary_text: "MA8402"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.cseMA8402u3()
                            ThreeLineListItem:
                                text:"Probability and Queueing Theory"
                                secondary_text: "MA8402"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.cseMA8402u4()
                            ThreeLineListItem:
                                text:"Probability and Queueing Theory"
                                secondary_text: "MA8402"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.cseMA8402u5()
                            ThreeLineListItem:
                                text:"Computer Architecture"
                                secondary_text: "CS8491"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.cseCS8491u1to5()
                            ThreeLineListItem:
                                text:"Database Management Systems"
                                secondary_text: "CS8492"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.cseCS8492u1to5()
                            ThreeLineListItem:
                                text:"Design and Analysis of Algorithms"
                                secondary_text: "CS8451"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.cseCS8451u1to5()
                            ThreeLineListItem:
                                text:"Operating Systems"
                                secondary_text: "CS8493"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.cseCS8493u1to5()
                            ThreeLineListItem:
                                text:"Software Engineering"
                                secondary_text: "CS8494"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.cseCS8494u1to5()
      




                                                             
<Csesem5screen>:         
    name:'csesem5'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        CSE SEM-5'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_screen()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                            ThreeLineListItem:
                                text:"Algebra and Number Theory"
                                secondary_text: "MA8551"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.cseMA8551u1to5()
                            ThreeLineListItem:
                                text:"Computer Networks"
                                secondary_text: "CS8591"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.cseCS8591u1to5()
                            ThreeLineListItem:
                                text:"Microprocessors and Microcontrollers"
                                secondary_text: "EC8691"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.cseEC8691u1to5()
                            ThreeLineListItem:
                                text:"Theory of Computation"
                                secondary_text: "CS6503"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.cseCS6503u1to5()
                            ThreeLineListItem:
                                text:"Object Oriented Analysis and Design"
                                secondary_text: "CS8592"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.cseCS8592u1to5()
                            ThreeLineListItem:
                                text:"Geographic Information System"
                                secondary_text: "OCE552"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.cseOCE552u1to5()
         
                                                             
<Csesem6screen>:         
    name:'csesem6'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        CSE SEM-6'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_screen()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                            ThreeLineListItem:
                                text:"Internet Programming"
                                secondary_text: "CS8651"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.cseCS8651u1to5()
                            ThreeLineListItem:
                                text:"Artificial Intelligence"
                                secondary_text: "CS8691"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.cseCS8691u1to5()
                            ThreeLineListItem:
                                text:"Mobile Computing"
                                secondary_text: "CS8601"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.cseCS8601u1to5()
                            ThreeLineListItem:
                                text:"Compiler Design"
                                secondary_text: "CS8602"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.cseCS8602u1to5()
                            ThreeLineListItem:
                                text:"Distributed Systems"

                                secondary_text: "CS8603"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.cseCS8603u1to5()
                            ThreeLineListItem:
                                text:"Software Testing"
                                secondary_text: "IT8076"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.cseIT8076u1to5()
         
                                                             
<Csesem7screen>:         
    name:'csesem7'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        CSE SEM-7'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_screen()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                            ThreeLineListItem:
                                text:"Principles of Management"
                                secondary_text: "MG8591"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.cseMG8591u1()
                            ThreeLineListItem:
                                text:"Principles of Management"
                                secondary_text: "MG8591"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.cseMG8591u2()
                            ThreeLineListItem:
                                text:"Principles of Management"
                                secondary_text: "MG8591"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.cseMG8591u3()
                            ThreeLineListItem:
                                text:"Principles of Management"
                                secondary_text: "MG8591"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.cseMG8591u4()
                            ThreeLineListItem:
                                text:"Principles of Management"
                                secondary_text: "MG8591"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.cseMG8591u5()
        
              
<Csesem8screen>:        
    name:'csesem8'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        CSE SEM-8'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_screen()]]
                    Widget:
        
                                
                            
                                                            

<Itsem1screen>:        
    name:'itsem1'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        IT SEM-1'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_s()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                            ThreeLineListItem:
                                text:"Communicative English"
                                secondary_text: "HS8151"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shhs8151()
                                    
                            ThreeLineListItem:
                                text:"Engineering Mathematics I"
                                secondary_text: "MA8151"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shma8151()
                                    
                            ThreeLineListItem:
                                text:"Engineering Physics"
                                secondary_text: "PH8151"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shph8151()
                            
                            ThreeLineListItem:
                                text:"Engineering Chemistry"
                                secondary_text: "CY8151"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shcy8151()
                                    
                            ThreeLineListItem:
                                text:"Problem Solving and Python Programming"
                                secondary_text: "GE8151"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shge8151()
                                    
                            ThreeLineListItem:
                                text:"Engineering Graphics"
                                secondary_text: "GE8152"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shge8152()
       
                                                                                                                             




<Itsem2screen>:        
    name:'itsem2' 
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        IT SEM-2'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_s()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                            ThreeLineListItem:
                                text:"Technical English"
                                secondary_text: "HS8251"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shhs8251()
                                    
                            ThreeLineListItem:
                                text:"Engineering Mathematics II"
                                secondary_text: "MA8251"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shma8251()
                    
                                    
                            ThreeLineListItem:
                                text:"Physics for Information Science"
                                secondary_text: "PH8252"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.shph8252u1()
                            ThreeLineListItem:
                                text:"Physics for Information Science"
                                secondary_text: "PH8252"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.shph8252u2()
                            ThreeLineListItem:
                                text:"Physics for Information Science"
                                secondary_text: "PH8252"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.shph8252u3()
                            ThreeLineListItem:
                                text:"Physics for Information Science"
                                secondary_text: "PH8252"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.shph8252u4()
                            ThreeLineListItem:
                                text:"Physics for Information Science"
                                secondary_text: "PH8252"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.shph8252u5()
                                    
                            ThreeLineListItem:
                                text:"Basic Electrical, Electronics and Measurement Engineering"
                                secondary_text: "BE8255"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.shbe8255u1()
                            ThreeLineListItem:
                                text:"Basic Electrical, Electronics and Measurement Engineering"
                                secondary_text: "BE8255"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.shbe8255u2()
                            ThreeLineListItem:
                                text:"Basic Electrical, Electronics and Measurement Engineering"
                                secondary_text: "BE8255"
                                tertiary_text: "Unit -3"
                                on_release:
                                    app.shbe8255u3()
                            ThreeLineListItem:
                                text:"Basic Electrical, Electronics and Measurement Engineering"
                                secondary_text: "BE8255"
                                tertiary_text: "Unit 4"
                                on_release:
                                    app.shbe8255u4()
                            ThreeLineListItem:
                                text:"Basic Electrical, Electronics and Measurement Engineering"
                                secondary_text: "BE8255"
                                tertiary_text: "Unit 5"
                                on_release:
                                    app.shbe8255u5()
                            ThreeLineListItem:
                                text:"Programming in C"
                                secondary_text: "CS8251"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shcs8251()        
        
                                




<Itsem3screen>:        
    name:'itsem3'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        IT SEM-3'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_s()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                            ThreeLineListItem:
                                text:"Discrete Mathematics"
                                secondary_text: "MA8351"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.cseMA8351u1()

                            ThreeLineListItem:
                                text: "Discrete Mathematics"
                                secondary_text: "MA8351"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.cseMA8351u2()
                            ThreeLineListItem:
                                text: "Discrete Mathematics"
                                secondary_text: "MA8351"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.cseMA8351u3()
                            ThreeLineListItem:
                                text: "Discrete Mathematics"
                                secondary_text: "MA8351"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.cseMA8351u4()
                            ThreeLineListItem:
                                text: "Discrete Mathematics"
                                secondary_text: "MA8351"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.cseMA8351u5()
                            ThreeLineListItem:
                                text:"Digital Principles and System Design"
                                secondary_text: "CS8351"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itcs8351u1()

                            ThreeLineListItem:
                                text: "Digital Principles and System Design"
                                secondary_text: "CS8351"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itcs8351u2()
                            ThreeLineListItem:
                                text: "Digital Principles and System Design"
                                secondary_text: "CS8351"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itcs8351u3()
                            ThreeLineListItem:
                                text: "Digital Principles and System Design"
                                secondary_text: "CS8351"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itcs8351u4()
                            ThreeLineListItem:
                                text: "Digital Principles and System Design"
                                secondary_text: "CS8351"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.itcs8351u5()
                            ThreeLineListItem:
                                text:"Object Oriented Programming"
                                secondary_text: "CS8392"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itcs8392u1()

                            ThreeLineListItem:
                                text: "Object Oriented Programming"
                                secondary_text: "CS8392"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itcs8392u2()
                            ThreeLineListItem:
                                text: "Object Oriented Programming"
                                secondary_text: "CS8392"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itcs8392u3()
                            ThreeLineListItem:
                                text: "Object Oriented Programming"
                                secondary_text: "CS8392"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itcs8392u4()
                            ThreeLineListItem:
                                text: "Object Oriented Programming"
                                secondary_text: "CS8392"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.itcs8392u5()
                            ThreeLineListItem:
                                text:"Data Structures"
                                secondary_text: "CS8391"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.itcs8391()

                            
                            ThreeLineListItem:
                                text: "Analog and Digital Communication"
                                secondary_text: "EC8394"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itec8394u1()
                            ThreeLineListItem:
                                text: "Analog and Digital Communication"
                                secondary_text: "EC8394"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itec8394u2()
                            ThreeLineListItem:
                                text: "Analog and Digital Communication"
                                secondary_text: "EC8394"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itec8394u3()
                            ThreeLineListItem:
                                text: "Analog and Digital Communication"
                                secondary_text: "EC8394"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itec8394u4()
                            ThreeLineListItem:
                                text: "Analog and Digital Communication"
                                secondary_text: "EC8394"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.itec8394u5()
       
                             
                                
                                
<Itsem4screen>:        
    name:'itsem4'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        IT SEM-4'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_s()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                            ThreeLineListItem:
                                text:"Computer Architecture"
                                secondary_text: "CS8491"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itcs8491u1()
                            ThreeLineListItem:
                                text:"Computer Architecture"
                                secondary_text: "CS8491"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itcs8491u2()
                            ThreeLineListItem:
                                text:"Computer Architecture"
                                secondary_text: "CS8491"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itcs8491u3()
                            ThreeLineListItem:
                                text:"Computer Architecture"
                                secondary_text: "CS8491"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itcs8491u4()
                            ThreeLineListItem:
                                text:"Computer Architecture"
                                secondary_text: "CS8491"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.itcs8491u5()
                                    
                            ThreeLineListItem:
                                text:"PROBABILITY& STATISTICS"
                                secondary_text: "MA8391"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.itma8391()
                                    
                            ThreeLineListItem:
                                text:"DBMS"
                                secondary_text: "CS8492"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.itcs8492()
                            ThreeLineListItem:
                                text:"OS"
                                secondary_text: "CS8493"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.itcs8493()
                            ThreeLineListItem:
                                text:"DAA"
                                secondary_text: "CS8451"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.itcs8451()
                            ThreeLineListItem:
                                text:"EVS"
                                secondary_text: "GE8291"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shge8291()        
     
                                                                


<Itsem5screen>:        
    name:'itsem5'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        IT SEM-5'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_s()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                                    
                            ThreeLineListItem:
                                text:"Computer Networks"
                                secondary_text: "CS8591"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itcs8591u1()
                            ThreeLineListItem:
                                text:"Computer Networks"
                                secondary_text: "CS8591"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itcs8591u2()
                            ThreeLineListItem:
                                text:"Computer Networks"
                                secondary_text: "CS8591"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itcs8591u3()
                            ThreeLineListItem:
                                text:"Computer Networks"
                                secondary_text: "CS8591"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itcs8591u4()
                            ThreeLineListItem:
                                text:"Computer Networks"
                                secondary_text: "CS8591"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.itcs8591u5()
                                    
                            ThreeLineListItem:
                                text:"Microprocessor and Microcontroller"
                                secondary_text: "EC8691"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itec8691u1()
                            ThreeLineListItem:
                                text:"Microprocessor and Microcontroller"
                                secondary_text: "EC8691"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itec8691u2()
                            ThreeLineListItem:
                                text:"Microprocessor and Microcontroller"
                                secondary_text: "EC8691"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itec8691u3()
                            ThreeLineListItem:
                                text:"Microprocessor and Microcontroller"
                                secondary_text: "EC8691"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itec8691u4()
                            ThreeLineListItem:
                                text:"Microprocessor and Microcontroller"
                                secondary_text: "EC8691"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.itec8691u5()
                                    
                            ThreeLineListItem:
                                text:"Web Technology"
                                secondary_text: "IT8501"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.itit8501()
                                
                            ThreeLineListItem:
                                text:"ALGEBRA & NUMBER THEORY"
                                secondary_text: "MA8551"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itma8551u1()
                            ThreeLineListItem:
                                text:"ALGEBRA & NUMBER THEORY"
                                secondary_text: "MA8551"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itma8551u2()
                            ThreeLineListItem:
                                text:"ALGEBRA & NUMBER THEORY"
                                secondary_text: "MA8551"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itma8551u3()
                            ThreeLineListItem:
                                text:"ALGEBRA & NUMBER THEORY"
                                secondary_text: "MA8551"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itma8551u4()
                            ThreeLineListItem:
                                text:"ALGEBRA & NUMBER THEORY"
                                secondary_text: "MA8551"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.itma8551u5()
                                    
                            ThreeLineListItem:
                                text:"Air pollution and Control Engineering"
                                secondary_text: "OCE551"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itoce551u1()
                            ThreeLineListItem:
                                text:"Air pollution and Control Engineering"
                                secondary_text: "OCE551"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itoce551u2()
                            ThreeLineListItem:
                                text:"Air pollution and Control Engineering"
                                secondary_text: "OCE551"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itoce551u3()
                            ThreeLineListItem:
                                text:"Air pollution and Control Engineering"
                                secondary_text: "OCE551"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itoce551u4()
                            ThreeLineListItem:
                                text:"Air pollution and Control Engineering"
                                secondary_text: "OCE551"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.avali()
                                    #app.itoce551u5()
                            ThreeLineListItem:
                                text:"Software Engineering"
                                secondary_text: "CS8494"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itcs8494u1()
                            ThreeLineListItem:
                                text:"Software Engineering"
                                secondary_text: "CS8494"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itcs8494u2()
                            ThreeLineListItem:
                                text:"Software Engineering"
                                secondary_text: "CS8494"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itcs8494u3()
                            ThreeLineListItem:
                                text:"Software Engineering"
                                secondary_text: "CS8494"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itcs8494u4()
                            ThreeLineListItem:
                                text:"Software Engineering"
                                secondary_text: "CS8494"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.itcs8494u5()
      


<Itsem6screen>:        
    name:'itsem6'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        IT SEM-6'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_s()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList:     
                            ThreeLineListItem:
                                text:"OOAD"
                                secondary_text: "CS8592"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itcs8592u1()
                            ThreeLineListItem:
                                text:"OOAD"
                                secondary_text: "CS8592"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itcs8592u2()
                                    
                            ThreeLineListItem:
                                text:"OOAD"
                                secondary_text: "CS8592"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itcs8592u3()
                            ThreeLineListItem:
                                text:"OOAD"
                                secondary_text: "CS8592"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itcs8592u4()
                            ThreeLineListItem:
                                text:"OOAD"
                                secondary_text: "CS8592"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.itcs8592u5()
                                    
                            ThreeLineListItem:
                                text:"BIG DATA"
                                secondary_text: "CS8091"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itcs8091u1()
                            ThreeLineListItem:
                                text:"BIG DATA"
                                secondary_text: "CS8091"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itcs8091u1()
                            ThreeLineListItem:
                                text:"BIG DATA"
                                secondary_text: "CS8091"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itcs8091u2()
                            ThreeLineListItem:
                                text:"BIG DATA"
                                secondary_text: "CS8091"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itcs8091u3()
                            ThreeLineListItem:
                                text:"BIG DATA"
                                secondary_text: "CS8091"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itcs8091u4()
                            ThreeLineListItem:
                                text:"BIG DATA"
                                secondary_text: "CS8091"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.itcs8091u5()
                                    
                            ThreeLineListItem:
                                text:"Computational Intelligence"
                                secondary_text: "IT8601"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itit8601u1()
                            ThreeLineListItem:
                                text:"Computational Intelligence"
                                secondary_text: "IT8601"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itit8601u2()
                            ThreeLineListItem:
                                text:"Computational Intelligence"
                                secondary_text: "IT8601"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itit8601u3()
                            ThreeLineListItem:
                                text:"Computational Intelligence"
                                secondary_text: "IT8601"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itit8601u4()
                            ThreeLineListItem:
                                text:"Computational Intelligence"
                                secondary_text: "IT8601"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.itit8601u5()
                            ThreeLineListItem:
                                text:"Software testing"
                                secondary_text: "IT8076"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itit8076u1()
                            ThreeLineListItem:
                                text:"Software testing"
                                secondary_text: "IT8076"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itit8076u2()
                            ThreeLineListItem:
                                text:"Software testing"
                                secondary_text: "IT8076"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itit8076u3()
                            ThreeLineListItem:
                                text:"Software testing"
                                secondary_text: "IT8076"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itit8076u4()
                            ThreeLineListItem:
                                text:"Software testing"
                                secondary_text: "IT8076"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.itit8076u5()
                            ThreeLineListItem:
                                text:"COMPUTER GRAPHICS"
                                secondary_text: "CS8092"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itcs8092u1()
                            ThreeLineListItem:
                                text:"COMPUTER GRAPHICS"
                                secondary_text: "CS8092"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itcs8092u2()
                            ThreeLineListItem:
                                text:"COMPUTER GRAPHICS"
                                secondary_text: "CS8092"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itcs8092u3()
                            ThreeLineListItem:
                                text:"COMPUTER GRAPHICS"
                                secondary_text: "CS8092"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itcs8092u4()
                            ThreeLineListItem:
                                text:"COMPUTER GRAPHICS"
                                secondary_text: "CS8092"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.itcs8092u1()
                                    
                            ThreeLineListItem:
                                text:"MOBILE COMPUTATION"
                                secondary_text: "CS8602"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itcs8602u1()
                            ThreeLineListItem:
                                text:"MOBILE COMPUTATION"
                                secondary_text: "CS8602"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itcs8602u2()
                            ThreeLineListItem:
                                text:"MOBILE COMPUTATION"
                                secondary_text: "CS8602"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itcs8602u3()
                            ThreeLineListItem:
                                text:"MOBILE COMPUTATION"
                                secondary_text: "CS8602"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itcs8602u4()
                            ThreeLineListItem:
                                text:"MOBILE COMPUTATION"
                                secondary_text: "CS8602"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.itcs8602u5()
                        
                                
                                
<Itsem7screen>:        
    name:'itsem7'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        IT SEM-7'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_s()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList:     
                            ThreeLineListItem:
                                text:"Cloud Computing"
                                secondary_text: "CS8791"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itcs8791u1()
                            ThreeLineListItem:
                                text:"Cloud Computing"
                                secondary_text: "CS8791"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itcs8791u2()
                            ThreeLineListItem:
                                text:"Cloud Computing"
                                secondary_text: "CS8791"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itcs8791u3()
                            ThreeLineListItem:
                                text:"Cloud Computing"
                                secondary_text: "CS8791"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itcs8791u4()
                            ThreeLineListItem:
                                text:"Cloud Computing"
                                secondary_text: "CS8791"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.itcs8791u5()
                            
                            ThreeLineListItem:
                                text:"Principles of Management"
                                secondary_text: "MG8591"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itmg8591u1()
                            ThreeLineListItem:
                                text:"Principles of Management"
                                secondary_text: "MG8591"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itmg8591u2()
                            ThreeLineListItem:
                                text:"Principles of Management"
                                secondary_text: "MG8591"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itmg8591u3()
                            ThreeLineListItem:
                                text:"Principles of Management"
                                secondary_text: "MG8591"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itmg8591u4()
                            ThreeLineListItem:
                                text:"Principles of Management"
                                secondary_text: "MG8591"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.avali()
                                    #app.itmg8591u5()
                                    
                            ThreeLineListItem:
                                text:"Cryptography and Network Security"
                                secondary_text: "CS8792"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itcs8792u1()
                            ThreeLineListItem:
                                text:"Cryptography and Network Security"
                                secondary_text: "CS8792"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itcs8792u2()
                            ThreeLineListItem:
                                text:"Cryptography and Network Security"
                                secondary_text: "CS8792"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itcs8792u3()
                            ThreeLineListItem:
                                text:"Cryptography and Network Security"
                                secondary_text: "CS8792"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itcs8792u4()
                            ThreeLineListItem:
                                text:"Cryptography and Network Security"
                                secondary_text: "CS8792"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.itcs8792u5()
                                    
                            ThreeLineListItem:
                                text:"Human Computer Interaction"
                                secondary_text: "CS8079"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itcs8079u1()
                            ThreeLineListItem:
                                text:"Human Computer Interaction"
                                secondary_text: "CS8079"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itcs8079u2()
                            ThreeLineListItem:
                                text:"Human Computer Interaction"
                                secondary_text: "CS8079"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itcs8079u3()
                            ThreeLineListItem:
                                text:"Human Computer Interaction"
                                secondary_text: "CS8079"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itcs8079u4()
                            ThreeLineListItem:
                                text:"Human Computer Interaction"
                                secondary_text: "CS8079"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.avali()
                                    #app.itcs8079u5()
                                    
                            ThreeLineListItem:
                                text:"Total Quality Management"
                                secondary_text: "GE8077"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itge8077u1()
                            ThreeLineListItem:
                                text:"Total Quality Management"
                                secondary_text: "GE8077"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itge8077u2()
                            ThreeLineListItem:
                                text:"Total Quality Management"
                                secondary_text: "GE8077"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itge8077u3()
                            ThreeLineListItem:
                                text:"Total Quality Management"
                                secondary_text: "GE8077"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itge8077u4()
                            ThreeLineListItem:
                                text:"Total Quality Management"
                                secondary_text: "GE8077"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.avali()
                                    #app.itge8077u5()
                            
                            ThreeLineListItem:
                                text:"Supply chain management"
                                secondary_text: "OME752"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.itome752u1()
                            ThreeLineListItem:
                                text:"Supply chain management"
                                secondary_text: "OME752"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.itome752u2()
                            ThreeLineListItem:
                                text:"Supply chain management"
                                secondary_text: "OME752"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.itome752u3()
                            ThreeLineListItem:
                                text:"Supply chain management"
                                secondary_text: "OME752"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.itome752u4()
                            ThreeLineListItem:
                                text:"Supply chain management"
                                secondary_text: "OME752"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.avali()
                                    #app.itome752u5()
                                    



<Itsem8screen>:        
    name:'itsem8'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        IT SEM-8'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_s()]]
                    Widget:
       
                                
                                
                                
<Ecesem1screen>:        
    name:'ecesem1'
    MDLabel:
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        ECE SEM-1'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_se()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                            ThreeLineListItem:
                                text:"Communicative English"
                                secondary_text: "HS8151"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shhs8151()
                                    
                            ThreeLineListItem:
                                text:"Engineering Mathematics I"
                                secondary_text: "MA8151"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shma8151()
                                    
                            ThreeLineListItem:
                                text:"Engineering Physics"
                                secondary_text: "PH8151"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shph8151()
                            
                            ThreeLineListItem:
                                text:"Engineering Chemistry"
                                secondary_text: "CY8151"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shcy8151()
                                    
                            ThreeLineListItem:
                                text:"Problem Solving and Python Programming"
                                secondary_text: "GE8151"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shge8151()
                                    
                            ThreeLineListItem:
                                text:"Engineering Graphics"
                                secondary_text: "GE8152"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shge8152()
        
                                
                                
                                
<Ecesem2screen>:        
    name:'ecesem2'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        ECE SEM-2'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_se()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList:  
                            ThreeLineListItem:
                                text:"Technical English"
                                secondary_text: "HS8251"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shhs8251()
                            ThreeLineListItem:
                                text:"Engineering Mathematics II"
                                secondary_text: "MA8251"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shma8251()           
                            ThreeLineListItem:
                                text:"Electronic Devices"
                                secondary_text: "EC8252"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.eceEC8252u1()
                            ThreeLineListItem:
                                text:"Electronic Devices"
                                secondary_text: "EC8252"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.eceEC8252u2()
                            ThreeLineListItem:
                                text:"Electronic Devices"
                                secondary_text: "EC8252"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.eceEC8252u3()
                            ThreeLineListItem:
                                text:"Electronic Devices"
                                secondary_text: "EC8252"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.eceEC8252u4()
                            ThreeLineListItem:
                                text:"Electronic Devices"
                                secondary_text: "EC8252"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.eceEC8252u5()
                            ThreeLineListItem:
                                text:"Circuit Analysis"
                                secondary_text: "EC8251"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceEC8251all()
                            ThreeLineListItem:
                                text:"Basic Electrical & Instrumentation Engineering"
                                secondary_text: "BE8254"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.eceBE8254u1()
                            ThreeLineListItem:
                                text:"Basic Electrical & Instrumentation Engineering"
                                secondary_text: "BE8254"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.eceBE8254u2()
                            ThreeLineListItem:
                                text:"Basic Electrical & Instrumentation Engineering"
                                secondary_text: "BE8254"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.eceBE8254u3()
                            ThreeLineListItem:
                                text:"Basic Electrical & Instrumentation Engineering"
                                secondary_text: "BE8254"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.eceBE8254u4()
                            ThreeLineListItem:
                                text:"Basic Electrical & Instrumentation Engineering"
                                secondary_text: "BE8254"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.eceBE8254u5()
                            ThreeLineListItem:
                                text:"Physics for Electronics Engineering"
                                secondary_text: "PH8253"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.ecePH8253u1()
                            ThreeLineListItem:
                                text:"Physics for Electronics Engineering"
                                secondary_text: "PH8253"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.ecePH8253u2()
                            ThreeLineListItem:
                                text:"Physics for Electronics Engineering"
                                secondary_text: "PH8253"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.ecePH8253u3()
                            ThreeLineListItem:
                                text:"Physics for Electronics Engineering"
                                secondary_text: "PH8253"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.ecePH8253u4()
                            ThreeLineListItem:
                                text:"Physics for Electronics Engineering"
                                secondary_text: "PH8253"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.ecePH8253u5()
                                                                                                                                                                        
                                                                       
                               
                                  
<Ecesem3screen>:        
    name:'ecesem3'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        ECE SEM-3'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_se()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                            ThreeLineListItem:
                                text:"Linear Algebra and Partial Differential Equations"
                                secondary_text: "MA8352"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceMA8352all()
                            ThreeLineListItem:
                                text:"Fundamentals of Data Structures in C"
                                secondary_text: "EC8393"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceEC8393all() 
                            ThreeLineListItem:
                                text:"Electronic Circuits-I"
                                secondary_text: "EC8351"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceEC8351all()
                            ThreeLineListItem:
                                text:"Signals & Systems"
                                secondary_text: "EC8352"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceEC8352all()
                            ThreeLineListItem:
                                text:"Digital Electronics"
                                secondary_text: "EC8392"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceEC8392all()
                            ThreeLineListItem:
                                text:"Control Systems Engineering"
                                secondary_text: "EC8391"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceEC8391all()                
                                                           
                                                                  
                                
                            
                                
<Ecesem4screen>:        
    name:'ecesem4'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        ECE SEM-4'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_se()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                            ThreeLineListItem:
                                text:"Electronic Circuits-II"
                                secondary_text: "EC8452"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceEC8452all()
                            ThreeLineListItem:
                                text:"Linear Integrated Circuits"
                                secondary_text: "EC8453"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceEC8453all()        
                            ThreeLineListItem:
                                text:"Environmental Science and Engineering"
                                secondary_text: "GE8291"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceGE8291all()
                            ThreeLineListItem:
                                text:"Communication Theory"
                                secondary_text: "EC8491"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceEC8491all()
                            ThreeLineListItem:
                                text:"Electromagnetic Fields"
                                secondary_text: "EC8451"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceEC8451all()                    



<Ecesem5screen>:        
    name:'ecesem5'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        ECE SEM-5'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_se()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                            ThreeLineListItem:
                                text:"Digital Communication"
                                secondary_text: "EC8501"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceEC8501all()
                            ThreeLineListItem:
                                text:"Discrete Time Signal Processing"
                                secondary_text: "EC8553"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceEC8553all()
                            ThreeLineListItem:
                                text:"Computer Architecture and Organization"
                                secondary_text: "EC8552"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceEC8552all()
                            ThreeLineListItem:
                                text:"Communication Networks"
                                secondary_text: "EC8551"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceEC8551all()
                            ThreeLineListItem:
                                text:"Medical Electronics"
                                secondary_text: "EC8073"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.eceEC8551u1()
                            ThreeLineListItem:
                                text:"Medical Electronics"
                                secondary_text: "EC8073"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.eceEC8551u2()
                            ThreeLineListItem:
                                text:"Medical Electronics"
                                secondary_text: "EC8073"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.eceEC8551u3()
                            ThreeLineListItem:
                                text:"Medical Electronics"
                                secondary_text: "EC8073"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.eceEC8551u4()
                            ThreeLineListItem:
                                text:"Medical Electronics"
                                secondary_text: "EC8073"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.avali()
                                    #app.eceEC8551u5()                                                        
                            ThreeLineListItem:
                                text:"Basics of Biomedical Instrumentation"
                                secondary_text: "OMD551"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.eceEC8551u1() 
                            ThreeLineListItem:
                                text:"Basics of Biomedical Instrumentation"
                                secondary_text: "OMD551"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.eceEC8551u2() 
                            ThreeLineListItem:
                                text:"Basics of Biomedical Instrumentation"
                                secondary_text: "OMD551"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.eceEC8551u3() 
                            ThreeLineListItem:
                                text:"Basics of Biomedical Instrumentation"
                                secondary_text: "OMD551"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.eceEC8551u4()
                            ThreeLineListItem:
                                text:"Basics of Biomedical Instrumentation"
                                secondary_text: "OMD551"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.avali()
                                    #app.eceEC8551u5()                                 
                                    
                            

<Ecesem6screen>:        
    name:'ecesem6'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        ECE SEM-6'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_se()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                            ThreeLineListItem:
                                text:"Microprocessor & Microcontroller"
                                secondary_text: "EC8691"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceEC8691all()
                            ThreeLineListItem:
                                text:"VLSI Design"
                                secondary_text: "EC8095"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceEC8095all() 
                            ThreeLineListItem:
                                text:"Wireless Communication"
                                secondary_text: "EC8652"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceEC8652all()
                            ThreeLineListItem:
                                text:"Principles of Management"
                                secondary_text: "MG8591"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceMG8591all()
                            ThreeLineListItem:
                                text:"Transmission Lines & RF systems"
                                secondary_text: "EC8651"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceEC8651all()
                            ThreeLineListItem:
                                text:"Multimedia Compression and Communication"
                                secondary_text: "EC8002"
                                tertiary_text: "All Units"
                                on_release:
                                    app.eceEC8002all()          
                                                                  
       


<Ecesem7screen>:        
    name:'ecesem7'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        ECE SEM-7'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_se()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                            ThreeLineListItem:
                                text:"Antennas & Microwave Engineering"
                                secondary_text: "EC8701"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.eceEC8701u1()
                            ThreeLineListItem:
                                text:"Antennas & Microwave Engineering"
                                secondary_text: "EC8701"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.eceEC8701u2()
                            ThreeLineListItem:
                                text:"Antennas & Microwave Engineering"
                                secondary_text: "EC8701"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.eceEC8701u3()
                            ThreeLineListItem:
                                text:"Antennas & Microwave Engineering"
                                secondary_text: "EC8701"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.eceEC8701u4()
                            ThreeLineListItem:
                                text:"Antennas & Microwave Engineering"
                                secondary_text: "EC8701"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.avali()
                                    #app.eceEC8701u5() 
                            ThreeLineListItem:
                                text:"Optical Communication"
                                secondary_text: "EC8751"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.eceEC8751u1()
                            ThreeLineListItem:
                                text:"Optical Communication"
                                secondary_text: "EC8751"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.eceEC8751u2()
                            ThreeLineListItem:
                                text:"Optical Communication"
                                secondary_text: "EC8751"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.eceEC8751u3()
                            ThreeLineListItem:
                                text:"Optical Communication"
                                secondary_text: "EC8751"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.eceEC8751u4()
                            ThreeLineListItem:
                                text:"Optical Communication"
                                secondary_text: "EC8751"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.avali()
                                    #app.eceEC8751u5()
                            ThreeLineListItem:
                                text:"Embedded & Real Time Systems"
                                secondary_text: "EC8791"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.eceEC8791u1()
                            ThreeLineListItem:
                                text:"Embedded & Real Time Systems"
                                secondary_text: "EC8791"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.eceEC8791u2()
                            ThreeLineListItem:
                                text:"Embedded & Real Time Systems"
                                secondary_text: "EC8791"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.eceEC8791u3()
                            ThreeLineListItem:
                                text:"Embedded & Real Time Systems"
                                secondary_text: "EC8791"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.eceEC8791u4()
                            ThreeLineListItem:
                                text:"Embedded & Real Time Systems"
                                secondary_text: "EC8791"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.avali()
                                    #app.eceEC8791u5()
                            ThreeLineListItem:
                                text:"Ad Hoc & Wireless Sensor Networks"
                                secondary_text: "EC8702"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.eceEC8702u1()
                            ThreeLineListItem:
                                text:"Ad Hoc & Wireless Sensor Networks"
                                secondary_text: "EC8702"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.eceEC8702u2()
                            ThreeLineListItem:
                                text:"Ad Hoc & Wireless Sensor Networks"
                                secondary_text: "EC8702"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.eceEC8702u3()
                            ThreeLineListItem:
                                text:"Ad Hoc & Wireless Sensor Networks"
                                secondary_text: "EC8702"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.eceEC8702u4()
                            ThreeLineListItem:
                                text:"Ad Hoc & Wireless Sensor Networks"
                                secondary_text: "EC8702"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.avali()
                                    #app.eceEC8702u5()
                            ThreeLineListItem:
                                text:"Cognitive Radio"
                                secondary_text: "EC8071"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.eceEC8071u1()
                            ThreeLineListItem:
                                text:"Cognitive Radio"
                                secondary_text: "EC8071"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.eceEC8071u2()
                            ThreeLineListItem:
                                text:"Cognitive Radio"
                                secondary_text: "EC8071"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.eceEC8071u3()
                            ThreeLineListItem:
                                text:"Cognitive Radio"
                                secondary_text: "EC8071"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.eceEC8071u4()
                            ThreeLineListItem:
                                text:"Cognitive Radio"
                                secondary_text: "EC8071"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.avali()
                                    #app.eceEC8071u5()
                            ThreeLineListItem:
                                text:"Transducer Engineering"
                                secondary_text: "OIC751"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.eceOIC751u1()
                            ThreeLineListItem:
                                text:"Transducer Engineering"
                                secondary_text: "OIC751"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.eceOIC751u2()
                            ThreeLineListItem:
                                text:"Transducer Engineering"
                                secondary_text: "OIC751"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.eceOIC751u3()
                            ThreeLineListItem:
                                text:"Transducer Engineering"
                                secondary_text: "OIC751"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.eceOIC751u4()
                            ThreeLineListItem:
                                text:"Transducer Engineering"
                                secondary_text: "OIC751"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.avali()
                                    #app.eceOIC751u5()                                                                                                
                                                                                                                                            
                                                            
        
     
                                

<Ecesem8screen>:        
    name:'ecesem8'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        ECE SEM-8'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_se()]]
       
      
                                

<Mechsem1screen>:        
    name:'mechsem1'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        MECH SEM-1'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_sce()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                            ThreeLineListItem:
                                text:"Communicative English"
                                secondary_text: "HS8151"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shhs8151()
                                    
                            ThreeLineListItem:
                                text:"Engineering Mathematics I"
                                secondary_text: "MA8151"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shma8151()
                                    
                            ThreeLineListItem:
                                text:"Engineering Physics"
                                secondary_text: "PH8151"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shph8151()
                            
                            ThreeLineListItem:
                                text:"Engineering Chemistry"
                                secondary_text: "CY8151"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shcy8151()
                                    
                            ThreeLineListItem:
                                text:"Problem Solving and Python Programming"
                                secondary_text: "GE8151"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shge8151()
                                    
                            ThreeLineListItem:
                                text:"Engineering Graphics"
                                secondary_text: "GE8152"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.shge8152()
       
                                
                                
<Mechsem2screen>:        
    name:'mechsem2'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        MECH SEM-2'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_sce()]]
                    Widget:
                                       



<Mechsem3screen>:        
    name:'mechsem3'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        MECH SEM-3'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_sce()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                            ThreeLineListItem:
                                text:"Engineering Thermodynamics"
                                secondary_text: "ME8391"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.mME8391u1()
                            ThreeLineListItem:
                                text:"Engineering Thermodynamics"
                                secondary_text: "ME8391"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.mME8391u2()
                            ThreeLineListItem:
                                text:"Engineering Thermodynamics"
                                secondary_text: "ME8391"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.mME8391u3()
                            ThreeLineListItem:
                                text:"Engineering Thermodynamics"
                                secondary_text: "ME8391"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.mME8391u4()
                            ThreeLineListItem:
                                text:"Engineering Thermodynamics"
                                secondary_text: "ME8391"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.mME8391u5()
                            ThreeLineListItem:
                                text:"Electrical Drives and Controls"
                                secondary_text: "EE8353"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.mEE8353u1()
                            ThreeLineListItem:
                                text:"Electrical Drives and Controls"
                                secondary_text: "EE8353"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.mEE8353u2()
                            ThreeLineListItem:
                                text:"Electrical Drives and Controls"
                                secondary_text: "EE8353"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.mEE8353u3()
                            ThreeLineListItem:
                                text:"Electrical Drives and Controls"
                                secondary_text: "EE8353"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.mEE8353u4()
                            ThreeLineListItem:
                                text:"Electrical Drives and Controls"
                                secondary_text: "EE8353"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.mEE8353u5()
                            ThreeLineListItem:
                                text:"Fluid Mechanics and machinery"
                                secondary_text: "CE8394"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.mCE8394u1()
                            ThreeLineListItem:
                                text:"Fluid Mechanics and machinery"
                                secondary_text: "CE8394"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.mCE8394u2()
                            ThreeLineListItem:
                                text:"Fluid Mechanics and machinery"
                                secondary_text: "CE8394"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.mCE8394u3()
                            ThreeLineListItem:
                                text:"Fluid Mechanics and machinery"
                                secondary_text: "CE8394"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.mCE8394u4()
                            ThreeLineListItem:
                                text:"Fluid Mechanics and machinery"
                                secondary_text: "CE8394"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.mCE8394u5()
                            ThreeLineListItem:
                                text:"Manufacturing Technology - I"
                                secondary_text: "ME8351"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.mME8351u1()
                            ThreeLineListItem:
                                text:"Manufacturing Technology - I"
                                secondary_text: "ME8351"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.mME8351u2()
                            ThreeLineListItem:
                                text:"Manufacturing Technology - I"
                                secondary_text: "ME8351"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.mME8351u3()
                            ThreeLineListItem:
                                text:"Manufacturing Technology - I"
                                secondary_text: "ME8351"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.mME8351u4()
                            ThreeLineListItem:
                                text:"Manufacturing Technology - I"
                                secondary_text: "ME8351"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.mME8351u5()
                            ThreeLineListItem:
                                text:"Transforms and Partial Differential Equations"
                                secondary_text: "MA8353"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.mMA8353u1()
                            ThreeLineListItem:
                                text:"Transforms and Partial Differential Equations"
                                secondary_text: "MA8353"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.mMA8353u2()
                            ThreeLineListItem:
                                text:"Transforms and Partial Differential Equations"
                                secondary_text: "MA8353"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.mMA8353u3()
                            ThreeLineListItem:
                                text:"Transforms and Partial Differential Equations"
                                secondary_text: "MA8353"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.mMA8353u4()
                            ThreeLineListItem:
                                text:"Transforms and Partial Differential Equations"
                                secondary_text: "MA8353"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.mMA8353u5()
       
                                
                                
                                
<Mechsem4screen>:        
    name:'mechsem4'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        MECH SEM-4'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_sce()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList: 
                            ThreeLineListItem:
                                text:"Engineering Metallurgy"
                                secondary_text: "ME8491"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.mME8491u1to5()
                            ThreeLineListItem:
                                text:"Kinematics of Machinery"
                                secondary_text: "ME8492"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.mME8492u1to5()
                            ThreeLineListItem:
                                text:"Statistics and Numerical Methods"
                                secondary_text: "MA8452"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.mMA8452u1to5()
                            ThreeLineListItem:
                                text:"Thermal Engineering- I"
                                secondary_text: "ME8493"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.mME8493u1to5()
                            ThreeLineListItem:
                                text:"Manufacturing Technology-II"
                                secondary_text: "ME8451"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.mME8451u1to5()
                            ThreeLineListItem:
                                text:"Strength of Materials for Mechanical Engineers"
                                secondary_text: "CE8395"
                                tertiary_text: "Unit-1 to Unit-5"
                                on_release:
                                    app.mCE8395u1to5()
                                       
                                


<Mechsem5screen>:        
    name:'mechsem5'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        MECH SEM-5'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_sce()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList:     
                            ThreeLineListItem:
                                text:"Metrology and Measurements"
                                secondary_text: "ME8501"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.mme8501u1()
                            ThreeLineListItem:
                                text:"Metrology and Measurements"
                                secondary_text: "ME8501"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.mme8501u2()
                            ThreeLineListItem:
                                text:"Metrology and Measurements"
                                secondary_text: "ME8501"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.mme8501u3()
                            ThreeLineListItem:
                                text:"Metrology and Measurements"
                                secondary_text: "ME8501"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.mme8501u4()
                            ThreeLineListItem:
                                text:"Metrology and Measurements"
                                secondary_text: "ME8501"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.mme8501u5()
                                    
                            ThreeLineListItem:
                                text:"Design of Machine Elements"
                                secondary_text: "ME8593"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.mme8593u1()
                            ThreeLineListItem:
                                text:"Design of Machine Elements"
                                secondary_text: "ME8593"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.mme8593u2()
                            ThreeLineListItem:
                                text:"Design of Machine Elements"
                                secondary_text: "ME8593"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.mme8593u3()
                            ThreeLineListItem:
                                text:"Design of Machine Elements"
                                secondary_text: "ME8593"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.mme8593u4()
                            ThreeLineListItem:
                                text:"Design of Machine Elements"
                                secondary_text: "ME8593"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.mme8593u5()
                                    
                            ThreeLineListItem:
                                text:"Dynamics of Machines"
                                secondary_text: "ME8594"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.mme8594u1()
                            ThreeLineListItem:
                                text:"Dynamics of Machines"
                                secondary_text: "ME8594"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.mme8594u2()
                            ThreeLineListItem:
                                text:"Dynamics of Machines"
                                secondary_text: "ME8594"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.mme8594u3()
                            ThreeLineListItem:
                                text:"Dynamics of Machines"
                                secondary_text: "ME8594"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.mme8594u4()
                            ThreeLineListItem:
                                text:"Dynamics of Machines"
                                secondary_text: "ME8594"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.mme8594u5()
                                    
                            ThreeLineListItem:
                                text:"Thermal Engineering- II"
                                secondary_text: "ME8595"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.mme8595u1()
                            ThreeLineListItem:
                                text:"Thermal Engineering- II"
                                secondary_text: "ME8595"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.mme8595u2()
                            ThreeLineListItem:
                                text:"Thermal Engineering- II"
                                secondary_text: "ME8595"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.mme8595u3()
                            ThreeLineListItem:
                                text:"Thermal Engineering- II"
                                secondary_text: "ME8595"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.mme8595u4()
                            ThreeLineListItem:
                                text:"Thermal Engineering- II"
                                secondary_text: "ME8595"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.mme8595u5()
                            
                            ThreeLineListItem:
                                text:"Product Design & Development"
                                secondary_text: "OMF551"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.momf551u1()
                            ThreeLineListItem:
                                text:"Product Design & Development"
                                secondary_text: "OMF551"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.momf551u2()
                            ThreeLineListItem:
                                text:"Product Design & Development"
                                secondary_text: "OMF551"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.momf551u3()
                            ThreeLineListItem:
                                text:"Product Design & Development"
                                secondary_text: "OMF551"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.momf551u4()
                            ThreeLineListItem:
                                text:"Product Design & Development"
                                secondary_text: "OMF551"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.avali()
                                    #app.momf551u5()
       


<Mechsem6screen>:        
    name:'mechsem6'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        MECH SEM-6'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_sce()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList:     
                            ThreeLineListItem:
                                text:"Computer Aided Design and Manufacturing"
                                secondary_text: "ME8691"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.mme8691()
                            
                            ThreeLineListItem:
                                text:"Hydraulics and Pneumatics"
                                secondary_text: "ME8694"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.mme8694()
                                    
                            ThreeLineListItem:
                                text:"Heat and Mass transfer"
                                secondary_text: "ME8693"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.mme8693()
                            
                            ThreeLineListItem:
                                text:"Automobile Engineering"
                                secondary_text: "ME8091"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.mme8091()
                                    
                            ThreeLineListItem:
                                text:"Design of Transmission System"
                                secondary_text: "ME8651"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.mme8651()
                                    
                            ThreeLineListItem:
                                text:"finite element analysis"
                                secondary_text: "ME8692"
                                tertiary_text: "Unit 1-5"
                                on_release:
                                    app.mme8692()
        


<Mechsem7screen>:        
    name:'mechsem7'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        MECH SEM-7'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_sce()]]
                    ScrollView:
                        do_scroll_x: False
                        MDList:     
                            ThreeLineListItem:
                                text:"Testing of Materials"
                                secondary_text: "OML751"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.moml751u1()
                            ThreeLineListItem:
                                text:"Testing of Materials"
                                secondary_text: "OML751"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.moml751u2()
                            ThreeLineListItem:
                                text:"Testing of Materials"
                                secondary_text: "OML751"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.moml751u3()
                            ThreeLineListItem:
                                text:"Testing of Materials"
                                secondary_text: "OML751"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.moml751u4()
                            ThreeLineListItem:
                                text:"Testing of Materials"
                                secondary_text: "OML751"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.avali()
                                    #app.moml751u5()
                                    
                            ThreeLineListItem:
                                text:"Non Destructive testing and evaluation"
                                secondary_text: "ME8097"
                                tertiary_text: "Unit-1"
                                on_release:
                                    app.mme8097u1()
                            ThreeLineListItem:
                                text:"Non Destructive testing and evaluation"
                                secondary_text: "ME8097"
                                tertiary_text: "Unit-2"
                                on_release:
                                    app.mme8097u2()
                            ThreeLineListItem:
                                text:"Non Destructive testing and evaluation"
                                secondary_text: "ME8097"
                                tertiary_text: "Unit-3"
                                on_release:
                                    app.mme8097u3()
                            ThreeLineListItem:
                                text:"Non Destructive testing and evaluation"
                                secondary_text: "ME8097"
                                tertiary_text: "Unit-4"
                                on_release:
                                    app.mme8097u4()
                            ThreeLineListItem:
                                text:"Non Destructive testing and evaluation"
                                secondary_text: "ME8097"
                                tertiary_text: "Unit-5"
                                on_release:
                                    app.avali()
                                    #app.mme8097u5()
       




<Mechsem8screen>:        
    name:'mechsem8'
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: '        MECH SEM-8'
                        spacing:10
                        padding:1
                        elevation: 11
                        left_action_items: [["keyboard-backspace",lambda x: app.change_sce()]]
                    Widget:
       

                        
                                        
"""