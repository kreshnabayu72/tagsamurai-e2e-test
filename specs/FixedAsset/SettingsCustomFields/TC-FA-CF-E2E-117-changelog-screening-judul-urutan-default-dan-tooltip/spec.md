---
id: TC-FA-CF-E2E-117-changelog-screening-judul-urutan-default-dan-tooltip
title: "Modal Changelog: Screening, Judul, Penutupan, Urutan Default, dan Tooltip"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-450
  - TC-FA-CF-451
  - TC-FA-CF-452
  - TC-FA-CF-453
  - TC-FA-CF-456
  - TC-FA-CF-457
coverage:
  web: automated
---

# Modal Changelog: Screening, Judul, Penutupan, Urutan Default, dan Tooltip

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Changelog (Pre-setup #19) dengan email mengikuti pola Pre-setup #1 `totalControl_automated_{namaCompany}@qwertysystem.net` dan `{namaCompany}` = Company Changelog (email akun ini tidak tertulis di Pre-setup TC, lihat Temuan untuk QA). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_CHANGELOG_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_CHANGELOG_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Data Pre-setup (tetap di environment, tidak diubah spec ini): Company Changelog (Pre-setup #19; Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Jakarta) dengan dua belas entri Changelog tab General dan dua entri Create tab Purchasing, dirujuk lewat fixture baru `Fixture.faCustomFields.changelogSeed` (fixture belum ada, disediakan tim FE). Seed dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE). Tiga entri teratas tab General menurut urutan seeding (terbaru ke terlama):

| Seed | Date | Action | Field Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|---|
| L1 | `17/10/26, 10:45` | `Create` | `Asset Serial Tag` | `Name` | `—` | `Asset Serial Tag` | `Budi S` (Budi Santoso) |
| L2 | `16/10/26, 14:20` | `Edit` | `Storage Capacity` | `Scope` | `Pump` | `Generator, Pump` | `Siti A` |
| L3 | `15/10/26, 11:30` | `Activate` | `Equipment Class` | `Active` | `Inactive` | `Active` | `Siti A` |

- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data dan tidak menambah entri Changelog.
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan jumlah entri Changelog tab Purchasing sebelum aksi (N_P; audit trail tidak diasersi sebagai angka absolut, bagian 8b butir 10; dua menurut seed), hover tooltip, penekanan tombol `Esc`, dan klik area backdrop modal.
- State global: tidak ada yang diubah.
- Parameter iterasi langkah 20 dan 21 (tabel Tooltip Modal Changelog, TC-FA-CF-457):

| No | Elemen | Tooltip |
|---|---|---|
| 1 | icon Search pada toolbar modal | `Search` |
| 2 | icon Filter pada toolbar modal | `Filter` |
| 3 | icon Download pada toolbar modal | `Download` |
| 4 | header kolom Actions `(⋯)` | `Column Visibility` |

## Test Steps

1. Catat jumlah entri Changelog tab Purchasing (N_P) sebelum aksi pertama

### TC-FA-CF-450: Screening Modal Changelog: Custom Field tab General

2. Klik icon Changelog di toolbar
3. Perhatikan Header, Body, dan Footer modal
4. Verifikasi Header: judul `Changelog: Custom Field > General`
5. Verifikasi Header: icon close `[✕]` tampil
6. Verifikasi Header: toolbar `Search | Filter | Download` tampil
7. Verifikasi Body: kolom `Date (sortable) | Action (sortable) | Field Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯) (unsortable — header klik = buka Overlay Column Visibility, isi per baris = kosong)`
8. Verifikasi Body: sepuluh entri pertama tampil pada halaman 1
9. Verifikasi Body: sepuluh entri pertama urut Date terbaru di atas
10. Verifikasi Footer: pagination default 10 baris per halaman
11. Verifikasi Footer tidak memuat tombol teks `[Close]`

### TC-FA-CF-453: Urutan default entri Date terbaru ke terlama dengan nilai kolom dan format sesuai definisi

12. Perhatikan tiga baris pertama pada modal yang sedang terbuka
13. Verifikasi baris 1: `17/10/26, 10:45` | `Create` | `Asset Serial Tag` | `Name` | `—` | `Asset Serial Tag` | `Budi S`
14. Verifikasi baris 2: `16/10/26, 14:20` | `Edit` | `Storage Capacity` | `Scope` | `Pump` | `Generator, Pump` | `Siti A`
15. Verifikasi baris 3: `15/10/26, 11:30` | `Activate` | `Equipment Class` | `Active` | `Inactive` | `Active` | `Siti A`
16. Verifikasi kolom Action tampil sebagai teks polos, bukan badge

### TC-FA-CF-456: Kolom Modified By Changelog tampil singkat dengan tooltip nama lengkap

17. Arahkan kursor ke Modified By baris 1
18. Verifikasi sel Modified By baris 1 menampilkan `Budi S`
19. Verifikasi tooltip `Budi Santoso` tampil

### TC-FA-CF-457: Tooltip icon toolbar dan header Actions pada Modal Changelog

Untuk setiap baris tabel Tooltip Modal Changelog pada `## Prerequisites` (langkah 20 dan 21):

20. Arahkan kursor ke elemen
21. Verifikasi tooltip pada elemen sesuai kolom Tooltip tabel tampil

### TC-FA-CF-452: Modal Changelog ditutup lewat icon close dan Esc tetapi tidak oleh klik backdrop

22. Klik area backdrop di luar modal
23. Verifikasi modal tetap terbuka (klik backdrop tidak menutup modal)
24. Klik icon `[✕]`
25. Verifikasi modal tertutup
26. Klik icon Changelog di toolbar
27. Tekan `Esc`
28. Verifikasi modal tertutup

### TC-FA-CF-451: Judul Modal Changelog mengikuti tab aktif

29. Klik tab `Purchasing`
30. Klik icon Changelog di toolbar
31. Verifikasi judul `Changelog: Custom Field > Purchasing`
32. Verifikasi hanya entri grup Purchasing tampil: jumlah entri sama dengan N_P (dua menurut seed)
33. Verifikasi entri tab General (`Storage Capacity`, `Equipment Class`) tidak tampil
34. Klik icon `[✕]` untuk menutup modal

## Notes

- Spec memuat 34 langkah nominal dan sekitar 40 langkah setelah ekspansi blok berparameter (langkah 20 dan 21 diulang empat kali), di atas smell 35 langkah. Alasan: satu topik (screening dan perilaku dasar Modal Changelog), satu akun, satu dataset (Company Changelog) tanpa mengubah data; tiap blok berdiri sendiri dan blok tooltip memakai idiom berparameter (bagian 8b butir 7), sehingga memecahnya hanya menambah login dan hook.
- Langkah yang diulang: langkah 20 dan 21 untuk tiap baris tabel Tooltip Modal Changelog.
- Urutan TC di spec: 450, 453, 456, 457, 452, 451. TC-FA-CF-453, 456, dan 457 memakai modal yang dibuka pada langkah 2 (tidak membuka ulang); TC-FA-CF-452 menutup dan membuka kembali modal; TC-FA-CF-451 di akhir karena berpindah tab. Jumlah buka modal (langkah 2, 26, 30) tidak melebihi jumlah tutup (langkah 25, 28, 34).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (mencatat N_P), langkah 3 (mengamati modal sesuai langkah uji TC-FA-CF-450), langkah 12 (mengamati tiga baris pertama sesuai langkah uji TC-FA-CF-453), langkah 29 dan 34 (pindah tab dan menutup modal).
- Anchor absence: langkah 10 mendahului absence langkah 11; langkah 32 mendahului absence langkah 33 (bagian 8b butir 2).
- Langkah 8 dan 9 memecah klausa "Sepuluh entri pertama urut Date terbaru di atas" (TC-FA-CF-450 Expected Body ii) menjadi jumlah entri dan urutan (S-01).
- Temuan untuk QA:
  - Email akun Total Control Company Changelog tidak tertulis di Pre-setup TC; spec memakai pola Pre-setup #1, dan akunnya disediakan tim FE.
  - TC-FA-CF-451 Expected ("hanya dua entri grup Purchasing") menyebut dua entri tanpa Field Name; karena audit trail tidak boleh diasersi sebagai angka absolut (S-12), spec membandingkan dengan N_P yang dibaca sebelum aksi, dan menyatakan "hanya" lewat ketidakhadiran entri tab General.
  - TC-FA-CF-453 mengasumsikan tidak ada entri baru yang lebih baru daripada `17/10/26, 10:45` pada Company Changelog; audit trail permanen sehingga urutan teratas bergantung pada seed reset Company dan pada tidak adanya spec lain yang menulis entri ke Company ini.
  - TC-FA-CF-452 Langkah Uji tidak menyebut apakah modal harus dibuka ulang sebelum `Esc`; spec membuka ulang modal (langkah 26).
  - TC-FA-CF-457 Langkah Uji "Arahkan kursor ... header kolom Actions" tidak menyebut apakah tooltip diasersi sebelum hover berikutnya; spec memeriksa tiap tooltip tepat setelah hover (bagian 8b butir 5).
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
