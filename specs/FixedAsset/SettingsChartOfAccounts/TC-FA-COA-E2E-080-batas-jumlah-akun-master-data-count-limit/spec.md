---
id: TC-FA-COA-E2E-080-batas-jumlah-akun-master-data-count-limit
title: "Batas Jumlah Akun: Master Data Count Limit Memblokir Penambahan Akun"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-COA-31
  - TC-FA-COA-159
  - TC-FA-COA-282
coverage:
  web: automated
---

# Batas Jumlah Akun: Master Data Count Limit Memblokir Penambahan Akun

## Prerequisites

- Mode: FE+BE.
- Kelas harness e (volume data: batas Master Data Count Limit 1000 akun). Suite berjalan serial (`parallel: false`).
- Akun login hook `before` spec ini: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada client uji batas akun plan Growth (Pre-setup P23), password dari `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite. Dua ganti akun eksplisit: langkah 6 ke Total Control client plan Enterprise (P24) dan langkah 16 ke Total Control client Create berulang (P89). Hook `after` mengembalikan sesi ke akun default suite. Kecocokan akun Total Control pada ketiga client perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` sudah terdaftar.
- Data client Pre-setup (disediakan tim FE, seed atau API; kunci fixture ditetapkan tim FE):

  | Client | Pre-setup | Isi | Dipakai di |
  |---|---|---|---|
  | Plan Growth | P23 | Master Data Count Limit 1000 (nilai minimum, Lifecycle Settings > System Limits), 1000 akun (600 Active, 400 Inactive) | TC-FA-COA-31 |
  | Plan Enterprise | P24 | Master Data Count Limit 1000, 1000 akun (600 Active, 400 Inactive) | TC-FA-COA-159 |
  | Plan Growth, Create berulang | P89 | Master Data Count Limit 1000, 999 akun | TC-FA-COA-282 |

- Data Dinamis pada client P89: Code `CAP-8500` (dibuat) dan `CAP-8501` (ditolak), Account Name `Batas Stay {runId}-080` dan `Batas Stay B {runId}-080`, Account Function Capitalization Offset. Account Code `CAP-8500` dan `CAP-8501` literal (maksimal 15 karakter, tidak diberi suffix `{runId}`); hook `before` dan `after` menghapus akun dengan Code tersebut bila ada, sehingga client P89 kembali berjumlah 999 akun (fixture sekali pakai).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): seed ketiga client; kemampuan membaca dari server jumlah akun dan daftar Code per client; penghapusan akun milik spec untuk pemulihan.
- Seed dan pemulihan client mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.

## Test Steps

### TC-FA-COA-31: Plan Growth, jumlah akun sama dengan batas

1. Klik `+ Account`
2. Verifikasi dialog "Cannot Add Account" dengan body "You've reached the platform limit of 1000 records. Contact support if you need a higher limit."
3. Verifikasi tombol `[OK]` tampil pada dialog
4. Verifikasi Modal Add Account tidak terbuka
5. Klik `[OK]`

### TC-FA-COA-159: Plan Enterprise, Active kurang dari batas tetapi total sama dengan batas

6. Ganti akun: logout, lalu login sebagai Total Control pada client plan Enterprise (P24) dengan `Spectra.env.FA_TC_PASSWORD`
7. Buka Fixed Asset > Settings > Accounting, tab `Chart of Accounts`
8. Catat jumlah akun client P24 dari server (baseline, 1000: Active 600, Inactive 400)
9. Klik `+ Account`
10. Verifikasi dialog "Cannot Add Account" dengan body "You've reached the platform limit of 1000 records. Contact support if you need a higher limit." walau jumlah akun Active hanya 600
11. Verifikasi tombol `[OK]` tampil pada dialog
12. Verifikasi Modal Add Account tidak terbuka
13. Klik `[OK]`
14. Verifikasi dialog "Cannot Add Account" tertutup
15. Verifikasi tidak ada akun dibuat: jumlah akun client P24 dari server sama dengan langkah 8

### TC-FA-COA-282: Create berulang dengan Stay hingga batas

16. Ganti akun: logout, lalu login sebagai Total Control pada client Create berulang (P89) dengan `Spectra.env.FA_TC_PASSWORD`
17. Buka Fixed Asset > Settings > Accounting, tab `Chart of Accounts`
18. Klik `+ Account` lalu centang "Stay on this form after submitting"
19. Isi Account Code `CAP-8500`, Account Name `Batas Stay {runId}-080`, Account Function Capitalization Offset, lalu klik `[Submit]`
20. Verifikasi Toast "Success, account has been created."
21. Verifikasi Modal Add Account tetap terbuka
22. Isi Account Code `CAP-8501`, Account Name `Batas Stay B {runId}-080`, Account Function Capitalization Offset, lalu klik `[Submit]`
23. Verifikasi dialog "Cannot Add Account" dengan body "You've reached the platform limit of 1000 records. Contact support if you need a higher limit."
24. Verifikasi akun `CAP-8501` tidak dibuat: daftar akun client P89 dari server tidak memuat Code `CAP-8501`
25. Klik `[OK]`
26. Klik `✕` pada Modal Add Account
27. Verifikasi dialog `Unsaved Changes` tampil
28. Klik `[Leave]`

## Notes

- Alasan 28 langkah: tidak ada; di bawah ambang sekitar 35 langkah.
- Langkah penghubung (S-03): langkah 5 dan 13 menutup dialog (langkah 13 juga Klik `[OK]` pada TC-FA-COA-159 langkah 2), langkah 6 dan 16 ganti akun, langkah 7 dan 17 membuka tab setelah ganti akun, langkah 8 mencatat baseline, langkah 25 sampai 28 menutup form dirty (S-08, S-09; pemulihan akun `CAP-8500` oleh hook `after`).
- Langkah 24 memakai dialog pada langkah 23 sebagai anchor positif (respons server sudah diproses) sebelum asersi `CAP-8501` tidak ada (bagian 8b butir 2); pembacaan dari server oleh kemampuan baca yang disediakan tim FE/BE.
- Ganti client memakai ganti akun eksplisit (Pre-setup P23, P24, P89 berbeda client).
- Temuan untuk QA:
  - TC-FA-COA-159 Post Condition ("tidak ada log") dan TC-FA-COA-282 Post Condition ("Jumlah akun client 1000") tanpa langkah observasi; tidak diasersi, kecuali langkah 15 yang membandingkan jumlah akun sebagai padanan Expected d. Asersi "tidak ada log" bukan milik spec ini (spec absence 083 tidak memuat TC ini).
  - TC-FA-COA-282 tidak menyebut Account Name dan Account Function; spec memilih nilai valid. Account Code `CAP-8500` dan `CAP-8501` literal karena batas 15 karakter.
  - Teks dialog blok memakai [Limit] = 1000 sesuai TC; urutan penulisan "Stay" tidak menyebut isi kolom setelah submit pertama (diasumsikan form kosong kembali sehingga langkah 22 mengisi ulang).
  - Kolom ACC TC-FA-COA-31/159/282 mengacu P23, P24, P89 tanpa kunci fixture atau email akun per client; disediakan tim FE.
