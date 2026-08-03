# ahgFeedbackPlugin Technical Documentation

## Overview

The ahgFeedbackPlugin provides user feedback management functionality for AtoM using Laravel Query Builder. It allows users to submit feedback on archival records or general feedback, with full CRUD operations for administrators.

## Architecture

### Plugin Structure
<div style="overflow-x:auto;margin:1rem 0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 366 404" style="max-width:100%;height:auto;font-family:ui-monospace,Menlo,Consolas,monospace"><rect x="0.5" y="0.5" width="365" height="403" rx="8" fill="#f7faf9" stroke="#d8e6e3"/><line x1="13.6" y1="34.0" x2="17.2" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="26.0" x2="13.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="34.0" x2="13.6" y2="42.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="34.0" x2="20.8" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="34.0" x2="24.4" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="34.0" x2="28.0" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="34.0" x2="31.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="42.0" x2="13.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="13.6" y2="58.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="50.0" x2="46.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="42.0" x2="42.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="50.0" x2="49.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="50.0" x2="53.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="50.0" x2="56.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="50.0" x2="60.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="17.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="58.0" x2="13.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="13.6" y2="74.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="66.0" x2="20.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="66.0" x2="24.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="66.0" x2="28.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="66.0" x2="31.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="74.0" x2="13.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="82.0" x2="13.6" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="82.0" x2="46.0" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="74.0" x2="42.4" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="82.0" x2="49.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="82.0" x2="53.2" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="82.0" x2="56.8" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="82.0" x2="60.4" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="98.0" x2="17.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="90.0" x2="13.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="98.0" x2="13.6" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="98.0" x2="20.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="98.0" x2="24.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="98.0" x2="28.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="98.0" x2="31.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="114.0" x2="17.2" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="106.0" x2="13.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="114.0" x2="13.6" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="114.0" x2="20.8" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="114.0" x2="24.4" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="114.0" x2="28.0" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="114.0" x2="31.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="122.0" x2="13.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="130.0" x2="13.6" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="130.0" x2="46.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="122.0" x2="42.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="130.0" x2="49.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="130.0" x2="53.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="130.0" x2="56.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="130.0" x2="60.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="146.0" x2="17.2" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="138.0" x2="13.6" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="146.0" x2="13.6" y2="154.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="146.0" x2="20.8" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="146.0" x2="24.4" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="146.0" x2="28.0" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="146.0" x2="31.6" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="154.0" x2="13.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="162.0" x2="13.6" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="162.0" x2="46.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="154.0" x2="42.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="162.0" x2="49.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="162.0" x2="53.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="162.0" x2="56.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="162.0" x2="60.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="170.0" x2="13.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="178.0" x2="13.6" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="178.0" x2="74.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="170.0" x2="71.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="178.0" x2="71.2" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="178.0" x2="78.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="178.0" x2="82.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="178.0" x2="85.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="178.0" x2="89.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="186.0" x2="13.6" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="194.0" x2="13.6" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="186.0" x2="71.2" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="194.0" x2="71.2" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="194.0" x2="103.6" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="186.0" x2="100.0" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="194.0" x2="100.0" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="194.0" x2="107.2" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="194.0" x2="110.8" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="194.0" x2="114.4" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="194.0" x2="118.0" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="202.0" x2="13.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="210.0" x2="13.6" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="202.0" x2="71.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="210.0" x2="71.2" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="210.0" x2="103.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="202.0" x2="100.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="210.0" x2="100.0" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="210.0" x2="107.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="210.0" x2="110.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="210.0" x2="114.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="210.0" x2="118.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="218.0" x2="13.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="226.0" x2="13.6" y2="234.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="218.0" x2="71.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="226.0" x2="71.2" y2="234.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="226.0" x2="103.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="218.0" x2="100.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="226.0" x2="100.0" y2="234.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="226.0" x2="107.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="226.0" x2="110.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="226.0" x2="114.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="226.0" x2="118.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="234.0" x2="13.6" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="242.0" x2="13.6" y2="250.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="234.0" x2="71.2" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="242.0" x2="71.2" y2="250.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="242.0" x2="103.6" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="234.0" x2="100.0" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="242.0" x2="100.0" y2="250.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="242.0" x2="107.2" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="242.0" x2="110.8" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="242.0" x2="114.4" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="242.0" x2="118.0" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="250.0" x2="13.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="258.0" x2="13.6" y2="266.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="250.0" x2="71.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="258.0" x2="71.2" y2="266.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="258.0" x2="103.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="250.0" x2="100.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="258.0" x2="100.0" y2="266.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="258.0" x2="107.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="258.0" x2="110.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="258.0" x2="114.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="258.0" x2="118.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="266.0" x2="13.6" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="274.0" x2="13.6" y2="282.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="266.0" x2="71.2" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="274.0" x2="71.2" y2="282.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="274.0" x2="103.6" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="266.0" x2="100.0" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="274.0" x2="107.2" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="274.0" x2="110.8" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="274.0" x2="114.4" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="274.0" x2="118.0" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="282.0" x2="13.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="290.0" x2="13.6" y2="298.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="290.0" x2="74.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="282.0" x2="71.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="290.0" x2="78.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="290.0" x2="82.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="290.0" x2="85.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="290.0" x2="89.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="298.0" x2="13.6" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="306.0" x2="13.6" y2="314.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="306.0" x2="103.6" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="298.0" x2="100.0" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="306.0" x2="100.0" y2="314.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="306.0" x2="107.2" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="306.0" x2="110.8" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="306.0" x2="114.4" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="306.0" x2="118.0" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="314.0" x2="13.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="322.0" x2="13.6" y2="330.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="322.0" x2="103.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="314.0" x2="100.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="322.0" x2="100.0" y2="330.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="322.0" x2="107.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="322.0" x2="110.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="322.0" x2="114.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="322.0" x2="118.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="330.0" x2="13.6" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="338.0" x2="13.6" y2="346.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="338.0" x2="103.6" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="330.0" x2="100.0" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="338.0" x2="100.0" y2="346.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="338.0" x2="107.2" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="338.0" x2="110.8" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="338.0" x2="114.4" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="338.0" x2="118.0" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="346.0" x2="13.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="354.0" x2="13.6" y2="362.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="354.0" x2="103.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="346.0" x2="100.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="354.0" x2="100.0" y2="362.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="354.0" x2="107.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="354.0" x2="110.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="354.0" x2="114.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="354.0" x2="118.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="362.0" x2="13.6" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="370.0" x2="13.6" y2="378.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="370.0" x2="103.6" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="362.0" x2="100.0" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="370.0" x2="100.0" y2="378.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="370.0" x2="107.2" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="370.0" x2="110.8" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="370.0" x2="114.4" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="370.0" x2="118.0" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="378.0" x2="13.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="386.0" x2="13.6" y2="394.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="386.0" x2="103.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="378.0" x2="100.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="386.0" x2="107.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="386.0" x2="110.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="386.0" x2="114.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="386.0" x2="118.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><text x="10.0" y="22.0" font-size="9.5" fill="#10373E">ahgFeedbackPlugin/</text><text x="38.8" y="38.0" font-size="9.5" fill="#10373E">config/</text><text x="67.6" y="54.0" font-size="9.5" fill="#10373E">ahgFeedbackPluginConfiguration.class.php</text><text x="38.8" y="70.0" font-size="9.5" fill="#10373E">data/</text><text x="67.6" y="86.0" font-size="9.5" fill="#10373E">install.sql</text><text x="38.8" y="102.0" font-size="9.5" fill="#10373E">extension.json</text><text x="38.8" y="118.0" font-size="9.5" fill="#10373E">lib/</text><text x="67.6" y="134.0" font-size="9.5" fill="#10373E">task/</text><text x="38.8" y="150.0" font-size="9.5" fill="#10373E">modules/</text><text x="67.6" y="166.0" font-size="9.5" fill="#10373E">ahgFeedback/</text><text x="96.4" y="182.0" font-size="9.5" fill="#10373E">actions/</text><text x="125.2" y="198.0" font-size="9.5" fill="#10373E">browseAction.class.php</text><text x="125.2" y="214.0" font-size="9.5" fill="#10373E">deleteAction.class.php</text><text x="125.2" y="230.0" font-size="9.5" fill="#10373E">editAction.class.php</text><text x="125.2" y="246.0" font-size="9.5" fill="#10373E">generalAction.class.php</text><text x="125.2" y="262.0" font-size="9.5" fill="#10373E">submitAction.class.php</text><text x="125.2" y="278.0" font-size="9.5" fill="#10373E">viewAction.class.php</text><text x="96.4" y="294.0" font-size="9.5" fill="#10373E">templates/</text><text x="125.2" y="310.0" font-size="9.5" fill="#10373E">browseSuccess.php</text><text x="125.2" y="326.0" font-size="9.5" fill="#10373E">deleteSuccess.php</text><text x="125.2" y="342.0" font-size="9.5" fill="#10373E">editSuccess.php</text><text x="125.2" y="358.0" font-size="9.5" fill="#10373E">generalSuccess.php</text><text x="125.2" y="374.0" font-size="9.5" fill="#10373E">submitSuccess.php</text><text x="125.2" y="390.0" font-size="9.5" fill="#10373E">viewSuccess.php</text></svg></div>

