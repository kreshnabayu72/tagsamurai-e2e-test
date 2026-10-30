---
id: TC-GS-POS-E2E-034-resilience-baca-loading-error-dan-try-again
title: "Resilience Baca Tabel Position: Loading State dan Error Load dengan Try Again"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-6
  - TC-GS-POS-8
coverage:
  web: automated
---

# Resilience Baca Tabel Position: Loading State dan Error Load dengan Try Again

## Prerequisites

- Mode: mock. Seluruh API di-mock (dijalankan tim FE sebagai integration test, tanpa backend nyata). Tidak ada data yang di-seed atau dibuat di backend.
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1) sebagai identitas sesi; sesi disediakan harness mock, tanpa login nyata dan tanpa password.
- Kebutuhan mock (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit. Endpoint yang dipanggil halaman pada kondisi tes:
  - `POST /v2/iam/positions/list` (low-level-design.md:9, openapi.yaml:11, `operationId: post_positions_list`): list Position tabel utama, dipakai langkah 1 sampai 16.
  - Stream SSE event `position.created`, `position.updated`, dan `position.deleted` (low-level-design.md:182, :337, :260; PRD position.md bagian Sync + Realtime): halaman berlangganan stream ini; disediakan tim FE, tanpa asersi dan tanpa event yang dikirim spec ini.
  - API pendukung di luar sumber modul (identitas pengguna, menu, flag Guided Tooltip): disediakan tim FE, tanpa asersi.
  - Respons list Position, tahan 3 detik lalu jawab normal dengan 3 baris `IT Manager`, `Finance Analyst`, dan `Warehouse Supervisor` (fixture baru `Fixture.position.mockList034`; langkah 1 sampai 8, TC-GS-POS-6).
  - Respons list Position, jawab 500 (langkah 9 sampai 13, TC-GS-POS-8). Intercept 500 yang sama dilepas dan diganti respons normal 3 baris di langkah 14 sebelum `[Try Again]` (tidak dibutuhkan intercept "500 sekali" terpisah).
  - Payload sesi dan izin Total Control (capability "Manage user and role" penuh) disediakan tim FE sebagai API pendukung supaya tab Position tampil.
  - Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true (lihat `suite.md`); pada mode mock nilai flag itu bagian dari API pendukung yang disediakan tim FE, supaya tab Position tampil tanpa walkthrough yang menutupi layar.
- Pemulihan di hook `after`: semua intercept dilepas walau spec gagal di tengah. Spec tidak mengubah data backend.
- Suite berjalan serial (`parallel: false`).
- Layar awal: tidak dibuka di hook `beforeEach`; pembukaan Global Settings > User > Position adalah aksi yang diuji (loading state dan error load), sehingga ditulis di `## Test Steps`.

## Test Steps

### TC-GS-POS-6: Loading state saat data tabel Position sedang dimuat

1. Pasang intercept pada respons list Position: tahan 3 detik lalu jawab normal (3 baris)
2. Buka Global Settings > User dari sidebar Global Settings
3. Klik sub-tab Position
4. Verifikasi area tabel menampilkan skeleton loader / Loading component
5. Verifikasi area tabel tidak menampilkan empty state
6. Verifikasi area tabel tidak menampilkan error state
7. Tunggu respons diterima
8. Lepas intercept respons list Position

### TC-GS-POS-8: Error load tabel Position dan pemulihan via Try Again

9. Pasang intercept pada respons list Position: jawab 500
10. Muat ulang halaman Global Settings > User > Position (F5)
11. Verifikasi area tabel menampilkan "Unable to load this data."
12. Verifikasi area tabel menampilkan tombol `[Try Again]`
13. Verifikasi area tabel tidak menampilkan empty state
14. Lepas intercept 500 dan pasang respons list Position normal (3 baris)
15. Klik `[Try Again]`
16. Verifikasi tabel memuat ulang dan menampilkan baris `IT Manager`, `Finance Analyst`, dan `Warehouse Supervisor`

## Notes

- Mode: mock (seluruh API di-mock, konvensi bagian 6). Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Asersi yang menyangkut state backend nyata tidak teruji pada mode mock: spec ini hanya menguji rendering FE terhadap respons list yang dipaksa; baris yang tampil pada langkah 16 berasal dari respons mock, bukan dari data backend.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 (menunggu respons), langkah 8 (melepas intercept TC-GS-POS-6), langkah 10 (muat ulang agar list Position diminta ulang pada saat intercept 500 aktif; tidak ada form terbuka sehingga tidak ada dialog `beforeunload`), dan langkah 14 (mengganti respons 500 dengan respons normal sebelum `[Try Again]`).
- Loading state pada langkah 4 sampai 6 diasersi sebelum respons diterima (langkah 7), sebelum langkah yang mengubah state-nya.
- Tombol `[Try Again]` pada langkah 15 memuat ulang list Position dari respons normal yang dipasang di langkah 14 (Expected b TC-GS-POS-8).
- Pembagian TC lintas spec: kegagalan tulis (TC-GS-POS-67, 68, 106 sampai 108) ada di spec 035; kegagalan hapus (TC-GS-POS-121, 149) di spec 036; kegagalan download (TC-GS-POS-199, 240) di spec 037.
- Temuan untuk QA:
  - Precondition TC-GS-POS-6 menyebut throttle jaringan via DevTools; pada mode mock spec menahan respons list 3 detik lewat intercept sebagai pengganti throttle DevTools, tanpa mengubah Expected.
  - TC-GS-POS-8 langkah 1 ("Buka Global Settings > User > Position") tidak menyebut cara memicu pemuatan ulang list ketika halaman Position sudah terbuka dari TC-GS-POS-6; spec memuat ulang dengan F5.
  - Apakah halaman Position berlangganan stream SSE pada mode mock disimpulkan dari LLD dan PRD (Sync + Realtime), tidak dikonfirmasi dari aplikasi; spec menyatakan stream itu sebagai kebutuhan yang disediakan tim FE.
  - TC-GS-POS-6 dan 8 tidak menyebut jumlah dan nama baris pada respons normal; spec memakai 3 baris mock (`IT Manager`, `Finance Analyst`, `Warehouse Supervisor`).
