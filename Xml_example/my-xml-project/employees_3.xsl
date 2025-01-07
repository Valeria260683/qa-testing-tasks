<!--XML19. Преобразование XML в HTML с использованием XSLT
Задание: Создайте XSLT-шаблон для преобразования XML в HTML-таблицу.-->

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/employees">
  <html>
  <body>
    <table border="1">
      <thead>
        <tr>
          <th>ID</th>
          <th>Имя</th>
          <th>Должность</th>
          <th>Зарплата</th>
        </tr>
      </thead>
      <tbody>
        <xsl:apply-templates select="employee"/>
      </tbody>
    </table>
  </body>
  </html>
</xsl:template>

<xsl:template match="employee">
  <tr>
    <td><xsl:value-of select="@id"/></td>
    <td><xsl:value-of select="name"/></td>
    <td><xsl:value-of select="position"/></td>
    <td><xsl:value-of select="salary"/></td>
  </tr>
</xsl:template>
</xsl:stylesheet>