---
id: TC-FA-FAAM-E2E-130-setup-column-kelas-teks-pin-dan-chip-ceklis
title: "Setup Column: Kelas Teks Pin dan Kelas Chip +N more Ceklis"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-409
  - TC-FA-FAAM-416
coverage:
  web: automated
---

# Setup Column: Kelas Teks Pin dan Kelas Chip +N more Ceklis

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`).
- Kemampuan teknis: drag and drop, scroll horizontal tabel, hapus preferensi kolom di browser (disediakan tim FE).
- Kolom yang diuji untuk TC-FA-FAAM-409 (tiga kolom di-pin sekaligus, batas maksimal tiga) dan TC-FA-FAAM-416 (diulang pada langkah 19 sampai 22):

  | Kolom TC-FA-FAAM-409 | Kolom TC-FA-FAAM-416 |
  |---|---|
  | Code | Brand |
  | UoM | Model/Type |
  | Modified By | Default Addon |
  |  | Default Label |
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: konfigurasi kolom tabel utama (preferensi di browser) diubah spec ini. Pemulihan: hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE; spec ini terdaftar di `suite.md`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-409: Setup Column pin dan unpin kelas Code, UoM, Modified By (teks)
1. Buka Popup Setup Column: klik header kolom Actions (⋯), lalu `Setup Column...`
2. Pin kolom `Code`, `UoM`, dan `Modified By` satu per satu (tiga kolom ter-pin sekaligus), lalu klik `[Save]`
3. Scroll tabel secara horizontal
4. Verifikasi kolom `Code` membeku di sisi kiri saat scroll horizontal
5. Verifikasi kolom `UoM` membeku di sisi kiri saat scroll horizontal
6. Verifikasi kolom `Modified By` membeku di sisi kiri saat scroll horizontal
7. Tekan F5
8. Scroll tabel secara horizontal
9. Verifikasi kolom `Code` tetap membeku di sisi kiri setelah F5
10. Verifikasi kolom `UoM` tetap membeku di sisi kiri setelah F5
11. Verifikasi kolom `Modified By` tetap membeku di sisi kiri setelah F5
12. Buka Popup Setup Column
13. Unpin kolom `Code`, `UoM`, dan `Modified By`, lalu klik `[Save]`
14. Scroll tabel secara horizontal
15. Verifikasi kolom `Code` bergeser normal saat scroll
16. Verifikasi kolom `UoM` bergeser normal saat scroll
17. Verifikasi kolom `Modified By` bergeser normal saat scroll
### TC-FA-FAAM-416: Setup Column ceklis dan unceklis kelas Brand, Model/Type, Default Addon, Default Label (chip +N more)
18. Buka Popup Setup Column
19. Untuk setiap baris kolom TC-FA-FAAM-416 pada tabel "Kolom yang diuji", uncheck kolom tersebut
20. Verifikasi kolom hilang dari Live Preview dan dari tabel di balik modal
21. Check kembali kolom tersebut
22. Verifikasi kolom muncul kembali di Live Preview dan di tabel di balik modal
23. Uncheck kolom `Brand`, lalu klik `[Save]`
24. Verifikasi kolom `Brand` tersembunyi di tabel
25. Tekan F5
26. Verifikasi kolom `Brand` tetap tersembunyi setelah F5
27. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, lalu tekan F5

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): membuka Popup Setup Column dan pemulihan konfigurasi kolom (hapus preferensi kolom di browser lalu F5) di akhir blok supaya blok berikutnya mulai dari konfigurasi bawaan (S-09).
- Persistensi "tersimpan di `localStorage`" diamati lewat F5 (tersembunyi atau urutan tetap), bukan lewat pembacaan penyimpanan browser.
- Pada TC-FA-FAAM-409 ketiga kolom di-pin sekaligus (batas maksimal tiga, TC-FA-FAAM-428); langkah TC "satu per satu (maksimal tiga sekaligus)" dibaca sebagai memin kolom berurutan sampai tiga kolom ter-pin.
- Langkah yang diulang per kolom pada TC-FA-FAAM-416: langkah 19 sampai 22; parameter tiap iterasi ada di tabel "Kolom yang diuji" (kolom TC-FA-FAAM-416). Verifikasi diulang satu per klausa (bagian 8b butir 7). Ekspansi: 4 kolom x 4 langkah = 16 langkah (dari 4 langkah nominal).
- Kolom yang di-uncheck sebelum `[Save]` pada TC-FA-FAAM-416 adalah `Brand` (pilihan spec; TC hanya menyebut "satu kolom kelas ini").
- Spec berjumlah 39 langkah setelah ekspansi (blok 409 berjumlah 17 langkah, blok 416 berjumlah 22 langkah), melewati sekitar 35. Semua blok adalah Setup Column pada tabel utama yang sama dengan satu kelas harness dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
