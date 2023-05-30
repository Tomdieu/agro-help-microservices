import amqp from "amqplib/callback_api";
import Culture from "./Culture";

const username = "myuser";
const password = "mypass";
const host = "localhost";
const url = `amqp://${username}:${password}@${host}`;

type MessageType = {
  type: string;
  data: object;
};

amqp.connect(url, (err, conn) => {
  if (err) {
    throw err;
  }

  conn.createChannel((err, ch) => {
    if (err) {
      throw err;
    }

    const exchange = "culture_exchange";
    const routingKey = "culture";

    ch.assertExchange(exchange, "direct", { durable: true });

    Culture.addHook("afterCreate", (culture) => {
      const message = {
        type: "created",
        data: culture.toJSON(),
      };

      publishToQueues(message);
    });

    Culture.addHook("afterUpdate", (culture) => {
      const message = {
        type: "updated",
        data: culture.toJSON(),
      };

      publishToQueues(message);
    });

    Culture.addHook("afterDestroy", (culture: Culture) => {
      const message = {
        type: "deleted",
        data: { id: culture.id },
      };

      publishToQueues(message);
    });

    function publishToQueues(message: MessageType) {
      const data = JSON.stringify(message);

      ch.publish(exchange, "soil", Buffer.from(data));
      console.log(`[x] Sent ${data} to soil queue`);

      ch.publish(exchange, "parcel", Buffer.from(data));
      console.log(`[x] Sent ${data} to parcel queue`);
    }
  });
});
