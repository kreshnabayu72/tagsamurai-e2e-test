---
id: TC-FA-CF-E2E-137-form-registrasi-dan-detail-aset-perubahan-konfigurasi-field
title: "Form dan Detail Aset: Deactivate, Rename Opsi, Hapus Opsi, dan Delete Field"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-531
  - TC-FA-CF-532
  - TC-FA-CF-533
  - TC-FA-CF-534
coverage:
  web: automated
---

# Form dan Detail Aset: Deactivate, Rename Opsi, Hapus Opsi, dan Delete Field

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai, pengguna Sarah Johnson (Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Nilai (Pre-setup #1 dan #18). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Nilai (Pre-setup #18; dasar Company Alpha #11 dan baseline #12) dengan aset A1 (Pump, Active), A2 (Generator, Active), dan A3 (Pump, deleted), dirujuk lewat fixture `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE). Field yang diubah: `Maintenance Note` (Text, General, `Checked` pada A1) dan `Brand Tier` (Dropdown `Gold`, `Silver`, `Bronze`; A1 = `Gold`); `Rated Power` (Numeric, `12.5` pada A1) dipakai sebagai anchor.
- Data Dinamis: tidak ada; perubahan konfigurasi pada field baseline dipulihkan seed reset Company.
- Pemulihan: hook `before` memulihkan baseline Company lewat seed reset Company; hook `after` membersihkan field Dinamis milik spec dan memulihkan baseline (Last Updated dan Modified By field baseline berubah oleh aksi spec; dipulihkan seed reset). Langkah 16 memulihkan opsi `Gold` `Brand Tier` sebelum TC-FA-CF-534.
- State global: tidak ada yang diubah.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-531: Deactivate menyembunyikan field dari form dan Detail aset tanpa menghapus nilai

1. Geser switch Active baris `Maintenance Note` ke OFF lalu klik `[Deactivate]` pada dialog
2. Buka Detail aset `A1`
3. Verifikasi Detail aset `A1` menampilkan field `Brand Tier` dengan nilai `Gold`
4. Verifikasi field `Maintenance Note` dan nilai `Checked` tidak tampil di Detail aset `A1`
5. Buka form edit aset `A1`
6. Verifikasi form edit aset `A1` menampilkan input `Brand Tier`
7. Verifikasi field `Maintenance Note` dan nilai `Checked` tidak tampil di form edit aset `A1`
8. Buka Fixed Asset > Settings > Custom Fields, geser switch Active baris `Maintenance Note` ke ON lalu klik `[Activate]` pada dialog
9. Buka Detail aset `A1`
10. Verifikasi field `Maintenance Note` dan nilai `Checked` tampil kembali di Detail aset `A1`
11. Buka form edit aset `A1`
12. Verifikasi field `Maintenance Note` dan nilai `Checked` tampil kembali di form edit aset `A1`

### TC-FA-CF-533: Rename opsi Dropdown yang dipakai aset memperbarui teks nilai pada Detail aset

13. Buka Fixed Asset > Settings > Custom Fields, klik row action `⋯` > `Edit` pada baris `Brand Tier`, rename opsi `Gold` menjadi `Platinum`, lalu klik `[Save]`
14. Buka Detail aset `A1`
15. Verifikasi Detail aset `A1` menampilkan `Platinum` untuk `Brand Tier`

### TC-FA-CF-534: Hapus opsi in-use mengosongkan nilai pada aset yang memilihnya

16. Pulihkan baseline Company lewat seed reset Company (`Brand Tier` kembali dengan opsi `Gold` dan A1 = `Gold`) lalu buka Fixed Asset > Settings > Custom Fields
17. Klik row action `⋯` > `Edit` pada baris `Brand Tier`, hapus opsi `Gold` dan konfirmasi `[Remove]`, lalu klik `[Save]`
18. Buka Detail aset `A1`
19. Verifikasi Detail aset `A1` menampilkan field `Rated Power` dengan nilai `12.5`
20. Verifikasi nilai `Brand Tier` pada `A1` kosong

### TC-FA-CF-532: Delete field menghapus field dan nilai dari form dan Detail aset

21. Buka Fixed Asset > Settings > Custom Fields, klik row action `⋯` > `Delete` pada baris `Maintenance Note`, lalu klik `[Delete]` pada dialog
22. Buka Detail aset `A1`
23. Verifikasi Detail aset `A1` menampilkan field `Rated Power` dengan nilai `12.5`
24. Verifikasi field `Maintenance Note` dan nilai `Checked` tidak tampil di Detail aset `A1` (tidak ada nilai orphan)
25. Buka form edit aset `A1`
26. Verifikasi form edit aset `A1` menampilkan input `Rated Power`
27. Verifikasi field `Maintenance Note` dan nilai `Checked` tidak tampil di form edit aset `A1` (tidak ada nilai orphan)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec memuat TC lintas modul (NC-01): tata letak Detail aset dan form edit aset tidak didefinisikan PRD modul ini; spec hanya mengasersi sejauh teks Expected TC.
- Urutan TC di spec: 531, 533, 534, 532. TC-FA-CF-531 ditempatkan lebih dulu karena Activate memulihkan `Maintenance Note`; TC-FA-CF-533 dan TC-FA-CF-534 memakai opsi `Gold` yang sama sehingga langkah 16 memulihkan opsi `Gold` di antaranya; TC-FA-CF-532 berjalan terakhir karena Delete menghapus data (S-10). TC-FA-CF-535 sampai 537 ada di spec 178.
- Absence field pada Detail dan form didahului `Verifikasi` field lain pada surface yang sama (anchor, 8b butir 2).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 16 dan pembukaan Detail aset serta form edit aset.
- Temuan untuk QA:
  - TC-FA-CF-532 Expected "tidak ada nilai orphan" tidak punya langkah observasi sendiri; spec menggabungkannya dengan asersi nilai tidak tampil di Detail dan form.
  - TC-FA-CF-533 dan TC-FA-CF-534 tidak menyebut cara menyimpan perubahan opsi selain `[Save]`; spec memakai `[Save]` dan `[Remove]` sesuai TC.
  - Email akun Total Control Company Nilai tidak tertulis di Pre-setup TC; env var `FA_TC_NILAI_PASSWORD` disediakan tim FE.
