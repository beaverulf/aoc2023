package day1

import java.io.File

fun main() {
    File("src/main/kotlin/day1/data.txt").useLines { it.toList() }.sumOf {
        it.filter { char -> char.isDigit() }.run {
            "${first()}${last()}".toInt()
        }
    }.run { println(this) }
}