---
id: TC-GS-IMPORT-E2E-149-multi-konteks-penekanan-saran-ai-dismiss-dibagikan-ke-seluruh-admin
title: "Multi-konteks: penekanan saran AI (Dismiss) dibagikan ke seluruh admin pada draft yang sama (Client C)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-297
coverage:
  web: automated
---

# Multi-konteks: penekanan saran AI (Dismiss) dibagikan ke seluruh admin pada draft yang sama (Client C)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): draft Client C dibagikan ke seluruh admin dan mode mock AI adalah state global; lihat `suite.md`.
- Dua konteks browser dalam satu spec, ditandai `[Sesi A]` dan `[Sesi B]` (keduanya mengasersi hasil, jadi sesi UI kedua, bukan pemicu API):
  - Sesi A (aktor): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Login di hook `before`; layar awal Global Settings > Import dibuka hook `beforeEach`.
  - Sesi B (pengamat): Admin kedua Client C (Oki Setiawan) `totalControlSecond_automated_qaTeam3@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTC_TC2_PASSWORD`. Login di hook `before` pada konteks browser terpisah.
  - Password tidak ditulis di spec atau fixture.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk kedua akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE): dua konteks browser paralel; mock layanan AI mode normal D-40 (tabel D-41 dan D-42); skrip fixture reset Client C ke tanpa draft pada Sub-Tab Brand.
- Data Dinamis (milik spec ini; draft dibuang oleh reset sehingga nama baris berkas literal): D-44 `ai-brand-long.csv`, kolom `Brand Name`, 1 baris dengan Brand Name nilai sumber Brand D-41 (121 karakter); saran mock `Samsung Electronics Indonesia`.
- Pemulihan (hook `after`): hapus draft Brand Client C, tutup konteks Sesi B, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-297: Penekanan saran dibagikan ke seluruh admin

1. [Sesi A] Reset Client C ke tanpa draft pada Sub-Tab Brand (aksi fixture); pastikan mock AI mode normal
2. [Sesi A] Muat ulang halaman Import > Brand
3. [Sesi A] Klik `[Upload File]` di Dropzone dan pilih berkas `ai-brand-long.csv`
4. [Sesi A] Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
5. [Sesi A] Tunggu aksi selesai (Modal Column Mapping tertutup)
6. [Sesi B] Buka Global Settings > Import, pilih Sub-Tab Brand
7. [Sesi B] Verifikasi sel Brand Name baris #1 menampilkan badge "AI suggestion: 'Samsung Electronics Indonesia'?"
8. [Sesi A] Klik `[Dismiss]` pada badge saran sel Brand Name baris #1
9. [Sesi A] Tunggu aksi selesai (permintaan mendapat respons)
10. [Sesi B] Muat ulang halaman Import > Brand
11. [Sesi B] Verifikasi sel Brand Name baris #1 tidak menampilkan badge saran
12. [Sesi B] Verifikasi baris #1 tetap `error`
13. [Sesi B] Verifikasi Error Summary Callout memuat "Brand Name: Max. 120 characters"

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: multi-konteks (c); tidak ada pemicu kelas lain.
- Langkah penghubung (tanpa `Verifikasi`): reset (langkah 1), pembukaan halaman dan Sub-Tab (langkah 2, 6), memuat ulang (langkah 10), dan langkah 9 (menunggu `[Dismiss]` selesai sebelum Sesi B memuat ulang). Langkah 5 (Tunggu aksi selesai: menunggu aksi tanpa `Verifikasi` selesai sebelum Sesi B membuka halaman; penanda Modal Column Mapping tertutup).
- Langkah 12 dan 13 tidak punya anchor positif terpisah: baris #1 tetap `error` dan Callout memuat teks pelanggaran sudah menjadi anchor bagi asersi absence badge pada langkah 11 yang diurutkan sebelumnya; langkah 11 didahului pemuatan ulang halaman yang menampilkan Staging Table (elemen halaman tampil lewat langkah 12 dan 13). Untuk menjaga urutan state, langkah 11 tetap dibaca sebelum langkah 12.
- Temuan untuk QA:
  - TC-GS-IMPORT-297 Expected b mengasersi "tidak melihat badge" sesudah muat ulang di Sesi B tanpa menyebut anchor positif; spec menyusun asersi baris `error` dan Callout sebagai pelengkap pada surface yang sama.
  - Post Condition TC-GS-IMPORT-297 ("draft berisi 1 baris `error` tanpa saran AI untuk nilai sel tersebut") dikonfirmasi oleh Expected b; tidak ada langkah observasi tambahan.
  - Penanda selesai untuk langkah 9 (klik `[Dismiss]` Sesi A sebelum Sesi B memuat ulang) tidak disebut di TC, PRD, atau spec ini; langkah "Tunggu aksi selesai" memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati di surface Sesi A.
  - TC-GS-IMPORT-297 tidak menyebut apakah Sesi B harus berada pada halaman Import sebelum Sesi A mengunggah; spec membuka halaman Sesi B sesudah Confirm Mapping (urutan sesuai Langkah TC).
