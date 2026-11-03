---
id: TC-AC-ACC-E2E-254-modal-changelog-asset-control-screening-isi-kolom-search-dan-download
title: "Modal Changelog: Asset Control: Screening, Isi Kolom Object dan Field, Search per Kolom, dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-349
  - TC-AC-ACC-351
  - TC-AC-ACC-352
  - TC-AC-ACC-355
coverage:
  web: automated
---

# Modal Changelog: Asset Control: Screening, Isi Kolom Object dan Field, Search per Kolom, dan Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca): Client C-01 "PT Sejahtera Abadi" (Tab Asset Control).
- Data fixture Tabel A3 (hanya dibaca, skrip seed): riwayat Changelog Asset Control AL-01 (10 Jan 2026 08:00, Action `Generate Enrollment QR`, Object `Enrollment Token`, Field `Status`, Old Value `—`, New Value `Active`, Modified By Andi Wijaya); AL-02 (02 Mar 2026 09:00, `Deactivate Station`, `Gerbang Lama`, `Status`, `Inactive`, `Deactivated`, Budi Santoso); AL-03 (12 Dec 2025 10:00, `Revoke Tablet`, `Tablet Lama`, `Status`, `Active`, `Revoked`, Citra Dewi).
- Parameter blok TC-AC-ACC-351 (langkah 19 sampai 22):

| Kolom | Kata kunci | Baris tampil | Baris tidak tampil |
|---|---|---|---|
| Action | revoke | AL-03 | AL-01 |
| Object | gerbang | AL-02 | AL-01 |
| Old Value | inactive | AL-02 | AL-03 |
| New Value | deactivated | AL-02 | AL-03 |
| Modified By | budi | AL-02 | AL-01 |

- Kemampuan teknis: penangkapan nama berkas unduhan di browser uji (disediakan tim FE). Changelog adalah audit trail permanen: ukuran halaman 100 dan Search dipakai untuk baris seed (S-14); total baris tidak diasersi sebagai angka absolut (S-12).
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search "PT Sejahtera Abadi" di List Client, tekan Enter, klik Company Name "PT Sejahtera Abadi", lalu klik Tab Asset Control

### TC-AC-ACC-349: Screening Modal Changelog: Asset Control

2. Klik ikon Changelog di Tab Asset Control
3. Verifikasi Header: Title "Changelog: Asset Control"
4. Verifikasi Toolbar: Search dengan placeholder "Search action, field, or value..."
5. Verifikasi Toolbar: `Filter` dan `Download` tampil
6. Verifikasi tabel memuat kolom `Date`, `Action`, `Object`, `Field`, `Old Value`, `New Value`, `Modified By`, `Column Visibility (⋯)`
7. Verifikasi urutan default Date terbaru
8. Verifikasi tabel read-only tanpa row action
9. Verifikasi Footer: Pagination dengan default 10 baris per halaman
10. Verifikasi opsi ukuran halaman 10, 25, 50, 100
11. Verifikasi modal berlebar 800 px dan tinggi hug content maksimum 648 px

### TC-AC-ACC-355: Kolom Object berisi objek berubah dan Field hanya Status

12. Ubah ukuran halaman modal menjadi 100 baris, ketik Search "Status", tekan Enter
13. Verifikasi Object baris AL-01 `Enrollment Token`, baris AL-02 nama Station `Gerbang Lama`, dan baris AL-03 nama Tablet `Tablet Lama`
14. Verifikasi kolom Field baris AL-01, AL-02, dan AL-03 selalu `Status`
15. Klik Filter pada toolbar modal
16. Verifikasi panel Filter tidak memiliki field filter untuk kolom Field
17. Klik ulang ikon Filter untuk menutup panel, lalu klik ikon ✕ pada input Search dan tekan Enter

### TC-AC-ACC-351: Search per kolom

18. Klik ikon Search
19. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-351" (langkah 19 sampai 22): ketik kata kunci pada kolom Search, tekan Enter
20. Verifikasi baris pada kolom "Baris tampil" tampil
21. Verifikasi baris pada kolom "Baris tidak tampil" tidak tampil
22. Klik ikon ✕ pada input Search lalu tekan Enter
23. Ketik Search "status", tekan Enter
24. Verifikasi baris AL-01, AL-02, dan AL-03 tampil (Field bernilai Status pada ketiga baris)
25. Klik ikon ✕ pada input Search lalu tekan Enter

### TC-AC-ACC-352: Download Changelog: Asset Control

26. Klik Download pada toolbar modal
27. Verifikasi overlay memuat opsi "Download as CSV" dan "Download as XLSX"
28. Klik "Download as CSV"
29. Verifikasi tidak ada toast sukses
30. Verifikasi berkas `Changelog-AssetControl-PT Sejahtera Abadi.csv` terunduh
31. Klik Download lagi lalu klik "Download as XLSX"
32. Verifikasi tidak ada toast sukses
33. Verifikasi berkas `Changelog-AssetControl-PT Sejahtera Abadi.xlsx` terunduh

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search dan buka Detail Client; hook suite hanya membuka List Client), langkah 12 (Search "Status" memperkecil baris audit trail ke baris seed, S-14), langkah 17 (menutup panel Filter lewat klik ulang ikon Filter, D-001 `docs/spec-decisions.md`, dan mengosongkan Search), langkah 22 dan 25 (mengosongkan Search).
- Langkah 19 sampai 22 diulang untuk 5 baris tabel parameter (20 langkah setelah ekspansi); Field ditulis eksplisit (langkah 23 sampai 25) karena tidak punya baris yang tidak tampil. Urutan TC (349, 355, 351, 352) berbeda dari urutan nomor TC agar screening dan isi kolom di awal.
- Spec ini melewati sekitar 35 langkah setelah ekspansi. Alasan: semua blok satu topik (Modal Changelog: Asset Control, baca-saja atas data seed) pada satu modal; Search dikosongkan di antara blok sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: Filter dan Sort Changelog: Asset Control ada di spec 255; Setup Column di spec 256 sampai 260; empty state genuinely kosong di spec 261; SSE di spec 262; isolasi per viewer di spec 263 dan 264; pencatatan nyata Generate, Deactivate, dan Revoke di Changelog ada di spec 234, 238, 239, dan 270.
- Temuan untuk QA:
  - TC-AC-ACC-355 langkah 1 ("Buka Changelog Asset Control setelah Generate, Deactivate, Revoke") tidak menyebut Client dan data aksi; spec membaca baris seed AL-01 sampai AL-03 yang mencerminkan ketiga aksi tersebut (Object `Enrollment Token`, nama Station, nama Tablet).
  - TC-AC-ACC-349 mensyaratkan ">10 baris" riwayat Changelog sedangkan fixture AL-01 sampai AL-03 hanya tiga baris untuk "PT Sejahtera Abadi"; asersi pagination default 10 tetap diasersi sebagai elemen UI.
