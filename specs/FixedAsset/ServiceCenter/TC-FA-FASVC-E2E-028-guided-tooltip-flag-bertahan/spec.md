---
id: TC-FA-FASVC-E2E-028-guided-tooltip-flag-bertahan
title: "Guided Tooltip: Muncul di Kunjungan Pertama dan Flag Bertahan Antar Sesi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-TBL-10"]
smoke: []
dependsOn: []
trace:
  "EB-TBL-10": [3, 5, 7, 9, 10, 14, 15, 17, 19, 21, 24, 25, 29]
anchor: []
coverage:
  web: automated
---

# Guided Tooltip: Muncul di Kunjungan Pertama dan Flag Bertahan Antar Sesi

## Prerequisites
- Aktor: Total Control `Bayu Tur {runId}` dan Total Control `Citra Tur {runId}`; keduanya belum pernah membuka halaman daftar Service Center (flag `guided_tooltip_seen_fams-service-center-list` belum tersetel).
- Layar awal: halaman login.
- Data:
  - DU-028-1: User `Bayu Tur {runId}`, role Total Control, Status `Active`, flag Guided Tooltip halaman daftar Service Center belum tersetel.
  - DU-028-2: User `Citra Tur {runId}`, role Total Control, Status `Active`, flag Guided Tooltip halaman daftar Service Center belum tersetel.
  - DU-028-3: Service Center `Bengkel Tur {runId}`, Service type `Routine`, Available to `Cabang Tur {runId}`, City `Kota Tur {runId}`, Usage `0`, Status `Active`, Company email `tur@bengkeltur.example`.
  - DU-028-4: Group `Cabang Tur {runId}`, anak langsung dari root pohon Group.
- Kondisi: client memiliki lisensi addon Maintenance berstatus aktif. Setup Column kedua akun memakai konfigurasi bawaan (kolom `Available To` dan `Usage` tampil).

## Test Steps

### Kunjungan pertama menampilkan Guided Tooltip otomatis, dan keluar tanpa selesai tidak menyetel flag
1. Masuk sebagai `Bayu Tur {runId}`
2. Buka Add-ons > Service Center
3. Verifikasi Guided Tooltip step 1 tampil otomatis dengan judul `Add your vendors`
4. Muat ulang halaman Service Center
5. Verifikasi Guided Tooltip step 1 tampil lagi dengan judul `Add your vendors`, karena walkthrough sebelumnya ditutup tanpa Skip atau Done

### Skip menyetel flag dan Guided Tooltip tidak muncul lagi di sesi login berikutnya
6. Klik `[Skip]`
7. Verifikasi halaman daftar Service Center tampil dengan tombol `[?]` di sebelah Breadcrumb
8. Muat ulang halaman Service Center
9. Verifikasi tombol `[+ Service Center]` tampil pada toolbar daftar
10. Verifikasi Guided Tooltip tidak tampil sesudah muat ulang
11. Keluar dari akun `Bayu Tur {runId}`
12. Masuk sebagai `Bayu Tur {runId}`
13. Buka Add-ons > Service Center
14. Verifikasi tombol `[+ Service Center]` tampil pada toolbar daftar
15. Verifikasi Guided Tooltip tidak tampil di sesi login baru

### Replay lewat tombol [?] memutar ulang dari step 1 tanpa mereset flag
16. Klik `[?]` di sebelah Breadcrumb
17. Verifikasi Guided Tooltip step 1 tampil dengan judul `Add your vendors`
18. Klik `[Next]`
19. Verifikasi Guided Tooltip step 2 tampil dengan judul `Choose where they work`
20. Klik `[Next]`
21. Verifikasi Guided Tooltip step 3 tampil dengan judul `See where it's used`
22. Klik `[Done]`
23. Muat ulang halaman Service Center
24. Verifikasi tombol `[+ Service Center]` tampil pada toolbar daftar
25. Verifikasi Guided Tooltip tidak tampil sesudah replay selesai, karena flag tidak direset

### Flag disimpan per user: user lain tetap melihat Guided Tooltip di kunjungan pertamanya
26. Keluar dari akun `Bayu Tur {runId}`
27. Masuk sebagai `Citra Tur {runId}`
28. Buka Add-ons > Service Center
29. Verifikasi Guided Tooltip step 1 tampil otomatis dengan judul `Add your vendors`