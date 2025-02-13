%global debug_package %{nil}

%global _firmwarepath	/usr/lib/firmware
%define _binaries_in_noarch_packages_terminate_build 0

Name:		linux-firmware
Version:	20250211
Release:	1%{?dist}
Summary:	Firmware files used by the Linux kernel
License:	GPL-1.0-or-later AND GPL-2.0-or-later AND MIT AND LicenseRef-Callaway-Redistributable-no-modification-permitted
URL:		http://www.kernel.org/
BuildArch:	noarch

Source0:	https://www.kernel.org/pub/linux/kernel/firmware/%{name}-%{version}.tar.xz

BuildRequires:	make
BuildRequires:	git-core
BuildRequires:	python3
%if %{undefined rhel}
# Not required but de-dupes FW so reduces size
BuildRequires:	rdfind
%endif

Requires:	linux-firmware-whence
Recommends:	amd-gpu-firmware
Recommends:	amd-ucode-firmware
Recommends:	atheros-firmware
Recommends:	brcmfmac-firmware
Recommends:	cirrus-audio-firmware
Recommends:	intel-audio-firmware
Recommends:	intel-gpu-firmware
Recommends:	mt7xxx-firmware
Recommends:	nvidia-gpu-firmware
Recommends:	nxpwireless-firmware
Recommends:	realtek-firmware
Recommends:	tiwilink-firmware

%description
This package includes firmware files required for some devices to
operate.

%package whence
Summary:	WHENCE License file
License:	GPL-1.0-or-later AND GPL-2.0-or-later AND MIT AND LicenseRef-Callaway-Redistributable-no-modification-permitted
%description whence
This package contains the WHENCE license file which documents the vendor license details.

# GPU firmwares
%package -n amd-gpu-firmware
Summary:	Firmware for AMD GPUs
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n amd-gpu-firmware
Firmware for AMD amdgpu and radeon GPUs.

%package -n intel-gpu-firmware
Summary:	Firmware for Intel GPUs
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n intel-gpu-firmware
Firmware for Intel GPUs including GuC (Graphics Microcontroller), HuC (HEVC/H.265
Microcontroller) and DMC (Display Microcontroller) firmware for Skylake and later
platforms.

%package -n nvidia-gpu-firmware
Summary:	Firmware for NVIDIA GPUs
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n nvidia-gpu-firmware
Firmware for NVIDIA GPUs.

# Microcode updates
%package -n amd-ucode-firmware
Summary:	Microcode updates for AMD CPUs
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n amd-ucode-firmware
Microcode updates for AMD CPUs, AMD SEV and AMD TEE.

# WiFi/Bluetooth firmwares
%package -n atheros-firmware
Summary:	Firmware for Qualcomm Atheros WiFi/Bluetooth adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n atheros-firmware
Firmware for Qualcomm Atheros ath6k/ath9k/ath10k/ath11k WiFi adapters.

%package -n brcmfmac-firmware
Summary:	Firmware for Broadcom/Cypress brcmfmac WiFi/Bluetooth adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n brcmfmac-firmware
Firmware for Broadcom/Cypress brcmfmac WiFi/Bluetooth adapters.

%package -n iwlegacy-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 3945(A)BG and 4965AGN adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n iwlegacy-firmware
This package contains the firmware required by the iwlegacy driver
for Linux. This includes the 3945(A)BG and 4965AGN WiFi NICs. Usage
of the firmware is subject to the terms and conditions contained
inside the provided LICENSE file. Please read it carefully.

%package -n iwlwifi-dvm-firmware
Summary:	DVM Firmware for Intel(R) Wireless WiFi adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n iwlwifi-dvm-firmware
This package contains the firmware required by the iwlwifi driver
for Linux built with DVM firmware support (CONFIG_IWLDVM=y/m). Usage of
the firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%package -n iwlwifi-mvm-firmware
Summary:	MVM Firmware for Intel(R) Wireless WiFi adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n iwlwifi-mvm-firmware
This package contains the firmware required by the iwlwifi driver
for Linux built with MVM firmware support (CONFIG_IWLMVM=y/m).  Usage of
the firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%package -n libertas-firmware
Summary:	Firmware for Marvell Libertas SD/USB WiFi Network Adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n libertas-firmware
Firmware for the Marvell Libertas series of WiFi Network Adapters
Including the SD 8686/8787 and USB 8388/8388.

%package -n mt7xxx-firmware
Summary:	Firmware for Mediatek 7600/7900 series WiFi/Bluetooth adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n mt7xxx-firmware
Firmware for Mediatek 7600/7900 series WiFi/Bluetooth adapters

