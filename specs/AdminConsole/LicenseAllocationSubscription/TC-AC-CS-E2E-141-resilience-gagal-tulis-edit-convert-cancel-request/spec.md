---
id: TC-AC-CS-E2E-141-resilience-gagal-tulis-edit-convert-cancel-request
title: "Resilience: Gagal Tulis Edit, Convert, Cancel Request"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-235
  - TC-AC-CS-277
  - TC-AC-CS-257
  - TC-AC-CS-258
coverage:
  web: automated
---

# Resilience: Gagal Tulis Edit, Convert, Cancel Request

## Prerequisites

- Mode: FE+BE. Spec memaksa sebagian respons lewat `Spectra.intercept()` di atas backend nyata (bagian 6); `Mode: mock` tidak dipakai karena modul ini tidak punya `openapi.yaml` maupun LLD sebagai sumber daftar endpoint (R-15, S-13).
- Akun aktor pertama: Create-Only Distributor (Pre-setup #6) `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`), password `Spectra.env.AC_SUB_CREATE_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Akun ganti akun di tengah spec (Test Steps memuat langkah Logout dan login eksplisit): Group Manager Distributor scoped (Pre-setup #5) `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`), password `Spectra.env.AC_SUB_GM_PASSWORD`.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- State global: toggle Require Approval for Allocation PT Maju Bersama diatur ON oleh fixture backend yang disediakan tim FE/BE di hook `before` dan dipulihkan di hook `after` (S-06, pengecualian 2026-10-30). Suite berjalan serial.
- Data milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12; request yang diuji gagal sehingga tidak ada perubahan data; bersuffix `+{runId}-141`):
  1. TC-AC-CS-235: pengajuan Waiting for Approval Client `Apotek Sehat Sentosa+{runId}-141` FAMS Growth, Subscription ID `{idW235}` dibaca lewat API seeding, milik `Fajar Nugroho` (setara `SUBS-20260819-00001`, Pre-setup #49: Client Apotek Sehat Sentosa, FAMS, Growth, Plan Owner PT Maju Bersama).
  2. TC-AC-CS-277: pengajuan Waiting for Approval Client `Toko Pembatalan+{runId}-141` FAMS, Subscription ID `{idW277}` dibaca lewat API seeding, milik `Fajar Nugroho` (setara #49).
  3. TC-AC-CS-257: trial SAMS Growth Active Client `Klinik Harapan Bunda+{runId}-141`, Subscription ID `{idT257}` dibaca lewat API seeding (Start 10/08/26, End 08/09/26, Plan Owner CV Karya Mandiri, tanpa term paid SAMS; setara #71).
  4. TC-AC-CS-258: Client `Toko Konversi+{runId}-141` dengan term paid SAMS Growth Active (End Date 14/09/26, Plan Owner PT Maju Bersama) dan trial SAMS Professional Active (Plan Owner CV Karya Mandiri); setara #73.
- Kebutuhan intercept (parsial, disediakan tim FE; endpoint hanya yang dinamai TC dan path-nya tidak tertulis di TC, PRD, atau LLD): respons Save Edit 500, Cancel Request 500, Convert mode New 500, dan Convert mode Renewal 500. Intercept dilepas segera setelah dipakai (S-09).
- Kemampuan teknis (disediakan tim FE/BE): jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (fixture waktu, disediakan tim FE/BE), dipulihkan di hook `after` (status trial Active dan Start Date Convert hari ini bergantung pada tanggal acuan).
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-235: Edit gagal 5xx mempertahankan input

1. Ketik Search `{idW235}`, tekan Enter
2. Klik ikon `⋯` pada `{idW235}`, klik `Edit` (modal Edit Subscription terbuka ter-isi dari record)
3. Ubah Duration menjadi `2`
4. Paksa respons Save gagal 500 lewat `Spectra.intercept()`
5. Klik `[Save]`
6. Verifikasi toast error "Error, failed to update subscription."
7. Verifikasi modal tetap terbuka
8. Verifikasi Duration `2` dipertahankan
9. Verifikasi data lama `{idW235}` tidak berubah
10. Lepas intercept respons Save
11. Klik `✕` pada modal
12. Verifikasi dialog `Unsaved Changes` tampil
13. Klik `[Leave]`

### TC-AC-CS-277: Cancel Request gagal 5xx mempertahankan dialog

14. Ganti isi kotak search dengan `{idW277}`, tekan Enter
15. Klik ikon `⋯` pada `{idW277}`, klik `Cancel Request` (dialog terbuka)
16. Paksa respons Cancel Request gagal 500 lewat `Spectra.intercept()`
17. Klik `[Cancel Request]`
18. Verifikasi toast error "Error, failed to cancel request."
19. Verifikasi dialog tetap terbuka untuk retry manual
20. Lepas intercept respons Cancel Request
21. Tutup dialog tanpa membatalkan pengajuan (klik `✕` pada dialog)
22. Verifikasi status `{idW277}` tetap Waiting for Approval

### TC-AC-CS-257: Convert gagal 5xx mode New mempertahankan input dan trial

23. Logout
24. Login sebagai Group Manager `Dewi Anggraini`
25. Buka menu `Allocation > Client Subscription`
26. Ketik Search `{idT257}`, tekan Enter
27. Klik ikon `⋯` pada trial `{idT257}`, klik `Convert` (modal Convert Trial terbuka)
28. Pilih Plan `Professional`, isi Duration `1`, klik `[Submit]`
29. Paksa respons Convert gagal 500 lewat `Spectra.intercept()`
30. Klik `[Convert]`
31. Verifikasi toast error "Error, failed to add subscription."
32. Verifikasi dialog tetap terbuka untuk retry manual
33. Lepas intercept respons Convert
34. Tutup dialog tanpa mengonversi (klik `✕` pada dialog)
35. Verifikasi trial `{idT257}` tetap Active dan tidak ada perubahan data

### TC-AC-CS-258: Convert gagal 5xx mode Renewal menampilkan toast Renew

36. Ganti isi kotak search dengan `Toko Konversi+{runId}-141`, tekan Enter
37. Klik ikon `⋯` pada trial SAMS Client `Toko Konversi+{runId}-141`, klik `Convert` (modal Convert Trial terbuka)
38. Pilih Plan, isi Duration `1`, klik `[Submit]`
39. Paksa respons Convert gagal 500 lewat `Spectra.intercept()`
40. Klik `[Convert]`
41. Verifikasi toast error "Error, failed to renew subscription."
42. Verifikasi dialog tetap terbuka
43. Lepas intercept respons Convert
44. Tutup dialog tanpa mengonversi (klik `✕` pada dialog)
45. Verifikasi trial dan predecessor Client `Toko Konversi+{runId}-141` tidak berubah

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC berbeda dari kolom `sourceTc` sumber (235, 257, 258, 277): TC-AC-CS-277 dipindah sebelum TC-AC-CS-257 dan 258 supaya hanya terjadi satu pergantian akun (S-07).
- Langkah penghubung (S-03): langkah 1, 14, 26, dan 36 (Search untuk menemukan baris target, R-16), langkah 10, 20, 33, 43 (melepas intercept segera setelah dipakai, S-09), langkah 11 sampai 13 (menutup form dirty, S-08), langkah 21, 34, 44 (menutup dialog Convert atau Cancel Request tanpa melanjutkan), langkah 23 (Logout sebagai bagian ganti akun, S-07), dan langkah 25 (membuka List sesudah ganti akun).
- Spec ini melewati ~35 langkah (45). Alasan: semua blok satu kelas harness (fault injection 5xx pada aksi tulis) dengan pola yang sama dan berdiri sendiri, masing-masing memakai data milik spec; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan pemecahan hanya menambah login dan hook.
- Temuan untuk QA:
  - TC-AC-CS-266, 277, 257, 258 tidak menyebut label tombol penutup dialog selain tombol aksi; spec memakai `✕` untuk menutup dialog (perlu konfirmasi QA).
  - TC-AC-CS-258 langkah 3 ("Pilih Plan") tidak menyebut Plan; nilai disepakati tim FE.
  - TC-AC-CS-235, 257, 258, 277 memakai record Pre-setup (#49, #71, #73) sebagai target aksi tulis yang gagal; spec memakai record milik spec (S-06).
  - TC-AC-CS-257 Expected a menyebut toast "Error, failed to add subscription." untuk Convert mode New, sedangkan TC-AC-CS-258 menyebut "Error, failed to renew subscription." untuk mode Renewal; diikuti apa adanya.
