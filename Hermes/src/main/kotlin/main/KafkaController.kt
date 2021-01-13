package main

import io.streamthoughts.kafka.clients.kafka
import io.streamthoughts.kafka.clients.producer.Acks
import io.streamthoughts.kafka.clients.producer.ProducerContainer
import io.streamthoughts.kafka.clients.producer.callback.closeOnErrorProducerSendCallback
import main.model.Container
import main.model.ContainerSerializer
import org.apache.kafka.common.serialization.StringSerializer

object KafkaController {

    private const val BOOTSTRAP_SERVER = "localhost:9092"
    private const val CLIENT_ID = ""
    private const val TOPIC = ""

    private val PRODUCER: ProducerContainer<String, Container> = kafka(BOOTSTRAP_SERVER) {
        client {
            clientId(CLIENT_ID)
        }

        producer {
            configure {
                acks(Acks.InSyncReplicas)
            }
            keySerializer(StringSerializer())
            valueSerializer(ContainerSerializer())

            defaultTopic(topic = TOPIC)

            onSendError(closeOnErrorProducerSendCallback())

            onSendSuccess { _, _, metadata ->
                println("Record was sent successfully: topic=${metadata.topic()}, partition=${metadata.partition()}, offset=${metadata.offset()} ")
            }
        }
    }

    fun send(messages: List<Container>) {
        PRODUCER.use {
            PRODUCER.init()
            messages.forEach {
                PRODUCER.send(value = it)
            }
        }
    }
}
