# ahgDataMigrationPlugin - Technical Documentation

**Plugin Version:** 1.4.0
**Last Updated:** 2026-02-03
**Framework:** AtoM AHG Framework (Laravel Query Builder + Symfony 1.x)

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Directory Structure](#2-directory-structure)
3. [Database Schema](#3-database-schema)
4. [Core Components](#4-core-components)
5. [Validation Framework](#5-validation-framework)
6. [Parsers](#6-parsers)
7. [Exporters](#7-exporters)
8. [Preservica Integration](#8-preservica-integration)
9. [Sector Definitions](#9-sector-definitions)
10. [CLI Tasks](#10-cli-tasks)
11. [Gearman Jobs](#11-gearman-jobs)
12. [Extending the Plugin](#12-extending-the-plugin)
13. [Digital Object Import](#13-digital-object-import)

---

## 1. Architecture Overview
<div style="overflow-x:auto;margin:1rem 0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 502 404" style="max-width:100%;height:auto;font-family:ui-monospace,Menlo,Consolas,monospace"><rect x="0.5" y="0.5" width="501" height="403" rx="8" fill="#f7faf9" stroke="#d8e6e3"/><line x1="13.6" y1="18.0" x2="17.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="18.0" x2="13.6" y2="26.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="18.0" x2="20.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="18.0" x2="24.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="18.0" x2="28.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="18.0" x2="31.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="31.6" y1="18.0" x2="35.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="18.0" x2="38.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="18.0" x2="42.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="18.0" x2="46.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="18.0" x2="49.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="18.0" x2="53.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="18.0" x2="56.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="18.0" x2="60.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="18.0" x2="64.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="18.0" x2="67.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="18.0" x2="71.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="18.0" x2="74.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="18.0" x2="78.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="18.0" x2="82.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="18.0" x2="85.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="18.0" x2="89.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="89.2" y1="18.0" x2="92.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="92.8" y1="18.0" x2="96.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="18.0" x2="100.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="18.0" x2="103.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="18.0" x2="107.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="18.0" x2="110.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="18.0" x2="114.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="18.0" x2="118.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="118.0" y1="18.0" x2="121.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="121.6" y1="18.0" x2="125.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="125.2" y1="18.0" x2="128.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="128.8" y1="18.0" x2="132.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="132.4" y1="18.0" x2="136.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="136.0" y1="18.0" x2="139.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="139.6" y1="18.0" x2="143.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="18.0" x2="146.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="146.8" y1="18.0" x2="150.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="150.4" y1="18.0" x2="154.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="154.0" y1="18.0" x2="157.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="18.0" x2="161.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="161.2" y1="18.0" x2="164.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="18.0" x2="168.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="168.4" y1="18.0" x2="172.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="18.0" x2="175.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="175.6" y1="18.0" x2="179.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="179.2" y1="18.0" x2="182.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="182.8" y1="18.0" x2="186.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="186.4" y1="18.0" x2="190.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="190.0" y1="18.0" x2="193.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="193.6" y1="18.0" x2="197.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="197.2" y1="18.0" x2="200.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="200.8" y1="18.0" x2="204.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="204.4" y1="18.0" x2="208.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="208.0" y1="18.0" x2="211.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="211.6" y1="18.0" x2="215.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="215.2" y1="18.0" x2="218.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="218.8" y1="18.0" x2="222.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="222.4" y1="18.0" x2="226.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="226.0" y1="18.0" x2="229.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="229.6" y1="18.0" x2="233.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="233.2" y1="18.0" x2="236.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="236.8" y1="18.0" x2="240.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="240.4" y1="18.0" x2="244.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="244.0" y1="18.0" x2="247.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="247.6" y1="18.0" x2="251.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="18.0" x2="254.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="254.8" y1="18.0" x2="258.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="258.4" y1="18.0" x2="262.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="262.0" y1="18.0" x2="265.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="265.6" y1="18.0" x2="269.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="269.2" y1="18.0" x2="272.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="272.8" y1="18.0" x2="276.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="276.4" y1="18.0" x2="280.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="280.0" y1="18.0" x2="283.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="283.6" y1="18.0" x2="287.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="287.2" y1="18.0" x2="290.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="290.8" y1="18.0" x2="294.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="18.0" x2="298.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="298.0" y1="18.0" x2="301.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="301.6" y1="18.0" x2="305.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="305.2" y1="18.0" x2="308.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="308.8" y1="18.0" x2="312.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="312.4" y1="18.0" x2="316.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="316.0" y1="18.0" x2="319.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="319.6" y1="18.0" x2="323.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="323.2" y1="18.0" x2="326.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="326.8" y1="18.0" x2="330.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="330.4" y1="18.0" x2="334.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="334.0" y1="18.0" x2="337.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="337.6" y1="18.0" x2="341.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="341.2" y1="18.0" x2="344.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="344.8" y1="18.0" x2="348.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="348.4" y1="18.0" x2="352.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="18.0" x2="355.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="355.6" y1="18.0" x2="359.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="359.2" y1="18.0" x2="362.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="362.8" y1="18.0" x2="366.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="18.0" x2="370.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="370.0" y1="18.0" x2="373.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="373.6" y1="18.0" x2="377.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="377.2" y1="18.0" x2="380.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="380.8" y1="18.0" x2="384.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="384.4" y1="18.0" x2="388.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="388.0" y1="18.0" x2="391.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="391.6" y1="18.0" x2="395.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="395.2" y1="18.0" x2="398.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="398.8" y1="18.0" x2="402.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="402.4" y1="18.0" x2="406.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="406.0" y1="18.0" x2="409.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="409.6" y1="18.0" x2="413.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="413.2" y1="18.0" x2="416.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="18.0" x2="420.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="420.4" y1="18.0" x2="424.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="18.0" x2="427.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="427.6" y1="18.0" x2="431.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="18.0" x2="434.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="434.8" y1="18.0" x2="438.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="438.4" y1="18.0" x2="442.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="442.0" y1="18.0" x2="445.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="445.6" y1="18.0" x2="449.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="449.2" y1="18.0" x2="452.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="452.8" y1="18.0" x2="456.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="456.4" y1="18.0" x2="460.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="460.0" y1="18.0" x2="463.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="463.6" y1="18.0" x2="467.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="18.0" x2="470.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="470.8" y1="18.0" x2="474.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="474.4" y1="18.0" x2="478.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="478.0" y1="18.0" x2="481.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="481.6" y1="18.0" x2="485.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="485.2" y1="18.0" x2="488.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="18.0" x2="488.8" y2="26.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="26.0" x2="13.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="34.0" x2="13.6" y2="42.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="26.0" x2="488.8" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="34.0" x2="488.8" y2="42.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="17.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="42.0" x2="13.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="13.6" y2="58.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="50.0" x2="20.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="50.0" x2="24.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="50.0" x2="28.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="50.0" x2="31.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="31.6" y1="50.0" x2="35.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="50.0" x2="38.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="50.0" x2="42.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="50.0" x2="46.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="50.0" x2="49.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="50.0" x2="53.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="50.0" x2="56.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="50.0" x2="60.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="50.0" x2="64.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="50.0" x2="67.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="50.0" x2="71.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="50.0" x2="74.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="50.0" x2="78.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="50.0" x2="82.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="50.0" x2="85.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="50.0" x2="89.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="89.2" y1="50.0" x2="92.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="92.8" y1="50.0" x2="96.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="50.0" x2="100.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="50.0" x2="103.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="50.0" x2="107.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="50.0" x2="110.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="50.0" x2="114.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="50.0" x2="118.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="118.0" y1="50.0" x2="121.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="121.6" y1="50.0" x2="125.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="125.2" y1="50.0" x2="128.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="128.8" y1="50.0" x2="132.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="132.4" y1="50.0" x2="136.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="136.0" y1="50.0" x2="139.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="139.6" y1="50.0" x2="143.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="50.0" x2="146.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="146.8" y1="50.0" x2="150.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="150.4" y1="50.0" x2="154.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="154.0" y1="50.0" x2="157.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="50.0" x2="161.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="161.2" y1="50.0" x2="164.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="50.0" x2="168.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="168.4" y1="50.0" x2="172.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="50.0" x2="175.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="175.6" y1="50.0" x2="179.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="179.2" y1="50.0" x2="182.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="182.8" y1="50.0" x2="186.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="186.4" y1="50.0" x2="190.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="190.0" y1="50.0" x2="193.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="193.6" y1="50.0" x2="197.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="197.2" y1="50.0" x2="200.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="200.8" y1="50.0" x2="204.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="204.4" y1="50.0" x2="208.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="208.0" y1="50.0" x2="211.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="211.6" y1="50.0" x2="215.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="215.2" y1="50.0" x2="218.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="218.8" y1="50.0" x2="222.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="222.4" y1="50.0" x2="226.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="226.0" y1="50.0" x2="229.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="229.6" y1="50.0" x2="233.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="233.2" y1="50.0" x2="236.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="236.8" y1="50.0" x2="240.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="240.4" y1="50.0" x2="244.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="244.0" y1="50.0" x2="247.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="247.6" y1="50.0" x2="251.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="50.0" x2="254.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="254.8" y1="50.0" x2="258.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="258.4" y1="50.0" x2="262.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="262.0" y1="50.0" x2="265.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="265.6" y1="50.0" x2="269.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="269.2" y1="50.0" x2="272.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="272.8" y1="50.0" x2="276.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="276.4" y1="50.0" x2="280.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="280.0" y1="50.0" x2="283.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="283.6" y1="50.0" x2="287.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="287.2" y1="50.0" x2="290.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="290.8" y1="50.0" x2="294.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="50.0" x2="298.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="298.0" y1="50.0" x2="301.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="301.6" y1="50.0" x2="305.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="305.2" y1="50.0" x2="308.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="308.8" y1="50.0" x2="312.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="312.4" y1="50.0" x2="316.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="316.0" y1="50.0" x2="319.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="319.6" y1="50.0" x2="323.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="323.2" y1="50.0" x2="326.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="326.8" y1="50.0" x2="330.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="330.4" y1="50.0" x2="334.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="334.0" y1="50.0" x2="337.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="337.6" y1="50.0" x2="341.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="341.2" y1="50.0" x2="344.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="344.8" y1="50.0" x2="348.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="348.4" y1="50.0" x2="352.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="50.0" x2="355.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="355.6" y1="50.0" x2="359.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="359.2" y1="50.0" x2="362.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="362.8" y1="50.0" x2="366.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="50.0" x2="370.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="370.0" y1="50.0" x2="373.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="373.6" y1="50.0" x2="377.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="377.2" y1="50.0" x2="380.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="380.8" y1="50.0" x2="384.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="384.4" y1="50.0" x2="388.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="388.0" y1="50.0" x2="391.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="391.6" y1="50.0" x2="395.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="395.2" y1="50.0" x2="398.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="398.8" y1="50.0" x2="402.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="402.4" y1="50.0" x2="406.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="406.0" y1="50.0" x2="409.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="409.6" y1="50.0" x2="413.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="413.2" y1="50.0" x2="416.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="50.0" x2="420.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="420.4" y1="50.0" x2="424.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="50.0" x2="427.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="427.6" y1="50.0" x2="431.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="50.0" x2="434.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="434.8" y1="50.0" x2="438.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="438.4" y1="50.0" x2="442.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="442.0" y1="50.0" x2="445.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="445.6" y1="50.0" x2="449.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="449.2" y1="50.0" x2="452.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="452.8" y1="50.0" x2="456.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="456.4" y1="50.0" x2="460.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="460.0" y1="50.0" x2="463.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="463.6" y1="50.0" x2="467.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="50.0" x2="470.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="470.8" y1="50.0" x2="474.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="474.4" y1="50.0" x2="478.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="478.0" y1="50.0" x2="481.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="481.6" y1="50.0" x2="485.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="485.2" y1="50.0" x2="488.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="42.0" x2="488.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="50.0" x2="488.8" y2="58.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="58.0" x2="13.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="13.6" y2="74.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="58.0" x2="488.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="66.0" x2="488.8" y2="74.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="74.0" x2="13.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="82.0" x2="13.6" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="74.0" x2="488.8" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="82.0" x2="488.8" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="98.0" x2="17.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="90.0" x2="13.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="98.0" x2="13.6" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="98.0" x2="20.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="98.0" x2="24.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="98.0" x2="28.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="98.0" x2="31.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="31.6" y1="98.0" x2="35.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="98.0" x2="38.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="98.0" x2="42.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="98.0" x2="46.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="98.0" x2="49.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="98.0" x2="53.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="98.0" x2="56.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="98.0" x2="60.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="98.0" x2="64.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="98.0" x2="67.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="98.0" x2="71.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="98.0" x2="74.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="98.0" x2="78.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="98.0" x2="82.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="98.0" x2="85.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="98.0" x2="89.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="89.2" y1="98.0" x2="92.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="92.8" y1="98.0" x2="96.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="98.0" x2="100.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="98.0" x2="103.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="98.0" x2="107.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="98.0" x2="110.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="98.0" x2="114.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="98.0" x2="118.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="118.0" y1="98.0" x2="121.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="121.6" y1="98.0" x2="125.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="125.2" y1="98.0" x2="128.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="128.8" y1="98.0" x2="132.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="132.4" y1="98.0" x2="136.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="136.0" y1="98.0" x2="139.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="139.6" y1="98.0" x2="143.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="98.0" x2="146.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="146.8" y1="98.0" x2="150.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="150.4" y1="98.0" x2="154.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="154.0" y1="98.0" x2="157.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="98.0" x2="161.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="161.2" y1="98.0" x2="164.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="98.0" x2="168.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="168.4" y1="98.0" x2="172.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="98.0" x2="175.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="175.6" y1="98.0" x2="179.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="179.2" y1="98.0" x2="182.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="182.8" y1="98.0" x2="186.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="186.4" y1="98.0" x2="190.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="190.0" y1="98.0" x2="193.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="193.6" y1="98.0" x2="197.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="197.2" y1="98.0" x2="200.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="200.8" y1="98.0" x2="204.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="204.4" y1="98.0" x2="208.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="208.0" y1="98.0" x2="211.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="211.6" y1="98.0" x2="215.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="215.2" y1="98.0" x2="218.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="218.8" y1="98.0" x2="222.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="222.4" y1="98.0" x2="226.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="226.0" y1="98.0" x2="229.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="229.6" y1="98.0" x2="233.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="233.2" y1="98.0" x2="236.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="236.8" y1="98.0" x2="240.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="240.4" y1="98.0" x2="244.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="244.0" y1="98.0" x2="247.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="247.6" y1="98.0" x2="251.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="98.0" x2="254.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="254.8" y1="98.0" x2="258.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="258.4" y1="98.0" x2="262.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="262.0" y1="98.0" x2="265.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="265.6" y1="98.0" x2="269.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="269.2" y1="98.0" x2="272.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="272.8" y1="98.0" x2="276.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="276.4" y1="98.0" x2="280.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="280.0" y1="98.0" x2="283.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="283.6" y1="98.0" x2="287.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="287.2" y1="98.0" x2="290.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="290.8" y1="98.0" x2="294.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="98.0" x2="298.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="298.0" y1="98.0" x2="301.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="301.6" y1="98.0" x2="305.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="305.2" y1="98.0" x2="308.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="308.8" y1="98.0" x2="312.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="312.4" y1="98.0" x2="316.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="316.0" y1="98.0" x2="319.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="319.6" y1="98.0" x2="323.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="323.2" y1="98.0" x2="326.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="326.8" y1="98.0" x2="330.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="330.4" y1="98.0" x2="334.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="334.0" y1="98.0" x2="337.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="337.6" y1="98.0" x2="341.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="341.2" y1="98.0" x2="344.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="344.8" y1="98.0" x2="348.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="348.4" y1="98.0" x2="352.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="98.0" x2="355.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="355.6" y1="98.0" x2="359.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="359.2" y1="98.0" x2="362.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="362.8" y1="98.0" x2="366.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="98.0" x2="370.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="370.0" y1="98.0" x2="373.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="373.6" y1="98.0" x2="377.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="377.2" y1="98.0" x2="380.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="380.8" y1="98.0" x2="384.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="384.4" y1="98.0" x2="388.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="388.0" y1="98.0" x2="391.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="391.6" y1="98.0" x2="395.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="395.2" y1="98.0" x2="398.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="398.8" y1="98.0" x2="402.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="402.4" y1="98.0" x2="406.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="406.0" y1="98.0" x2="409.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="409.6" y1="98.0" x2="413.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="413.2" y1="98.0" x2="416.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="98.0" x2="420.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="420.4" y1="98.0" x2="424.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="98.0" x2="427.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="427.6" y1="98.0" x2="431.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="98.0" x2="434.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="434.8" y1="98.0" x2="438.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="438.4" y1="98.0" x2="442.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="442.0" y1="98.0" x2="445.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="445.6" y1="98.0" x2="449.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="449.2" y1="98.0" x2="452.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="452.8" y1="98.0" x2="456.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="456.4" y1="98.0" x2="460.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="460.0" y1="98.0" x2="463.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="463.6" y1="98.0" x2="467.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="98.0" x2="470.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="470.8" y1="98.0" x2="474.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="474.4" y1="98.0" x2="478.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="478.0" y1="98.0" x2="481.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="481.6" y1="98.0" x2="485.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="485.2" y1="98.0" x2="488.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="90.0" x2="488.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="98.0" x2="488.8" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="106.0" x2="13.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="114.0" x2="13.6" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="106.0" x2="157.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="114.0" x2="157.6" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="301.6" y1="106.0" x2="301.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="301.6" y1="114.0" x2="301.6" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="106.0" x2="488.8" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="114.0" x2="488.8" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="130.0" x2="17.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="122.0" x2="13.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="130.0" x2="13.6" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="130.0" x2="20.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="130.0" x2="24.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="130.0" x2="28.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="130.0" x2="31.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="31.6" y1="130.0" x2="35.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="130.0" x2="38.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="130.0" x2="42.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="130.0" x2="46.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="130.0" x2="49.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="130.0" x2="53.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="130.0" x2="56.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="130.0" x2="60.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="130.0" x2="64.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="130.0" x2="67.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="130.0" x2="71.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="130.0" x2="74.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="130.0" x2="78.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="130.0" x2="82.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="130.0" x2="85.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="130.0" x2="89.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="89.2" y1="130.0" x2="92.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="92.8" y1="130.0" x2="96.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="130.0" x2="100.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="130.0" x2="103.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="130.0" x2="107.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="130.0" x2="110.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="130.0" x2="114.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="130.0" x2="118.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="118.0" y1="130.0" x2="121.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="121.6" y1="130.0" x2="125.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="125.2" y1="130.0" x2="128.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="128.8" y1="130.0" x2="132.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="132.4" y1="130.0" x2="136.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="136.0" y1="130.0" x2="139.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="139.6" y1="130.0" x2="143.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="130.0" x2="146.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="146.8" y1="130.0" x2="150.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="150.4" y1="130.0" x2="154.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="154.0" y1="130.0" x2="157.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="130.0" x2="161.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="161.2" y1="130.0" x2="164.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="130.0" x2="168.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="168.4" y1="130.0" x2="172.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="130.0" x2="175.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="175.6" y1="130.0" x2="179.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="179.2" y1="130.0" x2="182.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="182.8" y1="130.0" x2="186.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="186.4" y1="130.0" x2="190.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="190.0" y1="130.0" x2="193.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="193.6" y1="130.0" x2="197.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="197.2" y1="130.0" x2="200.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="200.8" y1="130.0" x2="204.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="204.4" y1="130.0" x2="208.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="208.0" y1="130.0" x2="211.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="211.6" y1="130.0" x2="215.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="215.2" y1="130.0" x2="218.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="218.8" y1="130.0" x2="222.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="222.4" y1="130.0" x2="226.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="226.0" y1="130.0" x2="229.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="229.6" y1="130.0" x2="233.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="233.2" y1="130.0" x2="236.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="236.8" y1="130.0" x2="240.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="240.4" y1="130.0" x2="244.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="244.0" y1="130.0" x2="247.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="247.6" y1="130.0" x2="251.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="130.0" x2="254.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="254.8" y1="130.0" x2="258.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="258.4" y1="130.0" x2="262.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="262.0" y1="130.0" x2="265.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="265.6" y1="130.0" x2="269.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="269.2" y1="130.0" x2="272.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="272.8" y1="130.0" x2="276.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="276.4" y1="130.0" x2="280.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="280.0" y1="130.0" x2="283.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="283.6" y1="130.0" x2="287.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="287.2" y1="130.0" x2="290.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="290.8" y1="130.0" x2="294.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="130.0" x2="298.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="298.0" y1="130.0" x2="301.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="301.6" y1="130.0" x2="305.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="305.2" y1="130.0" x2="308.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="308.8" y1="130.0" x2="312.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="312.4" y1="130.0" x2="316.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="316.0" y1="130.0" x2="319.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="319.6" y1="130.0" x2="323.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="323.2" y1="130.0" x2="326.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="326.8" y1="130.0" x2="330.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="330.4" y1="130.0" x2="334.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="334.0" y1="130.0" x2="337.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="337.6" y1="130.0" x2="341.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="341.2" y1="130.0" x2="344.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="344.8" y1="130.0" x2="348.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="348.4" y1="130.0" x2="352.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="130.0" x2="355.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="355.6" y1="130.0" x2="359.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="359.2" y1="130.0" x2="362.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="362.8" y1="130.0" x2="366.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="130.0" x2="370.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="370.0" y1="130.0" x2="373.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="373.6" y1="130.0" x2="377.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="377.2" y1="130.0" x2="380.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="380.8" y1="130.0" x2="384.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="384.4" y1="130.0" x2="388.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="388.0" y1="130.0" x2="391.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="391.6" y1="130.0" x2="395.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="395.2" y1="130.0" x2="398.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="398.8" y1="130.0" x2="402.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="402.4" y1="130.0" x2="406.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="406.0" y1="130.0" x2="409.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="409.6" y1="130.0" x2="413.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="413.2" y1="130.0" x2="416.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="130.0" x2="420.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="420.4" y1="130.0" x2="424.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="130.0" x2="427.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="427.6" y1="130.0" x2="431.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="130.0" x2="434.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="434.8" y1="130.0" x2="438.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="438.4" y1="130.0" x2="442.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="442.0" y1="130.0" x2="445.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="445.6" y1="130.0" x2="449.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="449.2" y1="130.0" x2="452.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="452.8" y1="130.0" x2="456.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="456.4" y1="130.0" x2="460.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="460.0" y1="130.0" x2="463.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="463.6" y1="130.0" x2="467.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="130.0" x2="470.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="470.8" y1="130.0" x2="474.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="474.4" y1="130.0" x2="478.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="478.0" y1="130.0" x2="481.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="481.6" y1="130.0" x2="485.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="485.2" y1="130.0" x2="488.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="122.0" x2="488.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="130.0" x2="488.8" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="138.0" x2="13.6" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="146.0" x2="13.6" y2="154.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="138.0" x2="488.8" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="146.0" x2="488.8" y2="154.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="154.0" x2="13.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="162.0" x2="13.6" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="162.0" x2="38.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="162.0" x2="35.2" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="162.0" x2="42.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="162.0" x2="46.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="162.0" x2="49.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="162.0" x2="53.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="162.0" x2="56.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="162.0" x2="60.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="162.0" x2="64.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="162.0" x2="67.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="162.0" x2="71.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="162.0" x2="74.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="162.0" x2="78.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="162.0" x2="82.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="162.0" x2="85.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="162.0" x2="89.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="89.2" y1="162.0" x2="92.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="92.8" y1="162.0" x2="96.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="162.0" x2="100.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="162.0" x2="103.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="162.0" x2="107.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="162.0" x2="110.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="162.0" x2="114.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="162.0" x2="118.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="118.0" y1="162.0" x2="121.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="121.6" y1="162.0" x2="125.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="125.2" y1="162.0" x2="128.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="128.8" y1="162.0" x2="132.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="132.4" y1="162.0" x2="136.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="136.0" y1="162.0" x2="139.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="139.6" y1="162.0" x2="143.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="162.0" x2="146.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="162.0" x2="143.2" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="146.8" y1="162.0" x2="150.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="150.4" y1="162.0" x2="154.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="154.0" y1="162.0" x2="157.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="162.0" x2="161.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="161.2" y1="162.0" x2="164.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="162.0" x2="168.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="168.4" y1="162.0" x2="172.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="162.0" x2="175.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="175.6" y1="162.0" x2="179.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="179.2" y1="162.0" x2="182.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="182.8" y1="162.0" x2="186.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="186.4" y1="162.0" x2="190.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="190.0" y1="162.0" x2="193.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="193.6" y1="162.0" x2="197.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="197.2" y1="162.0" x2="200.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="200.8" y1="162.0" x2="204.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="204.4" y1="162.0" x2="208.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="208.0" y1="162.0" x2="211.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="211.6" y1="162.0" x2="215.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="215.2" y1="162.0" x2="218.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="218.8" y1="162.0" x2="222.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="222.4" y1="162.0" x2="226.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="226.0" y1="162.0" x2="229.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="229.6" y1="162.0" x2="233.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="233.2" y1="162.0" x2="236.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="236.8" y1="162.0" x2="240.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="240.4" y1="162.0" x2="244.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="244.0" y1="162.0" x2="247.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="247.6" y1="162.0" x2="251.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="162.0" x2="254.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="162.0" x2="251.2" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="254.8" y1="162.0" x2="258.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="258.4" y1="162.0" x2="262.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="262.0" y1="162.0" x2="265.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="265.6" y1="162.0" x2="269.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="269.2" y1="162.0" x2="272.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="272.8" y1="162.0" x2="276.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="276.4" y1="162.0" x2="280.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="280.0" y1="162.0" x2="283.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="283.6" y1="162.0" x2="287.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="287.2" y1="162.0" x2="290.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="290.8" y1="162.0" x2="294.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="162.0" x2="298.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="298.0" y1="162.0" x2="301.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="301.6" y1="162.0" x2="305.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="305.2" y1="162.0" x2="308.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="308.8" y1="162.0" x2="312.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="312.4" y1="162.0" x2="316.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="316.0" y1="162.0" x2="319.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="319.6" y1="162.0" x2="323.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="323.2" y1="162.0" x2="326.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="326.8" y1="162.0" x2="330.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="330.4" y1="162.0" x2="334.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="334.0" y1="162.0" x2="337.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="337.6" y1="162.0" x2="341.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="341.2" y1="162.0" x2="344.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="344.8" y1="162.0" x2="348.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="348.4" y1="162.0" x2="352.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="162.0" x2="355.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="162.0" x2="352.0" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="355.6" y1="162.0" x2="359.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="359.2" y1="162.0" x2="362.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="362.8" y1="162.0" x2="366.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="162.0" x2="370.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="370.0" y1="162.0" x2="373.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="373.6" y1="162.0" x2="377.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="377.2" y1="162.0" x2="380.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="380.8" y1="162.0" x2="384.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="384.4" y1="162.0" x2="388.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="388.0" y1="162.0" x2="391.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="391.6" y1="162.0" x2="395.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="395.2" y1="162.0" x2="398.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="398.8" y1="162.0" x2="402.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="402.4" y1="162.0" x2="406.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="406.0" y1="162.0" x2="409.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="409.6" y1="162.0" x2="413.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="413.2" y1="162.0" x2="416.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="162.0" x2="420.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="420.4" y1="162.0" x2="424.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="162.0" x2="427.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="427.6" y1="162.0" x2="431.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="162.0" x2="434.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="434.8" y1="162.0" x2="438.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="438.4" y1="162.0" x2="442.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="442.0" y1="162.0" x2="445.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="445.6" y1="162.0" x2="449.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="449.2" y1="162.0" x2="452.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="452.8" y1="162.0" x2="456.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="456.4" y1="162.0" x2="460.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="460.0" y1="162.0" x2="463.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="463.6" y1="162.0" x2="467.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="162.0" x2="467.2" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="154.0" x2="488.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="162.0" x2="488.8" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="170.0" x2="13.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="178.0" x2="13.6" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="170.0" x2="35.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="178.0" x2="35.2" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="170.0" x2="143.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="178.0" x2="143.2" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="170.0" x2="251.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="178.0" x2="251.2" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="170.0" x2="352.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="178.0" x2="352.0" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="170.0" x2="467.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="178.0" x2="467.2" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="170.0" x2="488.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="178.0" x2="488.8" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="186.0" x2="13.6" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="194.0" x2="13.6" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="186.0" x2="35.2" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="194.0" x2="35.2" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="186.0" x2="143.2" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="194.0" x2="143.2" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="186.0" x2="251.2" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="194.0" x2="251.2" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="186.0" x2="352.0" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="194.0" x2="352.0" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="186.0" x2="467.2" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="194.0" x2="467.2" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="186.0" x2="488.8" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="194.0" x2="488.8" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="202.0" x2="13.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="210.0" x2="13.6" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="210.0" x2="38.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="202.0" x2="35.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="210.0" x2="42.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="210.0" x2="46.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="210.0" x2="49.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="210.0" x2="53.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="210.0" x2="56.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="210.0" x2="60.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="210.0" x2="64.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="210.0" x2="67.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="210.0" x2="71.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="210.0" x2="74.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="210.0" x2="78.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="210.0" x2="82.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="210.0" x2="85.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="210.0" x2="89.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="89.2" y1="210.0" x2="92.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="92.8" y1="210.0" x2="96.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="210.0" x2="100.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="210.0" x2="103.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="210.0" x2="107.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="210.0" x2="110.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="210.0" x2="114.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="210.0" x2="118.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="118.0" y1="210.0" x2="121.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="121.6" y1="210.0" x2="125.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="125.2" y1="210.0" x2="128.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="128.8" y1="210.0" x2="132.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="132.4" y1="210.0" x2="136.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="136.0" y1="210.0" x2="139.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="139.6" y1="210.0" x2="143.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="210.0" x2="146.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="202.0" x2="143.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="146.8" y1="210.0" x2="150.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="150.4" y1="210.0" x2="154.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="154.0" y1="210.0" x2="157.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="210.0" x2="161.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="161.2" y1="210.0" x2="164.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="210.0" x2="168.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="168.4" y1="210.0" x2="172.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="210.0" x2="175.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="175.6" y1="210.0" x2="179.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="179.2" y1="210.0" x2="182.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="182.8" y1="210.0" x2="186.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="186.4" y1="210.0" x2="190.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="190.0" y1="210.0" x2="193.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="193.6" y1="210.0" x2="197.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="197.2" y1="210.0" x2="200.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="200.8" y1="210.0" x2="204.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="204.4" y1="210.0" x2="208.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="208.0" y1="210.0" x2="211.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="211.6" y1="210.0" x2="215.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="215.2" y1="210.0" x2="218.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="218.8" y1="210.0" x2="222.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="222.4" y1="210.0" x2="226.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="226.0" y1="210.0" x2="229.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="229.6" y1="210.0" x2="233.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="233.2" y1="210.0" x2="236.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="236.8" y1="210.0" x2="240.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="240.4" y1="210.0" x2="244.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="244.0" y1="210.0" x2="247.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="247.6" y1="210.0" x2="251.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="210.0" x2="254.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="202.0" x2="251.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="254.8" y1="210.0" x2="258.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="258.4" y1="210.0" x2="262.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="262.0" y1="210.0" x2="265.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="265.6" y1="210.0" x2="269.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="269.2" y1="210.0" x2="272.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="272.8" y1="210.0" x2="276.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="276.4" y1="210.0" x2="280.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="280.0" y1="210.0" x2="283.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="283.6" y1="210.0" x2="287.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="287.2" y1="210.0" x2="290.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="290.8" y1="210.0" x2="294.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="210.0" x2="298.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="298.0" y1="210.0" x2="301.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="301.6" y1="210.0" x2="305.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="305.2" y1="210.0" x2="308.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="308.8" y1="210.0" x2="312.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="312.4" y1="210.0" x2="316.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="316.0" y1="210.0" x2="319.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="319.6" y1="210.0" x2="323.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="323.2" y1="210.0" x2="326.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="326.8" y1="210.0" x2="330.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="330.4" y1="210.0" x2="334.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="334.0" y1="210.0" x2="337.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="337.6" y1="210.0" x2="341.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="341.2" y1="210.0" x2="344.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="344.8" y1="210.0" x2="348.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="348.4" y1="210.0" x2="352.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="210.0" x2="355.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="202.0" x2="352.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="355.6" y1="210.0" x2="359.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="359.2" y1="210.0" x2="362.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="362.8" y1="210.0" x2="366.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="210.0" x2="370.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="370.0" y1="210.0" x2="373.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="373.6" y1="210.0" x2="377.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="377.2" y1="210.0" x2="380.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="380.8" y1="210.0" x2="384.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="384.4" y1="210.0" x2="388.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="388.0" y1="210.0" x2="391.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="391.6" y1="210.0" x2="395.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="395.2" y1="210.0" x2="398.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="398.8" y1="210.0" x2="402.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="402.4" y1="210.0" x2="406.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="406.0" y1="210.0" x2="409.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="409.6" y1="210.0" x2="413.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="413.2" y1="210.0" x2="416.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="210.0" x2="420.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="420.4" y1="210.0" x2="424.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="210.0" x2="427.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="427.6" y1="210.0" x2="431.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="210.0" x2="434.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="434.8" y1="210.0" x2="438.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="438.4" y1="210.0" x2="442.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="442.0" y1="210.0" x2="445.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="445.6" y1="210.0" x2="449.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="449.2" y1="210.0" x2="452.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="452.8" y1="210.0" x2="456.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="456.4" y1="210.0" x2="460.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="460.0" y1="210.0" x2="463.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="463.6" y1="210.0" x2="467.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="202.0" x2="467.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="202.0" x2="488.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="210.0" x2="488.8" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="226.0" x2="17.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="218.0" x2="13.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="226.0" x2="13.6" y2="234.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="226.0" x2="20.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="226.0" x2="24.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="226.0" x2="28.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="226.0" x2="31.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="31.6" y1="226.0" x2="35.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="226.0" x2="38.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="226.0" x2="42.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="226.0" x2="46.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="226.0" x2="49.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="226.0" x2="53.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="226.0" x2="56.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="226.0" x2="60.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="226.0" x2="64.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="226.0" x2="67.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="226.0" x2="71.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="226.0" x2="74.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="226.0" x2="78.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="226.0" x2="82.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="226.0" x2="85.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="226.0" x2="89.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="89.2" y1="226.0" x2="92.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="92.8" y1="226.0" x2="96.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="226.0" x2="100.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="226.0" x2="103.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="226.0" x2="107.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="226.0" x2="110.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="226.0" x2="114.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="226.0" x2="118.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="118.0" y1="226.0" x2="121.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="121.6" y1="226.0" x2="125.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="125.2" y1="226.0" x2="128.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="128.8" y1="226.0" x2="132.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="132.4" y1="226.0" x2="136.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="136.0" y1="226.0" x2="139.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="139.6" y1="226.0" x2="143.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="226.0" x2="146.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="146.8" y1="226.0" x2="150.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="150.4" y1="226.0" x2="154.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="154.0" y1="226.0" x2="157.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="226.0" x2="161.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="161.2" y1="226.0" x2="164.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="226.0" x2="168.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="168.4" y1="226.0" x2="172.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="226.0" x2="175.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="175.6" y1="226.0" x2="179.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="179.2" y1="226.0" x2="182.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="182.8" y1="226.0" x2="186.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="186.4" y1="226.0" x2="190.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="190.0" y1="226.0" x2="193.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="193.6" y1="226.0" x2="197.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="197.2" y1="226.0" x2="200.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="200.8" y1="226.0" x2="204.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="204.4" y1="226.0" x2="208.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="208.0" y1="226.0" x2="211.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="211.6" y1="226.0" x2="215.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="215.2" y1="226.0" x2="218.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="218.8" y1="226.0" x2="222.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="222.4" y1="226.0" x2="226.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="226.0" y1="226.0" x2="229.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="229.6" y1="226.0" x2="233.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="233.2" y1="226.0" x2="236.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="236.8" y1="226.0" x2="240.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="240.4" y1="226.0" x2="244.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="244.0" y1="226.0" x2="247.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="247.6" y1="226.0" x2="251.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="226.0" x2="254.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="254.8" y1="226.0" x2="258.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="258.4" y1="226.0" x2="262.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="262.0" y1="226.0" x2="265.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="265.6" y1="226.0" x2="269.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="269.2" y1="226.0" x2="272.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="272.8" y1="226.0" x2="276.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="276.4" y1="226.0" x2="280.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="280.0" y1="226.0" x2="283.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="283.6" y1="226.0" x2="287.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="287.2" y1="226.0" x2="290.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="290.8" y1="226.0" x2="294.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="226.0" x2="298.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="298.0" y1="226.0" x2="301.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="301.6" y1="226.0" x2="305.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="305.2" y1="226.0" x2="308.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="308.8" y1="226.0" x2="312.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="312.4" y1="226.0" x2="316.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="316.0" y1="226.0" x2="319.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="319.6" y1="226.0" x2="323.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="323.2" y1="226.0" x2="326.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="326.8" y1="226.0" x2="330.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="330.4" y1="226.0" x2="334.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="334.0" y1="226.0" x2="337.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="337.6" y1="226.0" x2="341.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="341.2" y1="226.0" x2="344.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="344.8" y1="226.0" x2="348.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="348.4" y1="226.0" x2="352.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="226.0" x2="355.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="355.6" y1="226.0" x2="359.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="359.2" y1="226.0" x2="362.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="362.8" y1="226.0" x2="366.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="226.0" x2="370.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="370.0" y1="226.0" x2="373.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="373.6" y1="226.0" x2="377.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="377.2" y1="226.0" x2="380.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="380.8" y1="226.0" x2="384.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="384.4" y1="226.0" x2="388.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="388.0" y1="226.0" x2="391.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="391.6" y1="226.0" x2="395.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="395.2" y1="226.0" x2="398.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="398.8" y1="226.0" x2="402.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="402.4" y1="226.0" x2="406.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="406.0" y1="226.0" x2="409.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="409.6" y1="226.0" x2="413.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="413.2" y1="226.0" x2="416.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="226.0" x2="420.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="420.4" y1="226.0" x2="424.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="226.0" x2="427.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="427.6" y1="226.0" x2="431.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="226.0" x2="434.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="434.8" y1="226.0" x2="438.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="438.4" y1="226.0" x2="442.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="442.0" y1="226.0" x2="445.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="445.6" y1="226.0" x2="449.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="449.2" y1="226.0" x2="452.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="452.8" y1="226.0" x2="456.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="456.4" y1="226.0" x2="460.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="460.0" y1="226.0" x2="463.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="463.6" y1="226.0" x2="467.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="226.0" x2="470.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="470.8" y1="226.0" x2="474.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="474.4" y1="226.0" x2="478.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="478.0" y1="226.0" x2="481.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="481.6" y1="226.0" x2="485.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="485.2" y1="226.0" x2="488.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="218.0" x2="488.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="226.0" x2="488.8" y2="234.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="234.0" x2="13.6" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="242.0" x2="13.6" y2="250.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="234.0" x2="143.2" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="242.0" x2="143.2" y2="250.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="234.0" x2="488.8" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="242.0" x2="488.8" y2="250.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="258.0" x2="17.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="250.0" x2="13.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="258.0" x2="13.6" y2="266.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="258.0" x2="20.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="258.0" x2="24.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="258.0" x2="28.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="258.0" x2="31.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="31.6" y1="258.0" x2="35.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="258.0" x2="38.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="258.0" x2="42.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="258.0" x2="46.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="258.0" x2="49.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="258.0" x2="53.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="258.0" x2="56.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="258.0" x2="60.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="258.0" x2="64.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="258.0" x2="67.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="258.0" x2="71.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="258.0" x2="74.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="258.0" x2="78.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="258.0" x2="82.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="258.0" x2="85.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="258.0" x2="89.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="89.2" y1="258.0" x2="92.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="92.8" y1="258.0" x2="96.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="258.0" x2="100.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="258.0" x2="103.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="258.0" x2="107.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="258.0" x2="110.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="258.0" x2="114.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="258.0" x2="118.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="118.0" y1="258.0" x2="121.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="121.6" y1="258.0" x2="125.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="125.2" y1="258.0" x2="128.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="128.8" y1="258.0" x2="132.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="132.4" y1="258.0" x2="136.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="136.0" y1="258.0" x2="139.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="139.6" y1="258.0" x2="143.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="258.0" x2="146.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="146.8" y1="258.0" x2="150.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="150.4" y1="258.0" x2="154.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="154.0" y1="258.0" x2="157.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="258.0" x2="161.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="161.2" y1="258.0" x2="164.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="258.0" x2="168.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="168.4" y1="258.0" x2="172.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="258.0" x2="175.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="175.6" y1="258.0" x2="179.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="179.2" y1="258.0" x2="182.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="182.8" y1="258.0" x2="186.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="186.4" y1="258.0" x2="190.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="190.0" y1="258.0" x2="193.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="193.6" y1="258.0" x2="197.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="197.2" y1="258.0" x2="200.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="200.8" y1="258.0" x2="204.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="204.4" y1="258.0" x2="208.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="208.0" y1="258.0" x2="211.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="211.6" y1="258.0" x2="215.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="215.2" y1="258.0" x2="218.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="218.8" y1="258.0" x2="222.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="222.4" y1="258.0" x2="226.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="226.0" y1="258.0" x2="229.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="229.6" y1="258.0" x2="233.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="233.2" y1="258.0" x2="236.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="236.8" y1="258.0" x2="240.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="240.4" y1="258.0" x2="244.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="244.0" y1="258.0" x2="247.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="247.6" y1="258.0" x2="251.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="258.0" x2="254.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="254.8" y1="258.0" x2="258.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="258.4" y1="258.0" x2="262.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="262.0" y1="258.0" x2="265.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="265.6" y1="258.0" x2="269.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="269.2" y1="258.0" x2="272.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="272.8" y1="258.0" x2="276.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="276.4" y1="258.0" x2="280.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="280.0" y1="258.0" x2="283.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="283.6" y1="258.0" x2="287.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="287.2" y1="258.0" x2="290.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="290.8" y1="258.0" x2="294.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="258.0" x2="298.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="298.0" y1="258.0" x2="301.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="301.6" y1="258.0" x2="305.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="305.2" y1="258.0" x2="308.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="308.8" y1="258.0" x2="312.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="312.4" y1="258.0" x2="316.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="316.0" y1="258.0" x2="319.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="319.6" y1="258.0" x2="323.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="323.2" y1="258.0" x2="326.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="326.8" y1="258.0" x2="330.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="330.4" y1="258.0" x2="334.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="334.0" y1="258.0" x2="337.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="337.6" y1="258.0" x2="341.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="341.2" y1="258.0" x2="344.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="344.8" y1="258.0" x2="348.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="348.4" y1="258.0" x2="352.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="258.0" x2="355.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="355.6" y1="258.0" x2="359.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="359.2" y1="258.0" x2="362.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="362.8" y1="258.0" x2="366.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="258.0" x2="370.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="370.0" y1="258.0" x2="373.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="373.6" y1="258.0" x2="377.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="377.2" y1="258.0" x2="380.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="380.8" y1="258.0" x2="384.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="384.4" y1="258.0" x2="388.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="388.0" y1="258.0" x2="391.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="391.6" y1="258.0" x2="395.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="395.2" y1="258.0" x2="398.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="398.8" y1="258.0" x2="402.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="402.4" y1="258.0" x2="406.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="406.0" y1="258.0" x2="409.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="409.6" y1="258.0" x2="413.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="413.2" y1="258.0" x2="416.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="258.0" x2="420.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="420.4" y1="258.0" x2="424.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="258.0" x2="427.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="427.6" y1="258.0" x2="431.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="258.0" x2="434.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="434.8" y1="258.0" x2="438.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="438.4" y1="258.0" x2="442.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="442.0" y1="258.0" x2="445.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="445.6" y1="258.0" x2="449.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="449.2" y1="258.0" x2="452.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="452.8" y1="258.0" x2="456.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="456.4" y1="258.0" x2="460.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="460.0" y1="258.0" x2="463.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="463.6" y1="258.0" x2="467.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="258.0" x2="470.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="470.8" y1="258.0" x2="474.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="474.4" y1="258.0" x2="478.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="478.0" y1="258.0" x2="481.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="481.6" y1="258.0" x2="485.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="485.2" y1="258.0" x2="488.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="250.0" x2="488.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="258.0" x2="488.8" y2="266.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="266.0" x2="13.6" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="274.0" x2="13.6" y2="282.0" stroke="#10373E" stroke-width="1.3"/><line x1="150.4" y1="266.0" x2="150.4" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="150.4" y1="274.0" x2="150.4" y2="282.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="266.0" x2="488.8" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="274.0" x2="488.8" y2="282.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="290.0" x2="17.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="282.0" x2="13.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="290.0" x2="13.6" y2="298.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="290.0" x2="20.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="290.0" x2="24.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="290.0" x2="28.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="290.0" x2="31.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="31.6" y1="290.0" x2="35.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="290.0" x2="38.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="290.0" x2="42.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="290.0" x2="46.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="290.0" x2="49.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="290.0" x2="53.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="290.0" x2="56.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="290.0" x2="60.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="290.0" x2="64.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="290.0" x2="67.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="290.0" x2="71.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="290.0" x2="74.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="290.0" x2="78.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="290.0" x2="82.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="290.0" x2="85.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="290.0" x2="89.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="89.2" y1="290.0" x2="92.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="92.8" y1="290.0" x2="96.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="290.0" x2="100.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="290.0" x2="103.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="290.0" x2="107.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="290.0" x2="110.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="290.0" x2="114.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="290.0" x2="118.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="118.0" y1="290.0" x2="121.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="121.6" y1="290.0" x2="125.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="125.2" y1="290.0" x2="128.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="128.8" y1="290.0" x2="132.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="132.4" y1="290.0" x2="136.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="136.0" y1="290.0" x2="139.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="139.6" y1="290.0" x2="143.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="290.0" x2="146.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="146.8" y1="290.0" x2="150.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="150.4" y1="290.0" x2="154.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="154.0" y1="290.0" x2="157.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="290.0" x2="161.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="161.2" y1="290.0" x2="164.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="290.0" x2="168.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="168.4" y1="290.0" x2="172.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="290.0" x2="175.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="175.6" y1="290.0" x2="179.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="179.2" y1="290.0" x2="182.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="182.8" y1="290.0" x2="186.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="186.4" y1="290.0" x2="190.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="190.0" y1="290.0" x2="193.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="193.6" y1="290.0" x2="197.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="197.2" y1="290.0" x2="200.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="200.8" y1="290.0" x2="204.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="204.4" y1="290.0" x2="208.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="208.0" y1="290.0" x2="211.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="211.6" y1="290.0" x2="215.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="215.2" y1="290.0" x2="218.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="218.8" y1="290.0" x2="222.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="222.4" y1="290.0" x2="226.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="226.0" y1="290.0" x2="229.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="229.6" y1="290.0" x2="233.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="233.2" y1="290.0" x2="236.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="236.8" y1="290.0" x2="240.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="240.4" y1="290.0" x2="244.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="244.0" y1="290.0" x2="247.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="247.6" y1="290.0" x2="251.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="290.0" x2="254.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="254.8" y1="290.0" x2="258.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="258.4" y1="290.0" x2="262.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="262.0" y1="290.0" x2="265.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="265.6" y1="290.0" x2="269.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="269.2" y1="290.0" x2="272.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="272.8" y1="290.0" x2="276.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="276.4" y1="290.0" x2="280.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="280.0" y1="290.0" x2="283.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="283.6" y1="290.0" x2="287.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="287.2" y1="290.0" x2="290.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="290.8" y1="290.0" x2="294.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="290.0" x2="298.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="298.0" y1="290.0" x2="301.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="301.6" y1="290.0" x2="305.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="305.2" y1="290.0" x2="308.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="308.8" y1="290.0" x2="312.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="312.4" y1="290.0" x2="316.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="316.0" y1="290.0" x2="319.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="319.6" y1="290.0" x2="323.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="323.2" y1="290.0" x2="326.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="326.8" y1="290.0" x2="330.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="330.4" y1="290.0" x2="334.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="334.0" y1="290.0" x2="337.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="337.6" y1="290.0" x2="341.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="341.2" y1="290.0" x2="344.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="344.8" y1="290.0" x2="348.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="348.4" y1="290.0" x2="352.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="290.0" x2="355.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="355.6" y1="290.0" x2="359.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="359.2" y1="290.0" x2="362.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="362.8" y1="290.0" x2="366.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="290.0" x2="370.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="370.0" y1="290.0" x2="373.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="373.6" y1="290.0" x2="377.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="377.2" y1="290.0" x2="380.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="380.8" y1="290.0" x2="384.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="384.4" y1="290.0" x2="388.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="388.0" y1="290.0" x2="391.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="391.6" y1="290.0" x2="395.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="395.2" y1="290.0" x2="398.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="398.8" y1="290.0" x2="402.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="402.4" y1="290.0" x2="406.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="406.0" y1="290.0" x2="409.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="409.6" y1="290.0" x2="413.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="413.2" y1="290.0" x2="416.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="290.0" x2="420.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="420.4" y1="290.0" x2="424.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="290.0" x2="427.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="427.6" y1="290.0" x2="431.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="290.0" x2="434.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="434.8" y1="290.0" x2="438.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="438.4" y1="290.0" x2="442.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="442.0" y1="290.0" x2="445.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="445.6" y1="290.0" x2="449.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="449.2" y1="290.0" x2="452.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="452.8" y1="290.0" x2="456.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="456.4" y1="290.0" x2="460.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="460.0" y1="290.0" x2="463.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="463.6" y1="290.0" x2="467.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="290.0" x2="470.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="470.8" y1="290.0" x2="474.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="474.4" y1="290.0" x2="478.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="478.0" y1="290.0" x2="481.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="481.6" y1="290.0" x2="485.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="485.2" y1="290.0" x2="488.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="282.0" x2="488.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="290.0" x2="488.8" y2="298.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="298.0" x2="13.6" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="306.0" x2="13.6" y2="314.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="298.0" x2="488.8" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="306.0" x2="488.8" y2="314.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="322.0" x2="17.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="314.0" x2="13.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="322.0" x2="13.6" y2="330.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="322.0" x2="20.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="322.0" x2="24.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="322.0" x2="28.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="322.0" x2="31.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="31.6" y1="322.0" x2="35.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="322.0" x2="38.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="322.0" x2="42.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="322.0" x2="46.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="322.0" x2="49.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="322.0" x2="53.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="322.0" x2="56.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="322.0" x2="60.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="322.0" x2="64.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="322.0" x2="67.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="322.0" x2="71.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="322.0" x2="74.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="322.0" x2="78.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="322.0" x2="82.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="322.0" x2="85.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="322.0" x2="89.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="89.2" y1="322.0" x2="92.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="92.8" y1="322.0" x2="96.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="322.0" x2="100.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="322.0" x2="103.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="322.0" x2="107.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="322.0" x2="110.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="322.0" x2="114.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="322.0" x2="118.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="118.0" y1="322.0" x2="121.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="121.6" y1="322.0" x2="125.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="125.2" y1="322.0" x2="128.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="128.8" y1="322.0" x2="132.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="132.4" y1="322.0" x2="136.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="136.0" y1="322.0" x2="139.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="139.6" y1="322.0" x2="143.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="322.0" x2="146.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="146.8" y1="322.0" x2="150.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="150.4" y1="322.0" x2="154.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="154.0" y1="322.0" x2="157.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="322.0" x2="161.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="161.2" y1="322.0" x2="164.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="322.0" x2="168.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="168.4" y1="322.0" x2="172.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="322.0" x2="175.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="175.6" y1="322.0" x2="179.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="179.2" y1="322.0" x2="182.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="182.8" y1="322.0" x2="186.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="186.4" y1="322.0" x2="190.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="190.0" y1="322.0" x2="193.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="193.6" y1="322.0" x2="197.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="197.2" y1="322.0" x2="200.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="200.8" y1="322.0" x2="204.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="204.4" y1="322.0" x2="208.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="208.0" y1="322.0" x2="211.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="211.6" y1="322.0" x2="215.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="215.2" y1="322.0" x2="218.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="218.8" y1="322.0" x2="222.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="222.4" y1="322.0" x2="226.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="226.0" y1="322.0" x2="229.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="229.6" y1="322.0" x2="233.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="233.2" y1="322.0" x2="236.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="236.8" y1="322.0" x2="240.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="240.4" y1="322.0" x2="244.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="244.0" y1="322.0" x2="247.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="247.6" y1="322.0" x2="251.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="322.0" x2="254.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="254.8" y1="322.0" x2="258.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="258.4" y1="322.0" x2="262.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="262.0" y1="322.0" x2="265.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="265.6" y1="322.0" x2="269.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="269.2" y1="322.0" x2="272.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="272.8" y1="322.0" x2="276.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="276.4" y1="322.0" x2="280.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="280.0" y1="322.0" x2="283.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="283.6" y1="322.0" x2="287.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="287.2" y1="322.0" x2="290.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="290.8" y1="322.0" x2="294.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="322.0" x2="298.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="298.0" y1="322.0" x2="301.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="301.6" y1="322.0" x2="305.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="305.2" y1="322.0" x2="308.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="308.8" y1="322.0" x2="312.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="312.4" y1="322.0" x2="316.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="316.0" y1="322.0" x2="319.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="319.6" y1="322.0" x2="323.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="323.2" y1="322.0" x2="326.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="326.8" y1="322.0" x2="330.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="330.4" y1="322.0" x2="334.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="334.0" y1="322.0" x2="337.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="337.6" y1="322.0" x2="341.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="341.2" y1="322.0" x2="344.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="344.8" y1="322.0" x2="348.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="348.4" y1="322.0" x2="352.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="322.0" x2="355.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="355.6" y1="322.0" x2="359.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="359.2" y1="322.0" x2="362.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="362.8" y1="322.0" x2="366.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="322.0" x2="370.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="370.0" y1="322.0" x2="373.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="373.6" y1="322.0" x2="377.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="377.2" y1="322.0" x2="380.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="380.8" y1="322.0" x2="384.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="384.4" y1="322.0" x2="388.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="388.0" y1="322.0" x2="391.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="391.6" y1="322.0" x2="395.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="395.2" y1="322.0" x2="398.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="398.8" y1="322.0" x2="402.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="402.4" y1="322.0" x2="406.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="406.0" y1="322.0" x2="409.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="409.6" y1="322.0" x2="413.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="413.2" y1="322.0" x2="416.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="322.0" x2="420.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="420.4" y1="322.0" x2="424.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="322.0" x2="427.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="427.6" y1="322.0" x2="431.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="322.0" x2="434.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="434.8" y1="322.0" x2="438.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="438.4" y1="322.0" x2="442.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="442.0" y1="322.0" x2="445.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="445.6" y1="322.0" x2="449.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="449.2" y1="322.0" x2="452.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="452.8" y1="322.0" x2="456.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="456.4" y1="322.0" x2="460.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="460.0" y1="322.0" x2="463.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="463.6" y1="322.0" x2="467.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="322.0" x2="470.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="470.8" y1="322.0" x2="474.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="474.4" y1="322.0" x2="478.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="478.0" y1="322.0" x2="481.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="481.6" y1="322.0" x2="485.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="485.2" y1="322.0" x2="488.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="314.0" x2="488.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="322.0" x2="488.8" y2="330.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="330.0" x2="13.6" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="338.0" x2="13.6" y2="346.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="330.0" x2="488.8" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="338.0" x2="488.8" y2="346.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="354.0" x2="17.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="346.0" x2="13.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="354.0" x2="13.6" y2="362.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="354.0" x2="20.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="354.0" x2="24.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="354.0" x2="28.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="354.0" x2="31.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="31.6" y1="354.0" x2="35.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="354.0" x2="38.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="354.0" x2="42.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="354.0" x2="46.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="354.0" x2="49.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="354.0" x2="53.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="354.0" x2="56.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="354.0" x2="60.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="354.0" x2="64.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="354.0" x2="67.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="354.0" x2="71.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="354.0" x2="74.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="354.0" x2="78.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="354.0" x2="82.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="354.0" x2="85.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="354.0" x2="89.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="89.2" y1="354.0" x2="92.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="92.8" y1="354.0" x2="96.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="354.0" x2="100.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="354.0" x2="103.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="354.0" x2="107.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="354.0" x2="110.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="354.0" x2="114.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="354.0" x2="118.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="118.0" y1="354.0" x2="121.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="121.6" y1="354.0" x2="125.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="125.2" y1="354.0" x2="128.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="128.8" y1="354.0" x2="132.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="132.4" y1="354.0" x2="136.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="136.0" y1="354.0" x2="139.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="139.6" y1="354.0" x2="143.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="354.0" x2="146.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="146.8" y1="354.0" x2="150.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="150.4" y1="354.0" x2="154.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="154.0" y1="354.0" x2="157.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="354.0" x2="161.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="161.2" y1="354.0" x2="164.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="354.0" x2="168.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="168.4" y1="354.0" x2="172.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="354.0" x2="175.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="175.6" y1="354.0" x2="179.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="179.2" y1="354.0" x2="182.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="182.8" y1="354.0" x2="186.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="186.4" y1="354.0" x2="190.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="190.0" y1="354.0" x2="193.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="193.6" y1="354.0" x2="197.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="197.2" y1="354.0" x2="200.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="200.8" y1="354.0" x2="204.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="204.4" y1="354.0" x2="208.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="208.0" y1="354.0" x2="211.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="211.6" y1="354.0" x2="215.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="215.2" y1="354.0" x2="218.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="218.8" y1="354.0" x2="222.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="222.4" y1="354.0" x2="226.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="226.0" y1="354.0" x2="229.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="229.6" y1="354.0" x2="233.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="233.2" y1="354.0" x2="236.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="236.8" y1="354.0" x2="240.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="240.4" y1="354.0" x2="244.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="244.0" y1="354.0" x2="247.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="247.6" y1="354.0" x2="251.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="354.0" x2="254.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="254.8" y1="354.0" x2="258.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="258.4" y1="354.0" x2="262.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="262.0" y1="354.0" x2="265.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="265.6" y1="354.0" x2="269.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="269.2" y1="354.0" x2="272.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="272.8" y1="354.0" x2="276.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="276.4" y1="354.0" x2="280.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="280.0" y1="354.0" x2="283.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="283.6" y1="354.0" x2="287.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="287.2" y1="354.0" x2="290.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="290.8" y1="354.0" x2="294.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="354.0" x2="298.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="298.0" y1="354.0" x2="301.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="301.6" y1="354.0" x2="305.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="305.2" y1="354.0" x2="308.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="308.8" y1="354.0" x2="312.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="312.4" y1="354.0" x2="316.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="316.0" y1="354.0" x2="319.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="319.6" y1="354.0" x2="323.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="323.2" y1="354.0" x2="326.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="326.8" y1="354.0" x2="330.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="330.4" y1="354.0" x2="334.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="334.0" y1="354.0" x2="337.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="337.6" y1="354.0" x2="341.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="341.2" y1="354.0" x2="344.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="344.8" y1="354.0" x2="348.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="348.4" y1="354.0" x2="352.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="354.0" x2="355.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="355.6" y1="354.0" x2="359.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="359.2" y1="354.0" x2="362.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="362.8" y1="354.0" x2="366.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="354.0" x2="370.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="370.0" y1="354.0" x2="373.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="373.6" y1="354.0" x2="377.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="377.2" y1="354.0" x2="380.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="380.8" y1="354.0" x2="384.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="384.4" y1="354.0" x2="388.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="388.0" y1="354.0" x2="391.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="391.6" y1="354.0" x2="395.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="395.2" y1="354.0" x2="398.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="398.8" y1="354.0" x2="402.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="402.4" y1="354.0" x2="406.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="406.0" y1="354.0" x2="409.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="409.6" y1="354.0" x2="413.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="413.2" y1="354.0" x2="416.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="354.0" x2="420.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="420.4" y1="354.0" x2="424.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="354.0" x2="427.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="427.6" y1="354.0" x2="431.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="354.0" x2="434.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="434.8" y1="354.0" x2="438.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="438.4" y1="354.0" x2="442.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="442.0" y1="354.0" x2="445.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="445.6" y1="354.0" x2="449.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="449.2" y1="354.0" x2="452.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="452.8" y1="354.0" x2="456.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="456.4" y1="354.0" x2="460.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="460.0" y1="354.0" x2="463.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="463.6" y1="354.0" x2="467.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="354.0" x2="470.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="470.8" y1="354.0" x2="474.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="474.4" y1="354.0" x2="478.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="478.0" y1="354.0" x2="481.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="481.6" y1="354.0" x2="485.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="485.2" y1="354.0" x2="488.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="346.0" x2="488.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="354.0" x2="488.8" y2="362.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="362.0" x2="13.6" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="370.0" x2="13.6" y2="378.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="362.0" x2="488.8" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="370.0" x2="488.8" y2="378.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="386.0" x2="17.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="378.0" x2="13.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="386.0" x2="20.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="386.0" x2="24.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="386.0" x2="28.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="386.0" x2="31.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="31.6" y1="386.0" x2="35.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="386.0" x2="38.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="386.0" x2="42.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="386.0" x2="46.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="386.0" x2="49.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="386.0" x2="53.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="386.0" x2="56.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="386.0" x2="60.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="386.0" x2="64.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="386.0" x2="67.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="386.0" x2="71.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="386.0" x2="74.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="386.0" x2="78.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="386.0" x2="82.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="386.0" x2="85.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="386.0" x2="89.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="89.2" y1="386.0" x2="92.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="92.8" y1="386.0" x2="96.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="386.0" x2="100.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="386.0" x2="103.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="386.0" x2="107.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="386.0" x2="110.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="386.0" x2="114.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="386.0" x2="118.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="118.0" y1="386.0" x2="121.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="121.6" y1="386.0" x2="125.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="125.2" y1="386.0" x2="128.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="128.8" y1="386.0" x2="132.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="132.4" y1="386.0" x2="136.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="136.0" y1="386.0" x2="139.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="139.6" y1="386.0" x2="143.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="386.0" x2="146.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="146.8" y1="386.0" x2="150.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="150.4" y1="386.0" x2="154.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="154.0" y1="386.0" x2="157.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="386.0" x2="161.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="161.2" y1="386.0" x2="164.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="386.0" x2="168.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="168.4" y1="386.0" x2="172.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="386.0" x2="175.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="175.6" y1="386.0" x2="179.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="179.2" y1="386.0" x2="182.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="182.8" y1="386.0" x2="186.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="186.4" y1="386.0" x2="190.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="190.0" y1="386.0" x2="193.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="193.6" y1="386.0" x2="197.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="197.2" y1="386.0" x2="200.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="200.8" y1="386.0" x2="204.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="204.4" y1="386.0" x2="208.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="208.0" y1="386.0" x2="211.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="211.6" y1="386.0" x2="215.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="215.2" y1="386.0" x2="218.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="218.8" y1="386.0" x2="222.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="222.4" y1="386.0" x2="226.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="226.0" y1="386.0" x2="229.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="229.6" y1="386.0" x2="233.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="233.2" y1="386.0" x2="236.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="236.8" y1="386.0" x2="240.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="240.4" y1="386.0" x2="244.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="244.0" y1="386.0" x2="247.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="247.6" y1="386.0" x2="251.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="386.0" x2="254.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="254.8" y1="386.0" x2="258.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="258.4" y1="386.0" x2="262.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="262.0" y1="386.0" x2="265.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="265.6" y1="386.0" x2="269.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="269.2" y1="386.0" x2="272.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="272.8" y1="386.0" x2="276.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="276.4" y1="386.0" x2="280.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="280.0" y1="386.0" x2="283.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="283.6" y1="386.0" x2="287.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="287.2" y1="386.0" x2="290.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="290.8" y1="386.0" x2="294.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="386.0" x2="298.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="298.0" y1="386.0" x2="301.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="301.6" y1="386.0" x2="305.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="305.2" y1="386.0" x2="308.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="308.8" y1="386.0" x2="312.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="312.4" y1="386.0" x2="316.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="316.0" y1="386.0" x2="319.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="319.6" y1="386.0" x2="323.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="323.2" y1="386.0" x2="326.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="326.8" y1="386.0" x2="330.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="330.4" y1="386.0" x2="334.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="334.0" y1="386.0" x2="337.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="337.6" y1="386.0" x2="341.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="341.2" y1="386.0" x2="344.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="344.8" y1="386.0" x2="348.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="348.4" y1="386.0" x2="352.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="386.0" x2="355.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="355.6" y1="386.0" x2="359.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="359.2" y1="386.0" x2="362.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="362.8" y1="386.0" x2="366.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="386.0" x2="370.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="370.0" y1="386.0" x2="373.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="373.6" y1="386.0" x2="377.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="377.2" y1="386.0" x2="380.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="380.8" y1="386.0" x2="384.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="384.4" y1="386.0" x2="388.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="388.0" y1="386.0" x2="391.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="391.6" y1="386.0" x2="395.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="395.2" y1="386.0" x2="398.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="398.8" y1="386.0" x2="402.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="402.4" y1="386.0" x2="406.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="406.0" y1="386.0" x2="409.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="409.6" y1="386.0" x2="413.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="413.2" y1="386.0" x2="416.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="386.0" x2="420.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="420.4" y1="386.0" x2="424.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="386.0" x2="427.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="427.6" y1="386.0" x2="431.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="386.0" x2="434.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="434.8" y1="386.0" x2="438.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="438.4" y1="386.0" x2="442.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="442.0" y1="386.0" x2="445.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="445.6" y1="386.0" x2="449.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="449.2" y1="386.0" x2="452.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="452.8" y1="386.0" x2="456.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="456.4" y1="386.0" x2="460.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="460.0" y1="386.0" x2="463.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="463.6" y1="386.0" x2="467.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="386.0" x2="470.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="470.8" y1="386.0" x2="474.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="474.4" y1="386.0" x2="478.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="478.0" y1="386.0" x2="481.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="481.6" y1="386.0" x2="485.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="485.2" y1="386.0" x2="488.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="488.8" y1="378.0" x2="488.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><text x="190.0" y="38.0" font-size="9.5" fill="#10373E">Web</text><text x="218.8" y="38.0" font-size="9.5" fill="#10373E">UI</text><text x="240.4" y="38.0" font-size="9.5" fill="#10373E">/</text><text x="254.8" y="38.0" font-size="9.5" fill="#10373E">CLI</text><text x="154.0" y="70.0" font-size="9.5" fill="#10373E">ahgDataMigrationActions</text><text x="67.6" y="86.0" font-size="9.5" fill="#10373E">(Upload,</text><text x="132.4" y="86.0" font-size="9.5" fill="#10373E">Map,</text><text x="168.4" y="86.0" font-size="9.5" fill="#10373E">Preview,</text><text x="233.2" y="86.0" font-size="9.5" fill="#10373E">Validate,</text><text x="305.2" y="86.0" font-size="9.5" fill="#10373E">Import,</text><text x="362.8" y="86.0" font-size="9.5" fill="#10373E">Export)</text><text x="31.6" y="118.0" font-size="9.5" fill="#10373E">MigrationService</text><text x="168.4" y="118.0" font-size="9.5" fill="#10373E">ValidationService</text><text x="312.4" y="118.0" font-size="9.5" fill="#10373E">PreservicaImportService</text><text x="118.0" y="150.0" font-size="9.5" fill="#10373E">Validation</text><text x="197.2" y="150.0" font-size="9.5" fill="#10373E">Framework</text><text x="269.2" y="150.0" font-size="9.5" fill="#10373E">(NEW</text><text x="305.2" y="150.0" font-size="9.5" fill="#10373E">in</text><text x="326.8" y="150.0" font-size="9.5" fill="#10373E">1.4.0)</text><text x="46.0" y="182.0" font-size="9.5" fill="#10373E">SchemaValid.</text><text x="154.0" y="182.0" font-size="9.5" fill="#10373E">Referential</text><text x="262.0" y="182.0" font-size="9.5" fill="#10373E">Duplicate</text><text x="362.8" y="182.0" font-size="9.5" fill="#10373E">SectorValid.</text><text x="154.0" y="198.0" font-size="9.5" fill="#10373E">Validator</text><text x="262.0" y="198.0" font-size="9.5" fill="#10373E">Detector</text><text x="362.8" y="198.0" font-size="9.5" fill="#10373E">(5</text><text x="384.4" y="198.0" font-size="9.5" fill="#10373E">sectors)</text><text x="31.6" y="246.0" font-size="9.5" fill="#10373E">ParserFactory</text><text x="161.2" y="246.0" font-size="9.5" fill="#10373E">Parsers</text><text x="218.8" y="246.0" font-size="9.5" fill="#10373E">(CSV,</text><text x="262.0" y="246.0" font-size="9.5" fill="#10373E">Excel,</text><text x="312.4" y="246.0" font-size="9.5" fill="#10373E">OPEX,</text><text x="355.6" y="246.0" font-size="9.5" fill="#10373E">PAX)</text><text x="31.6" y="278.0" font-size="9.5" fill="#10373E">SourceDetector</text><text x="168.4" y="278.0" font-size="9.5" fill="#10373E">Mappings</text><text x="233.2" y="278.0" font-size="9.5" fill="#10373E">(Field</text><text x="283.6" y="278.0" font-size="9.5" fill="#10373E">Definitions)</text><text x="31.6" y="310.0" font-size="9.5" fill="#10373E">Sectors</text><text x="89.2" y="310.0" font-size="9.5" fill="#10373E">(Archives,</text><text x="168.4" y="310.0" font-size="9.5" fill="#10373E">Museum,</text><text x="226.0" y="310.0" font-size="9.5" fill="#10373E">Library,</text><text x="290.8" y="310.0" font-size="9.5" fill="#10373E">Gallery,</text><text x="355.6" y="310.0" font-size="9.5" fill="#10373E">DAM)</text><text x="96.4" y="342.0" font-size="9.5" fill="#10373E">Laravel</text><text x="154.0" y="342.0" font-size="9.5" fill="#10373E">Query</text><text x="197.2" y="342.0" font-size="9.5" fill="#10373E">Builder</text><text x="254.8" y="342.0" font-size="9.5" fill="#10373E">(Illuminate\Database)</text><text x="175.6" y="374.0" font-size="9.5" fill="#10373E">MySQL</text><text x="218.8" y="374.0" font-size="9.5" fill="#10373E">Database</text></svg></div>

### Data Flow

1. **Upload** → File received, stored in `/uploads/migrations/`
2. **Detect** → SourceDetector identifies format and source system
3. **Parse** → ParserFactory creates appropriate parser
4. **Map** → Field mappings applied from `atom_data_mapping`
5. **Transform** → Transformations applied (trim, date format, etc.)
6. **Import** → Records created in AtoM database
7. **Post-process** → Slugs generated, nested set calculated, rights imported

---

## 2. Directory Structure
<div style="overflow-x:auto;margin:1rem 0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 538 1844" style="max-width:100%;height:auto;font-family:ui-monospace,Menlo,Consolas,monospace"><rect x="0.5" y="0.5" width="537" height="1843" rx="8" fill="#f7faf9" stroke="#d8e6e3"/><line x1="13.6" y1="34.0" x2="17.2" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="26.0" x2="13.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="34.0" x2="13.6" y2="42.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="34.0" x2="20.8" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="34.0" x2="24.4" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="34.0" x2="28.0" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="34.0" x2="31.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="42.0" x2="13.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="13.6" y2="58.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="50.0" x2="46.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="42.0" x2="42.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="50.0" x2="49.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="50.0" x2="53.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="50.0" x2="56.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="50.0" x2="60.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="17.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="58.0" x2="13.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="13.6" y2="74.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="66.0" x2="20.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="66.0" x2="24.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="66.0" x2="28.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="66.0" x2="31.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="74.0" x2="13.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="82.0" x2="13.6" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="82.0" x2="46.0" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="74.0" x2="42.4" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="82.0" x2="42.4" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="82.0" x2="49.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="82.0" x2="53.2" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="82.0" x2="56.8" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="82.0" x2="60.4" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="90.0" x2="13.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="98.0" x2="13.6" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="98.0" x2="46.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="90.0" x2="42.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="98.0" x2="49.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="98.0" x2="53.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="98.0" x2="56.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="98.0" x2="60.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="114.0" x2="17.2" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="106.0" x2="13.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="114.0" x2="13.6" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="114.0" x2="20.8" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="114.0" x2="24.4" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="114.0" x2="28.0" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="114.0" x2="31.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="122.0" x2="13.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="130.0" x2="13.6" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="130.0" x2="46.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="122.0" x2="42.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="130.0" x2="42.4" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="130.0" x2="49.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="130.0" x2="53.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="130.0" x2="56.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="130.0" x2="60.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="138.0" x2="13.6" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="146.0" x2="13.6" y2="154.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="146.0" x2="46.0" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="138.0" x2="42.4" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="146.0" x2="42.4" y2="154.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="146.0" x2="49.6" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="146.0" x2="53.2" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="146.0" x2="56.8" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="146.0" x2="60.4" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="154.0" x2="13.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="162.0" x2="13.6" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="154.0" x2="42.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="162.0" x2="42.4" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="162.0" x2="74.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="154.0" x2="71.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="162.0" x2="71.2" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="162.0" x2="78.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="162.0" x2="82.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="162.0" x2="85.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="162.0" x2="89.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="170.0" x2="13.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="178.0" x2="13.6" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="170.0" x2="42.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="178.0" x2="42.4" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="178.0" x2="74.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="170.0" x2="71.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="178.0" x2="71.2" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="178.0" x2="78.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="178.0" x2="82.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="178.0" x2="85.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="178.0" x2="89.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="186.0" x2="13.6" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="194.0" x2="13.6" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="186.0" x2="42.4" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="194.0" x2="42.4" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="194.0" x2="74.8" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="186.0" x2="71.2" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="194.0" x2="71.2" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="194.0" x2="78.4" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="194.0" x2="82.0" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="194.0" x2="85.6" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="194.0" x2="89.2" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="202.0" x2="13.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="210.0" x2="13.6" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="202.0" x2="42.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="210.0" x2="42.4" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="210.0" x2="74.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="202.0" x2="71.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="210.0" x2="71.2" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="210.0" x2="78.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="210.0" x2="82.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="210.0" x2="85.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="210.0" x2="89.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="218.0" x2="13.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="226.0" x2="13.6" y2="234.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="218.0" x2="42.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="226.0" x2="42.4" y2="234.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="226.0" x2="74.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="218.0" x2="71.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="226.0" x2="78.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="226.0" x2="82.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="226.0" x2="85.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="226.0" x2="89.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="234.0" x2="13.6" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="242.0" x2="13.6" y2="250.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="242.0" x2="46.0" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="234.0" x2="42.4" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="242.0" x2="42.4" y2="250.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="242.0" x2="49.6" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="242.0" x2="53.2" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="242.0" x2="56.8" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="242.0" x2="60.4" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="250.0" x2="13.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="258.0" x2="13.6" y2="266.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="250.0" x2="42.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="258.0" x2="42.4" y2="266.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="258.0" x2="74.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="250.0" x2="71.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="258.0" x2="71.2" y2="266.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="258.0" x2="78.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="258.0" x2="82.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="258.0" x2="85.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="258.0" x2="89.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="266.0" x2="13.6" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="274.0" x2="13.6" y2="282.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="266.0" x2="42.4" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="274.0" x2="42.4" y2="282.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="274.0" x2="74.8" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="266.0" x2="71.2" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="274.0" x2="71.2" y2="282.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="274.0" x2="78.4" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="274.0" x2="82.0" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="274.0" x2="85.6" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="274.0" x2="89.2" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="282.0" x2="13.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="290.0" x2="13.6" y2="298.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="282.0" x2="42.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="290.0" x2="42.4" y2="298.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="290.0" x2="74.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="282.0" x2="71.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="290.0" x2="71.2" y2="298.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="290.0" x2="78.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="290.0" x2="82.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="290.0" x2="85.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="290.0" x2="89.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="298.0" x2="13.6" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="306.0" x2="13.6" y2="314.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="298.0" x2="42.4" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="306.0" x2="42.4" y2="314.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="306.0" x2="74.8" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="298.0" x2="71.2" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="306.0" x2="71.2" y2="314.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="306.0" x2="78.4" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="306.0" x2="82.0" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="306.0" x2="85.6" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="306.0" x2="89.2" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="314.0" x2="13.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="322.0" x2="13.6" y2="330.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="314.0" x2="42.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="322.0" x2="42.4" y2="330.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="322.0" x2="74.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="314.0" x2="71.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="322.0" x2="78.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="322.0" x2="82.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="322.0" x2="85.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="322.0" x2="89.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="330.0" x2="13.6" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="338.0" x2="13.6" y2="346.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="338.0" x2="46.0" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="330.0" x2="42.4" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="338.0" x2="49.6" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="338.0" x2="53.2" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="338.0" x2="56.8" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="338.0" x2="60.4" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="346.0" x2="13.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="354.0" x2="13.6" y2="362.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="354.0" x2="74.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="346.0" x2="71.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="354.0" x2="78.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="354.0" x2="82.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="354.0" x2="85.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="354.0" x2="89.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="362.0" x2="13.6" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="370.0" x2="13.6" y2="378.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="370.0" x2="103.6" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="362.0" x2="100.0" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="370.0" x2="100.0" y2="378.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="370.0" x2="107.2" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="370.0" x2="110.8" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="370.0" x2="114.4" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="370.0" x2="118.0" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="378.0" x2="13.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="386.0" x2="13.6" y2="394.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="386.0" x2="103.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="378.0" x2="100.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="386.0" x2="100.0" y2="394.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="386.0" x2="107.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="386.0" x2="110.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="386.0" x2="114.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="386.0" x2="118.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="394.0" x2="13.6" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="402.0" x2="13.6" y2="410.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="402.0" x2="103.6" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="394.0" x2="100.0" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="402.0" x2="100.0" y2="410.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="402.0" x2="107.2" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="402.0" x2="110.8" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="402.0" x2="114.4" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="402.0" x2="118.0" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="410.0" x2="13.6" y2="418.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="418.0" x2="13.6" y2="426.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="418.0" x2="103.6" y2="418.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="410.0" x2="100.0" y2="418.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="418.0" x2="100.0" y2="426.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="418.0" x2="107.2" y2="418.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="418.0" x2="110.8" y2="418.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="418.0" x2="114.4" y2="418.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="418.0" x2="118.0" y2="418.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="426.0" x2="13.6" y2="434.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="434.0" x2="13.6" y2="442.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="434.0" x2="103.6" y2="434.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="426.0" x2="100.0" y2="434.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="434.0" x2="100.0" y2="442.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="434.0" x2="107.2" y2="434.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="434.0" x2="110.8" y2="434.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="434.0" x2="114.4" y2="434.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="434.0" x2="118.0" y2="434.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="442.0" x2="13.6" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="450.0" x2="13.6" y2="458.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="450.0" x2="103.6" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="442.0" x2="100.0" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="450.0" x2="100.0" y2="458.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="450.0" x2="107.2" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="450.0" x2="110.8" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="450.0" x2="114.4" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="450.0" x2="118.0" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="458.0" x2="13.6" y2="466.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="466.0" x2="13.6" y2="474.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="466.0" x2="103.6" y2="466.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="458.0" x2="100.0" y2="466.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="466.0" x2="100.0" y2="474.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="466.0" x2="107.2" y2="466.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="466.0" x2="110.8" y2="466.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="466.0" x2="114.4" y2="466.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="466.0" x2="118.0" y2="466.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="474.0" x2="13.6" y2="482.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="482.0" x2="13.6" y2="490.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="482.0" x2="103.6" y2="482.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="474.0" x2="100.0" y2="482.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="482.0" x2="107.2" y2="482.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="482.0" x2="110.8" y2="482.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="482.0" x2="114.4" y2="482.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="482.0" x2="118.0" y2="482.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="498.0" x2="17.2" y2="498.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="490.0" x2="13.6" y2="498.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="498.0" x2="13.6" y2="506.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="498.0" x2="20.8" y2="498.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="498.0" x2="24.4" y2="498.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="498.0" x2="28.0" y2="498.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="498.0" x2="31.6" y2="498.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="506.0" x2="13.6" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="514.0" x2="13.6" y2="522.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="514.0" x2="46.0" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="506.0" x2="42.4" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="514.0" x2="49.6" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="514.0" x2="53.2" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="514.0" x2="56.8" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="514.0" x2="60.4" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="530.0" x2="17.2" y2="530.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="522.0" x2="13.6" y2="530.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="530.0" x2="13.6" y2="538.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="530.0" x2="20.8" y2="530.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="530.0" x2="24.4" y2="530.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="530.0" x2="28.0" y2="530.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="530.0" x2="31.6" y2="530.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="538.0" x2="13.6" y2="546.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="546.0" x2="13.6" y2="554.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="546.0" x2="46.0" y2="546.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="538.0" x2="42.4" y2="546.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="546.0" x2="42.4" y2="554.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="546.0" x2="49.6" y2="546.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="546.0" x2="53.2" y2="546.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="546.0" x2="56.8" y2="546.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="546.0" x2="60.4" y2="546.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="554.0" x2="13.6" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="562.0" x2="13.6" y2="570.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="554.0" x2="42.4" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="562.0" x2="42.4" y2="570.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="562.0" x2="74.8" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="554.0" x2="71.2" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="562.0" x2="71.2" y2="570.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="562.0" x2="78.4" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="562.0" x2="82.0" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="562.0" x2="85.6" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="562.0" x2="89.2" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="570.0" x2="13.6" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="578.0" x2="13.6" y2="586.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="570.0" x2="42.4" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="578.0" x2="42.4" y2="586.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="578.0" x2="74.8" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="570.0" x2="71.2" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="578.0" x2="71.2" y2="586.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="578.0" x2="78.4" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="578.0" x2="82.0" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="578.0" x2="85.6" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="578.0" x2="89.2" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="586.0" x2="13.6" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="594.0" x2="13.6" y2="602.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="586.0" x2="42.4" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="594.0" x2="42.4" y2="602.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="594.0" x2="74.8" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="586.0" x2="71.2" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="594.0" x2="71.2" y2="602.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="594.0" x2="78.4" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="594.0" x2="82.0" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="594.0" x2="85.6" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="594.0" x2="89.2" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="602.0" x2="13.6" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="610.0" x2="13.6" y2="618.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="602.0" x2="42.4" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="610.0" x2="42.4" y2="618.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="610.0" x2="74.8" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="602.0" x2="71.2" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="610.0" x2="71.2" y2="618.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="610.0" x2="78.4" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="610.0" x2="82.0" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="610.0" x2="85.6" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="610.0" x2="89.2" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="618.0" x2="13.6" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="626.0" x2="13.6" y2="634.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="618.0" x2="42.4" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="626.0" x2="42.4" y2="634.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="626.0" x2="74.8" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="618.0" x2="71.2" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="626.0" x2="71.2" y2="634.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="626.0" x2="78.4" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="626.0" x2="82.0" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="626.0" x2="85.6" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="626.0" x2="89.2" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="634.0" x2="13.6" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="642.0" x2="13.6" y2="650.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="634.0" x2="42.4" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="642.0" x2="42.4" y2="650.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="642.0" x2="74.8" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="634.0" x2="71.2" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="642.0" x2="71.2" y2="650.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="642.0" x2="78.4" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="642.0" x2="82.0" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="642.0" x2="85.6" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="642.0" x2="89.2" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="650.0" x2="13.6" y2="658.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="658.0" x2="13.6" y2="666.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="650.0" x2="42.4" y2="658.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="658.0" x2="42.4" y2="666.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="658.0" x2="74.8" y2="658.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="650.0" x2="71.2" y2="658.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="658.0" x2="78.4" y2="658.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="658.0" x2="82.0" y2="658.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="658.0" x2="85.6" y2="658.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="658.0" x2="89.2" y2="658.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="666.0" x2="13.6" y2="674.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="674.0" x2="13.6" y2="682.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="666.0" x2="42.4" y2="674.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="674.0" x2="42.4" y2="682.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="674.0" x2="103.6" y2="674.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="666.0" x2="100.0" y2="674.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="674.0" x2="100.0" y2="682.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="674.0" x2="107.2" y2="674.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="674.0" x2="110.8" y2="674.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="674.0" x2="114.4" y2="674.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="674.0" x2="118.0" y2="674.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="682.0" x2="13.6" y2="690.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="690.0" x2="13.6" y2="698.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="682.0" x2="42.4" y2="690.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="690.0" x2="42.4" y2="698.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="690.0" x2="103.6" y2="690.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="682.0" x2="100.0" y2="690.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="690.0" x2="100.0" y2="698.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="690.0" x2="107.2" y2="690.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="690.0" x2="110.8" y2="690.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="690.0" x2="114.4" y2="690.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="690.0" x2="118.0" y2="690.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="698.0" x2="13.6" y2="706.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="706.0" x2="13.6" y2="714.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="698.0" x2="42.4" y2="706.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="706.0" x2="42.4" y2="714.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="706.0" x2="103.6" y2="706.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="698.0" x2="100.0" y2="706.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="706.0" x2="100.0" y2="714.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="706.0" x2="107.2" y2="706.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="706.0" x2="110.8" y2="706.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="706.0" x2="114.4" y2="706.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="706.0" x2="118.0" y2="706.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="714.0" x2="13.6" y2="722.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="722.0" x2="13.6" y2="730.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="714.0" x2="42.4" y2="722.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="722.0" x2="42.4" y2="730.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="722.0" x2="103.6" y2="722.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="714.0" x2="100.0" y2="722.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="722.0" x2="100.0" y2="730.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="722.0" x2="107.2" y2="722.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="722.0" x2="110.8" y2="722.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="722.0" x2="114.4" y2="722.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="722.0" x2="118.0" y2="722.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="730.0" x2="13.6" y2="738.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="738.0" x2="13.6" y2="746.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="730.0" x2="42.4" y2="738.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="738.0" x2="42.4" y2="746.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="738.0" x2="103.6" y2="738.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="730.0" x2="100.0" y2="738.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="738.0" x2="107.2" y2="738.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="738.0" x2="110.8" y2="738.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="738.0" x2="114.4" y2="738.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="738.0" x2="118.0" y2="738.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="746.0" x2="13.6" y2="754.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="754.0" x2="13.6" y2="762.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="754.0" x2="46.0" y2="754.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="746.0" x2="42.4" y2="754.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="754.0" x2="42.4" y2="762.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="754.0" x2="49.6" y2="754.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="754.0" x2="53.2" y2="754.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="754.0" x2="56.8" y2="754.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="754.0" x2="60.4" y2="754.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="762.0" x2="13.6" y2="770.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="770.0" x2="13.6" y2="778.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="762.0" x2="42.4" y2="770.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="770.0" x2="42.4" y2="778.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="770.0" x2="74.8" y2="770.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="762.0" x2="71.2" y2="770.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="770.0" x2="71.2" y2="778.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="770.0" x2="78.4" y2="770.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="770.0" x2="82.0" y2="770.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="770.0" x2="85.6" y2="770.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="770.0" x2="89.2" y2="770.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="778.0" x2="13.6" y2="786.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="786.0" x2="13.6" y2="794.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="778.0" x2="42.4" y2="786.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="786.0" x2="42.4" y2="794.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="786.0" x2="74.8" y2="786.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="778.0" x2="71.2" y2="786.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="786.0" x2="71.2" y2="794.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="786.0" x2="78.4" y2="786.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="786.0" x2="82.0" y2="786.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="786.0" x2="85.6" y2="786.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="786.0" x2="89.2" y2="786.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="794.0" x2="13.6" y2="802.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="802.0" x2="13.6" y2="810.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="794.0" x2="42.4" y2="802.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="802.0" x2="42.4" y2="810.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="802.0" x2="74.8" y2="802.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="794.0" x2="71.2" y2="802.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="802.0" x2="71.2" y2="810.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="802.0" x2="78.4" y2="802.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="802.0" x2="82.0" y2="802.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="802.0" x2="85.6" y2="802.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="802.0" x2="89.2" y2="802.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="810.0" x2="13.6" y2="818.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="818.0" x2="13.6" y2="826.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="810.0" x2="42.4" y2="818.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="818.0" x2="42.4" y2="826.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="818.0" x2="74.8" y2="818.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="810.0" x2="71.2" y2="818.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="818.0" x2="71.2" y2="826.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="818.0" x2="78.4" y2="818.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="818.0" x2="82.0" y2="818.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="818.0" x2="85.6" y2="818.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="818.0" x2="89.2" y2="818.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="826.0" x2="13.6" y2="834.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="834.0" x2="13.6" y2="842.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="826.0" x2="42.4" y2="834.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="834.0" x2="42.4" y2="842.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="834.0" x2="74.8" y2="834.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="826.0" x2="71.2" y2="834.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="834.0" x2="71.2" y2="842.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="834.0" x2="78.4" y2="834.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="834.0" x2="82.0" y2="834.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="834.0" x2="85.6" y2="834.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="834.0" x2="89.2" y2="834.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="842.0" x2="13.6" y2="850.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="850.0" x2="13.6" y2="858.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="842.0" x2="42.4" y2="850.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="850.0" x2="42.4" y2="858.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="850.0" x2="74.8" y2="850.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="842.0" x2="71.2" y2="850.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="850.0" x2="78.4" y2="850.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="850.0" x2="82.0" y2="850.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="850.0" x2="85.6" y2="850.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="850.0" x2="89.2" y2="850.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="858.0" x2="13.6" y2="866.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="866.0" x2="13.6" y2="874.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="866.0" x2="46.0" y2="866.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="858.0" x2="42.4" y2="866.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="866.0" x2="42.4" y2="874.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="866.0" x2="49.6" y2="866.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="866.0" x2="53.2" y2="866.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="866.0" x2="56.8" y2="866.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="866.0" x2="60.4" y2="866.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="874.0" x2="13.6" y2="882.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="882.0" x2="13.6" y2="890.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="874.0" x2="42.4" y2="882.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="882.0" x2="42.4" y2="890.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="882.0" x2="74.8" y2="882.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="874.0" x2="71.2" y2="882.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="882.0" x2="71.2" y2="890.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="882.0" x2="78.4" y2="882.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="882.0" x2="82.0" y2="882.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="882.0" x2="85.6" y2="882.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="882.0" x2="89.2" y2="882.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="890.0" x2="13.6" y2="898.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="898.0" x2="13.6" y2="906.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="890.0" x2="42.4" y2="898.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="898.0" x2="42.4" y2="906.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="898.0" x2="74.8" y2="898.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="890.0" x2="71.2" y2="898.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="898.0" x2="71.2" y2="906.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="898.0" x2="78.4" y2="898.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="898.0" x2="82.0" y2="898.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="898.0" x2="85.6" y2="898.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="898.0" x2="89.2" y2="898.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="906.0" x2="13.6" y2="914.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="914.0" x2="13.6" y2="922.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="906.0" x2="42.4" y2="914.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="914.0" x2="42.4" y2="922.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="914.0" x2="74.8" y2="914.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="906.0" x2="71.2" y2="914.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="914.0" x2="71.2" y2="922.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="914.0" x2="78.4" y2="914.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="914.0" x2="82.0" y2="914.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="914.0" x2="85.6" y2="914.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="914.0" x2="89.2" y2="914.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="922.0" x2="13.6" y2="930.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="930.0" x2="13.6" y2="938.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="922.0" x2="42.4" y2="930.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="930.0" x2="42.4" y2="938.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="930.0" x2="74.8" y2="930.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="922.0" x2="71.2" y2="930.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="930.0" x2="71.2" y2="938.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="930.0" x2="78.4" y2="930.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="930.0" x2="82.0" y2="930.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="930.0" x2="85.6" y2="930.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="930.0" x2="89.2" y2="930.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="938.0" x2="13.6" y2="946.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="946.0" x2="13.6" y2="954.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="938.0" x2="42.4" y2="946.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="946.0" x2="42.4" y2="954.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="946.0" x2="74.8" y2="946.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="938.0" x2="71.2" y2="946.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="946.0" x2="71.2" y2="954.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="946.0" x2="78.4" y2="946.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="946.0" x2="82.0" y2="946.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="946.0" x2="85.6" y2="946.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="946.0" x2="89.2" y2="946.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="954.0" x2="13.6" y2="962.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="962.0" x2="13.6" y2="970.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="954.0" x2="42.4" y2="962.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="962.0" x2="42.4" y2="970.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="962.0" x2="74.8" y2="962.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="954.0" x2="71.2" y2="962.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="962.0" x2="71.2" y2="970.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="962.0" x2="78.4" y2="962.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="962.0" x2="82.0" y2="962.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="962.0" x2="85.6" y2="962.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="962.0" x2="89.2" y2="962.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="970.0" x2="13.6" y2="978.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="978.0" x2="13.6" y2="986.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="970.0" x2="42.4" y2="978.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="978.0" x2="42.4" y2="986.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="978.0" x2="74.8" y2="978.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="970.0" x2="71.2" y2="978.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="978.0" x2="78.4" y2="978.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="978.0" x2="82.0" y2="978.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="978.0" x2="85.6" y2="978.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="978.0" x2="89.2" y2="978.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="986.0" x2="13.6" y2="994.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="994.0" x2="13.6" y2="1002.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="994.0" x2="46.0" y2="994.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="986.0" x2="42.4" y2="994.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="994.0" x2="42.4" y2="1002.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="994.0" x2="49.6" y2="994.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="994.0" x2="53.2" y2="994.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="994.0" x2="56.8" y2="994.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="994.0" x2="60.4" y2="994.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1002.0" x2="13.6" y2="1010.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1010.0" x2="13.6" y2="1018.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1002.0" x2="42.4" y2="1010.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1010.0" x2="42.4" y2="1018.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1010.0" x2="74.8" y2="1010.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1002.0" x2="71.2" y2="1010.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1010.0" x2="78.4" y2="1010.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1010.0" x2="82.0" y2="1010.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1010.0" x2="85.6" y2="1010.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1010.0" x2="89.2" y2="1010.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1018.0" x2="13.6" y2="1026.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1026.0" x2="13.6" y2="1034.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1026.0" x2="46.0" y2="1026.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1018.0" x2="42.4" y2="1026.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1026.0" x2="42.4" y2="1034.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="1026.0" x2="49.6" y2="1026.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="1026.0" x2="53.2" y2="1026.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="1026.0" x2="56.8" y2="1026.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="1026.0" x2="60.4" y2="1026.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1034.0" x2="13.6" y2="1042.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1042.0" x2="13.6" y2="1050.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1034.0" x2="42.4" y2="1042.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1042.0" x2="42.4" y2="1050.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1042.0" x2="74.8" y2="1042.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1034.0" x2="71.2" y2="1042.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1042.0" x2="71.2" y2="1050.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1042.0" x2="78.4" y2="1042.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1042.0" x2="82.0" y2="1042.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1042.0" x2="85.6" y2="1042.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1042.0" x2="89.2" y2="1042.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1050.0" x2="13.6" y2="1058.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1058.0" x2="13.6" y2="1066.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1050.0" x2="42.4" y2="1058.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1058.0" x2="42.4" y2="1066.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1058.0" x2="74.8" y2="1058.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1050.0" x2="71.2" y2="1058.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1058.0" x2="71.2" y2="1066.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1058.0" x2="78.4" y2="1058.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1058.0" x2="82.0" y2="1058.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1058.0" x2="85.6" y2="1058.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1058.0" x2="89.2" y2="1058.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1066.0" x2="13.6" y2="1074.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1074.0" x2="13.6" y2="1082.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1066.0" x2="42.4" y2="1074.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1074.0" x2="42.4" y2="1082.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1074.0" x2="74.8" y2="1074.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1066.0" x2="71.2" y2="1074.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1074.0" x2="71.2" y2="1082.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1074.0" x2="78.4" y2="1074.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1074.0" x2="82.0" y2="1074.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1074.0" x2="85.6" y2="1074.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1074.0" x2="89.2" y2="1074.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1082.0" x2="13.6" y2="1090.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1090.0" x2="13.6" y2="1098.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1082.0" x2="42.4" y2="1090.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1090.0" x2="42.4" y2="1098.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1090.0" x2="74.8" y2="1090.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1082.0" x2="71.2" y2="1090.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1090.0" x2="71.2" y2="1098.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1090.0" x2="78.4" y2="1090.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1090.0" x2="82.0" y2="1090.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1090.0" x2="85.6" y2="1090.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1090.0" x2="89.2" y2="1090.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1098.0" x2="13.6" y2="1106.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1106.0" x2="13.6" y2="1114.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1098.0" x2="42.4" y2="1106.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1106.0" x2="42.4" y2="1114.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1106.0" x2="74.8" y2="1106.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1098.0" x2="71.2" y2="1106.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1106.0" x2="78.4" y2="1106.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1106.0" x2="82.0" y2="1106.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1106.0" x2="85.6" y2="1106.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1106.0" x2="89.2" y2="1106.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1114.0" x2="13.6" y2="1122.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1122.0" x2="13.6" y2="1130.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1122.0" x2="46.0" y2="1122.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1114.0" x2="42.4" y2="1122.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1122.0" x2="42.4" y2="1130.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="1122.0" x2="49.6" y2="1122.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="1122.0" x2="53.2" y2="1122.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="1122.0" x2="56.8" y2="1122.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="1122.0" x2="60.4" y2="1122.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1130.0" x2="13.6" y2="1138.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1138.0" x2="13.6" y2="1146.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1130.0" x2="42.4" y2="1138.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1138.0" x2="42.4" y2="1146.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1138.0" x2="74.8" y2="1138.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1130.0" x2="71.2" y2="1138.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1138.0" x2="71.2" y2="1146.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1138.0" x2="78.4" y2="1138.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1138.0" x2="82.0" y2="1138.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1138.0" x2="85.6" y2="1138.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1138.0" x2="89.2" y2="1138.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1146.0" x2="13.6" y2="1154.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1154.0" x2="13.6" y2="1162.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1146.0" x2="42.4" y2="1154.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1154.0" x2="42.4" y2="1162.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1154.0" x2="74.8" y2="1154.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1146.0" x2="71.2" y2="1154.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1154.0" x2="71.2" y2="1162.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1154.0" x2="78.4" y2="1154.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1154.0" x2="82.0" y2="1154.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1154.0" x2="85.6" y2="1154.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1154.0" x2="89.2" y2="1154.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1162.0" x2="13.6" y2="1170.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1170.0" x2="13.6" y2="1178.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1162.0" x2="42.4" y2="1170.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1170.0" x2="42.4" y2="1178.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1170.0" x2="74.8" y2="1170.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1162.0" x2="71.2" y2="1170.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1170.0" x2="71.2" y2="1178.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1170.0" x2="78.4" y2="1170.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1170.0" x2="82.0" y2="1170.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1170.0" x2="85.6" y2="1170.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1170.0" x2="89.2" y2="1170.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1178.0" x2="13.6" y2="1186.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1186.0" x2="13.6" y2="1194.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1178.0" x2="42.4" y2="1186.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1186.0" x2="42.4" y2="1194.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1186.0" x2="74.8" y2="1186.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1178.0" x2="71.2" y2="1186.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1186.0" x2="71.2" y2="1194.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1186.0" x2="78.4" y2="1186.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1186.0" x2="82.0" y2="1186.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1186.0" x2="85.6" y2="1186.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1186.0" x2="89.2" y2="1186.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1194.0" x2="13.6" y2="1202.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1202.0" x2="13.6" y2="1210.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1194.0" x2="42.4" y2="1202.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1202.0" x2="42.4" y2="1210.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1202.0" x2="74.8" y2="1202.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1194.0" x2="71.2" y2="1202.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1202.0" x2="71.2" y2="1210.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1202.0" x2="78.4" y2="1202.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1202.0" x2="82.0" y2="1202.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1202.0" x2="85.6" y2="1202.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1202.0" x2="89.2" y2="1202.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1210.0" x2="13.6" y2="1218.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1218.0" x2="13.6" y2="1226.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1210.0" x2="42.4" y2="1218.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1218.0" x2="42.4" y2="1226.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1218.0" x2="74.8" y2="1218.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1210.0" x2="71.2" y2="1218.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1218.0" x2="78.4" y2="1218.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1218.0" x2="82.0" y2="1218.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1218.0" x2="85.6" y2="1218.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1218.0" x2="89.2" y2="1218.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1226.0" x2="13.6" y2="1234.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1234.0" x2="13.6" y2="1242.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1234.0" x2="46.0" y2="1234.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1226.0" x2="42.4" y2="1234.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1234.0" x2="42.4" y2="1242.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="1234.0" x2="49.6" y2="1234.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="1234.0" x2="53.2" y2="1234.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="1234.0" x2="56.8" y2="1234.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="1234.0" x2="60.4" y2="1234.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1242.0" x2="13.6" y2="1250.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1250.0" x2="13.6" y2="1258.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1250.0" x2="46.0" y2="1250.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1242.0" x2="42.4" y2="1250.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="1250.0" x2="49.6" y2="1250.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="1250.0" x2="53.2" y2="1250.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="1250.0" x2="56.8" y2="1250.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="1250.0" x2="60.4" y2="1250.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1258.0" x2="13.6" y2="1266.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1266.0" x2="13.6" y2="1274.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1266.0" x2="74.8" y2="1266.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1258.0" x2="71.2" y2="1266.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1266.0" x2="71.2" y2="1274.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1266.0" x2="78.4" y2="1266.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1266.0" x2="82.0" y2="1266.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1266.0" x2="85.6" y2="1266.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1266.0" x2="89.2" y2="1266.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1274.0" x2="13.6" y2="1282.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1282.0" x2="13.6" y2="1290.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1282.0" x2="74.8" y2="1282.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1274.0" x2="71.2" y2="1282.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1282.0" x2="71.2" y2="1290.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1282.0" x2="78.4" y2="1282.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1282.0" x2="82.0" y2="1282.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1282.0" x2="85.6" y2="1282.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1282.0" x2="89.2" y2="1282.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1290.0" x2="13.6" y2="1298.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1298.0" x2="13.6" y2="1306.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1298.0" x2="74.8" y2="1298.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1290.0" x2="71.2" y2="1298.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1298.0" x2="71.2" y2="1306.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1298.0" x2="78.4" y2="1298.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1298.0" x2="82.0" y2="1298.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1298.0" x2="85.6" y2="1298.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1298.0" x2="89.2" y2="1298.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1306.0" x2="13.6" y2="1314.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1314.0" x2="13.6" y2="1322.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1314.0" x2="74.8" y2="1314.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1306.0" x2="71.2" y2="1314.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1314.0" x2="71.2" y2="1322.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1314.0" x2="78.4" y2="1314.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1314.0" x2="82.0" y2="1314.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1314.0" x2="85.6" y2="1314.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1314.0" x2="89.2" y2="1314.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1322.0" x2="13.6" y2="1330.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1330.0" x2="13.6" y2="1338.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1330.0" x2="74.8" y2="1330.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1322.0" x2="71.2" y2="1330.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1330.0" x2="71.2" y2="1338.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1330.0" x2="78.4" y2="1330.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1330.0" x2="82.0" y2="1330.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1330.0" x2="85.6" y2="1330.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1330.0" x2="89.2" y2="1330.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1338.0" x2="13.6" y2="1346.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1346.0" x2="13.6" y2="1354.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1346.0" x2="74.8" y2="1346.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1338.0" x2="71.2" y2="1346.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1346.0" x2="71.2" y2="1354.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1346.0" x2="78.4" y2="1346.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1346.0" x2="82.0" y2="1346.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1346.0" x2="85.6" y2="1346.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1346.0" x2="89.2" y2="1346.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1354.0" x2="13.6" y2="1362.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1362.0" x2="13.6" y2="1370.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1362.0" x2="74.8" y2="1362.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1354.0" x2="71.2" y2="1362.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1362.0" x2="71.2" y2="1370.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1362.0" x2="78.4" y2="1362.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1362.0" x2="82.0" y2="1362.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1362.0" x2="85.6" y2="1362.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1362.0" x2="89.2" y2="1362.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1370.0" x2="13.6" y2="1378.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1378.0" x2="13.6" y2="1386.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1378.0" x2="74.8" y2="1378.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1370.0" x2="71.2" y2="1378.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1378.0" x2="71.2" y2="1386.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1378.0" x2="78.4" y2="1378.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1378.0" x2="82.0" y2="1378.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1378.0" x2="85.6" y2="1378.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1378.0" x2="89.2" y2="1378.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1386.0" x2="13.6" y2="1394.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1394.0" x2="13.6" y2="1402.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1394.0" x2="74.8" y2="1394.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1386.0" x2="71.2" y2="1394.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1394.0" x2="71.2" y2="1402.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1394.0" x2="78.4" y2="1394.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1394.0" x2="82.0" y2="1394.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1394.0" x2="85.6" y2="1394.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1394.0" x2="89.2" y2="1394.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1402.0" x2="13.6" y2="1410.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1410.0" x2="13.6" y2="1418.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1410.0" x2="74.8" y2="1410.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1402.0" x2="71.2" y2="1410.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1410.0" x2="78.4" y2="1410.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1410.0" x2="82.0" y2="1410.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1410.0" x2="85.6" y2="1410.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1410.0" x2="89.2" y2="1410.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1426.0" x2="17.2" y2="1426.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1418.0" x2="13.6" y2="1426.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1426.0" x2="13.6" y2="1434.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="1426.0" x2="20.8" y2="1426.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="1426.0" x2="24.4" y2="1426.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="1426.0" x2="28.0" y2="1426.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="1426.0" x2="31.6" y2="1426.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1434.0" x2="13.6" y2="1442.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1442.0" x2="13.6" y2="1450.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1442.0" x2="46.0" y2="1442.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1434.0" x2="42.4" y2="1442.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="1442.0" x2="49.6" y2="1442.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="1442.0" x2="53.2" y2="1442.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="1442.0" x2="56.8" y2="1442.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="1442.0" x2="60.4" y2="1442.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1450.0" x2="13.6" y2="1458.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1458.0" x2="13.6" y2="1466.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1458.0" x2="74.8" y2="1458.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1450.0" x2="71.2" y2="1458.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1458.0" x2="71.2" y2="1466.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1458.0" x2="78.4" y2="1458.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1458.0" x2="82.0" y2="1458.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1458.0" x2="85.6" y2="1458.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1458.0" x2="89.2" y2="1458.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1466.0" x2="13.6" y2="1474.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1474.0" x2="13.6" y2="1482.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1466.0" x2="71.2" y2="1474.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1474.0" x2="71.2" y2="1482.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1474.0" x2="103.6" y2="1474.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1466.0" x2="100.0" y2="1474.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1474.0" x2="100.0" y2="1482.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="1474.0" x2="107.2" y2="1474.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="1474.0" x2="110.8" y2="1474.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="1474.0" x2="114.4" y2="1474.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="1474.0" x2="118.0" y2="1474.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1482.0" x2="13.6" y2="1490.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1490.0" x2="13.6" y2="1498.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1482.0" x2="71.2" y2="1490.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1490.0" x2="71.2" y2="1498.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1490.0" x2="103.6" y2="1490.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1482.0" x2="100.0" y2="1490.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1490.0" x2="100.0" y2="1498.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="1490.0" x2="107.2" y2="1490.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="1490.0" x2="110.8" y2="1490.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="1490.0" x2="114.4" y2="1490.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="1490.0" x2="118.0" y2="1490.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1498.0" x2="13.6" y2="1506.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1506.0" x2="13.6" y2="1514.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1498.0" x2="71.2" y2="1506.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1506.0" x2="71.2" y2="1514.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1506.0" x2="103.6" y2="1506.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1498.0" x2="100.0" y2="1506.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1506.0" x2="100.0" y2="1514.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="1506.0" x2="107.2" y2="1506.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="1506.0" x2="110.8" y2="1506.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="1506.0" x2="114.4" y2="1506.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="1506.0" x2="118.0" y2="1506.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1514.0" x2="13.6" y2="1522.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1522.0" x2="13.6" y2="1530.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1514.0" x2="71.2" y2="1522.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1522.0" x2="71.2" y2="1530.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1522.0" x2="103.6" y2="1522.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1514.0" x2="100.0" y2="1522.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1522.0" x2="100.0" y2="1530.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="1522.0" x2="107.2" y2="1522.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="1522.0" x2="110.8" y2="1522.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="1522.0" x2="114.4" y2="1522.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="1522.0" x2="118.0" y2="1522.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1530.0" x2="13.6" y2="1538.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1538.0" x2="13.6" y2="1546.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1530.0" x2="71.2" y2="1538.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1538.0" x2="71.2" y2="1546.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1538.0" x2="103.6" y2="1538.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1530.0" x2="100.0" y2="1538.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1538.0" x2="100.0" y2="1546.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="1538.0" x2="107.2" y2="1538.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="1538.0" x2="110.8" y2="1538.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="1538.0" x2="114.4" y2="1538.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="1538.0" x2="118.0" y2="1538.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1546.0" x2="13.6" y2="1554.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1554.0" x2="13.6" y2="1562.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1546.0" x2="71.2" y2="1554.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1554.0" x2="71.2" y2="1562.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1554.0" x2="103.6" y2="1554.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1546.0" x2="100.0" y2="1554.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1554.0" x2="100.0" y2="1562.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="1554.0" x2="107.2" y2="1554.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="1554.0" x2="110.8" y2="1554.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="1554.0" x2="114.4" y2="1554.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="1554.0" x2="118.0" y2="1554.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1562.0" x2="13.6" y2="1570.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1570.0" x2="13.6" y2="1578.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1562.0" x2="71.2" y2="1570.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1570.0" x2="71.2" y2="1578.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1570.0" x2="103.6" y2="1570.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1562.0" x2="100.0" y2="1570.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1570.0" x2="100.0" y2="1578.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="1570.0" x2="107.2" y2="1570.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="1570.0" x2="110.8" y2="1570.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="1570.0" x2="114.4" y2="1570.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="1570.0" x2="118.0" y2="1570.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1578.0" x2="13.6" y2="1586.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1586.0" x2="13.6" y2="1594.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1578.0" x2="71.2" y2="1586.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1586.0" x2="71.2" y2="1594.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1586.0" x2="103.6" y2="1586.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1578.0" x2="100.0" y2="1586.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1586.0" x2="100.0" y2="1594.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="1586.0" x2="107.2" y2="1586.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="1586.0" x2="110.8" y2="1586.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="1586.0" x2="114.4" y2="1586.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="1586.0" x2="118.0" y2="1586.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1594.0" x2="13.6" y2="1602.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1602.0" x2="13.6" y2="1610.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1594.0" x2="71.2" y2="1602.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1602.0" x2="71.2" y2="1610.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1602.0" x2="103.6" y2="1602.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1594.0" x2="100.0" y2="1602.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1602.0" x2="100.0" y2="1610.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="1602.0" x2="107.2" y2="1602.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="1602.0" x2="110.8" y2="1602.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="1602.0" x2="114.4" y2="1602.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="1602.0" x2="118.0" y2="1602.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1610.0" x2="13.6" y2="1618.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1618.0" x2="13.6" y2="1626.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1610.0" x2="71.2" y2="1618.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1618.0" x2="71.2" y2="1626.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1618.0" x2="103.6" y2="1618.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1610.0" x2="100.0" y2="1618.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1618.0" x2="100.0" y2="1626.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="1618.0" x2="107.2" y2="1618.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="1618.0" x2="110.8" y2="1618.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="1618.0" x2="114.4" y2="1618.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="1618.0" x2="118.0" y2="1618.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1626.0" x2="13.6" y2="1634.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1634.0" x2="13.6" y2="1642.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1626.0" x2="71.2" y2="1634.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1634.0" x2="71.2" y2="1642.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1634.0" x2="103.6" y2="1634.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1626.0" x2="100.0" y2="1634.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1634.0" x2="100.0" y2="1642.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="1634.0" x2="107.2" y2="1634.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="1634.0" x2="110.8" y2="1634.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="1634.0" x2="114.4" y2="1634.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="1634.0" x2="118.0" y2="1634.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1642.0" x2="13.6" y2="1650.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1650.0" x2="13.6" y2="1658.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1642.0" x2="71.2" y2="1650.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1650.0" x2="71.2" y2="1658.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1650.0" x2="103.6" y2="1650.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1642.0" x2="100.0" y2="1650.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1650.0" x2="100.0" y2="1658.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="1650.0" x2="107.2" y2="1650.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="1650.0" x2="110.8" y2="1650.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="1650.0" x2="114.4" y2="1650.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="1650.0" x2="118.0" y2="1650.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1658.0" x2="13.6" y2="1666.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1666.0" x2="13.6" y2="1674.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1658.0" x2="71.2" y2="1666.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1666.0" x2="71.2" y2="1674.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1666.0" x2="103.6" y2="1666.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1658.0" x2="100.0" y2="1666.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1666.0" x2="100.0" y2="1674.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="1666.0" x2="107.2" y2="1666.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="1666.0" x2="110.8" y2="1666.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="1666.0" x2="114.4" y2="1666.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="1666.0" x2="118.0" y2="1666.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1674.0" x2="13.6" y2="1682.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1682.0" x2="13.6" y2="1690.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1674.0" x2="71.2" y2="1682.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1682.0" x2="71.2" y2="1690.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1682.0" x2="103.6" y2="1682.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1674.0" x2="100.0" y2="1682.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="1682.0" x2="107.2" y2="1682.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="1682.0" x2="110.8" y2="1682.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="1682.0" x2="114.4" y2="1682.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="1682.0" x2="118.0" y2="1682.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1690.0" x2="13.6" y2="1698.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1698.0" x2="13.6" y2="1706.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1698.0" x2="74.8" y2="1698.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="1690.0" x2="71.2" y2="1698.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="1698.0" x2="78.4" y2="1698.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="1698.0" x2="82.0" y2="1698.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="1698.0" x2="85.6" y2="1698.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="1698.0" x2="89.2" y2="1698.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1706.0" x2="13.6" y2="1714.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1714.0" x2="13.6" y2="1722.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1714.0" x2="103.6" y2="1714.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1706.0" x2="100.0" y2="1714.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1714.0" x2="100.0" y2="1722.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="1714.0" x2="107.2" y2="1714.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="1714.0" x2="110.8" y2="1714.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="1714.0" x2="114.4" y2="1714.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="1714.0" x2="118.0" y2="1714.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1722.0" x2="13.6" y2="1730.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1730.0" x2="13.6" y2="1738.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1730.0" x2="103.6" y2="1730.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1722.0" x2="100.0" y2="1730.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1730.0" x2="100.0" y2="1738.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="1730.0" x2="107.2" y2="1730.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="1730.0" x2="110.8" y2="1730.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="1730.0" x2="114.4" y2="1730.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="1730.0" x2="118.0" y2="1730.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1738.0" x2="13.6" y2="1746.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1746.0" x2="13.6" y2="1754.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1746.0" x2="103.6" y2="1746.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1738.0" x2="100.0" y2="1746.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1746.0" x2="100.0" y2="1754.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="1746.0" x2="107.2" y2="1746.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="1746.0" x2="110.8" y2="1746.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="1746.0" x2="114.4" y2="1746.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="1746.0" x2="118.0" y2="1746.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1754.0" x2="13.6" y2="1762.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1762.0" x2="13.6" y2="1770.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1762.0" x2="103.6" y2="1762.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1754.0" x2="100.0" y2="1762.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1762.0" x2="100.0" y2="1770.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="1762.0" x2="107.2" y2="1762.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="1762.0" x2="110.8" y2="1762.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="1762.0" x2="114.4" y2="1762.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="1762.0" x2="118.0" y2="1762.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1770.0" x2="13.6" y2="1778.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1778.0" x2="13.6" y2="1786.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1778.0" x2="103.6" y2="1778.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1770.0" x2="100.0" y2="1778.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1778.0" x2="100.0" y2="1786.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="1778.0" x2="107.2" y2="1778.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="1778.0" x2="110.8" y2="1778.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="1778.0" x2="114.4" y2="1778.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="1778.0" x2="118.0" y2="1778.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1786.0" x2="13.6" y2="1794.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1794.0" x2="13.6" y2="1802.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1794.0" x2="103.6" y2="1794.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="1786.0" x2="100.0" y2="1794.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="1794.0" x2="107.2" y2="1794.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="1794.0" x2="110.8" y2="1794.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="1794.0" x2="114.4" y2="1794.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="1794.0" x2="118.0" y2="1794.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1810.0" x2="17.2" y2="1810.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="1802.0" x2="13.6" y2="1810.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="1810.0" x2="20.8" y2="1810.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="1810.0" x2="24.4" y2="1810.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="1810.0" x2="28.0" y2="1810.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="1810.0" x2="31.6" y2="1810.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1826.0" x2="46.0" y2="1826.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="1818.0" x2="42.4" y2="1826.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="1826.0" x2="49.6" y2="1826.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="1826.0" x2="53.2" y2="1826.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="1826.0" x2="56.8" y2="1826.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="1826.0" x2="60.4" y2="1826.0" stroke="#10373E" stroke-width="1.3"/><text x="10.0" y="22.0" font-size="9.5" fill="#10373E">atom-ahg-plugins/ahgDataMigrationPlugin/</text><text x="38.8" y="38.0" font-size="9.5" fill="#10373E">bin/</text><text x="67.6" y="54.0" font-size="9.5" fill="#10373E">setup-gearman.sh</text><text x="254.8" y="54.0" font-size="9.5" fill="#10373E">#</text><text x="269.2" y="54.0" font-size="9.5" fill="#10373E">Gearman</text><text x="326.8" y="54.0" font-size="9.5" fill="#10373E">installation</text><text x="420.4" y="54.0" font-size="9.5" fill="#10373E">script</text><text x="38.8" y="70.0" font-size="9.5" fill="#10373E">config/</text><text x="67.6" y="86.0" font-size="9.5" fill="#10373E">ahgDataMigrationPluginConfiguration.class.php</text><text x="67.6" y="102.0" font-size="9.5" fill="#10373E">routing.yml</text><text x="38.8" y="118.0" font-size="9.5" fill="#10373E">data/</text><text x="67.6" y="134.0" font-size="9.5" fill="#10373E">install.sql</text><text x="67.6" y="150.0" font-size="9.5" fill="#10373E">samples/</text><text x="262.0" y="150.0" font-size="9.5" fill="#10373E">#</text><text x="276.4" y="150.0" font-size="9.5" fill="#10373E">NEW:</text><text x="312.4" y="150.0" font-size="9.5" fill="#10373E">Sample</text><text x="362.8" y="150.0" font-size="9.5" fill="#10373E">CSV</text><text x="391.6" y="150.0" font-size="9.5" fill="#10373E">files</text><text x="96.4" y="166.0" font-size="9.5" fill="#10373E">archives_sample.csv</text><text x="254.8" y="166.0" font-size="9.5" fill="#10373E">#</text><text x="269.2" y="166.0" font-size="9.5" fill="#10373E">ISAD-G</text><text x="319.6" y="166.0" font-size="9.5" fill="#10373E">hierarchy</text><text x="391.6" y="166.0" font-size="9.5" fill="#10373E">example</text><text x="96.4" y="182.0" font-size="9.5" fill="#10373E">museum_sample.csv</text><text x="254.8" y="182.0" font-size="9.5" fill="#10373E">#</text><text x="269.2" y="182.0" font-size="9.5" fill="#10373E">Spectrum</text><text x="334.0" y="182.0" font-size="9.5" fill="#10373E">objects</text><text x="96.4" y="198.0" font-size="9.5" fill="#10373E">library_sample.csv</text><text x="254.8" y="198.0" font-size="9.5" fill="#10373E">#</text><text x="269.2" y="198.0" font-size="9.5" fill="#10373E">MARC/RDA</text><text x="334.0" y="198.0" font-size="9.5" fill="#10373E">records</text><text x="96.4" y="214.0" font-size="9.5" fill="#10373E">gallery_sample.csv</text><text x="254.8" y="214.0" font-size="9.5" fill="#10373E">#</text><text x="269.2" y="214.0" font-size="9.5" fill="#10373E">CCO</text><text x="298.0" y="214.0" font-size="9.5" fill="#10373E">artworks</text><text x="96.4" y="230.0" font-size="9.5" fill="#10373E">dam_sample.csv</text><text x="254.8" y="230.0" font-size="9.5" fill="#10373E">#</text><text x="269.2" y="230.0" font-size="9.5" fill="#10373E">Dublin</text><text x="319.6" y="230.0" font-size="9.5" fill="#10373E">Core</text><text x="355.6" y="230.0" font-size="9.5" fill="#10373E">assets</text><text x="67.6" y="246.0" font-size="9.5" fill="#10373E">validation/</text><text x="254.8" y="246.0" font-size="9.5" fill="#10373E">#</text><text x="269.2" y="246.0" font-size="9.5" fill="#10373E">NEW:</text><text x="305.2" y="246.0" font-size="9.5" fill="#10373E">Validation</text><text x="384.4" y="246.0" font-size="9.5" fill="#10373E">rules</text><text x="96.4" y="262.0" font-size="9.5" fill="#10373E">archive_rules.json</text><text x="96.4" y="278.0" font-size="9.5" fill="#10373E">museum_rules.json</text><text x="96.4" y="294.0" font-size="9.5" fill="#10373E">library_rules.json</text><text x="96.4" y="310.0" font-size="9.5" fill="#10373E">gallery_rules.json</text><text x="96.4" y="326.0" font-size="9.5" fill="#10373E">dam_rules.json</text><text x="67.6" y="342.0" font-size="9.5" fill="#10373E">mappings/</text><text x="96.4" y="358.0" font-size="9.5" fill="#10373E">defaults/</text><text x="125.2" y="374.0" font-size="9.5" fill="#10373E">information_object.json</text><text x="125.2" y="390.0" font-size="9.5" fill="#10373E">museum.json</text><text x="125.2" y="406.0" font-size="9.5" fill="#10373E">library.json</text><text x="283.6" y="406.0" font-size="9.5" fill="#10373E">#</text><text x="298.0" y="406.0" font-size="9.5" fill="#10373E">MARC/RDA</text><text x="362.8" y="406.0" font-size="9.5" fill="#10373E">fields</text><text x="125.2" y="422.0" font-size="9.5" fill="#10373E">gallery.json</text><text x="283.6" y="422.0" font-size="9.5" fill="#10373E">#</text><text x="298.0" y="422.0" font-size="9.5" fill="#10373E">CCO/VRA</text><text x="355.6" y="422.0" font-size="9.5" fill="#10373E">fields</text><text x="125.2" y="438.0" font-size="9.5" fill="#10373E">dam.json</text><text x="283.6" y="438.0" font-size="9.5" fill="#10373E">#</text><text x="298.0" y="438.0" font-size="9.5" fill="#10373E">Dublin</text><text x="348.4" y="438.0" font-size="9.5" fill="#10373E">Core/IPTC</text><text x="420.4" y="438.0" font-size="9.5" fill="#10373E">fields</text><text x="125.2" y="454.0" font-size="9.5" fill="#10373E">preservica_opex.json</text><text x="125.2" y="470.0" font-size="9.5" fill="#10373E">preservica_xip.json</text><text x="125.2" y="486.0" font-size="9.5" fill="#10373E">...</text><text x="38.8" y="502.0" font-size="9.5" fill="#10373E">docs/</text><text x="67.6" y="518.0" font-size="9.5" fill="#10373E">GEARMAN.md</text><text x="254.8" y="518.0" font-size="9.5" fill="#10373E">#</text><text x="269.2" y="518.0" font-size="9.5" fill="#10373E">Gearman</text><text x="326.8" y="518.0" font-size="9.5" fill="#10373E">setup</text><text x="370.0" y="518.0" font-size="9.5" fill="#10373E">documentation</text><text x="38.8" y="534.0" font-size="9.5" fill="#10373E">lib/</text><text x="67.6" y="550.0" font-size="9.5" fill="#10373E">Validation/</text><text x="254.8" y="550.0" font-size="9.5" fill="#10373E">#</text><text x="269.2" y="550.0" font-size="9.5" fill="#10373E">NEW:</text><text x="305.2" y="550.0" font-size="9.5" fill="#10373E">Validation</text><text x="384.4" y="550.0" font-size="9.5" fill="#10373E">framework</text><text x="96.4" y="566.0" font-size="9.5" fill="#10373E">AhgBaseValidator.class.php</text><text x="96.4" y="582.0" font-size="9.5" fill="#10373E">AhgValidatorCollection.class.php</text><text x="96.4" y="598.0" font-size="9.5" fill="#10373E">AhgValidationReport.class.php</text><text x="96.4" y="614.0" font-size="9.5" fill="#10373E">AhgSchemaValidator.class.php</text><text x="96.4" y="630.0" font-size="9.5" fill="#10373E">AhgReferentialValidator.class.php</text><text x="96.4" y="646.0" font-size="9.5" fill="#10373E">AhgDuplicateDetector.class.php</text><text x="96.4" y="662.0" font-size="9.5" fill="#10373E">Sectors/</text><text x="125.2" y="678.0" font-size="9.5" fill="#10373E">ArchivesValidator.class.php</text><text x="125.2" y="694.0" font-size="9.5" fill="#10373E">MuseumValidator.class.php</text><text x="125.2" y="710.0" font-size="9.5" fill="#10373E">LibraryValidator.class.php</text><text x="125.2" y="726.0" font-size="9.5" fill="#10373E">GalleryValidator.class.php</text><text x="125.2" y="742.0" font-size="9.5" fill="#10373E">DamValidator.class.php</text><text x="67.6" y="758.0" font-size="9.5" fill="#10373E">Services/</text><text x="96.4" y="774.0" font-size="9.5" fill="#10373E">MigrationService.php</text><text x="96.4" y="790.0" font-size="9.5" fill="#10373E">ValidationService.php</text><text x="269.2" y="790.0" font-size="9.5" fill="#10373E">#</text><text x="283.6" y="790.0" font-size="9.5" fill="#10373E">NEW:</text><text x="319.6" y="790.0" font-size="9.5" fill="#10373E">Validation</text><text x="398.8" y="790.0" font-size="9.5" fill="#10373E">orchestration</text><text x="96.4" y="806.0" font-size="9.5" fill="#10373E">PreservicaImportService.php</text><text x="96.4" y="822.0" font-size="9.5" fill="#10373E">PreservicaExportService.php</text><text x="96.4" y="838.0" font-size="9.5" fill="#10373E">PathTransformer.php</text><text x="96.4" y="854.0" font-size="9.5" fill="#10373E">RightsImportService.php</text><text x="67.6" y="870.0" font-size="9.5" fill="#10373E">Exporters/</text><text x="254.8" y="870.0" font-size="9.5" fill="#10373E">#</text><text x="269.2" y="870.0" font-size="9.5" fill="#10373E">Sector-specific</text><text x="384.4" y="870.0" font-size="9.5" fill="#10373E">CSV</text><text x="413.2" y="870.0" font-size="9.5" fill="#10373E">exporters</text><text x="96.4" y="886.0" font-size="9.5" fill="#10373E">BaseExporter.php</text><text x="96.4" y="902.0" font-size="9.5" fill="#10373E">ExporterFactory.php</text><text x="96.4" y="918.0" font-size="9.5" fill="#10373E">ArchivesExporter.php</text><text x="96.4" y="934.0" font-size="9.5" fill="#10373E">MuseumExporter.php</text><text x="96.4" y="950.0" font-size="9.5" fill="#10373E">LibraryExporter.php</text><text x="96.4" y="966.0" font-size="9.5" fill="#10373E">GalleryExporter.php</text><text x="96.4" y="982.0" font-size="9.5" fill="#10373E">DamExporter.php</text><text x="67.6" y="998.0" font-size="9.5" fill="#10373E">Mappings/</text><text x="96.4" y="1014.0" font-size="9.5" fill="#10373E">PreservicaMapping.php</text><text x="67.6" y="1030.0" font-size="9.5" fill="#10373E">Parsers/</text><text x="96.4" y="1046.0" font-size="9.5" fill="#10373E">CsvParser.php</text><text x="96.4" y="1062.0" font-size="9.5" fill="#10373E">ExcelParser.php</text><text x="96.4" y="1078.0" font-size="9.5" fill="#10373E">OpexParser.php</text><text x="96.4" y="1094.0" font-size="9.5" fill="#10373E">PaxParser.php</text><text x="96.4" y="1110.0" font-size="9.5" fill="#10373E">ParserFactory.php</text><text x="67.6" y="1126.0" font-size="9.5" fill="#10373E">Sectors/</text><text x="96.4" y="1142.0" font-size="9.5" fill="#10373E">SectorFactory.php</text><text x="96.4" y="1158.0" font-size="9.5" fill="#10373E">ArchivesSector.php</text><text x="96.4" y="1174.0" font-size="9.5" fill="#10373E">MuseumSector.php</text><text x="96.4" y="1190.0" font-size="9.5" fill="#10373E">LibrarySector.php</text><text x="96.4" y="1206.0" font-size="9.5" fill="#10373E">GallerySector.php</text><text x="96.4" y="1222.0" font-size="9.5" fill="#10373E">DamSector.php</text><text x="67.6" y="1238.0" font-size="9.5" fill="#10373E">SourceDetector.php</text><text x="67.6" y="1254.0" font-size="9.5" fill="#10373E">task/</text><text x="96.4" y="1270.0" font-size="9.5" fill="#10373E">migrationImportTask.class.php</text><text x="96.4" y="1286.0" font-size="9.5" fill="#10373E">sectorImportTask.class.php</text><text x="348.4" y="1286.0" font-size="9.5" fill="#10373E">#</text><text x="362.8" y="1286.0" font-size="9.5" fill="#10373E">NEW:</text><text x="398.8" y="1286.0" font-size="9.5" fill="#10373E">Base</text><text x="434.8" y="1286.0" font-size="9.5" fill="#10373E">sector</text><text x="485.2" y="1286.0" font-size="9.5" fill="#10373E">import</text><text x="96.4" y="1302.0" font-size="9.5" fill="#10373E">archivesCsvImportTask.class.php</text><text x="348.4" y="1302.0" font-size="9.5" fill="#10373E">#</text><text x="362.8" y="1302.0" font-size="9.5" fill="#10373E">NEW:</text><text x="398.8" y="1302.0" font-size="9.5" fill="#10373E">ISAD-G</text><text x="449.2" y="1302.0" font-size="9.5" fill="#10373E">import</text><text x="96.4" y="1318.0" font-size="9.5" fill="#10373E">museumCsvImportTask.class.php</text><text x="348.4" y="1318.0" font-size="9.5" fill="#10373E">#</text><text x="362.8" y="1318.0" font-size="9.5" fill="#10373E">NEW:</text><text x="398.8" y="1318.0" font-size="9.5" fill="#10373E">Spectrum</text><text x="463.6" y="1318.0" font-size="9.5" fill="#10373E">import</text><text x="96.4" y="1334.0" font-size="9.5" fill="#10373E">libraryCsvImportTask.class.php</text><text x="348.4" y="1334.0" font-size="9.5" fill="#10373E">#</text><text x="362.8" y="1334.0" font-size="9.5" fill="#10373E">NEW:</text><text x="398.8" y="1334.0" font-size="9.5" fill="#10373E">MARC/RDA</text><text x="463.6" y="1334.0" font-size="9.5" fill="#10373E">import</text><text x="96.4" y="1350.0" font-size="9.5" fill="#10373E">galleryCsvImportTask.class.php</text><text x="348.4" y="1350.0" font-size="9.5" fill="#10373E">#</text><text x="362.8" y="1350.0" font-size="9.5" fill="#10373E">NEW:</text><text x="398.8" y="1350.0" font-size="9.5" fill="#10373E">CCO</text><text x="427.6" y="1350.0" font-size="9.5" fill="#10373E">import</text><text x="96.4" y="1366.0" font-size="9.5" fill="#10373E">damCsvImportTask.class.php</text><text x="348.4" y="1366.0" font-size="9.5" fill="#10373E">#</text><text x="362.8" y="1366.0" font-size="9.5" fill="#10373E">NEW:</text><text x="398.8" y="1366.0" font-size="9.5" fill="#10373E">Dublin</text><text x="449.2" y="1366.0" font-size="9.5" fill="#10373E">Core</text><text x="485.2" y="1366.0" font-size="9.5" fill="#10373E">import</text><text x="96.4" y="1382.0" font-size="9.5" fill="#10373E">preservicaImportTask.class.php</text><text x="96.4" y="1398.0" font-size="9.5" fill="#10373E">preservicaExportTask.class.php</text><text x="96.4" y="1414.0" font-size="9.5" fill="#10373E">preservicaInfoTask.class.php</text><text x="38.8" y="1430.0" font-size="9.5" fill="#10373E">modules/</text><text x="67.6" y="1446.0" font-size="9.5" fill="#10373E">dataMigration/</text><text x="96.4" y="1462.0" font-size="9.5" fill="#10373E">actions/</text><text x="125.2" y="1478.0" font-size="9.5" fill="#10373E">indexAction.class.php</text><text x="125.2" y="1494.0" font-size="9.5" fill="#10373E">uploadAction.class.php</text><text x="125.2" y="1510.0" font-size="9.5" fill="#10373E">mapAction.class.php</text><text x="125.2" y="1526.0" font-size="9.5" fill="#10373E">previewAction.class.php</text><text x="125.2" y="1542.0" font-size="9.5" fill="#10373E">executeAction.class.php</text><text x="125.2" y="1558.0" font-size="9.5" fill="#10373E">validateAction.class.php</text><text x="348.4" y="1558.0" font-size="9.5" fill="#10373E">#</text><text x="362.8" y="1558.0" font-size="9.5" fill="#10373E">NEW:</text><text x="398.8" y="1558.0" font-size="9.5" fill="#10373E">Validation-only</text><text x="125.2" y="1574.0" font-size="9.5" fill="#10373E">previewValidationAction.class.php</text><text x="370.0" y="1574.0" font-size="9.5" fill="#10373E">#</text><text x="384.4" y="1574.0" font-size="9.5" fill="#10373E">NEW:</text><text x="420.4" y="1574.0" font-size="9.5" fill="#10373E">AJAX</text><text x="456.4" y="1574.0" font-size="9.5" fill="#10373E">validation</text><text x="125.2" y="1590.0" font-size="9.5" fill="#10373E">exportMappingAction.class.php</text><text x="348.4" y="1590.0" font-size="9.5" fill="#10373E">#</text><text x="362.8" y="1590.0" font-size="9.5" fill="#10373E">NEW:</text><text x="398.8" y="1590.0" font-size="9.5" fill="#10373E">Profile</text><text x="456.4" y="1590.0" font-size="9.5" fill="#10373E">export</text><text x="125.2" y="1606.0" font-size="9.5" fill="#10373E">importMappingAction.class.php</text><text x="348.4" y="1606.0" font-size="9.5" fill="#10373E">#</text><text x="362.8" y="1606.0" font-size="9.5" fill="#10373E">NEW:</text><text x="398.8" y="1606.0" font-size="9.5" fill="#10373E">Profile</text><text x="456.4" y="1606.0" font-size="9.5" fill="#10373E">import</text><text x="125.2" y="1622.0" font-size="9.5" fill="#10373E">sectorExportAction.class.php</text><text x="348.4" y="1622.0" font-size="9.5" fill="#10373E">#</text><text x="362.8" y="1622.0" font-size="9.5" fill="#10373E">NEW:</text><text x="398.8" y="1622.0" font-size="9.5" fill="#10373E">DB</text><text x="420.4" y="1622.0" font-size="9.5" fill="#10373E">export</text><text x="125.2" y="1638.0" font-size="9.5" fill="#10373E">batchExportAction.class.php</text><text x="348.4" y="1638.0" font-size="9.5" fill="#10373E">#</text><text x="362.8" y="1638.0" font-size="9.5" fill="#10373E">Batch</text><text x="406.0" y="1638.0" font-size="9.5" fill="#10373E">export</text><text x="456.4" y="1638.0" font-size="9.5" fill="#10373E">UI</text><text x="125.2" y="1654.0" font-size="9.5" fill="#10373E">exportCsvAction.class.php</text><text x="125.2" y="1670.0" font-size="9.5" fill="#10373E">jobsAction.class.php</text><text x="125.2" y="1686.0" font-size="9.5" fill="#10373E">...</text><text x="96.4" y="1702.0" font-size="9.5" fill="#10373E">templates/</text><text x="125.2" y="1718.0" font-size="9.5" fill="#10373E">indexSuccess.php</text><text x="125.2" y="1734.0" font-size="9.5" fill="#10373E">mapSuccess.php</text><text x="125.2" y="1750.0" font-size="9.5" fill="#10373E">previewSuccess.php</text><text x="125.2" y="1766.0" font-size="9.5" fill="#10373E">validateSuccess.php</text><text x="348.4" y="1766.0" font-size="9.5" fill="#10373E">#</text><text x="362.8" y="1766.0" font-size="9.5" fill="#10373E">NEW:</text><text x="398.8" y="1766.0" font-size="9.5" fill="#10373E">Validation</text><text x="478.0" y="1766.0" font-size="9.5" fill="#10373E">UI</text><text x="125.2" y="1782.0" font-size="9.5" fill="#10373E">batchExportSuccess.php</text><text x="125.2" y="1798.0" font-size="9.5" fill="#10373E">jobsSuccess.php</text><text x="38.8" y="1814.0" font-size="9.5" fill="#10373E">css/</text><text x="67.6" y="1830.0" font-size="9.5" fill="#10373E">data-migration.css</text></svg></div>

---

## 3. Database Schema

### atom_data_mapping

Stores field mapping configurations.
```sql
CREATE TABLE IF NOT EXISTS atom_data_mapping (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    source_type VARCHAR(100),
    target_type VARCHAR(50),
    field_mappings JSON,
    transformations JSON,
    default_values JSON,
    is_system TINYINT(1) DEFAULT 0,
    created_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES user(id) ON DELETE SET NULL
);
```

**Field Descriptions:**
- `source_type` - Source system identifier (archivesspace, vernon, preservica_opex)
- `target_type` - Target sector (ARCHIVES, MUSEUM, LIBRARY, GALLERY, DAM)
- `field_mappings` - JSON object `{"source_field": "target_field"}`
- `transformations` - JSON object `{"field": "transform_type"}`
- `default_values` - JSON object `{"field": "default_value"}`

### atom_data_migration_job

Tracks background import jobs.
```sql
CREATE TABLE IF NOT EXISTS atom_data_migration_job (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mapping_id INT,
    file_path VARCHAR(500),
    file_name VARCHAR(255),
    total_records INT DEFAULT 0,
    processed_records INT DEFAULT 0,
    created_records INT DEFAULT 0,
    updated_records INT DEFAULT 0,
    skipped_records INT DEFAULT 0,
    error_count INT DEFAULT 0,
    status ENUM('queued','running','completed','failed','cancelled') DEFAULT 'queued',
    error_log JSON,
    options JSON,
    started_at TIMESTAMP NULL,
    completed_at TIMESTAMP NULL,
    created_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (mapping_id) REFERENCES atom_data_mapping(id) ON DELETE SET NULL,
    FOREIGN KEY (created_by) REFERENCES user(id) ON DELETE SET NULL
);
```

### atom_data_migration_log

Audit log for individual record imports.
```sql
CREATE TABLE IF NOT EXISTS atom_data_migration_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    job_id INT,
    record_id INT,
    legacy_id VARCHAR(255),
    action ENUM('create','update','skip','error'),
    details JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (job_id) REFERENCES atom_data_migration_job(id) ON DELETE CASCADE
);
```

### atom_validation_rule (NEW in 1.4.0)

Stores configurable validation rules per sector.
```sql
CREATE TABLE IF NOT EXISTS atom_validation_rule (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    sector_code VARCHAR(50) NOT NULL,
    rule_type ENUM('required', 'type', 'pattern', 'enum', 'range', 'length', 'referential', 'custom') NOT NULL,
    field_name VARCHAR(255) NOT NULL,
    rule_config JSON NOT NULL,
    error_message VARCHAR(500),
    severity ENUM('error', 'warning', 'info') DEFAULT 'error',
    is_active TINYINT(1) DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_sector (sector_code),
    INDEX idx_field (field_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

**Rule Types:**
- `required` - Field must not be empty
- `type` - Data type validation (string, integer, float, date, boolean)
- `pattern` - Regex pattern matching
- `enum` - Value must be in allowed list
- `range` - Numeric range validation
- `length` - String length validation
- `referential` - Parent/child relationship validation
- `custom` - Custom PHP validation callback

### atom_validation_log (NEW in 1.4.0)

Logs validation errors per job.
```sql
CREATE TABLE IF NOT EXISTS atom_validation_log (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    job_id BIGINT UNSIGNED,
    row_number INT,
    column_name VARCHAR(255),
    rule_type VARCHAR(50),
    severity ENUM('error', 'warning', 'info'),
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_job (job_id),
    INDEX idx_row (row_number),
    FOREIGN KEY (job_id) REFERENCES atom_data_migration_job(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

---

## 4. Core Components

### SourceDetector.php

Auto-detects source system from file content.
```php
class SourceDetector
{
    public function detect(string $filePath): array
    {
        $extension = pathinfo($filePath, PATHINFO_EXTENSION);
        
        return match($extension) {
            'opex' => ['format' => 'opex', 'source' => 'preservica_opex'],
            'pax', 'zip' => $this->detectPaxOrZip($filePath),
            'csv' => $this->detectCsvSource($filePath),
            'xlsx', 'xls' => $this->detectExcelSource($filePath),
            'xml' => $this->detectXmlSource($filePath),
            default => ['format' => 'unknown', 'source' => 'unknown']
        };
    }
    
    protected function detectCsvSource(string $filePath): array
    {
        $headers = $this->getCsvHeaders($filePath);
        
        // ArchivesSpace detection
        if (in_array('ead_id', $headers) || in_array('resource_type', $headers)) {
            return ['format' => 'csv', 'source' => 'archivesspace'];
        }
        
        // Vernon CMS detection
        if (in_array('object_number', $headers) || in_array('accession_number', $headers)) {
            return ['format' => 'csv', 'source' => 'vernon'];
        }
        
        // Generic CSV
        return ['format' => 'csv', 'source' => 'generic'];
    }
}
```

### MigrationService.php

Main orchestration service for imports.
```php
namespace ahgDataMigrationPlugin\Services;

use Illuminate\Database\Capsule\Manager as DB;

class MigrationService
{
    protected $mapping;
    protected $parser;
    protected $sector;
    protected $options = [];
    protected $stats = [
        'total' => 0,
        'created' => 0,
        'updated' => 0,
        'skipped' => 0,
        'errors' => 0
    ];

    public function import(string $filePath, int $mappingId, array $options = []): array
    {
        $this->loadMapping($mappingId);
        $this->initParser($filePath);
        $this->initSector();
        $this->options = $options;
        
        $records = $this->parser->parse($filePath);
        $this->stats['total'] = count($records);
        
        // Build hierarchy map for parent resolution
        $hierarchyMap = $this->buildHierarchyMap($records);
        
        foreach ($records as $record) {
            try {
                $this->processRecord($record, $hierarchyMap);
            } catch (\Exception $e) {
                $this->logError($record, $e->getMessage());
            }
        }
        
        return $this->stats;
    }

    protected function processRecord(array $data, array $hierarchyMap): void
    {
        // Apply field mappings
        $mapped = $this->applyMappings($data);
        
        // Apply transformations
        $transformed = $this->applyTransformations($mapped);
        
        // Apply defaults
        $final = $this->applyDefaults($transformed);
        
        // Resolve parent ID
        if (!empty($final['parentId'])) {
            $final['parent_id'] = $hierarchyMap[$final['parentId']] ?? null;
        }
        
        // Create or update record
        $this->saveRecord($final);
    }

    protected function saveRecord(array $data): int
    {
        // Check for existing record (update mode)
        if ($this->options['update'] ?? false) {
            $existing = $this->findExisting($data);
            if ($existing) {
                return $this->updateRecord($existing, $data);
            }
        }
        
        // Create new information_object
        $objectId = DB::table('object')->insertGetId([
            'class_name' => 'QubitInformationObject',
            'created_at' => now(),
            'updated_at' => now(),
        ]);
        
        // Insert information_object
        DB::table('information_object')->insert([
            'id' => $objectId,
            'identifier' => $data['identifier'] ?? null,
            'level_of_description_id' => $this->resolveLevelId($data['levelOfDescription']),
            'repository_id' => $data['repository_id'] ?? $this->options['repository'] ?? null,
            'parent_id' => $data['parent_id'] ?? QubitInformationObject::ROOT_ID,
            'source_culture' => $data['culture'] ?? 'en',
        ]);
        
        // Insert i18n data
        DB::table('information_object_i18n')->insert([
            'id' => $objectId,
            'culture' => $data['culture'] ?? 'en',
            'title' => $data['title'],
            'scope_and_content' => $data['scopeAndContent'] ?? null,
            // ... other i18n fields
        ]);
        
        // Generate slug
        $this->generateSlug($objectId, $data['title']);
        
        // Calculate nested set (lft/rgt)
        $this->updateNestedSet($objectId, $data['parent_id'] ?? QubitInformationObject::ROOT_ID);
        
        // Set publication status
        $this->setPublicationStatus($objectId);
        
        $this->stats['created']++;
        return $objectId;
    }
}
```

---

## 5. Validation Framework

The validation framework (new in 1.4.0) provides comprehensive data quality checks before import.

### AhgValidationReport.class.php

Tracks errors by row and column with severity levels.
```php
class AhgValidationReport
{
    const SEVERITY_ERROR = 'error';
    const SEVERITY_WARNING = 'warning';
    const SEVERITY_INFO = 'info';

    protected array $errors = [];      // [row => [column => [errors]]]
    protected array $summary = [];     // Counts by severity
    protected int $totalRows = 0;

    public function addError(int $row, string $column, string $message, string $severity = 'error'): void
    {
        $this->errors[$row][$column][] = [
            'message' => $message,
            'severity' => $severity
        ];
        $this->summary[$severity] = ($this->summary[$severity] ?? 0) + 1;
    }

    public function hasErrors(): bool
    {
        return ($this->summary['error'] ?? 0) > 0;
    }

    public function getRowErrors(int $row): array
    {
        return $this->errors[$row] ?? [];
    }

    public function toArray(): array
    {
        return [
            'total_rows' => $this->totalRows,
            'error_count' => $this->summary['error'] ?? 0,
            'warning_count' => $this->summary['warning'] ?? 0,
            'info_count' => $this->summary['info'] ?? 0,
            'errors' => $this->errors
        ];
    }
}
```

### AhgSchemaValidator.class.php

Validates required fields, data types, patterns, and max lengths.
```php
class AhgSchemaValidator extends AhgBaseValidator
{
    protected array $rules = [];

    public function loadRulesFromJson(string $path): void
    {
        $json = file_get_contents($path);
        $config = json_decode($json, true);
        $this->rules = $config['rules'] ?? [];
    }

    public function validate(array $row, int $rowNumber): void
    {
        // Required fields
        foreach ($this->rules['required'] ?? [] as $field) {
            if (empty($row[$field])) {
                $this->report->addError($rowNumber, $field, "Required field is empty");
            }
        }

        // Data types
        foreach ($this->rules['types'] ?? [] as $field => $type) {
            if (!empty($row[$field]) && !$this->validateType($row[$field], $type)) {
                $this->report->addError($rowNumber, $field, "Invalid type: expected $type");
            }
        }

        // Patterns (regex)
        foreach ($this->rules['patterns'] ?? [] as $field => $pattern) {
            if (!empty($row[$field]) && !preg_match("/$pattern/", $row[$field])) {
                $this->report->addError($rowNumber, $field, "Value does not match pattern");
            }
        }

        // Max lengths
        foreach ($this->rules['maxLengths'] ?? [] as $field => $maxLen) {
            if (!empty($row[$field]) && strlen($row[$field]) > $maxLen) {
                $this->report->addError($rowNumber, $field, "Exceeds max length of $maxLen");
            }
        }

        // Enums (allowed values)
        foreach ($this->rules['enums'] ?? [] as $field => $allowed) {
            if (!empty($row[$field]) && !in_array($row[$field], $allowed)) {
                $this->report->addError($rowNumber, $field,
                    "Invalid value: must be one of " . implode(', ', $allowed));
            }
        }
    }
}
```

### AhgReferentialValidator.class.php

Validates parent-child relationships and detects circular references.
```php
class AhgReferentialValidator extends AhgBaseValidator
{
    protected array $idIndex = [];     // legacyId => row number
    protected array $parentIndex = []; // legacyId => parentId
    protected array $existingIds = []; // IDs from database

    public function buildIndex(array $rows): void
    {
        foreach ($rows as $rowNum => $row) {
            $legacyId = $row['legacyId'] ?? $row['identifier'] ?? null;
            if ($legacyId) {
                $this->idIndex[$legacyId] = $rowNum;
                $this->parentIndex[$legacyId] = $row['parentId'] ?? null;
            }
        }
    }

    public function validate(array $row, int $rowNumber): void
    {
        $parentId = $row['parentId'] ?? null;
        $legacyId = $row['legacyId'] ?? $row['identifier'] ?? null;

        if (empty($parentId)) {
            return; // Root record, no parent to validate
        }

        // Check parent exists in file or database
        if (!isset($this->idIndex[$parentId]) && !$this->existsInDatabase($parentId)) {
            $this->report->addError($rowNumber, 'parentId',
                "Parent '$parentId' not found in file or database");
        }

        // Check for circular reference
        if ($this->detectCycle($legacyId)) {
            $this->report->addError($rowNumber, 'parentId',
                "Circular reference detected in hierarchy");
        }
    }

    protected function detectCycle(string $id): bool
    {
        $visited = [];
        $current = $id;

        while ($current && isset($this->parentIndex[$current])) {
            if (isset($visited[$current])) {
                return true; // Cycle detected
            }
            $visited[$current] = true;
            $current = $this->parentIndex[$current];
        }

        return false;
    }
}
```

### AhgDuplicateDetector.class.php

Configurable duplicate detection with multiple strategies.
```php
class AhgDuplicateDetector extends AhgBaseValidator
{
    const STRATEGY_IDENTIFIER = 'identifier';
    const STRATEGY_LEGACY_ID = 'legacyId';
    const STRATEGY_TITLE_DATE = 'title_date';
    const STRATEGY_COMPOSITE = 'composite';

    protected string $strategy = self::STRATEGY_IDENTIFIER;
    protected array $compositeFields = [];
    protected array $seenValues = [];

    public function setStrategy(string $strategy, array $fields = []): void
    {
        $this->strategy = $strategy;
        $this->compositeFields = $fields;
    }

    public function validate(array $row, int $rowNumber): void
    {
        $key = $this->buildKey($row);

        if (isset($this->seenValues[$key])) {
            $firstRow = $this->seenValues[$key];
            $this->report->addError($rowNumber, $this->getKeyField(),
                "Duplicate of row $firstRow", self::SEVERITY_WARNING);
        } else {
            $this->seenValues[$key] = $rowNumber;
        }

        // Check against database
        if ($this->checkDatabase && $this->existsInDatabase($key)) {
            $this->report->addError($rowNumber, $this->getKeyField(),
                "Record already exists in database", self::SEVERITY_WARNING);
        }
    }

    protected function buildKey(array $row): string
    {
        return match($this->strategy) {
            self::STRATEGY_IDENTIFIER => $row['identifier'] ?? '',
            self::STRATEGY_LEGACY_ID => $row['legacyId'] ?? '',
            self::STRATEGY_TITLE_DATE => ($row['title'] ?? '') . '|' . ($row['dateRange'] ?? ''),
            self::STRATEGY_COMPOSITE => implode('|', array_map(
                fn($f) => $row[$f] ?? '',
                $this->compositeFields
            )),
        };
    }
}
```

### Sector-Specific Validators

Each sector has specialized validation rules:

| Validator | Sector | Key Validations |
|-----------|--------|-----------------|
| `ArchivesValidator` | ISAD-G | Level hierarchy, fonds→series→file→item flow |
| `MuseumValidator` | Collections Procedures | Object number format, acquisition date |
| `LibraryValidator` | MARC/RDA | ISBN-10/13 checksum, ISSN format |
| `GalleryValidator` | CCO | Work type vocabulary, creator format |
| `DamValidator` | Dublin Core | DC type, MIME type, GPS coordinates |

#### LibraryValidator ISBN Validation
```php
protected function validateIsbn(string $isbn, int $row): void
{
    $clean = preg_replace('/[^0-9X]/', '', strtoupper($isbn));

    if (strlen($clean) === 10) {
        // ISBN-10 checksum
        $sum = 0;
        for ($i = 0; $i < 9; $i++) {
            $sum += (int)$clean[$i] * (10 - $i);
        }
        $check = (11 - ($sum % 11)) % 11;
        $expected = $check === 10 ? 'X' : (string)$check;

        if ($clean[9] !== $expected) {
            $this->report->addError($row, 'isbn', "Invalid ISBN-10 checksum");
        }
    } elseif (strlen($clean) === 13) {
        // ISBN-13 checksum
        $sum = 0;
        for ($i = 0; $i < 12; $i++) {
            $sum += (int)$clean[$i] * ($i % 2 === 0 ? 1 : 3);
        }
        $check = (10 - ($sum % 10)) % 10;

        if ((int)$clean[12] !== $check) {
            $this->report->addError($row, 'isbn', "Invalid ISBN-13 checksum");
        }
    } else {
        $this->report->addError($row, 'isbn', "ISBN must be 10 or 13 digits");
    }
}
```

### ValidationService.php

Orchestrates all validators.
```php
namespace ahgDataMigrationPlugin\Services;

class ValidationService
{
    protected AhgValidatorCollection $validators;
    protected string $sectorCode;

    public function validate(string $filepath, array $mapping = [], array $rows = []): AhgValidationReport
    {
        $report = new AhgValidationReport();

        // Parse file if rows not provided
        if (empty($rows)) {
            $parser = ParserFactory::create($this->detectFormat($filepath));
            $rows = $parser->parse($filepath);
        }

        $report->setTotalRows(count($rows));

        // Initialize validators
        $this->validators = new AhgValidatorCollection($report);
        $this->validators->add(new AhgSchemaValidator($report, $this->sectorCode));
        $this->validators->add(new AhgReferentialValidator($report));
        $this->validators->add(new AhgDuplicateDetector($report));
        $this->validators->add($this->getSectorValidator($report));

        // Build index for referential validation
        $this->validators->buildIndex($rows);

        // Validate each row
        foreach ($rows as $rowNum => $row) {
            $mapped = $this->applyMapping($row, $mapping);
            $this->validators->validateRow($mapped, $rowNum + 1);
        }

        return $report;
    }

    public function validateOnly(string $filepath, array $mapping = []): AhgValidationReport
    {
        return $this->validate($filepath, $mapping);
    }

    protected function getSectorValidator(AhgValidationReport $report): AhgBaseValidator
    {
        return match($this->sectorCode) {
            'archive', 'archives' => new ArchivesValidator($report),
            'museum', 'spectrum' => new MuseumValidator($report),
            'library', 'marc' => new LibraryValidator($report),
            'gallery', 'cco' => new GalleryValidator($report),
            'dam', 'dc' => new DamValidator($report),
            default => new AhgBaseValidator($report),
        };
    }
}
```

### Validation Rules JSON Format

Located in `data/validation/{sector}_rules.json`:
```json
{
    "sector": "archive",
    "rules": {
        "required": ["identifier", "title", "levelOfDescription"],
        "types": {
            "legacyId": "string",
            "dateRange": "string"
        },
        "patterns": {
            "identifier": "^[A-Za-z0-9/-]+$"
        },
        "maxLengths": {
            "title": 1024,
            "identifier": 255
        },
        "enums": {
            "levelOfDescription": ["fonds", "collection", "series", "subseries", "file", "item"]
        },
        "referential": {
            "parentId": "legacyId"
        }
    }
}
```

### New Routes

```yaml
# config/routing.yml

dataMigration_validate:
  url: /dataMigration/validate
  param: { module: dataMigration, action: validate }

dataMigration_previewValidation:
  url: /dataMigration/previewValidation
  param: { module: dataMigration, action: previewValidation }

dataMigration_exportMapping:
  url: /dataMigration/exportMapping/:id
  param: { module: dataMigration, action: exportMapping }

dataMigration_importMapping:
  url: /dataMigration/importMapping
  param: { module: dataMigration, action: importMapping }

dataMigration_sectorExport:
  url: /dataMigration/export/:sector
  param: { module: dataMigration, action: sectorExport }
```

---

## 6. Parsers

### ParserFactory.php
```php
class ParserFactory
{
    public static function create(string $format): ParserInterface
    {
        return match($format) {
            'csv' => new CsvParser(),
            'xlsx', 'xls' => new ExcelParser(),
            'opex' => new OpexParser(),
            'pax', 'xip' => new PaxParser(),
            default => throw new \InvalidArgumentException("Unknown format: $format")
        };
    }
}
```

### OpexParser.php

Parses Preservica OPEX XML format with full rights extraction.
```php
class OpexParser implements ParserInterface
{
    protected $namespaces = [
        'opex' => 'http://www.openpreservationexchange.org/opex/v1.2',
        'dc' => 'http://purl.org/dc/elements/1.1/',
        'dcterms' => 'http://purl.org/dc/terms/',
        'mods' => 'http://www.loc.gov/mods/v3',
        'ead' => 'urn:isbn:1-931666-22-9',
    ];

    public function parse(string $filePath): array
    {
        $xml = simplexml_load_file($filePath);
        foreach ($this->namespaces as $prefix => $uri) {
            $xml->registerXPathNamespace($prefix, $uri);
        }
        
        $records = [];
        
        // Parse folders
        foreach ($xml->xpath('//opex:Folder') as $folder) {
            $records[] = $this->parseFolder($folder);
        }
        
        // Parse assets
        foreach ($xml->xpath('//opex:Asset') as $asset) {
            $records[] = $this->parseAsset($asset);
        }
        
        return $records;
    }

    protected function parseFolder(\SimpleXMLElement $folder): array
    {
        $record = [
            'legacyId' => (string)$folder['id'],
            'title' => (string)$folder->Title,
            'levelOfDescription' => 'Series',
        ];
        
        // Extract Dublin Core
        $this->extractDublinCore($folder, $record);
        
        // Extract rights
        $record['rights'] = $this->extractRights($folder);
        
        // Extract provenance/history
        $record['provenance'] = $this->extractProvenance($folder);
        
        return $record;
    }

    protected function extractRights(\SimpleXMLElement $element): array
    {
        $rights = [];
        
        // SecurityDescriptor
        $security = $element->xpath('.//opex:SecurityDescriptor');
        if (!empty($security)) {
            $rights[] = [
                'type' => 'access',
                'basis' => 'policy',
                'value' => (string)$security[0],
            ];
        }
        
        // dc:rights
        $dcRights = $element->xpath('.//dc:rights');
        foreach ($dcRights as $r) {
            $rights[] = [
                'type' => 'copyright',
                'basis' => 'copyright',
                'value' => (string)$r,
            ];
        }
        
        // dcterms:license
        $license = $element->xpath('.//dcterms:license');
        foreach ($license as $l) {
            $rights[] = [
                'type' => 'license',
                'basis' => 'license',
                'value' => (string)$l,
            ];
        }
        
        // MODS accessCondition
        $mods = $element->xpath('.//mods:accessCondition');
        foreach ($mods as $m) {
            $rights[] = [
                'type' => (string)$m['type'] ?: 'access',
                'basis' => 'statute',
                'value' => (string)$m,
            ];
        }
        
        // EAD userestrict/accessrestrict
        foreach (['userestrict', 'accessrestrict'] as $tag) {
            $ead = $element->xpath(".//ead:$tag");
            foreach ($ead as $e) {
                $rights[] = [
                    'type' => $tag === 'userestrict' ? 'use' : 'access',
                    'basis' => 'policy',
                    'value' => (string)$e->p,
                ];
            }
        }
        
        return $rights;
    }

    protected function extractProvenance(\SimpleXMLElement $element): array
    {
        $provenance = [];
        
        $history = $element->xpath('.//opex:History/opex:Event');
        foreach ($history as $event) {
            $provenance[] = [
                'date' => (string)$event->Date,
                'type' => (string)$event->Type,
                'agent' => (string)$event->Agent,
                'description' => (string)$event->Description,
            ];
        }
        
        return $provenance;
    }
}
```

---

## 7. Exporters

The plugin includes sector-specific CSV exporters for both transformation (during import) and batch export of existing AtoM records.

### ExporterFactory.php

Creates the appropriate exporter based on sector code.
```php
namespace ahgDataMigrationPlugin\Exporters;

class ExporterFactory
{
    private static array $exporters = [
        'archive' => ArchivesExporter::class,
        'archives' => ArchivesExporter::class,
        'museum' => MuseumExporter::class,
        'spectrum' => MuseumExporter::class,
        'library' => LibraryExporter::class,
        'marc' => LibraryExporter::class,
        'gallery' => GalleryExporter::class,
        'cco' => GalleryExporter::class,
        'dam' => DamExporter::class,
        'dc' => DamExporter::class,
    ];

    public static function create(string $sector): BaseExporter
    {
        $sector = strtolower(trim($sector));
        if (!isset(self::$exporters[$sector])) {
            throw new \InvalidArgumentException("Unknown sector: $sector");
        }
        return new (self::$exporters[$sector])();
    }

    public static function getAvailableSectors(): array
    {
        return ['archives', 'museum', 'library', 'gallery', 'dam'];
    }
}
```

### BaseExporter.php

Abstract base class for all exporters.
```php
abstract class BaseExporter
{
    protected array $data = [];

    abstract public function getSectorCode(): string;
    abstract public function getColumns(): array;
    abstract public function mapRecord(array $record): array;

    public function setData(array $data): self
    {
        $this->data = $data;
        return $this;
    }

    public function export(): string
    {
        $columns = $this->getColumns();
        $output = fopen('php://temp', 'r+');
        fputcsv($output, $columns);

        foreach ($this->data as $record) {
            $mapped = $this->mapRecord($record);
            $row = [];
            foreach ($columns as $col) {
                $row[] = $mapped[$col] ?? '';
            }
            fputcsv($output, $row);
        }

        rewind($output);
        return stream_get_contents($output);
    }

    public function getFilename(string $baseName): string
    {
        return pathinfo($baseName, PATHINFO_FILENAME) . '_' . $this->getSectorCode() . '_import.csv';
    }
}
```

### Sector Exporters

| Exporter | Columns | Standard |
|----------|---------|----------|
| `ArchivesExporter` | 45 | ISAD(G) |
| `MuseumExporter` | 38 | Collections Procedures |
| `LibraryExporter` | 32 | MARC/RDA |
| `GalleryExporter` | 35 | CCO/VRA |
| `DamExporter` | 52 | Dublin Core/IPTC |

### Default Mapping Files

Located in `data/mappings/defaults/`:

| File | Description |
|------|-------------|
| `library.json` | Maps MARC/RDA fields (ISBN, call number, publisher, etc.) |
| `gallery.json` | Maps CCO/VRA fields (creator, provenance, exhibition history, etc.) |
| `dam.json` | Maps Dublin Core/IPTC fields (camera metadata, GPS, keywords, etc.) |
| `museum.json` | Maps Collections Procedures fields |
| `information_object.json` | Generic ISAD(G) mapping |

### Database Export (NEW in 1.4.0)

The `exportFromDatabase()` method allows exporting directly from AtoM database:
```php
abstract class BaseExporter
{
    // ... existing methods

    /**
     * Export records from database
     * @param array $objectIds Array of information_object IDs to export
     * @return string CSV content
     */
    public function exportFromDatabase(array $objectIds): string
    {
        $columns = $this->getColumns();
        $output = fopen('php://temp', 'r+');
        fputcsv($output, $columns);

        foreach ($objectIds as $id) {
            $record = $this->loadRecordFromDatabase($id);
            if ($record) {
                $mapped = $this->mapRecord($record);
                $row = [];
                foreach ($columns as $col) {
                    $row[] = $mapped[$col] ?? '';
                }
                fputcsv($output, $row);
            }
        }

        rewind($output);
        return stream_get_contents($output);
    }

    /**
     * Load a single record from database
     */
    protected function loadRecordFromDatabase(int $id): ?array
    {
        $record = DB::table('information_object as io')
            ->join('information_object_i18n as ioi', 'io.id', '=', 'ioi.id')
            ->leftJoin('slug', 'io.id', '=', 'slug.object_id')
            ->leftJoin('term_i18n as ti', 'io.level_of_description_id', '=', 'ti.id')
            ->leftJoin('repository_i18n as ri', 'io.repository_id', '=', 'ri.id')
            ->where('io.id', $id)
            ->where('ioi.culture', 'en')
            ->first();

        if (!$record) {
            return null;
        }

        return (array)$record;
    }
}
```

### Batch Export Action

The `batchExportAction` allows exporting existing AtoM records:

```php
class dataMigrationBatchExportAction extends sfAction
{
    public function execute($request)
    {
        // Filter options
        $sector = $request->getParameter('sector', 'archives');
        $repositoryId = $request->getParameter('repository_id');
        $levelIds = $request->getParameter('level_ids', []);
        $parentSlug = $request->getParameter('parent_slug', '');
        $includeDescendants = $request->getParameter('include_descendants', false);

        // Build query with filters
        $query = $DB::table('information_object')
            ->join('information_object_i18n', ...)
            ->where(...);

        $count = $query->count();

        // Direct download for small exports
        if ($count <= 500) {
            return $this->directExport($query, $sector, $DB);
        }

        // Queue background job for large exports
        return $this->queueBackgroundExport($request, $DB, $count);
    }
}
```

**Route:** `GET/POST /dataMigration/batchExport`

---

## 8. Preservica Integration

### PreservicaImportService.php

Handles full Preservica import workflow.
```php
class PreservicaImportService
{
    protected $parser;
    protected $rightsService;
    protected $provenanceService;
    protected $stats = [];

    public function import(string $filePath, array $options = []): array
    {
        $format = $this->detectFormat($filePath);
        $this->parser = ParserFactory::create($format);
        
        $records = $this->parser->parse($filePath);
        
        foreach ($records as $record) {
            $objectId = $this->createRecord($record, $options);
            
            // Import rights
            if (!empty($record['rights'])) {
                $this->rightsService->importRights($objectId, $record['rights']);
            }
            
            // Import provenance
            if (!empty($record['provenance'])) {
                $this->provenanceService->importEvents($objectId, $record['provenance']);
            }
            
            // Handle digital objects (PAX only)
            if (!empty($record['digitalObjects'])) {
                $this->importDigitalObjects($objectId, $record['digitalObjects']);
            }
        }
        
        return $this->stats;
    }
}
```

### PreservicaExportService.php

Exports AtoM records to Preservica formats.
```php
class PreservicaExportService
{
    public function exportOpex(int $objectId, array $options = []): string
    {
        $record = $this->loadRecord($objectId);
        
        $xml = new \DOMDocument('1.0', 'UTF-8');
        $opex = $xml->createElementNS(
            'http://www.openpreservationexchange.org/opex/v1.2',
            'opex:OPEXMetadata'
        );
        
        // Add Dublin Core
        $this->addDublinCore($opex, $record);
        
        // Add rights
        $this->addRights($opex, $record);
        
        // Add history/provenance
        $this->addHistory($opex, $record);
        
        // Include children if hierarchy requested
        if ($options['hierarchy'] ?? false) {
            $this->addChildren($opex, $objectId);
        }
        
        $xml->appendChild($opex);
        return $xml->saveXML();
    }

    public function exportPax(int $objectId, array $options = []): string
    {
        // Create temporary directory
        $tempDir = sys_get_temp_dir() . '/pax_' . uniqid();
        mkdir($tempDir);
        
        // Export metadata
        $metadata = $this->exportXip($objectId, $options);
        file_put_contents("$tempDir/metadata.xml", $metadata);
        
        // Copy digital objects
        $this->copyDigitalObjects($objectId, "$tempDir/content");
        
        // Create ZIP
        $zipPath = "/uploads/exports/preservica/{$objectId}.pax";
        $this->createZip($tempDir, $zipPath);
        
        // Cleanup
        $this->removeDirectory($tempDir);
        
        return $zipPath;
    }
}
```

---

## 9. Sector Definitions

Each sector defines its target fields.

### ArchivesSector.php
```php
class ArchivesSector implements SectorInterface
{
    public function getFields(): array
    {
        return [
            'legacyId' => ['required' => true],
            'parentId' => ['required' => false],
            'title' => ['required' => true],
            'identifier' => ['required' => false],
            'levelOfDescription' => ['required' => true],
            'repository' => ['required' => false],
            'scopeAndContent' => ['required' => false],
            'arrangement' => ['required' => false],
            'extentAndMedium' => ['required' => false],
            'dateRange' => ['required' => false],
            'creators' => ['required' => false, 'multivalue' => true],
            'subjectAccessPoints' => ['required' => false, 'multivalue' => true],
            'placeAccessPoints' => ['required' => false, 'multivalue' => true],
            'nameAccessPoints' => ['required' => false, 'multivalue' => true],
            'genreAccessPoints' => ['required' => false, 'multivalue' => true],
            'digitalObjectPath' => ['required' => false],
            'digitalObjectURI' => ['required' => false],
        ];
    }

    public function getLevelMappings(): array
    {
        return [
            'fonds' => QubitTerm::FONDS_ID,
            'collection' => QubitTerm::COLLECTION_ID,
            'series' => QubitTerm::SERIES_ID,
            'subseries' => QubitTerm::SUBSERIES_ID,
            'file' => QubitTerm::FILE_ID,
            'item' => QubitTerm::ITEM_ID,
        ];
    }
}
```

### MuseumSector.php
```php
class MuseumSector implements SectorInterface
{
    public function getFields(): array
    {
        return [
            // Core fields
            'legacyId' => ['required' => true],
            'title' => ['required' => true],
            'objectNumber' => ['required' => false],
            'accessionNumber' => ['required' => false],
            
            // CCO/CDWA fields
            'objectType' => ['required' => false],
            'materials' => ['required' => false],
            'techniques' => ['required' => false],
            'measurements' => ['required' => false],
            'inscriptions' => ['required' => false],
            'condition' => ['required' => false],
            
            // Spectrum fields
            'acquisitionMethod' => ['required' => false],
            'acquisitionDate' => ['required' => false],
            'currentLocation' => ['required' => false],
            'normalLocation' => ['required' => false],
        ];
    }
}
```

---

## 10. CLI Tasks

### migrationImportTask.class.php
```php
class migrationImportTask extends arBaseTask
{
    protected function configure()
    {
        $this->addArguments([
            new sfCommandArgument('file', sfCommandArgument::REQUIRED, 'File to import'),
        ]);
        
        $this->addOptions([
            new sfCommandOption('mapping', null, sfCommandOption::PARAMETER_REQUIRED, 'Mapping ID or name'),
            new sfCommandOption('repository', null, sfCommandOption::PARAMETER_OPTIONAL, 'Repository ID'),
            new sfCommandOption('culture', null, sfCommandOption::PARAMETER_OPTIONAL, 'Culture code', 'en'),
            new sfCommandOption('update', null, sfCommandOption::PARAMETER_NONE, 'Update existing records'),
            new sfCommandOption('dry-run', null, sfCommandOption::PARAMETER_NONE, 'Preview without importing'),
            new sfCommandOption('list-mappings', null, sfCommandOption::PARAMETER_NONE, 'List available mappings'),
        ]);
        
        $this->namespace = 'migration';
        $this->name = 'import';
        $this->briefDescription = 'Import records using field mappings';
    }

    protected function execute($arguments = [], $options = [])
    {
        if ($options['list-mappings']) {
            return $this->listMappings();
        }
        
        $service = new MigrationService();
        $stats = $service->import(
            $arguments['file'],
            $this->resolveMapping($options['mapping']),
            [
                'repository' => $options['repository'],
                'culture' => $options['culture'],
                'update' => $options['update'],
                'dry_run' => $options['dry-run'],
            ]
        );
        
        $this->logSection('import', sprintf(
            'Complete: %d total, %d created, %d updated, %d errors',
            $stats['total'], $stats['created'], $stats['updated'], $stats['errors']
        ));
    }
}
```

### sectorImportTask.class.php (NEW in 1.4.0)

Abstract base class for sector-specific imports with integrated validation.
```php
abstract class sectorImportTask extends arBaseTask
{
    abstract protected function getSectorCode(): string;
    abstract protected function getColumnMap(): array;
    abstract protected function getRequiredColumns(): array;
    abstract protected function saveSectorMetadata(int $objectId, array $row): void;

    protected function configure()
    {
        $this->addArguments([
            new sfCommandArgument('file', sfCommandArgument::REQUIRED, 'CSV file to import'),
        ]);

        $this->addOptions([
            new sfCommandOption('validate-only', null, sfCommandOption::PARAMETER_NONE,
                'Validate without importing'),
            new sfCommandOption('mapping', null, sfCommandOption::PARAMETER_OPTIONAL,
                'Mapping profile ID'),
            new sfCommandOption('repository', null, sfCommandOption::PARAMETER_OPTIONAL,
                'Target repository slug'),
            new sfCommandOption('update', null, sfCommandOption::PARAMETER_OPTIONAL,
                'Match field for updates'),
        ]);
    }

    protected function execute($arguments = [], $options = [])
    {
        $filepath = $arguments['file'];

        // Parse CSV
        $parser = new CsvParser();
        $rows = $parser->parse($filepath);

        $this->logSection('import', sprintf('Parsed %d rows from %s', count($rows), basename($filepath)));

        // Validate
        $validationService = new ValidationService();
        $validationService->setSector($this->getSectorCode());
        $report = $validationService->validate($filepath, [], $rows);

        // Output validation results
        $this->outputValidationReport($report);

        if ($options['validate-only']) {
            $this->logSection('validate', 'Validation-only mode - no records imported');
            return $report->hasErrors() ? 1 : 0;
        }

        if ($report->hasErrors()) {
            $this->logSection('error', 'Validation failed - fix errors and retry');
            return 1;
        }

        // Process import
        foreach ($rows as $rowNum => $row) {
            try {
                $objectId = $this->processRow($row, $options);
                $this->stats['created']++;
            } catch (\Exception $e) {
                $this->stats['errors']++;
                $this->log(sprintf('Row %d: %s', $rowNum + 1, $e->getMessage()));
            }
        }

        $this->logSection('import', sprintf(
            'Complete: %d created, %d updated, %d errors',
            $this->stats['created'],
            $this->stats['updated'],
            $this->stats['errors']
        ));
    }
}
```

### Sector-Specific Import Tasks

| Task Class | Command | Sector |
|------------|---------|--------|
| `archivesCsvImportTask` | `php symfony sector:archives-csv-import` | ISAD-G |
| `museumCsvImportTask` | `php symfony sector:museum-csv-import` | Collections Procedures |
| `libraryCsvImportTask` | `php symfony sector:library-csv-import` | MARC/RDA |
| `galleryCsvImportTask` | `php symfony sector:gallery-csv-import` | CCO |
| `damCsvImportTask` | `php symfony sector:dam-csv-import` | Dublin Core |

**Example: archivesCsvImportTask**
```php
class archivesCsvImportTask extends sectorImportTask
{
    protected function configure()
    {
        parent::configure();
        $this->namespace = 'sector';
        $this->name = 'archives-csv-import';
        $this->briefDescription = 'Import archival records from CSV (ISAD-G)';
    }

    protected function getSectorCode(): string
    {
        return 'archive';
    }

    protected function getColumnMap(): array
    {
        return [
            'legacyId' => 'legacyId',
            'parentId' => 'parentId',
            'identifier' => 'identifier',
            'title' => 'title',
            'levelOfDescription' => 'levelOfDescription',
            'repository' => 'repository',
            'scopeAndContent' => 'scopeAndContent',
            'arrangement' => 'arrangement',
            'extentAndMedium' => 'extentAndMedium',
            'dateRange' => 'dateRange',
            'creators' => 'creators',
            // ... more fields
        ];
    }

    protected function getRequiredColumns(): array
    {
        return ['identifier', 'title', 'levelOfDescription'];
    }

    protected function saveSectorMetadata(int $objectId, array $row): void
    {
        // Archives don't have separate metadata table - all data in information_object
    }
}
```

### preservicaImportTask.class.php
```php
class preservicaImportTask extends arBaseTask
{
    protected function configure()
    {
        $this->addArguments([
            new sfCommandArgument('source', sfCommandArgument::REQUIRED, 'OPEX file or PAX package'),
        ]);

        $this->addOptions([
            new sfCommandOption('format', null, sfCommandOption::PARAMETER_OPTIONAL, 'Format: opex or xip', 'opex'),
            new sfCommandOption('repository', null, sfCommandOption::PARAMETER_OPTIONAL, 'Repository ID'),
            new sfCommandOption('parent', null, sfCommandOption::PARAMETER_OPTIONAL, 'Parent object ID'),
            new sfCommandOption('update', null, sfCommandOption::PARAMETER_NONE, 'Update existing records'),
            new sfCommandOption('dry-run', null, sfCommandOption::PARAMETER_NONE, 'Preview without importing'),
            new sfCommandOption('batch', null, sfCommandOption::PARAMETER_NONE, 'Batch import directory'),
        ]);

        $this->namespace = 'preservica';
        $this->name = 'import';
        $this->briefDescription = 'Import from Preservica OPEX or PAX format';
    }
}
```

---

## 11. Gearman Jobs

For detailed Gearman setup instructions, see: `atom-ahg-plugins/ahgDataMigrationPlugin/docs/GEARMAN.md`

### Quick Setup

```bash
# Automated setup
cd /usr/share/nginx/archive/atom-ahg-plugins/ahgDataMigrationPlugin
sudo ./bin/setup-gearman.sh

# Or manual
sudo apt-get install -y gearman-job-server php8.3-gearman
sudo systemctl enable gearman-job-server atom-worker
sudo systemctl start gearman-job-server atom-worker
```

### DataMigrationJob.class.php

Background job for large imports.
```php
class DataMigrationJob extends arBaseJob
{
    public function run($payload)
    {
        $jobId = $payload['job_id'];
        
        // Update job status
        DB::table('atom_data_migration_job')
            ->where('id', $jobId)
            ->update(['status' => 'running', 'started_at' => now()]);
        
        try {
            $job = DB::table('atom_data_migration_job')->find($jobId);
            $options = json_decode($job->options, true);
            
            $service = new MigrationService();
            $service->setProgressCallback(function($processed, $total) use ($jobId) {
                DB::table('atom_data_migration_job')
                    ->where('id', $jobId)
                    ->update(['processed_records' => $processed]);
            });
            
            $stats = $service->import($job->file_path, $job->mapping_id, $options);
            
            // Update job completion
            DB::table('atom_data_migration_job')
                ->where('id', $jobId)
                ->update([
                    'status' => 'completed',
                    'completed_at' => now(),
                    'created_records' => $stats['created'],
                    'updated_records' => $stats['updated'],
                    'skipped_records' => $stats['skipped'],
                    'error_count' => $stats['errors'],
                ]);
                
        } catch (\Exception $e) {
            DB::table('atom_data_migration_job')
                ->where('id', $jobId)
                ->update([
                    'status' => 'failed',
                    'error_log' => json_encode(['message' => $e->getMessage()]),
                ]);
        }
    }
}
```

---

## 12. Extending the Plugin

### Adding a New Source System

1. **Update SourceDetector.php:**
```php
protected function detectCsvSource(string $filePath): array
{
    $headers = $this->getCsvHeaders($filePath);
    
    // Add detection for new system
    if (in_array('my_system_field', $headers)) {
        return ['format' => 'csv', 'source' => 'my_system'];
    }
    // ...
}
```

2. **Create default mapping JSON:**
```json
// data/mappings/defaults/my_system.json
{
    "name": "My System Import",
    "source_type": "my_system",
    "target_type": "ARCHIVES",
    "field_mappings": {
        "my_id": "legacyId",
        "my_title": "title",
        "my_description": "scopeAndContent"
    }
}
```

3. **Register mapping in install.sql:**
```sql
INSERT INTO atom_data_mapping (name, source_type, target_type, field_mappings, is_system)
VALUES ('My System Import', 'my_system', 'ARCHIVES', '{"my_id":"legacyId",...}', 1);
```

### Adding a New Parser

1. **Create parser class:**
```php
// lib/Parsers/MyFormatParser.php
class MyFormatParser implements ParserInterface
{
    public function parse(string $filePath): array
    {
        // Parse your format
        return $records;
    }
}
```

2. **Register in ParserFactory:**
```php
return match($format) {
    // ...existing parsers
    'myformat' => new MyFormatParser(),
};
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.4.0 | 2026-02-03 | Universal validation framework, sector-specific validators (Archives/Museum/Library/Gallery/DAM), sector CLI import tasks with --validate-only, validation-only mode, sample CSV files, mapping profile export/import, validation rules JSON |
| 1.3.0 | 2026-02-01 | Batch Export UI, Library/Gallery/DAM default mappings, Gearman setup script and docs |
| 1.2.0 | 2026-01-17 | Preservica OPEX/PAX, rights import, provenance, Gearman jobs |
| 1.1.0 | 2026-01-10 | Sector-specific CSV exporters |
| 1.0.0 | 2025-12-15 | Initial release |

---

## Related Plugins

- **ahgRightsPlugin** - Rights management (used for OPEX rights import)
- **ahgProvenancePlugin** - Provenance tracking (used for OPEX history import)
- **ahgOaisPlugin** - OAIS preservation (native SIP/AIP/DIP)

---

## Support

- **Documentation:** https://github.com/ArchiveHeritageGroup/atom-extensions-catalog/docs/
- **Issues:** https://github.com/ArchiveHeritageGroup/atom-extensions-catalog/issues
- **Contact:** support@theahg.co.za

---

## 13. Digital Object Import

### How It Works

Digital objects are imported from Preservica packages using two methods:

#### Method 1: Native AtoM (Default) - `generate_derivatives: true`

Uses `QubitDigitalObject` class which automatically:
- Creates master file record
- Generates thumbnail (150px)
- Generates reference image (480px)
- Applies watermarks if configured
```php
$digitalObject = new \QubitDigitalObject();
$digitalObject->informationObjectId = $objectId;
$digitalObject->usageId = \QubitTerm::MASTER_ID;
$digitalObject->createDerivatives = true;
$digitalObject->assets[] = new \QubitAsset($filePath);
$digitalObject->save();
```

#### Method 2: Direct DB Insert - `generate_derivatives: false`

Faster for large batch imports but skips derivative generation:
- Copies master file to uploads
- Creates `digital_object` record directly
- Optional: Queue derivative generation via Gearman

### CLI Options

| Option | Description |
|--------|-------------|
| `--no-digital-objects` | Skip digital object import entirely |
| `--no-derivatives` | Import masters but skip thumbnail/reference generation |
| `--queue-derivatives` | Queue derivative generation as background job |
| `--no-checksums` | Skip SHA256 checksum verification |

### File Resolution

The importer looks for digital objects in this order:
1. `{basePath}/{filename}` - Direct path
2. `{basePath}/content/{filename}` - PAX content directory

### Checksum Verification

When `verify_checksums: true` (default):
- Extracts expected checksum from `Fixity` or `Checksum` field
- Computes SHA256 of actual file
- Fails import if mismatch

### Upload Path Structure

Files are copied to AtoM's standard structure:
```
/uploads/r/{XX}/{digitalObjectId}_{filename}
```
Where `{XX}` is first 2 characters of MD5 hash of the ID.

### Performance Recommendations

| Scenario | Recommended Options |
|----------|---------------------|
| Small import (<100 files) | Default (generate_derivatives: true) |
| Large import (100-1000) | `--no-derivatives --queue-derivatives` |
| Very large (>1000) | `--no-derivatives` then run `digitalobject:regen-derivatives` |

### Supported File Types

AtoM generates derivatives for:
- Images: JPG, PNG, GIF, TIFF, BMP
- Documents: PDF (first page thumbnail)
- Audio: MP3, WAV, OGG (waveform)
- Video: MP4, AVI, MOV (frame grab)

3D models use ahg3DModelPlugin for Blender-based thumbnails.