%package -n nxpwireless-firmware
Summary:	Firmware for NXP WiFi/Bluetooth/UWB adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n nxpwireless-firmware
Firmware for NXP WiFi/Bluetooth/UWB adapters.

%package -n realtek-firmware
Summary:	Firmware for Realtek WiFi/Bluetooth adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n realtek-firmware
Firmware for Realtek WiFi/Bluetooth adapters

%package -n tiwilink-firmware
Summary:	Firmware for Texas Instruments WiFi/Bluetooth adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n tiwilink-firmware
Firmware for Texas Instruments WiFi/Bluetooth adapters

# SMART NIC and network switch firmwares
%package -n liquidio-firmware
Summary:	Firmware for Cavium LiquidIO Intelligent Server Adapter
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n liquidio-firmware
Firmware for Cavium LiquidIO Intelligent Server Adapter

%package -n mlxsw_spectrum-firmware
Summary:	Firmware for Mellanox Spectrum 1/2/3 Switches
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n mlxsw_spectrum-firmware
Firmware for Mellanox Spectrumi series 1/2/3 ethernet switches.

%package -n mrvlprestera-firmware
Summary:	Firmware for Marvell Prestera Switchdev/ASIC devices
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n mrvlprestera-firmware
Firmware for Marvell Prestera Switchdev/ASIC devices

%package -n netronome-firmware
Summary:	Firmware for Netronome Smart NICs
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n netronome-firmware
Firmware for Netronome Smart NICs

%package -n qed-firmware
Summary:	Firmware for Marvell FastLinQ adapters family
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n qed-firmware
Firmware for Marvell FastLinQ adapters family (QDE), this device
supports RoCE (RDMA over Converged Ethernet), iSCSI, iWARP, FCoE
and ethernet including SRIOV, DCB etc.

# Silicon Vendor specific
%package -n qcom-firmware
Summary:	Firmware for Qualcomm SoCs
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
Requires:	atheros-firmware = %{version}-%{release}
%description -n qcom-firmware
Firmware for various compoents in Qualcomm SoCs including Adreno
GPUs, Venus video encode/decode, Audio DSP, Compute DSP, WWAN
modem, Sensor DSPs.

# Vision and ISP hardware
%package -n intel-vsc-firmware
Summary:	Firmware files for Intel Visual Sensing Controller (IVSC)
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n intel-vsc-firmware
Firmware files for Intel Visual Sensing Controller (IVSC) for
Tiger Lake, Alder Lake and Raptor Lake SoCs and the IPU3/6 firmware.

# Sound codec hardware
%package -n cirrus-audio-firmware
Summary:	Firmware for Cirrus audio amplifiers and codecs
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n cirrus-audio-firmware
Firmware for Cirrus audio amplifiers and codecs

%package -n intel-audio-firmware
Summary:	Firmware for Intel audio DSP amplifiers and codecs
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n intel-audio-firmware
Firmware for Intel audio DSP amplifiers and codecs

# Random other hardware
%package -n dvb-firmware
Summary:	Firmware for various DVB broadcast receivers
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence
%description -n dvb-firmware
Firmware for various DVB broadcast receivers. These include the
Siano DTV devices, devices based on Conexant chipsets (cx18,
cx23885, cx23840, cx231xx), Xceive xc4000/xc5000, DiBcom dib0700,
Terratec H5 DRX-K, ITEtech IT9135 Ax and Bx, and av7110.

%prep
%autosetup -S git -p1

%build

%install
mkdir -p %{buildroot}/%{_firmwarepath}
mkdir -p %{buildroot}/%{_firmwarepath}/updates

make DESTDIR=%{buildroot}/ FIRMWAREDIR=%{_firmwarepath} install-xz
%if %{undefined rhel}
make DESTDIR=%{buildroot}/ FIRMWAREDIR=%{_firmwarepath} dedup
%endif

#Cleanup files we don't want to ship
pushd %{buildroot}/%{_firmwarepath}
# Remove firmware shipped in separate packages already
# Perhaps these should be built as subpackages of linux-firmware?
rm -rf ess korg sb16 yamaha

# Remove firmware for Creative CA0132 HD as it's in alsa-firmware
rm -f ctefx.bin* ctspeq.bin*

# Remove source files we don't need to install
rm -rf carl9170fw
rm -rf cis/{src,Makefile}
rm -f atusb/ChangeLog
rm -f av7110/{Boot.S,Makefile}
rm -f dsp56k/{bootstrap.asm,concat-bootstrap.pl,Makefile}
rm -f iscis/{*.c,*.h,README,Makefile}
rm -f keyspan_pda/{keyspan_pda.S,xircom_pgs.S,Makefile}
rm -f usbdux/*dux */*.asm

