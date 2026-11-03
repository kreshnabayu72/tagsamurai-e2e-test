---
id: TC-AC-SG-E2E-025-popup-create-screening-new-group-dan-add-subgroup-beserta-konteks-under
title: "Popup Create: Screening New Group dan Add Subgroup beserta Konteks Under"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-78
  - TC-AC-SG-79
  - TC-AC-SG-80
coverage:
  web: automated
---

# Popup Create: Screening New Group dan Add Subgroup beserta Konteks Under

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data: `Pohon Uji Utama` entitas Principal (Pre-setup #16 dan #17, 14 group) dibaca saja (`Branch 1` di bawah `Region A`, `Region B`). Popup hanya dibuka dan ditutup tanpa mengisi atau menyimpan, sehingga tidak ada data yang ditulis.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah data atau state global.

## Test Steps

### TC-AC-SG-78: Screening Popup New Group

1. Klik `[+] Group` di Sidebar Group Tree
2. Verifikasi Header popup: Title "New Group" dan ikon close `[✕]`
3. Verifikasi tidak ada konteks "Under:" pada popup
4. Verifikasi Body: field Group Name kosong dengan placeholder "Enter group name"
5. Verifikasi Footer: checkbox "Stay on this form after submitting" default tidak tercentang dan rata kanan, di atas baris tombol
6. Verifikasi tombol `[Clear Field]` (varian teks) dan `[Submit]` (filled, success)
7. Verifikasi tidak ada tombol `[Cancel]`
8. Klik `[✕]` pada popup

### TC-AC-SG-79: Screening Popup Add Subgroup

9. Klik ikon `⋯` pada baris group `Branch 1` di tabel
10. Klik "+ Add Subgroup"
11. Verifikasi Title popup "Add Subgroup" (tanpa nama parent di title)
12. Verifikasi teks konteks di bawah title: "Under: Region A > Branch 1" (full path parent)
13. Verifikasi field Group Name kosong dengan placeholder "Enter group name"
14. Verifikasi checkbox "Stay on this form after submitting" tidak tercentang
15. Verifikasi tombol `[Clear Field]` dan `[Submit]` tampil
16. Klik `[✕]` pada popup

### TC-AC-SG-80: Konteks Under untuk subgroup di bawah group level 1

17. Klik ikon `⋯` pada node `Region B` di sidebar, lalu pilih "+ Add Subgroup"
18. Verifikasi konteks menampilkan "Under: Region B"
19. Verifikasi Title popup "Add Subgroup"
20. Klik `[✕]` pada popup

## Notes

- Langkah penghubung (S-03): langkah 8, 16, dan 20 (menutup popup yang kosong; popup tanpa isian tertutup tanpa dialog Unsaved Changes).
- Baris `Branch 1` pada langkah 9 dibaca dari halaman tabel All Groups; bila baris tidak berada pada halaman pertama, Search atas nama group dipakai sebagai langkah penghubung (R-16).
