# DarkForge UI

**DarkForge UI** is a modern firmware for devices based on **ESP32-S3** and **ESP32-P4** microcontrollers.

<p align="center">
 <img width="200px" src="public/docs/images/1.jpg">
 <img width="200px" src="public/docs/images/2.jpg">
 <img width="200px" src="public/docs/images/3.jpg">
 <img width="200px" src="public/docs/images/4.jpg">
 <img width="200px" src="public/docs/images/5.jpg">
 <img width="200px" src="public/docs/images/6.jpg">
</p>


It brings the **Home Assistant** ecosystem together with a smooth, intuitive touch interface. Customize your screens with dozens of functional widgets and manage your home with a single touch.

Get started in minutes — the firmware can be installed directly from your browser.

> DarkForge UI is currently in beta. Some features, supported devices, translations, and UI components may change as the project evolves.

---

## Features

- Convenient touch interface optimized for compact screens
- Dashboard pages with customizable cards
- Basic and advanced cards for supported entity domains
- Web-based configuration
- **“Local first” philosophy**: the firmware does not require internet access for normal operation
- Support for various display orientations and layouts
- Entity-related cards: media, weather, camera, sensor, switch, light, and more

---

## Supported Devices

The list of supported devices may vary depending on the firmware version.

Support for new devices will be added gradually. Check the project website for the latest available firmware versions and the current list of supported models.

---

## License and Trial Period

DarkForge UI uses a license key model.

A trial period is provided, during which you can set up your device and evaluate the firmware’s functionality.

The license key:

- is tied to the device identifier
- is stored in the device memory
- does **not** use E-FUSE
- does **not** permanently lock the device
- is valid indefinitely once issued

If you completely erase the device’s flash memory or NVS, you will need to re-enter the license key.

After a full flash erase, you can install another compatible firmware.

---

## Local Operation and Privacy

DarkForge UI is designed for local smart home control.

The firmware does not send your data to external servers during normal operation. Communication with Home Assistant is intended to work within your local network.

Additional online services may be added in the future, but they are not required for basic local functionality.

Remember that overall security depends not only on the firmware, but also on:

- your local network configuration
- router settings
- Home Assistant configuration
- token permissions
- firewall rules and remote access settings

No system can guarantee absolute security, so network-level protection is very important.

---

## Camera Setup

For proper camera operation, it is recommended to configure a camera sub-stream in **MJPEG** format.

Many cameras provide multiple streams:

- main stream — higher resolution, often H.264/H.265
- sub-stream — lower resolution, usually more suitable for embedded devices

For DarkForge UI, the sub-stream is generally the best option.

### Recommended Camera Requirements

For the best results:

- use the camera’s sub-stream
- configure the sub-stream as **MJPEG**
- choose a resolution that matches your target display
- avoid streams with very high bitrates
- ensure Home Assistant can reliably access the stream

### Home Assistant Configuration Example

Create or update a camera entity in your Home Assistant `configuration.yaml` file:

```
camera:
  - platform: ffmpeg
    name: "Test Camera"
    input: "rtsp://admin:admin@192.168.1.47:554/Streaming/Channels/102"
    extra_arguments: "-q:v 5 -r 15"
```

After changing `configuration.yaml`, restart Home Assistant or reload the relevant integration if your configuration supports it.

---

## Known Issues

The following are known limitations of the current beta version. They do not necessarily appear on all devices and may be fixed or improved in future updates.

### Character Display in Some Translations

In certain localizations, some characters may be displayed incorrectly or fail to load.

For example, this issue may occur in the German translation due to missing glyphs in the font set used.

Possible manifestations:

- missing characters
- empty squares instead of letters
- incorrect display of special characters

### Weather Forecast Card Loading After Startup

After the device starts up, the weather forecast card may not appear immediately.

If the forecast fails to load at startup, it should refresh automatically during the next data update cycle.

Estimated update time: **up to 10 minutes**.