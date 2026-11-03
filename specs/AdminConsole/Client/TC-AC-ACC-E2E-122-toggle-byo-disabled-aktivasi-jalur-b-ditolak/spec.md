---
id: TC-AC-ACC-E2E-122-toggle-byo-disabled-aktivasi-jalur-b-ditolak
title: "Toggle BYO Disabled: Aktivasi Device Jalur B di Global Settings Hardware Ditolak dan Jalur A Tetap Berhasil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-255
coverage:
  web: automated
---

# Toggle BYO Disabled: Aktivasi Device Jalur B di Global Settings Hardware Ditolak dan Jalur A Tetap Berhasil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup: C-01 `PT Sejahtera Abadi` dengan toggle "Allow Self-Purchased Device Activation" Disabled (kondisi awal; hook `before` memastikan Disabled lewat Fixture BE yang disediakan tim FE/BE). Spec ini tidak mengubah toggle.
- Kemampuan teknis (hardware berisiko, spec sendiri): perangkat atau simulator device BYO (Jalur B, tidak dikirim melalui rantai distribusi) dan device resmi (Jalur A) untuk aktivasi di Global Settings > Hardware tenant `PT Sejahtera Abadi`; disediakan tim FE. Device hasil aktivasi Jalur A dibersihkan oleh hook `after` lewat Fixture BE (disediakan tim FE/BE).
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client dan Detail disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-255: Toggle Disabled: aktivasi Jalur B di Global Settings ditolak; Jalur A tetap bisa

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name `PT Sejahtera Abadi` lalu lihat Section Settings
3. Verifikasi toggle "Allow Self-Purchased Device Activation" Disabled
4. Aktivasi device BYO (Jalur B) di Global Settings > Hardware tenant `PT Sejahtera Abadi`
5. Verifikasi aktivasi Jalur B ditolak
6. Aktivasi device resmi (Jalur A) di Global Settings > Hardware tenant `PT Sejahtera Abadi`
7. Verifikasi aktivasi Jalur A berhasil

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`.
- Langkah 1 sampai 3 menegakkan precondition TC ("Pastikan toggle Disabled"): langkah 3 adalah asersi precondition yang dicatat sebagai langkah penghubung (S-03) agar hasil Jalur B bermakna.
- Post Condition TC-AC-ACC-255: `-`.
- Temuan untuk QA:
  - TC-AC-ACC-255 tidak menyebut pesan penolakan atau indikator penolakan Jalur B, dan tidak menyebut indikator keberhasilan Jalur A; spec menegakkan asersi sebatas "ditolak" dan "berhasil" sesuai Expected, dan tim FE perlu menentukan elemen UI-nya di tahap script.
  - TC-AC-ACC-255 tidak menyebut Post Condition untuk device Jalur A yang teraktivasi; pembersihan dilakukan di hook `after`.
  - TC-AC-ACC-255 berlabel "Manual Only: perangkat hardware" sehingga kemampuan simulasi hardware menjadi kebutuhan tim FE (bagian 2 konvensi).
