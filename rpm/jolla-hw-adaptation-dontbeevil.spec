Name: jolla-hw-adaptation-dontbeevil
Summary: Jolla HW Adaptation dontbeevil
Version: 0.0.1
Release: 1
License: BSD-3-Clause
Source: %{name}-%{version}.tar.gz

Requires: qt5-plugin-generic-evdev

 # bluetooth tools
Requires: bluez5-tools
Requires: bluetooth-rfkill-event-hciattach

# Vibra
Requires: ngfd-plugin-native-vibrator
Requires: qt5-feedback-haptics-native-vibrator

# Sensors
Requires: hybris-libsensorfw-qt5

Requires: pulseaudio-modules-droid
Requires: pulseaudio-modules-droid-glue

# for audio recording to work:
Requires: qt5-qtmultimedia-plugin-mediaservice-gstmediacapture

# These need to be per-device due to differing backends (fbdev, eglfs, hwc, ..?)
Requires: qt5-qtwayland-wayland_egl
Requires: qt5-qpa-hwcomposer-plugin
Requires: qtscenegraph-adaptation

# Add GStreamer v1.0 as standard
Requires: gstreamer1.0
Requires: gstreamer1.0-plugins-good
Requires: gstreamer1.0-plugins-base
Requires: gstreamer1.0-plugins-bad
Requires: nemo-gstreamer1.0-interfaces
Requires: gstreamer1.0-droid

# This is needed for notification LEDs
Requires: mce-plugin-libhybris

## USB mode controller
## Enables mode selector upon plugging USB cable:
Requires: usb-moded
#Requires: usb-moded-defaults-android
Requires: usb-moded-developer-mode-android

Requires: rfkill

# enable device lock and allow to select untrusted software
Requires: jolla-devicelock-plugin-encsfa

# For GPS
Requires: gpsd
Requires: geoclue

# For mounting SD card automatically
Requires: sd-utils

Requires: droid-hal-kernel-donebeevil
Requires: droid-config-donebeevil-sailfish
Requires: droid-config-donebeevil-pulseaudio-settings
Requires: droid-config-donebeevil-policy-settings
Requires: droid-config-donebeevil-preinit-plugin
Requires: droid-config-donebeevil-bluez5
Requires: droid-hal-version-donebeevil
#Requires: droid-config-donebeevil-flashing

%description
Meta package to install packages for dontbeevil HW Adaptation
%files
 
