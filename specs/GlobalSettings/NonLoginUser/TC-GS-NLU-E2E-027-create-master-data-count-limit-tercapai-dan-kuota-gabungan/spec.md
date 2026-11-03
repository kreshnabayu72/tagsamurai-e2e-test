---
id: TC-GS-NLU-E2E-027-create-master-data-count-limit-tercapai-dan-kuota-gabungan
title: "Create: Master Data Count Limit tercapai dan kuota gabungan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-NLU-100
  - TC-GS-NLU-101
  - TC-GS-NLU-430
  - TC-GS-NLU-462
coverage:
  web: automated
---

# Create: Master Data Count Limit tercapai dan kuota gabungan

## Prerequisites

- Mode: FE+BE (backend nyata; Master Data Count Limit dan hitungan user Login + Non-Login dibaca dan ditegakkan oleh backend nyata).
- Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password lewat `Spectra.env.GS_TC_PASSWORD`.
- Env var: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk akun aktor (lihat `suite.md`); sesi API aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9, 10, dan 17, hanya dibaca): Division `Logistics`, Login User `Ahmad Fauzi` (pool Represented By), System Limits.
- State global yang diubah: Master Data Count Limit `1000` (Lifecycle Settings > System Limits, Pre-setup No. 17) dengan jumlah user Login + Non-Login tepat 1000 sebelum langkah 1. Penguji menurunkan limit dan menyiapkan hitungan itu di hook `before`; akun pelaku, mekanisme penurunan limit, dan pemulihan tidak disebut TC, PRD, atau LLD (disediakan tim FE). Hook `after` memulihkan limit ke nilai awal dan menghapus Login User serta Non-Login User milik spec lewat API (tidak berasumsi seeding berhasil penuh). Suite berjalan serial.
- Data Dinamis milik spec, di-seed lewat API di hook `before` sebelum limit diatur (mekanisme disediakan tim FE/BE): Non-Login User `Batas Hapus {runId}-027` (First Name `Batas`, Last Name `Hapus {runId}-027`, Division `Logistics`, Represented By `Ahmad Fauzi`), Email `batashapus+{runId}-027@qwertysystem.net` (target Delete TC-GS-NLU-462; dibuat spec sendiri, bukan `Batas Hapus` Pre-setup).
- Data Dinamis dibuat UI: Non-Login User `Batas Satu {runId}-027` (Last Name `Satu {runId}-027`) Email `batas01+{runId}-027@qwertysystem.net` dan `Batas Dua {runId}-027` (Last Name `Dua {runId}-027`) Email `batas02+{runId}-027@qwertysystem.net` (First Name `Batas`, Division `Logistics`, Represented By `Ahmad Fauzi`); Login User milik spec dibuat lewat sesi API pada langkah 31 (Email `limitlogin+{runId}-027@qwertysystem.net`).
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` belum ada dan dibuat di tahap script.

## Test Steps

### TC-GS-NLU-100: Limit tercapai memblok pembukaan Popup Create

1. Klik `[+ Non-Login User]`
2. Verifikasi dialog tampil dengan Title `Limit Reached`, teks `You've reached the platform limit of 1000 users. Contact support if you need a higher limit.`, dan tombol `[OK]`
3. Klik area gelap di luar dialog
4. Verifikasi dialog tetap tampil (klik backdrop tidak menutup dialog)
5. Klik `[OK]`
6. Verifikasi dialog tertutup
7. Verifikasi Popup Create tidak terbuka

### TC-GS-NLU-462: Record soft-deleted tidak dihitung pada limit

8. Klik `[+ Non-Login User]`
9. Verifikasi dialog `Limit Reached` dengan teks `You've reached the platform limit of 1000 users. Contact support if you need a higher limit.`
10. Klik `[OK]`
11. Ketik Search `Batas Hapus {runId}-027`, tekan Enter
12. Klik `⋯` pada baris `Batas Hapus {runId}-027` > `Delete`
13. Klik `[Delete]` pada dialog
14. Klik `[+ Non-Login User]`
15. Verifikasi Popup Create terbuka (satu slot terbebas karena record soft-deleted tidak dihitung)

### TC-GS-NLU-101: Create ke-N berhasil dan ke-N+1 ditolak

