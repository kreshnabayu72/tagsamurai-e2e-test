---
id: TC-FA-NOTIF-E2E-050-filter-date-satu-tanggal-zona-waktu-dan-kombinasi
title: "Filter Date: Satu Tanggal, Batas Hari, Zona Waktu Tenant, Kombinasi dengan Event Type, dan Empty State"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-205
  - TC-FA-NOTIF-206
  - TC-FA-NOTIF-207
  - TC-FA-NOTIF-208
  - TC-FA-NOTIF-426
coverage:
  web: automated
---

# Filter Date: Satu Tanggal, Batas Hari, Zona Waktu Tenant, Kombinasi dengan Event Type, dan Empty State

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; General Settings `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, jam fixture 18/06/26). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: seed N-01 sampai N-37 (Pre-setup #17 dan #18, total 37 notifikasi; tidak ada notifikasi dibuat pada 01/01/26) milik akun aktor, dipulihkan fixture BE pemulih di hook `before` dan `after`.
- Data Dinamis: tiga notifikasi uji milik spec dibuat fixture BE pembuat notifikasi dengan waktu pembuatan ditentukan (disediakan tim FE/BE; endpoint tidak dikarang), Title bersuffix `{runId}-050`, dihapus di hook `after`: `Batas Hari A {runId}-050` dibuat 18/06/26 23:59:59 Asia/Jakarta, `Batas Hari B {runId}-050` dibuat 19/06/26 00:00:00 Asia/Jakarta, dan `Zona UTC {runId}-050` dibuat 18/06/26 20:00 UTC. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- State global: TC-207 mengubah Time Zone General Settings tenant ke `(UTC+00:00) UTC` lewat fixture BE penyetel General Settings (disediakan tim FE/BE) dan memulihkannya ke `Asia/Jakarta` pada langkah 20 serta di hook `after`. Suite berjalan serial (`parallel: false`).
- Hook suite yang berlaku (rujukan ke `suite.md`): flag Guided Tooltip (akun #1 sudah true) dan fixture BE pemulih seed notifikasi.

## Test Steps

### TC-FA-NOTIF-205: Filter Date menyaring notifikasi pada satu tanggal kalender

1. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center
2. Klik icon Filter, pilih tanggal 18/06/26 pada field `Date`, lalu klik `[Apply]`
3. Scroll sampai akhir list hingga seluruh item termuat
4. Verifikasi list memuat sedikitnya satu item
5. Verifikasi list hanya memuat notifikasi yang dibuat pada 18/06/26

### TC-FA-NOTIF-206: Filter Date batas 23:59:59 dan 00:00:00 pada zona waktu tenant

6. Buat dua notifikasi uji lewat fixture BE pembuat notifikasi: `Batas Hari A {runId}-050` pada 18/06/26 23:59:59 dan `Batas Hari B {runId}-050` pada 19/06/26 00:00:00 (zona Asia/Jakarta), muat ulang halaman, lalu klik Bell icon dan `[Show All]`
7. Klik icon Filter, pilih tanggal 18/06/26 pada field `Date`, lalu klik `[Apply]`
8. Scroll sampai akhir list hingga seluruh item termuat
9. Verifikasi notifikasi `Batas Hari A {runId}-050` tampil
10. Verifikasi notifikasi `Batas Hari B {runId}-050` tidak tampil
11. Pilih tanggal 19/06/26 pada field `Date`, lalu klik `[Apply]`
12. Scroll sampai akhir list hingga seluruh item termuat
13. Verifikasi notifikasi `Batas Hari B {runId}-050` tampil
14. Verifikasi notifikasi `Batas Hari A {runId}-050` tidak tampil

### TC-FA-NOTIF-207: Filter Date mengikuti zona waktu tenant yang berbeda

15. Ubah Time Zone General Settings tenant ke `(UTC+00:00) UTC` lewat fixture BE penyetel General Settings, buat notifikasi uji `Zona UTC {runId}-050` pada 18/06/26 20:00 UTC lewat fixture BE pembuat notifikasi, muat ulang halaman, lalu klik Bell icon dan `[Show All]`
16. Klik icon Filter, pilih tanggal 18/06/26 pada field `Date`, lalu klik `[Apply]`
17. Scroll sampai akhir list hingga seluruh item termuat
18. Verifikasi notifikasi `Zona UTC {runId}-050` tampil pada tanggal 18/06/26 sesuai zona waktu tenant
19. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
20. Pulihkan Time Zone General Settings tenant ke `Asia/Jakarta` lewat fixture BE penyetel General Settings, lalu muat ulang halaman

### TC-FA-NOTIF-208: Filter Event Type dan Date digabung dengan logika AND

21. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
22. Klik icon Filter, centang `Damaged Repaired`, pilih tanggal 18/06/26 pada field `Date`, lalu klik `[Apply]`
23. Scroll sampai akhir list hingga seluruh item termuat
24. Verifikasi list memuat sedikitnya satu item
25. Verifikasi list hanya memuat notifikasi `damaged_repaired` yang dibuat pada 18/06/26

### TC-FA-NOTIF-426: Filter Date pada tanggal tanpa notifikasi menampilkan empty state filtered S-07

26. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
27. Klik icon Filter, pilih tanggal 01/01/26 pada field `Date`, lalu klik `[Apply]`
28. Verifikasi empty state tampil dengan Illustration, Title `No results found`, dan Description `Try adjusting your search or filter.`
29. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 19, 21, 26, 29 (masuk kembali lewat `[Show All]` yang mereset kontrol ke default; perilaku reset ini diasersi spec 114), 6 dan 15 (pembuatan notifikasi uji dan muat ulang), 3, 8, 12, 17, 23 (memuat seluruh item), 20 (pemulihan state global Time Zone, aksi tanpa `Verifikasi`).
- Asersi tambahan di luar Expected TC (S-03): langkah 4 dan 24 (item pembanding sebelum asersi universal, 8b butir 2), langkah 9 dan 13 (anchor positif sebelum asersi absence langkah 10 dan 14, 8b butir 2).
- Urutan langkah 9 sebelum 10 dan 13 sebelum 14 mengikuti anchor positif sebelum absence; klausa "hanya notifikasi ..." TC-206 dipecah menjadi tampil dan tidak tampil.
- Temuan untuk QA:
  - TC-205, 206, 208 tidak menyebut cara membaca tanggal pembuatan item pada list (item notifikasi memakai timestamp relatif untuk umur kurang dari 7 hari); spec mengasersi himpunan item dan, untuk TC-206 dan 207, item bernama milik spec. Asersi "dibuat pada 18/06/26" untuk seluruh item mengandalkan tanggal pembuatan seed di fixture.
  - TC-206 dan 207 tidak menyebut Title notifikasi uji dan cara membuatnya dengan waktu pembuatan tertentu; spec memakai Title bersuffix dan fixture BE pembuat notifikasi (disediakan tim FE/BE).
  - TC-207 mengubah Time Zone General Settings tenant tanpa menyebut cara pengubahannya; spec memakai fixture BE penyetel General Settings.
