# hyperblog
Blog inicial curso de Git y GitHub platzi

Respuesta a:
Readme.md es una excelente práctica
Después de mucho indagar pude diseñar una plantilla efectiva que uso en todos mis repositorios. Por ejemplo, mi repositorio más votado es https://github.com/ManuelGil/Reset-Windows-Update-Tool y cumple con los siguientes consejos:

-Usa emblemas (badges) que informen a otros desarrolladores sobre el estado de tu desarrollo (actualización, versión, licencia). Puedes encontrar o crear badges en https://shields.io/.
-Puedes colocar atajos (follow, fork, issue, download) en tu repositorio que inviten a la acción. Aquí algunos atajos https://buttons.github.io/.
-Los repositorios más votados son aquellos que tienen un manual de contribución y un código de conducta. Ejemplos en inglés: CONTRIBUTING.md - CODE_OF_CONDUCT.md.
-Puedes agregar emojis en tu archivo README y en tus commits. Algunos truco para los mensajes en tus commits.
-Como última recomendación, puedes hacer un archivo README en inglés para que tu repositorios lleguen a un público mucho mayor.
-En la siguiente página puedes escribir tu readme y darle diseño https://pandao.github.io/editor.md/en.html.

<h2>Nota: La siguiente es una plantilla readme.md para usarla en mis proyectos.</h2>

<div align="center">
	<h1> Reset Windows Update Tool </h1>
</div>

<div align="center">
	<a href="https://www.wureset.com/">
		<img src="https://github.com/ManuelGil/Reset-Windows-Update-Tool/blob/master/docs/images/wureset.png?raw=true" alt="Logo" height="300" width="300">
	</a>
</div>
<br />
<div align="center">
	<a href="#changelog">
		<img src="https://img.shields.io/badge/stability-stable-green.svg" alt="Status">
	</a>
	<a href="#changelog">
		<img src="https://img.shields.io/badge/release-v11.0.0.8-blue.svg" alt="Version">
	</a>
	<a href="#changelog">
		<img src="https://img.shields.io/badge/update-april-yellowgreen.svg" alt="Update">
	</a>
	<a href="#license">
		<img src="https://img.shields.io/badge/license-MS--PL%20License-green.svg" alt="License">
	</a>
</div>
<div align="center">
	<a href="https://twitter.com/intent/follow?screen_name=wureset">
		<img src="https://img.shields.io/twitter/follow/wureset.svg?style=social" alt="Twitter">
	</a>
</div>
<br />
<div align="center">
	<a href="https://support.microsoft.com/en-us/help/13853/windows-lifecycle-fact-sheet">
		<img src="https://github.com/ManuelGil/Reset-Windows-Update-Tool/blob/master/docs/images/Windows-Update.png?raw=true" alt="Lifecycle">
	</a>
</div>
<br />

Reset Windows Update Tool is a complete troubleshooting tool that can be
 generated with Windows updates.

This tool was developed as a script for the Windows command console, it is
 possible to use a development language that allows the use of command line in
 a simple way.

<div align="center">
	<img src="https://github.com/ManuelGil/Reset-Windows-Update-Tool/blob/master/docs/images/menu.gif?raw=true" alt="menu">
</div>
<br />

This tool has been developed for use as a support of system repair options.
 It is possible to reset the Windows Update Components. Also is able to delete
 temporary files, scan, detect and repair corruptions with the Windows System
 image, scan all protected system files and replace any corrupted files, change
 invalid values in the Windows Registry, reset Winsock settings and more.

## :traffic_light: Getting Started

This page will help you get started with Reset Windows Update Tool.

### Requirements

  * Microsoft Windows 7 SP1 or later
  * Dev-C++

### Installation

  1. Clone or Download this repository
  2. Unzip the archive if needed
  3. Start Dev-C++
  4. Goto "File" > "Open project or file" > Search "WUReset.dev" file

