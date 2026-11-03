---
id: TC-FA-RP-E2E-311-modal-changelog-title-kolom-object-dan-placeholder-per-varian
title: "Modal Changelog: Title, kolom Object, dan placeholder tiap varian"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-761
coverage:
  web: automated
---

# Modal Changelog: Title, kolom Object, dan placeholder tiap varian

## Prerequisites

- Mode: FE+BE
- Akun: Total Control pada client `Company Changelog` (Pre-setup #24), akun disediakan tim FE; email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA), `Spectra.env.FA_CHANGELOG_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #24 (`Company Changelog`: 25 entri log campuran seluruh varian), #43 (Seed GM beragam: Fajar Nugroho GM di `IT Infrastructure`; Kevin Susanto GM di `Data Center`; Lina Marlina GM di `Head Office`), #18 (pohon Group Company Alpha), dan #19 (seed Role Transaksi pada `IT Infrastructure` untuk sub-tab Disposal). Seluruhnya dipakai sebagai precondition TC, tidak diasersi. Spec ini tidak mengubah data.
- Tabel Varian modal Changelog:

| Varian | Cara membuka Changelog | Title | Kolom Object | Placeholder Search | Placeholder filter Object |
|---|---|---|---|---|---|
| Tab Total Control | tab awal; klik ikon Changelog pada toolbar | `Changelog: Role & Permission > Total Control` | `User Name` | `Search action, user, or value...` | `All users` |
| Tab Read Only | klik Tab `Read Only`; klik ikon Changelog pada toolbar | `Changelog: Role & Permission > Read Only` | `User Name` | `Search action, user, or value...` | `All users` |
| Tab Group Manager | klik Tab `Group Manager`; klik ikon Changelog pada toolbar | `Changelog: Role & Permission > Group Manager` | `User Name — Group Name` | `Search action, user, group, or value...` | `All users` |
| Tab System | klik Tab `System`; klik ikon Changelog pada toolbar | `Changelog: Role & Permission > System` | `Role — User` | `Search action, role, user, or value...` | `All roles` |
| Detail Role `Manage files` | klik Tab `System`; klik Role Name `Manage files`; klik ikon Changelog pada toolbar Detail Role | `Changelog: Role & Permission > Manage files` | `Role Name — User` | `Search action, user, or value...` | `All users` |
| Detail Role `Manage accounting` | klik Tab `System`; klik Role Name `Manage accounting`; klik ikon Changelog pada toolbar Detail Role | `Changelog: Role & Permission > Manage accounting` | `Role Name — User` | `Search action, user, or value...` | `All users` |
| Transaction Role sub-tab `Disposal` | klik Tab `Transaction Role`; klik sub-tab `Disposal`; klik ikon `[Changelog]` di baris sub-tab | `Changelog: Role & Permission > Transaction Role > Disposal` | tanpa kolom Object | `Search action, role, group, user, or value...` | tanpa filter Object |

## Test Steps

1. Untuk setiap baris pada tabel Varian modal Changelog, lakukan langkah 2 sampai 12.
2. Buka halaman Role & Permission lewat menu sidebar (kembali ke Tab `Total Control`).
3. Buka Changelog varian sesuai kolom Cara membuka Changelog pada tabel.
4. Verifikasi Title modal sesuai kolom Title pada tabel.
5. Verifikasi kolom Object sesuai kolom Kolom Object pada tabel (varian Transaction Role tanpa kolom Object).
6. Klik ikon Search.
7. Verifikasi placeholder Search sesuai kolom Placeholder Search pada tabel.
8. Klik ikon `(←)` pada kotak Search.
9. Klik ikon Filter.
10. Verifikasi panel Filter tampil dengan field filter Object sesuai kolom Placeholder filter Object pada tabel (varian Transaction Role tanpa filter Object).
11. Verifikasi teks `All objects` tidak muncul pada panel Filter.
12. Klik ikon Filter untuk menutup panel, lalu tutup modal Changelog.

## Notes

- Alasan di atas 35 langkah: langkah 2 sampai 12 adalah blok berulang dengan parameter pada tabel Prerequisites (tujuh iterasi); seluruh blok berkelas fungsional sama, dataset sama (satu TC), dan tiap iterasi berdiri sendiri. Langkah yang diulang: 2 sampai 12. Tanpa ekspansi, spec berisi 12 langkah.
- Langkah penghubung (S-03): langkah 1 (kepala perulangan), 2 (mereset ke halaman awal antar varian), 8 (menutup input Search), dan 12 (menutup panel dan modal). Langkah 10 menjadi anchor positif bagi asersi absence langkah 11 (bagian 8b butir 2).
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite.
- Copy bertanda `copy usulan, PRD 12 #1` (placeholder Search dan placeholder filter Object tiap varian) diasersi literal sesuai TC; asersi itu bergantung pada persetujuan PM atas copy tersebut.
- TC 761 satu-satunya TC di spec ini; TC 759 dan 760 ada di spec `TC-FA-RP-E2E-231-modal-changelog-pagination-download-kombinasi-dan-varian-4`.
- Temuan untuk QA:
  - Email dan password akun Total Control `Company Changelog` tidak tertulis di Pre-setup TC (hanya data #24); akun disediakan tim FE.
  - Precondition TC 761 menyebut #24 bersama #43, #18, dan #19 (data Company Alpha); spec memakai akun Total Control `Company Changelog` dan menganggap #43, #18, #19 tersedia pada client itu.
  - TC 761 menyebut kolom Object `User Name — Group Name` dan `Role — User` tanpa menyebut apakah teks header sama persis dengan pola tersebut; spec mengasersi teks sesuai TC.