### Database Schema

The plugin uses existing AtoM feedback tables with the object inheritance pattern:
```sql
-- Base object table (AtoM standard)
object (
    id INT PRIMARY KEY AUTO_INCREMENT,
    class_name VARCHAR(255),  -- 'QubitFeedback'
    created_at DATETIME,
    updated_at DATETIME,
    serial_number INT
)

-- Main feedback table
feedback (
    id INT PRIMARY KEY,        -- FK to object.id
    feed_name VARCHAR(50),
    feed_surname VARCHAR(50),
    feed_phone VARCHAR(50),
    feed_email VARCHAR(50),
    feed_relationship TEXT,
    parent_id VARCHAR(50),
    feed_type_id INT,
    lft INT,                   -- Nested set
    rgt INT,                   -- Nested set
    source_culture VARCHAR(14)
)

-- Internationalized fields
feedback_i18n (
    id INT,                    -- FK to feedback.id
    culture VARCHAR(14),
    name VARCHAR(1024),        -- Subject/record title
    unique_identifier VARCHAR(1024),
    remarks TEXT,
    object_id TEXT,            -- FK to information_object.id
    completed_at DATETIME,
    created_at DATETIME,
    status_id INT              -- QubitTerm::PENDING_ID or COMPLETED_ID
)
```

