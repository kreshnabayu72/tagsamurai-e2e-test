---
id: TC-FA-GRP-E2E-021-role-matrix-positif-edit-manage-group-ru-dan-group-manager
title: "Role Matrix Positif Edit: Edit Branch West 1 (R+U), Ubah Function (R+U), dan Edit Room 301 (Group Manager)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-65
  - TC-FA-GRP-69
  - TC-FA-GRP-947
coverage:
  web: automated
---

# Role Matrix Positif Edit: Edit Branch West 1 (R+U), Ubah Function (R+U), dan Edit Room 301 (Group Manager)

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (spec ditulis per blok role karena langkah tiap role berbeda):

| Role | Akun (Pre-setup) | Password | Blok langkah |
|---|---|---|---|
| Manage Group R+U scope Region West (TC-FA-GRP-65, 947) | No 6 `manageGroupUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGRU_PASSWORD` | langkah 1 sampai 17 |
| Group Manager scope Region West (TC-FA-GRP-69) | No 4 `groupManagerGroups_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` | langkah 18 sampai 26 |

- Login di hook `before` spec ini sebagai Manage Group R+U; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` untuk kedua akun disetel `seen` di hook `before` spec ini dan dipulihkan di hook `after` (kemampuan disediakan tim FE/BE); hook suite hanya menyetel akun aktor default suite.
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`). Node milik spec dipakai sebagai target Edit agar Branch West 1 dan Room 301 Tabel A tidak berubah (S-06):

| TC | Nama TC | Nama seed | State |
|---|---|---|---|
| TC-FA-GRP-65, 947 | Branch West 1 | `Branch Edit {runId}-021` | Anak langsung Region West, Function None, Description kosong, kosong aset |
| TC-FA-GRP-69 | Room 301 (cucu Region West) | `Room Edit {runId}-021` | Anak `Branch Edit {runId}-021`, Function None |

- Nilai Code baru TC-FA-GRP-69: `RE` diikuti `{runId}` (tidak lebih dari 15 karakter); nilai Description baru TC-FA-GRP-65: `Deskripsi {runId}-021`.
- Kemampuan teknis: fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### Role Manage Group R+U (TC-FA-GRP-65)

1. Klik node Region West di sidebar
2. Klik (⋯) pada baris `Branch Edit {runId}-021`
3. Klik `Edit`
4. Ubah Description menjadi `Deskripsi {runId}-021`
5. Klik [Save]
6. Verifikasi toast sukses `Success, group has been updated.`
7. Klik (⋯) pada baris `Branch Edit {runId}-021`
8. Klik `Detail`
9. Verifikasi header Popup Detail Group menampilkan Description `Deskripsi {runId}-021`
10. Tutup popup dengan [X]

### Role Manage Group R+U (TC-FA-GRP-947)

11. Klik (⋯) pada baris `Branch Edit {runId}-021`
12. Klik `Edit`
13. Pilih Function `Assignable`
14. Klik [Save]
15. Verifikasi toast sukses `Success, group has been updated.`
16. Verifikasi badge Function baris `Branch Edit {runId}-021` menjadi `Assignable`
17. Verifikasi dot Function node `Branch Edit {runId}-021` di sidebar berwarna primary

### Role Group Manager (TC-FA-GRP-69)

18. Logout dari akun Manage Group R+U
19. Login sebagai Group Manager dengan `Spectra.env.FA_GM_PASSWORD`
20. Buka Fixed Asset > Settings > Groups
21. Klik toggle expand-all pada sidebar
22. Klik (⋯) pada node `Room Edit {runId}-021` di sidebar
23. Klik `Edit`
24. Ubah Code menjadi `RE{runId}`
25. Klik [Save]
26. Verifikasi toast sukses `Success, group has been updated.`

## Notes

- Spec 26 langkah, di bawah batas sekitar 35 langkah.
- Langkah penghubung (S-03): langkah 1 (memilih Region West agar baris target tampil), langkah 7 sampai 10 (membuka Detail untuk mengamati Description tersimpan; TC tidak memberi langkah observasi), langkah 10 (menutup popup), langkah 18 sampai 20 (ganti akun eksplisit), langkah 21 (expand-all).
- Urutan TC dalam spec: 65, 947, 69.
- Pembagian TC lintas spec: Role Matrix positif Create ada di spec 020 dan Delete di spec 022.
- Temuan untuk QA:
  - TC-FA-GRP-65, 69 memakai Branch West 1 dan Room 301 Tabel A sebagai target Edit; spec memakai node bersuffix milik spec agar Pre-setup tidak berubah (S-06).
  - TC-FA-GRP-65 tidak menyebut cara mengamati "Description baru tersimpan"; spec memakai Popup Detail Group.
  - Post Condition TC-FA-GRP-947 (baris Changelog Edit Function None → Assignable, Modified By aktor) tidak punya langkah observasi di TC sehingga tidak diasersi; Expected TC-FA-GRP-69 tidak menyebut perubahan Code yang terlihat sehingga hanya toast yang diasersi.
