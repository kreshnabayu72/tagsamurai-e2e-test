---
id: TC-FA-CF-E2E-119-changelog-filter-screening-dropdown-dan-modified-by
title: "Modal Changelog: Filter Screening, Dropdown, dan Modified By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-463
  - TC-FA-CF-464
  - TC-FA-CF-465
  - TC-FA-CF-466
coverage:
  web: automated
---

# Modal Changelog: Filter Screening, Dropdown, dan Modified By

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Changelog (Pre-setup #19) dengan email mengikuti pola Pre-setup #1 `totalControl_automated_{namaCompany}@qwertysystem.net` dan `{namaCompany}` = Company Changelog (email akun ini tidak tertulis di Pre-setup TC, lihat Temuan untuk QA). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_CHANGELOG_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_CHANGELOG_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Data Pre-setup (tetap di environment, tidak diubah spec ini): Company Changelog (Pre-setup #19; Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Jakarta) dengan dua belas entri Changelog tab General dan dua entri Create tab Purchasing, dirujuk lewat fixture baru `Fixture.faCustomFields.changelogSeed` (fixture belum ada, disediakan tim FE). Seed dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE). Entri seed tab General (Action | Field Name | Field | Modified By), urutan seeding terbaru ke terlama:
  - L1 `Create` | `Asset Serial Tag` | `Name` | `Budi S`
  - L2 `Edit` | `Storage Capacity` | `Scope` | `Siti A`
  - L3 `Activate` | `Equipment Class` | `Active` | `Siti A`
  - L4 `Edit` | `Operating Voltage` | `Global Value` | `Budi S`
  - L5 `Deactivate` | `Total Cost` | `Active` | `Joko W`
  - L6 `Delete` | `Old Field` | `Name` | `Joko W`
  - L7 `Bulk Delete` | `Old Field B` | `Name` | `Joko W`
  - L8 `Edit` | `Depreciated Ratio` | `Required` | `Joko W`
  - L9 `Edit` | `Equipment Class` | `Dropdown Options` | `Siti A`
  - L10 `Edit` | `Compliance File` | `Data Type` | `Budi S`
  - L11 `Edit` | `Legacy Tag` | `Placeholder` | `Joko W`
  - L12 `Edit` | `Asset Serial Tag` | `Name` | `Budi S`
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data dan tidak menambah entri Changelog.
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan opsi dropdown filter dan isi baris tabel Modal Changelog.
- State global: tidak ada yang diubah.

## Test Steps

1. Klik icon Changelog di toolbar

### TC-FA-CF-463: Screening Filter Panel Modal Changelog

2. Klik icon Filter di toolbar modal
3. Verifikasi field Filter Panel berurutan: `Date` (date range, `Select date`), `Action` (`All actions`), `Field Name` (`All field names`), `Field` (`All fields`), `Modified By` (`All users`)
4. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil

### TC-FA-CF-464: Opsi filter Modal Changelog diambil dari entri log tab aktif

5. Buka dropdown Action
6. Verifikasi opsi Action: `Activate`, `Bulk Delete`, `Create`, `Deactivate`, `Delete`, `Edit` (tepat enam nilai yang ada di log)
7. Tutup dropdown Action
8. Buka dropdown Field
9. Verifikasi opsi Field: `Active`, `Data Type`, `Dropdown Options`, `Global Value`, `Name`, `Placeholder`, `Required`, `Scope` (hanya properti yang tercatat)
10. Tutup dropdown Field

### TC-FA-CF-465: Filter dropdown multi-select standar menyaring Action, Field Name, dan Field

11. Pilih Action `Edit`, klik `[Apply]`
12. Verifikasi tujuh entri `Edit` tampil: `Storage Capacity`, `Operating Voltage`, `Depreciated Ratio`, `Equipment Class`, `Compliance File`, `Legacy Tag`, dan `Asset Serial Tag`
13. Klik `[Clear Field]`, pilih Field Name `Asset Serial Tag`, klik `[Apply]`
14. Verifikasi dua entri `Asset Serial Tag` tampil: Create dan rename
15. Klik `[Clear Field]`, pilih Field `Name`, klik `[Apply]`
16. Verifikasi entri Create, Delete, Bulk Delete, dan rename tampil

### TC-FA-CF-466: Filter Modified By Changelog berlabel singkat dan menyaring dengan nama lengkap

17. Klik `[Clear Field]`, pilih Modified By `Siti A`, klik `[Apply]`
18. Verifikasi tiga entri milik Siti Amelia tampil: `Storage Capacity` (Edit), `Equipment Class` (Activate), dan `Equipment Class` (Edit Dropdown Options)
19. Verifikasi tidak ada entri milik Budi S atau Joko W pada tabel
20. Klik `[Clear Field]`, lalu klik `[Apply]`
21. Klik icon `[✕]` untuk menutup modal

## Notes

- Spec memuat 21 langkah, di bawah ambang sekitar 35 langkah. Satu topik (Filter Modal Changelog: screening, opsi, dan penyaringan dropdown), satu akun, satu dataset (Company Changelog) tanpa mengubah data.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka modal sesuai langkah uji TC), langkah 7 dan 10 (menutup dropdown), langkah 20 dan 21 (membersihkan filter dan menutup modal). Langkah `[Clear Field]` pada langkah 13, 15, dan 17 adalah "Bersihkan" sesuai langkah uji TC-FA-CF-465.
- Anchor absence: langkah 18 (tiga entri tampil) mendahului absence langkah 19 (bagian 8b butir 2).
- Hitungan entri pada langkah 12, 14, dan 18 diturunkan dari seed Pre-setup #19 yang dipulihkan hook `before`; spec tidak menulis entri sehingga hitungan itu tetap.
- Temuan untuk QA:
  - Email akun Total Control Company Changelog tidak tertulis di Pre-setup TC; spec memakai pola Pre-setup #1, dan akunnya disediakan tim FE.
  - TC-FA-CF-464 Expected ("tepat enam nilai", "hanya properti yang tercatat") bergantung pada audit trail Company Changelog yang tidak bertambah entri jenis lain; Changelog bersifat permanen, sehingga hasil bergantung pada seed reset Company.
  - TC-FA-CF-465 Expected a sampai c menyebut hitungan entri (tujuh, dua) tanpa menyebut nama entri; spec menurunkan namanya dari Pre-setup #19. Audit trail tidak boleh diasersi sebagai angka absolut (S-12), sehingga asersi memakai nama entri seed.
  - TC-FA-CF-466 judul ("berlabel singkat") tidak punya Expected yang memeriksa label opsi; spec hanya memeriksa hasil Filter dan memilih opsi `Siti A`.
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
