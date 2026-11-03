---
id: TC-AC-ACHA-E2E-045-download-volume-di-atas-5000-baris
title: "Download di Atas 5.000 Baris pada List Device Allocation"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHA-365
coverage:
  web: automated
---

# Download di Atas 5.000 Baris pada List Device Allocation

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #21) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (entitas PT ABC), password `Spectra.env.AC_TC_PASSWORD` (nama env tercantum di daftar env var `suite.md`, didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor (lihat `suite.md`).
- Data Pre-setup (kelas e, volume data khusus): Seed API 5.100 baris alokasi Completed pada scope Total Control Principal (Pre-setup #62). Seed dibuat lewat fixture API yang disediakan tim FE/BE di hook `before` spec ini dan dipulihkan ke Seed List 30 baris (Pre-setup #48) di hook `after` (disediakan tim FE/BE; mekanisme seeding tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis dengan endpoint karangan). Dataset scope aktor yang diunduh adalah dataset Pre-setup #62 (lihat Temuan untuk QA tentang Seed List 30 baris).
- Kemampuan teknis (disediakan tim FE): browser mengunduh berkas ke folder uji yang dikosongkan sebelum unduhan; membuka berkas CSV untuk menghitung baris; membaca jumlah notifikasi in-app milik akun aktor.
- Jendela absence notifikasi in-app (pilihan spec sesuai TC-AC-ACHA-408 b dan 412, bukan nilai PRD): "Tunggu 5 detik tanpa memuat ulang halaman" ditulis sebelum asersi absence notifikasi, sesudah anchor positif `Verifikasi` berkas langsung terunduh.
- State global yang diubah: dataset Device Allocation (5.100 baris) dipulihkan lewat fixture di hook `after`; spec ini tidak berjalan paralel dengan spec lain.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACHA-365: Download di atas 5.000 baris memakai loading screen tanpa job background

1. Catat jumlah notifikasi in-app milik akun aktor sebagai baseline
2. Klik ikon Download
3. Klik `Download as CSV`
4. Verifikasi loading screen tampil sampai berkas siap
5. Verifikasi berkas langsung terunduh
6. Tunggu 5 detik tanpa memuat ulang halaman
7. Verifikasi tidak ada notifikasi in-app baru (jumlah notifikasi sama dengan baseline)
8. Buka berkas CSV
9. Verifikasi berkas memuat seluruh 5.100 baris

## Notes

- Sumber TC: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (bagian 4a-7). Seluruh TC primer spec ini (TC-AC-ACHA-365) dikerjakan di sini. Spec ini kelas e (volume data khusus, 5.100 baris di atas ambang 5.000).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): pencatatan baseline notifikasi in-app, langkah `Tunggu 5 detik tanpa memuat ulang halaman` (jendela absence, lihat Prerequisites), dan pembukaan berkas unduhan. Asersi absence notifikasi in-app ditaruh sesudah anchor positif `Verifikasi` berkas terunduh dan jendela tunggu 5 detik tanpa memuat ulang halaman (bagian 8b butir 11 dan bagian 6 konvensi); klik pilihan format adalah pemicu, dan berkas terunduh membuktikan respons sudah diproses.
- Temuan untuk QA:
  - TC-AC-ACHA-365 Expected a ("memuat seluruh 5.100 baris") bertentangan dengan Pre-setup #48: Seed List 30 baris ada di environment yang sama pada scope Total Control Principal sehingga berkas dapat memuat 5.130 baris. Spec mengikuti TC (5.100 baris) dan menyerahkan penyetelan dataset ke fixture "disediakan tim FE/BE".
  - TC-AC-ACHA-365 Expected b ("Tidak ada job background") tidak punya cara observasi dari UI; spec hanya mengasersi tidak ada notifikasi in-app baru dan tidak mengasersi job background.
  - TC-AC-ACHA-365 tidak menyebut apakah loading screen berupa overlay penuh atau indikator pada tombol; spec menulis "loading screen tampil" mengikuti Expected.
