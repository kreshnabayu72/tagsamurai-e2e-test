---
id: TC-FA-FAAM-E2E-131-setup-column-kelas-chip-geser-dan-pin
title: "Setup Column: Kelas Chip +N more Geser dan Pin"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-417
  - TC-FA-FAAM-418
coverage:
  web: automated
---

# Setup Column: Kelas Chip +N more Geser dan Pin

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`).
- Kemampuan teknis: drag and drop, scroll horizontal tabel, hapus preferensi kolom di browser (disediakan tim FE).
- Kolom yang diuji (kolom TC-FA-FAAM-417 diulang pada langkah 2 sampai 3; ronde pin TC-FA-FAAM-418 maksimal tiga kolom sekaligus, kolom keempat pada ronde kedua):

  | Kolom | Ronde pin TC-FA-FAAM-418 |
  |---|---|
  | Brand | 1 |
  | Model/Type | 1 |
  | Default Addon | 1 |
  | Default Label | 2 |
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: konfigurasi kolom tabel utama (preferensi di browser) diubah spec ini. Pemulihan: hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE; spec ini terdaftar di `suite.md`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-417: Setup Column geser urutan kelas Brand, Model/Type, Default Addon, Default Label (chip +N more)
1. Buka Popup Setup Column: klik header kolom Actions (⋯), lalu `Setup Column...`
2. Untuk setiap baris tabel "Kolom yang diuji", drag kolom tersebut satu posisi ke atas
3. Verifikasi urutan kolom berubah di Live Preview dan di tabel
4. Klik `[Save]`
5. Tekan F5
6. Verifikasi urutan baru kolom `Brand` tetap setelah Save dan F5
7. Verifikasi urutan baru kolom `Model/Type` tetap setelah Save dan F5
8. Verifikasi urutan baru kolom `Default Addon` tetap setelah Save dan F5
9. Verifikasi urutan baru kolom `Default Label` tetap setelah Save dan F5
10. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, lalu tekan F5
### TC-FA-FAAM-418: Setup Column pin dan unpin kelas Brand, Model/Type, Default Addon, Default Label (chip +N more)
11. Buka Popup Setup Column
12. Pin kolom ronde 1 (`Brand`, `Model/Type`, `Default Addon`) satu per satu (tiga kolom ter-pin sekaligus), lalu klik `[Save]`
13. Scroll tabel secara horizontal
14. Verifikasi kolom `Brand` membeku di sisi kiri saat scroll horizontal
15. Verifikasi kolom `Model/Type` membeku di sisi kiri saat scroll horizontal
16. Verifikasi kolom `Default Addon` membeku di sisi kiri saat scroll horizontal
17. Tekan F5
18. Scroll tabel secara horizontal
19. Verifikasi kolom `Brand` tetap membeku di sisi kiri setelah F5
20. Verifikasi kolom `Model/Type` tetap membeku di sisi kiri setelah F5
21. Verifikasi kolom `Default Addon` tetap membeku di sisi kiri setelah F5
22. Buka Popup Setup Column
23. Unpin kolom `Brand`, `Model/Type`, dan `Default Addon`, lalu klik `[Save]`
24. Scroll tabel secara horizontal
25. Verifikasi kolom `Brand` bergeser normal saat scroll
26. Verifikasi kolom `Model/Type` bergeser normal saat scroll
27. Verifikasi kolom `Default Addon` bergeser normal saat scroll
28. Buka Popup Setup Column
29. Pin kolom ronde 2 (`Default Label`), lalu klik `[Save]`
30. Scroll tabel secara horizontal
31. Verifikasi kolom `Default Label` membeku di sisi kiri saat scroll horizontal
32. Tekan F5
33. Scroll tabel secara horizontal
34. Verifikasi kolom `Default Label` tetap membeku di sisi kiri setelah F5
35. Buka Popup Setup Column
36. Unpin kolom `Default Label`, lalu klik `[Save]`
37. Scroll tabel secara horizontal
38. Verifikasi kolom `Default Label` bergeser normal saat scroll

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): membuka Popup Setup Column dan pemulihan konfigurasi kolom (hapus preferensi kolom di browser lalu F5) di akhir blok supaya blok berikutnya mulai dari konfigurasi bawaan (S-09).
- Persistensi "tersimpan di `localStorage`" diamati lewat F5 (tersembunyi atau urutan tetap), bukan lewat pembacaan penyimpanan browser.
- Langkah yang diulang per kolom pada TC-FA-FAAM-417: langkah 2 sampai 3; parameter tiap iterasi ada di tabel "Kolom yang diuji". Verifikasi diulang satu per klausa (bagian 8b butir 7).
- TC-FA-FAAM-418 menyebut empat kolom dengan "satu per satu (maksimal tiga sekaligus)"; batas pin adalah tiga kolom (TC-FA-FAAM-428), sehingga tiga kolom di-pin sekaligus pada ronde 1 dan kolom keempat pada ronde 2. Temuan untuk QA: pembagian ronde ini adalah pilihan spec karena TC tidak menyebut cara menangani kolom keempat.
- Di atas smell 35 langkah. Spec berjumlah 44 langkah setelah ekspansi (blok 417 berjumlah 16 langkah, blok 418 berjumlah 28 langkah), melewati sekitar 35. Semua blok adalah Setup Column pada tabel utama yang sama dengan satu kelas harness dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
