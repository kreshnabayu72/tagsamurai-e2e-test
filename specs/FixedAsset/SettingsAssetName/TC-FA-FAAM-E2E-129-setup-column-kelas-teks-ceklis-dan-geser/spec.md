---
id: TC-FA-FAAM-E2E-129-setup-column-kelas-teks-ceklis-dan-geser
title: "Setup Column: Kelas Code, UoM, Modified By (Ceklis dan Geser)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-407
  - TC-FA-FAAM-408
coverage:
  web: automated
---

# Setup Column: Kelas Code, UoM, Modified By (Ceklis dan Geser)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`).
- Kemampuan teknis: drag and drop, scroll horizontal tabel, hapus preferensi kolom di browser (disediakan tim FE).
- Kolom yang diuji (diulang pada langkah 2 sampai 5 dan langkah 12 sampai 13):

  | Kolom |
  |---|
  | Code |
  | UoM |
  | Modified By |
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: konfigurasi kolom tabel utama (preferensi di browser) diubah spec ini. Pemulihan: hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE; spec ini terdaftar di `suite.md`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-407: Setup Column ceklis dan unceklis kelas Code, UoM, Modified By (teks)
1. Buka Popup Setup Column: klik header kolom Actions (⋯), lalu `Setup Column...`
2. Untuk setiap baris tabel "Kolom yang diuji", uncheck kolom tersebut
3. Verifikasi kolom hilang dari Live Preview dan dari tabel di balik modal
4. Check kembali kolom tersebut
5. Verifikasi kolom muncul kembali di Live Preview dan di tabel di balik modal
6. Uncheck kolom `Code`, lalu klik `[Save]`
7. Verifikasi kolom `Code` tersembunyi di tabel
8. Tekan F5
9. Verifikasi kolom `Code` tetap tersembunyi setelah F5
10. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, lalu tekan F5
### TC-FA-FAAM-408: Setup Column geser urutan kelas Code, UoM, Modified By (teks)
11. Buka Popup Setup Column
12. Untuk setiap baris tabel "Kolom yang diuji", drag kolom tersebut satu posisi ke atas
13. Verifikasi urutan kolom berubah di Live Preview dan di tabel
14. Klik `[Save]`
15. Tekan F5
16. Verifikasi urutan baru kolom `Code` tetap setelah Save dan F5
17. Verifikasi urutan baru kolom `UoM` tetap setelah Save dan F5
18. Verifikasi urutan baru kolom `Modified By` tetap setelah Save dan F5
19. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, lalu tekan F5

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): membuka Popup Setup Column dan pemulihan konfigurasi kolom (hapus preferensi kolom di browser lalu F5) di akhir blok supaya blok berikutnya mulai dari konfigurasi bawaan (S-09).
- Persistensi "tersimpan di `localStorage`" diamati lewat F5 (tersembunyi atau urutan tetap), bukan lewat pembacaan penyimpanan browser.
- Langkah yang diulang per kolom: langkah 2 sampai 5 (TC-FA-FAAM-407) dan langkah 12 sampai 13 (TC-FA-FAAM-408); parameter tiap iterasi ada di tabel "Kolom yang diuji" pada Prerequisites. Verifikasi diulang satu per klausa (bagian 8b butir 7). Ekspansi: blok 407 berjumlah 18 langkah dan blok 408 berjumlah 13 langkah (total 31, di bawah sekitar 35).
- Kolom yang di-uncheck sebelum `[Save]` pada TC-FA-FAAM-407 adalah `Code` (pilihan spec; TC hanya menyebut "satu kolom kelas ini").
