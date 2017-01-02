from page import Page

class JigPage(Page):
    def __init__(self,page_num):
        super(JigPage, self).__init__(page_num)
        self.in_index = False
        self.title = "SCORPIONS"
        self.tagline = "SCORPIONS"

    def generate_content(self):
        self.add_title("SCORPIONS",font="size4")
        self.add_text("""
       `.'##';.`                                                   
       +@#@@#; #@.      :#,                                        
         .+@#+# .+,      `',   :#`                                 
          `:+#';';;':    ;+',  ,#.   :+           `,,,,,,          
              .`#; ,+;   :;', `+#,  :+,  `     .;#+.+:  ,@'#;`     
                 ++++,   +'+: `#;  ;',   +.   :#:'';.;@'.#` ,',    
                  ;;`;'  ',;; .#` :#;     ;##@#,          `#::':   
                  ;#++` .:,:..@; ,#:  .+'  .,.             '` ;;   
                  .;.`# .:::..'@:;;;;;;:                    +#+:   
                 ` :@+#+';#;;+,+,+@#+++;```                +`,#;   
                 '##'`;. '.;;.# ,:`,;;'+####+,        `;++@,;##:   
                 +#,,' # ;`:; `, '.';.;,@;;;;,:;''::,,'' .''.      
               `+':`.+`'`;`:; `, ,.;:,: @#@#,,';@:...,'#@++        
                :#++@+.#`+'+;,+.;+,':.'';#;##;;+:+;:`:,            
               .#@@@#'@'##;`,#+;@:+..+@@+@@##+.                    
               `+@@####++:;#+,,:;:;#@#+'@+:`                       
                  ;+'#:@;##+#@#;#+#;,.`                            
                 ,';;' +.':.,'',':,'+:`                            
              `.#:`,,  :',:;,`:`'`  ,#+                            
           .``#` ;.   .#' '',.`#.  `,''                            
       `;##@#,@''.   ,;',.:+:`;;@`   ``                            
    `++@@+,`,'+   .:,'@. .'+,.#+                                   
    `##@++##+:    ,''`  ,'#..#'                                    
      ,.                         

""")

page = JigPage("116")
