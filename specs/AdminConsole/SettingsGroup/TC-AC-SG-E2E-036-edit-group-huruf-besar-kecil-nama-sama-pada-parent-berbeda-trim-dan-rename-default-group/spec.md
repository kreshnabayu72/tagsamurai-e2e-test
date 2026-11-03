---
id: TC-AC-SG-E2E-036-edit-group-huruf-besar-kecil-nama-sama-pada-parent-berbeda-trim-dan-rename-default-group
title: "Edit Group: Huruf Besar/Kecil, Nama Sama pada Parent Berbeda, Trim, dan Rename Default Group"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-117
  - TC-AC-SG-121
  - TC-AC-SG-123
  - TC-AC-SG-128
coverage:
  web: automated
---

# Edit Group: Huruf Besar/Kecil, Nama Sama pada Parent Berbeda, Trim, dan Rename Default Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data seed milik spec (entitas Principal, di-seed Fixture BE di hook `before`): `Region B-{runId}-036` (level 1); `Region A-{runId}-036` (level 1) dengan anak `Branch 1-{runId}-036`; `Induk-{runId}-036` (level 1) dengan anak `Branch 4-{runId}-036`; `Region C-{runId}-036` (level 1). Nama TC diganti nama bersuffix karena target aksi tulis tidak memakai node Pre-setup bersama (S-06):

| TC | Nama di TC | Awal di spec | Hasil di spec |
|---|---|---|---|
| TC-AC-SG-117 | `Region B` -> `REGION B` | `Region B-{runId}-036` | `REGION B-{runId}-036` |
| TC-AC-SG-121 | `Branch 4` -> `Branch 1` | `Branch 4-{runId}-036` (anak `Induk-{runId}-036`) | `Branch 1-{runId}-036` (sudah ada di bawah `Region A-{runId}-036`) |
| TC-AC-SG-123 | `Region C` -> `   Region C Trim   ` | `Region C-{runId}-036` | `Region C Trim-{runId}-036` |

- TC-AC-SG-128 menuntut node Pre-setup `Default Group` entitas Principal (pengecualian S-06): `Default Group` di-rename menjadi `Kantor Utama`; Fixture BE memulihkan baseline `Pohon Uji Utama` di hook `before` dan `after` dan sebagai langkah penghubung (disediakan tim FE/BE, lihat `suite.md`). Efek: Last Updated dan Modified By `Default Group` dipulihkan oleh baseline Fixture BE; entri Changelog Group yang bertambah adalah audit trail permanen dan tidak dihapus.
- Asersi Last Updated memakai satu cara: waktu dicatat sesudah `[Save]`, Last Updated dibandingkan dengan waktu itu dengan toleransi satu menit; jam server dan jam browser sinkron. Modified By diasersi berformat `[First Name] [Last Initial]` (`Budi S`).
- Jumlah entri Changelog Group (N) dibaca lewat kemampuan baca Changelog (disediakan tim FE/BE) sebelum aksi; asersi memakai selisih terhadap N, bukan angka absolut.
- Pemulihan: hook `after` menghapus seluruh group milik spec lewat Fixture BE.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-117: Hanya huruf besar/kecil dianggap perubahan

1. Catat jumlah entri Changelog Group (N) sebelum aksi
2. Ketik Search `Region B-{runId}-036`, tekan Enter
3. Klik ikon `⋯` pada baris `Region B-{runId}-036`, lalu pilih "Edit"
4. Ubah nama menjadi `REGION B-{runId}-036`, klik `[Save]`
5. Catat waktu sesudah `[Save]`
6. Verifikasi toast sukses: "Success, group has been updated."
7. Verifikasi nama `REGION B-{runId}-036` tampil pada tabel
8. Verifikasi tidak ada error duplikat terhadap diri sendiri pada halaman Settings > Group
9. Verifikasi kolom Modified By pada tabel untuk baris terbarui menjadi `Budi S`
10. Verifikasi kolom Last Updated pada tabel untuk baris terbarui sesuai waktu pada langkah 5 (toleransi satu menit)
11. Klik ikon Changelog pada toolbar
12. Verifikasi Modal "Changelog: Group" tampil
13. Verifikasi jumlah entri Changelog Group bertambah tepat 1 dari N
14. Verifikasi entri terbaru pada Modal "Changelog: Group" adalah entri Edit dengan Old Value `Region B-{runId}-036` dan New Value `REGION B-{runId}-036`
15. Tutup Modal "Changelog: Group"
16. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SG-121: Nama sama dengan group pada parent berbeda

17. Ketik Search `Branch 4-{runId}-036`, tekan Enter
18. Klik ikon `⋯` pada baris `Branch 4-{runId}-036`, lalu pilih "Edit"
19. Ubah nama menjadi `Branch 1-{runId}-036` (ada di bawah `Region A-{runId}-036`, parent berbeda)
20. Verifikasi tidak ada error duplikat pada Group Name
21. Klik `[Save]`
22. Verifikasi toast sukses: "Success, group has been updated."
23. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SG-123: Edit di-trim otomatis

24. Ketik Search `Region C-{runId}-036`, tekan Enter
25. Klik ikon `⋯` pada baris `Region C-{runId}-036`, lalu pilih "Edit"
26. Ketik `   Region C Trim-{runId}-036   ` (spasi di awal dan akhir) pada Group Name, klik `[Save]`
27. Ganti isi kotak Search tabel utama dengan `Region C Trim-{runId}-036`, tekan Enter
28. Verifikasi nama tersimpan `Region C Trim-{runId}-036` tanpa spasi tepi
29. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SG-128: Default Group dapat di-rename

30. Ketik Search `Default Group`, tekan Enter
31. Klik ikon `⋯` pada baris `Default Group`, lalu pilih "Edit"
32. Ubah nama menjadi `Kantor Utama`, klik `[Save]`
33. Verifikasi toast sukses: "Success, group has been updated."
34. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
35. Pulihkan baseline `Pohon Uji Utama` lewat Fixture BE (nama `Default Group` dikembalikan)

## Notes

- Langkah penghubung (S-03): langkah 1 dan 5 (baseline dan penanda waktu), langkah 2, 17, 24, dan 30 (Search untuk menemukan baris target, R-16), langkah 27 (mengganti isi Search dengan nama hasil trim karena Search `Region C-{runId}-036` masih aktif setelah rename dan tidak lagi memuat baris itu, R-16), langkah 15 (menutup modal), langkah 16, 23, 29, dan 34 (reset Search, S-09), langkah 35 (pemulihan baseline).
- TC-AC-SG-128 Expected "tidak ada logic yang bergantung pada nama `Default Group`" adalah kesimpulan dari keberhasilan rename (langkah 33) dan tidak teramati terpisah (S-03).
- Temuan untuk QA: TC-AC-SG-117 Expected memuat "Changelog mencatat 1 entri Edit"; TC tidak menyebut cara membaca N sebelum aksi, sehingga spec memakai kemampuan baca Changelog (disediakan tim FE/BE) untuk baseline.