### Support
  * Issues: [https://github.com/ManuelGil/Reset-Windows-Update-Tool/issues](https://github.com/ManuelGil/Reset-Windows-Update-Tool/issues)
  * Wiki: [:us:] [:es:] [:it:] [:brazil:]

## :gift: Donate!

If you want to help me to continue this project, you might donate via PayPal.

<a href="https://paypal.me/ManuelFGil"><img src="https://www.paypalobjects.com/webstatic/en_US/i/btn/png/btn_donate_92x26.png" alt="Donate via PayPal"></a>

## :package: Deployment

![Classes Diagram](https://github.com/ManuelGil/Reset-Windows-Update-Tool/blob/master/docs/images/Classes-Diagram.png)

## :wrench: Built With

  * Dev-C++ ([Orwell Dev-C++ 5.11](https://sourceforge.net/projects/orwelldevcpp/))

## :information_source: Changelog

**11.0.0.8** (04/15/2019)

  * <table border="0" cellpadding="4">
		<tr>
			<td>
				<strong>Language:</strong>
			</td>
			<td>
				C++
			</td>
		</tr>
		<tr>
			<td><strong>
				Requirements:
			</strong></td>
			<td>
				Windows 7, Windows 8, Windows 8.1 and Windows 10
			</td>
		</tr>
		<tr>
			<td>
				<strong>Filename:</strong>
			</td>
			<td>
				<a href="https://github.com/ManuelGil/Reset-Windows-Update-Tool">
					wureset.exe
				</a>
			</td>
		</tr>
		<tr>
			<td>
				<strong>Changes:</strong>
			</td>
			<td>
				<ul>
					<li>
						Change ms-settings:windowsupdate to ms-settings:windowsupdate-action.
					</li>
					<li>
						Add link to the configuration from the menu
					</li>
				</ul>
			</td>
		</tr>
	</table>

**11.0.0.7** (03/12/2019)

  * <table border="0" cellpadding="4">
		<tr>
			<td>
				<strong>Language:</strong>
			</td>
			<td>
				C++
			</td>
		</tr>
		<tr>
			<td><strong>
				Requirements:
			</strong></td>
			<td>
				Windows 7, Windows 8, Windows 8.1 and Windows 10
			</td>
		</tr>
		<tr>
			<td>
				<strong>Filename:</strong>
			</td>
			<td>
				<a href="https://github.com/ManuelGil/Reset-Windows-Update-Tool">
					wureset.exe
				</a>
			</td>
		</tr>
		<tr>
			<td>
				<strong>Changes:</strong>
			</td>
			<td>
				<ul>
					<li>
						Add new option to select menu.
					</li>
				</ul>
			</td>
		</tr>
	</table>

**11.0.0.6** (05/06/2018)

  * <table border="0" cellpadding="4">
		<tr>
			<td>
				<strong>Language:</strong>
			</td>
			<td>
				C++
			</td>
		</tr>
		<tr>
			<td><strong>
				Requirements:
			</strong></td>
			<td>
				Windows 7, Windows 8, Windows 8.1 and Windows 10
			</td>
		</tr>
		<tr>
			<td>
				<strong>Filename:</strong>
			</td>
			<td>
				<a href="https://github.com/ManuelGil/Reset-Windows-Update-Tool">
					wureset.exe
				</a>
			</td>
		</tr>
		<tr>
			<td>
				<strong>Changes:</strong>
			</td>
			<td>
				<ul>
					<li>
						Force Group Policy Update.
					</li>
				</ul>
			</td>
		</tr>
	</table>

**11.0.0.5** (04/18/2018)

  * <table border="0" cellpadding="4">
		<tr>
			<td>
				<strong>Language:</strong>
			</td>
			<td>
				C++
			</td>
		</tr>
		<tr>
			<td><strong>
				Requirements:
			</strong></td>
			<td>
				Windows 7, Windows 8, Windows 8.1 and Windows 10
			</td>
		</tr>
		<tr>
			<td>
				<strong>Filename:</strong>
			</td>
			<td>
				<a href="https://github.com/ManuelGil/Reset-Windows-Update-Tool">
					wureset.exe
				</a>
			</td>
		</tr>
		<tr>
			<td>
				<strong>Changes:</strong>
			</td>
			<td>
				<ul>
					<li>
						Force the stopped of services
					</li>
				</ul>
			</td>
		</tr>
	</table>

**11.0.0.4** (03/28/2018)

  * <table border="0" cellpadding="4">
		<tr>
			<td>
				<strong>Language:</strong>
			</td>
			<td>
				C++
			</td>
		</tr>
		<tr>
			<td><strong>
				Requirements:
			</strong></td>
			<td>
				Windows 7, Windows 8, Windows 8.1 and Windows 10
			</td>
		</tr>
		<tr>
			<td>
				<strong>Filename:</strong>
			</td>
			<td>
				<a href="https://github.com/ManuelGil/Reset-Windows-Update-Tool">
					wureset.exe
				</a>
			</td>
		</tr>
		<tr>
			<td>
				<strong>Changes:</strong>
			</td>
			<td>
				<ul>
					<li>
						Improves the export in the Windows Registry
					</li>
				</ul>
			</td>
		</tr>
	</table>

**11.0.0.3** (03/26/2018)

  * <table border="0" cellpadding="4">
		<tr>
			<td>
				<strong>Language:</strong>
			</td>
			<td>
				C++
			</td>
		</tr>
		<tr>
			<td><strong>
				Requirements:
			</strong></td>
			<td>
				Windows 7, Windows 8, Windows 8.1 and Windows 10
			</td>
		</tr>
		<tr>
			<td>
				<strong>Filename:</strong>
			</td>
			<td>
				<a href="https://github.com/ManuelGil/Reset-Windows-Update-Tool">
					wureset.exe
				</a>
			</td>
		</tr>
		<tr>
			<td>
				<strong>Changes:</strong>
			</td>
			<td>
				<ul>
					<li>
						Correction of texts in the menus
					</li>
					<li>
						Verification of errors in the hard disk
					</li>
					<li>
						Checking when renaming the 'SoftwareDistribution' folder
					</li>
					<li>
						Link to official documentation
					</li>
				</ul>
			</td>
		</tr>
	</table>

**10.5.3.5** (12/22/2017)

  * <table border="0" cellpadding="4">
		<tr>
			<td>
				<strong>Language:</strong>
			</td>
			<td>
				Windows Shell Script
			</td>
		</tr>
		<tr>
			<td><strong>
				Requirements:
			</strong></td>
			<td>
				Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1
				and Windows 10
			</td>
		</tr>
		<tr>
			<td>
				<strong>Filename:</strong>
			</td>
			<td>
				<a href="https://gallery.technet.microsoft.com/scriptcenter/Reset-Windows-Update-Agent-d824badc" target="_blank">
					ResetWUEng.cmd
				</a>
			</td>
		</tr>
		<tr>
			<td>
				<strong>Changes:</strong>
			</td>
			<td>
				<ul>
					<li>
						Link to official website
					</li>
				</ul>
			</td>
		</tr>
	</table>

**10.5.3.4** (11/27/2017)

  * <table border="0" cellpadding="4">
		<tr>
			<td>
				<strong>Language:</strong>
			</td>
			<td>
				Windows Shell Script
			</td>
		</tr>
		<tr>
			<td><strong>
				Requirements:
			</strong></td>
			<td>
				Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1
				and Windows 10
			</td>
		</tr>
		<tr>
			<td>
				<strong>Filename:</strong>
			</td>
			<td>
				<a href="https://gallery.technet.microsoft.com/scriptcenter/Reset-Windows-Update-Agent-d824badc" target="_blank">
					ResetWUEng.cmd
				</a>
			</td>
		</tr>
		<tr>
			<td>
				<strong>Changes:</strong>
			</td>
			<td>
				<ul>
					<li>
						Correction of texts in the menus
					</li>
					<li>
						Verification of errors in the hard disk
					</li>
					<li>
						Checking when renaming the 'SoftwareDistribution' folder
					</li>
				</ul>
			</td>
		</tr>
	</table>

**10.5.3.3** (07/23/2017)

  * <table border="0" cellpadding="4">
		<tr>
			<td>
				<strong>Language:</strong>
			</td>
			<td>
				Windows Shell Script
			</td>
		</tr>
		<tr>
			<td><strong>
				Requirements:
			</strong></td>
			<td>
				Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1
				and Windows 10
			</td>
		</tr>
		<tr>
			<td>
				<strong>Filename:</strong>
			</td>
			<td>
				<a href="https://gallery.technet.microsoft.com/scriptcenter/Reset-Windows-Update-Agent-d824badc" target="_blank">
					ResetWUEng.cmd
				</a>
			</td>
		</tr>
		<tr>
			<td>
				<strong>Changes:</strong>
			</td>
			<td>
				<ul>
					<li>
						Compatibility with all versions of Windows 10
						(includes technical preview)
					</li>
				</ul>
			</td>
		</tr>
	</table>

## :octocat: Contributing [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](https://github.com/ManuelGil/Reset-Windows-Update-Tool/issues)

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct.

## :eyeglasses: Authors

  * **Manuel Gil** - *Owner* - [ManuelGil](https://github.com/ManuelGil) 
  * **Kunal Kumar Gupta** - *Guest* - [kunal817](https://github.com/kunal817)
  * **Robin350** - *Guest* - [Robin350](https://github.com/Robin350)
  * **Kosmas Tsiakas** - *Guest* - [kosmastsk](https://github.com/kosmastsk)
  * **Akhil09** - *Guest* - [Akhil09](https://github.com/Akhil09)
  * **Michael Wiarda** - *Guest* - [xift](https://github.com/xift)
  * **Jovan Ferryal E. F.** - *Guest* - [jovanzers](https://github.com/jovanzers)

See also the list of [contributors](https://github.com/ManuelGil/Reset-Windows-Update-Tool/contributors)
 who participated in this project.

## :memo: License

Reset Windows Update Tool is licensed under the MS-PL License - see the
 [Microsoft Public License](https://opensource.org/licenses/MS-PL) for details.


[:us:]: https://github.com/ManuelGil/Reset-Windows-Update-Tool/wiki
[:es:]: https://github.com/ManuelGil/Reset-Windows-Update-Tool/wiki/Home-%5Bes%5D
[:it:]: https://github.com/ManuelGil/Reset-Windows-Update-Tool/wiki/Home-%5Bit%5D
[:brazil:]: https://github.com/ManuelGil/Reset-Windows-Update-Tool/wiki/Home-%5Bbr%5D
