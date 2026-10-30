---
id: TC-GS-USER-E2E-023-create-validasi-duplikat-email-dan-employee-id
title: "Create User: Validasi Duplikat Email Lintas Client dan Employee ID Real-Time, Termasuk Trim Spasi dan Sensitivitas Huruf"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-112
  - TC-GS-USER-114
  - TC-GS-USER-1031
  - TC-GS-USER-1032
  - TC-GS-USER-1033
coverage:
  web: automated
---

# Create User: Validasi Duplikat Email Lintas Client dan Employee ID Real-Time, Termasuk Trim Spasi dan Sensitivitas Huruf

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Akun seeding (hook `before`, hanya lewat API, tidak dipakai di UI): admin Client B (Client PT Sinar Abadi, Tabel Pre-setup No. 26), disediakan tim FE, kredensial `Spectra.env.GS_CLIENTB_TC_PASSWORD`.
- Env var: `GS_TC_PASSWORD`, `GS_CLIENTB_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup, hanya dibaca; spec tidak mengubah atau menghapus data):
  - John Doe (No. 18), Employee ID `EMP-0001`, di Client aktor; dipakai sebagai Employee ID duplikat. Spec hanya mengetik nilainya di form Create dan tidak menyimpan.
  - Master Data Division `Finance` (No. 23).
  - Custom Field aktif `Emergency Phone` (Phone, Required) (No. 24).
  - Hendra Gunawan (Default User, No. 1), email `defaultUserGlobalSettings_automated_{namaCompany}@qwertysystem.net`; pembanding pembacaan user lewat backend.
- Data Dinamis (di-seed lewat API di hook `before`, kemampuan seeding user lintas client disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD):
  - U-1: user di Client B (PT Sinar Abadi) dengan Email `teguhsantoso+{runId}-023@qwertysystem.net` (huruf kecil). Dipakai TC-GS-USER-112 dan TC-GS-USER-1031 (email dipakai user di client lain). Cleanup di hook `after`: hapus U-1 lewat API.
  - Email uji untuk Submit TC-GS-USER-1032: `budisantoso+{runId}-023@qwertysystem.net` (tidak ada di backend). Cleanup di hook `after`: hapus user ber-Email ini bila ada (cadangan bila validasi gagal dan user tercipta), tanpa mengandalkan hook `before` berhasil penuh.
- State global yang diubah: tidak ada. Suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE bila belum ada): membaca user menurut Email dari backend pada Client aktor (dipakai Verifikasi "user tidak dibuat"; endpoint tidak disebut di TC dan PRD); menunggu ±500 ms nyata untuk debounce validasi real-time (jeda pendek yang disebut TC).

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Verifikasi pembacaan user lewat backend berfungsi: user Hendra Gunawan (Default User) ditemukan menurut Email
3. Klik `[+ User]` di Table Tools

### TC-GS-USER-112: Email yang dipakai user di client lain ditolak real-time via debounce

4. Ketik Email `teguhsantoso+{runId}-023@qwertysystem.net`
5. Tunggu ±500 ms tanpa memindahkan kursor
6. Verifikasi inline error `Email already exists` muncul di Email tanpa blur dan tanpa `[Submit]`
7. Isi First Name `Teguh`, Last Name `Santoso`, Division `Finance`, centang Access `Fixed Asset`, Emergency Phone `081234567890`
8. Klik `[Submit]`
9. Verifikasi user tidak dibuat: tidak ada user ber-Email `teguhsantoso+{runId}-023@qwertysystem.net` pada Client aktor di backend

### TC-GS-USER-1031: Email dengan huruf besar/kecil berbeda dan spasi tepi dianggap duplikat

10. Klik `[Clear Field]`
11. Ketik Email ` TeguhSantoso+{runId}-023@qwertysystem.net ` (huruf besar `S`, spasi di awal dan akhir)
12. Tunggu ±500 ms tanpa memindahkan kursor
13. Verifikasi inline error `Email already exists` muncul di Email tanpa blur dan tanpa `[Submit]`
14. Isi First Name `Teguh`, Last Name `Santoso`, Division `Finance`, centang Access `Fixed Asset`, Emergency Phone `081234567890`
15. Klik `[Submit]`
16. Verifikasi user tidak dibuat: tidak ada user ber-Email `teguhsantoso+{runId}-023@qwertysystem.net` pada Client aktor di backend

### TC-GS-USER-114: Employee ID duplikat di entitas yang sama ditolak real-time

17. Klik `[Clear Field]`
18. Ketik Employee ID `EMP-0001`
19. Tunggu ±500 ms
20. Verifikasi inline error `Employee ID already exists` muncul di Employee ID tanpa blur dan tanpa `[Submit]`

### TC-GS-USER-1032: Employee ID dengan spasi tepi dianggap duplikat

21. Klik `[Clear Field]`
22. Ketik Employee ID ` EMP-0001 ` (spasi di awal dan akhir)
23. Tunggu ±500 ms tanpa memindahkan kursor
24. Verifikasi inline error `Employee ID already exists` muncul di Employee ID tanpa blur dan tanpa `[Submit]`
25. Isi First Name `Budi`, Last Name `Santoso`, Division `Finance`, Email `budisantoso+{runId}-023@qwertysystem.net`, centang Access `Fixed Asset`, Emergency Phone `081234567890`
26. Klik `[Submit]`
27. Verifikasi user tidak dibuat: tidak ada user ber-Email `budisantoso+{runId}-023@qwertysystem.net` di backend

### TC-GS-USER-1033: Employee ID dengan huruf besar/kecil berbeda tidak dianggap duplikat

28. Ganti isi Employee ID dengan `emp-0001`
29. Tunggu ±500 ms tanpa memindahkan kursor
30. Verifikasi tidak ada error `Employee ID already exists` pada field Employee ID

### Penutup

31. Klik `✕` di header Popup
32. Verifikasi dialog `Unsaved Changes` tampil
33. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan (112, 1031, 114, 1032, 1033). TC-GS-USER-1033 berada sesudah TC-GS-USER-1032 pada field Employee ID yang sama, sehingga Verifikasi "tidak ada error" didahului Verifikasi bahwa error `Employee ID already exists` untuk ` EMP-0001 ` tampil di field yang sama (8b butir 2).
- Spec memakai satu pembukaan Popup dengan `[Clear Field]` di antara kasus, sehingga error dari kasus sebelumnya tidak tersisa saat kasus berikutnya diamati (S-09).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): `[Clear Field]` di awal blok; pengisian field wajib lain dan `Emergency Phone` `081234567890` serta `[Submit]` pada TC-GS-USER-112, 1031, dan 1032 untuk mengamati Expected "Submit tidak membuat user".
- Verifikasi pembacaan user Hendra Gunawan lewat backend di bagian Pembukaan layar adalah anchor positif untuk Verifikasi "user tidak dibuat" (8b butir 2); asersi tambahan ini tidak ada di TC dan dicatat sebagai pengecualian S-03.
- Penutup Popup memakai alur form dirty deterministik (`✕`, dialog `Unsaved Changes`, `[Leave]`) sesuai S-08; Verifikasi dialog di langkah penutup adalah prosedur penutupan, bukan Expected TC.
- Email U-1 memakai suffix `{runId}-023` pada bagian lokal (`teguhsantoso+{runId}-023`) sehingga unik per run; nilai TC `teguhsantoso@qwertysystem.net` tidak diketik apa adanya.
- Employee ID `EMP-0001` dan `emp-0001` memakai nilai literal Tabel Pre-setup (John Doe, No. 18) karena objek uji adalah duplikat terhadap data Pre-setup; spec tidak menyimpan Employee ID itu.
- Temuan untuk QA:
  - TC-GS-USER-112 dan 1031 mensyaratkan Email dipakai user di client lain tanpa menyebut user atau client; Tabel Pre-setup tidak memuatnya. Spec men-seed U-1 di Client PT Sinar Abadi (No. 26) dengan sesi admin Client B yang disediakan tim FE.
  - TC-GS-USER-112, 1031, dan 1032 menyebut "Submit tidak membuat user" tanpa langkah Submit dan tanpa Data Uji field wajib lain; spec menambah pengisian field wajib lain dan `[Submit]` supaya Expected dapat diasersi, dan membaca backend menurut Email (kemampuan disediakan tim FE/BE).
  - TC-GS-USER-1031 menyebut Email ` TeguhSantoso@qwertysystem.net ` dengan huruf besar `S`; pembanding tidak case-sensitive. Spec mengikuti suffix `{runId}-023` pada bagian lokal, huruf besar `S` dipertahankan.
  - Tabel Pre-setup No. 24 mendefinisikan `Emergency Phone` Required, tetapi TC tidak mengisi Custom Field; spec mengisinya pada blok yang menekan `[Submit]` supaya penyebab penolakan adalah duplikat.
  - TC-GS-USER-114 menyebut "John Doe Employee ID `EMP-0001`" sebagai precondition, sedangkan TC-GS-USER-1032 dan 1033 merujuk Tabel Pre-setup No. 10 sampai 22; spec memakai John Doe (No. 18) untuk ketiganya.
