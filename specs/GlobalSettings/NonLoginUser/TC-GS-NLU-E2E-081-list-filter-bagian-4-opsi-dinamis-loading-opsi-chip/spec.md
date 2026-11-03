---
id: TC-GS-NLU-E2E-081-list-filter-bagian-4-opsi-dinamis-loading-opsi-chip
title: "List Filter bagian 4: opsi dropdown dinamis, indikator loading opsi, chip +N more, dan nilai filter stale dibersihkan"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-NLU-490
  - TC-GS-NLU-491
  - TC-GS-NLU-493
  - TC-GS-NLU-500
coverage:
  web: automated
---

# List Filter bagian 4: opsi dropdown dinamis, indikator loading opsi, chip +N more, dan nilai filter stale dibersihkan

## Prerequisites

- Mode: FE+BE (backend nyata). TC-GS-NLU-491 memakai intercept penundaan respons di atas backend nyata.
- Akun aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1; `{namaCompany}` diisi sesuai Client uji). Login sekali di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password lewat `Spectra.env.GS_TC_PASSWORD`, tidak ditulis di spec atau fixture.
- Layar awal: Global Settings > User > User List > sub-tab Non-Login User, dibuka hook `beforeEach` suite.
- Data Pre-setup (No. 9 sampai 12; hanya dibaca, tidak diubah, tanpa suffix): Login User `Ahmad Fauzi` (Active) dan pool Login User Represented By lain; Position `Warehouse Supervisor` belum dipakai baris Non-Login User mana pun (Pre-setup No. 9). Fixture baru `Fixture.nonLoginUser.preSetup` (belum ada).
- Data Dinamis: Non-Login User `Opsi` `Baru {runId}-081` dengan email `opsibaru+{runId}-081@qwertysystem.net` dibuat TC-GS-NLU-490 lewat UI (Division `Operations`, Position `Warehouse Supervisor`, Represented By `Ahmad Fauzi`). Di-seed hook `before` lewat API (mekanisme disediakan tim FE/BE) untuk TC-GS-NLU-500: Login User `Wakil Filter {runId}-081` (Active) dan Non-Login User `Filter Stale Satu {runId}-081` (Represented By `Wakil Filter {runId}-081`); menggantikan `Wakil Filter` dan `Filter Stale Satu` Pre-setup agar Pre-setup tidak dihapus (S-06). Hook `after` menghapus sisa data `{runId}-081`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-non-login-user` true untuk akun Total Control dan hook suite `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: `Spectra.intercept()` untuk menunda respons request opsi dropdown Position (endpoint tidak disebut TC; dipasang tim FE) dan melepasnya; sesi API aktor untuk pelaku kedua penghapus Login User (butir sesi API pada `suite.md`).
- State global: intercept dilepas pada langkah 5 dan oleh hook `after`; state Filter dibersihkan oleh langkah penghubung. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-491: Dropdown filter menampilkan indikator loading saat opsi sedang di-fetch

1. Pasang intercept yang menunda respons request opsi dropdown Position
2. Buka Filter Panel
3. Buka dropdown Position
4. Verifikasi skeleton atau spinner mini tampil selama opsi di-fetch (bukan dropdown kosong tanpa indikator)
5. Lepaskan respons yang ditunda
6. Verifikasi opsi Position tampil
7. Klik ikon Filter untuk menutup Filter Panel

### TC-GS-NLU-493: Chip opsi terpilih yang melebihi lebar field diringkas menjadi chip +N more

8. Buka Filter Panel, buka dropdown Represented By
9. Centang seluruh opsi satu per satu sampai chip melebihi lebar field
10. Verifikasi chip ditampilkan sebanyak yang muat pada lebar field dan sisanya diringkas dalam satu chip `+N more`
11. Verifikasi jumlah chip tampil ditambah N sama dengan jumlah opsi terpilih
12. Verifikasi field tidak melebar keluar panel
13. Verifikasi field tidak digulir horizontal
14. Klik `[Clear Field]`, klik `[Apply]`

