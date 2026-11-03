---
id: TC-FA-CF-E2E-136-form-registrasi-field-muncul-sesuai-scope-active-dan-value-type
title: "Form Registrasi Aset: Field Muncul Sesuai Scope, Active, dan Value Type"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-524
  - TC-FA-CF-525
  - TC-FA-CF-526
  - TC-FA-CF-527
  - TC-FA-CF-528
  - TC-FA-CF-529
  - TC-FA-CF-530
coverage:
  web: automated
---

# Form Registrasi Aset: Field Muncul Sesuai Scope, Active, dan Value Type

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha, pengguna Sarah Johnson (Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha (Pre-setup #1). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (plan Professional, lisensi FA-7 aktif; Pre-setup #11) dengan baseline tab General delapan field (Pre-setup #12) yang dirujuk lewat fixture `Fixture.faCustomFields.baselineGeneral`. Aset konsumen A1 (Asset Name `Pump`, Active) dan A2 (Asset Name `Generator`, Active) (Pre-setup #31); form registrasi aset pada modul Asset Registration. Field yang diamati: `Asset Serial Tag` (Text, General, Required Yes), `Storage Capacity` (Scope Generator dan Pump, Placeholder `Capacity in GB`), `Depreciated Ratio` (Inactive), dan `Operating Voltage` (Global Generator = `220V`).
- Data Dinamis: aset baru hasil registrasi (TC-FA-CF-527) dibersihkan di hook `after`; nilai input `Asset Serial Tag` dan isian wajib form registrasi lain disediakan fixture baru `Fixture.faCustomFields.asetBaru` (tidak tertulis di TC; lihat Temuan untuk QA). Hasil rename `Serial Number {runId}-136`.
- State global: rename `Asset Serial Tag` dipulihkan seed reset Company di hook `after`.
- Pemulihan: hook `before` memulihkan baseline Company lewat seed reset Company; hook `after` membersihkan field Dinamis milik spec dan memulihkan baseline (Last Updated dan Modified By field baseline berubah oleh aksi spec; dipulihkan seed reset).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-524: Field Active ber-Scope General muncul di form registrasi untuk Asset Name apa pun

1. Buka form registrasi aset pada modul Asset Registration
2. Pilih Asset Name `Pump`
3. Verifikasi label `Asset Serial Tag` tampil untuk `Pump`
4. Ganti ke Asset Name `Generator`
5. Verifikasi label `Asset Serial Tag` tampil untuk `Generator`

### TC-FA-CF-530: Placeholder field tampil pada input form registrasi

6. Pilih Asset Name `Pump`
7. Verifikasi input `Storage Capacity` menampilkan placeholder `Capacity in GB`

### TC-FA-CF-525: Field Scope Specific hanya muncul bila Asset Name aset termasuk dalam himpunan

8. Verifikasi label `Storage Capacity` tampil untuk `Pump`
9. Pilih Asset Name `Compressor`
10. Verifikasi label `Asset Serial Tag` tampil untuk `Compressor`
11. Verifikasi label `Storage Capacity` tidak tampil untuk `Compressor`

### TC-FA-CF-526: Field Inactive tidak muncul di form registrasi

12. Verifikasi label `Depreciated Ratio` tidak tampil untuk Asset Name yang dipilih (field Inactive)

### TC-FA-CF-529: Required menandai input dengan asterisk dan memvalidasi saat registrasi

13. Pilih Asset Name `Generator`
14. Kosongkan input `Asset Serial Tag` (Required Yes) lalu simpan
15. Verifikasi input `Asset Serial Tag` ditandai wajib (asterisk)
16. Verifikasi penyimpanan ditolak dengan pesan inline pada input `Asset Serial Tag` (teks pesan tidak diassert)

### TC-FA-CF-527: Field Value Type Global tidak tampil di form registrasi dan nilainya read-only di detail aset

17. Verifikasi label `Operating Voltage` tidak tampil di form registrasi untuk `Generator`
18. Isi input `Asset Serial Tag` dengan nilai dari fixture `Fixture.faCustomFields.asetBaru` lalu simpan aset
19. Verifikasi aset tersimpan tanpa error validasi pada `Operating Voltage` (Required tidak ditegakkan)
20. Buka Detail aset yang baru disimpan
21. Verifikasi Detail aset menampilkan nilai `220V` untuk `Operating Voltage` secara read-only

### TC-FA-CF-528: Rename Field Name langsung menjadi label input form registrasi

22. Buka Settings > Custom Fields, klik row action `⋯` > `Edit` pada baris `Asset Serial Tag`, ubah Field Name menjadi `Serial Number {runId}-136`, lalu klik `[Save]`
23. Buka form registrasi aset pada modul Asset Registration
24. Verifikasi label input pada form registrasi adalah `Serial Number {runId}-136`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec memuat TC lintas modul (NC-01): tata letak, label, dan kontrol form registrasi aset dan Detail aset tidak didefinisikan PRD modul ini; spec hanya mengasersi sejauh teks Expected TC.
- Urutan TC di spec: 524, 530, 525, 526, 529, 527, 528 (bukan urutan nomor). Satu pembukaan form (langkah 1) dipakai bersama karena TC-FA-CF-524, 525, 526, 527, 529, dan 530 hanya mengamati dan mengubah pilihan Asset Name pada form yang sama (halaman yang sama dipakai berulang, bagian 3); TC-FA-CF-527 berjalan sesudah TC-FA-CF-529 karena menyimpan aset, dan TC-FA-CF-528 berjalan terakhir karena mengganti nama field (S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan pemilihan Asset Name.
- Temuan untuk QA:
  - TC-FA-CF-527 "Simpan aset" dan TC-FA-CF-529 "Kosongkan input ... lalu simpan" tidak menyebut isian wajib form registrasi aset selain custom field; spec memakai fixture baru `Fixture.faCustomFields.asetBaru` yang disediakan tim FE.
  - TC-FA-CF-529 tidak menyebut tombol simpan dan teks pesan inline; spec menulis "simpan" dan tidak mengasersi teks pesan sesuai Expected TC.
  - TC-FA-CF-525 Expected a menyebut `Pump` bersama `Compressor` pada langkah yang sama; spec memeriksa `Pump` lebih dulu lalu `Compressor`, dengan `Asset Serial Tag` sebagai anchor untuk absence `Storage Capacity` dan `Depreciated Ratio`.
  - TC-FA-CF-527 Expected a menyebut "Required tidak ditegakkan" tanpa langkah observasi tersendiri; spec mengasersi aset tersimpan tanpa error pada `Operating Voltage`.
  - Email akun Total Control Company Alpha mengikuti pola Pre-setup #1; env var `FA_TC_PASSWORD` disediakan tim FE.
