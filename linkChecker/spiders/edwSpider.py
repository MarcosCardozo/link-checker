import scrapy
from linkChecker.items import LinkcheckerItem


class EdwspiderSpider(scrapy.Spider):
    name = "edwSpider"
    allowed_domains = ["edw.walterelias.com.ar"]
    start_urls = ["https://edw.walterelias.com.ar/marcos/"]

    def parse(self, response):
        # Extraer la URL y el estado de la respuesta
        url = response.url
        estado = response.status

        # Extraer los enlaces de la página
        enlaces = response.css('a::attr(href)').getall()

        # Crear un objeto LinkcheckerItem con la URL, el estado y los enlaces
        pagina = LinkcheckerItem(url=url, estado=estado, enlaces=enlaces)

        # Devolver el objeto LinkcheckerItem
        yield pagina
        
        # Seguir los enlaces encontrados
        for enlace in enlaces:
            yield response.follow(enlace, callback=self.parse)
