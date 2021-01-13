package main.model

import com.google.gson.Gson
import org.apache.kafka.common.errors.SerializationException
import org.apache.kafka.common.serialization.Serializer
import java.io.UnsupportedEncodingException

data class Container(
    val bus: Bus,
    val id: String,
    val people_expected_at_next_station: Int,
    val people_expected_to_get_off_at_next_station: Int,
    val station: Station,
    val time: String,
    val time_by_schedule: String
)

class ContainerSerializer : Serializer<Container> {
    override fun serialize(topic: String, data: Container?): ByteArray? {
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
