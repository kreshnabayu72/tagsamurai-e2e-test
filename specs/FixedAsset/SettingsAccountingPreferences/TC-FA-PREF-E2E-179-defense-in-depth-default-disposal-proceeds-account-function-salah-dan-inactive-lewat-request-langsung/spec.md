---
id: TC-FA-PREF-E2E-179-defense-in-depth-default-disposal-proceeds-account-function-salah-dan-inactive-lewat-request-langsung
title: "Defense-in-Depth: Default Disposal Proceeds Account dengan Akun Function di Luar Disposal Proceeds atau Inactive Ditolak Server Lewat Request Langsung"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-627
  - TC-FA-PREF-628
coverage:
  web: automated
---

# Defense-in-Depth: Default Disposal Proceeds Account dengan Akun Function di Luar Disposal Proceeds atau Inactive Ditolak Server Lewat Request Langsung

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI dan sesi API: Total Control "Rina Anggraini" `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Request langsung dan pembacaan ulang memakai sesi API aktor yang sama (butir "Sesi API aktor" di `suite.md`).
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: seri PC (TC-FA-PREF-362-631), PC-1 (Default Disposal Proceeds Account tersimpan kosong) dan PC-22 (Chart of Accounts: `4-9100 – Laba Pelepasan Aset` berstatus Active dengan function Gain on Disposal; `1-3190 – Kliring Hasil Lama` berstatus Inactive dengan function Disposal Proceeds).
- Kemampuan teknis: kirim request langsung ke endpoint Save Preferences dengan klien HTTP dan baca jumlah baris Changelog, System Log, dan Activity Log FAMS (N dibaca sebelum aksi, bagian 8b butir 10). Disediakan tim FE/BE tanpa endpoint karangan (S-13).
- Seed dan pemulihan Preferences lewat API: lihat butir "Seed dan pemulihan lewat API" di `suite.md`. Spec ini tidak menyimpan perubahan.
- Flag Guided Tooltip halaman Preferences: lihat butir "Flag Guided Tooltip" di `suite.md`.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Seed company ke seri PC (Preferences PC-1 dan Chart of Accounts PC-22) lewat API hingga tersimpan
2. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS

### TC-FA-PREF-627: Request langsung Default Disposal Proceeds Account dengan akun function di luar Disposal Proceeds ditolak server

3. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengisi Default Disposal Proceeds Account dengan akun 4-9100 – Laba Pelepasan Aset yang ber-function Gain on Disposal
4. Verifikasi server menolak permintaan dengan pesan "This default disposal proceeds account no longer exists. Please select another."
5. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
6. Verifikasi Default Disposal Proceeds Account tetap kosong
7. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-628: Request langsung Default Disposal Proceeds Account dengan akun Inactive ditolak server

8. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengisi Default Disposal Proceeds Account dengan akun 1-3190 – Kliring Hasil Lama yang berstatus Inactive
9. Verifikasi server menolak permintaan dengan pesan "This default disposal proceeds account no longer exists. Please select another."
10. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
11. Verifikasi Default Disposal Proceeds Account tetap kosong
12. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE. Request langsung ke server tidak melewati browser: asersi hanya respons server, nilai Preferences tersimpan, dan jumlah baris log (8b butir 1).
- Langkah penghubung (S-03): langkah 1 (seed seri PC), langkah 2 (baseline jumlah baris log; 8b butir 10), langkah 5 dan 10 (baca ulang).
- Asersi "jumlah baris ketiga surface sama dengan jumlah awal" (langkah 7 dan 12) adalah perbandingan terhadap baseline yang dicatat langkah 2, bukan absence entri tanpa pembanding (S-12).
- Temuan untuk QA:
  - TC-FA-PREF-627 dan 628 Expected b menyebut "jumlah baris Changelog, System Log, serta Activity Log sama dengan jumlah awal" tanpa menyebut sumber baseline; spec mencatat baseline pada langkah 2 lewat kemampuan baca BE (S-12).
  - TC-FA-PREF-627 dan 628 tidak menyebut kode HTTP penolakan; spec mengasersi pesan Expected apa adanya.
  - Post Condition TC-FA-PREF-627 dan 628 ("Default Disposal Proceeds Account tetap kosong") sama dengan Expected b yang diasersi (langkah 6 dan 11).
