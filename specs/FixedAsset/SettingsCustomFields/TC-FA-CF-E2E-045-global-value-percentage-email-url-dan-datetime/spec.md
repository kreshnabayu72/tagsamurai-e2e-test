---
id: TC-FA-CF-E2E-045-global-value-percentage-email-url-dan-datetime
title: "Global Value Percentage, Email, URL, dan DateTime: Nilai Tidak Valid Ditolak"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-136
  - TC-FA-CF-137
  - TC-FA-CF-138
  - TC-FA-CF-139
coverage:
  web: automated
---

# Global Value Percentage, Email, URL, dan DateTime: Nilai Tidak Valid Ditolak

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Alpha. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Company Alpha baseline (Pre-setup #11 dan #12) dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE).
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-045`): `Global Percentage {runId}-045` (Percentage, nilai akhir `100`, tersimpan), `Global Email {runId}-045` (Email, nilai `bukan-email`, tidak tersimpan), `Global URL {runId}-045` (URL, nilai `bukan url`, tidak tersimpan), `Global DateTime {runId}-045` (DateTime, nilai `31/02/26 25:61`, tidak tersimpan). Nilai Percentage yang diketik: `101`, `-1`, `100`.
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-045`.
- Kemampuan teknis: pengetikan nilai tanggal dan jam mentah ke input DateTime.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik [+ Custom Field]

### TC-FA-CF-136: Global Value Percentage 100 diterima dan di atas 100 atau negatif ditolak

2. Isi Field Name `Global Percentage {runId}-045`, pilih Data Type `Percentage`, Scope `General`, Value Type `Global`
3. Isi Value `101`
4. Klik [Submit]
5. Verifikasi nilai `101` ditolak dengan pesan inline pada input Value (teks pesan tidak diassert)
6. Ganti Value menjadi `-1`
7. Klik [Submit]
8. Verifikasi nilai `-1` ditolak dengan pesan inline pada input Value (teks pesan tidak diassert)
9. Ganti Value menjadi `100`
10. Klik [Submit]
11. Verifikasi nilai `100` diterima: toast "Success, custom field has been created." tampil

### TC-FA-CF-137: Global Value Email berformat tidak valid ditolak

12. Klik [+ Custom Field]
13. Isi Field Name `Global Email {runId}-045`, pilih Data Type `Email`, Scope `General`, Value Type `Global`
14. Isi Value `bukan-email`
15. Klik [Submit]
16. Verifikasi input ditolak dengan pesan inline pada input Value (teks pesan tidak diassert)
17. Verifikasi Submit tidak menyimpan field: modal tetap terbuka
18. Klik [Clear Field]

### TC-FA-CF-138: Global Value URL berformat tidak valid ditolak

19. Isi Field Name `Global URL {runId}-045`, pilih Data Type `URL`, Scope `General`, Value Type `Global`
20. Isi Value `bukan url`
21. Klik [Submit]
22. Verifikasi input ditolak dengan pesan inline pada input Value (teks pesan tidak diassert)
23. Verifikasi Submit tidak menyimpan field: modal tetap terbuka
24. Klik [Clear Field]

### TC-FA-CF-139: Global Value DateTime berformat tidak valid ditolak

25. Isi Field Name `Global DateTime {runId}-045`, pilih Data Type `DateTime`, Scope `General`, Value Type `Global`
26. Ketik tanggal dan jam tidak valid `31/02/26 25:61` pada input Value
27. Klik [Submit]
28. Verifikasi input ditolak dengan pesan inline pada input Value (teks pesan tidak diassert)
29. Verifikasi Submit tidak menyimpan field: modal tetap terbuka
30. Klik `[✕]`
31. Verifikasi dialog `Unsaved Changes` dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]` tampil
32. Klik `[Leave]`

### Penutup: field yang ditolak tidak tersimpan

33. Ketik Search `{runId}-045`, tekan Enter
34. Verifikasi tabel menampilkan tepat 1 baris `Global Percentage {runId}-045` (field Email, URL, dan DateTime bersuffix `{runId}-045` tidak tersimpan)
35. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sama dengan sumber (136, 137, 138, 139). Pada TC-FA-CF-136 nilai diuji `101`, `-1`, lalu `100` (urutan sumber `100`, `101`, `-1`) karena Submit dengan `100` menyimpan field dan menutup modal; nilai yang ditolak harus lebih dulu agar tetap pada modal yang sama.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 6, 9, 12, 18, 24, 30, 32, 33, 35, serta pengisian form sebagai bagian langkah TC. Langkah 33 sampai 35 membuktikan lewat satu baris tersimpan sebagai anchor positif bahwa tiga field yang ditolak tidak muncul.
- Asersi "nilai `100` diterima" ditulis sebagai toast sukses baku `Success, custom field has been created.` (tertulis di TC-FA-CF-141, 143, dan 155); asersi tambahan itu dicatat sesuai S-03. "Submit ditolak" diamati lewat modal yang tetap terbuka.
- Teks pesan validasi Percentage, Email, URL, dan DateTime tidak diassert sesuai NC-15.
- Temuan untuk QA:
  - TC-FA-CF-136: Langkah Uji hanya mengklik [Submit] sekali sesudah Value `-1`, sedangkan Expected b mengasersi penolakan `101` dan `-1`; spec mengklik [Submit] pada tiap nilai (langkah 4, 7, dan 10) agar tiap penolakan teramati.
  - Nama field memakai suffix `{runId}-045` (S-12) sehingga tidak sama dengan `Global Percentage`, `Global Email`, `Global URL`, dan `Global DateTime` pada Data Uji TC.
