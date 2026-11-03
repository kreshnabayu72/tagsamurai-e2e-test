---
id: TC-AC-CS-E2E-137-multi-konteks-dua-admin-sesi-bersamaan-principal
title: "Multi-konteks: Dua Admin Sesi Bersamaan Principal"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-CS-483
  - TC-AC-CS-515
coverage:
  web: automated
---

# Multi-konteks: Dua Admin Sesi Bersamaan Principal

## Prerequisites

- Mode: FE+BE.
- Kelas harness c (multi-konteks). Sesi A: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Sesi B (konteks browser kedua, objek asersi TC-AC-CS-515): Total Control Principal kedua `Fixture.license-allocation-subscription.principalSessionB`, password `Spectra.env.AC_SUB_TC_B_PASSWORD`. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Sesi API aktor (TC-AC-CS-483) memakai akun Principal kedua yang sama; token API tidak dihitung sebagai sesi web (bagian 5).
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-137`):
  1. TC-AC-CS-483: term Active (setara `SUBS-20260101-00001`, Pre-setup #61) dengan Client `Client Sesi Bersamaan+{runId}-137` dan Product milik spec; Subscription ID-nya dibaca lewat API seeding dan dipakai sebagai `T483` pada Test Steps.
  2. TC-AC-CS-515: Client `Client Trial Satu+{runId}-137` dan `Client Trial Dua+{runId}-137` (setara `Client Tanpa Subscription`, Pre-setup #48: binaan langsung PT Maju Bersama pada group `Jawa`, belum punya term maupun trial), Product `FAMS`.
- Nilai kuota Activate Trial (Trial Duration, Asset Quota, Concurrent User Quota) yang sama pada kedua sesi dirujuk lewat `Fixture.license-allocation-subscription.trialQuota515` (TC tidak menyebut nilainya; lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE/BE): konteks browser kedua yang menekan `[Submit]` bersamaan dengan sesi A (sinkronisasi klik oleh runner); sesi API aktor Principal kedua; membaca jumlah trial per Client; endpoint tulis tidak tertulis di TC, PRD, atau LLD (S-13). Konteks sesi B ditutup dan sesi login browser terkait dihapus di akhir TC-AC-CS-515 (S-09).
- Jendela pengamatan propagasi SSE antar-sesi (langkah 5) adalah 5 detik, pilihan spec (bukan nilai TC atau PRD).
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen` untuk akun UI suite termasuk sesi B. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-483: List disegarkan diam-diam saat status berubah dari sesi lain

1. Ketik Search `T483`, tekan Enter
2. Verifikasi baris `T483` berstatus Active tampil di tab `Current`
3. Picu lewat sesi API aktor Principal kedua: Cancel Subscription `T483` hingga perubahan tersimpan
4. Verifikasi tidak ada toast pada sesi A
5. Tunggu 5 detik tanpa memuat ulang halaman
6. Verifikasi baris `T483` hilang dari tab `Current` pada sesi A tanpa muat ulang (empty state `No results found`)
7. Klik tab `History`
8. Ganti isi kotak search dengan `T483`, tekan Enter
9. Verifikasi baris `T483` muncul di tab `History` dengan status Archive
10. Klik `(←)` pada kotak Search, klik tab `Current`

### TC-AC-CS-515: Dua admin mengaktifkan trial untuk Client dan Product yang sama bersamaan

11. Buka sesi B (konteks browser kedua) dan login sebagai Total Control Principal kedua, buka Allocation > Client Subscription tab Current
12. Sesi A klik `[+ Activate Trial]`; sesi B klik `[+ Activate Trial]`
13. Sesi A pilih Client `Client Trial Satu+{runId}-137`, Product `FAMS`, Plan `Growth`; sesi B pilih Client `Client Trial Satu+{runId}-137`, Product `FAMS`, Plan `Professional`
14. Isi kuota yang sama pada kedua sesi (`Fixture.license-allocation-subscription.trialQuota515`)
15. Klik `[Submit]` pada kedua sesi hampir bersamaan
16. Verifikasi hanya satu trial aktif per Client `Client Trial Satu+{runId}-137` dan Product `FAMS` yang terbentuk
17. Verifikasi sesi yang kalah mendapat pesan "This client already has an active trial. Wait until it expires or it converts."
18. Pada sesi yang kalah (form masih terbuka) klik `✕`
19. Verifikasi dialog `Unsaved Changes` tampil pada sesi yang kalah
20. Klik `[Leave]` pada sesi yang kalah
21. Sesi A klik `[+ Activate Trial]`; sesi B klik `[+ Activate Trial]`
22. Pada kedua sesi pilih Client `Client Trial Dua+{runId}-137`, Product `FAMS`, Plan `Growth`
23. Isi kuota yang sama pada kedua sesi (`Fixture.license-allocation-subscription.trialQuota515`)
24. Klik `[Submit]` pada kedua sesi hampir bersamaan
25. Verifikasi pesan "Trial already used for Growth" tampil lebih dulu pada sesi yang kalah
26. Tutup konteks sesi B dan hapus sesi login browser terkait

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-CS-516, 517, dan 577 (race Add mode New, Cancel dan Renew, serta Convert ganda) ada di spec 162.
- Kelas c: sesi UI kedua adalah objek asersi pada TC-AC-CS-515 (bukan pemicu), sehingga `P-2` tidak dipakai; pada TC-AC-CS-483 pelaku kedua memakai sesi API, bukan konteks kedua.
- Langkah penghubung (S-03): langkah 1 dan 8 (Search untuk menemukan baris target, R-16), langkah 7 dan 10 (pindah tab dan mengosongkan Search), langkah 11 (membuka konteks kedua), langkah 18 sampai 20 (menutup form dirty pada sesi yang kalah; form sesi pemenang sudah tertutup, S-08) dan langkah 26 (menutup konteks kedua, S-09).
- Langkah 4 (absence toast) diletakkan segera setelah pemicu dan sebelum asersi artefak (bagian 8b butir 11); langkah 6 menjadi anchor positif bahwa respons sudah diproses.
- Asersi pemenang dan pecundang pada langkah 16, 17, 25 tidak bergantung pada sesi mana yang menang: sesi yang kalah ditentukan saat run.
- Temuan untuk QA:
  - TC-AC-CS-483 dan 515 ditandai `Manual Only — (d) dua sesi paralel` di kolom Automation; spec mengotomasikannya dengan sinkronisasi klik oleh runner (kemampuan disediakan tim FE/BE).
  - TC-AC-CS-515 menyebut "Dua sesi Principal" tetapi Pre-setup hanya punya satu akun Total Control Principal (#1) dan batas satu sesi web per akun; spec memakai akun Principal kedua yang disediakan tim FE (S-11).
  - TC-AC-CS-515 langkah 1 ("isi kuota yang sama") tidak menyebut nilai kuota; dirujuk lewat fixture.
  - TC-AC-CS-515 Expected c ("Bila Plan sama ... lebih dulu") tidak punya langkah sendiri karena langkah TC memakai Plan berbeda; spec menambah ronde kedua pada Client `Client Trial Dua+{runId}-137` dengan Plan yang sama (langkah 21 sampai 25) tanpa kolom Pre-setup, dan nilai Client `Client Trial Dua+{runId}-137` disediakan tim FE.
  - TC-AC-CS-483 Expected a ("tanpa toast") tidak menyebut jendela pengamatan; spec memakai jendela 5 detik (bagian 6, jendela SSE) sebagai pilihan spec.
