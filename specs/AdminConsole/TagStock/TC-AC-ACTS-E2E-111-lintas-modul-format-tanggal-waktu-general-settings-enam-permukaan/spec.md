---
id: TC-AC-ACTS-E2E-111-lintas-modul-format-tanggal-waktu-general-settings-enam-permukaan
title: "Lintas Modul: Format Tanggal dan Waktu Mengikuti General Settings di Stock List, Tab Available, Tab In Use, Event Log, dan Approvals Tab Active dan History"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-691
  - TC-AC-ACTS-692
  - TC-AC-ACTS-693
  - TC-AC-ACTS-694
  - TC-AC-ACTS-696
  - TC-AC-ACTS-697
coverage:
  web: automated
---

# Lintas Modul: Format Tanggal dan Waktu Mengikuti General Settings di Stock List, Tab Available, Tab In Use, Event Log, dan Approvals Tab Active dan History

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- State global General Settings: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta diatur oleh Principal pengubah General Settings lewat sesi API aktor sebelum langkah pertama (akun pengubah tidak ada di Pre-setup TC; disediakan tim FE/BE). Nilai awal General Settings dicatat dan dipulihkan di hook `after` (R-08), dan suite berjalan serial karena state global ini.
- SKU `RFID-ASSET-CORE-R5` (Data Pre-setup #12) dengan sedikitnya satu baris di Tab Available, Tab In Use, modal Event Log, dan Approvals Tab Active dan Tab History, disiapkan seeding fixture BE (disediakan tim FE/BE). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### Pengaturan General Settings

1. Atur General Settings: Date Format `dd/MM/yy`, Time Format 24 jam, dan Timezone Asia/Jakarta hingga tersimpan (sesi API aktor)

### TC-AC-ACTS-691: Format tanggal dan waktu di Stock List (Last Updated)

2. Buka TAG > Stock
3. Verifikasi kolom tanggal Last Updated tampil dengan Date Format `dd/MM/yy`, jam 24 jam, dan zona waktu Asia/Jakarta
4. Buka Filter dan pilih tanggal pada field tanggal
5. Verifikasi teks tanggal terpilih di input Filter mengikuti Date Format `dd/MM/yy`

### TC-AC-ACTS-692: Format tanggal dan waktu di Tab Available (Registered At)

6. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
7. Verifikasi kolom tanggal Registered At tampil dengan Date Format `dd/MM/yy`, jam 24 jam, dan zona waktu Asia/Jakarta
8. Buka Filter dan pilih tanggal pada field tanggal
9. Verifikasi teks tanggal terpilih di input Filter mengikuti Date Format `dd/MM/yy`

### TC-AC-ACTS-693: Format tanggal dan waktu di Tab In Use (Registered At, Activated At)

10. Buka Tab In Use
11. Verifikasi kolom tanggal Registered At dan Activated At tampil dengan Date Format `dd/MM/yy`, jam 24 jam, dan zona waktu Asia/Jakarta
12. Buka Filter dan pilih tanggal pada field tanggal
13. Verifikasi teks tanggal terpilih di input Filter mengikuti Date Format `dd/MM/yy`

### TC-AC-ACTS-694: Format tanggal dan waktu di modal Event Log (Date)

14. Buka modal `[Event Log]`
15. Verifikasi kolom tanggal Date tampil dengan Date Format `dd/MM/yy`, jam 24 jam, dan zona waktu Asia/Jakarta
16. Buka Filter dan pilih tanggal pada field tanggal
17. Verifikasi teks tanggal terpilih di input Filter mengikuti Date Format `dd/MM/yy`
18. Tutup modal Event Log

### TC-AC-ACTS-696: Format tanggal dan waktu di Approvals Tab Active (Requested At)

19. Buka Approvals > TAG Stock > Tab Active
20. Verifikasi kolom tanggal Requested At tampil dengan Date Format `dd/MM/yy`, jam 24 jam, dan zona waktu Asia/Jakarta
21. Buka Filter dan pilih tanggal pada field tanggal
22. Verifikasi teks tanggal terpilih di input Filter mengikuti Date Format `dd/MM/yy`

### TC-AC-ACTS-697: Format tanggal dan waktu di Approvals Tab History (Requested At, Resolved At)

23. Buka Tab History
24. Verifikasi kolom tanggal Requested At dan Resolved At tampil dengan Date Format `dd/MM/yy`, jam 24 jam, dan zona waktu Asia/Jakarta
25. Buka Filter dan pilih tanggal pada field tanggal
26. Verifikasi teks tanggal terpilih di input Filter mengikuti Date Format `dd/MM/yy`

## Notes

- Mode: FE+BE. State global General Settings dipulihkan di hook `after` (R-08). Spec ini tidak mengubah data lain.
- Langkah penghubung tanpa Verifikasi (S-03): mengatur General Settings lewat sesi API aktor ("hingga tersimpan", R-20) dan membuka layar baca. Langkah "Lihat kolom tanggal" TC digabung ke Verifikasi kolom tanggal (langkah aksi tidak memuat klaim keadaan, R-02). Langkah "Tutup modal Event Log" menutup modal sebelum pindah surface atau ganti akun (pemulihan state, S-09).
- Temuan untuk QA:
  - TC-AC-ACTS-691 sampai TC-AC-ACTS-697 menyebut "General Settings" tanpa akun pengubah dan tanpa nilai awal yang dipulihkan; disediakan tim FE/BE.
  - TC-AC-ACTS-695 dihapus pada Changelog TC 2026-10-20; permukaan Popup Detail Event Log tidak punya TC format tanggal di rentang ini.
