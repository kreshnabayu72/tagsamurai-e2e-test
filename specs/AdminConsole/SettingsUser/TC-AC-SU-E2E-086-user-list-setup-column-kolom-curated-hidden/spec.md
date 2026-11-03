---
id: TC-AC-SU-E2E-086-user-list-setup-column-kolom-curated-hidden
title: "User List Setup Column: Kolom Curated Hidden (Ceklis, Drag Reorder, Pin dan Unpin)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-308
  - TC-AC-SU-309
  - TC-AC-SU-310
coverage:
  web: automated
---

# User List Setup Column: Kolom Curated Hidden (Ceklis, Drag Reorder, Pin dan Unpin)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-086`): `John Doe {runId}-086` (Active, Activated, Temporary User `No`, TAG `E2801{runId}`, Office Location `Jakarta HQ`; dipakai sebagai precondition TC, tidak diasersi).
- Viewport: lebar 1280px diatur oleh langkah 20 (awal TC-310) agar tabel dapat di-scroll horizontal, dan dipulihkan ke ukuran semula oleh langkah 36 serta hook `after`.
- Kolom curated hidden: Activation Status, Temporary User, Temporary Until, TAG, Office Location (Custom Field Pre-setup `Office Location` berstatus Active, Pre-setup #10).
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.
- Pemulihan Setup Column: preferensi kolom yang disimpan spec ini dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.

## Test Steps

### TC-AC-SU-308: Setup Column ceklis dan unceklis kelas curated hidden

1. Klik `⋯` pada header Actions
2. Klik `[Setup Column]`
3. Centang kolom Activation Status, Temporary User, Temporary Until, TAG, dan Office Location satu per satu
4. Verifikasi Live Preview memuat kolom Activation Status, Temporary User, Temporary Until, TAG, dan Office Location
5. Klik `[Save]`
6. Verifikasi tabel memuat kolom Activation Status, Temporary User, Temporary Until, TAG, dan Office Location
7. Tekan F5
8. Verifikasi konfigurasi bertahan: tabel tetap memuat kolom Activation Status, Temporary User, Temporary Until, TAG, dan Office Location
9. Klik `⋯` pada header Actions, klik `[Setup Column]`, klik `[Reset to Default]`, klik `[Save]`

### TC-AC-SU-309: Setup Column drag reorder kelas curated hidden

10. Klik `⋯` pada header Actions
11. Klik `[Setup Column]`
12. Centang kolom Activation Status, Temporary User, Temporary Until, TAG, dan Office Location
13. Drag tiap kolom curated ke posisi lain sehingga urutannya menjadi: Office Location, TAG, Temporary Until, Temporary User, Activation Status
14. Verifikasi urutan baru tampil di Live Preview
15. Klik `[Save]`
16. Verifikasi urutan baru tampil di tabel
17. Tekan F5
18. Verifikasi urutan baru bertahan di tabel
19. Klik `⋯` pada header Actions, klik `[Setup Column]`, klik `[Reset to Default]`, klik `[Save]`

### TC-AC-SU-310: Setup Column pin dan unpin kelas curated hidden

20. Atur lebar viewport menjadi 1280px sehingga tabel dapat di-scroll horizontal
21. Klik `⋯` pada header Actions
22. Klik `[Setup Column]`
23. Centang kolom Activation Status, Temporary User, Temporary Until, TAG, dan Office Location
24. Klik icon Pin pada kolom Activation Status, Temporary User, Temporary Until, TAG, dan Office Location satu per satu
25. Klik `[Save]`
26. Scroll tabel secara horizontal
27. Verifikasi kolom ter-pin tetap terlihat saat tabel di-scroll
28. Tekan F5
29. Scroll tabel secara horizontal
30. Verifikasi pin bertahan setelah F5
31. Klik `⋯` pada header Actions, klik `[Setup Column]`
32. Klik icon Pin (unpin) pada kolom yang ter-pin satu per satu, klik `[Save]`
33. Scroll tabel secara horizontal
34. Verifikasi kolom ikut ter-scroll setelah unpin
35. Klik `⋯` pada header Actions, klik `[Setup Column]`, klik `[Reset to Default]`, klik `[Save]`
36. Pulihkan lebar viewport ke ukuran semula

## Notes

- Langkah penghubung (S-03): langkah 20 mengatur lebar viewport dan langkah 36 memulihkannya; `[Reset to Default]` lalu `[Save]` di akhir tiap TC mengembalikan konfigurasi kolom (S-09); pemulihan lain oleh hook `after`.
- Pengulangan per kolom ditulis sebagai satu langkah daftar kolom (aksi identik per kolom); `Verifikasi` Live Preview dan tabel menyebut seluruh kolom sebagai daftar elemen yang sama.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-086` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-308 sampai TC-310 menyebut "(untuk kelas default visible, sisakan Name)" pada langkah yang berlaku untuk kelas lain; spec tidak menyisakan kolom karena hanya kolom curated yang dicentang.
  - TC-309 dan TC-310 tidak menyebut urutan tujuan drag; spec memakai urutan terbalik dari urutan centang.
- Jumlah langkah 36 (di atas smell 35 langkah): pengulangan per kolom sudah ditulis sebagai satu langkah daftar kolom; langkah 20 dan 36 (atur dan pulihkan viewport) adalah langkah penghubung tanpa `Verifikasi`. TC sumber berbagi permukaan Setup Column dan konfigurasi kolom yang sama, sehingga pemecahan menggandakan seeding dan pembentukan state kolom.
