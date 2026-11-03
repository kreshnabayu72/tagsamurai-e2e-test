---
id: TC-AC-PF-E2E-163-filter-tab-assigned-clients-screening-subscription-status
title: "Filter Tab Assigned Clients: screening Filter Panel, Subscription Status, Assigned By, dan Plan Version"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-418
  - TC-AC-PF-419
  - TC-AC-PF-420
coverage:
  web: automated
---

# Filter Tab Assigned Clients: screening Filter Panel, Subscription Status, Assigned By, dan Plan Version

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip mengikuti pernyataan di `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE, sesuai `suite.md`): sesi API aktor, klien HTTP, dan fixture backend yang memulihkan Dataset Plan D ke keadaan awal secara idempoten. Fixture `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis literal sesuai Pre-setup.
- Data Pre-setup: Dataset Plan D, default plan `Growth` v5 dengan 9 client: PT Sejahtera Abadi Active v5 17 Jun 26 John Doe; PT Wahana Nusantara Active v1 05 Jun 26 John Doe; PT Karya Abadi Active v1 03 Jun 26 Jane Smith; PT Cahaya Mandiri Grace v5 20 Jun 26 Jane Smith; PT Bumi Sentosa Active v1 11 Jun 26 Jane Smith; PT Timur Jaya Active v1 09 Jun 26 John Doe; PT Zona Nol Active v5 25 Jun 26 John Doe; PT Hak Parsial Satu Active v1 12 Jun 26 Jane Smith; PT Hak Parsial Dua Active v1 13 Jun 26 Jane Smith. Pengecualian S-06/S-12 butir A-14 (nama literal tanpa suffix; seeding idempoten dan pemulihan oleh fixture backend di hook `before` dan `after`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global dan pemulihan: spec hanya membaca; Last Updated dan Changelog plan tidak berubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### Screening Filter Panel (TC-AC-PF-418)

1. Buka Plan Detail `Growth` (klik nama plan `Growth` pada tab Default, sub-tab Active).
2. Klik Tab Assigned Clients.
3. Verifikasi tabel menampilkan sedikitnya satu baris (footer `Showing 1–9 of 9 entries`).
4. Klik ikon Filter.
5. Verifikasi Filter Panel memuat field `Subscription Status` berupa multi-select searchable dengan placeholder `All statuses`.
6. Verifikasi Filter Panel memuat field `Plan Version` berupa multi-select searchable dengan placeholder `All versions`.
7. Verifikasi Filter Panel memuat field `Assigned Date` berupa date range picker dengan placeholder `Select date`.
8. Verifikasi Filter Panel memuat field `Assigned By` berupa multi-select searchable dengan placeholder `All users`.
9. Verifikasi Filter Panel tidak memuat field Client Name.
10. Tutup Filter Panel tanpa menerapkan filter.

### Filter Subscription Status dan Assigned By (TC-AC-PF-419)

11. Buka Filter Panel, pilih Subscription Status `Grace`, klik `[Apply]`.
12. Verifikasi tabel menampilkan hanya baris `PT Cahaya Mandiri`.
13. Buka Filter Panel, hapus filter Subscription Status `Grace`, pilih Assigned By `John Doe`, klik `[Apply]`.
14. Verifikasi tabel menampilkan empat baris: `PT Sejahtera Abadi`, `PT Timur Jaya`, `PT Wahana Nusantara`, `PT Zona Nol`.

### Filter Plan Version (TC-AC-PF-420)

15. Buka Filter Panel, hapus filter Assigned By `John Doe`, pilih Plan Version `Outdated`, klik `[Apply]`.
16. Verifikasi tabel menampilkan enam baris dengan versi di bawah terbaru: `PT Bumi Sentosa`, `PT Hak Parsial Dua`, `PT Hak Parsial Satu`, `PT Karya Abadi`, `PT Timur Jaya`, `PT Wahana Nusantara`.
17. Buka Filter Panel, ganti pilihan Plan Version ke `Up to Date`, klik `[Apply]`.
18. Verifikasi tabel menampilkan tiga baris: `PT Cahaya Mandiri`, `PT Sejahtera Abadi`, `PT Zona Nol`.
19. Buka Filter Panel, pilih Plan Version `Outdated` dan `Up to Date`, klik `[Apply]`.
20. Verifikasi tabel menampilkan sembilan baris (footer `Showing 1–9 of 9 entries`).
21. Buka Filter Panel, kosongkan seluruh filter, klik `[Apply]`.

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 10 (menutup Filter Panel tanpa Apply) dan 21 (mengosongkan filter di akhir spec).
- Langkah 3 menjadi pembanding positif bagi asersi tabel tersaring pada langkah 12, 14, 16, dan 18 (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-PF-419 dan TC-AC-PF-420 menulis "Hapus filter" tanpa menyebut kontrol yang dipakai; spec menghapus pilihan lewat Filter Panel sebelum `[Apply]`.
  - TC-AC-PF-420 Expected a menyebut "enam baris dengan versi < terbaru"; spec mengasersi enam nama baris yang tercantum.
