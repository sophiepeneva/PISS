package main

import io.streamthoughts.kafka.clients.kafka
import io.streamthoughts.kafka.clients.producer.Acks
import io.streamthoughts.kafka.clients.producer.ProducerContainer
import io.streamthoughts.kafka.clients.producer.callback.closeOnErrorProducerSendCallback
import main.model.Bus
import main.model.BusSerializer
import org.apache.kafka.common.serialization.StringSerializer

object KafkaController {

    private const val BOOTSTRAP_SERVER = "localhost:9092"
    private const val CLIENT_ID = "Hermes"
    private const val TOPIC = "quickstart-events"

    private val PRODUCER: ProducerContainer<String, Bus> = kafka(BOOTSTRAP_SERVER) {
        client {
            clientId(CLIENT_ID)
        }

        producer {
            configure {
                acks(Acks.InSyncReplicas)
            }
            keySerializer(StringSerializer())
            valueSerializer(BusSerializer())

            defaultTopic(topic = TOPIC)

            onSendError(closeOnErrorProducerSendCallback())

            onSendSuccess { _, _, metadata ->
                println("Record was sent successfully: topic=${metadata.topic()}, partition=${metadata.partition()}, offset=${metadata.offset()} ")
            }
        }
    }

    fun send(messages: List<Bus>) {
        PRODUCER.use {
            PRODUCER.init()
            messages.forEach {
                PRODUCER.send(value = it)
            }
        }
    }
}
