---
id: TC-FA-PREF-E2E-006-tooltip-ikon-info-setting-set-01-sampai-set-07
title: "Tooltip Ikon Info ⓘ Setting SET-01 sampai SET-07"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-29
  - TC-FA-PREF-30
  - TC-FA-PREF-31
  - TC-FA-PREF-32
  - TC-FA-PREF-33
  - TC-FA-PREF-34
  - TC-FA-PREF-35
coverage:
  web: automated
---

# Tooltip Ikon Info ⓘ Setting SET-01 sampai SET-07

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup (hanya dibaca, tidak diubah): Preferences nilai awal PA-2, tidak terkunci, semua setting wajib terisi. Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-29: Tooltip Fiscal Year Start (SET-01)

1. Hover ikon ⓘ di sebelah label "Fiscal Year Start"
2. Verifikasi tooltip tampil dengan teks persis: "The month your company's financial year starts every year. Can be changed until depreciation is posted or a period is closed."

### TC-FA-PREF-30: Tooltip Default Capitalization Threshold (SET-02)

3. Hover ikon ⓘ di sebelah label "Default Capitalization Threshold"
4. Verifikasi tooltip tampil dengan teks persis: "Purchases at or above this amount are recorded as fixed assets. Lower amounts are suggested to be expensed. Used when an asset class has no threshold of its own."

### TC-FA-PREF-31: Tooltip In-service Date Source (SET-03)

5. Hover ikon ⓘ di sebelah label "In-service Date Source"
6. Verifikasi tooltip tampil dengan teks persis: "When depreciation starts. Activation date: the date the asset first moves to an operational status. Manual: Accounting enters the date on each asset. Changes apply to new assets only."

### TC-FA-PREF-32: Tooltip Depreciation in Disposal Month (SET-04)

7. Hover ikon ⓘ di sebelah label "Depreciation in Disposal Month"
8. Verifikasi tooltip tampil dengan teks persis: "Whether the disposal month is still depreciated. Daily prorata depreciates it by days up to the disposal date. Applies to disposals posted after this change."

### TC-FA-PREF-33: Tooltip Default Gain on Disposal (SET-05)

9. Hover ikon ⓘ di sebelah label "Default Gain on Disposal"
10. Verifikasi tooltip tampil dengan teks persis: "Account for gains when an asset is sold above its book value. Used when an asset class has no gain account. If no gain account is available, the disposal journal is held at export."

### TC-FA-PREF-34: Tooltip Default Loss on Disposal (SET-06)

11. Hover ikon ⓘ di sebelah label "Default Loss on Disposal"
12. Verifikasi tooltip tampil dengan teks persis: "Account for losses when an asset is sold below book value, scrapped, lost or written off. Can be the same account as Gain. If no loss account is available, the disposal journal is held at export."

### TC-FA-PREF-35: Tooltip Disposal Documents (SET-07)

13. Hover ikon ⓘ di sebelah label "Disposal Documents"
14. Verifikasi tooltip tampil dengan teks persis: "Choose whether a supporting document is required or optional for each disposal type. Required documents must be attached before the disposal can be submitted."

## Notes

- Layar Preferences dibuka hook `beforeEach` suite, sehingga langkah TC "Buka Tab Preferences" tidak diulang. Tooltip diasersi tepat setelah hover (8b butir 5); hover berikutnya memindahkan kursor ke ikon lain.
- Urutan TC dalam spec: TC-FA-PREF-29 sampai 35 sesuai urutan setting SET-01 sampai SET-07. Spec tidak mengubah Preferences; form tidak dirty di akhir spec.
- Temuan untuk QA: tidak ada temuan pada TC sumber spec ini.
