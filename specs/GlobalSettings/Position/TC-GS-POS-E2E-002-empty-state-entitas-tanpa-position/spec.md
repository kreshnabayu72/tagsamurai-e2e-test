---
id: TC-GS-POS-E2E-002-empty-state-entitas-tanpa-position
title: "Empty State Entitas Tanpa Position dan Entitas Diprovisioning Tanpa Default User Position"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-7
  - TC-GS-POS-296
coverage:
  web: automated
---

# Empty State Entitas Tanpa Position dan Entitas Diprovisioning Tanpa Default User Position

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor:
  - Total Control Client Kosong (Pre-setup 18) untuk TC-GS-POS-7. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTEMPTY_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Email akun ini tidak tertulis di tabel Pre-setup TC (lihat Temuan untuk QA). Password tidak ditulis di spec atau fixture.
  - Total Control entitas `Client Tanpa Seed` untuk TC-GS-POS-296: login lewat langkah ganti akun eksplisit. Akun dan env var-nya tidak ditetapkan di TC (lihat Temuan untuk QA); env var baru `GS_CLIENTNOSEED_TC_PASSWORD` (tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`).
  - Hook `after` mengembalikan sesi ke akun Total Control default suite (`superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`).
- Layar awal: hook `beforeEach` suite membuka Global Settings > User > Position untuk akun yang sedang aktif; spec ini tidak menguji navigasi sidebar sehingga langkah buka hanya ditulis sesudah ganti akun.
- Data Pre-setup: entitas `Client Kosong` (Pre-setup 18) dengan 0 record Position dan tanpa Changelog; entitas baca-saja menurut TC, tidak diubah spec ini, dan tidak ada spec dalam suite ini yang menulis ke entitas tersebut.
- Data Dinamis: entitas `Client Tanpa Seed` dibuat dari Admin Console dengan field Position Default User dikosongkan, beserta satu akun Total Control entitas itu. Pembuatan entitas dan akun di hook `before` serta penghapusan atau penonaktifannya di hook `after` memakai mekanisme yang disediakan tim FE/BE (mekanisme tidak didefinisikan di TC, PRD, atau LLD). Nama entitas bersuffix `Client Tanpa Seed {runId}-002`. Fixture baru `Fixture.position.clientNoSeed002`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true, lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus atau nonaktifkan entitas `Client Tanpa Seed {runId}-002` dan akunnya bila masih ada.
- Kemampuan teknis: ganti akun (logout lalu login); pembuatan entitas dari Admin Console lewat API/seeding oleh tim FE/BE.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`) dan sesi akun (dipulihkan hook `after` seperti di atas).

## Test Steps

### TC-GS-POS-7: Empty state tabel Position, entitas belum punya jabatan

1. Amati area tabel
2. Verifikasi area tabel menampilkan Illustration
3. Verifikasi area tabel menampilkan Title "No position yet"
4. Verifikasi area tabel menampilkan Description "Get started by creating your first position."
5. Verifikasi tidak ada tombol CTA di dalam empty state
6. Verifikasi `[+ Position]` tetap tampil di Table Tools

### TC-GS-POS-296: Entitas diprovisioning tanpa Position Default User memulai katalog kosong

7. Ganti akun: logout dari akun Total Control Client Kosong
8. Login sebagai Total Control entitas `Client Tanpa Seed {runId}-002`
9. Buka Global Settings > User > Position
10. Verifikasi tabel menampilkan empty state "No position yet"
11. Klik ikon Changelog
12. Verifikasi Changelog menampilkan "No changelog yet"
13. Tutup Popup Changelog dengan klik `✕` di header

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan: TC-GS-POS-7 pada akun Client Kosong, lalu ganti akun ke Client Tanpa Seed untuk TC-GS-POS-296.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 13 (menutup Popup Changelog) dan langkah ganti akun 7 sampai 8.
- Asersi empty state Changelog untuk `Client Kosong` ada di spec 038 (TC-GS-POS-204); spec ini hanya memverifikasi Changelog entitas `Client Tanpa Seed` (TC-GS-POS-296).
- Temuan untuk QA:
  - TC-GS-POS-296 berstatus Manual Only di TC tetapi tetap ditulis (konvensi bagian 2). TC tidak menyebut akun, email, atau env var untuk entitas `Client Tanpa Seed`, juga tidak menyebut mekanisme pembuatannya selain "dibuat dari Admin Console"; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE tanpa mengarang endpoint.
  - Email akun Total Control Client Kosong tidak tertulis di Pre-setup 18, dan env var `GS_CLIENTEMPTY_TC_PASSWORD` baru.
  - TC-GS-POS-7 Expected b menyebut "tidak ada tombol CTA di dalam empty state" tanpa menyebut bentuk elemen yang dicek; spec mengasersi tidak ada tombol di dalam area empty state.
