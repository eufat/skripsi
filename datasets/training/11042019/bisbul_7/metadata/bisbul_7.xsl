@field"/></td>
                <td style="padding-left: 0.5em"><xsl:value-of select="."/></td>
              </tr>
              </xsl:if>
            </xsl:for-each>
          </table>
        </p>
      </div>
	  <xsl:if test="/properties/core">
  	    <div class="section">
			<h2>Core</h2>
			<p>
			  <table>
				<tr class="table_header">
				  <th class="attributes">Attributes</th>
				  <th>Value</th>
				</tr>
				<xsl:for-each select="properties/core/key">
				  <xsl:choose>
					<xsl:when test="@field != 'description'">
					  <tr>
						<td style="padding-left: 0.5em">
						  <xsl:value-of select="@field"/>
						</td>
						<td style="padding-left: 0.5em">
						  <xsl:value-of select="."/>
						</td>
					  </tr>
					</xsl:when>
				  </xsl:choose>
				</xsl:for-each>
			  </table>
			</p>
	    </div>
  	  </xsl:if>	
	  <div class="section">
        <h2>Metadata</h2>
        <p>
          <table>
            <tr class="table_header">
              <th class="attributes">Attributes</th>
              <th >Value</th>
            </tr>
            <xsl:for-each select="properties/userdefined/key">
              <xsl:if test="(@field != 'date text') and (@field != 'sample name') and (@field != 'date') and (@field != 'time')and (@field != 'error') and (@field != 'description')">
                <tr>
                  <td style="padding-left: 0.5em">
                    <xsl:value-of select="@field"/>
                  </td>
                  <td style="padding-left: 0.5em">
                    <xsl:copy-of select="."/>
                  </td>
                </tr>
              </xsl:if>
            </xsl:for-each>
          </table>
        </p>
      </div>
    </div>
  </body>
</html>
</xsl:template>
</xsl:stylesheet>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ENVI
description = {
File Imported into ENVI}
file type = ENVI

sensor type = FX10 , Lumo - Recorder v2016-401
acquisition date = DATE(yyyy-mm-dd): 2019-04-11
Start Time = UTC TIME: 09:27:41
Stop Time = UTC TIME: 09:28:02

samples = 512
bands = 224
lines = 512

errors = {none}

interleave = bil
data type = 12
header offset = 0
byte order = 0
x start = 0
y start = 0
default bands = {113, 76, 32}

himg = {1, 512}
vimg = {1, 224}
hroi = {1, 512}
vroi = {1, 224}

fps = 25.00
fps_qpf = 25.10
tint = 10.000000
binning = {2, 2}
trigger mode = Internal
fodis = {0, 0}
sensorid = 1200018_Elcee
acquisitionwindow left = 144
acquisitionwindow top = 223
calibration pack = C:/Users/Public/Documents/Specim/CalibrationPacks/1200018_20180605_FX_calpack.scp

VNIR temperature = 49.70

temperature = {
49.70
}


Wavelength = {
397.66,
400.28,
402.90,
405.52,
408.13,
410.75,
413.37,
416.00,
418.62,
421.24,
423.86,
426.49,
429.12,
431.74,
434.37,
437.00,
439.63,
442.26,
444.89,
447.52,
450.16,
452.79,
455.43,
458.06,
460.70,
463.34,
465.98,
468.62,
471.26,
473.90,
476.54,
479.18,
481.83,
484.47,
487.12,
489.77,
492.42,
495.07,
497.72,
500.37,
503.02,
505.67,
508.32,
510.98,
513.63,
516.29,
518.95,
521.61,
524.27,
526.93,
529.59,
532.25,
534.91,
537.57,
540.24,
542.91,
545.57,
548.24,
550.91,
553.58,
556.25,
558.92,
561.59,
564.26,
566.94,
569.61,
572.29,
574.96,
577.64,
580.32,
583.00,
585.68,
588.36,
591.04,
593.73,
596.41,
599.10,
601.78,
604.47,
607.16,
609.85,
612.53,
615.23,
617.92,
620.61,
623.30,
626.00,
628.69,
631.39,
634.08,
636.78,
639.48,
642.18,
644.88,
647.58,
650.29,
652.99,
655.69,
658.40,
661.10,
663.81,
666.52,
669.23,
671.94,
674.65,
677.36,
680