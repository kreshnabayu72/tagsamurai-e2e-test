---
id: TC-FA-LBL-E2E-034-batas-katalog-master-data-count-limit-d-06-pada-create-bagian-1
title: "Batas Katalog Master Data Count Limit (D-06) pada Create (bagian 1/2)"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-103
  - TC-FA-LBL-102
  - TC-FA-LBL-104
coverage:
  web: automated
---

# Batas Katalog Master Data Count Limit (D-06) pada Create (bagian 1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Limit (Pre-setup #11, pengguna `Total Control Limit`; email akun ini tidak tertulis di Pre-setup TC, lihat Temuan untuk QA), password dari `Spectra.env.FA_TC_LIMIT_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_LIMIT_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak mengubah state global kecuali dinyatakan di bawah.
- Suffix nama bersuffix spec ini: `{runId}-034` (`{runId}` hanya digit).
- State global: Master Data Count Limit Company Limit diturunkan ke 1000 (nilai terendah yang diizinkan) di hook `before` dan dipulihkan di hook `after` (S-13: akun atau kemampuan pelaku disediakan tim FE). Suite berjalan serial (`parallel: false`).
- Seeding hook `before`: katalog Company Limit diisi lewat API sampai tepat dua label di bawah batas (seed ini milik spec dan dihapus di `after`).
- Label yang dibuat: `Edge Slot A 103 {runId}-034`, `Edge Slot B 103 {runId}-034`, `Last Slot 102 {runId}-034` (tidak tersimpan), `Race Filler 102 {runId}-034` (via API), `Stay Last 104 {runId}-034`, `Stay Over 104 {runId}-034` (tidak tersimpan).
- Label yang dibuat spec ini (nama bersuffix `{runId}-034`) dihapus di hook `after` lewat sesi API aktor.
- Kemampuan teknis (disediakan tim FE/BE, suite.md): sesi API aktor dan fixture BE untuk membaca state katalog, menambah dan menghapus label tunggal, serta menyetel dan memulihkan Master Data Count Limit.

## Test Steps

### TC-FA-LBL-103: Batas diuji di ambang: satu di bawah batas berhasil, tepat di batas ditolak

1. Klik `[+ Label]`
2. Isi Label Name `Edge Slot A 103 {runId}-034`
3. Klik `[Submit]`
4. Verifikasi toast `Success, label has been created.` (katalog satu di bawah batas)
5. Klik `[+ Label]`
6. Isi Label Name `Edge Slot B 103 {runId}-034`
7. Klik `[Submit]`
8. Verifikasi toast `Success, label has been created.` (katalog tepat di batas)
9. Klik `[+ Label]`
10. Verifikasi dialog dengan title `Label Limit Reached` dan body `You've reached the platform limit of [Limit] labels. Contact support if you need a higher limit.` tampil
11. Verifikasi modal Create Label tidak dibuka
12. Klik `[OK]`

### TC-FA-LBL-102: Submit saat batas baru tercapai antara klik dan Submit menampilkan D-06 dan menahan input

13. Hapus label `Edge Slot B 103 {runId}-034` lewat sesi API hingga katalog tepat satu di bawah batas tersimpan
14. Klik `[+ Label]`
15. Isi Label Name `Last Slot 102 {runId}-034`
16. Tambah label `Race Filler 102 {runId}-034` lewat sesi API hingga katalog tepat di batas tersimpan
17. Klik `[Submit]`
18. Verifikasi dialog dengan title `Label Limit Reached` dan body `You've reached the platform limit of [Limit] labels. Contact support if you need a higher limit.` tampil
19. Verifikasi label `Last Slot 102 {runId}-034` tidak dibuat (lewat fixture BE)
20. Klik `[OK]` pada dialog
21. Verifikasi dialog tertutup
22. Verifikasi modal Create tetap terbuka dengan Label Name `Last Slot 102 {runId}-034` dipertahankan

### TC-FA-LBL-104: Stay on this form: pembuatan berulang sampai batas lalu ditolak tanpa menyimpan

23. Hapus label `Race Filler 102 {runId}-034` lewat sesi API hingga katalog tepat satu di bawah batas tersimpan
24. Centang `Stay on this form after submitting`
25. Ganti isi Label Name dengan `Stay Last 104 {runId}-034`
26. Klik `[Submit]`
27. Verifikasi toast `Success, label has been created.`
28. Verifikasi form ter-reset dan modal tetap terbuka
29. Isi Label Name `Stay Over 104 {runId}-034`
30. Klik `[Submit]`
31. Verifikasi dialog dengan title `Label Limit Reached` dan body `You've reached the platform limit of [Limit] labels. Contact support if you need a higher limit.` tampil
32. Verifikasi label `Stay Over 104 {runId}-034` tidak dibuat (lewat fixture BE)
33. Klik `[OK]`
34. Verifikasi modal tetap terbuka dengan input dipertahankan walau Stay tercentang
35. Klik icon `[✕]`
36. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` dan `[Leave]` tampil
37. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 103, 102, 104. Kuota katalog dibangun berurutan: dua di bawah batas (hook), tepat di batas (akhir TC-FA-LBL-103), satu di bawah batas lewat penghapusan label milik spec (langkah 13 dan 23). Satu pembukaan modal dipakai TC-FA-LBL-102 dan TC-FA-LBL-104 (prinsip 6).
- Spec ini melewati ±35 langkah (langkah terakhir 37). Alasan pertahanan, P-4 (state global bersama): ketiga TC berbagi kuota Master Data Count Limit Company Limit yang sama dan membangunnya berurutan; seeding katalog sampai batas lewat API mahal (sekitar 1000 label), sehingga memecah spec berarti mengulang seeding itu tanpa mengubah makna. Semua langkah satu kelas harness (volume data, kelas e).
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 12 (menutup dialog D-06), langkah 13 dan 23 (menyetel ulang kuota lewat sesi API, ditulis "... hingga ... tersimpan", R-20), dan langkah 37 (menutup modal; form dirty karena Label Name terisi, jadi ditutup lewat dialog `Unsaved Changes` dengan `[Leave]`, S-08).
- Asersi `[Limit]` terisi nilai Master Data Count Limit ada di spec 035 (TC-FA-LBL-101).
- Temuan untuk QA:
  - Email dan password akun `Total Control Limit` (Pre-setup #11) tidak tertulis di Pre-setup TC; email mengikuti pola `totalControl_automated_{namaCompany}@qwertysystem.net` dan akun disediakan tim FE.
  - TC-FA-LBL-102 Post Condition "tidak ada entri log untuk percobaan ditolak" tidak punya langkah observasi di TC dan tidak diasersi di spec ini (S-05).
  - TC-FA-LBL-102 langkah 3 "Tambah satu label lewat API" tidak menyebut aktor atau endpoint; spec memakai sesi API aktor yang disediakan tim FE/BE.