16. Centang `Stay on this form after submitting`
17. Isi First Name `Batas`, Last Name `Satu {runId}-027`, dan Email `batas01+{runId}-027@qwertysystem.net`, lalu pilih Division `Logistics`
18. Klik `[+ Select User]`, klik baris `Ahmad Fauzi` pada popup Select User, klik `[Select]`
19. Klik `[Submit]`
20. Verifikasi toast sukses `Success, non-login user has been created.`
21. Isi ulang First Name `Batas`, Last Name `Dua {runId}-027`, dan Email `batas02+{runId}-027@qwertysystem.net`, pilih Division `Logistics`, lalu pilih Represented By `Ahmad Fauzi` lewat `[+ Select User]`, baris `Ahmad Fauzi`, `[Select]`
22. Klik `[Submit]`
23. Verifikasi dialog `Limit Reached` dengan teks `You've reached the platform limit of 1000 users. Contact support if you need a higher limit.` dan tombol `[OK]`
24. Klik `[OK]`
25. Klik `✕`
26. Verifikasi dialog `Unsaved Changes` tampil
27. Klik `[Leave]`
28. Ketik Search `Batas Dua {runId}-027`, tekan Enter
29. Verifikasi tabel menampilkan `No results found` (record `Batas Dua {runId}-027` tidak tersimpan)

### TC-GS-NLU-430: Create Login User menghabiskan kuota gabungan

30. Hapus `Batas Satu {runId}-027` lewat sesi API aktor hingga terhapus, sehingga sisa slot tepat 1
31. Buat satu Login User `limitlogin+{runId}-027@qwertysystem.net` lewat sesi API aktor hingga tersimpan
32. Klik `[+ Non-Login User]`
33. Verifikasi dialog `Limit Reached` dengan teks `You've reached the platform limit of 1000 users. Contact support if you need a higher limit.` (kuota gabungan Login + Non-Login) dan tombol `[OK]`
34. Klik `[OK]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan spec mengikuti state limit, bukan urutan nomor TC: TC-GS-NLU-100 (limit tercapai) lalu TC-GS-NLU-462 (menghapus satu record membebaskan satu slot) lalu TC-GS-NLU-101 (slot terakhir terpakai, slot berikutnya ditolak) lalu TC-GS-NLU-430 (slot dibebaskan lagi, Login User menghabiskannya). Tiap TC berikutnya mewarisi sisa slot dari TC sebelumnya, dengan pembebasan eksplisit di langkah 30 (S-09, S-10). Kelas state global; TC-GS-NLU-430 memicu state lewat Login User dan tetap objek uji Create Non-Login User.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 11 (Search untuk menemukan baris target; R-16), langkah 25 sampai 27 (menutup form dirty secara deterministik; S-08), langkah 28 (Search untuk memeriksa `Batas Dua {runId}-027` lewat Name bersuffix; kolom Email tidak termasuk kolom Search List), langkah 30 dan 31 (pelaku penyiapan state lewat sesi API aktor; bukan konteks kedua, sehingga `P-2` tidak dipakai).
- Langkah 29 memakai empty state `No results found` hasil Search sebagai anchor absence (8b.2).
- Temuan untuk QA:
  - TC-GS-NLU-100, 101, 430, dan 462 menulis teks dialog dengan angka `1000`; hitungan user Login + Non-Login tepat 1000 dan cara menurunkan limit ke 1000 tidak disebut TC (hanya "dapat diturunkan oleh penguji" di Pre-setup No. 17). Disediakan tim FE.
  - TC-GS-NLU-430 langkah 1 ("Buat satu Login User") tidak menyebut cara membuatnya (UI atau API); spec memakai sesi API aktor sebagai pemicu state.
  - TC-GS-NLU-462 menyebut baris `Batas Hapus` sebagai Non-Login User bantuan tanpa Email; spec men-seed record milik spec dengan Name dan Email unik agar Pre-setup tidak terhapus.
  - TC-GS-NLU-101 Expected b tidak menyebut apakah isian Batas Dua tetap ada sesudah dialog `[OK]`; spec mengasumsikan form masih dirty (langkah 25 sampai 27).
