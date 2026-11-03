---
id: TC-FA-CAT-E2E-118-modal-changelog-setup-column-guard-satu-kolom-dan-tutup-tanpa-save
title: "Modal Changelog: Guard Satu Kolom Tersisa dan Penutupan Popup Setup Column Tanpa Save"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-411
  - TC-FA-CAT-546
coverage:
  web: automated
---

# Modal Changelog: Guard Satu Kolom Tersisa dan Penutupan Popup Setup Column Tanpa Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 (pohon kategori CatMain) dan #23 (12 baris riwayat Changelog CatMain sesuai Example Data PRD §4.1: Create `Electronics`, Create `Electronics › Laptop`, Create `Vehicle`, Edit rename `Laptop` ke `Notebook` dan Code `LAP-01` ke `NBK-01`, Edit Description `Furniture`, Delete `Kunci Locker`, Delete `Peripheral` dan `Accessory` satu batch, Marked/Restored as Excess, Marked as Excess `Heavy Equipment` oleh System). Seed client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Konfigurasi Setup Column yang disimpan spec ini dipulihkan di hook `after` dengan menghapus preferensi kolom di browser (butir "Pemulihan Setup Column" di `suite.md`), bukan lewat `[Reset to Default]`.

## Test Steps

### TC-FA-CAT-411: Guard satu kolom tersisa pada Setup Column Changelog

1. Klik icon Changelog di Table Tools
2. Klik header Actions (⋯) > `Setup Column...`
3. Hilangkan centang enam kolom (`Date`, `Action`, `Category Name`, `Field`, `Old Value`, `New Value`) hingga tersisa `Modified By`
4. Hover checkbox `Modified By` yang tersisa
5. Verifikasi checkbox `Modified By` disabled
6. Verifikasi tooltip `At least one column must remain visible.` tampil
7. Klik icon close (✕) pada popup Setup Column

### TC-FA-CAT-546: Menutup popup Setup Column Changelog tanpa Save membuang perubahan

8. Klik header Actions (⋯) > `Setup Column...`
9. Hilangkan centang kolom `Old Value` lalu klik icon close (✕)
10. Verifikasi tabel memakai konfigurasi tersimpan terakhir: kolom `Old Value` masih tampil
11. Klik header Actions (⋯) > `Setup Column...`
12. Ubah urutan kolom dengan menggeser `Modified By` ke posisi pertama lalu tekan `Esc`
13. Verifikasi tabel memakai konfigurasi tersimpan terakhir: urutan kolom data tetap Date, Action, Category Name, Field, Old Value, New Value, Modified By
14. Klik icon Close (✕) pada modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Langkah penghubung (S-03): langkah 7 menutup popup tanpa Save sebelum TC berikutnya, langkah 14 menutup modal.
- Spec ini tidak menyimpan konfigurasi kolom apa pun (tidak ada `[Save]`); hook `after` tetap menghapus preferensi kolom sebagai jaring pengaman.
- Temuan untuk QA:
  - TC-FA-CAT-411 tidak menyebut kolom mana yang tersisa dan tidak menyebut pembukaan Setup Column; spec menyisakan `Modified By` dan membuka Setup Column lewat header Actions (⋯).
  - TC-FA-CAT-546 langkah 4 ("ubah urutan kolom") tidak menyebut kolom yang digeser; spec menggeser `Modified By` ke posisi pertama.
