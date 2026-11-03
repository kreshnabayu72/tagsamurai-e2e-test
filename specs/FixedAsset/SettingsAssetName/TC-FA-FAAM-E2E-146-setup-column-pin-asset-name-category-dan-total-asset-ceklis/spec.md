---
id: TC-FA-FAAM-E2E-146-setup-column-pin-asset-name-category-dan-total-asset-ceklis
title: "Setup Column: Pin Kelas Asset Name dan Category serta Ceklis Total Asset"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-406
  - TC-FA-FAAM-412
  - TC-FA-FAAM-419
coverage:
  web: automated
---

# Setup Column: Pin Kelas Asset Name dan Category serta Ceklis Total Asset

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`).
- Kemampuan teknis: drag and drop, scroll horizontal tabel, hapus preferensi kolom di browser (disediakan tim FE).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: konfigurasi kolom tabel utama (preferensi di browser) diubah spec ini. Pemulihan: hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE; spec ini terdaftar di `suite.md`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-406: Setup Column pin dan unpin kelas Asset Name (text link)
1. Buka Popup Setup Column
2. Pin kolom `Asset Name`, lalu klik `[Save]`
3. Scroll tabel secara horizontal
4. Verifikasi kolom `Asset Name` membeku di sisi kiri saat scroll horizontal
5. Tekan F5
6. Scroll tabel secara horizontal
7. Verifikasi kolom `Asset Name` tetap membeku di sisi kiri setelah F5
8. Buka Popup Setup Column
9. Unpin kolom `Asset Name`, lalu klik `[Save]`
10. Scroll tabel secara horizontal
11. Verifikasi kolom `Asset Name` bergeser normal saat scroll
### TC-FA-FAAM-412: Setup Column pin dan unpin kelas Category (badge)
12. Buka Popup Setup Column
13. Pin kolom `Category`, lalu klik `[Save]`
14. Scroll tabel secara horizontal
15. Verifikasi kolom `Category` membeku di sisi kiri saat scroll horizontal
16. Tekan F5
17. Scroll tabel secara horizontal
18. Verifikasi kolom `Category` tetap membeku di sisi kiri setelah F5
19. Buka Popup Setup Column
20. Unpin kolom `Category`, lalu klik `[Save]`
21. Scroll tabel secara horizontal
22. Verifikasi kolom `Category` bergeser normal saat scroll
### TC-FA-FAAM-419: Setup Column ceklis dan unceklis kelas Total Asset (angka)
23. Buka Popup Setup Column: klik header kolom Actions (⋯), lalu `Setup Column...`
24. Uncheck kolom `Total Asset`
25. Verifikasi kolom `Total Asset` hilang dari Live Preview dan dari tabel di balik modal
26. Check kembali kolom `Total Asset`
27. Verifikasi kolom `Total Asset` muncul kembali di Live Preview dan di tabel di balik modal
28. Uncheck kolom `Total Asset`, lalu klik `[Save]`
29. Verifikasi kolom `Total Asset` tersembunyi di tabel
30. Tekan F5
31. Verifikasi kolom `Total Asset` tetap tersembunyi setelah F5
32. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, lalu tekan F5

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): membuka Popup Setup Column dan pemulihan konfigurasi kolom (hapus preferensi kolom di browser lalu F5) di akhir blok supaya blok berikutnya mulai dari konfigurasi bawaan (S-09).
- Persistensi "tersimpan di `localStorage`" diamati lewat F5 (tersembunyi atau urutan tetap), bukan lewat pembacaan penyimpanan browser.
- Pada blok pin, unpin dilakukan dengan membuka Popup Setup Column kembali karena `[Save]` menutup popup (langkah 4 TC: "Unpin kolom lalu Save").
