---
id: TC-FA-CAT-E2E-159-tabel-step-setup-column-geser-urutan-reset-dan-tutup-tanpa-save
title: "Tabel Step Category Consolidation: Setup Column Geser Urutan Kolom dengan Persistensi, Reset to Default, dan Penutupan Popup Tanpa Save"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-567
  - TC-FA-CAT-569
  - TC-FA-CAT-570
coverage:
  web: automated
---

# Tabel Step Category Consolidation: Setup Column Geser Urutan Kolom dengan Persistensi, Reset to Default, dan Penutupan Popup Tanpa Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPostT0 (Pre-setup #33), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #33 (CatPostT0, Starter cap 5, T-0 sudah lewat, belum pernah submit selection) hanya dibaca: 8 kategori root `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`.
- Kolom yang digeser pada langkah 3 dan 4 (langkah diulang untuk setiap baris tabel, berurutan): `Category Name`, `Code`, `Depth`, `Total Asset`, `Status`, `Modified By`, `Last Updated`.
- State yang diubah spec: konfigurasi kolom tabel Step (langkah 5 dan 13). Dipulihkan dengan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) di hook `after` suite; kemampuan disediakan tim FE. Hasil akhir spec sudah konfigurasi default (langkah 13).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-567: Geser urutan kolom tabel Step lewat popup dan persist (per kolom)

1. Klik `[Choose Categories]` pada Alert Category Consolidation, lalu klik header Actions (⋯) > `Setup Column...`
2. Tunggu popup `Setup Column` dengan Live Preview tabel tampil
3. Geser kolom pada tabel Kolom yang digeser ke posisi pertama pada daftar
4. Verifikasi Live Preview menempatkan kolom itu sebagai kolom data pertama
5. Klik `[Save]`
6. Tekan F5
7. Klik `[Choose Categories]` pada Alert Category Consolidation
8. Verifikasi urutan kolom data tabel Step menjadi Last Updated, Modified By, Status, Total Asset, Depth, Code, Category Name (bertahan setelah F5)

### TC-FA-CAT-569: Reset to Default mengembalikan konfigurasi bawaan setelah Save

9. Klik header Actions (⋯) > `Setup Column...`
10. Hilangkan centang kolom `Code` dan geser kolom `Last Updated` ke posisi pertama
11. Klik `[Reset to Default]`
12. Verifikasi Live Preview kembali ke kolom default berurutan Category Name, Code, Depth, Total Asset, Status, Modified By, Last Updated
13. Klik `[Save]`
14. Verifikasi tabel Step kembali ke kolom default berurutan Category Name, Code, Depth, Total Asset, Status, Modified By, Last Updated
15. Tekan F5
16. Klik `[Choose Categories]` pada Alert Category Consolidation
17. Verifikasi konfigurasi default bertahan setelah F5 (kolom berurutan Category Name, Code, Depth, Total Asset, Status, Modified By, Last Updated)

### TC-FA-CAT-570: Menutup popup Setup Column tanpa Save membuang perubahan preview

18. Klik header Actions (⋯) > `Setup Column...`
19. Hilangkan centang kolom `Code`, lalu klik icon close (✕)
20. Verifikasi tabel Step memakai konfigurasi tersimpan terakhir (kolom Code tampil) setelah ditutup lewat icon close (✕)
21. Klik header Actions (⋯) > `Setup Column...`
22. Ubah urutan kolom dengan menggeser kolom `Last Updated` ke posisi pertama, lalu tekan `Esc`
23. Verifikasi tabel Step memakai konfigurasi tersimpan terakhir (urutan default) setelah ditutup lewat `Esc`

## Notes

- Spec melewati sekitar 35 langkah setelah ekspansi (23 langkah nominal, geser tujuh kolom diulang: 2 langkah x 7 = 14, total sekitar 35 sampai 37). Alasan: seluruh blok satu kelas fungsional pada popup Setup Column tabel Step yang sama, berdiri sendiri, dan langkah geser identik per kolom dengan parameter di butir `Kolom yang digeser` (bagian 8b butir 7). Langkah yang diulang: 3 dan 4.
- Urutan: TC-FA-CAT-567 (menyimpan urutan terbalik) mendahului TC-FA-CAT-569 yang mereset ke default dan menyimpannya, sehingga TC-FA-CAT-570 mengasersi konfigurasi tersimpan terakhir berupa default (S-10, S-09).
- Langkah penghubung (S-03): langkah 1 (membuka wizard dan popup), langkah 7 dan 16 (membuka wizard sesudah F5).
- Langkah 2 adalah langkah penghubung tanpa asersi (menunggu popup tampil sebelum menggeser kolom).
- Temuan untuk QA:
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
  - TC-FA-CAT-567 Expected h menyebut urutan akhir Last Updated sampai Category Name; spec mengikuti urutan itu dan menganggap kolom digeser berurutan dari Category Name sampai Last Updated.
  - TC-FA-CAT-570 Expected tidak menyebut konfigurasi mana yang "tersimpan terakhir"; spec menganggap konfigurasi default hasil TC-FA-CAT-569.
  - TC-FA-CAT-569 langkah 5 ("Tekan F5") tidak menyebut membuka kembali wizard; spec menambah langkah 16.
