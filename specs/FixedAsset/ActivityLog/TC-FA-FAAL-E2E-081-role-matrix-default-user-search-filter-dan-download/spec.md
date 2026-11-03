---
id: TC-FA-FAAL-E2E-081-role-matrix-default-user-search-filter-dan-download
title: "Role Matrix: Default User Melihat Seluruh Baris Kedua Tab dan Menjalankan Search, Filter, dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-277
coverage:
  web: automated
---

# Role Matrix: Default User Melihat Seluruh Baris Kedua Tab dan Menjalankan Search, Filter, dan Download

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

  | TC | Role | Pre-setup | Email | Env var password |
  |---|---|---|---|---|
  | TC-FA-FAAL-277 | Default User | #3 | `defaultUserFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DU_PASSWORD` |
- Login akun aktor (Default User, Pre-setup #3) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Env var `FA_DU_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (R-07). Password tidak ditulis di spec atau fixture.
- Data: Tab Session SS-01 sampai SS-11 (Pre-setup #11, total 11 baris) dan Tab User Action UA-01 sampai UA-15 (Pre-setup #12, total 15 baris), dipulihkan ke keadaan Pre-setup sebelum spec (disediakan tim FE/BE). Total absolut 11 dan 15 diasersi dalam Filter Date Jendela Seed. Baris Tab Session berasal dari user pada group berbeda (Gedung A, Gedung B, tanpa group) dan baris Tab User Action dari aksi pada group berbeda. Urutan default Date terbaru di atas dengan 10 baris per halaman.
- Kemampuan teknis disediakan tim FE: penangkap unduhan browser dan parser CSV (butir "Kemampuan teknis tambahan" di `suite.md`).
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nilai data ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-277: Default User melihat seluruh baris kedua tab dan menjalankan Search, Filter, dan Download

1. Klik tab Session
2. Klik icon Filter
3. Pilih tanggal mulai `14/07/26` dan tanggal akhir `16/07/26` pada field Date
4. Klik `[Apply]`
5. Verifikasi Default User: tab Session menampilkan `Showing 1–10 of 11 entries`
6. Ketik Search `Budi`, tekan Enter
7. Verifikasi Default User: setelah Search hanya baris SS-06 tampil
8. Klik `(←)` pada kotak Search
9. Klik tab User Action
10. Klik icon Filter
11. Pilih tanggal mulai `18/06/26` dan tanggal akhir `18/06/26` pada field Date
12. Klik `[Apply]`
13. Verifikasi Default User: tab User Action menampilkan `Showing 1–10 of 15 entries`
14. Klik icon Filter
15. Pilih `Delete` pada field Action
16. Klik `[Apply]`
17. Verifikasi Default User: setelah Apply hanya baris UA-03 tampil
18. Verifikasi Default User: icon Filter menampilkan badge titik
19. Klik icon Download
20. Pilih `Download as CSV`
21. Verifikasi Default User: tidak ada toast
22. Verifikasi Default User: berkas `Activity-Log-User-Action.csv` terunduh dan memuat header dan satu baris data (UA-03)

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec Role Matrix (bagian 3a): data yang terlihat untuk Default User. Akun aktor login di hook `before` (S-07).
- Langkah penghubung (S-03): langkah 1 dan 9 (klik tab untuk membuka tab yang diamati TC), langkah 2 sampai 4 dan 10 sampai 12 (menerapkan Filter Date Jendela Seed pada tiap tab sesuai precondition e TC-FA-FAAL-277), langkah 8 (mengosongkan Search sebelum pindah tab).
- Pembanding asersi universal (bagian 8b butir 2): teks pagination `Showing 1–10 of 11 entries` (langkah 5) dan `Showing 1–10 of 15 entries` (langkah 13) membuktikan baris ada di tabel sebelum asersi "hanya baris SS-06" dan "hanya baris UA-03".
- Langkah 21 (absence toast) diletakkan segera setelah pemicu `Download as CSV` dan sebelum asersi berkas (bagian 8b butir 11); langkah 20 menjadi anchor positif yang buktinya langkah 22.
- Langkah 5 dan 13 memakai total absolut dalam Filter Date Jendela Seed (Tab Session 14/07/26 sampai 16/07/26; Tab User Action 18/06/26 sampai 18/06/26) seperti Expected TC-FA-FAAL-277.
- Search, Filter, dan Download untuk Default User berada dalam satu Role Matrix karena TC-FA-FAAL-277 satu TC dengan satu daftar Expected (bagian 3a).
- Temuan untuk QA:
  - TC-FA-FAAL-277 tidak menyebut env var password; nama env var diusulkan dari butir "Env var" di `suite.md`.
  - TC-FA-FAAL-277 Expected butir a tidak menyebut jumlah baris setelah Search selain "hanya SS-06"; spec tidak menambah asersi jumlah.
  - TC-FA-FAAL-277 tidak menyebut apakah Filter Panel tetap terbuka setelah `[Apply]`; spec menulis "Klik icon Filter" sebelum tiap pembukaan panel mengikuti langkah TC.