### TC-GS-NLU-500: Nilai filter yang record sumbernya dihapus dibersihkan saat filter di-reapply

15. Buka Filter Panel, pilih Represented By `Wakil Filter {runId}-081` dan `Ahmad Fauzi`, klik `[Apply]`
16. Tunggu aksi selesai (tabel termuat dengan filter ter-Apply)
17. Di sesi API admin, hapus Login User `Wakil Filter {runId}-081` hingga penghapusan tersimpan
18. Di sesi uji, buka Filter Panel dan klik `[Apply]` kembali
19. Verifikasi nilai `Wakil Filter {runId}-081` dibersihkan dari kriteria: chip `Wakil Filter {runId}-081` hilang
20. Verifikasi chip `Ahmad Fauzi` tetap
21. Verifikasi tabel mengikuti kriteria yang tersisa: sedikitnya satu baris tampil dan seluruh baris hasil ber-Represented By `Ahmad F`
22. Verifikasi tidak ada pesan error
23. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`

### TC-GS-NLU-490: Opsi dropdown filter bertambah setelah record baru dibuat tanpa muat ulang halaman

24. Buka Filter Panel, buka dropdown Position
25. Verifikasi opsi Position tidak memuat `Warehouse Supervisor`
26. Tanpa memuat ulang halaman, klik `[+ Non-Login User]`
27. Isi First Name `Opsi`
28. Isi Last Name `Baru {runId}-081`
29. Pilih Division `Operations`
30. Pilih Position `Warehouse Supervisor`
31. Isi Email `opsibaru+{runId}-081@qwertysystem.net`
32. Klik `[+ Select User]`, klik baris `Ahmad Fauzi` pada popup Select User, klik `[Select]`
33. Klik `[Submit]`
34. Verifikasi toast sukses `Success, non-login user has been created.`
35. Buka Filter Panel, buka dropdown Position
36. Verifikasi opsi `Warehouse Supervisor` muncul tanpa muat ulang halaman
37. Klik ikon Filter untuk menutup Filter Panel

## Notes

- Urutan TC di dalam spec: TC-GS-NLU-490 (membuat data) berada di akhir spec supaya kegagalan kerasnya tidak menutupi hasil TC lain (S-10).
- Di atas 35 langkah, alasan: Spec ini sekitar 37 langkah dan dipertahankan utuh karena seluruh blok satu kelas harness (fungsional dengan intercept penundaan respons sebagai pemicu state loading, tanpa asersi atas kegagalan) pada Filter Panel yang sama dan berdiri sendiri: kegagalan satu TC tidak membuat TC lain kehilangan makna; seluruh data yang dibuat milik spec.
- Langkah penghubung (S-03): menutup Filter Panel, `[Clear Field]` lalu `[Apply]` yang membersihkan Filter (S-09), dan "Tunggu aksi selesai" sebelum ganti pelaku ke sesi API (bagian 8b butir 8). Asumsi dari TC-GS-NLU-274 dan TC-GS-NLU-275: `[Apply]` menutup Filter Panel.
- Asersi tambahan (S-03): "tidak ada pesan error" pada TC-GS-NLU-500 mengikuti Expected b; toast sukses TC-GS-NLU-490 mengikuti Expected b TC itu.
- Temuan untuk QA:
  - TC-GS-NLU-500 mensyaratkan Login User `Wakil Filter` dan `Filter Stale Satu` Pre-setup dihapus; spec memakai pasangan milik sendiri (`{runId}-081`) dan tetap mengasersi perilaku yang sama.
  - TC-GS-NLU-491 tidak menyebut endpoint opsi Position yang ditunda; endpoint dan pemasangan intercept disediakan tim FE (S-13).
  - TC-GS-NLU-490 precondition d mensyaratkan Position `Warehouse Supervisor` belum dipakai baris mana pun; Create lain yang memakai Position itu harus dibersihkan spec masing-masing.
  - TC-GS-NLU-493 tidak menyebut jumlah opsi Represented By; jumlah dibaca dari dropdown.
