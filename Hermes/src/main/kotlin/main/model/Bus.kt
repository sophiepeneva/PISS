package main.model

import com.google.gson.Gson
import org.apache.kafka.common.errors.SerializationException
import org.apache.kafka.common.serialization.Serializer
import java.io.UnsupportedEncodingException

data class Bus(
    val id: String,
    val number: Int,
    val peopleCountCurrent: Int,
    val peopleGettingOffTheBus: Int,
    val peopleGettingOnTheBus: Int,
    val stationId: String,
    val timestamp: String
)

class BusSerializer : Serializer<Bus> {
    override fun serialize(topic: String, data: Bus?): ByteArray? {
        return try {
            data?.let {
                return Gson().toJson(data).toByteArray()
            }
            null
        } catch (e: UnsupportedEncodingException) {
            throw SerializationException("Error when serializing string to byte[] due to unsupported encoding")
        }
    }
}
