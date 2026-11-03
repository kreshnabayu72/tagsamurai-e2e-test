---
id: TC-FA-CAT-E2E-122-modal-changelog-penutupan-modal-tooltip-toolbar-dan-isolasi-state-search
title: "Modal Changelog: Penutupan Lewat Backdrop dan Esc, Tooltip Toolbar, dan Isolasi State Search ke Tabel Utama"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-414
  - TC-FA-CAT-416
  - TC-FA-CAT-417
coverage:
  web: automated
---

# Modal Changelog: Penutupan Lewat Backdrop dan Esc, Tooltip Toolbar, dan Isolasi State Search ke Tabel Utama

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 (pohon kategori CatMain) dan #23 (12 baris riwayat Changelog CatMain sesuai Example Data PRD §4.1: Create `Electronics`, Create `Electronics › Laptop`, Create `Vehicle`, Edit rename `Laptop` ke `Notebook` dan Code `LAP-01` ke `NBK-01`, Edit Description `Furniture`, Delete `Kunci Locker`, Delete `Peripheral` dan `Accessory` satu batch, Marked/Restored as Excess, Marked as Excess `Heavy Equipment` oleh System). Seed client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).

## Test Steps

### TC-FA-CAT-414: Modal Changelog ditutup lewat icon Close dan Esc, backdrop diabaikan

1. Klik icon Changelog di Table Tools
2. Klik backdrop
3. Verifikasi klik backdrop tidak menutup modal
4. Tekan `Esc`
5. Verifikasi `Esc` menutup modal tanpa dialog

### TC-FA-CAT-416: Tooltip toolbar Modal Changelog

6. Klik icon Changelog di Table Tools
7. Hover icon Search pada toolbar modal
8. Verifikasi tooltip `Search`
9. Hover icon Filter pada toolbar modal
10. Verifikasi tooltip `Filter`
11. Hover icon Download pada toolbar modal
12. Verifikasi tooltip `Download`

### TC-FA-CAT-417: State Search Changelog tidak bocor ke tabel utama

13. Klik icon Search di toolbar modal, ketik `Electronics`, lalu tekan `Enter`
14. Klik icon Close (✕) pada modal Changelog
15. Verifikasi tabel utama tidak terpengaruh Search modal dan tetap memuat seluruh baris kategori

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Langkah penghubung (S-03): tidak ada langkah penghubung tersendiri; penutupan modal pada TC-FA-CAT-417 adalah aksi TC itu sendiri.
- Tooltip toolbar modal dibandingkan dengan toolbar utama (judul TC-FA-CAT-416) hanya pada teks tooltip yang disebut Expected.
- Temuan untuk QA:
  - TC-FA-CAT-414 butir Expected "Esc menutup tanpa dialog" tidak menyebut dialog apa yang dimaksud; spec mengasersi bahwa tidak ada dialog konfirmasi apa pun yang tampil.
  - TC-FA-CAT-417 menyebut "perhatikan tabel utama" dan "seluruh baris kategori" tanpa jumlah; spec mengasersi bahwa baris kategori tidak tersaring oleh keyword `Electronics`.