### Key Design Decisions

1. **No QubitFeedback Model**: Uses Laravel Query Builder exclusively to avoid Propel model dependencies
2. **Object Table Inheritance**: Inserts into `object` table first, then `feedback`, then `feedback_i18n`
3. **Nested Set Pattern**: Maintains `lft`/`rgt` columns for AtoM compatibility
4. **i18n Support**: Culture-aware queries joining `feedback` and `feedback_i18n`

## Actions

### browseAction

Lists all feedback with filtering and pagination.

**Route**: `/feedback` or `/feedback?filter=pending|completed`

**Query Builder Pattern**:
```php
$query = DB::table('feedback')
    ->join('feedback_i18n', 'feedback.id', '=', 'feedback_i18n.id')
    ->where('feedback_i18n.culture', $culture)
    ->select('feedback.*', 'feedback_i18n.*');
```

**Template Variables**:
- `$feedbackItems` - Collection of feedback records
- `$totalCount`, `$pendingCount`, `$completedCount` - Count statistics
- `$filter`, `$sort`, `$page` - Current filter state
- `$totalPages`, `$currentPage` - Pagination info

### generalAction

Handles general feedback submission (not linked to a record).

**Route**: `/feedback/general`

**Insert Pattern**:
```php
// 1. Insert into object table
$objectId = DB::table('object')->insertGetId([
    'class_name' => 'QubitFeedback',
    'created_at' => $now,
    'updated_at' => $now,
    'serial_number' => 0,
]);

// 2. Get nested set values
$maxRgt = DB::table('feedback')->max('rgt') ?? 0;

// 3. Insert into feedback table
DB::table('feedback')->insert([
    'id' => $objectId,
    'feed_name' => $value,
    // ... other fields
    'lft' => $maxRgt + 1,
    'rgt' => $maxRgt + 2,
    'source_culture' => $culture,
]);

// 4. Insert into feedback_i18n
DB::table('feedback_i18n')->insert([
    'id' => $objectId,
    'culture' => $culture,
    'status_id' => QubitTerm::PENDING_ID,
    // ... other fields
]);
```

### submitAction

Handles feedback submission linked to an information object.

**Route**: `/{slug}/ahgFeedback/submit`

**Key Difference from generalAction**:
- Receives `slug` parameter to identify linked record
- Stores `object_id` in `feedback_i18n` referencing the information object
- Pre-populates `name` field with record title

### editAction

Administrator edit interface for feedback.

**Route**: `/feedback/{id}/edit`

**Update Pattern**:
```php
DB::table('feedback')
    ->where('id', $id)
    ->update([...]);

DB::table('feedback_i18n')
    ->where('id', $id)
    ->where('culture', $culture)
    ->update([...]);

DB::table('object')
    ->where('id', $id)
    ->update(['updated_at' => $now]);
```

### deleteAction

Deletes feedback (cascades via foreign keys).

**Route**: `/feedback/{id}/delete`

**Delete Pattern**:
```php
// Object table has ON DELETE CASCADE
DB::table('object')->where('id', $id)->delete();
```

