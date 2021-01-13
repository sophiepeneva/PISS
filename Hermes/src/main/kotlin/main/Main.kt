package main

import com.google.gson.Gson
import main.model.Container


fun main() {
    val classloader = Thread.currentThread().contextClassLoader

    classloader.getResourceAsStream("exampleData.json")?.bufferedReader().use { reader ->
        val container: List<Container> = Gson().fromJson(reader, Array<Container>::class.java).toList()

        KafkaController.send(container)
    }
}
