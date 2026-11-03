---
id: TC-FA-CF-E2E-120-changelog-filter-date-irisan-dan-search
title: "Modal Changelog: Filter Date, Irisan Dua Filter, dan Search Gabungan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-467
  - TC-FA-CF-468
  - TC-FA-CF-469
coverage:
  web: automated
---

# Modal Changelog: Filter Date, Irisan Dua Filter, dan Search Gabungan

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Changelog (Pre-setup #19) dengan email mengikuti pola Pre-setup #1 `totalControl_automated_{namaCompany}@qwertysystem.net` dan `{namaCompany}` = Company Changelog (email akun ini tidak tertulis di Pre-setup TC, lihat Temuan untuk QA). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_CHANGELOG_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_CHANGELOG_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Data Pre-setup (tetap di environment, tidak diubah spec ini): Company Changelog (Pre-setup #19; Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Jakarta) dengan dua belas entri Changelog tab General dan dua entri Create tab Purchasing, dirujuk lewat fixture baru `Fixture.faCustomFields.changelogSeed` (fixture belum ada, disediakan tim FE). Seed dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE). Entri seed yang dipakai: `17/10/26, 10:45` `Create` `Asset Serial Tag` (satu-satunya entri bertanggal 17/10/26); entri `Edit` milik Joko Widodo: `Depreciated Ratio` (Field `Required`, `10/10/26, 11:15`) dan `Legacy Tag` (Field `Placeholder`, `07/10/26, 09:30`); entri `Edit` `Storage Capacity` (Field `Scope`, `16/10/26, 14:20`, satu-satunya entri `Storage Capacity`).
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data dan tidak menambah entri Changelog.
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan isi baris tabel Modal Changelog dan pemilihan rentang tanggal pada kontrol Date.
- State global: tidak ada yang diubah.

## Test Steps

1. Klik icon Changelog di toolbar

### TC-FA-CF-467: Filter Date Modal Changelog inklusif pada satu hari

2. Klik icon Filter di toolbar modal
3. Pilih Date `17/10/26` sampai `17/10/26`
4. Klik `[Apply]`
5. Verifikasi entri tanggal `17/10/26` (`Asset Serial Tag`, `Create`) tampil
6. Verifikasi tidak ada entri bertanggal selain 17/10/26 pada tabel

### TC-FA-CF-468: Kombinasi dua filter Modal Changelog menghasilkan irisan

7. Klik `[Clear Field]`, pilih Action `Edit` dan Modified By `Joko W`, klik `[Apply]`
8. Verifikasi entri `Edit` milik Joko Widodo tampil: `Depreciated Ratio` dan `Legacy Tag`
9. Verifikasi tidak ada entri selain `Edit` milik Joko Widodo pada tabel

### TC-FA-CF-469: Search dan Filter Changelog digabung menghasilkan irisan dan melepas satu memulihkan data

10. Klik `[Clear Field]`, lalu klik `[Apply]`
11. Ketik Search `Storage`, tekan Enter
12. Klik icon Filter, pilih Action `Create`, klik `[Apply]`
13. Verifikasi empty state `No results found` tampil (Search `Storage` irisan Action `Create`)
14. Hapus filter Action (klik `✕` pada chip Action), klik `[Apply]`
15. Verifikasi entri `Storage Capacity` tampil kembali
16. Klik `(←)` pada kotak Search
17. Klik icon `[✕]` untuk menutup modal

## Notes

- Spec memuat 17 langkah, di bawah ambang sekitar 35 langkah. Satu topik (Filter Date, irisan, dan Search gabungan Modal Changelog), satu akun, satu dataset (Company Changelog) tanpa mengubah data.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka modal sesuai langkah uji TC), langkah 7 dan 10 (`[Clear Field]` membersihkan filter sebelumnya), langkah 16 (`(←)` menutup kotak Search dan mereset tabel), langkah 17 (menutup modal). Search pada langkah 11 adalah objek uji TC-FA-CF-469.
- Anchor absence: langkah 5 mendahului absence langkah 6, langkah 8 mendahului langkah 9, dan langkah 13 (empty state hasil Filter) menjadi anchor bagi langkah 15 (bagian 8b butir 2).
- Temuan untuk QA:
  - Email akun Total Control Company Changelog tidak tertulis di Pre-setup TC; spec memakai pola Pre-setup #1, dan akunnya disediakan tim FE.
  - TC-FA-CF-467 dan 468 Expected tidak menyebut nama entri; spec menurunkannya dari Pre-setup #19 (satu entri tanggal 17/10/26; dua entri `Edit` milik Joko Widodo).
  - TC-FA-CF-468 Langkah Uji tidak menyebut pembersihan filter Date dari TC-FA-CF-467; spec menambah `[Clear Field]` (langkah 7).
  - TC-FA-CF-469 Langkah Uji tidak menyebut teks pada Description empty state; spec hanya memeriksa Title `No results found` sesuai Expected a.
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
