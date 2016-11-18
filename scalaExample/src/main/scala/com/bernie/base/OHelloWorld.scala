package com.bernie.base

/**
 * Created by bida on 2015/10/22.
 */
class Rational(n:Int, d:Int){
  require(d!=0)
  val number = n
  val denom = d
  override def toString = number + "/" + denom
  def add(that:Rational) =
    new Rational(
      number * that.denom + that.number* denom, denom * that.denom
    )
}