# No need to install old firmware versions where we also provide newer versions
# which are preferred and support the same (or more) hardware
rm -f libertas/sd8686_v8*
rm -f libertas/usb8388_v5.bin*

# Remove superfluous infra files
rm -f check_whence.py Makefile README
popd

# Create file list but exclude firmwares that we place in subpackages
FILEDIR=`pwd`
pushd %{buildroot}/%{_firmwarepath}
find . \! -type d > $FILEDIR/linux-firmware.files
find . -type d | sed -e '/^.$/d' > $FILEDIR/linux-firmware.dirs
popd
sed -i -e 's:^./::' linux-firmware.{files,dirs}
sed \
	-i -e '/^a300_p/d' \
	-i -e '/^amdgpu/d' \
	-i -e '/^amdnpu/d' \
	-i -e '/^amd/d' \
	-i -e '/^amdtee/d' \
	-i -e '/^amd-ucode/d' \
	-i -e '/^ar3k/d' \
	-i -e '/^ath6k/d' \
	-i -e '/^ath9k_htc/d' \
	-i -e '/^ath10k/d' \
	-i -e '/^ath11k/d' \
	-i -e '/^ath12k/d' \
	-i -e '/^as102_data/d' \
	-i -e '/^av7110/d' \
	-i -e '/^brcm/d' \
	-i -e '/^cirrus/d' \
	-i -e '/^cmmb/d' \
	-i -e '/^cypress/d' \
	-i -e '/^dvb/d' \
	-i -e '/^i915/d' \
	-i -e '/^intel\/avs/d' \
	-i -e '/^intel\/catpt/d' \
	-i -e '/^intel\/dsp_fw/d' \
	-i -e '/^intel\/fw_sst/d' \
	-i -e '/^intel\/ipu/d' \
	-i -e '/^intel\/ipu3/d' \
	-i -e '/^intel\/irci_irci/d' \
	-i -e '/^intel\/vsc/d' \
	-i -e '/^isdbt/d' \
	-i -e '/^iwlwifi/d' \
	-i -e '/^nvidia\/a/d' \
	-i -e '/^nvidia\/g/d' \
	-i -e '/^nvidia\/tu/d' \
	-i -e '/^lgs8g75/d' \
	-i -e '/^libertas/d' \
	-i -e '/^liquidio/d' \
	-i -e '/^mellanox/d' \
	-i -e '/^mediatek\/mt76/d' \
	-i -e '/^mediatek\/mt79/d' \
	-i -e '/^mediatek\/BT/d' \
	-i -e '/^mediatek\/WIFI/d' \
	-i -e '/^mrvl\/prestera/d' \
	-i -e '/^mrvl\/sd8787/d' \
	-i -e '/^mt76/d' \
	-i -e '/^netronome/d' \
	-i -e '/^nxp/d' \
	-i -e '/^qca/d' \
	-i -e '/^qcom/d' \
	-i -e '/^qed/d' \
	-i -e '/^radeon/d' \
	-i -e '/^rtl_bt/d' \
	-i -e '/^rtlwifi/d' \
	-i -e '/^rtw88/d' \
	-i -e '/^rtw89/d' \
	-i -e '/^sms1xxx/d' \
	-i -e '/^tdmb/d' \
	-i -e '/^ti-connectivity/d' \
	-i -e '/^v4l-cx2/d' \
	linux-firmware.files
sed -i -e 's!^!/usr/lib/firmware/!' linux-firmware.{files,dirs}
sed -i -e 's/^/"/;s/$/"/' linux-firmware.files
sed -e 's/^/%%dir /' linux-firmware.dirs >> linux-firmware.files


%files -f linux-firmware.files
%dir %{_firmwarepath}
%license LICENCE.* LICENSE.* GPL*

%files whence
%license WHENCE

# GPU firmwares
%files -n amd-gpu-firmware
%license LICENSE.radeon LICENSE.amdgpu LICENSE.amdnpu
%{_firmwarepath}/amdgpu/
%{_firmwarepath}/amdnpu/
%{_firmwarepath}/radeon/

%files -n intel-gpu-firmware
%license LICENSE.i915
%{_firmwarepath}/i915/

%files -n nvidia-gpu-firmware
%license LICENCE.nvidia
%dir %{_firmwarepath}/nvidia/
%{_firmwarepath}/nvidia/a*/
%{_firmwarepath}/nvidia/g*/
%{_firmwarepath}/nvidia/tu*/

