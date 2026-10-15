---
id: TC-AC-PP-E2E-002-published-by-seed-satu-kata-akun-dihapus
title: "Published By: Nilai Seed System, Nama Satu Kata, dan Snapshot Akun Dihapus pada Tampil, Search, Filter, dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-04
  - TC-AC-PP-105
  - TC-AC-PP-107
  - TC-AC-PP-124
coverage:
  web: automated
---

# Published By: Nilai Seed System, Nama Satu Kata, dan Snapshot Akun Dihapus pada Tampil, Search, Filter, dan Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Dataset Riwayat S: Version 1 (Published By `System`, hasil seed), Version 2 (`Budi`), Version 3 (`Jane Smith`, akun sudah dihapus). Hook `before` men-seed dataset ini lewat Fixture BE (riwayat append-only, tidak dapat dihapus lewat UI); hook `after` mengembalikan dataset ke Riwayat A. Spec read-only, tidak membuat data.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah).
- Kemampuan teknis: Fixture BE (membuat ulang dataset Riwayat S). Tidak memakai intercept, jam server, atau klien HTTP.
- Dokumen Privacy Policy bersifat tunggal platform-wide; suite berjalan serial (`parallel: false`).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-PP-04: Baris Version 1 hasil seed menampilkan Published By `System` dan nama satu kata tampil utuh

1. Klik menu Settings > Privacy Policy di sidebar
2. Amati sel Published By baris `Version 1` dan baris `Version 2`
3. Hover teks pada sel Published By baris `Version 1`
4. Verifikasi baris `Version 1` menampilkan `System` apa adanya (bukan `—`)
5. Verifikasi tooltip `System` tampil
6. Hover teks pada sel Published By baris `Version 2`
7. Verifikasi baris `Version 2` menampilkan `Budi` tanpa inisial tambahan
8. Verifikasi tooltip `Budi` tampil

### TC-AC-PP-105: Search menemukan nama snapshot pengguna yang sudah dihapus dan nilai seed `System`

9. Klik icon Search, ketik "system", tekan Enter
10. Verifikasi hanya baris `Version 1` dengan Published By `System` tampil
11. Ganti keyword dengan "jane smith", tekan Enter
12. Verifikasi hanya baris `Version 3` dengan Published By `Jane S` tampil
13. Verifikasi baris `Version 3` tetap tampil walau akun Jane Smith sudah dihapus
14. Ganti keyword dengan "budi", tekan Enter
15. Verifikasi hanya baris `Version 2` dengan Published By `Budi` tampil
16. Klik icon `(←)` untuk menutup search dan mereset tabel

### TC-AC-PP-107: Isi opsi dropdown Published By dipopulasi dari nama lengkap snapshot yang ada di tabel

17. Klik icon Filter di toolbar sehingga panel Filter terbuka
18. Klik field `Published By`
19. Verifikasi dropdown menampilkan tepat tiga opsi: `Budi`, `Jane Smith`, `System` (urutan opsi tidak diasersi)
20. Verifikasi nama tampil dalam bentuk lengkap, bukan bentuk singkat `Jane S`
21. Verifikasi tidak ada opsi untuk nama yang tidak ada di tabel
22. Tutup dropdown dan panel Filter tanpa menekan `[Apply]`

### TC-AC-PP-124: Sort kolom Published By berdasarkan nama lengkap snapshot, bukan format singkat

23. Klik header `Published By` satu kali
24. Verifikasi urutan Published By (A–Z nama lengkap): `Budi` (Version 2), `Jane S` (Version 3), `System` (Version 1)
25. Klik header `Published By` kedua kali
26. Verifikasi urutan Published By (Z–A): `System`, `Jane S`, `Budi`
27. Klik header `Published By` ketiga kali
28. Verifikasi indikator sort pada header `Published By` hilang
29. Verifikasi urutan kembali ke default Published At Newest First (`Jane S`, `Budi`, `System`)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Semua TC memakai dataset Riwayat S yang sama (read-only), digabung dalam satu spec.
- Langkah penghubung (tanpa awalan Verifikasi, S-03/S-09): langkah 16 (tutup Search dan reset tabel), langkah 22 (tutup dropdown dan panel Filter tanpa Apply sehingga tidak ada filter aktif yang memengaruhi sort), langkah 2, 3, 6 (amati/hover untuk asersi tooltip).
- Urutan mengikuti prinsip 3: screening (TC-AC-PP-04) di awal, lalu Search, Filter, Sort; TC sumber memakai urutan nomor yang sama.
- Temuan untuk QA:
  - TC-AC-PP-124 Expected c menyebut urutan default `Jane S`, `Budi`, `System`, tetapi Tabel Data Uji Riwayat S tidak menyebut nilai Published At per versi; urutan default itu bergantung pada Published At yang tidak dituliskan (kurang precondition).
  - TC-AC-PP-107 Data Uji menyebut dataset tanpa nilai Published At; tidak berdampak pada asersi.
