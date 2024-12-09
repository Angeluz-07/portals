package controllers

import javax.inject._
import play.api._
import play.api.mvc._

//import java.io.File
//import com.github.tototoshi.csv._

/**
 * This controller creates an `Action` to handle HTTP requests to the
 * application's home page.
 */
@Singleton
class HomeController @Inject()(val controllerComponents: ControllerComponents) extends BaseController {

  /**
   * Create an Action to render an HTML page.
   *
   * The configuration in the `routes` file means that this method
   * will be called when the application receives a `GET` request with
   * a path of `/`.
   */
  def index() = Action { implicit request: Request[AnyContent] =>
    Ok(views.html.index())
  }

  def printSum(first: Long, second: Long) = Action { implicit request: Request[AnyContent] =>
    val sum = first + second
    Ok(views.html.index())
  }

  def dummy() = Action { implicit request: Request[AnyContent] =>
    val elements: List[(String,String)] = List(
      ("Iraq: elezioni, dopo denunce brogli domani nuovi conteggi","https://cdn.tuttosport.com/img/600/400/2021/10/26/103904635-f90f58ee-f6d4-4002-bf78-7eac86700221.jpg"),
      ("Brahim Diaz negativo al Covid 19: il Milan e Pioli possono sorridere","https://cdn.tuttosport.com/img/600/400/2021/09/27/124308247-66ca927f-9779-4626-99ab-947537a599b3.jpg"),
      ("Le staffette del Torino: con Juric le riserve sono un valore aggiunto","https://cdn.tuttosport.com/img/600/400/2021/10/26/103405207-5775923d-0ef1-4290-b227-937796728bbe.png"))
    Ok(views.html.dummy(elements))
  }
}
