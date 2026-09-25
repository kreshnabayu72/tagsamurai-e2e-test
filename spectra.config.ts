import { defineConfig } from "@testspectra/cli";

export default defineConfig({
  webConfig: {
    baseUrl: "http://localhost:5180",
    maxConcurrentSessions: "1",
    headless: true,
    implicitWait: "5000",
    parallelizationMode: "testcase",
    // Failure-only video recording (default: true)
    video: true,
  },
  androidConfig: {
    driverServer: "tcp://127.0.0.1:8200",
    appPackage: "dev.testspectra.demoapp",
    appActivity: "dev.testspectra.demoapp.MainActivity",
    noReset: false,
    implicitWait: "10000",
    parallelizationMode: "suite",
    // Failure-only video recording (default: true)
    video: true,
    devices: [
      {
        id: "emulator-5554",
        name: "Pixel 8a Emulator",
        version: "14.0",
        systemPort: 8200,
      },
    ],
  },
  iosConfig: {
    appiumServer: "http://127.0.0.1:4723",
    automationName: "XCUITest",
    bundleId: "",
    autoAcceptAlerts: true,
    noReset: false,
    implicitWait: "10000",
    parallelizationMode: "suite",
    devices: [
      {
        id: "iphone-15-pro",
        name: "iPhone 15 Pro Simulator",
        version: "17.0",
        udid: "auto",
        wdaLocalPort: 8100,
      },
    ],
  },
  executionConfig: {
    networkMonitoringEnabled: true,
    fastResponseTime: "200",
    normalResponseTime: "1000",
    monitoredDomains: [],
    environmentVariables: { DEMO_API_MODE: "sandbox" },
    // Demo plugin: registers Spectra.findComponent() / Spectra.findButton() commands.
    plugins: ["@testspectra/plugin-demo"],
  },
});
