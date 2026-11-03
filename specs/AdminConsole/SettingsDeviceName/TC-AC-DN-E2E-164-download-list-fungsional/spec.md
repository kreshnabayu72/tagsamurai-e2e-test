---
id: TC-AC-DN-E2E-164-download-list-fungsional
title: "Download List: Tooltip, Overlay Format, Nama Berkas CSV/XLSX Tanpa Toast, Seluruh Baris, dan Filter Kosong"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-365
  - TC-AC-DN-366
  - TC-AC-DN-367
  - TC-AC-DN-369
  - TC-AC-DN-378
coverage:
  web: automated
---

# Download List: Tooltip, Overlay Format, Nama Berkas CSV/XLSX Tanpa Toast, Seluruh Baris, dan Filter Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (`suite.md`): `beforeEach` (membuka sub-tab Device Name, jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- General Settings entitas uji (Pre-setup #20): Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta; jam server dan jam browser sinkron.
- Data Pre-setup (hanya dibaca): #16 Device Name inti dan #17 seed 120 baris (`Seed Device 001` sampai `Seed Device 120`); total baris fixture 130 (9 inti, 120 seed, 1 nama panjang #23) diturunkan dari seeding (bagian 8b butir 10).
- Data Dinamis: tidak ada. Unduhan hanya dibaca.
- Kemampuan teknis (disediakan tim FE/BE): seeding Device Name, SKU, dan riwayat lewat sesi API akun #1 (token tidak dihitung sebagai sesi web, lihat `suite.md`); kemampuan baca jumlah entri Changelog, Activity Log, dan System Log aktor untuk baseline (bagian 8b butir 10).
- Kemampuan teknis (disediakan tim FE): pembaca berkas CSV dan XLSX hasil unduhan; nama berkas, header, dan jumlah baris adalah asersi fungsional (prinsip 13 butir f). Kelas harness e: dataset 130 baris.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Entri audit trail yang tercipta (Changelog, Activity Log, System Log aktor) bersifat permanen dan tidak dihapus; record milik spec dihapus di hook `after` dan entri historisnya tetap, bersuffix unik `{runId}-NNN` (`{runId}` hanya digit).

## Test Steps

1. TC-AC-DN-365: Tooltip ikon Download dan overlay pilihan format
2. Arahkan kursor ke ikon Download
3. Verifikasi tooltip `Download` tampil
4. Klik ikon Download
5. Verifikasi overlay memuat dua opsi: `Download as CSV` dan `Download as XLSX`
6. TC-AC-DN-366: Download as CSV menghasilkan file Device-Name.csv tanpa toast sukses
7. Klik `Download as CSV`
8. Verifikasi tidak ada toast sukses
9. Verifikasi file bernama `Device-Name.csv` terunduh
10. TC-AC-DN-367: Download as XLSX menghasilkan file Device-Name.xlsx tanpa toast sukses
11. Klik ikon Download lalu klik `Download as XLSX`
12. Verifikasi tidak ada toast sukses
13. Verifikasi file bernama `Device-Name.xlsx` terunduh
14. TC-AC-DN-369: Download tanpa Search dan Filter memuat seluruh baris lintas halaman
15. Klik ikon Download lalu klik `Download as CSV`
16. Buka file hasil unduhan dengan pembaca berkas CSV
17. Verifikasi file memuat baris header ditambah 130 baris data (seluruh Device Name, bukan hanya 10 baris halaman 1)
18. TC-AC-DN-378: Download dengan hasil filter kosong menghasilkan file hanya berisi header
19. Ketik Search `zzzxyz`, tekan Enter
20. Verifikasi List menampilkan empty state `No results found`
21. Verifikasi tombol Download tetap aktif
22. Klik ikon Download lalu klik `Download as CSV`
23. Verifikasi tidak ada toast
24. Verifikasi file terunduh
25. Buka file hasil unduhan dengan pembaca berkas CSV
26. Verifikasi file hanya memuat baris header kolom yang tampil tanpa baris data
27. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 'Klik `(←)` pada kotak Search' di akhir mengosongkan Search; pembaca berkas dibuka sebagai langkah observasi.
- Search dengan nama record bersuffix unik menggantikan kata kunci TC (S-12); akun aktor pada System Log dirujuk lewat email Fixture (R-06).
- Urutan: mengikuti sourceTc; TC-AC-DN-378 di akhir karena memakai Search yang dikosongkan.
- Temuan untuk QA:
  - TC-AC-DN-366, 367, dan 378 menempatkan asersi absence toast tanpa pemicu terpisah; spec menempatkannya segera sesudah klik pilihan format (bagian 8b butir 11) sebelum asersi berkas (langkah 8, 12, dan 23).
  - TC sumber memakai nama literal Pre-setup (`Dock Station`, `Door Antenna`, `Cable Tester`); spec memakai record milik spec bersuffix `{runId}-<NNN>` (S-06, S-12) dan Pre-setup #16 tidak diubah.
