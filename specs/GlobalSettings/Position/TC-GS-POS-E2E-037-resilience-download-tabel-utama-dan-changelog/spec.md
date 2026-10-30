---
id: TC-GS-POS-E2E-037-resilience-download-tabel-utama-dan-changelog
title: "Resilience Download: Toast Error saat Unduh Tabel Utama dan Popup Changelog Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-199
  - TC-GS-POS-240
coverage:
  web: automated
---

# Resilience Download: Toast Error saat Unduh Tabel Utama dan Popup Changelog Gagal

## Prerequisites

- Mode: mock. Seluruh API di-mock (dijalankan tim FE sebagai integration test, tanpa backend nyata). Respons yang dipaksa:
  - Daftar Position (`POST /v2/iam/positions/list`, LLD:9, openapi:11): memuat Position Pre-setup 10 sampai 16 (`IT Manager`, `Finance Analyst`, `Warehouse Supervisor`, `Customer Success Manager`, `Procurement Officer`, `Field Technician`, `Sales Coordinator`, tanpa suffix) dan Position Data Dinamis No. 1 sampai 13 bersuffix `{runId}-037` (`HR Business Partner`, `IT Support Specialist`, `Temporary Staff`, `iOS Developer`, `Legal Counsel`, `Marketing Executive`, `Quality Assurance Analyst`, `Data Engineer`, `Office Administrator`, `Logistics Coordinator`, `Payroll Specialist`, `Security Officer`, `Training Coordinator`).
  - Daftar entri Changelog Position (endpoint list Changelog tidak ada di openapi/LLD, disediakan tim FE): memuat entri Create `IT Support Specialist {runId}-037`, Edit `IT Support Specialist {runId}-037` menjadi `IT Operations Lead {runId}-037`, dan Delete `Temporary Staff {runId}-037` oleh `Budi Santoso`, serta entri Create `Procurement Analyst {runId}-037` oleh `Sari Dewi`.
  - Request export tabel utama (opsi CSV; `POST /v2/iam/positions/export`, LLD:48, openapi:76): respons 500 (langkah 1).
  - Request export Changelog (opsi CSV; endpoint export Changelog tidak ada di openapi/LLD, disediakan tim FE): respons 500 (langkah 11).
  - SSE `position.created`, `position.updated`, dan `position.deleted` (LLD:182, :337, :260): halaman berlangganan; stream disediakan tim FE dan tidak ada event yang dikirim selama spec ini.
  - API pendukung di luar sumber modul (identitas pengguna, menu, payload sesi dan izin Total Control agar ikon Download dan ikon Changelog tampil) disediakan tim FE.
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1) sebagai identitas sesi; sesi disediakan harness mock, tanpa login nyata dan tanpa password.
- Data Dinamis (hanya sebagai isi respons mock, tidak ada data yang dibuat di backend): nama bersuffix di atas; data list tabel utama dan entri Changelog dipakai sebagai precondition TC (c, d), tidak diasersi langkah. Fixture baru `Fixture.position.resilienceDownload037`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): lepas semua intercept dan mock yang dipasang spec ini; tutup Popup Changelog bila masih terbuka.
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 500 pada request export; memantau event unduhan browser (untuk memastikan tidak ada berkas terunduh); membaca ketahanan toast (toast error tidak hilang otomatis; toast sukses hilang otomatis setelah 4 detik, `foundation/functions/toast-copy.md`) dan men-dismiss toast.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`; pada mode mock flag ini termasuk API pendukung yang disediakan tim FE.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi.

## Test Steps

### TC-GS-POS-199: Download tabel utama gagal menampilkan toast error

1. Pasang intercept pada request export tabel utama: respons 500
2. Klik ikon Download
3. Pilih opsi `Download as CSV`
4. Verifikasi toast error "Error, failed to download Position." tampil
5. Verifikasi toast error tetap tampil setelah jeda melebihi 4 detik (durasi hilang otomatis toast sukses), tidak hilang otomatis
6. Verifikasi tidak ada berkas terunduh
7. Dismiss toast error
8. Lepas intercept pada request export tabel utama

### TC-GS-POS-240: Download Popup Changelog gagal

9. Klik ikon Changelog
10. Verifikasi User > Position > Popup Changelog: Position terbuka
11. Pasang intercept pada request export Changelog: respons 500
12. Klik ikon Download pada toolbar Popup Changelog
13. Pilih opsi `Download as CSV`
14. Verifikasi toast error "Error, failed to download Changelog-Position." tampil
15. Verifikasi toast error tetap tampil setelah jeda melebihi 4 detik (durasi hilang otomatis toast sukses), tidak hilang otomatis
16. Dismiss toast error
17. Lepas intercept pada request export Changelog
18. Klik `✕` di header untuk menutup Popup Changelog

## Notes

- Mode: mock. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Asersi yang menyangkut state backend nyata tidak teruji pada mode mock: spec ini hanya mengasersi tampilan toast dan tidak adanya berkas terunduh dari respons mock. Post Condition kedua TC kosong ("-").
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 dan 16 (dismiss toast), langkah 8 dan 17 (melepas intercept), langkah 18 (menutup Popup Changelog; tidak ada form dirty sehingga tidak ada dialog).
- Verifikasi langkah 6 (tidak ada berkas terunduh) berasal dari Expected b TC-GS-POS-199; TC-GS-POS-240 tidak punya Expected serupa sehingga tidak diasersi.
- Temuan untuk QA:
  - TC-GS-POS-199 dan 240 menyebut "opsi CSV"; label persis opsi memakai keputusan NC-17, yaitu `Download as CSV`.
  - TC-GS-POS-199 dan 240 tidak menyebut path endpoint export; export tabel utama memakai endpoint dari LLD/openapi, sedangkan endpoint list dan export Changelog tidak tercantum di openapi/LLD sehingga disediakan tim FE.
  - Nama berkas pada toast "Error, failed to download Changelog-Position." mengikuti TC; PRD §6 T-01 hanya mendefinisikan toast "Error, failed to download Position." untuk tabel utama.
