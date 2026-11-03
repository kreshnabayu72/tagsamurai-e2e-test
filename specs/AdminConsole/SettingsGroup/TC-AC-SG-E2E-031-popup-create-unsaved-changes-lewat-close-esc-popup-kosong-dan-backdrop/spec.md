---
id: TC-AC-SG-E2E-031-popup-create-unsaved-changes-lewat-close-esc-popup-kosong-dan-backdrop
title: "Popup Create: Unsaved Changes lewat Close, Esc, Popup Kosong, dan Backdrop"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-98
  - TC-AC-SG-99
  - TC-AC-SG-100
  - TC-AC-SG-101
coverage:
  web: automated
---

# Popup Create: Unsaved Changes lewat Close, Esc, Popup Kosong, dan Backdrop

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubah flag itu.
- Data: `Pohon Uji Utama` entitas Principal (Pre-setup #16 dan #17) dibaca saja. Semua popup ditutup tanpa Submit sehingga tidak ada data yang ditulis; nilai ketikan memakai nilai literal TC karena tidak pernah disimpan.
- Jumlah group dasar (N) dibaca dari label root "All Groups (N)"; tidak memakai angka absolut.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah data atau state global.

## Test Steps

1. Catat jumlah group N pada label root "All Groups (N)" di Sidebar Group Tree

### TC-AC-SG-98: Unsaved Changes lewat ikon close

2. Klik `[+] Group` di Sidebar Group Tree
3. Ketik `Draft Group` pada Group Name
4. Klik ikon `[✕]`
5. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` serta `[Leave]`
6. Klik `[Cancel]` pada dialog
7. Verifikasi dialog tertutup
8. Verifikasi popup tetap terbuka dengan input `Draft Group`
9. Klik `[✕]` lagi
10. Verifikasi dialog Unsaved Changes tampil
11. Klik `[Leave]`
12. Verifikasi popup tertutup
13. Verifikasi label root tetap "All Groups (N)" (tanpa membuat group)

### TC-AC-SG-99: Unsaved Changes lewat Esc

14. Klik `[+] Group` di Sidebar Group Tree
15. Ketik `Draft Esc` pada Group Name
16. Tekan Esc
17. Verifikasi dialog Unsaved Changes yang sama tampil: "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]`
18. Klik `[Leave]`

### TC-AC-SG-100: Popup Create kosong tanpa dialog

19. Klik `[+] Group` di Sidebar Group Tree
20. Klik `[✕]` tanpa mengisi apa pun
21. Verifikasi popup tertutup langsung tanpa dialog Unsaved Changes

### TC-AC-SG-101: Klik backdrop tidak menutup popup

22. Klik `[+] Group` di Sidebar Group Tree
23. Ketik `Draft Backdrop` pada Group Name
24. Klik area gelap di luar popup
25. Verifikasi popup tetap terbuka dengan input `Draft Backdrop` dipertahankan
26. Verifikasi dialog Unsaved Changes tidak muncul
27. Klik `[✕]`
28. Verifikasi dialog Unsaved Changes tampil
29. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 1 (baseline jumlah group), langkah 18 dan 29 (menutup popup yang sudah dibuktikan dialognya; Verifikasi dialog pada langkah 17 dan 28 memenuhi S-08).
- Langkah 26 memakai langkah 25 (popup masih tampil) sebagai anchor positif bagi asersi absence dialog (bagian 8b butir 2).
