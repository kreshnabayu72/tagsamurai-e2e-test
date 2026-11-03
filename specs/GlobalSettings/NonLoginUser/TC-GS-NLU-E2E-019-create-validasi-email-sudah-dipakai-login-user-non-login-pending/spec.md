---
id: TC-GS-NLU-E2E-019-create-validasi-email-sudah-dipakai-login-user-non-login-pending
title: "Create: validasi Email sudah dipakai (Login User, Non-Login User, pending konfirmasi)"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-70
  - TC-GS-NLU-71
  - TC-GS-NLU-471
coverage:
  web: automated
---

# Create: validasi Email sudah dipakai (Login User, Non-Login User, pending konfirmasi)

## Prerequisites

- Mode: FE+BE (backend nyata; duplikasi Email divalidasi server).
- Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password lewat `Spectra.env.GS_TC_PASSWORD`.
- Env var: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk akun aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9 sampai 13, hanya dibaca), dipakai sebagai Email yang sudah terpakai dan tidak diubah:
  - Login User `Ahmad Fauzi` (`ahmadfauzi@qwertysystem.net`, No. 10) sebagai Represented By dan sebagai Email milik Login User (TC-GS-NLU-70).
  - Non-Login User `Budi Kurniawan` (`budi.kurniawan@qwertysystem.net`, No. 11) untuk TC-GS-NLU-71.
  - Login User `Rina Putri` (Activated, email pending `rinaputri.baru@qwertysystem.net`, badge `Pending Email Confirmation`, No. 10) untuk TC-GS-NLU-471.
  - Division `Operations`.
- Nilai input uji milik spec: First Name `Email`, Last Name `Duplikat` (TC-GS-NLU-70 dan 71) atau `Pending` (TC-GS-NLU-471). Email yang diketik adalah Email Pre-setup di atas dan sengaja tanpa suffix `{runId}` karena justru duplikasi dengan Pre-setup yang diuji; tidak ada record tersimpan sehingga tidak ada cleanup.
- Kemampuan teknis: menunggu sekitar 500 ms sesudah mengetik Email (jeda pendek yang disebut TC).
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` belum ada dan dibuat di tahap script.
- State global yang diubah: tidak ada. Suite berjalan serial.

## Test Steps

### TC-GS-NLU-70: Email sudah dipakai Login User

1. Klik `[+ Non-Login User]`
2. Isi First Name `Email` dan Last Name `Duplikat`
3. Pilih Division `Operations`
4. Klik `[+ Select User]`, klik baris `Ahmad Fauzi` pada popup Select User, klik `[Select]`
5. Ketik Email `ahmadfauzi@qwertysystem.net`, lalu tunggu sekitar 500 ms tanpa berpindah field
6. Verifikasi pesan inline `Email already exists` muncul tanpa menunggu kursor keluar field
7. Klik `[Submit]`
8. Verifikasi Popup Create tetap terbuka
9. Verifikasi tidak ada toast sukses
10. Klik `[Clear Field]`

### TC-GS-NLU-71: Email sudah dipakai Non-Login User lain

11. Isi First Name `Email` dan Last Name `Duplikat`
12. Pilih Division `Operations`
13. Klik `[+ Select User]`, klik baris `Ahmad Fauzi` pada popup Select User, klik `[Select]`
14. Ketik Email `budi.kurniawan@qwertysystem.net`, lalu tunggu sekitar 500 ms tanpa berpindah field
15. Verifikasi pesan inline `Email already exists` muncul tanpa menunggu kursor keluar field
16. Klik `[Submit]`
17. Verifikasi Popup Create tetap terbuka
18. Verifikasi tidak ada toast sukses
19. Klik `[Clear Field]`

### TC-GS-NLU-471: Email yang sedang pending konfirmasi di Login User

20. Isi First Name `Email` dan Last Name `Pending`
21. Pilih Division `Operations`
22. Klik `[+ Select User]`, klik baris `Ahmad Fauzi` pada popup Select User, klik `[Select]`
23. Ketik Email `rinaputri.baru@qwertysystem.net`, lalu tunggu sekitar 500 ms tanpa berpindah field
24. Verifikasi pesan inline `Email already exists` muncul tanpa menunggu kursor keluar field
25. Klik `[Submit]`
26. Verifikasi Popup Create tetap terbuka
27. Verifikasi tidak ada toast sukses

### Penutup dan asersi record tidak tersimpan

28. Klik `✕`
29. Verifikasi dialog `Unsaved Changes` tampil
30. Klik `[Leave]`
31. Ketik Search `Email Duplikat`, tekan Enter
32. Verifikasi tabel menampilkan empty state `No results found`
33. Ganti isi kotak search dengan `Email Pending`, tekan Enter
34. Verifikasi tabel menampilkan empty state `No results found`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan mengikuti nomor TC dengan TC-GS-NLU-471 (varian Login User pending) terakhir.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 10 dan 19 (`[Clear Field]` karena dua TC berurutan memakai form yang sama dengan pesan inline identik; R-12), langkah 28 sampai 30 (menutup form dirty secara deterministik; S-08), langkah 31 dan 33 (Search untuk menemukan baris target; R-16).
- Klausa "tidak ada record `Email Duplikat`" (TC-GS-NLU-70 dan TC-GS-NLU-71 Expected b) diasersi di langkah 32 dan klausa "tidak ada record `Email Pending`" (TC-GS-NLU-471 Expected b) di langkah 34, setelah Popup ditutup, karena tabel tidak dapat dicari selama Popup terbuka. Empty state `No results found` hasil Search menjadi anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - Ketiga TC mengetik Email setelah First Name dan Last Name; TC tidak menyatakan kolom yang divalidasi server saat blur, sehingga spec hanya mengasersi pesan inline muncul tanpa berpindah field (Expected a).
  - Email Pre-setup `ahmadfauzi@qwertysystem.net`, `budi.kurniawan@qwertysystem.net`, dan `rinaputri.baru@qwertysystem.net` dipakai tanpa suffix karena duplikasi dengan data Pre-setup adalah objek uji.
