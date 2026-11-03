---
id: TC-FA-LBL-E2E-109-drawer-kolom-baru-filter-sumber-0-baris-dan-sort-tag-awalan-pendek
title: "Drawer Kolom Baru: Filter Sumber 0 Baris dan Sort TAG Awalan Pendek"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-542
  - TC-FA-LBL-588
coverage:
  web: automated
---

# Drawer Kolom Baru: Filter Sumber 0 Baris dan Sort TAG Awalan Pendek

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control `Company Probe` (Pre-setup #37, pengguna `Total Control Probe`), `Fixture.assetLabeling.akun.totalControlProbe`, `Spectra.env.FA_TC_PROBE_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Probe` (#37), hanya dibaca dan dirujuk lewat `Fixture.assetLabeling.probe` (nama label, aset, tag aktif, Symbol UoM, policy, dan Last Scanned sesuai Tabel Pre-setup TC): label `Empty Probe` tanpa aset dan label `Tag Sort Probe` pada `Probe Asset - 48` (`Probe Item H`; tag aktif `NFC`), `Probe Asset - 49` (`Probe Item I`; tag aktif `NFC` dan `QR`), `Probe Asset - 50` (`Probe Item J`; tag aktif `QR`), dan `Probe Asset - 51` (`Probe Item K`; tanpa tag aktif).
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlProbe` (email akun Total Control `Company Probe`) dan `Fixture.assetLabeling.probe` (data Pre-setup #37).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4).
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Kemampuan menghapus preferensi itu disediakan tim FE. Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah (Last Updated tidak berubah).
- Env var: `Spectra.env.FA_TC_PROBE_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-LBL-542: Filter Panel Drawer pada sumber 0 baris: dropdown Measurement dan TAG menampilkan No options available, Transactional Policy tetap memuat empat transaksi

1. Klik chip `Empty Probe` di kolom Label
2. Verifikasi empty state `No assets tagged`
3. Klik icon Filter di toolbar Drawer
4. Verifikasi Filter Panel terbuka dengan field `Measurement`, `TAG`, dan `Transactional Policy`
5. Buka dropdown `Measurement`
6. Verifikasi dropdown `Measurement` menampilkan teks `No options available`
7. Verifikasi dropdown `Measurement` tanpa pesan error
8. Tutup dropdown `Measurement`, lalu buka dropdown `TAG`
9. Verifikasi dropdown `TAG` menampilkan teks `No options available` (opsi berasal dari data tabel)
10. Tutup dropdown `TAG`, lalu buka dropdown `Transactional Policy`
11. Verifikasi dropdown `Transactional Policy` tetap memuat `Borrow`, `Self Service Borrow`, `Assign`, `Transfer` (empat opsi tetap)
12. Tutup dropdown `Transactional Policy`, lalu tutup Filter Panel
13. Tutup Drawer Tagged Asset

### TC-FA-LBL-588: Sort Drawer kolom TAG: urutan label ikon A-Z, awalan lebih pendek lebih dulu, dan — mengikuti aturan nilai kosong

14. Klik chip `Tag Sort Probe` di kolom Label
15. Klik header kolom `TAG` satu kali
16. Verifikasi urutan klik 1 (Ascending): `Probe Asset - 48` (`NFC`), `Probe Asset - 49` (`NFC, QR`), `Probe Asset - 50` (`QR`), lalu `Probe Asset - 51` (`—`) di akhir
17. Klik header kolom `TAG` kedua kali
18. Verifikasi urutan klik 2 (Descending): `Probe Asset - 51` (`—`) di awal, lalu `Probe Asset - 50`, `Probe Asset - 49`, `Probe Asset - 48`
19. Klik header kolom `TAG` ketiga kali
20. Verifikasi urutan klik 3 (Netral) kembali ke default Name A-Z
21. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Pembagian TC lintas spec: Sort kolom baru ada di spec 108 (TC-FA-LBL-540, 574) dan Filter kolom baru di spec 171 (TC-FA-LBL-541).
- Langkah penghubung (S-03): langkah tutup Drawer sesudah tiap TC; tidak ada kolom yang dicentang sehingga tidak ada Pemulihan Setup Column.
- Temuan untuk QA:
  - TC-FA-LBL-542 Expected c menyebut dropdown `Measurement` "tanpa pesan error" tanpa menyebut elemen error; spec memverifikasi dropdown tidak menampilkan pesan error dengan teks `No options available` pada langkah sebelumnya sebagai anchor positif.
