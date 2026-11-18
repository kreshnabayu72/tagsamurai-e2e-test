---
id: TC-AC-PF-E2E-065-template-tidak-disimpan-sebagai-relasi-perubahan-default-plan-tidak-mengubah-custom
title: "Template Tidak Disimpan sebagai Relasi: Perubahan Default Plan Tidak Mengubah Custom Plan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-152
coverage:
  web: automated
---

# Template Tidak Disimpan sebagai Relasi: Perubahan Default Plan Tidak Mengubah Custom Plan

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal), akun #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.AC_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_ac-plans-features` true dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): sesi API aktor dan fixture backend idempoten untuk memulihkan Dataset Pre-setup dan menghapus plan buatan spec. General Settings (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) disiapkan fixture sebagai precondition TC dan tidak diubah spec.
- Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12): nilai Pre-setup dirujuk lewat kunci fixture yang dibuat tim FE; password dan token tidak ditulis di spec.
- Data Pre-setup: Dataset Plan A dengan default plan `Growth` v5 (Asset Name cap 50, Group count 3, Group hierarchy depth 2, Category count 20, Category hierarchy depth 2, Scheduled reports 1, API call quota 100K/month, Asset ID Configuration ON, License allocation per group ON, Open API ON, SAMP & Document Center OFF, Custom Report Builder OFF, Approval Workflow OFF, Borrowing Basic, Assignment Basic, Transfer None, Disposal Full, Accounting & Depreciation None).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup (`Growth` v5, `Growth Baru`) dipakai apa adanya, sebagai target Edit (Group count 25, rename ke `Growth Baru`); pemulihan ke `Growth` v5 dijalankan sebagai langkah penghubung sesudah asersi. Efek pada Last Updated dan entri Changelog `Growth` dicatat di Notes; pemulihan Dataset dijamin fixture backend idempoten yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini.
- Data Dinamis: custom plan `Paket Principal Baru-{runId}-065` (bersuffix `-{runId}-065`) dibuat dari Template `Growth` lewat UI (langkah dependensi TC-AC-PF-146 disalin); tersimpan v1.
- State global: Dataset Pre-setup bersama; suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Pembersihan: hook `after` menghapus plan buatan spec ini (nama bersuffix `-{runId}-065`) lewat fixture backend, memulihkan Dataset (`Growth` kembali v5, Group count `3`, nama `Growth`), dan mengembalikan sesi ke akun default suite.

## Test Steps

### Dependensi: custom plan dari Template (disalin dari TC-AC-PF-146)

1. Buka tab `Custom`, sub-tab `Active`
2. Klik `+ Custom Plan` pada toolbar
3. Pilih Product `FAMS`, pilih Template `Growth`, isi Plan Name `Paket Principal Baru-{runId}-065`
4. Klik `[Submit]`
5. Tunggu aksi selesai

### Perubahan default plan Template (TC-AC-PF-152)

6. Buka tab `Default`, sub-tab `Active`
7. Buka Edit `Growth`, ubah Group count menjadi `25`, lalu klik `[Save]`
8. Tunggu aksi selesai
9. Buka tab `Default`, sub-tab `Active`
10. Buka Edit `Growth`, ubah Plan Name menjadi `Growth Baru`, lalu klik `[Save]`
11. Tunggu aksi selesai
12. Buka tab `Custom`, sub-tab `Active`, ketik Search `Paket Principal Baru-{runId}-065`, tekan Enter, lalu buka Plan Detail baris itu pada Tab Overview
13. Verifikasi custom plan `Paket Principal Baru-{runId}-065` tetap Group count `3`, versi `v1`
14. Verifikasi tidak ada kolom Base Plan atau label Template pada Plan Detail custom plan
15. Pulihkan Dataset Plan A lewat fixture backend (default plan `Growth` kembali v5, Group count `3`, nama `Growth`)

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 5, 6, 8, 9, 11, 12, 15.
- TC-AC-PF-152 ada di spec sendiri karena mengubah default plan `Growth` yang menjadi Template TC-AC-PF-146 dan TC-AC-PF-149 di spec 057; langkah dependensi TC-AC-PF-146 disalin ke sini (S-04) tanpa `Verifikasi` karena Expected-nya milik spec 057.
- Efek pada Pre-setup: dua Save pada `Growth` menambah versi, mengubah Last Updated, dan menambah entri Changelog default plan `Growth`; seluruhnya dipulihkan fixture backend di langkah akhir dan di hook `before` serta `after` (A-6). Suite berjalan serial.
- Langkah penghubung: Search untuk menemukan baris target (R-16), tunggu aksi selesai sesudah `[Submit]` dan `[Save]` yang hasilnya tidak diasersi sebelum pindah surface (bagian 8b butir 8), dan pemulihan Dataset.
- Temuan untuk QA: (1) Langkah 2 TC-AC-PF-152 ("Rename `Growth` menjadi `Growth Baru`") tidak menyebut apakah rename dilakukan di Edit yang sama dengan Group count atau Edit terpisah; spec memakai Edit terpisah. (2) Kondisi form Edit sesudah `[Save]` (kembali ke daftar atau ke Plan Detail) tidak disebut TC; spec hanya menunggu aksi selesai.
