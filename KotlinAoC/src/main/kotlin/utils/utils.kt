package utils

import java.io.File

fun parseDoc(fileName:String) = File(fileName).useLines { it.toList() }



