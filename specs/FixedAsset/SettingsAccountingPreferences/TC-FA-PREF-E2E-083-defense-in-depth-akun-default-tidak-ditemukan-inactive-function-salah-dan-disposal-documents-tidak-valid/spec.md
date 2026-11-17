---
id: TC-FA-PREF-E2E-083-defense-in-depth-akun-default-tidak-ditemukan-inactive-function-salah-dan-disposal-documents-tidak-valid
title: "Defense-in-Depth: Akun Default Tidak Ditemukan, Inactive, atau Function Salah dan Disposal Documents Tidak Valid Ditolak Server Lewat Request Langsung"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-536
  - TC-FA-PREF-537
  - TC-FA-PREF-538
  - TC-FA-PREF-539
  - TC-FA-PREF-540
  - TC-FA-PREF-542
  - TC-FA-PREF-543
sourceRules: ["V-04", "E-FAPREF-04", "RG-02", "FAPREF-LOGIC-07h", "FAPREF-LOGIC-07a"]
smoke: []
dependsOn: []
trace:
  "V-04": [3, 8, 13, 18, 23]
  "E-FAPREF-04": [5, 10, 15, 20, 25]
  "RG-02": [6, 11, 16, 21, 26, 31, 36]
  "FAPREF-LOGIC-07h": [28, 30, 33, 35]
  "FAPREF-LOGIC-07a": [30, 35]
coverage:
  web: automated
---

# Defense-in-Depth: Akun Default Tidak Ditemukan, Inactive, atau Function Salah dan Disposal Documents Tidak Valid Ditolak Server Lewat Request Langsung

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI dan sesi API: Total Control "Rina Anggraini" `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Request langsung dan pembacaan ulang memakai sesi API aktor yang sama (butir "Sesi API aktor" di `suite.md`).
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: PC-1 (Disposal Documents jenis Sell tersimpan Optional) dan PC-5 (Default Gain on Disposal, Default Loss on Disposal, Default Capitalization Offset, dan Found Asset Credit Account tersimpan kosong; akun `6-9300 – Rugi Penghapusan Lama` berstatus Inactive; akun `1-2900 – Biaya Dikapitalisasi` ber-function Capitalization Offset; akun `4-9100 – Laba Pelepasan Aset` ber-function Gain on Disposal). Identitas akun "tidak ada di Chart of Accounts" pada TC-536 disediakan tim FE (TC tidak menyebut nilainya).
- Kemampuan teknis: kirim request langsung ke endpoint Save Preferences dengan klien HTTP dan baca jumlah baris Changelog, System Log, dan Activity Log FAMS (N dibaca sebelum aksi, bagian 8b butir 10). Disediakan tim FE/BE tanpa endpoint karangan (S-13).
- Seed dan pemulihan Preferences lewat API: lihat butir "Seed dan pemulihan lewat API" di `suite.md`. Spec ini tidak menyimpan perubahan.
- Flag Guided Tooltip halaman Preferences: lihat butir "Flag Guided Tooltip" di `suite.md`.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS

### TC-FA-PREF-536: Request langsung Default Gain on Disposal dengan akun tidak ditemukan ditolak server

2. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengisi Default Gain on Disposal dengan identitas akun yang tidak ada di Chart of Accounts
3. Verifikasi server menolak permintaan dengan pesan "This default gain on disposal no longer exists. Please select another."
4. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
5. Verifikasi Default Gain on Disposal tetap kosong
6. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-537: Request langsung Default Loss on Disposal dengan akun Inactive ditolak server

7. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengisi Default Loss on Disposal dengan akun 6-9300 – Rugi Penghapusan Lama yang berstatus Inactive
8. Verifikasi server menolak permintaan dengan pesan "This default loss on disposal no longer exists. Please select another."
9. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
10. Verifikasi Default Loss on Disposal tetap kosong
11. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-538: Request langsung Default Gain on Disposal dengan akun function di luar Gain on Disposal atau Loss on Disposal ditolak server

12. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengisi Default Gain on Disposal dengan akun 1-2900 – Biaya Dikapitalisasi yang ber-function Capitalization Offset
13. Verifikasi server menolak permintaan dengan pesan "This default gain on disposal no longer exists. Please select another."
14. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
15. Verifikasi Default Gain on Disposal tetap kosong
16. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-539: Request langsung Default Capitalization Offset dengan akun function di luar Capitalization Offset ditolak server

17. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengisi Default Capitalization Offset dengan akun 4-9100 – Laba Pelepasan Aset yang ber-function Gain on Disposal
18. Verifikasi server menolak permintaan dengan pesan "This default capitalization offset no longer exists. Please select another."
19. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
20. Verifikasi Default Capitalization Offset tetap kosong
21. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-540: Request langsung Found Asset Credit Account dengan akun Inactive ditolak server

22. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengisi Found Asset Credit Account dengan akun 6-9300 – Rugi Penghapusan Lama yang berstatus Inactive
23. Verifikasi server menolak permintaan dengan pesan "This found asset credit account no longer exists. Please select another."
24. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
25. Verifikasi Found Asset Credit Account tetap kosong
26. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-542: Request langsung Disposal Documents jenis Sell dengan nilai kosong ditolak server

27. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengisi Disposal Documents jenis Sell dengan nilai kosong
28. Verifikasi server menolak permintaan
29. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
30. Verifikasi Disposal Documents jenis Sell tetap Optional
31. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-543: Request langsung Disposal Documents jenis Sell dengan nilai Mandatory yang bukan Required atau Optional ditolak server

32. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengisi Disposal Documents jenis Sell dengan nilai Mandatory yang bukan Required atau Optional
33. Verifikasi server menolak permintaan
34. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
35. Verifikasi Disposal Documents jenis Sell tetap Optional
36. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pengecualian K-1: spec defense-in-depth (kelas a) dengan Expected respons API. Request langsung tidak melewati browser; asersi penolakan ada pada langkah Verifikasi respons.
- Spec ini 36 langkah (di atas smell 35 langkah) karena tujuh TC defense-in-depth berbagi satu baseline log dan satu tahap pemulihan; memecahnya menggandakan baseline tanpa memperjelas asersi.
- Baseline log (langkah 1) dicatat sekali; penolakan tidak mengubah jumlah baris log sehingga hitung ulang tiap TC dibandingkan dengan jumlah awal yang sama (S-12).
- Post Condition semua TC ("... tidak berubah") dicakup Expected butir b dan diasersi pada langkah nilai tersimpan dan jumlah baris log.
- Temuan untuk QA:
  - TC-FA-PREF-536 tidak menyebut identitas akun yang tidak ada di Chart of Accounts; spec meminta tim FE menyediakannya (S-11).
  - TC-FA-PREF-542 dan 543 hanya menyebut "server menolak permintaan" tanpa pesan atau kode respons; spec tidak menetapkan keduanya.
  - TC-FA-PREF-543 menyebut nilai "Mandatory" sebagai payload bukan Required atau Optional tanpa menyatakan apakah Mandatory nilai tidak valid atau label lama; spec mengikuti TC.
  - Pesan TC-FA-PREF-538 ("This default gain on disposal no longer exists. Please select another.") dipakai untuk akun ber-function salah; pesan itu semula untuk akun yang tidak ada lagi sehingga kesesuaian teks perlu dikonfirmasi terhadap PRD (V-04).
