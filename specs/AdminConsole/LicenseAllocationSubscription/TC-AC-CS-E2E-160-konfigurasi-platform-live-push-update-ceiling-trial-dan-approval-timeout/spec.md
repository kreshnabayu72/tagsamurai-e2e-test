---
id: TC-AC-CS-E2E-160-konfigurasi-platform-live-push-update-ceiling-trial-dan-approval-timeout
title: "Konfigurasi Platform Live: Push Update Plan, Ceiling Trial, dan Approval Timeout"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-CS-484
  - TC-AC-CS-485
  - TC-AC-CS-487
coverage:
  web: automated
---

# Konfigurasi Platform Live: Push Update Plan, Ceiling Trial, dan Approval Timeout

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data milik spec untuk TC-AC-CS-484 (S-06, S-12; bersuffix `+{runId}-160`), lima term plan `Professional` versi 3 dengan Client masing-masing, dibuat lewat API di hook `before` (status Expired, Grace, dan Waiting for Approval lewat kemampuan fixture yang disediakan tim FE/BE) dan dibersihkan di hook `after`; Subscription ID dibangkitkan sistem dan dibaca saat seeding. Spec tidak menulis data term, hanya efek Push Update:

| Status term | Client seed | Subscription ID | Setara Pre-setup | Versi plan sesudah Push Update |
|---|---|---|---|---|
| Active | `Push Active+{runId}-160` | `[Subscription ID term Active seed]` | #61 | 4 |
| Expired | `Push Expired+{runId}-160` | `[Subscription ID term Expired seed]` | tidak bernomor di TC | 4 |
| Grace | `Push Grace+{runId}-160` | `[Subscription ID term Grace seed]` | tidak bernomor di TC | 4 |
| Waiting for Approval | `Push Waiting+{runId}-160` | `[Subscription ID term Waiting seed]` | #131 | 3 |
| Pending | `Push Pending+{runId}-160` | `[Subscription ID term Pending seed]` | #57 | 3 |

