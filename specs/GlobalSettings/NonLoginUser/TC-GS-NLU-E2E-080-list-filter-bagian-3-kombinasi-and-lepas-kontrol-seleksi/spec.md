---
id: TC-GS-NLU-E2E-080-list-filter-bagian-3-kombinasi-and-lepas-kontrol-seleksi
title: "List Filter bagian 3: kombinasi AND dengan Search, melepas satu kontrol, seleksi dipertahankan, dan Create baru yang tidak cocok"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-NLU-275
  - TC-GS-NLU-276
  - TC-GS-NLU-277
  - TC-GS-NLU-278
  - TC-GS-NLU-279
coverage:
  web: automated
---

# List Filter bagian 3: kombinasi AND dengan Search, melepas satu kontrol, seleksi dipertahankan, dan Create baru yang tidak cocok

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1; `{namaCompany}` diisi sesuai Client uji). Login sekali di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password lewat `Spectra.env.GS_TC_PASSWORD`, tidak ditulis di spec atau fixture.
- Layar awal: Global Settings > User > User List > sub-tab Non-Login User, dibuka hook `beforeEach` suite.
- Data Pre-setup (No. 9 sampai 12; hanya dibaca, tidak diubah, tanpa suffix): Non-Login User `Budi Kurniawan` (Field Technician, Operations, Active), `Rina Marlina` (Driver, Logistics, Temporary), `Joko Susilo` dan `Agus Salim` (Contractor, Operations, Inactive); Login User `Ahmad Fauzi` (Represented By). Fixture baru `Fixture.nonLoginUser.preSetup` (belum ada).
- Data Dinamis (dibuat TC-GS-NLU-279 lewat UI, dihapus lewat API di hook `after`): Non-Login User `Zulfa` `Hanif {runId}-080` dengan email `zulfahanif+{runId}-080@qwertysystem.net`, Division `Operations`, Represented By `Ahmad Fauzi`. Field wajib lain tidak disebut TC-GS-NLU-279; pola isian mengikuti TC-GS-NLU-490.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-non-login-user` true untuk akun Total Control dan hook suite `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pembacaan ikon sort pada header kolom; penghapusan data lewat API di hook `after` (disediakan tim FE/BE).
- State global: tidak ada yang diubah. State Search, Filter, Sort, dan seleksi dibersihkan oleh langkah penghubung (29 dan langkah akhir tiap TC). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-275: Filter tetap berlaku walau kolom disembunyikan dan Clear Field membersihkan filter

1. Buka Filter Panel, pilih Division `Operations`, klik `[Apply]`
2. Klik `⋯` pada header kolom Actions, hapus centang kolom Division, tutup overlay Column Visibility
3. Verifikasi Filter Division tetap berlaku: tabel tidak kosong dan baris `Rina Marlina` (Division `Logistics`) tidak tampil
4. Buka Filter Panel
5. Verifikasi field Division tetap ada di panel dan berisi `Operations`
6. Klik `[Clear Field]`, klik `[Apply]`
7. Verifikasi tabel kembali penuh: baris `Rina Marlina` tampil
8. Klik `⋯` pada header kolom Actions, centang kembali kolom Division, tutup overlay Column Visibility

### TC-GS-NLU-276: Kombinasi multi-field filter menggunakan logika AND dan Search beririsan simetris

9. Buka Filter Panel, pilih Position `Contractor` dan Active `Inactive`, klik `[Apply]`
10. Ketik Search `Joko`, tekan Enter
11. Verifikasi hasil adalah irisan kedua filter dan keyword: baris `Joko Susilo` tampil dan baris `Agus Salim` tidak tampil
12. Klik `(←)` pada kotak Search, buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`
13. Ketik Search `Joko`, tekan Enter
14. Buka Filter Panel, pilih Position `Contractor` dan Active `Inactive`, klik `[Apply]`
15. Verifikasi urutan Search lalu Filter menghasilkan baris identik dengan urutan Filter lalu Search: baris `Joko Susilo` tampil dan baris `Agus Salim` tidak tampil
16. Klik `(←)` pada kotak Search, buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`

### TC-GS-NLU-277: Melepas satu kontrol mempertahankan kontrol lain dan memulihkan empty state