# Microcode updates
%files -n amd-ucode-firmware
%license LICENSE.amd-ucode
%{_firmwarepath}/amd/
%{_firmwarepath}/amdtee/
%{_firmwarepath}/amd-ucode/

# WiFi/Bluetooth firmwares
%files -n atheros-firmware
%license LICENCE.atheros_firmware
%license LICENSE.QualcommAtheros_ar3k
%license LICENSE.QualcommAtheros_ath10k
%license LICENCE.open-ath9k-htc-firmware
%license qca/NOTICE.txt
%{_firmwarepath}/ar3k/
%{_firmwarepath}/ath6k/
%{_firmwarepath}/ath9k_htc/
%{_firmwarepath}/ath10k/
%{_firmwarepath}/ath11k/
%{_firmwarepath}/ath12k/
%{_firmwarepath}/qca/

%files -n brcmfmac-firmware
%license LICENCE.broadcom_bcm43xx
%license LICENCE.cypress
%{_firmwarepath}/brcm/
%{_firmwarepath}/cypress/

%files -n iwlegacy-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-3945-*.ucode*
%{_firmwarepath}/iwlwifi-4965-*.ucode*

%files -n iwlwifi-dvm-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-100-*.ucode*
%{_firmwarepath}/iwlwifi-105-*.ucode*
%{_firmwarepath}/iwlwifi-135-*.ucode*
%{_firmwarepath}/iwlwifi-1000-*.ucode*
%{_firmwarepath}/iwlwifi-2000-*.ucode*
%{_firmwarepath}/iwlwifi-2030-*.ucode*
%{_firmwarepath}/iwlwifi-5000-*.ucode*
%{_firmwarepath}/iwlwifi-5150-*.ucode*
%{_firmwarepath}/iwlwifi-6000-*.ucode*
%{_firmwarepath}/iwlwifi-6000g2a-*.ucode*
%{_firmwarepath}/iwlwifi-6000g2b-*.ucode*
%{_firmwarepath}/iwlwifi-6050-*.ucode*

%files -n iwlwifi-mvm-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-3160-*.ucode*
%{_firmwarepath}/iwlwifi-3168-*.ucode*
%{_firmwarepath}/iwlwifi-7260-*.ucode*
%{_firmwarepath}/iwlwifi-7265-*.ucode*
%{_firmwarepath}/iwlwifi-7265D-*.ucode*
%{_firmwarepath}/iwlwifi-8000C-*.ucode*
%{_firmwarepath}/iwlwifi-8265-*.ucode*
%{_firmwarepath}/iwlwifi-9000-*.ucode*
%{_firmwarepath}/iwlwifi-9260-*.ucode*
%{_firmwarepath}/iwlwifi-cc-a0-*.ucode*
%{_firmwarepath}/iwlwifi-gl-c0*
%{_firmwarepath}/iwlwifi-ma-b0*
%{_firmwarepath}/iwlwifi-Qu*.ucode*
%{_firmwarepath}/iwlwifi-ty-a0*
%{_firmwarepath}/iwlwifi-so-a0*
%{_firmwarepath}/iwlwifi-bz-b0*