- Data untuk TC-AC-CS-485: Max Trial Duration `60 day(s)` (Pre-setup #25). Data untuk TC-AC-CS-487: Approval Timeout `3 day(s)` (Pre-setup #26) dan pengajuan Waiting for Approval milik spec bersuffix `+{runId}-160`, dibuat lewat API di hook `before` (S-06, S-12); waktu submitnya dibaca lewat API seeding sebagai T0 (bagian 8b butir 3).
- State global yang diubah (suite serial): versi plan `Professional` (versi 4 dan seluruh efek Push Update; plan adalah konfigurasi platform bersama sehingga tidak dapat dimiliki spec), Max Trial Duration (`60` menjadi `45` hari), Approval Timeout (`3` menjadi `2` hari), serta jam server dan jam browser. Semuanya dipulihkan oleh fixture backend yang disediakan tim FE/BE di hook `after` (versi plan `Professional`, Max Trial Duration, Approval Timeout) dan jam dipulihkan di langkah penghubung serta di hook `after` (S-06: hanya keadaan global); efeknya (Last Updated dan entri audit trail Plans & Features dan Lifecycle Settings) tercatat di spec ini.
- Kemampuan teknis (disediakan tim FE/BE): mengubah Max Trial Duration lewat fixture backend tanpa memuat ulang halaman List; mengatur jam server dan jam browser absolut (fixture waktu, tanggal acuan uji `19/08/26`); memicu dan membaca status job lewat kueri fixture status job (batas tunggu 2 menit); membaca tenggat pengajuan dan notifikasi in-app terkirim lewat fixture BE.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-484: Push Update Plans & Features hanya menulis ulang versi plan term Active, Expired, dan Grace

1. Jalankan Push Update plan `Professional` ke versi 4 di Plans & Features hingga selesai
2. Klik menu `Client Subscription` di sidebar
3. Untuk setiap baris tabel Prerequisites (langkah 4 sampai 7): ulangi langkah 4 sampai 7
4. Ketik Search Subscription ID baris tabel, tekan Enter
5. Klik baris, Subscription Detail terbuka
6. Verifikasi versi plan di Subscription Detail sama dengan kolom "Versi plan sesudah Push Update" tabel
7. Klik menu `Client Subscription` di sidebar

### TC-AC-CS-485: Ceiling Trial dibaca live setiap form Activate Trial dibuka

8. Ubah Max Trial Duration menjadi `45` hari lewat fixture backend hingga tersimpan, tanpa memuat ulang halaman List
9. Klik `[+ Activate Trial]`
10. Pilih Product `FAMS`
11. Isi Trial Duration `46`
12. Verifikasi helper Trial Duration menampilkan "Maximum 45 days"
13. Verifikasi pesan error "Trial duration cannot exceed 45 days"
14. Klik `✕` pada form
15. Verifikasi dialog `Unsaved Changes` tampil
16. Klik `[Leave]`

### TC-AC-CS-487: Perubahan Approval Timeout menghitung ulang SLA pengajuan yang menunggu

17. Atur jam server dan jam browser ke T0 + 2 hari 6 jam (T0 = waktu submit pengajuan seed)
18. Buka Lifecycle Settings > Approval Settings, ubah Approval Timeout dari `3` menjadi `2` day(s), klik `[Save]`, catat waktu Save
19. Tunggu aksi selesai
20. Jalankan satu siklus job dan tunggu selesai (kueri fixture status job, batas 2 menit)
21. Verifikasi tenggat pengajuan seed diberi tenggat minimum 24 jam sejak waktu Save
22. Verifikasi warning H-24 terkirim ke approver aktif dan requester
23. Pulihkan jam server dan jam browser
24. Klik menu `Client Subscription` di sidebar
25. Ketik Search Subscription ID pengajuan seed, tekan Enter
26. Verifikasi pengajuan seed masih berstatus Waiting for Approval (tidak dibatalkan seketika saat Save)
27. Klik `(←)` pada kotak Search

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 2 dan 7 (memuat ulang List), langkah 4 (Search untuk menemukan baris target, R-16), langkah 19 (menunggu Save selesai sebelum siklus job), langkah 23 (memulihkan jam sebelum aksi aktor berikutnya, S-09), langkah 24 (pindah halaman), dan langkah 27 (mengosongkan Search).
- Langkah 4 sampai 7 diulang untuk 5 baris tabel Prerequisites (bagian 8b butir 7); ekspansi seluruh spec sekitar 43 langkah. Alasan di atas ~35 langkah: ketiga TC berbagi satu topik (konfigurasi platform yang diubah dan dibaca live oleh modul ini) dan satu kebutuhan state global serial; blok TC-AC-CS-484 berulang per baris dengan parameter di tabel Prerequisites tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa.
- TC-AC-CS-487 memakai jam dan job sebagai pemicu kondisi yang diuji (SLA dihitung ulang), `P-2`: pemicu bukan objek uji adalah perubahan Approval Timeout; objek asersi adalah tenggat, notifikasi, dan status pengajuan.
- Temuan untuk QA:
  - TC-AC-CS-484 menyebut lima status tetapi hanya menyebut Subscription ID untuk Active (#61) dan Pending (#57), Waiting for Approval hanya #131; Expired dan Grace tidak bernomor, dirujuk lewat fixture yang disediakan tim FE.
  - TC-AC-CS-484 langkah 1 menyebut Push Update tanpa langkah UI; spec memakai langkah Push Update di Plans & Features tanpa merinci kontrol UI-nya. Kontrol Subscription Detail untuk "versi plan" juga tidak disebut; spec mengasersi versi plan di Subscription Detail.
  - TC-AC-CS-487 Expected a dan b tidak menyebut surface tempat tenggat dan warning H-24 teramati; spec memakai kemampuan baca fixture BE yang disediakan tim FE/BE (S-11) tanpa endpoint karangan.
  - TC-AC-CS-487 tidak menyebut Subscription ID pengajuan "2 hari 6 jam lalu"; spec memakai pengajuan seed milik spec.
  - TC-AC-CS-485 tidak menyebut cara mengubah Max Trial Duration "sesudah halaman List dibuka" (Lifecycle Settings); spec memakai fixture backend agar List tidak dimuat ulang.
