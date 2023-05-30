import amqp from "amqplib";
var channel: amqp.Channel, connection: amqp.Connection;
import colors from "colors";

export async function sendData(channels: Array<string>, data: object) {
  try {
    connection = await amqp.connect("amqp://myuser:mypass@localhost:5672");
    channel = await connection.createChannel();

    channels.map((channel_name) => {
      async function transfer(channel_name: string) {
        await channel.assertQueue(channel_name, { durable: true });
        // send data to queue
        channel.sendToQueue(channel_name, Buffer.from(JSON.stringify(data)));

        console.log(
          `Message ${data} BroadCast To Channel ${channel_name}`.bold
        );
      }
      transfer(channel_name);
    });
  } catch (err) {
    console.log(err);
  }
}
