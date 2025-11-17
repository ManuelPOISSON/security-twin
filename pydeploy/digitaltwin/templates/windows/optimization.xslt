<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output omit-xml-declaration="yes" indent="yes"/>
  
  <!-- Copier tout le XML par défaut -->
  <xsl:template match="node()|@*">
    <xsl:copy>
      <xsl:apply-templates select="node()|@*"/>
    </xsl:copy>
  </xsl:template>

  <!-- Modifier <features> -->
  <xsl:template match="/domain/features">
    <xsl:copy>
      <acpi/>
      <apic/>
      <hyperv mode="custom">
        <relaxed state="on"/>
        <vapic state="on"/>
        <spinlocks state="on" retries="8191"/>
        <vpindex state="on"/>
        <runtime state="on"/>
        <synic state="on"/>
        <stimer state="on"/>
        <frequencies state="on"/>
        <tlbflush state="on"/>
        <ipi state="on"/>
        <evmcs state="on"/>
        <avic state="on"/>
      </hyperv>
      <vmport state="off"/>
    </xsl:copy>
  </xsl:template>

  <!-- Supprimer l'ancienne <clock> et en ajouter une nouvelle -->
  <xsl:template match="/domain/clock" />

  <xsl:template match="/domain">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
      <clock offset="localtime">
        <timer name="rtc" tickpolicy="catchup"/>
        <timer name="pit" tickpolicy="delay"/>
        <timer name="hpet" present="no"/>
        <timer name="hypervclock" present="yes"/>
      </clock>
    </xsl:copy>
  </xsl:template>
  <xsl:template match="/domain/devices/disk[@device='cdrom']/target/@bus">
    <xsl:attribute name="bus">
      <xsl:value-of select="'sata'"/>
    </xsl:attribute>
  </xsl:template>
  
  <xsl:template match="/domain/devices/disk[@device='cdrom']/alias" />
</xsl:stylesheet>
