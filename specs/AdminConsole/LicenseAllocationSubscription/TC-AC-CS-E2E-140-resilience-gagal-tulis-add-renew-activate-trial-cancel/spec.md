---
id: TC-AC-CS-E2E-140-resilience-gagal-tulis-add-renew-activate-trial-cancel
title: "Resilience: Gagal Tulis Add, Renew, Activate Trial, Cancel Subscription"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-172
  - TC-AC-CS-173
  - TC-AC-CS-209
  - TC-AC-CS-266
coverage:
  web: automated
---

# Resilience: Gagal Tulis Add, Renew, Activate Trial, Cancel Subscription

## Prerequisites

- Mode: FE+BE. Spec memaksa sebagian respons Submit lewat `Spectra.intercept()` di atas backend nyata (bagian 6); `Mode: mock` tidak dipakai karena modul ini tidak punya `openapi.yaml` maupun LLD sebagai sumber daftar endpoint (R-15, S-13).
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-140`): Client `Client Tanpa Subscription+{runId}-140` (setara `Client Tanpa Subscription`, Pre-setup #48: binaan langsung PT Maju Bersama, belum punya term maupun trial) untuk Add SAMS dengan Start Date `19/08/26`, Duration `1` (term yang terbentuk pada langkah 10 dibersihkan di hook `after`); term Active FAMS Professional Client `Warung Kopi Senja+{runId}-140` tanpa successor, Subscription ID `{idT173}` dibaca lewat API seeding (setara `SUBS-20250815-00001`, #69); Client `Klinik Aktivasi+{runId}-140` tanpa term maupun trial untuk Activate Trial FAMS `Growth` dengan Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10`; term Active FAMS Client `Apotek Sehat Sentosa+{runId}-140`, Subscription ID `{idT266}` dibaca lewat API seeding (setara `SUBS-20260101-00001`, #61).
- Kemampuan teknis (disediakan tim FE/BE): jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (fixture waktu), dipulihkan di hook `after`.
- Kebutuhan intercept (parsial, disediakan tim FE; endpoint hanya yang dinamai TC dan path-nya tidak tertulis di TC, PRD, atau LLD): respons Submit Add 500, Submit Renew 500, Submit Activate Trial 500, dan Cancel Subscription 500. Intercept dilepas segera setelah dipakai (S-09).
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-172: Submit Add gagal 5xx mempertahankan input

1. Klik `[+ Subscription]`
2. Pilih Client `Client Tanpa Subscription+{runId}-140`, Product `SAMS`, Plan `Growth`, isi Duration `1`, Start Date `19/08/26`
3. Paksa respons Submit Add gagal 500 lewat `Spectra.intercept()`
4. Klik `[Submit]`
5. Verifikasi toast error "Error, failed to add subscription."
6. Verifikasi modal tetap terbuka
7. Verifikasi input dipertahankan
8. Verifikasi `[Submit]` aktif kembali
9. Lepas intercept respons Submit Add
10. Klik `[Submit]`
11. Verifikasi toast sukses "Success, subscription has been added."

### TC-AC-CS-173: Submit Renew gagal 5xx mempertahankan input

12. Ketik Search `{idT173}`, tekan Enter
13. Klik ikon `⋯` pada term `{idT173}`, klik `Renew`
14. Isi Duration `1`
15. Paksa respons Submit Renew gagal 500 lewat `Spectra.intercept()`
16. Klik `[Submit]`
17. Verifikasi toast error "Error, failed to renew subscription."
18. Verifikasi modal tetap terbuka
19. Verifikasi Duration `1` dipertahankan
20. Lepas intercept respons Submit Renew
21. Klik `✕` pada modal
22. Verifikasi dialog `Unsaved Changes` tampil
23. Klik `[Leave]`

### TC-AC-CS-209: Aktivasi trial gagal 5xx mempertahankan input

24. Klik `[+ Activate Trial]`
25. Pilih Client `Klinik Aktivasi+{runId}-140`, Product `FAMS`, Plan `Growth`, isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10`
26. Paksa respons Submit Activate Trial gagal 500 lewat `Spectra.intercept()`
27. Klik `[Submit]`
28. Verifikasi toast error "Error, failed to activate trial."
29. Verifikasi modal tetap terbuka
30. Verifikasi input dipertahankan
31. Lepas intercept respons Submit Activate Trial
32. Klik `✕` pada modal
33. Verifikasi dialog `Unsaved Changes` tampil
34. Klik `[Leave]`

### TC-AC-CS-266: Cancel Subscription gagal 5xx mempertahankan dialog

35. Ganti isi kotak search dengan `{idT266}`, tekan Enter
36. Klik ikon `⋯` pada term `{idT266}`, klik `Cancel Subscription`
37. Paksa respons Cancel Subscription gagal 500 lewat `Spectra.intercept()`
38. Klik `[Cancel Subscription]`
39. Verifikasi toast error "Error, failed to cancel subscription."
40. Verifikasi dialog tetap terbuka untuk retry manual
41. Lepas intercept respons Cancel Subscription
42. Tutup dialog tanpa membatalkan term (klik `✕` pada dialog)
43. Verifikasi term `{idT266}` tetap Active

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-CS-521 dan 563 (retry setelah timeout, toast error bertahan) ada di spec 163.
- Langkah penghubung (S-03): langkah 12 dan 35 (Search untuk menemukan baris target, R-16), langkah 9, 20, 31, 41 (melepas intercept segera setelah dipakai, S-09), langkah 21 sampai 23 dan 32 sampai 34 (menutup form dirty, S-08), langkah 42 (menutup dialog Cancel Subscription).
- Spec ini melewati ~35 langkah (43). Alasan: semua blok satu kelas harness (fault injection 5xx pada Submit) dengan pola yang sama dan berdiri sendiri, masing-masing memakai data milik spec; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan pemecahan hanya menambah login dan hook.
- Langkah 10 pada TC-AC-CS-172 membuat satu term milik spec; term itu dibersihkan di hook `after`.
- Temuan untuk QA:
  - TC-AC-CS-172 Expected c dan TC-AC-CS-173 serta 209 tidak menyebut kondisi tombol `[Submit]` sesudah gagal pada TC-AC-CS-173/209; hanya TC-AC-CS-172 b memuat state tombol.
  - TC-AC-CS-266 Expected b ("dialog tetap terbuka untuk retry manual") tidak menyebut label tombol penutup dialog selain `[Cancel Subscription]`; spec memakai `✕` untuk menutup dialog (perlu konfirmasi QA).
  - TC-AC-CS-173 dan 266 memakai record Pre-setup (#69, #61) sebagai target aksi tulis yang gagal; spec memakai record milik spec (S-06).
