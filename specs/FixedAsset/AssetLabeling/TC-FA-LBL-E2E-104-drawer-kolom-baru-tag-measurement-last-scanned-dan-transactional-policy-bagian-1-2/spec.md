---
id: TC-FA-LBL-E2E-104-drawer-kolom-baru-tag-measurement-last-scanned-dan-transactional-policy-bagian-1-2
title: "Drawer Kolom Baru: TAG, Measurement, Last Scanned, dan Transactional Policy (bagian 1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-536
  - TC-FA-LBL-538
  - TC-FA-LBL-543
coverage:
  web: automated
---

# Drawer Kolom Baru: TAG, Measurement, Last Scanned, dan Transactional Policy (bagian 1/2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control `Company Probe` (Pre-setup #37, pengguna `Total Control Probe`), `Fixture.assetLabeling.akun.totalControlProbe`, `Spectra.env.FA_TC_PROBE_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Probe` (#37), hanya dibaca dan dirujuk lewat `Fixture.assetLabeling.probe` (nama label, aset, tag aktif, Symbol UoM, policy, dan Last Scanned sesuai Tabel Pre-setup TC): label `Column Probe` pada `Probe Asset - 41` (`Probe Item A`; tag aktif `RFID` Tag Code `RFID-41` dan `QR` Tag Code `QR-41`; UoM `Kilogram` Symbol `kg`; policy Borrow dan Assign On; Last Scanned 10 Oct 2026 08:00 dari Audit), `Probe Asset - 42` (`Probe Item B`; tanpa tag aktif; UoM `Piece` Symbol `pcs`; seluruh policy Off; belum pernah dipindai), `Probe Asset - 43` (`Probe Item C`; tag aktif `NFC` Tag Code `NFC-43`; `kg`; hanya Transfer On; Last Scanned 12 Oct 2026 09:00), dan `Probe Asset - 44` (`Probe Item D`; tag aktif `RFID` Tag Code `RFID-44`; `pcs`; Borrow, Self Service Borrow, dan Assign On; Last Scanned 08 Oct 2026 10:00).
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlProbe` (email akun Total Control `Company Probe`) dan `Fixture.assetLabeling.probe` (data Pre-setup #37).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4).
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Kemampuan menghapus preferensi itu disediakan tim FE. Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah (Last Updated tidak berubah).
- Env var: `Spectra.env.FA_TC_PROBE_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-LBL-536: Kolom TAG di Drawer: default Visible, ikon per tipe tag aktif, tanpa Tag Code, dan — bila tanpa tag

1. Klik chip `Column Probe` di kolom Label
2. Verifikasi kolom `TAG` tampil tanpa perlu dicentang, berada setelah `Asset ID` dan sebelum `Brand`
3. Verifikasi `Probe Asset - 41` menampilkan dua ikon (`RFID` dan `QR`) penuh
4. Verifikasi `Probe Asset - 43` menampilkan satu ikon `NFC`
5. Verifikasi `Probe Asset - 44` menampilkan satu ikon `RFID`
6. Verifikasi `Probe Asset - 42` (tanpa tag aktif) menampilkan `—`
7. Verifikasi tidak ada Tag Code (`RFID-41`, `QR-41`, `NFC-43`, `RFID-44`) yang tampil di sel TAG maupun kolom lain
8. Hover ikon `RFID` pada `Probe Asset - 41`
9. Verifikasi hover menampilkan label tipe `RFID`
10. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`
11. Verifikasi checkbox `TAG` tercentang dan enabled (Hideable)
12. Tutup Setup Column dengan `[✕]`
13. Tutup Drawer Tagged Asset

### TC-FA-LBL-538: Kolom Measurement di Drawer: default Hidden dan sel menampilkan Symbol saja

14. Klik chip `Column Probe` di kolom Label
15. Verifikasi kolom `Measurement` tidak tampil
16. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Measurement`, lalu klik `[Save]`
17. Verifikasi `Probe Asset - 41` dan `Probe Asset - 43` menampilkan `kg`
18. Verifikasi `Probe Asset - 42` dan `Probe Asset - 44` menampilkan `pcs`
19. Verifikasi Unit Name `Kilogram` dan `Piece` tidak tampil di tabel
20. Verifikasi kolom `Measurement` berada di antara `Model/Type` dan `Group`
21. Verifikasi tidak ada sel kosong pada kolom `Measurement`
22. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Measurement`, lalu klik `[Save]`
23. Tutup Drawer Tagged Asset

### TC-FA-LBL-543: Kolom Last Scanned di Drawer: default Hidden, format General Settings, dan — bila belum pernah dipindai

24. Klik chip `Column Probe` di kolom Label
25. Verifikasi kolom `Last Scanned` tidak tampil
26. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Last Scanned`, lalu klik `[Save]`
27. Verifikasi tanggal `Probe Asset - 41`, `Probe Asset - 43`, dan `Probe Asset - 44` mengikuti format General Settings
28. Verifikasi `Probe Asset - 42` (belum pernah dipindai) menampilkan `—`
29. Klik icon Filter di toolbar Drawer, lalu pilih rentang tanggal `09 Oct 2026` sampai `11 Oct 2026` pada `Last Scanned`
30. Verifikasi teks tanggal di kotak input Filter memakai pengaturan General Settings
31. Tutup Filter Panel tanpa `[Apply]`
32. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Last Scanned`, lalu klik `[Save]`
33. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03): tutup Setup Column dan Drawer, tutup Filter Panel pada TC-FA-LBL-543, dan langkah Pemulihan kolom bukan bagian Expected TC; pemulihan mengembalikan kolom baru ke Hidden sebagai keadaan awal blok berikutnya (S-09).
- Urutan TC-FA-LBL-536, 538, 543 mengikuti nomor TC.
- Temuan untuk QA:
  - TC-FA-LBL-543 Langkah Uji 5 hanya menyebut "pilih rentang tanggal pada Last Scanned" tanpa nilai; spec memakai rentang `09 Oct 2026` sampai `11 Oct 2026` seperti TC-FA-LBL-541 dan tidak meng-Apply filter karena Expected hanya menyangkut teks tanggal di kotak input Filter.
  - TC-FA-LBL-543 Expected b tidak menyebut string format tanggal; spec memverifikasi bahwa tanggal mengikuti pengaturan General Settings tanpa menuliskan string format.