## Integration Points

### Template Integration

The Item Feedback button is conditionally displayed based on plugin availability:
```php
<?php if (class_exists('ahgFeedbackPluginConfiguration')): ?>
    <?php echo link_to(
        '<i class="fas fa-comment me-1"></i>' . __('Item Feedback'),
        ['module' => 'ahgFeedback', 'action' => 'submit', 'slug' => $resource->slug],
        ['class' => 'btn btn-sm btn-outline-secondary']
    ); ?>
<?php endif; ?>
```

**Integrated Templates**:

| Location | Template | Button Type |
|----------|----------|-------------|
| ISAD | `sfIsadPlugin/templates/indexSuccess.php` | Standalone button |
| Museum (CCO) | `ahgMuseumPlugin/modules/cco/templates/indexSuccess.php` | Standalone button |
| Museum | `ahgMuseumPlugin/modules/ahgMuseumPlugin/templates/indexSuccess.php` | Standalone button |
| Library | `ahgLibraryPlugin/modules/ahgLibraryPlugin/templates/indexSuccess.php` | Dropdown menu |
| Gallery | `ahgGalleryPlugin/modules/ahgGalleryPlugin/templates/indexSuccess.php` | Dropdown menu |
| DAM/Others | `ahgThemeB5Plugin/modules/informationobject/templates/_actions.php` | Dropdown menu |

### Routing

Defined in `ahgThemeB5Plugin/config/routing.yml`:
```yaml
ahg_feedback_browse:
  url: /feedback
  param: { module: ahgFeedback, action: browse }

ahg_feedback_general:
  url: /feedback/general
  param: { module: ahgFeedback, action: general }

ahg_feedback_submit:
  url: /:slug/ahgFeedback/submit
  param: { module: ahgFeedback, action: submit }

ahg_feedback_edit:
  url: /feedback/:id/edit
  param: { module: ahgFeedback, action: edit }

ahg_feedback_delete:
  url: /feedback/:id/delete
  param: { module: ahgFeedback, action: delete }
```

### Plugin Registration

Registered in `atom_plugin` table:
```sql
INSERT INTO atom_plugin (name, class_name, is_enabled, category, version, description)
VALUES (
    'ahgFeedbackPlugin',
    'ahgFeedbackPluginConfiguration',
    1,
    'ahg',
    '1.0.0',
    'User feedback and suggestions management'
);
```

## Feedback Types

Stored in `feed_type_id`:

| ID | Type |
|----|------|
| 0 | General Feedback |
| 1 | Error Report |
| 2 | Suggestion |
| 3 | Correction Request |
| 4 | Need Assistance |

## Status Values

Uses AtoM's QubitTerm constants:

| Constant | Value | Description |
|----------|-------|-------------|
| `QubitTerm::PENDING_ID` | (varies) | Awaiting review |
| `QubitTerm::COMPLETED_ID` | (varies) | Addressed/closed |

## Security

- **Authentication**: Required for browse/edit/delete actions
- **Authorization**: Administrator access required for management
- **Public Access**: Submit and general actions can be public (configurable)
- **XSS Prevention**: All output escaped with `esc_entities()`

## Dependencies

- **atom-framework**: Laravel Query Builder (`Illuminate\Database`)
- **AtoM 2.10**: Base system with Symfony 1.x
- **Bootstrap 5**: UI framework (via ahgThemeB5Plugin)

## Configuration

Plugin can be enabled/disabled via:
- Admin → AHG Settings → Plugin Management
- CLI: `php bin/atom extension:enable ahgFeedbackPlugin`

## Testing

**Test URLs**:
- Browse: `https://[domain]/feedback`
- General: `https://[domain]/feedback/general`
- Edit: `https://[domain]/feedback/[id]/edit`
- Item Feedback: Click button on any record

## Troubleshooting

### Common Issues

**"Class QubitFeedback not found"**
- Cause: Old action using Propel model
- Solution: All actions must use Laravel Query Builder

**"Cannot use object of type stdClass as array"**
- Cause: url_for() expecting QubitObject
- Solution: Use explicit URL: `url_for(['module' => 'ahgFeedback', 'action' => 'edit', 'id' => $id])`

**"Foreign key constraint fails on feedback"**
- Cause: Not inserting into `object` table first
- Solution: Insert sequence: object → feedback → feedback_i18n

### Debug Queries
```php
// Enable query logging
DB::enableQueryLog();
// ... run queries
dd(DB::getQueryLog());
```

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-13 | Initial release with Laravel Query Builder |
