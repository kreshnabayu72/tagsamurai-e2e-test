---
id: TC-FA-RP-E2E-232-modal-changelog-pagination-download-kombinasi-dan-varian-5
title: "Modal Changelog: Pagination, Download, kombinasi, dan varian (5/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-762
  - TC-FA-RP-763
  - TC-FA-RP-1084
coverage:
  web: automated
---

# Modal Changelog: Pagination, Download, kombinasi, dan varian (5/5)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control pada client `Company Changelog` (Pre-setup #24), akun disediakan tim FE; email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA), `Spectra.env.FA_CHANGELOG_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #24 (`Company Changelog`: 25 entri log campuran seluruh varian, aktor dan tanggal berbeda, serta Total Control dan Read Only). Pre-setup #43, #18, dan #19 disebut Precondition TC 763 dan dipakai sebagai precondition TC, tidak diasersi. Spec ini tidak mengubah data.
- Kemampuan teknis: pembaca nama berkas unduhan; disediakan tim FE/BE.
- Tabel Varian Download (TC 763):

| Varian | Cara membuka Changelog | Nama berkas |
|---|---|---|
| Tab Total Control | tab awal; klik ikon Changelog pada toolbar | `Changelog-Role-Permission-Total-Control` |
| Tab Read Only | klik Tab `Read Only`; klik ikon Changelog pada toolbar | `Changelog-Role-Permission-Read-Only` |
| Tab Group Manager | klik Tab `Group Manager`; klik ikon Changelog pada toolbar | `Changelog-Role-Permission-Group-Manager` |
| Tab System | klik Tab `System`; klik ikon Changelog pada toolbar | `Changelog-Role-Permission-System` |
| Detail Role `Manage files` | klik Tab `System`; klik Role Name `Manage files`; klik ikon Changelog pada toolbar | `Changelog-Role-Permission-Manage-Files` |
| Detail Role `Manage asset & TAG` | klik Tab `System`; klik Role Name `Manage asset & TAG`; klik ikon Changelog pada toolbar | `Changelog-Role-Permission-Manage-Asset-And-TAG` |
| Transaction Role sub-tab `Disposal` | klik Tab `Transaction Role`; klik sub-tab `Disposal`; klik ikon `[Changelog]` di baris sub-tab | `Changelog-Role-Permission-Transaction-Role-Disposal` |


## Test Steps

### Filter Field hanya pada varian Tab System, Detail Role, dan Transaction Role (TC 762)

1. Klik Tab `System`.
2. Klik ikon Changelog pada toolbar.
3. Klik ikon Filter.
4. Verifikasi panel Filter memuat field `Field` (`All fields`).
5. Klik ikon Filter untuk menutup panel, lalu tutup modal Changelog.
6. Klik Tab `Group Manager`.
7. Klik ikon Changelog pada toolbar.
8. Klik ikon Filter.
9. Verifikasi panel Filter memuat field `Date`.
10. Verifikasi panel Filter tidak memuat field `Field` (nilai tunggal `Group Manager`).
11. Klik ikon Filter untuk menutup panel, lalu tutup modal Changelog.

### Filename Download Changelog tiap varian (TC 763)

12. Untuk setiap baris pada tabel Varian Download, lakukan langkah 13 sampai 17.
13. Buka halaman Role & Permission lewat menu sidebar (kembali ke Tab `Total Control`).
14. Buka Changelog varian sesuai kolom Cara membuka Changelog pada tabel.
15. Klik ikon Download, lalu klik `Download as CSV`.
16. Verifikasi berkas terunduh dengan nama sesuai kolom Nama berkas pada tabel dan extension `.csv`.
17. Tutup modal Changelog.
18. Verifikasi tidak ada berkas `Changelog-Role-Permission-Approval-Config` di antara ketujuh berkas yang terunduh.

### Sort kolom Field Tab System (TC 1084)

19. Buka halaman Role & Permission lewat menu sidebar (kembali ke Tab `Total Control`).
20. Klik Tab `System`.
21. Klik ikon Changelog pada toolbar.
22. Klik header kolom Field sekali.
23. Verifikasi kolom Field ascending dengan nilai Field berurut A-Z.
24. Klik header kolom Field kedua kali.
25. Verifikasi kolom Field descending dengan urutan terbalik dari langkah 23.
26. Klik header kolom Field ketiga kali.
27. Verifikasi urutan kembali ke default sort Date descending.

## Notes

- Langkah penghubung (S-03): langkah 5 dan 11 (menutup panel dan modal), 12 (kepala perulangan), 13 (mereset ke halaman awal antar varian), 17 (menutup modal), dan 19 (kembali ke halaman awal sebelum TC 1084). Langkah 9 menjadi anchor positif bagi asersi absence langkah 10 (bagian 8b butir 2).
- Langkah 13 sampai 17 diulang per varian (tujuh iterasi); parameter ada pada tabel Prerequisites dan tanpa langkah bersyarat.
- Klausa TC 763 "tidak ada varian modal maupun berkas Changelog-Role-Permission-Approval-Config" diasersi hanya sebagai ketiadaan berkas pada langkah 18; klausa "varian modal" tidak punya langkah observasi di TC.
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite.
- Temuan untuk QA:
  - Email dan password akun Total Control `Company Changelog` tidak tertulis di Pre-setup TC (hanya data #24); akun disediakan tim FE.
  - Precondition TC 762, 763, dan 1084 menyebut #24 (Company Changelog); TC 763 juga menyebut #43, #18, dan #19; spec memakai akun Total Control `Company Changelog` untuk seluruh isi spec ini.
  - TC 763 menyebut Role Name `Manage asset & TAG` tanpa section (Global Role atau Group Role); spec mengikuti TC.
  - TC 762 butir b hanya menyebut ketiadaan field `Field`; spec menambah `Verifikasi` field `Date` sebagai anchor panel (S-03).
  - TC 1084 tidak menyebut nilai Field yang diurutkan; spec mengasersi urutan A-Z nilai yang tampil.
