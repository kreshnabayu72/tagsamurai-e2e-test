---
id: TC-GS-NLU-E2E-085-list-setup-column-bagian-2
title: "List Setup Column bagian 2: Pin dan Unpin, Reset to Default, tutup tanpa Save, kolom visible terakhir, cache terpisah dari Login User, dan baris yang tidak muncul"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-NLU-291
  - TC-GS-NLU-292
  - TC-GS-NLU-293
  - TC-GS-NLU-294
  - TC-GS-NLU-295
  - TC-GS-NLU-296
coverage:
  web: automated
---

# List Setup Column bagian 2: Pin dan Unpin, Reset to Default, tutup tanpa Save, kolom visible terakhir, cache terpisah dari Login User, dan baris yang tidak muncul

## Prerequisites

- Mode: FE+BE (backend nyata). Konfigurasi kolom tersimpan di browser (tanpa request tulis ke server).
- Akun aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1; `{namaCompany}` diisi sesuai Client uji). Login sekali di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password lewat `Spectra.env.GS_TC_PASSWORD`, tidak ditulis di spec atau fixture.
- Layar awal: Global Settings > User > User List > sub-tab Non-Login User, dibuka hook `beforeEach` suite.
- Data Pre-setup (No. 9 sampai 13; hanya dibaca, tidak diubah, tanpa suffix): Non-Login User Pre-setup; Custom Field dasar `Blood Type`, `Emergency Phone`, `Badge Note` (Active); tabel sub-tab Login User memiliki kolom Position (TC-GS-NLU-295). Kolom default List Non-Login User: Active, Name, Position, Division, Employee ID, Represented By, Last Update. Fixture baru `Fixture.nonLoginUser.preSetup` (belum ada).
- Data Dinamis: tidak ada. Spec ini tidak menulis atau menghapus data.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-non-login-user` true untuk akun Total Control dan hook suite `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: muat ulang halaman (F5; tidak ada form terbuka); drag and drop baris di popup Setup Column; pengaturan lebar viewport agar tabel dapat digulir horizontal dan pemulihannya; penghapusan preferensi kolom di browser di hook `after` (disediakan tim FE), bukan `[Reset to Default]`.
- State global: konfigurasi kolom tabel List Non-Login User; dipulihkan oleh langkah penghubung dan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-291: Pin dan Unpin kolom pada Setup Column

1. Perkecil viewport hingga tabel dapat digulir horizontal
2. Klik `⋯` header Actions > `Setup Column...`, Pin kolom pertama, klik `[Save]`
3. Gulir tabel horizontal
4. Verifikasi kolom pertama membeku saat scroll horizontal
5. Klik `⋯` header Actions > `Setup Column...`, Unpin kolom pertama, klik `[Save]`
6. Gulir tabel horizontal
7. Verifikasi kolom pertama kembali ikut bergeser
8. Pulihkan viewport

### TC-GS-NLU-292: Reset to Default pada Setup Column

9. Klik `⋯` header Actions > `Setup Column...`, hapus centang kolom Division dan drag kolom Last Update ke posisi pertama
10. Klik `[Reset to Default]`
11. Verifikasi Live Preview kembali ke default modul
12. Klik `[Save]`
13. Verifikasi tabel mengikuti default modul
14. Tekan F5
15. Verifikasi tabel tetap mengikuti default modul setelah refresh

### TC-GS-NLU-293: Menutup Setup Column tanpa Save membuang perubahan

16. Klik `⋯` header Actions > `Setup Column...`, hapus centang kolom Division
17. Klik `✕`
18. Verifikasi modal tertutup
19. Verifikasi kolom Division kembali tampil seperti konfigurasi tersimpan
20. Klik `⋯` header Actions > `Setup Column...`, hapus centang kolom Division
21. Tekan `Esc`
22. Verifikasi modal tertutup
23. Verifikasi kolom Division kembali tampil seperti konfigurasi tersimpan

### TC-GS-NLU-294: Kolom visible terakhir tidak dapat dihapus centang

24. Klik `⋯` header Actions > `Setup Column...`, hapus centang semua kolom kecuali Last Update
25. Arahkan kursor ke checkbox kolom Last Update
26. Verifikasi checkbox kolom tersisa disabled
27. Verifikasi tooltip `At least one column must remain visible.`
28. Klik `✕`

### TC-GS-NLU-295: Cache Setup Column terpisah dari sub-tab Login User

29. Klik `⋯` header Actions > `Setup Column...`, hapus centang kolom Position, klik `[Save]`
30. Pindah ke sub-tab Login User
31. Verifikasi sub-tab Login User tidak ikut menyembunyikan kolom Position
32. Kembali ke sub-tab Non-Login User
33. Verifikasi sub-tab Non-Login User tetap tanpa kolom Position
34. Klik `⋯` header Actions > `Setup Column...`, centang kolom Position, klik `[Save]`

### TC-GS-NLU-296: Kolom checkbox dan Actions tidak muncul sebagai baris Setup Column

35. Klik `⋯` header Actions > `Setup Column...`
36. Verifikasi daftar kolom tidak memuat checkbox seleksi dan Actions
37. Verifikasi kolom checkbox seleksi dan Actions tetap ada di tabel
38. Klik `✕`

## Notes

- Langkah penghubung (S-03): memperkecil dan memulihkan viewport pada TC-GS-NLU-291 (S-14), `✕` yang menutup popup pada TC-GS-NLU-294 dan TC-GS-NLU-296, serta langkah terakhir TC-GS-NLU-295 yang memulihkan kolom Position (S-09); hook `after` menghapus preferensi kolom sebagai cadangan. TC-GS-NLU-293 hanya membuang perubahan sehingga tidak membutuhkan pemulihan.
- Asersi tambahan (S-03): TC-GS-NLU-292 Expected a ("tetap setelah refresh") memuat F5 yang tidak ada di langkah TC; langkah F5 ditambahkan.
- Di atas 35 langkah, alasan: Spec ini sekitar 38 langkah dan dipertahankan utuh karena seluruh blok satu kelas harness (fungsional, popup Setup Column yang sama, tanpa data milik spec) dan berdiri sendiri: kegagalan satu TC Setup Column tidak membuat TC lain kehilangan makna.
- Temuan untuk QA:
  - TC-GS-NLU-291 tidak menyebut cara membuat tabel dapat digulir horizontal; spec memperkecil viewport.
  - TC-GS-NLU-292 langkah 1 ("ubah visibilitas dan urutan kolom") tidak merinci perubahan; spec menyembunyikan Division dan menggeser Last Update ke posisi pertama.
  - TC-GS-NLU-295 mensyaratkan sub-tab Login User memiliki kolom Position tanpa menyebutnya di precondition.
