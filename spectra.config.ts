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
    // Secrets come from the runner's environment (see .env.example); never commit values.
    environmentVariables: {
      DEMO_API_MODE: "sandbox",
      GS_TC_PASSWORD: process.env.GS_TC_PASSWORD ?? "",
      AC_TC_PASSWORD: process.env.AC_TC_PASSWORD ?? "",
      ACT_PASSWORD: process.env.ACT_PASSWORD ?? "",
      ACT_PASSWORD_ALT: process.env.ACT_PASSWORD_ALT ?? "",
      ACT_PASSWORD_72: process.env.ACT_PASSWORD_72 ?? "",
      ACT_PASSWORD_SPECIAL: process.env.ACT_PASSWORD_SPECIAL ?? "",
    },
    // Demo plugin: registers Spectra.findComponent() / Spectra.findButton() commands.
    plugins: ["@testspectra/plugin-demo"],
  },
});
