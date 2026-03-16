# Changelog

## [Unreleased](https://github.com/eclipse-leda/leda-distro/tree/HEAD)

[Full Changelog](https://github.com/eclipse-leda/leda-distro/compare/v0.1.0-M1...HEAD)

**Merged pull requests:**

- Dockerized VSS vspec2json tool [\#67](https://github.com/eclipse-leda/leda-distro/pull/67)

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