17. Buka Filter Panel, pilih Position `Driver`, klik `[Apply]`
18. Ketik Search `zzzxxx`, tekan Enter
19. Klik header kolom `Name` dua kali (ascending lalu descending)
20. Verifikasi kombinasi menghasilkan `No results found`
21. Klik `(←)` pada kotak Search
22. Verifikasi data pulih: baris `Rina Marlina` tampil
23. Verifikasi Filter tetap aktif: baris `Budi Kurniawan` tidak tampil
24. Verifikasi Sort tetap aktif: ikon sort header `Name` menunjukkan descending
25. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`
26. Verifikasi Search dan Sort tetap setelah Clear Field: kotak Search kosong dan ikon sort header `Name` menunjukkan descending
27. Klik header kolom `Division`
28. Verifikasi ganti sort tidak mereset Search maupun Filter: kotak Search kosong dan ikon Filter tanpa titik indikator
29. Klik header kolom `Division` dua kali lagi hingga kembali ke default sort

### TC-GS-NLU-278: Seleksi checkbox dipertahankan saat Search atau Filter berubah

30. Centang baris `Budi Kurniawan`
31. Ketik Search `Rina`, tekan Enter
32. Klik `(←)` pada kotak Search
33. Verifikasi baris `Budi Kurniawan` masih tercentang setelah Search dikosongkan
34. Hapus centang baris `Budi Kurniawan`

### TC-GS-NLU-279: Create baru yang tidak cocok kriteria Search tidak muncul di tabel tersaring

35. Ketik Search `Rina`, tekan Enter
36. Klik `[+ Non-Login User]`
37. Isi First Name `Zulfa`, isi Last Name `Hanif {runId}-080`, pilih Division `Operations`, isi Email `zulfahanif+{runId}-080@qwertysystem.net`
38. Klik `[+ Select User]`, klik baris `Ahmad Fauzi` pada popup Select User, klik `[Select]`
39. Pastikan Stay on form tidak dicentang, klik `[Submit]`
40. Verifikasi toast sukses `Success, non-login user has been created.`
41. Verifikasi `Zulfa Hanif {runId}-080` tidak muncul di tabel yang masih tersaring `Rina` (baris `Rina Marlina` tampil)
42. Klik `(←)` pada kotak Search
43. Klik header kolom `Name` dua kali (descending)
44. Verifikasi `Zulfa Hanif {runId}-080` tampil
45. Klik header kolom `Name` sekali lagi hingga kembali ke default sort

## Notes

- Langkah penghubung (S-03): menutup overlay Column Visibility dan memulihkan kolom Division, `(←)` serta `[Clear Field]` dan `[Apply]` yang membersihkan Search dan Filter antar TC (S-09), memulihkan sort pada langkah 29, menghapus centang seleksi, serta sort Name descending pada TC-GS-NLU-279 supaya record bernama berawalan `Z` terlihat di halaman 1 (S-14). Asumsi dari TC-GS-NLU-274 dan TC-GS-NLU-275: `[Apply]` menutup Filter Panel.
- Di atas 35 langkah, alasan: Spec ini 45 langkah dan dipertahankan utuh karena seluruh blok satu kelas harness (fungsional, kombinasi Search, Filter, Sort, dan seleksi pada tabel List yang sama) dan berdiri sendiri: kegagalan satu TC tidak membuat TC lain kehilangan makna. TC-GS-NLU-279 (satu-satunya yang membuat data) berada di akhir spec dan memakai data milik spec, sehingga kegagalan kerasnya tidak menutupi hasil TC lain.
- Asersi tambahan (S-03): baris pembanding `Rina Marlina` dan `Budi Kurniawan` menjadi anchor asersi absence dan universal (bagian 8b butir 2); toast sukses Create diambil dari TC-GS-NLU-490 sebagai bukti "tersimpan" pada TC-GS-NLU-279.
- Temuan untuk QA:
  - TC-GS-NLU-277: langkah 2 mengosongkan Search sebelum langkah 3 dan 4, sehingga Expected c ("Search dan Sort tetap") dan d ("ganti sort tidak mereset Search maupun Filter") terjadi ketika Search dan Filter sudah kosong; spec mengasersi keadaan kosong itu dan Sort descending yang tetap.
  - TC-GS-NLU-278 judul menyebut Search atau Filter berubah, tetapi langkah hanya mengubah Search.
  - TC-GS-NLU-279 tidak menyebut field wajib selain nama dan email; spec memakai Division dan Represented By seperti TC-GS-NLU-490.
  - Posisi baris pada halaman 1 (mis. `Budi Kurniawan` pada TC-GS-NLU-278) bergantung pada urutan default Name A-Z dan populasi Pre-setup.
