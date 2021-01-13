package main

import com.google.gson.Gson
import main.model.Bus


fun main() {
    val classloader = Thread.currentThread().contextClassLoader

    classloader.getResourceAsStream("exampleData.json")?.bufferedReader().use { reader ->
        val container: List<Bus> = Gson().fromJson(reader, Array<Bus>::class.java).toList()

        KafkaController.send(container)
    }
}
