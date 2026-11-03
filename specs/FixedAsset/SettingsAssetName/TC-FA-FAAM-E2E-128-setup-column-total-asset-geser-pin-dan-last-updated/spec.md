---
id: TC-FA-FAAM-E2E-128-setup-column-total-asset-geser-pin-dan-last-updated
title: "Setup Column: Total Asset Geser dan Pin serta Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-420
  - TC-FA-FAAM-421
  - TC-FA-FAAM-422
  - TC-FA-FAAM-423
  - TC-FA-FAAM-424
coverage:
  web: automated
---

# Setup Column: Total Asset Geser dan Pin serta Last Updated

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`).
- Kemampuan teknis: drag and drop, scroll horizontal tabel, hapus preferensi kolom di browser (disediakan tim FE).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: konfigurasi kolom tabel utama (preferensi di browser) diubah spec ini. Pemulihan: hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE; spec ini terdaftar di `suite.md`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-420: Setup Column geser urutan kelas Total Asset (angka)
1. Buka Popup Setup Column
2. Drag kolom `Total Asset` satu posisi ke atas
3. Verifikasi urutan kolom `Total Asset` berubah di Live Preview dan di tabel
4. Klik `[Save]`
5. Tekan F5
6. Verifikasi urutan baru kolom `Total Asset` tetap setelah Save dan F5
7. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, lalu tekan F5
### TC-FA-FAAM-421: Setup Column pin dan unpin kelas Total Asset (angka)
8. Buka Popup Setup Column
9. Pin kolom `Total Asset`, lalu klik `[Save]`
10. Scroll tabel secara horizontal
11. Verifikasi kolom `Total Asset` membeku di sisi kiri saat scroll horizontal
12. Tekan F5
13. Scroll tabel secara horizontal
14. Verifikasi kolom `Total Asset` tetap membeku di sisi kiri setelah F5
15. Buka Popup Setup Column
16. Unpin kolom `Total Asset`, lalu klik `[Save]`
17. Scroll tabel secara horizontal
18. Verifikasi kolom `Total Asset` bergeser normal saat scroll
### TC-FA-FAAM-422: Setup Column ceklis dan unceklis kelas Last Updated (tanggal)
19. Buka Popup Setup Column: klik header kolom Actions (⋯), lalu `Setup Column...`
20. Uncheck kolom `Last Updated`
21. Verifikasi kolom `Last Updated` hilang dari Live Preview dan dari tabel di balik modal
22. Check kembali kolom `Last Updated`
23. Verifikasi kolom `Last Updated` muncul kembali di Live Preview dan di tabel di balik modal
24. Uncheck kolom `Last Updated`, lalu klik `[Save]`
25. Verifikasi kolom `Last Updated` tersembunyi di tabel
26. Tekan F5
27. Verifikasi kolom `Last Updated` tetap tersembunyi setelah F5
28. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, lalu tekan F5
### TC-FA-FAAM-423: Setup Column geser urutan kelas Last Updated (tanggal)
29. Buka Popup Setup Column
30. Drag kolom `Last Updated` satu posisi ke atas
31. Verifikasi urutan kolom `Last Updated` berubah di Live Preview dan di tabel
32. Klik `[Save]`
33. Tekan F5
34. Verifikasi urutan baru kolom `Last Updated` tetap setelah Save dan F5
35. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, lalu tekan F5
### TC-FA-FAAM-424: Setup Column pin dan unpin kelas Last Updated (tanggal)
36. Buka Popup Setup Column
37. Pin kolom `Last Updated`, lalu klik `[Save]`
38. Scroll tabel secara horizontal
39. Verifikasi kolom `Last Updated` membeku di sisi kiri saat scroll horizontal
40. Tekan F5
41. Scroll tabel secara horizontal
42. Verifikasi kolom `Last Updated` tetap membeku di sisi kiri setelah F5
43. Buka Popup Setup Column
44. Unpin kolom `Last Updated`, lalu klik `[Save]`
45. Scroll tabel secara horizontal
46. Verifikasi kolom `Last Updated` bergeser normal saat scroll

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): membuka Popup Setup Column dan pemulihan konfigurasi kolom (hapus preferensi kolom di browser lalu F5) di akhir blok supaya blok berikutnya mulai dari konfigurasi bawaan (S-09).
- Persistensi "tersimpan di `localStorage`" diamati lewat F5 (tersembunyi atau urutan tetap), bukan lewat pembacaan penyimpanan browser.
- Pada blok pin, unpin dilakukan dengan membuka Popup Setup Column kembali karena `[Save]` menutup popup (langkah 4 TC: "Unpin kolom lalu Save").
- Di atas smell 35 langkah. Spec berjumlah 46 langkah (melewati sekitar 35). Semua blok adalah Setup Column pada tabel utama yang sama dengan satu kelas harness dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
