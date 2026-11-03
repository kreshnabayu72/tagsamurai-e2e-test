---
id: TC-FA-LBL-E2E-107-drawer-kolom-baru-setup-column-guard-dan-search-bagian-2-2
title: "Drawer Kolom Baru: Setup Column, Guard, dan Search (bagian 2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-567
coverage:
  web: automated
---

# Drawer Kolom Baru: Setup Column, Guard, dan Search (bagian 2/2)

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

### TC-FA-LBL-567: Search Drawer mencocokkan label ikon kolom TAG dan nama transaksi kolom Transactional Policy

1. Klik chip `Column Probe` di kolom Label
2. Klik icon Search di toolbar Drawer, ketik `RFID`, tekan Enter
3. Verifikasi `Probe Asset - 44` dan `Probe Asset - 41` tampil (label ikon `RFID` salah satu ikon pada sel)
4. Ganti isi kotak search dengan `QR`, tekan Enter
5. Verifikasi hanya `Probe Asset - 41` tampil
6. Ganti isi kotak search dengan `NFC`, tekan Enter
7. Verifikasi hanya `Probe Asset - 43` tampil
8. Ganti isi kotak search dengan `Borrow`, tekan Enter
9. Verifikasi empty state `No results found` (kolom `Transactional Policy` tersembunyi tidak dicari)
10. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Transactional Policy`, lalu klik `[Save]`
11. Ganti isi kotak search dengan `Borrow`, tekan Enter
12. Verifikasi `Probe Asset - 41` dan `Probe Asset - 44` tampil (nama transaksi Borrow pada ikon)
13. Ganti isi kotak search dengan `Transfer`, tekan Enter
14. Verifikasi hanya `Probe Asset - 43` tampil
15. Ganti isi kotak search dengan `RFID-41`, tekan Enter
16. Verifikasi empty state `No results found` (Tag Code tidak tampil dan tidak dicari)
17. Klik `(←)` pada kotak Search
18. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Transactional Policy`, lalu klik `[Save]`
19. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03): mengosongkan Search, Pemulihan kolom `Transactional Policy` ke Hidden, dan menutup Drawer memulihkan keadaan awal.
- Temuan untuk QA:
  - TC-FA-LBL-567 Expected a menyebut `Probe Asset - 44` dan `Probe Asset - 41` tanpa kuantor "hanya"; spec memverifikasi kedua baris itu tampil sesuai TC.
