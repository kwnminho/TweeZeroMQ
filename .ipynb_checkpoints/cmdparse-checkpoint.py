class SCPIParser():
    def __init__(self):
        self.errormsg = 'Command "{}" is not defined. \nSelect from [{}]'

    def Error(self, string):
        return ("Error : " + string)

  ################################################################################
  ### START
  ################################################################################
  # starting lcoation for all commands
    def parsecmd(self, *args):
        if len(args)==1:
            #Function switch to map commands to functions
            cmd_switch = {
              b'START' : self.start,
              b'STOP' : self.stop,
              b'KILL_SERVER' : self.kill_server
            }
            func=cmd_switch.get(args[0])
            return func()
        
        if len(args)==2:
            cmd_switch = {
                 b'UPLOAD_DATA' : self.upload_data
             }
            func=cmd_switch.get(args[0])
            return func(args[1])

                
    def start(self):
        # Start the AWG
        reply_message=b'Starting the AWG'
        
        # if error is found, set the reply to be an error message
        return reply_message, True

    def stop(self):
        reply_message=b'Stopping the AWG'
        
        # if error is found, set the reply to be an error message
        return reply_message, True 
    
    def kill_server(self):        
        reply_message=b'Killing the server'
        return reply_message, False
    
    def upload_data(self, data):
        print('uploading the data to the AWG')
        print(data)
        reply_message=b'data uploaded'
        return reply_message, True
    


      