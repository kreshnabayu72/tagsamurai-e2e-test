---
id: TC-FA-LBL-E2E-106-drawer-kolom-baru-setup-column-guard-dan-search-bagian-1-2
title: "Drawer Kolom Baru: Setup Column, Guard, dan Search (bagian 1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-533
  - TC-FA-LBL-537
  - TC-FA-LBL-539
coverage:
  web: automated
---

# Drawer Kolom Baru: Setup Column, Guard, dan Search (bagian 1/2)

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
- Tabel 'Kolom Curated baru' (parameter langkah ulang TC-FA-LBL-533; urut sesuai Setup Column):

  | No | Kolom Curated baru | Posisi di Live Preview |
  |---|---|---|
  | 1 | `Measurement` | di antara `Model/Type` dan `Group` |
  | 2 | `Transactional Policy` | di antara `Status` dan `Last Updated` |
  | 3 | `Last Scanned` | di antara `Status` dan `Last Updated`, setelah `Transactional Policy` |
  | 4 | `Asset Value (Commercial)` | di antara `Status` dan `Last Updated`, setelah `Last Scanned` |
  | 5 | `Warranty Expiry` | di antara `Status` dan `Last Updated`, setelah `Asset Value (Commercial)` |

## Test Steps

### TC-FA-LBL-533: Setup Column Drawer: kolom Curated baru default Hidden, ceklis, dan unceklis

1. Klik chip `Column Probe` di kolom Label
2. Verifikasi kelima kolom pada tabel 'Kolom Curated baru' tidak tampil di header tabel Drawer
3. Verifikasi delapan kolom default tampil: `Name`, `Asset ID`, `TAG`, `Brand`, `Model/Type`, `Group`, `Status`, `Last Updated`
4. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`
5. Verifikasi kelima kolom pada tabel 'Kolom Curated baru' tidak tercentang
6. Verifikasi checkbox kelima kolom pada tabel 'Kolom Curated baru' enabled (kelas Curated)
7. Untuk setiap baris tabel 'Kolom Curated baru' (berurutan dari baris pertama; langkah 7 sampai 8): centang kolom pada baris itu
8. Verifikasi Live Preview langsung memuat kolom yang baru dicentang pada posisi 'Posisi di Live Preview' baris itu
9. Klik `[Save]`
10. Verifikasi kelima kolom pada tabel 'Kolom Curated baru' tampil di tabel Drawer
11. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`
12. Untuk setiap baris tabel 'Kolom Curated baru' (berurutan dari baris pertama): hapus centang kolom pada baris itu
13. Verifikasi kelima kolom pada tabel 'Kolom Curated baru' hilang dari Live Preview
14. Klik `[Save]`
15. Verifikasi kelima kolom pada tabel 'Kolom Curated baru' hilang dari tabel Drawer
16. Verifikasi delapan kolom default tetap tampil
17. Tutup Drawer Tagged Asset

### TC-FA-LBL-537: Guard: kolom Last Scanned tidak ikut dicari di Drawer

18. Klik chip `Column Probe` di kolom Label
19. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Last Scanned`, lalu klik `[Save]`
20. Verifikasi kolom `Last Scanned` tampil di tabel Drawer
21. Klik icon Search di toolbar Drawer, ketik `10 Oct 2026`, tekan Enter
22. Verifikasi empty state `No results found` dengan Description `Try adjusting your search or filter.`
23. Klik `(←)` pada kotak Search
24. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Last Scanned`, lalu klik `[Save]`
25. Tutup Drawer Tagged Asset

### TC-FA-LBL-539: Search Drawer kolom Measurement: tidak dicari saat tersembunyi, dicari Symbol setelah ditampilkan

26. Klik chip `Column Probe` di kolom Label
27. Klik icon Search di toolbar Drawer, ketik `kg`, tekan Enter
28. Verifikasi empty state `No results found` (kolom `Measurement` tersembunyi tidak dicari)
29. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Measurement`, lalu klik `[Save]`
30. Ganti isi kotak search dengan `kg`, tekan Enter
31. Verifikasi hanya `Probe Asset - 41` dan `Probe Asset - 43` tampil
32. Klik `(←)` pada kotak Search
33. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Measurement`, lalu klik `[Save]`
34. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Langkah ulang (bagian 8b butir 7): langkah 7 dan 8 diulang lima kali (satu iterasi per baris tabel 'Kolom Curated baru'), langkah 12 diulang lima kali tanpa asersi per iterasi. Ekspansi: 46 langkah.
- Langkah penghubung (S-03): langkah Pemulihan kolom ke Hidden, `Klik (←) pada kotak Search`, dan tutup Drawer memulihkan keadaan awal blok berikutnya (S-09).
- Ukuran spec (34 langkah nominal, di atas smell 35 langkah dengan ekspansi): ketiga TC satu kelas (fungsional, Setup Column dan Search Drawer kolom Curated baru, akun dan data Pre-setup #37 yang sama) dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah membengkak karena ekspansi loop lima kolom dan tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-FA-LBL-533 Expected c menyebut posisi `Transactional Policy`, `Last Scanned`, `Asset Value (Commercial)`, dan `Warranty Expiry` "berurutan di antara `Status` dan `Last Updated`" tanpa menyebut `Asset Value (Fiscal)` yang menurut TC-FA-LBL-589 berada di antara `Asset Value (Commercial)` dan `Warranty Expiry`; spec memakai urutan yang tertulis di TC-FA-LBL-533.
