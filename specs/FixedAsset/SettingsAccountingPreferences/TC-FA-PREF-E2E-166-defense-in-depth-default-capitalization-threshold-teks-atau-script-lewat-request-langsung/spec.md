---
id: TC-FA-PREF-E2E-166-defense-in-depth-default-capitalization-threshold-teks-atau-script-lewat-request-langsung
title: "Defense-in-Depth: Default Capitalization Threshold Berisi Teks atau Script Ditolak Server dan Tidak Tercatat di Changelog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-529
  - TC-FA-PREF-530
coverage:
  web: automated
---

# Defense-in-Depth: Default Capitalization Threshold Berisi Teks atau Script Ditolak Server dan Tidak Tercatat di Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI dan sesi API: Total Control "Rina Anggraini" `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Request langsung dan pembacaan ulang memakai sesi API aktor yang sama (butir "Sesi API aktor" di `suite.md`).
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: PC-1 dan PC-6 (Default Capitalization Threshold tersimpan 5.000.000).
- Kemampuan teknis: kirim request langsung ke endpoint Save Preferences dengan klien HTTP dan baca jumlah baris Changelog, System Log, dan Activity Log FAMS (N dibaca sebelum aksi, bagian 8b butir 10). Disediakan tim FE/BE tanpa endpoint karangan (S-13).
- Seed dan pemulihan Preferences lewat API: lihat butir "Seed dan pemulihan lewat API" di `suite.md`. Spec ini tidak menyimpan perubahan.
- Flag Guided Tooltip halaman Preferences: lihat butir "Flag Guided Tooltip" di `suite.md`.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS

### TC-FA-PREF-529: Request langsung Default Capitalization Threshold berisi teks abc ditolak server

2. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengisi Default Capitalization Threshold abc
3. Verifikasi server menolak permintaan karena tipe Decimal hanya menerima angka
4. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
5. Verifikasi nilai Preferences tersimpan tidak berubah (Default Capitalization Threshold tetap 5.000.000)
6. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal
7. Buka modal Changelog: Preferences
8. Verifikasi modal Changelog: Preferences tampil dengan baris entri yang sudah ada
9. Verifikasi modal Changelog: Preferences tidak memuat teks "abc"
10. Tutup modal Changelog: Preferences

### TC-FA-PREF-530: Request langsung Default Capitalization Threshold berisi teks <script>alert(1)</script> ditolak server

11. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengisi Default Capitalization Threshold <script>alert(1)</script>
12. Verifikasi server menolak permintaan karena tipe Decimal hanya menerima angka
13. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
14. Verifikasi nilai Preferences tersimpan tidak berubah (Default Capitalization Threshold tetap 5.000.000)
15. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal
16. Buka modal Changelog: Preferences
17. Verifikasi modal Changelog: Preferences tampil dengan baris entri yang sudah ada
18. Verifikasi modal Changelog: Preferences tidak memuat teks "<script>alert(1)</script>"

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pengecualian K-1: spec defense-in-depth (kelas a) dengan Expected respons API. Request langsung tidak melewati browser; asersi penolakan ada pada langkah Verifikasi respons.
- Asersi absence pada langkah 9 dan 18 didahului langkah anchor positif (langkah 8 dan 17: modal tampil dengan baris entri yang ada, 8b butir 2).
- Langkah penghubung (S-03): langkah 10 (menutup modal Changelog sebelum TC berikutnya, S-09).
- Baseline log (langkah 1) dicatat sekali; penolakan tidak mengubah jumlah baris log sehingga hitung ulang TC-530 dibandingkan dengan jumlah awal yang sama (S-12).
- Post Condition ("Default Capitalization Threshold tidak berubah") dicakup Expected butir b dan diasersi pada langkah 5 dan 14.
- Temuan untuk QA:
  - TC-FA-PREF-529 dan 530 tidak menyebut kode respons atau pesan penolakan; spec mengasersi alasan penolakan sesuai Expected ("tipe Decimal hanya menerima angka").
  - Precondition TC-FA-PREF-529 dan 530 menyebut jumlah baris awal dicatat penguji; spec mencatat pada langkah 1.
  - Asersi "tidak memuat teks payload" pada modal Changelog tidak menyebut kolom yang diperiksa; spec memeriksa isi modal secara keseluruhan.
