---
id: TC-FA-PREF-E2E-085-isolasi-tenant-tab-dan-request-langsung-hanya-berlaku-untuk-company-client-aktor
title: "Isolasi Tenant: Tab Preferences dan Request Langsung Hanya Berlaku untuk Company Client Aktor"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-546
  - TC-FA-PREF-547
sourceRules: ["FAPREF-LOGIC-01a", "FAPREF-LOGIC-03e", "L-01a", "L-02e", "§4.1.4#r15", "§4.1.4#r16"]
smoke: []
dependsOn: []
trace:
  "FAPREF-LOGIC-01a": [1, 6]
  "FAPREF-LOGIC-03e": 1
  "L-01a": 3
  "L-02e": 3
  "§4.1.4#r15": 4
  "§4.1.4#r16": 5
anchor: [12, 13]
coverage:
  web: automated
---

# Isolasi Tenant: Tab Preferences dan Request Langsung Hanya Berlaku untuk Company Client Aktor

## Prerequisites

- Mode: FE+BE.
- Kelas harness: c (dua tenant).
- Akun aktor: Total Control Client `PT Maju Sentosa` (Pre-setup PC-14: Dewi Lestari, tampil "Dewi L"); email akun ini tidak tertulis di Pre-setup TC (disediakan tim FE); password `Spectra.env.FA_TCC_PASSWORD` (env var belum terdaftar, didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; nama diusulkan spec mengikuti skema `FA_<ROLE>_PASSWORD`; password akun company lain perlu dikonfirmasi tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences) pada company `PT Maju Sentosa`. Hook `after` mengembalikan sesi ke akun default suite.
- Tenant kedua: `PT Contoh Konstruksi` (Pre-setup PC-1; Default Capitalization Threshold 5.000.000; Changelog Preferences 9 entri PB-C1 dengan Modified By "Rina A" dan "Budi S"), diakses lewat sesi API Total Control Rina Anggraini (Pre-setup PC-8, tampil "Rina A"; password `Spectra.env.FA_TC_PASSWORD`, env var belum terdaftar, didaftarkan tim FE; nama berbeda dari akun Dewi Lestari; butir "Sesi API aktor" di `suite.md`, tanpa sesi web).
- Data Pre-setup (hanya dibaca): `PT Maju Sentosa` dengan Default Capitalization Threshold tersimpan 3.000.000 dan Changelog Preferences tepat 2 entri (PC-14): (1) Date 18/10/26 09:30, Action Edit, Section Capitalization, Field Default Capitalization Threshold, Old Value 5.000.000, New Value 3.000.000, Modified By Dewi L; (2) Date 10/10/26 08:00, Action Create, Section —, Field Preferences, Old Value —, New Value Initial values, Modified By Dewi L. Format tanggal dd/MM/yy HH:mm. Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): request langsung Save Preferences memakai sesi API `PT Maju Sentosa` dengan identitas company `PT Contoh Konstruksi` pada payload; fixture BE untuk membaca Preferences `PT Contoh Konstruksi`; kemampuan baca BE jumlah baris Changelog Preferences `PT Contoh Konstruksi` (baseline, bagian 8b butir 10).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) untuk akun aktor spec ini.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-546: Tab Preferences hanya menampilkan data company client aktor

1. Verifikasi Default Capitalization Threshold menampilkan "Rp 3.000.000,00"
2. Klik ikon View history
3. Verifikasi modal Changelog: Preferences memuat tepat 2 baris
4. Verifikasi baris 1: Date 18/10/26 09:30, Action Edit, Section Capitalization, Field Default Capitalization Threshold, Old Value 5.000.000, New Value 3.000.000, Modified By Dewi L
5. Verifikasi baris 2: Date 10/10/26 08:00, Action Create, Section —, Field Preferences, Old Value —, New Value Initial values, Modified By Dewi L
6. Verifikasi tidak ada baris Changelog dengan Modified By "Rina A" atau "Budi S"
7. Klik ikon [✕] di header modal Changelog

### TC-FA-PREF-547: Request langsung dari Client lain tidak mengubah Preferences company client lain

8. Catat jumlah baris Changelog Preferences `PT Contoh Konstruksi` (baseline)
9. Kirim request langsung Save Preferences memakai sesi API `PT Maju Sentosa` dengan menyertakan identitas company `PT Contoh Konstruksi` dan Default Capitalization Threshold 9000000
10. Tunggu aksi selesai
11. Baca ulang nilai Preferences `PT Contoh Konstruksi` memakai sesi API Total Control Rina Anggraini
12. Verifikasi Default Capitalization Threshold `PT Contoh Konstruksi` tetap 5.000.000
13. Verifikasi jumlah baris Changelog `PT Contoh Konstruksi` sama dengan baseline langkah 8

## Notes

- Langkah penghubung (S-03): langkah 7 (menutup modal) dan langkah 10 (menunggu request langsung selesai sebelum berpindah ke sesi API Rina Anggraini, bagian 8b butir 8). Langkah 6 (absence) memakai baris 1 dan 2 pada langkah 4 dan 5 sebagai anchor positif (bagian 8b butir 2).
- Langkah 3 memakai "tepat 2 baris" karena data Changelog `PT Maju Sentosa` adalah seed terisolasi (PC-14) dan dibaca tanpa aksi tulis; asersi ini bukan total audit trail permanen yang tumbuh karena spec tidak menulis ke company itu.
- Pelaku kedua (Rina Anggraini) hanya memakai sesi API dan bukan konteks UI kedua (bagian 3 prinsip 13, P-2 2026-10-30); kelas c berlaku karena objek uji adalah dua tenant yang berbeda.
- Request langsung pada langkah 9 hanya mengasersi state data lewat fixture BE (bagian 8b butir 1); perilaku FE untuk respons itu tidak diasersi.
- Temuan untuk QA:
  - TC-FA-PREF-547 tidak menyebut status respons penolakan request langsung, sehingga spec tidak mengasersinya.
  - Expected TC-FA-PREF-547 butir a menulis nilai tampilan "Rp 5.000.000,00" untuk hasil pembacaan lewat sesi API; spec mengasersi nilai 5.000.000 hasil baca BE karena tampilan UI tidak diamati pada langkah ini.
  - Post Condition TC-FA-PREF-546 tidak ada; Post Condition TC-FA-PREF-547 ("Preferences company client lain tidak berubah") dicakup oleh Expected a pada langkah 12.
