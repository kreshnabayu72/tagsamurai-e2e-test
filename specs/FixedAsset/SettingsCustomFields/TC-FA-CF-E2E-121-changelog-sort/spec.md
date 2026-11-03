---
id: TC-FA-CF-E2E-121-changelog-sort
title: "Modal Changelog: Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-470
  - TC-FA-CF-471
  - TC-FA-CF-472
  - TC-FA-CF-473
coverage:
  web: automated
---

# Modal Changelog: Sort

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Changelog (Pre-setup #19) dengan email mengikuti pola Pre-setup #1 `totalControl_automated_{namaCompany}@qwertysystem.net` dan `{namaCompany}` = Company Changelog (email akun ini tidak tertulis di Pre-setup TC, lihat Temuan untuk QA). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_CHANGELOG_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_CHANGELOG_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Data Pre-setup (tetap di environment, tidak diubah spec ini): Company Changelog (Pre-setup #19; Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Jakarta) dengan dua belas entri Changelog tab General (halaman 1 memuat sepuluh entri, halaman 2 memuat dua entri) dan dua entri Create tab Purchasing, dirujuk lewat fixture baru `Fixture.faCustomFields.changelogSeed` (fixture belum ada, disediakan tim FE). Seed dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE). Entri seed tab General (Date | Action | Field Name | Field | Old Value | New Value | Modified By), urutan seeding terbaru ke terlama:
  - L1 `17/10/26, 10:45` | `Create` | `Asset Serial Tag` | `Name` | `—` | `Asset Serial Tag` | `Budi S`
  - L2 `16/10/26, 14:20` | `Edit` | `Storage Capacity` | `Scope` | `Pump` | `Generator, Pump` | `Siti A`
  - L3 `15/10/26, 11:30` | `Activate` | `Equipment Class` | `Active` | `Inactive` | `Active` | `Siti A`
  - L4 `14/10/26, 09:05` | `Edit` | `Operating Voltage` | `Global Value` | `Generator: 200V` | `Generator: 220V` | `Budi S`
  - L5 `13/10/26, 16:30` | `Deactivate` | `Total Cost` | `Active` | `Active` | `Inactive` | `Joko W`
  - L6 `12/10/26, 08:10` | `Delete` | `Old Field` | `Name` | `Old Field` | `—` | `Joko W`
  - L7 `11/10/26, 13:00` | `Bulk Delete` | `Old Field B` | `Name` | `Old Field B` | `—` | `Joko W`
  - L8 `10/10/26, 11:15` | `Edit` | `Depreciated Ratio` | `Required` | `No` | `Yes` | `Joko W`
  - L9 `09/10/26, 10:00` | `Edit` | `Equipment Class` | `Dropdown Options` | `Class A, Class B` | `Class A, Class B, Class C` | `Siti A`
  - L10 `08/10/26, 15:45` | `Edit` | `Compliance File` | `Data Type` | `Text` | `Document` | `Budi S`
  - L11 `07/10/26, 09:30` | `Edit` | `Legacy Tag` | `Placeholder` | `—` | `Enter legacy tag` | `Joko W`
  - L12 `06/10/26, 17:20` | `Edit` | `Asset Serial Tag` | `Name` | `Serial Tag` | `Asset Serial Tag` | `Budi S`
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data dan tidak menambah entri Changelog.
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan urutan baris tabel Modal Changelog dan indikator Sort pada header kolom.
- State global: tidak ada yang diubah (Sort hanya state tampilan).

## Test Steps

1. Klik icon Changelog di toolbar

### TC-FA-CF-470: Sort kolom Date Changelog Newest First default lalu Oldest First

2. Klik header `Date` sekali
3. Verifikasi Oldest First: entri `06/10/26, 17:20` berada di atas
4. Klik header `Date` sekali lagi
5. Verifikasi Newest First: entri `17/10/26, 10:45` berada di atas
6. Klik header `Date` sekali lagi
7. Verifikasi indikator Sort kolom `Date` netral
8. Verifikasi urutan kembali ke default Newest First (entri `17/10/26, 10:45` berada di atas)

### TC-FA-CF-471: Sort kolom Action, Field Name, dan Field Changelog alfabetis A-Z

9. Klik header `Action` sekali
10. Verifikasi Action menaik: `Activate`, `Bulk Delete`, `Create`, `Deactivate`, `Delete`, lalu `Edit`
11. Klik header `Field Name` sekali
12. Verifikasi Field Name menaik A-Z tanpa membedakan huruf besar-kecil: `Asset Serial Tag`, `Compliance File`, `Depreciated Ratio`, `Equipment Class`, `Legacy Tag`, `Old Field`, `Old Field B`, lalu `Operating Voltage`
13. Klik header `Field` sekali
14. Verifikasi Field menaik A-Z: `Active`, `Data Type`, `Dropdown Options`, `Global Value`, `Name`, lalu `Placeholder`

### TC-FA-CF-472: Sort kolom Old Value dan New Value campuran dengan nilai strip di akhir saat menaik

15. Klik header `Old Value` sekali
16. Verifikasi Old Value menaik pada halaman 1: nilai teks terurut (baris teratas `Active`)
17. Pindah ke halaman terakhir
18. Verifikasi Old Value `—` (entri Create) berada di akhir
19. Klik header `New Value` sekali
20. Pindah ke halaman 1
21. Verifikasi New Value menaik pada halaman 1: nilai teks terurut (baris teratas `Active`)
22. Pindah ke halaman terakhir
23. Verifikasi New Value `—` (entri Delete dan Bulk Delete) berada di akhir

### TC-FA-CF-473: Sort kolom Modified By Changelog berdasarkan nama lengkap

24. Pindah ke halaman 1
25. Klik header `Modified By` sekali
26. Verifikasi Modified By menaik berdasarkan nama lengkap: Budi Santoso (`Budi S`), Joko Widodo (`Joko W`), lalu Siti Amelia (`Siti A`)
27. Klik icon `[✕]` untuk menutup modal

## Notes

- Spec memuat 27 langkah, di bawah ambang sekitar 35 langkah. Satu topik (Sort Modal Changelog), satu akun, satu dataset (Company Changelog) tanpa mengubah data.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka modal sesuai langkah uji TC), langkah 17, 20, 22, dan 24 (pindah halaman supaya asersi "di akhir" dan halaman 1 bergantung pada posisi, S-14), langkah 27 (menutup modal).
- Asersi sort memakai baris seed halaman 1 yang dijamin teramati dan halaman terakhir untuk nilai `—` (S-14); setiap kolom yang diurutkan memiliki lebih dari dua nilai distinct pada seed (S-11).
- Temuan untuk QA:
  - Email akun Total Control Company Changelog tidak tertulis di Pre-setup TC; spec memakai pola Pre-setup #1, dan akunnya disediakan tim FE.
  - TC-FA-CF-470 Expected c ("netral kembali ke default Newest First") dipecah menjadi indikator netral dan urutan default (S-01).
  - TC-FA-CF-471 Expected b ("tanpa membedakan huruf besar-kecil") tidak teramati pada seed karena seluruh Field Name berawalan huruf kapital; asersi memeriksa urutan A-Z. Pengujian huruf besar-kecil ada pada Company Nama Khusus (Pre-setup #37) di TC tabel utama.
  - TC-FA-CF-472 Expected a mengaitkan `—` pada Old Value dengan entri Create, padahal entri `Edit` Placeholder (`Legacy Tag`) juga memiliki Old Value `—` pada Pre-setup #19; spec memeriksa nilai `—` berada di akhir tanpa membatasi jenis entri.
  - TC-FA-CF-473 Expected menyebut urutan nama lengkap, sedangkan sel menampilkan `[First Name] [Last Initial]`; spec mengasersi urutan blok Budi S, Joko W, Siti A pada halaman 1.
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
