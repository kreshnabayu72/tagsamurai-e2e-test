---
id: TC-AC-ACAL-E2E-021-absence-event-platform-dan-download-tidak-tercatat
title: "Absence: Event Platform dan Download Tidak Tercatat"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACAL-48
  - TC-AC-ACAL-133
coverage:
  web: automated
---

# Absence: Event Platform dan Download Tidak Tercatat

## Prerequisites

- Mode: FE+BE.
- Kelas harness g (asersi absence, bagian 3 prinsip 13): semua TC di spec ini mengasersi "tidak ada baris atau entri log" untuk kondisi yang ditolak atau tidak dicatat. Tiap TC punya baseline dan data sendiri.
- Suite serial (`parallel: false`); hook suite dinyatakan di suite.md.
- Guided Tooltip: hook suite before/after menyetel flag seen halaman Activity Log untuk akun Total Control Principal (lihat suite.md).
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Spec tidak berganti akun UI dan hook `after` tidak perlu memulihkan sesi (akun default suite).
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), dibuat lewat sesi API di hook `before`; password user dinamis `Spectra.env.AC_DYN_PASSWORD`:
  - User `John Doe {runId}-021` (First Name `John`, Last Name `Doe {runId}-021`; singkatan `John D`), staf Principal, belum punya entri Session sebelum langkah 1 (baseline nol, nama bersuffix unik). Mekanisme reset password dan change password via sesi API untuk user ini disediakan tim FE/BE (TC menyebutnya sebagai event platform).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API user dinamis di atas bila masih ada. Entri log tidak dapat dihapus; nama bersuffix run.
- Kemampuan teknis (disediakan tim FE/BE):
  - Sesi API aktor untuk user dinamis (login platform, buka Global Settings, buka dan tutup Admin Console, logout, reset password, change password).
  - Penangkapan berkas unduhan browser untuk langkah Download.
  - Baseline (S-12): jumlah total entri dibaca dari footer `Showing X–Y of Z entries` sebelum aksi pemicu dan dibandingkan sebagai selisih, bukan angka absolut.
- Jam server dan jam browser tidak diatur. Tidak ada state global yang diubah (semua data milik spec).

## Test Steps

### TC-AC-ACAL-48: Hanya event sesi AC yang tampil; event platform tidak pernah tampil

1. Pemicu API: `John Doe {runId}-021` login platform hingga tersimpan
2. Pemicu API: `John Doe {runId}-021` membuka Global Settings hingga tersimpan
3. Pemicu API: `John Doe {runId}-021` membuka Admin Console hingga baris `Session started` tersimpan
4. Pemicu API: `John Doe {runId}-021` menutup Admin Console hingga baris `Session ended` tersimpan
5. Pemicu API: `John Doe {runId}-021` logout hingga tersimpan
6. Pemicu API: reset password `John Doe {runId}-021` hingga password baru tersimpan
7. Pemicu API: `John Doe {runId}-021` login dengan password baru hingga tersimpan
8. Pemicu API: `John Doe {runId}-021` change password hingga tersimpan
9. Tunggu aksi selesai: seluruh aksi pemicu tersimpan
10. Klik icon Filter, pilih User `John Doe {runId}-021`, klik [Apply]
11. Verifikasi tabel hanya memuat dua baris milik `John D`: Note `Session started` dan Note `Session ended` untuk buka dan tutup Admin Console
12. Verifikasi tidak tampil baris Login, Logout, Reset Password, Change Password, maupun buka dan tutup Global Settings milik `John D`
13. Klik icon Filter, klik [Clear Field], lalu klik [Apply]

### TC-AC-ACAL-133: Download tidak menghasilkan entri log

14. Klik tab "User Action", lalu catat jumlah total entri dari footer `Showing X–Y of Z entries` (nilai Z) sebagai baseline D0
15. Klik icon Download, pilih `Download as CSV`
16. Verifikasi berkas `Activity-Log-User-Action.csv` terunduh
17. Klik tab "Session"
18. Klik icon Download, pilih `Download as CSV`
19. Verifikasi berkas `Activity-Log-Session.csv` terunduh
20. Muat ulang halaman (F5)
21. Klik tab "User Action"
22. Verifikasi Breadcrumb `Activity Log > User Action` tampil
23. Verifikasi jumlah total entri pada footer sama dengan baseline D0
24. Ketik Search `Download`, tekan Enter
25. Verifikasi hasil Search kosong: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`, tanpa entri terkait Download
26. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-48, 133).
- P-5 butir (a): spec absence boleh memuat pemicu kelas lain bila hanya membentuk kondisi yang diasersi tidak tercatat. Pemicu di sini: aksi platform lewat sesi API (TC-AC-ACAL-48). Tiap TC punya user atau baseline sendiri.
- TC-AC-ACAL-48 terbelah antara presence dan absence (S-05): presence "hanya `Session started`/`Session ended`" diasersi di langkah 11 dan absence di langkah 12, keduanya di spec ini (satu TC satu spec).
- Langkah penghubung (tanpa awalan `Verifikasi`): pemicu lewat sesi API (langkah 1 sampai 8), "Tunggu aksi selesai" (langkah 9; bagian 8b butir 8), memasang dan menutup Filter (langkah 10, 13), pindah tab (langkah 14, 17, 21), dan pencatatan baseline (langkah 14). Langkah 24 sampai 26 adalah Search pembanding dan pemulihannya.
- Asersi tambahan di luar Expected TC (S-03): langkah 22 (Breadcrumb sebagai anchor sesudah F5, bagian 8b butir 2 dan R-21). Asersi absence jumlah memakai baseline selisih pada surface agregat (bagian 8b butir 2).
- Asersi tambahan di luar Expected TC (S-03): nama berkas `Activity-Log-User-Action.csv` (langkah 16) dan `Activity-Log-Session.csv` (langkah 19) berasal dari TC-AC-ACAL-122 dan TC-AC-ACAL-123; Expected TC-AC-ACAL-133 hanya menyatakan Download tidak menghasilkan entri log.
- Label menu: TC menulis `Download > CSV|XLSX`, label UI adalah `Download as CSV|XLSX` (langkah 15, 18); spec memakai label UI.
- Pelaku platform pada TC-AC-ACAL-48 (langkah 1 sampai 8) memakai sesi API, bukan sesi UI kedua (bagian 3 prinsip 13, `[KEPUTUSAN 2026-10-30]`).
- Temuan untuk QA:
  - Sumber Tier 2 TC-AC-ACAL-48, `auth/_foundation/auth-foundation.md` (§9), tidak ditemukan di workspace; aturan "tidak ada event platform di Tab Session" tidak dapat dicek ke sumber. Spec mengikuti Expected TC.
  - TC-AC-ACAL-48 tidak menyebut urutan reset password dan change password (change password butuh login); spec memakai reset password, login dengan password baru, lalu change password. Mekanisme reset password via sesi API tidak disebut di TC, PRD, atau LLD: disediakan tim FE/BE.
  - TC-AC-ACAL-133 "Refresh Tab User Action" tidak menyebut cara refresh; spec memakai muat ulang halaman (F5) lalu membuka tab User Action.
  - TC-AC-ACAL-133 Search `Download` untuk "tidak ada entri terkait Download" mengandalkan nilai Object, Field, atau Description tidak memuat kata `Download`; QA konfirmasi.
  - Email Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD` (terdaftar di `.env.example` dan `spectra.config.ts`) serta `AC_DYN_PASSWORD` (nama usulan tim FE dan belum terdaftar di `.env.example` maupun `spectra.config.ts`).
