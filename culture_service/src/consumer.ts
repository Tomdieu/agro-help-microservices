import amqp from "amqplib";
import {Soil} from './models'
var channel: amqp.Channel, connection: amqp.Connection;
import colors from "colors";
// connectQueue();

export async function connectQueue() {
  try {
    connection = await amqp.connect("amqp://myuser:mypass@localhost:5672");
    channel = await connection.createChannel();

    await channel.assertQueue("culture");

    channel.consume("culture", (data) => {
      console.log("Recieve ".green.bold, { data });
      const receiveData = JSON.parse(data.content.toString());
      const contentType = data.properties.contentType;
      if(contentType=='soil_created'){
        Soil.create({id:receiveData.data.id,type:receiveData.data.type,description:receiveData.data.description,composition:receiveData.data.composition}).then(soil=>{
          console.log(`Soil ${soil.type} created!`)
        })
      }
      if(contentType == 'soil_updated'){
        Soil.findByPk(receiveData.data.id).then(soil=>{
          if(receiveData.data.type!=soil.type){
            soil.type = receiveData.data.type;
          }
          if(receiveData.data.description!=soil.description){
            soil.description = receiveData.data.description;
          }
          if(receiveData.data.composition!=soil.composition){
            soil.composition = receiveData.data.composition;
          }
          soil.save().then(updated_culture=>{
            console.log("CUlture updated")
          })
        })
      }
      console.log("Recieve Data : ", receiveData);
      console.log("Buffer Data : ", Buffer.from(data.content));
      channel.ack(data);
    });
    console.log(colors.white.bold("[culture] Start Consumming"));
    console.log(
      `[x] Waiting for messages. To exit press CTRL+C`.black.bgWhite.bold
    );
  } catch (err) {
    console.log(err);
  }
}
