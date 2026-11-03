---
id: TC-AC-PF-E2E-176-setup-column-tab-assigned-clients-independensi-cache
title: "Setup Column Tab Assigned Clients: cache terpisah dari tabel Plans List"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-438
coverage:
  web: automated
---

# Setup Column Tab Assigned Clients: cache terpisah dari tabel Plans List

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip mengikuti pernyataan di `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE, sesuai `suite.md`): sesi API aktor, klien HTTP, dan fixture backend yang memulihkan Dataset Plan D ke keadaan awal secara idempoten; penghapusan preferensi kolom Tab Assigned Clients di browser (disediakan tim FE). Fixture `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis literal sesuai Pre-setup.
- Data Pre-setup: Dataset Plan D, default plan `Growth` v5 dengan 9 client: PT Sejahtera Abadi Active v5 17 Jun 26 John Doe; PT Wahana Nusantara Active v1 05 Jun 26 John Doe; PT Karya Abadi Active v1 03 Jun 26 Jane Smith; PT Cahaya Mandiri Grace v5 20 Jun 26 Jane Smith; PT Bumi Sentosa Active v1 11 Jun 26 Jane Smith; PT Timur Jaya Active v1 09 Jun 26 John Doe; PT Zona Nol Active v5 25 Jun 26 John Doe; PT Hak Parsial Satu Active v1 12 Jun 26 Jane Smith; PT Hak Parsial Dua Active v1 13 Jun 26 Jane Smith. Pengecualian S-06/S-12 butir A-14 (nama literal tanpa suffix; seeding idempoten dan pemulihan oleh fixture backend di hook `before` dan `after`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global dan pemulihan: spec menyimpan konfigurasi kolom Tab Assigned Clients (preferensi di browser); langkah 11 dan hook `after` menghapus preferensi itu. Last Updated dan Changelog plan tidak berubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### Independensi cache Setup Column (TC-AC-PF-438)

1. Buka Plan Detail `Growth` (klik nama plan `Growth` pada tab Default, sub-tab Active).
2. Klik Tab Assigned Clients.
3. Buka Popup Setup Column (klik header kolom Actions (`⋯`), lalu `Setup Column...`).
4. Uncheck kolom `Assigned By`.
5. Klik `[Save]`.
6. Kembali ke Plans & Licensing > Plans & Features > Default > Active.
7. Verifikasi tabel Plans List Default Active tetap menampilkan seluruh kolomnya.
8. Buka Plan Detail `Growth`.
9. Klik Tab Assigned Clients.
10. Verifikasi Tab Assigned Clients tetap menyembunyikan kolom `Assigned By`.
11. Pulihkan konfigurasi kolom: hapus preferensi Setup Column Tab Assigned Clients di browser (kemampuan disediakan tim FE).

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 6 (kembali ke Plans List untuk mengamati kolom), 8 dan 9 (membuka kembali Tab Assigned Clients), 11 (pemulihan konfigurasi kolom, bagian 4 konvensi).
- TC-AC-PF-435, 436, dan 437 (Setup Column Tab Assigned Clients lainnya) ada di spec 168.
- Temuan untuk QA:
  - Expected TC-AC-PF-438 menyebut tabel Plans List "tetap menampilkan seluruh kolomnya" tanpa menuliskan daftar kolom Plans List Default Active; asersi langkah 7 mengikuti kalimat itu dan perlu daftar kolom dari TC atau PRD agar dapat diverifikasi per kolom.
