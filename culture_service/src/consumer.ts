import amqp from "amqplib";
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
