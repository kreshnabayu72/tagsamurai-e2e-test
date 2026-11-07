---
id: TC-FA-LBL-E2E-171-drawer-kolom-baru-filter-tag-measurement-transactional-policy-dan-last-scanned
title: "Drawer Kolom Baru: Filter TAG, Measurement, Transactional Policy, dan Last Scanned"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-541
coverage:
  web: automated
---

# Drawer Kolom Baru: Filter TAG, Measurement, Transactional Policy, dan Last Scanned

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
- Env var: `Spectra.env.FA_TC_PROBE_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-LBL-541: Filter Drawer kolom baru: TAG, Measurement, Transactional Policy, dan Last Scanned

1. Klik chip `Column Probe` di kolom Label
2. Klik icon Filter di toolbar Drawer
3. Pilih `TAG` = `NFC`, lalu klik `[Apply]`
4. Verifikasi hanya `Probe Asset - 43` tampil
5. Klik `[Clear Field]`, lalu buka dropdown `TAG`
6. Verifikasi dropdown `TAG` memuat opsi `NFC`, `QR`, `RFID` (tipe distinct dari data tabel)
7. Pilih `RFID`, lalu klik `[Apply]`
8. Verifikasi `Probe Asset - 41` (RFID dan QR) dan `Probe Asset - 44` tampil (OR atas tipe tag aktif)
9. Klik `[Clear Field]`, lalu buka dropdown `Measurement`
10. Verifikasi dropdown `Measurement` memuat opsi `kg` dan `pcs`
11. Pilih `pcs`, lalu klik `[Apply]`
12. Verifikasi `Probe Asset - 42` dan `Probe Asset - 44` tampil
13. Klik `[Clear Field]`, lalu buka dropdown `Transactional Policy`
14. Verifikasi dropdown `Transactional Policy` memuat empat opsi tetap `Borrow`, `Self Service Borrow`, `Assign`, `Transfer`
15. Pilih `Transfer`, lalu klik `[Apply]`
16. Verifikasi hanya `Probe Asset - 43` tampil
17. Klik `[Clear Field]`, pilih `Transactional Policy` = `Assign`, lalu klik `[Apply]`
18. Verifikasi `Probe Asset - 41` dan `Probe Asset - 44` tampil
19. Klik `[Clear Field]`, pilih rentang `Last Scanned` `09 Oct 2026` sampai `11 Oct 2026`, lalu klik `[Apply]`
20. Verifikasi hanya `Probe Asset - 41` (10 Oct 2026) tampil
21. Klik `[Clear Field]`, lalu tutup panel Filter dengan klik icon Filter di toolbar Drawer
22. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Pembagian TC lintas spec: TC-FA-LBL-541 (Filter kolom baru) ada di spec ini; Sort kolom baru (TC-FA-LBL-540, 574) ada di spec 108 dan Filter sumber 0 baris (TC-FA-LBL-542) di spec 109. Ketiganya memakai akun dan data Pre-setup #37 yang sama.
- Langkah penghubung (S-03): langkah kedua terakhir mengosongkan filter (S-09) dan langkah terakhir menutup Drawer; kolom baru tidak dicentang sehingga tidak ada Pemulihan Setup Column.
- Filter Panel Drawer tetap terbuka sesudah `[Apply]` (bagian 8b butir 9): langkah 5, 9, 13, 17, dan 19 mengubah filter dari panel yang sama tanpa membuka panel lagi; langkah 21 menutupnya dengan klik icon Filter.
- Temuan untuk QA:
  - TC-FA-LBL-541 menulis "Buka panel lagi" pada Langkah Uji 4 sampai 8; spec tidak membuka panel lagi karena panel tetap terbuka sesudah `[Apply]`. Perilaku panel pada Drawer menunggu konfirmasi tim FE.
  - TC-FA-LBL-541 Langkah Uji 3 menyebut `[Apply]` setelah memilih `TAG` = `NFC` tanpa langkah membuka dropdown; spec membuka dropdown `TAG` pada langkah yang memeriksa daftar opsi (Expected b) sesuai urutan TC.
