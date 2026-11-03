---
id: TC-FA-FAAL-E2E-004-error-load-dan-download-gagal
title: "Kegagalan Server: Error Load Kedua Tab dan Download Gagal Tab Session"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAL-10
  - TC-FA-FAAL-11
  - TC-FA-FAAL-171
coverage:
  web: automated
---

# Kegagalan Server: Error Load Kedua Tab dan Download Gagal Tab Session

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Reports & Logs > Activity Log. Kegagalan dipicu intercept jaringan parsial di atas backend nyata (bagian 6 konvensi); data log tetap dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Data: Data Log Tab Session SS-01 sampai SS-11 (Pre-setup #11, 11 baris) dan Tab User Action UA-01 sampai UA-15 (Pre-setup #12, 15 baris), dipulihkan ke keadaan Pre-setup oleh fixture backend sebelum spec. Urutan default Date terbaru di atas: halaman 1 Tab Session SS-11 sampai SS-02 dan halaman 2 SS-01; halaman 1 Tab User Action UA-01 sampai UA-10 dan halaman 2 UA-11 sampai UA-15 (10 baris per halaman).
- Kemampuan teknis: intercept jaringan yang memaksa respons list Tab Session, respons list Tab User Action, dan respons Download gagal dengan status 500, lalu melepasnya; penangkap unduhan browser untuk mengamati bahwa tidak ada berkas terunduh. Setiap intercept dilepas segera setelah pemicu selesai (S-09).
- Flag Guided Tooltip: mengikuti butir "Flag Guided Tooltip" di `suite.md` (flag akun Total Control bernilai true lewat hook suite).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).

## Test Steps

### TC-FA-FAAL-10: Error load Tab Session menampilkan pesan dan tombol Try Again

1. Paksa respons list Tab Session gagal (500) lewat intercept jaringan
2. Muat ulang halaman
3. Verifikasi area tabel menampilkan `Unable to load this data.`
4. Verifikasi tombol `[Try Again]` tampil
5. Verifikasi empty state dengan Title `No activity yet` tidak tampil
6. Verifikasi tab Session tetap aktif setelah muat ulang
7. Lepas intercept respons list Tab Session
8. Klik `[Try Again]`
9. Verifikasi tabel tampil dengan baris SS-11 sampai SS-02 pada halaman 1
10. Klik `[Next →]`
11. Verifikasi tabel tampil dengan baris SS-01 pada halaman 2

### TC-FA-FAAL-11: Error load Tab User Action menampilkan pesan dan tombol Try Again

12. Klik tab User Action
13. Paksa respons list Tab User Action gagal (500) lewat intercept jaringan
14. Muat ulang halaman
15. Verifikasi area tabel menampilkan `Unable to load this data.`
16. Verifikasi tombol `[Try Again]` tampil
17. Verifikasi empty state dengan Title `No activity yet` tidak tampil
18. Verifikasi tab User Action tetap aktif setelah muat ulang
19. Lepas intercept respons list Tab User Action
20. Klik `[Try Again]`
21. Verifikasi tabel tampil dengan baris UA-01 sampai UA-10 pada halaman 1
22. Klik `[Next →]`
23. Verifikasi tabel tampil dengan baris UA-11 sampai UA-15 pada halaman 2

### TC-FA-FAAL-171: Download Tab Session gagal menampilkan toast error

24. Klik tab Session
25. Paksa respons Download gagal (500) lewat intercept jaringan
26. Klik icon Download
27. Klik `Download as CSV`
28. Verifikasi toast error tampil: "Error, failed to download Activity-Log-Session."
29. Verifikasi tidak ada berkas terunduh
30. Verifikasi toast tidak memiliki tombol aksi
31. Verifikasi toast tidak memiliki tombol tutup
32. Lepas intercept respons Download
33. Verifikasi toast error hilang dengan sendiri tanpa klik apa pun

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini kelas fault injection (bagian 3 prinsip 13b), satu spec untuk error load kedua tab dan download gagal Tab Session; download gagal Tab User Action (TC-FA-FAAL-172) ada di spec 078.
- Langkah penghubung (S-03): langkah 12 (membuka tab User Action sesuai precondition b TC-FA-FAAL-11), langkah 24 (pindah tab), langkah 32 (melepas intercept), langkah 33 (Verifikasi toast hilang dengan sendiri sesuai Expected c TC-FA-FAAL-171; sekaligus memastikan toast lama tidak terbaca asersi berikutnya, R-12; lama tunggu mengikuti auto-wait Spectra, PRD tidak memberi durasi). Tab aktif setelah muat ulang diasersi langsung (langkah 6 dan 18, Expected a TC-FA-FAAL-10 dan 11). Langkah 30 dan 31 memverifikasi Expected b dan c TC-FA-FAAL-171 (tanpa tombol aksi dan tanpa tombol tutup).
- Pembatasan halaman (S-14): TC-FA-FAAL-10 memuat langkah `Next →` dan Expected SS-11 sampai SS-02 di halaman 1 serta SS-01 di halaman 2 (langkah 9 sampai 11). TC-FA-FAAL-11 butir b masih menyebut "UA-01 sampai UA-15" tanpa halaman; dengan 10 baris per halaman, spec mengasersi halaman 1 lalu halaman 2 (langkah 21 sampai 23) supaya seluruh baris diamati.
- TC-FA-FAAL-172 ada di spec 078.
- Temuan untuk QA:
  - TC-FA-FAAL-11 butir b menyebut tabel tampil dengan baris UA-01 sampai UA-15 padahal tabel menampilkan 10 baris per halaman; spec mengasersi lewat dua halaman.
  - Perilaku toast T-01: hilang dengan sendiri tanpa tombol aksi atau tutup manual (Expected b dan c TC-FA-FAAL-171); durasi tidak ditentukan PRD sehingga spec tidak menulis angka.
