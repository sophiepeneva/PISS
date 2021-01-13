plugins {
    id("java")
    id("org.jetbrains.kotlin.jvm") version "1.4.20"
}

repositories {
    mavenCentral()
}

dependencies {
    implementation("org.jetbrains.kotlin:kotlin-stdlib")
    implementation("io.streamthoughts:kafka-clients-kotlin:0.2.0")
    implementation("com.google.code.gson:gson:2.8.6")
}
