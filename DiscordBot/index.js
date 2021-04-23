const Discord = require("discord.js");
const { Client, MessageAttachment } = require('discord.js');
const config = require("./config.json");

const client = new Discord.Client();

const prefix = "!";

client.on("message", function(message) { 


    message.attachments.forEach(attachment => {
        
        const url = attachment.url;
        //message.channel.send(url);

        // import fs module in which writeFile function is defined. 
        const fsLibrary  = require('fs') 
  
        // Data which will need to add in a file. 
        let data = url;
  
        // Write data in 'newfile.txt' . 
        fsLibrary.writeFile('C:/Users/Dominic/PycharmProjects/Domert/url.txt', data, (error) => { 
      
            // In case of a error throw err exception. 
            if (error) throw err; 
        }) 
      });
});                                      

client.login(config.BOT_TOKEN);