package org.trustedanalytics.sparktk.frame.internal.ops.exportdata

import org.apache.commons.csv.{ CSVPrinter, CSVFormat }
import org.apache.spark.rdd.RDD
import org.apache.spark.sql.Row
import org.trustedanalytics.sparktk.frame.internal.{ FrameState, FrameSummarization, BaseFrame }

import scala.collection.mutable.ArrayBuffer

trait ExportToCsvSummarization extends BaseFrame {
  /**
   * Write current frame to HDFS in csv format.
   *
   * Export the frame to a file in csv format as a Hadoop file.
   *
   * @param fileName The HDFS folder path where the files will be created.
   * @param separator Delimiter character.  Defaults to use a comma (`,`).
   */
  def exportToCsv(fileName: String, separator: Char = ',') = {
    execute(ExportToCsv(fileName, separator))
  }
}

case class ExportToCsv(fileName: String, separator: Char) extends FrameSummarization[Unit] {

  override def work(state: FrameState): Unit = {
    ExportToCsv.exportToCsvFile(state.rdd, fileName, separator)
  }
}

object ExportToCsv {

  def exportToCsvFile(rdd: RDD[Row],
                      filename: String,
                      separator: Char) = {

    val csvFormat = CSVFormat.RFC4180.withDelimiter(separator)

    val csvRdd = rdd.map(row => {
      val stringBuilder = new java.lang.StringBuilder
      val printer = new CSVPrinter(stringBuilder, csvFormat)
      val array = row.toSeq.map {
        case null => ""
        case arr: ArrayBuffer[_] => arr.mkString(",")
        case seq: Seq[_] => seq.mkString(",")
        case x => x.toString
      }
      for (i <- array) printer.print(i)
      stringBuilder.toString
    })
    csvRdd.saveAsTextFile(filename)
  }
}

