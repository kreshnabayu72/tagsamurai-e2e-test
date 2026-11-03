---
id: TC-FA-CAT-E2E-018-new-category-screening-aksesibilitas-dan-saving-state
title: "New Category: Screening Popup, Aksesibilitas, dan Saving State Tombol Submit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-58
  - TC-FA-CAT-60
  - TC-FA-CAT-61
coverage:
  web: automated
---

# New Category: Screening Popup, Aksesibilitas, dan Saving State Tombol Submit

## Prerequisites

- Mode: FE+BE. Backend nyata; respons Create ditahan 3 detik lewat `Spectra.intercept()` hanya untuk mengamati saving state (bukan kegagalan yang dipaksa).
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settingsCategories.totalControl` (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`, client CatMain (Pre-setup #20). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan; keputusan tim).
- Data Pre-setup: client CatMain (Pre-setup #20); hanya dibaca.
- Data milik spec: kategori `Saving Cat {runId}-018` dibuat oleh TC-FA-CAT-61 lewat UI. Hook `after` menghapusnya lewat API.
- Kemampuan teknis: `Spectra.intercept()` untuk menunda respons Create Category 3 detik (intercept selesai sendiri setelah penundaan); kemampuan membaca atribut ARIA (`aria-required`, `aria-describedby`) dan memindahkan fokus dengan Tab.
- Seed dan pemulihan lewat API, flag Guided Tooltip, dan hook suite lain: lihat `suite.md`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-58: Screening popup New Category (3 zona)

1. Klik `[+] Category` pada sidebar
2. Verifikasi zona Header: Title `New Category`
3. Verifikasi zona Header: icon close (✕)
4. Verifikasi zona Header: tidak ada Breadcrumb
5. Verifikasi zona Body: field Category Name berlabel `Category Name *` dengan placeholder `Enter category name`
6. Verifikasi zona Body: field Code berlabel `Category Code` dengan placeholder `Enter code, or leave blank to auto-generate`
7. Verifikasi zona Body: helper text field Code `Letters, numbers, hyphens, underscores, and dots only`
8. Verifikasi zona Body: field Description (textarea) berlabel `Description` dengan placeholder `Enter description...`
9. Verifikasi zona Footer: checkbox `Stay on this form after submitting` Unchecked
10. Verifikasi zona Footer: checkbox rata kanan di baris atas footer tepat di atas tombol
11. Verifikasi zona Footer: tombol `[Clear Field]` (text, primary) dan `[Submit]` (success) di baris bawah
12. Verifikasi zona Footer: tidak ada tombol `[Cancel]`

### TC-FA-CAT-60: Accessibility popup New Category: aria-required, aria-describedby, dan focus trap

13. Inspeksi atribut field Category Name
14. Verifikasi field Category Name (satu-satunya field wajib) memiliki `aria-required="true"`
15. Verifikasi field Code dan Description tidak memiliki `aria-required="true"`
16. Klik `[Submit]` dengan field kosong
17. Inspeksi ulang atribut field Category Name
18. Verifikasi setelah error V-01 tampil, field Category Name memiliki `aria-describedby` yang menunjuk ke pesan error inline
19. Tekan Tab berulang sampai fokus kembali ke awal popup
20. Verifikasi fokus terjebak di dalam popup (focus trapped) dan tidak keluar ke halaman di belakang

### TC-FA-CAT-61: Tombol [Submit] masuk saving state dan mengunci kontrol form saat request berjalan

21. Isi Category Name `Saving Cat {runId}-018`
22. Hover tombol `[Submit]`
23. Verifikasi hover menampilkan state hover tombol `[Submit]`
24. Tunda respons Create 3 detik lewat intercept jaringan, lalu klik `[Submit]`
25. Verifikasi selama request berjalan `[Submit]` menampilkan spinner dan disabled
26. Verifikasi selama request berjalan `[Clear Field]`, icon close (✕), dan seluruh input disabled
27. Verifikasi setelah respons sukses popup tertutup
28. Verifikasi toast `Success, category has been created.` tampil

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan dan penggabungan form (S-10, prinsip 6): TC-FA-CAT-58 membuka popup dan TC-FA-CAT-60 serta TC-FA-CAT-61 membuka popup baru pada langkah pertamanya. Spec memakai satu sesi popup dari TC-FA-CAT-58 karena popup belum diisi (identik dengan popup baru); jumlah buka form tidak melebihi jumlah kejadian menutup (popup ditutup oleh Submit sukses di akhir). Urutan screening, aksesibilitas, lalu aksi sukses mengikuti bagian 3.
- Langkah penghubung (S-03): langkah 13 dan 17 (inspeksi atribut sebagai aksi pembaca ARIA) dan langkah 19 (Tab berulang). Langkah 21 (mengisi Category Name) sekaligus menghapus error V-01 dari TC-FA-CAT-60 sebelum Submit sukses (R-12).
- Menahan respons Create hanya untuk mengamati saving state; bukan kelas b (bagian 3 prinsip 13b) sehingga tetap di spec fungsional.
- Temuan untuk QA:
  - TC-FA-CAT-61 Post Condition tidak punya langkah observasi; kategori `Saving Cat` tersimpan tidak diasersi (S-01).
  - TC-FA-CAT-60 Expected b menyebut "error V-01" tanpa mengulang teksnya; spec mengasersi atribut `aria-describedby` yang menunjuk pesan error inline `Category name must not be empty` (teks dari TC-FA-CAT-77) tanpa asersi teks pesan terpisah.
