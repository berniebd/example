import java.util.UUID.randomUUID

object Example{
  def main(args: Array[String]): Unit ={
    val start = "2012-12-13"
    val content = s"""$start, %s """
    println(content)
    println("---------")
    println(content.format("world"))
  }
}
