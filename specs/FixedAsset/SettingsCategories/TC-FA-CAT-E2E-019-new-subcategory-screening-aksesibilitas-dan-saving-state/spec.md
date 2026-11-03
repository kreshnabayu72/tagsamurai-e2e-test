---
id: TC-FA-CAT-E2E-019-new-subcategory-screening-aksesibilitas-dan-saving-state
title: "New Subcategory: Screening Popup, Aksesibilitas, dan Saving State Tombol Submit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-59
  - TC-FA-CAT-624
  - TC-FA-CAT-627
coverage:
  web: automated
---

# New Subcategory: Screening Popup, Aksesibilitas, dan Saving State Tombol Submit

## Prerequisites

- Mode: FE+BE. Backend nyata; respons Add Subcategory ditahan 3 detik lewat `Spectra.intercept()` hanya untuk mengamati saving state (bukan kegagalan yang dipaksa).
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settingsCategories.totalControl` (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`, client CatMain (Pre-setup #20). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan; keputusan tim).
- Data Pre-setup: client CatMain (Pre-setup #20); baris `Peripheral` (level 1) dipakai sebagai parent dan hanya dibaca.
- Data milik spec: subkategori `Saving Sub {runId}-019` dibuat oleh TC-FA-CAT-627 lewat UI di bawah `Peripheral`. Hook `after` menghapusnya lewat API.
- Kemampuan teknis: `Spectra.intercept()` untuk menunda respons Add Subcategory 3 detik; kemampuan membaca atribut ARIA (`aria-required`, `aria-describedby`) dan memindahkan fokus dengan Tab.
- Seed dan pemulihan lewat API, flag Guided Tooltip, dan hook suite lain: lihat `suite.md`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-59: Screening popup New Subcategory dengan banner parent

1. Klik elipsis (⋯) pada baris `Peripheral`
2. Klik `+ Add Subcategory`
3. Verifikasi Title `New Subcategory` dan icon close (✕) tampil
4. Verifikasi banner konteks `Adding subcategory under parent: Peripheral`
5. Verifikasi field Category Name, Category Code, dan Description tampil dengan label, placeholder, dan helper text sama seperti popup New Category (`Category Name *` / `Enter category name`; `Category Code` / `Enter code, or leave blank to auto-generate` / helper `Letters, numbers, hyphens, underscores, and dots only`; `Description` / `Enter description...`)
6. Verifikasi footer: checkbox `Stay on this form after submitting` Unchecked
7. Verifikasi footer: tombol `[Clear Field]` dan `[Submit]` tampil

### TC-FA-CAT-624: Accessibility popup New Subcategory: aria-required, aria-describedby, dan focus trap

8. Inspeksi atribut field Category Name
9. Verifikasi field Category Name (satu-satunya field wajib) memiliki `aria-required="true"`
10. Verifikasi field Code dan Description tidak memiliki `aria-required="true"`
11. Klik `[Submit]` dengan field kosong
12. Inspeksi ulang atribut field Category Name
13. Verifikasi setelah error V-01 tampil, field Category Name memiliki `aria-describedby` yang menunjuk ke pesan error inline
14. Tekan Tab berulang sampai fokus kembali ke awal popup
15. Verifikasi fokus terjebak di dalam popup (focus trapped) dan tidak keluar ke halaman di belakang

### TC-FA-CAT-627: Tombol [Submit] New Subcategory: state hover dan saving state

16. Isi Category Name `Saving Sub {runId}-019`
17. Hover tombol `[Submit]`
18. Verifikasi hover menampilkan state hover tombol `[Submit]`
19. Tunda respons Add Subcategory 3 detik lewat intercept jaringan, lalu klik `[Submit]`
20. Verifikasi selama request berjalan `[Submit]` menampilkan spinner dan disabled
21. Verifikasi selama request berjalan `[Clear Field]`, icon close (✕), dan seluruh input disabled
22. Verifikasi setelah respons sukses popup tertutup
23. Verifikasi toast `Success, category has been created.` tampil

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan dan penggabungan form (S-10, prinsip 6): TC-FA-CAT-624 dan TC-FA-CAT-627 membuka popup baru pada langkah pertamanya. Spec memakai satu sesi popup dari TC-FA-CAT-59 karena popup belum diisi (identik dengan popup baru); jumlah buka form tidak melebihi jumlah kejadian menutup (popup ditutup oleh Submit sukses di akhir). Urutan screening, aksesibilitas, lalu aksi sukses mengikuti bagian 3.
- Langkah penghubung (S-03): langkah 8 dan 12 (inspeksi atribut sebagai aksi pembaca ARIA) dan langkah 14 (Tab berulang). Langkah 16 (mengisi Category Name) sekaligus menghapus error V-01 dari TC-FA-CAT-624 sebelum Submit sukses (R-12).
- Menahan respons Add Subcategory hanya untuk mengamati saving state; bukan kelas b (bagian 3 prinsip 13b) sehingga tetap di spec fungsional.
- Temuan untuk QA:
  - TC-FA-CAT-59 Expected c menyebut field "sama seperti popup New Category" tanpa mengulang teks; spec menyalin teks label, placeholder, dan helper dari TC-FA-CAT-58 (S-02).
  - TC-FA-CAT-627 Post Condition tidak punya langkah observasi; subkategori `Saving Sub` tersimpan tidak diasersi (S-01).
  - TC-FA-CAT-624 Expected b menyebut "error V-01" tanpa mengulang teksnya; spec mengasersi atribut `aria-describedby` yang menunjuk pesan error inline tanpa asersi teks pesan terpisah.
