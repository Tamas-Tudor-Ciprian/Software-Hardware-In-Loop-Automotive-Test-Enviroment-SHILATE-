# Changelog

## [v0.1.0-M3](https://github.com/eclipse-leda/leda-distro/tree/v0.1.0-M3) (2023-11-20)

[Full Changelog](https://github.com/eclipse-leda/leda-distro/compare/v0.1.0-M2...v0.1.0-M3)

**Implemented enhancements:**

- Support for WasmEdge WebAssembly [\#147](https://github.com/eclipse-leda/leda-distro/issues/147)
- Default hostname should be device specific [\#126](https://github.com/eclipse-leda/leda-distro/issues/126)
- Document installation on Debian, Ubuntu, RasperryPi OS [\#117](https://github.com/eclipse-leda/leda-distro/issues/117)
- Container with Framebuffer overlay for Leda / SDV / VSS events [\#80](https://github.com/eclipse-leda/leda-distro/issues/80)
- Include a larger subset of the python 3.10 standard library in sdv-image-full [\#69](https://github.com/eclipse-leda/leda-distro/issues/69)
- Preinstall COVESA VSS and Tooling [\#66](https://github.com/eclipse-leda/leda-distro/issues/66)
- Recipe to build self-update-agent as yocto-oci-container [\#37](https://github.com/eclipse-leda/leda-distro/issues/37)
- Documentation for desired state deployment [\#31](https://github.com/eclipse-leda/leda-distro/issues/31)
- Integrate Eclipse Kuksa.VAL - GPS Feeder [\#20](https://github.com/eclipse-leda/leda-distro/issues/20)

**Fixed bugs:**

- Cloud connector stopped working [\#158](https://github.com/eclipse-leda/leda-distro/issues/158)
- No WiFi on raspberry4 [\#105](https://github.com/eclipse-leda/leda-distro/issues/105)
- Seat Service Example with CAN-Bus missing candump and incorrect container descriptor [\#78](https://github.com/eclipse-leda/leda-distro/issues/78)
- sdv-motd is confused by wlan interfaces [\#71](https://github.com/eclipse-leda/leda-distro/issues/71)
- RAUC can not install in stream-mode on Raspberry Pi [\#64](https://github.com/eclipse-leda/leda-distro/issues/64)
- growdisk on RPi4 with sfdisk instead of parted \(signaling kernel\) [\#59](https://github.com/eclipse-leda/leda-distro/issues/59)
- `sdv-provision` produces an empty  `Device ID` [\#56](https://github.com/eclipse-leda/leda-distro/issues/56)
- Missing/Outdated Kuksa databroker-cli [\#34](https://github.com/eclipse-leda/leda-distro/issues/34)

**Closed issues:**

- How to connect Leda on Raspberry Pi to wifi-network [\#155](https://github.com/eclipse-leda/leda-distro/issues/155)
- \[ISSUE\] The latest cannot work on Leda v0.1.0-M1 based on QEMU X86\_64. [\#146](https://github.com/eclipse-leda/leda-distro/issues/146)
- Tools for serial ports as container [\#128](https://github.com/eclipse-leda/leda-distro/issues/128)
- Kanto cm containers not found in sdv-health [\#99](https://github.com/eclipse-leda/leda-distro/issues/99)

**Merged pull requests:**

- Add workspace cleanup to build.yml [\#163](https://github.com/eclipse-leda/leda-distro/pull/163)
- Update requirements for container metrics container due to CVE-2023-46136 found by OCAAS scan [\#161](https://github.com/eclipse-leda/leda-distro/pull/161)
- Cloud connector is disabled [\#160](https://github.com/eclipse-leda/leda-distro/pull/160)
- Wasmedge [\#157](https://github.com/eclipse-leda/leda-distro/pull/157)
- Add an owner check for release workflows to avoid running it on forks [\#153](https://github.com/eclipse-leda/leda-distro/pull/153)
- Add the self-hosted label to build.yml [\#152](https://github.com/eclipse-leda/leda-distro/pull/152)
- Update post-attach.sh [\#150](https://github.com/eclipse-leda/leda-distro/pull/150)
- Wrong IF param in post-attach.sh [\#149](https://github.com/eclipse-leda/leda-distro/pull/149)
- Fix workspace ownership in codespaces [\#148](https://github.com/eclipse-leda/leda-distro/pull/148)
- Add KAD Lock for the MQTT listener [\#145](https://github.com/eclipse-leda/leda-distro/pull/145)
- Blueprint selector [\#144](https://github.com/eclipse-leda/leda-distro/pull/144)
- Removing unneded workflow files [\#143](https://github.com/eclipse-leda/leda-distro/pull/143)
- UM using desired state to CUA and SUA [\#142](https://github.com/eclipse-leda/leda-distro/pull/142)
- Update manager robot test [\#140](https://github.com/eclipse-leda/leda-distro/pull/140)
- Fix general release workflow issues [\#139](https://github.com/eclipse-leda/leda-distro/pull/139)
- Remove a4f from ort scan [\#138](https://github.com/eclipse-leda/leda-distro/pull/138)
- Initial setup for RHIVOS [\#137](https://github.com/eclipse-leda/leda-distro/pull/137)
- FIX RAUC Certificate Paths [\#135](https://github.com/eclipse-leda/leda-distro/pull/135)
- Https port [\#134](https://github.com/eclipse-leda/leda-distro/pull/134)
- Obsolete files [\#133](https://github.com/eclipse-leda/leda-distro/pull/133)
- SUA over https download [\#132](https://github.com/eclipse-leda/leda-distro/pull/132)
- Removed cve-check [\#131](https://github.com/eclipse-leda/leda-distro/pull/131)
- SUA robot  build-177 [\#130](https://github.com/eclipse-leda/leda-distro/pull/130)
- Fix for robot test on SUA [\#125](https://github.com/eclipse-leda/leda-distro/pull/125)
- Fix workflow spdx [\#124](https://github.com/eclipse-leda/leda-distro/pull/124)
- Add meta-lts-mixins to .gitignore [\#123](https://github.com/eclipse-leda/leda-distro/pull/123)
- Robot SUA test update [\#122](https://github.com/eclipse-leda/leda-distro/pull/122)
- Robot changes for SUA Fine-Grained API [\#121](https://github.com/eclipse-leda/leda-distro/pull/121)
- Debian distro tests [\#120](https://github.com/eclipse-leda/leda-distro/pull/120)
- Added meta-lts-mixins [\#118](https://github.com/eclipse-leda/leda-distro/pull/118)
- OSS Compliance tooling [\#115](https://github.com/eclipse-leda/leda-distro/pull/115)
- Leda for Ti Jacinto 7 example kas config [\#109](https://github.com/eclipse-leda/leda-distro/pull/109)
- Update config to include meta-leda-backports layer [\#108](https://github.com/eclipse-leda/leda-distro/pull/108)
- SBOM conversion from SPDX to CycloneDX for self-hosted builds [\#104](https://github.com/eclipse-leda/leda-distro/pull/104)
- Updating OCAAS .ort.yml [\#102](https://github.com/eclipse-leda/leda-distro/pull/102)
- Fix ORT findings [\#96](https://github.com/eclipse-leda/leda-distro/pull/96)
- Fix filenames [\#95](https://github.com/eclipse-leda/leda-distro/pull/95)
- Release attach sboms [\#93](https://github.com/eclipse-leda/leda-distro/pull/93)
- KAS Config TI Jacinto Arago [\#85](https://github.com/eclipse-leda/leda-distro/pull/85)
- Unshallow git repo before reading tags [\#84](https://github.com/eclipse-leda/leda-distro/pull/84)
- Merge pull request \#5 from eclipse-leda/main [\#72](https://github.com/eclipse-leda/leda-distro/pull/72)
- Dockerized VSS vspec2json tool [\#67](https://github.com/eclipse-leda/leda-distro/pull/67)

## [v0.1.0-M2](https://github.com/eclipse-leda/leda-distro/tree/v0.1.0-M2) (2023-05-03)

[Full Changelog](https://github.com/eclipse-leda/leda-distro/compare/v0.1.0-M1...v0.1.0-M2)

**Fixed bugs:**

- Home/End key navigation does not work with putty [\#18](https://github.com/eclipse-leda/leda-distro/issues/18)

## [v0.1.0-M1](https://github.com/eclipse-leda/leda-distro/tree/v0.1.0-M1) (2023-04-11)

[Full Changelog](https://github.com/eclipse-leda/leda-distro/compare/0.0.6...v0.1.0-M1)

## [0.0.6](https://github.com/eclipse-leda/leda-distro/tree/0.0.6) (2023-03-21)

[Full Changelog](https://github.com/eclipse-leda/leda-distro/compare/0.0.5...0.0.6)

**Fixed bugs:**

- Problem with manifest files in 0.0.5 Pi Image [\#60](https://github.com/eclipse-leda/leda-distro/issues/60)
- enp0s2 IP address is not assigned [\#55](https://github.com/eclipse-leda/leda-distro/issues/55)
- multiple occurrences of sudo in run-leda.sh [\#54](https://github.com/eclipse-leda/leda-distro/issues/54)

**Merged pull requests:**

- Fixing ORT config file [\#62](https://github.com/eclipse-leda/leda-distro/pull/62)
- Update DEV\_DIR to point to manifests and remove initdir [\#61](https://github.com/eclipse-leda/leda-distro/pull/61)

## [0.0.5](https://github.com/eclipse-leda/leda-distro/tree/0.0.5) (2023-03-06)

[Full Changelog](https://github.com/eclipse-leda/leda-distro/compare/0.0.4...0.0.5)

**Implemented enhancements:**

- Missing MOTD [\#36](https://github.com/eclipse-leda/leda-distro/issues/36)
- Replacing k9s [\#22](https://github.com/eclipse-leda/leda-distro/issues/22)
- First automated smoke test using Docker setup [\#21](https://github.com/eclipse-leda/leda-distro/issues/21)

**Fixed bugs:**

- sdv-rauc-bundle missing VERSION\_ID [\#40](https://github.com/eclipse-leda/leda-distro/issues/40)
- Image for qemux86\_64 contains potentially unnecessary grub tools [\#28](https://github.com/eclipse-leda/leda-distro/issues/28)
- Image contains unused Kanto and Hawkbit components [\#27](https://github.com/eclipse-leda/leda-distro/issues/27)

**Merged pull requests:**

- Simplify runner scripts [\#58](https://github.com/eclipse-leda/leda-distro/pull/58)
- Robot tests more logs [\#57](https://github.com/eclipse-leda/leda-distro/pull/57)
- Fix test report merge [\#53](https://github.com/eclipse-leda/leda-distro/pull/53)
- Add tests for basic networking [\#52](https://github.com/eclipse-leda/leda-distro/pull/52)
- Docker: More Tests and Container Metrics [\#50](https://github.com/eclipse-leda/leda-distro/pull/50)
- Fix workflow [\#47](https://github.com/eclipse-leda/leda-distro/pull/47)
- Docker/Robot Setup [\#44](https://github.com/eclipse-leda/leda-distro/pull/44)
- Replace Rust tests with Robot [\#43](https://github.com/eclipse-leda/leda-distro/pull/43)

## [0.0.4](https://github.com/eclipse-leda/leda-distro/tree/0.0.4) (2023-01-23)

[Full Changelog](https://github.com/eclipse-leda/leda-distro/compare/0.0.3...0.0.4)

**Fixed bugs:**

- Default mosquitto configuration [\#30](https://github.com/eclipse-leda/leda-distro/issues/30)
- Raspi4 doesn't boot with release 0.0.3 [\#24](https://github.com/eclipse-leda/leda-distro/issues/24)
- No releases available [\#13](https://github.com/eclipse-leda/leda-distro/issues/13)
- SDV Container images [\#4](https://github.com/eclipse-leda/leda-distro/issues/4)

**Merged pull requests:**

- Populate downloads mirror [\#35](https://github.com/eclipse-leda/leda-distro/pull/35)
- Fix kas config for Raspberry Pi boot problem [\#25](https://github.com/eclipse-leda/leda-distro/pull/25)
- Docker Compose setup for Leda [\#17](https://github.com/eclipse-leda/leda-distro/pull/17)

## [0.0.3](https://github.com/eclipse-leda/leda-distro/tree/0.0.3) (2022-12-05)

[Full Changelog](https://github.com/eclipse-leda/leda-distro/compare/0.0.2...0.0.3)

## [0.0.2](https://github.com/eclipse-leda/leda-distro/tree/0.0.2) (2022-12-05)

[Full Changelog](https://github.com/eclipse-leda/leda-distro/compare/0.0.1...0.0.2)

## [0.0.1](https://github.com/eclipse-leda/leda-distro/tree/0.0.1) (2022-12-02)

[Full Changelog](https://github.com/eclipse-leda/leda-distro/compare/e99924c777056c160d81a557db8ce18339109bde...0.0.1)

**Closed issues:**

- git submodules are not available [\#3](https://github.com/eclipse-leda/leda-distro/issues/3)

**Merged pull requests:**

- Sync build and release workflows [\#16](https://github.com/eclipse-leda/leda-distro/pull/16)
- Running SPDX for the build [\#15](https://github.com/eclipse-leda/leda-distro/pull/15)
- Features and build process updates [\#14](https://github.com/eclipse-leda/leda-distro/pull/14)
- Custom BitBake/kas build container [\#12](https://github.com/eclipse-leda/leda-distro/pull/12)
- SPDX scanner and SBOM creation [\#11](https://github.com/eclipse-leda/leda-distro/pull/11)
- Mirrors, DHCP and TAP setup [\#10](https://github.com/eclipse-leda/leda-distro/pull/10)
- Multiple fixes and remote sstate-cache mirror [\#9](https://github.com/eclipse-leda/leda-distro/pull/9)
- Cleanup after switch to kas as build tool [\#8](https://github.com/eclipse-leda/leda-distro/pull/8)
- Cleanup Build for Raspi [\#7](https://github.com/eclipse-leda/leda-distro/pull/7)
- KAS build config and initial GH workflow [\#6](https://github.com/eclipse-leda/leda-distro/pull/6)
- Added 2 robot test files [\#5](https://github.com/eclipse-leda/leda-distro/pull/5)
- Update NOTICE.md [\#2](https://github.com/eclipse-leda/leda-distro/pull/2)



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
