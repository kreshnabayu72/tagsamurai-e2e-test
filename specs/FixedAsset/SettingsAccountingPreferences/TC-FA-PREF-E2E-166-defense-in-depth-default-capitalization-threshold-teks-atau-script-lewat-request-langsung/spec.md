---
id: TC-FA-PREF-E2E-166-defense-in-depth-default-capitalization-threshold-teks-atau-script-lewat-request-langsung
title: "Defense-in-Depth: Default Capitalization Threshold Berisi Teks atau Script Ditolak Server dan Tidak Tercatat di Changelog"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-529
  - TC-FA-PREF-530
sourceRules: ["F-FAPREF-01.k3", "§9.9#r3", "L-02a", "L-02b", "L-02c", "§4.1#r2"]
smoke: []
dependsOn: []
trace:
  "F-FAPREF-01.k3": [3, 5, 15, 17]
  "§9.9#r3": [3, 15]
  "L-02a": [6, 11, 18, 23]
  "L-02b": [7, 19]
  "L-02c": [8, 20]
  "§4.1#r2": [10, 22]
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
6. Verifikasi jumlah baris Changelog sama dengan jumlah awal
7. Verifikasi jumlah baris System Log sama dengan jumlah awal
8. Verifikasi jumlah baris Activity Log FAMS sama dengan jumlah awal
9. Buka modal Changelog: Preferences
10. Verifikasi modal Changelog: Preferences tampil dengan baris entri yang sudah ada
11. Verifikasi modal Changelog: Preferences tidak memuat teks "abc"
12. Tutup modal Changelog: Preferences

### TC-FA-PREF-530: Request langsung Default Capitalization Threshold berisi teks <script>alert(1)</script> ditolak server

13. Catat ulang jumlah baris Changelog, System Log, dan Activity Log FAMS sebagai baseline TC-FA-PREF-530
14. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengisi Default Capitalization Threshold <script>alert(1)</script>
15. Verifikasi server menolak permintaan karena tipe Decimal hanya menerima angka
16. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
17. Verifikasi nilai Preferences tersimpan tidak berubah (Default Capitalization Threshold tetap 5.000.000)
18. Verifikasi jumlah baris Changelog sama dengan jumlah awal
19. Verifikasi jumlah baris System Log sama dengan jumlah awal
20. Verifikasi jumlah baris Activity Log FAMS sama dengan jumlah awal
21. Buka modal Changelog: Preferences
22. Verifikasi modal Changelog: Preferences tampil dengan baris entri yang sudah ada
23. Verifikasi modal Changelog: Preferences tidak memuat teks "<script>alert(1)</script>"

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pengecualian K-1: spec defense-in-depth (kelas a) dengan Expected respons API. Request langsung tidak melewati browser; asersi penolakan ada pada langkah Verifikasi respons.
- Asersi absence pada langkah 11 dan 23 didahului langkah anchor positif (langkah 10 dan 22: modal tampil dengan baris entri yang ada, 8b butir 2).
- Langkah penghubung (S-03): langkah 12 (menutup modal Changelog sebelum TC berikutnya, S-09), langkah 13 (catat ulang baseline untuk TC berikutnya, S-12).
- Baseline log dicatat per TC (S-12): langkah 1 untuk TC-FA-PREF-529 dan langkah 13 untuk TC-FA-PREF-530; hitung ulang pada langkah 4 dan 16 dibandingkan dengan baseline TC masing-masing.
- Asersi jumlah baris tiga surface sama dengan baseline, satu Verifikasi per surface (langkah 6 sampai 8 dan 18 sampai 20) atas request langsung yang ditolak adalah asersi jumlah ber-baseline yang sah di spec kelas a (konvensi bagian 3 prinsip 13 butir g); S-05 (absence log kelas g) tidak berlaku untuk asersi jumlah, dan asersi "tidak memuat teks" pada Changelog (langkah 11 dan 23) ikut aturan yang sama.
- Post Condition ("Default Capitalization Threshold tidak berubah") dicakup Expected butir b dan diasersi pada langkah 5 dan 17.
- Temuan untuk QA:
  - TC-FA-PREF-529 dan 530 tidak menyebut kode respons atau pesan penolakan; spec mengasersi alasan penolakan sesuai Expected ("tipe Decimal hanya menerima angka").
  - Precondition TC-FA-PREF-529 dan 530 menyebut jumlah baris awal dicatat penguji; spec mencatat pada langkah 1.
  - Asersi "tidak memuat teks payload" pada modal Changelog tidak menyebut kolom yang diperiksa; spec memeriksa isi modal secara keseluruhan.