%files -n libertas-firmware
%license LICENCE.Marvell LICENCE.OLPC
%dir %{_firmwarepath}/libertas
%dir %{_firmwarepath}/mrvl
%{_firmwarepath}/libertas/*
%{_firmwarepath}/mrvl/sd8787*

%files -n mt7xxx-firmware
%license LICENCE.mediatek
%license LICENCE.ralink_a_mediatek_company_firmware
%dir %{_firmwarepath}/mediatek
%{_firmwarepath}/mediatek/mt76*
%{_firmwarepath}/mediatek/mt79*
%{_firmwarepath}/mediatek/BT*
%{_firmwarepath}/mediatek/WIFI*
%{_firmwarepath}/mt76*

%files -n nxpwireless-firmware
%license LICENSE.nxp
%dir %{_firmwarepath}/nxp
%{_firmwarepath}/nxp/*

%files -n realtek-firmware
%license LICENCE.rtlwifi_firmware.txt
%{_firmwarepath}/rtl_bt/
%{_firmwarepath}/rtlwifi/
%{_firmwarepath}/rtw88/
%{_firmwarepath}/rtw89/

%files -n tiwilink-firmware
%license LICENCE.ti-connectivity
%dir %{_firmwarepath}/ti-connectivity/
%{_firmwarepath}/ti-connectivity/*

# SMART NIC and network switch firmwares
%files -n liquidio-firmware
%license LICENCE.cavium_liquidio
%dir %{_firmwarepath}/liquidio
%{_firmwarepath}/liquidio/*

%files -n mrvlprestera-firmware
%license LICENCE.Marvell
%dir %{_firmwarepath}/mrvl/prestera
%{_firmwarepath}/mrvl/prestera/*

%files -n mlxsw_spectrum-firmware
%dir %{_firmwarepath}/mellanox/
%{_firmwarepath}/mellanox/*

%files -n netronome-firmware
%license LICENCE.Netronome
%dir %{_firmwarepath}/netronome
%{_firmwarepath}/netronome/*

%files -n qed-firmware
%dir %{_firmwarepath}/qed
%{_firmwarepath}/qed/*

# Silicon Vendor specific
%files -n qcom-firmware
%license LICENSE.qcom LICENSE.qcom_yamato qcom/NOTICE.txt
%dir %{_firmwarepath}/qcom
%{_firmwarepath}/qcom/*
%{_firmwarepath}/a300_p*

# Vision and ISP hardware
%files -n intel-vsc-firmware
%license LICENSE.ivsc
%dir %{_firmwarepath}/intel/ipu/
%dir %{_firmwarepath}/intel/vsc/
%{_firmwarepath}/intel/ipu3-fw.bin*
%{_firmwarepath}/intel/irci_irci_ecr-master_20161208_0213_20170112_1500.bin*
%{_firmwarepath}/intel/ipu/*
%{_firmwarepath}/intel/vsc/*

# Sound codec hardware
%files -n cirrus-audio-firmware
%license LICENSE.cirrus
%dir %{_firmwarepath}/cirrus
%{_firmwarepath}/cirrus/*

%files -n intel-audio-firmware
%license LICENCE.adsp_sst LICENCE.IntcSST2
%dir %{_firmwarepath}/intel/
%dir %{_firmwarepath}/intel/avs/
%dir %{_firmwarepath}/intel/catpt/
%{_firmwarepath}/intel/avs/*
%{_firmwarepath}/intel/catpt/*
%{_firmwarepath}/intel/dsp_fw*
%{_firmwarepath}/intel/fw_sst*

# Random other hardware
%files -n dvb-firmware
%license LICENSE.dib0700 LICENCE.it913x LICENCE.siano
%license LICENCE.xc4000 LICENCE.xc5000 LICENCE.xc5000c
%dir %{_firmwarepath}/av7110/
%{_firmwarepath}/av7110/*
%{_firmwarepath}/as102_data*
%{_firmwarepath}/cmmb*
%{_firmwarepath}/dvb*
%{_firmwarepath}/isdbt*
%{_firmwarepath}/lgs8g75*
%{_firmwarepath}/sms1xxx*
%{_firmwarepath}/tdmb*
%{_firmwarepath}/v4l-cx2*

%changelog
* Tue Feb 11 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 20250211-1
- Update to 20250211
- i915: Update Xe2LPD DMC to v2.28
- ASoC: tas2781: Add regbin firmware by index for single device
- rtl_bt: Update RTL8852B BT USB FW to 0x0474_842D
- iwlwifi: add Bz/gl/ty/So/Ma FW for core93-123 release
- iwlwifi: update cc/Qu/QuZ firmwares for core93-82 release
- ASoC: tas2781: Add dsp firmware for new projects
- amdgpu: DMCUB update for DCN401
- ath12k: WCN7850 hw2.0: update board-2.bin
- ath12k: QCN9274 hw2.0: update to WLAN.WBE.1.4.1-00199-QCAHKSWPL_SILICONZ-1
- ath12k: QCN9274 hw2.0: update board-2.bin
- ath11k: WCN6750 hw1.0: update board-2.bin
- ath11k: QCN9074 hw1.0: update to WLAN.HK.2.9.0.1-02146-QCAHKSWPL_SILICONZ-1
- ath11k: QCA6698AQ hw2.1: add to WLAN.HSP.1.1-04479-QCAHSPSWPL_V1_V2_SILICONZ_IOE-1
- ath11k: QCA6698AQ hw2.1: add board-2.bin
- ath11k: QCA6390 hw2.0: update board-2.bin
- ath11k: QCA2066 hw2.1: update to WLAN.HSP.1.1-03926.13-QCAHSPSWPL_V2_SILICONZ_CE-2.52297.6
- ath11k: QCA2066 hw2.1: update board-2.bin
- ath11k: IPQ8074 hw2.0: update to WLAN.HK.2.9.0.1-02146-QCAHKSWPL_SILICONZ-1
- ath11k: IPQ6018 hw1.0: update to WLAN.HK.2.7.0.1-02409-QCAHKSWPL_SILICONZ-1
- ath11k: add device-specific firmware for QCM6490 boards
- qca: add more WCN3950 1.3 NVM files
- qca: add firmware for WCN3950 chips
- qca: move QCA6390 firmware to separate section
- qca: restore licence information for WCN399x firmware
- qca: Update Bluetooth WCN6750 1.1.0-00476 firmware to 1.1.3-00069
- qcom:x1e80100: Support for Lenovo T14s G6 Qualcomm platform
- Update FW files for MRVL SD8997 chips
- i915: Update Xe2LPD DMC to v2.27
- qca: Update Bluetooth WCN6856 firmware 2.1.0-00642 to 2.1.0-00650
- rtl_bt: Update RTL8852B BT USB FW to 0x049B_5037
- amdgpu: Update ISP FW for isp v4.1.1
- QCA: Add Bluetooth firmware for QCA6698
- amlogic: update firmware for w265s2
- mediatek MT7925: update bluetooth firmware to 20250113153307
- update firmware for MT7925 WiFi device
- amdgpu: LOTS of firmware updates
- qcom: update SLPI firmware for RB5 board
- amdgpu: DMCUB updates for various AMDGPU ASICs
- qcom: add DSP firmware for SA8775p platform
- qcom: correct venus firmware versions
- qcom: add missing version information
- Update firmware (v10) for mt7988 internal
- iwlwifi: add Bz FW for core90-93 release
- wilc3000: add firmware for WILC3000 WiFi device
- rtw89: 8852b: update fw to v0.29.29.8
- rtw89: 8852c: update fw to v0.27.122.0
- rtw89: 8922a: update fw to v0.35.54.0
- rtw89: 8852bt: update fw to v0.29.110.0
- rtw89: 8852b: update fw to v0.29.29.7
- cirrus: cs35l56: Correct some links to address the correct amp instance
- Update firmware file for Intel Bluetooth Magnetar/BlazarU/Solar core

* Fri Jan 10 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 20250109-1
- Update to 20250109
- cirrus: cs35l41: Add Firmware for Ayaneo system 1f660105
- rtl_bt: Add separate config for RLT8723CS Bluetooth part
- amdgpu: revert some firmwares
- WHENCE: Link the Raspberry Pi CM5 and 500 to the 4B
- Add support to install files/symlinks in parallel.
- rtl_bt: Update RTL8852B BT USB FW to 0x04BE_1F5E
- cnm: update chips&media wave521c firmware.
- rtl_nic: add firmware rtl8125bp-2
- qcom: venus-5.4: update firmware binary for sc7180 and qcs615
- cirrus: cs35l56: Correct filenames of SSID 17aa3832
- cirrus: cs35l56: Add and update firmware for various Cirrus CS35L54/CS35L56 laptops
- cirrus: cs35l56: Correct SSID order for 103c8d01 103c8d08 10431f43
- rtl_nic: add firmware rtl8125d-2

* Tue Dec 10 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 20241210-1
- Update to upstream 20241210
- Update firmware file for Intel BlazarU core
- amdgpu: numerous firmware updates
- upstream amdnpu firmware
- QCA: Add Bluetooth nvm files for WCN785x
- i915: Update Xe2LPD DMC to v2.24
- cirrus: cs35l56: Add firmware for Cirrus CS35L56 for various Dell laptops
- iwlwifi: add Bz-gf FW for core89-91 release
- QCA: Update Bluetooth WCN785x firmware to 2.0.0-00515-2
- ice: update ice DDP wireless_edge package to 1.3.20.0
- ice: update ice DDP comms package to 1.3.52.0
- ice: update ice DDP package to ice-1.3.41.0
- amdgpu: update DMCUB to v9.0.10.0 for DCN314/DCN351
- Update AMD cpu microcode
- xe: Update GUC to v70.36.0 for BMG, LNL
- i915: Update GUC to v70.36.0 for ADL-P, DG1, DG2, MTL, TGL
- iwlwifi: add Bz-gf FW for core91-69 release
- qcom: venus-5.4: add venus firmware file for qcs615
- qcom: update venus firmware file for SC7280
- QCA: Add 22 bluetooth firmware nvm files for QCA2066
- mediatek MT7921/MT7922: update bluetooth firmware
- update for MT7921/MT7922 WiFi device
- qcom: Add QDU100 firmware image files.
- qcom: Update aic100 firmware files

* Mon Nov 11 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 20241110-1
- Update to upstream 20241110
- rtl_bt: Update RTL8852BT/RTL8852BE-VT BT USB FW to 0x04D7_63F7
- cnm: update chips&media wave521c firmware.
- MT7920: update WiFi/bluetooth firmware
- copy-firmware.sh: Run check_whence.py only if in a git repo
- cirrus: cs35l56: Add firmware for Cirrus CS35L56 for various Dell laptops
- amdgpu: update DMCUB to v9.0.10.0 for DCN351
- rtw89: 8852a: update fw to v0.13.36.2
- rtw88: Add firmware v52.14.0 for RTL8812AU
- i915: Update Xe2LPD DMC to v2.23
- MT7925: update WiFi/bluetooth firmware
- WHENCE: Add sof-tolg for mt8195
- Update firmware file for Intel BlazarI core
- qcom: Add link for QCS6490 GPU firmware
- qcom: update gpu firmwares for qcs615 chipset
- cirrus: cs35l56: Update firmware for Cirrus Amps for some HP laptops
- ath11k: move WCN6750 firmware to the device-specific subdir
- xe: Update LNL GSC to v104.0.0.1263
- i915: Update MTL/ARL GSC to v102.1.15.1926
- amdgpu: DMCUB updates for various AMDGPU ASICs
- mediatek: Add sof-tolg for mt8195
- i915: Add Xe3LPD DMC
- Add firmware for Cirrus CS35L41
- Update firmware file for Intel BlazarU core
- Makefile: error out of 'install' if COPYOPTS is set
- check_whence.py: skip some validation if git ls-files fails
- qcom: Add Audio firmware for X1E80100 CRD/QCPs
- amdgpu: DMCUB updates forvarious AMDGPU ASICs
- brcm: replace NVRAM for Jetson TX1

* Sat Oct 19 2024 Adam Williamson <awilliam@redhat.com> - 20241017-2
- Fix compression / deduplication for upstream changes in 20241017

* Thu Oct 17 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 20241017-1
- Update to upstream 20241017
- rtlwifi: Update firmware for RTL8192FU to v7.3
- Remove execute bit from firmware files
- rtl_nic: add firmware rtl8125d-1
- iwlwifi: add gl/Bz FW for core91-69 release
- iwlwifi: update ty/So/Ma firmwares for core91-69 release
- iwlwifi: update cc/Qu/QuZ firmwares for core91-69 release
- cirrus: cs35l56: Add firmware for Cirrus CS35L56 for somt7996me ASUS/HP/Lenovo Laptops
- update firmware for en8811h 2.5G ethernet phy
- mtk_wed: add firmware for mt7988 Wireless Ethernet Dispatcher
- ath12k: WCN7850 hw2.0: update board-2.bin
- ath12k: QCN9274 hw2.0: add to WLAN.WBE.1.3.1-00162-QCAHKSWPL_SILICONZ-1
- ath12k: QCN9274 hw2.0: add board-2.bin
- Add a link from TAS2XXX1EB3.bin -> ti/tas2781/TAS2XXX1EB30.bin
- tas2781: Upload dsp firmware for ASUS laptop 1EB30 & 1EB31
- rtlwifi: Add firmware v39.0 for RTL8192DU
- Revert "ath12k: WCN7850 hw2.0: update board-2.bin"
- QCA: Add Bluetooth firmwares for WCN785x with UART transport
- amdgpu: DMCUB DCN35 update
- brcm: Add BCM4354 NVRAM for Jetson TX1
- brcm: Link FriendlyElec NanoPi M4 to AP6356S nvram
- add firmware for MediaTek Bluetooth chip (MT7920)
- add firmware for MT7920
- amdgpu: update numerous firmware
- qcom: update gpu firmwares for qcm6490 chipset
- mt76: mt7996: add firmware files for mt7992/mt7996 chipset variants
- qcom: add gpu firmwares for sa8775p chipset
- rtw89: 8922a: add fw format-2 v0.35.42.1
- WHENCE: Fix battmgr.jsn entry type
- qcom: qcm6490: add ADSP and CDSP firmware
- Update firmware file for various Intel Bluetooth
- rtl_bt: Update RTL8852B BT USB FW to 0x0447_9301
- realtek: rt1320: Add patch firmware of MCU

* Mon Sep  9 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 20240909-1
- Update to upstream 20240909
- i915: Update MTL DMC v2.23
- cirrus: cs35l56: Add firmware for Cirrus CS35L54 for some HP laptops
- amdgpu: Revert sienna cichlid dmcub firmware update
- iwlwifi: add Bz FW for core89-58 release
- rtl_nic: add firmware rtl8126a-3
- update  MT7921 WiFi/bluetooth device firmware
- amdgpu: update DMCUB to v0.0.232.0 for DCN314 and DCN351
- amdgpu: DMCUB updates forvarious AMDGPU ASICs
- rtw89: 8922a: add fw format-1 v0.35.41.0
- update  MT7925 WiFi/bluetooth device firmware
- rtl_bt: Add firmware and config files for RTL8922A
- rtl_bt: Add firmware file for the the RTL8723CS Bluetooth part
- rtl_bt: de-dupe identical config.bin files
- rename rtl8723bs_config-OBDA8723.bin -> rtl_bt/rtl8723bs_config.bin
- Update AMD SEV firmware
- update firmware for MT7996
- Revert "i915: Update MTL DMC v2.22"
- ath12k: WCN7850 hw2.0: update board-2.bin
- ath11k: WCN6855 hw2.0: update to WLAN.HSP.1.1-03125-QCAHSPSWPL_V1_V2_SILICONZ_LITE-3.6510.41
- ath11k: WCN6855 hw2.0: update board-2.bin
- ath11k: QCA2066 hw2.1: add to WLAN.HSP.1.1-03926.13-QCAHSPSWPL_V2_SILICONZ_CE-2.52297.3
- ath11k: QCA2066 hw2.1: add board-2.bin
- ath11k: IPQ5018 hw1.0: update to WLAN.HK.2.6.0.1-01291-QCAHKSWPL_SILICONZ-1
- qcom: vpu: add video firmware for sa8775p
- amdgpu: DMCUB updates for various AMDGPU ASICs

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 20240811-3
- convert license to SPDX

* Fri Aug 16 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 20240811-2
- Delete intel sound topology files - duped in alsa-sof-firmware

* Mon Aug 12 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 20240811-1
- Update to upstream 20240811
- qcom: update path for video firmware for vpu-1/2/3.0
- QCA: Update Bluetooth WCN685x 2.1 firmware to 2.1.0-00642
- rtw89: 8852c: add fw format-1 v0.27.97.0
- rtw89: 8852bt: add firmware 0.29.91.0
- amdgpu: A lot of firmware updates
- mediatek: Update mt8195 SOF firmware
- xe: First GuC release v70.29.2 for BMG
- xe: Add GuC v70.29.2 for LNL
- i915: Add GuC v70.29.2 for ADL-P, DG1, DG2, MTL, and TGL
- i915: Update MTL DMC v2.22, MTL GSC to v102.0.10.1878
- xe: Add BMG HuC 8.2.10, GSC 104.0.0.1161 for LNL, LNL HuC 9.4.13
- i915: update DG2 HuC to v7.10.16
- QCA: Update Bluetooth QCA2066 firmware to 2.1.0-00641
- update firmware for MT7921/MT7922 WiFi device
- update firmware for mediatek bluetooth chip (MT7921/MT7922)
- iwlwifi: add gl FW for core89-58 release
- iwlwifi: update cc/Qu/QuZ firmwares for core89-58 release
- mediatek: Update mt8195 SOF firmware and sof-tplg
- ASoC: tas2781: fix the license issue for tas781 firmware
- rtl_bt: Update RTL8852B BT USB FW to 0x048F_4008
- i915: Update Xe2LPD DMC to v2.21
- qcom: move signed x1e80100 signed firmware to the SoC subdir
- qcom: add video firmware file for vpu-3.0
- amdgpu: update DMCUB to v0.0.225.0 for Various AMDGPU Asics
- qcom: add gpu firmwares for x1e80100 chipset
- add firmware for qat_402xx devices
- Update AMD cpu microcode
- intel: avs: Add numerous sound topology files
- Add a copy of Apache-2.0
- intel: avs: Update AudioDSP base firmware for APL-based platforms

* Wed Jul 10 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 20240709-1
- Update to upstream 20240709
- Add ISH firmware file for Intel Lunar Lake platform
- amdgpu: update DMCUB to v0.0.224.0 for Various AMDGPU Asics
- cirrus: cs35l41: Update various firmware for ASUS laptops using CS35L41
- amdgpu: Update ISP FW for isp v4.1.1
- mediatek: Update MT8173 VPU firmware to v1.2.0
- qcom: Add AIC100 firmware files
- amlogic: Update bluetooth firmware binary
- Various Intel Bluetooth firmware updates
- rtl_bt: Update RTL8822C BT UART/USB firmware
- amdgpu: update DMCUB to v0.0.222.0 for DCN314
- iwlwifi: add ty/So/Ma firmwares for core88-87 release
- iwlwifi: update cc/Qu/QuZ firmwares for core88-87 release
- add new cc33xx firmware for TI cc33xx WiFi chips
- cirrus: cs35l56: Update firmware for Cirrus CS35L56 for various ASUS laptops
