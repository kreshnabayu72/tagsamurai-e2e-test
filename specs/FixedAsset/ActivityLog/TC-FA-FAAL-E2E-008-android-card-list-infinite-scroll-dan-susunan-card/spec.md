---
id: TC-FA-FAAL-E2E-008-android-card-list-infinite-scroll-dan-susunan-card
title: "Android: Card List, Infinite Scroll, dan Susunan Card Tab Session dan User Action"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-30
  - TC-FA-FAAL-31
  - TC-FA-FAAL-32
  - TC-FA-FAAL-33
  - TC-FA-FAAL-34
coverage:
  mobile: automated
---

# Android: Card List, Infinite Scroll, dan Susunan Card Tab Session dan User Action

## Prerequisites

- Mode: FE+BE. Platform: aplikasi native Android Fixed Asset > Reports & Logs > Activity Log.
- Perangkat atau emulator Android dengan aplikasi Fixed Asset TAG Samurai terpasang dan driver perangkat yang mampu mengetuk, menggulir, dan membaca elemen UI; disediakan tim FE. Perangkat dipakai bersama sehingga suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di aplikasi Android di hook `before` spec ini; spec ini membuka halaman Activity Log sendiri di aplikasi karena hook `beforeEach` suite membuka halaman web. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Data: Data Log Tab Session SS-01 sampai SS-11 (Pre-setup #11, 11 card) dan Tab User Action UA-01 sampai UA-15 (Pre-setup #12, 15 card), dipulihkan ke keadaan Pre-setup oleh fixture backend sebelum spec. Urutan card Date terbaru di atas; batch awal 10 card dan batch berikutnya dimuat saat menggulir. Card yang diasersi: SS-01 (John Doe, Session started, EMP001, Staff, Marketing, 192.168.1.10, Chrome on Windows), SS-03 (Siti Nurbaya, Concurrent limit reached), SS-11 (card pertama Tab Session), UA-01 (card pertama Tab User Action), UA-02 (Edit, Groups, Gedung A > Lantai 3 - Renovasi, Group Name, Lantai 3, Lantai 3 - Renovasi, Modified By Admin Alpha).
- Setup Column: spec ini menyembunyikan kolom Note Tab Session (langkah 27); konfigurasi kolom dipulihkan di hook `after` dengan menghapus preferensi kolom (butir "Pemulihan Setup Column" di `suite.md`); kemampuan disediakan tim FE.
- Flag Guided Tooltip: mengikuti butir "Flag Guided Tooltip" di `suite.md` (flag akun Total Control bernilai true lewat hook suite).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).

## Test Steps

### TC-FA-FAAL-30: Android: Card List dimuat infinite scroll per batch 10 tanpa pagination

1. Ketuk tab Session
2. Verifikasi Tab Session menampilkan 10 card awal
3. Gulir ke bawah hingga akhir daftar
4. Verifikasi Tab Session menampilkan 11 card setelah batch berikutnya dimuat otomatis
5. Verifikasi Tab Session tidak memiliki pagination bernomor, teks `Showing X–Y of Z entries`, maupun Rows per page
6. Ketuk tab User Action
7. Verifikasi Tab User Action menampilkan 10 card awal
8. Gulir ke bawah hingga akhir daftar
9. Verifikasi Tab User Action menampilkan 15 card setelah batch berikutnya dimuat otomatis
10. Verifikasi Tab User Action tidak memiliki pagination bernomor, teks `Showing X–Y of Z entries`, maupun Rows per page

### TC-FA-FAAL-31: Android: urutan card Date terbaru di atas tanpa kontrol sort

11. Ketuk tab Session
12. Gulir ke card paling atas
13. Verifikasi card pertama Tab Session adalah SS-11
14. Ketuk tab User Action
15. Gulir ke card paling atas
16. Verifikasi card pertama Tab User Action adalah UA-01
17. Verifikasi tidak ada kontrol sort pada card dan toolbar

### TC-FA-FAAL-32: Android: susunan card Tab User Action

18. Verifikasi susunan card UA-02: Date (muted), Action + Object (bold), Name + Field, Old Value + New Value, lalu Modified By
19. Verifikasi card UA-02 menampilkan delapan kolom: `Edit`, `Groups`, `Gedung A > Lantai 3 - Renovasi`, `Group Name`, `Lantai 3`, `Lantai 3 - Renovasi`, `Admin A`

### TC-FA-FAAL-33: Android: susunan card Tab Session tanpa Activity dan Status

20. Ketuk tab Session
21. Gulir ke bawah hingga card SS-01 tampil
22. Verifikasi susunan card SS-01: Date (muted), User (bold) + Note, Employee ID + Position + Division, lalu IP Address + Device/Browser
23. Verifikasi card SS-01 menampilkan `John D`, `Session started`, `EMP001`, `Staff`, `Marketing`, `192.168.1.10`, `Chrome on Windows`
24. Verifikasi Activity `Session` dan Status `—` tidak tampil di card SS-01

### TC-FA-FAAL-34: Android: kolom yang disembunyikan hilang dari card

25. Ketuk `[⋯]` pada toolbar
26. Pilih Column Visibility
27. Sembunyikan kolom Note
28. Gulir ke card SS-03
29. Verifikasi card SS-03 tidak lagi menampilkan Note (`Concurrent limit reached` tidak tampil)
30. Verifikasi kolom lain pada card SS-03 tetap tampil

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec berjalan di aplikasi Android; `coverage.mobile: automated`. Kemampuan driver Android belum dipastikan tim FE; `coverage` dapat berubah menjadi `unsupported` bila tidak tersedia.
- Langkah penghubung (S-03): langkah 12, 15, 21, dan 28 (menggulir ke posisi card yang diasersi), langkah 11, 14, dan 20 (pindah tab di luar langkah TC).
- Asersi absence pada langkah 29 berjangkar pada card SS-03 yang tampil (langkah 28) dan kolom lain yang tetap tampil (langkah 30).
- TC-FA-FAAL-35 (card tidak dapat diketuk) ada di spec 079.
- TC-FA-FAAL-36 (toolbar dan Guided Tooltip Android dengan akun Pre-setup #4) ada di spec 064.
- Temuan untuk QA:
  - TC-FA-FAAL-30 sampai 34 memuat angka absolut jumlah card (10, 11, 15); audit trail tumbuh, sehingga angka hanya terjamin bila log dipulihkan ke Pre-setup (Catatan TC: fixture dipulihkan sebelum tiap TC); pemulihan itu kemampuan tim FE/BE (S-12, S-14).
  - TC-FA-FAAL-31 tidak menyebut posisi gulir setelah pindah tab; spec menggulir ke card paling atas.
  - TC-FA-FAAL-34 tidak menyebut apakah perubahan Column Visibility perlu disimpan dengan tombol; spec tidak menulis tombol simpan.
  - TC-FA-FAAL-33 mengambil card SS-01 yang berada di batch kedua (card ke-11); TC tidak menyebut gulir untuk memuatnya.
