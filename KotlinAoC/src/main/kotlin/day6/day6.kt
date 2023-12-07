package day6

import utils.parseDoc

fun main() {
    val times = mutableListOf<Long>()
    val distance = mutableListOf<Long>()


    parseDoc("src/main/kotlin/day6/data.txt").forEachIndexed { i, line ->
        if (i == 0) {
            times.addAll(line.parse())
        } else {
            distance.addAll(line.parse())
        }
    }
    println("Task 1: ${calc(times,distance)}")

    val bigTimes = listOf(times.joinToString(separator = "") { "$it" }.toLong())
    val bigDistance = listOf(distance.joinToString(separator = "") { "$it" }.toLong())
    println("Task 2: ${calc(bigTimes,bigDistance)}")

}

fun calc(times: List<Long>, distance: List<Long>) = times.mapIndexed { i, time ->
    (1..time).map { it calculateDistance time }.count { it > distance[i] }
}.reduce(Int::times)

infix fun Long.calculateDistance(totalTime: Long) = this * (totalTime - this)

fun String.parse(): List<Long> = Regex("\\d+").findAll(this).map { it.value.toLong() }.toList()
