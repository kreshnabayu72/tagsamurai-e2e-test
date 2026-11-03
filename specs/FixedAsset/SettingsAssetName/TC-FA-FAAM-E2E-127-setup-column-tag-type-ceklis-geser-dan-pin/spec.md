---
id: TC-FA-FAAM-E2E-127-setup-column-tag-type-ceklis-geser-dan-pin
title: "Setup Column: Ceklis, Geser, dan Pin Kelas TAG Type"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-413
  - TC-FA-FAAM-414
  - TC-FA-FAAM-415
coverage:
  web: automated
---

# Setup Column: Ceklis, Geser, dan Pin Kelas TAG Type

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`).
- Kemampuan teknis: drag and drop, scroll horizontal tabel, hapus preferensi kolom di browser (disediakan tim FE).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: konfigurasi kolom tabel utama (preferensi di browser) diubah spec ini. Pemulihan: hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE; spec ini terdaftar di `suite.md`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-413: Setup Column ceklis dan unceklis kelas TAG Type (icon)
1. Buka Popup Setup Column: klik header kolom Actions (⋯), lalu `Setup Column...`
2. Uncheck kolom `TAG Type`
3. Verifikasi kolom `TAG Type` hilang dari Live Preview dan dari tabel di balik modal
4. Check kembali kolom `TAG Type`
5. Verifikasi kolom `TAG Type` muncul kembali di Live Preview dan di tabel di balik modal
6. Uncheck kolom `TAG Type`, lalu klik `[Save]`
7. Verifikasi kolom `TAG Type` tersembunyi di tabel
8. Tekan F5
9. Verifikasi kolom `TAG Type` tetap tersembunyi setelah F5
10. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, lalu tekan F5
### TC-FA-FAAM-414: Setup Column geser urutan kelas TAG Type (icon)
11. Buka Popup Setup Column
12. Drag kolom `TAG Type` satu posisi ke atas
13. Verifikasi urutan kolom `TAG Type` berubah di Live Preview dan di tabel
14. Klik `[Save]`
15. Tekan F5
16. Verifikasi urutan baru kolom `TAG Type` tetap setelah Save dan F5
17. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, lalu tekan F5
### TC-FA-FAAM-415: Setup Column pin dan unpin kelas TAG Type (icon)
18. Buka Popup Setup Column
19. Pin kolom `TAG Type`, lalu klik `[Save]`
20. Scroll tabel secara horizontal
21. Verifikasi kolom `TAG Type` membeku di sisi kiri saat scroll horizontal
22. Tekan F5
23. Scroll tabel secara horizontal
24. Verifikasi kolom `TAG Type` tetap membeku di sisi kiri setelah F5
25. Buka Popup Setup Column
26. Unpin kolom `TAG Type`, lalu klik `[Save]`
27. Scroll tabel secara horizontal
28. Verifikasi kolom `TAG Type` bergeser normal saat scroll

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): membuka Popup Setup Column dan pemulihan konfigurasi kolom (hapus preferensi kolom di browser lalu F5) di akhir blok supaya blok berikutnya mulai dari konfigurasi bawaan (S-09).
- Persistensi "tersimpan di `localStorage`" diamati lewat F5 (tersembunyi atau urutan tetap), bukan lewat pembacaan penyimpanan browser.
- Pada blok pin, unpin dilakukan dengan membuka Popup Setup Column kembali karena `[Save]` menutup popup (langkah 4 TC: "Unpin kolom lalu Save").
