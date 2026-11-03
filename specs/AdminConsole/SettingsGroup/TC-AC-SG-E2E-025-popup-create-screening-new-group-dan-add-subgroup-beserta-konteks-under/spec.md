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
5. Verifikasi Footer: checkbox "Stay on this form after submitting" default tidak tercentang
6. Verifikasi Footer: checkbox "Stay on this form after submitting" rata kanan, di atas baris tombol
7. Verifikasi tombol `[Clear Field]` (varian teks) dan `[Submit]` (filled, success)
8. Verifikasi tidak ada tombol `[Cancel]`
9. Klik `[✕]` pada popup

### TC-AC-SG-79: Screening Popup Add Subgroup

10. Ketik Search `Branch 1`, tekan Enter
11. Klik ikon `⋯` pada baris group `Branch 1` di tabel
12. Klik "+ Add Subgroup"
13. Verifikasi Title popup "Add Subgroup" (tanpa nama parent di title)
14. Verifikasi teks konteks di bawah title: "Under: Region A > Branch 1" (full path parent)
15. Verifikasi field Group Name kosong dengan placeholder "Enter group name"
16. Verifikasi checkbox "Stay on this form after submitting" tidak tercentang
17. Verifikasi tombol `[Clear Field]` dan `[Submit]` tampil
18. Klik `[✕]` pada popup
19. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SG-80: Konteks Under untuk subgroup di bawah group level 1

20. Klik ikon `⋯` pada node `Region B` di sidebar, lalu pilih "+ Add Subgroup"
21. Verifikasi konteks menampilkan "Under: Region B"
22. Verifikasi Title popup "Add Subgroup"
23. Klik `[✕]` pada popup

## Notes

- Langkah penghubung (S-03, R-16): langkah 10 (Search `Branch 1` untuk menemukan baris target karena tabel All Groups terbagi dua halaman), langkah 19 (klik `(←)` pada kotak Search sesudah popup ditutup), langkah 9, 18, dan 23 (menutup popup yang kosong; popup tanpa isian tertutup tanpa dialog Unsaved Changes).
