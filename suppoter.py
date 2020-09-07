kv = """
windowmanager:
    Mainscreen:
    Secondscreen:
    Csescreen:
<Mainscreen>:
    name:"main"
    RelativeLayout:
        Image:
            source:"RMK_Engineering_College.png"
            pos_hint:{"center_x":.5,"center_y":.7}
            size_hint:.5,.2
        Image: 
            source:"quality.png"
            pos_hint:{"center_x":.8,"center_y":.9}
            size_hint:.2,.1
        Image:
            source:"naac.png"
            pos_hint:{"center_x":.2,"center_y":.9}
            size_hint:.2,.2
    MDRectangleFlatButton:
        text:"START"
        pos_hint:{'center_x':0.5,'center_y':0.3}
        on_release:
            app.root.current="second"


<Secondscreen>:
    name:"second"
    MDRectangleFlatButton:
        text:"BACK"
        pos_hint:{'center_x':0.5,'center_y':0.1}
        on_release:
            app.root.current="main"  
    MDRectangleFlatButton:
        text:"CSE"
        pos_hint:{'center_x':0.5,'center_y':0.6}
        on_release:
            app.root.current="main"         
    NavigationLayout:
        ScreenManager: 
            Screen:        
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'STUDY MATERIALS'
                        spacing:30
                        padding:1
                        left_action_items: [["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                    MDLabel:
                        text: 'SELECT DEPARTMENT'
                        halign:'center'
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '10dp'
                Image:
                    source: 'chairman.png'
                    size_hint:(1,1)
                MDLabel:
                    text: 'Mail : principal@rmkec.ac.in / rmkec@vsnl.com'
                    font_style:'Subtitle1'
                    size_hint_y:None
                    height: self.texture_size[1]
                MDLabel:
                    text: 'Contact No: 044-3330 3330'
                    font_style:'Subtitle1'
                    size_hint_y:None
                    height: self.texture_size[1] 
                ScrollView:     
                    MDList:
                        OneLineListItem:
                            text: 'Contact Mail'
                        OneLineListItem:
                            text: 'Contact Number'
                        OneLineListItem:
                            text: 'Share The App' 
                              
                                       
            
"""
