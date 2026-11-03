---
id: TC-FA-GRP-E2E-006-sidebar-group-tree-toggle-open-collapse-persisten-responsif-dan-label-panjang
title: "Sidebar Group Tree: Expand/Collapse All, Toggle Open/Collapse, State Persisten, Collapse Otomatis di Bawah 1280px, dan Label 120 Karakter"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-12
  - TC-FA-GRP-13
  - TC-FA-GRP-1085
  - TC-FA-GRP-1092
  - TC-FA-GRP-1093
coverage:
  web: automated
---

# Sidebar Group Tree: Expand/Collapse All, Toggle Open/Collapse, State Persisten, Collapse Otomatis di Bawah 1280px, dan Label 120 Karakter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- State awal sidebar: preferensi Open/Collapse sidebar untuk akun aktor belum tersimpan (kunjungan pertama, TC-FA-GRP-1085). Kemampuan menghapus preferensi itu disediakan tim FE dan dijalankan di hook `before` serta `after` spec ini; Mekanisme penyimpanan preferensi tidak disebut TC (lihat Temuan untuk QA).
- Data Pre-setup (hanya dibaca): pohon group baku Tabel A (Pre-setup No 9), termasuk Head Office > Floor 2 > IT Department > Server Room.
- Data Dinamis (di-seed di hook `before`, dihapus di hook `after`):

| TC | Nama TC | Nama seed | Keterangan |
|---|---|---|---|
| TC-FA-GRP-1093 | group bernama 120 karakter (Tabel B TC) | `Aa-{runId}-006-` dilengkapi huruf `a` sampai tepat 120 karakter termasuk suffix | Level 1, Function None |

- Lebar viewport awal 1440px; langkah mengubah lebar viewport dan memulihkannya ke 1440px.
- Kemampuan teknis: fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global selain preferensi sidebar akun aktor yang dipulihkan di hook `after`.

## Test Steps

### TC-FA-GRP-1085: Toggle Open/Collapse, kunjungan pertama

1. Verifikasi sidebar dalam state Open pada kunjungan pertama
2. Verifikasi toggle mengambang di tepi kiri panel, berwarna Primary, dengan ikon ▶ (ArrowRightSLine)
3. Hover toggle
4. Verifikasi tooltip dan aria-label toggle `Collapse Group Tree`
5. Klik toggle
6. Verifikasi sidebar tertutup
7. Verifikasi area konten melebar penuh
8. Verifikasi toggle berpindah ke tepi kanan layar dengan ikon ◀ (ArrowLeftSLine)
9. Hover toggle
10. Verifikasi tooltip dan aria-label toggle `Open Group Tree`
11. Klik toggle
12. Verifikasi sidebar terbuka kembali dengan toggle di tepi kiri panel dan ikon ▶

### TC-FA-GRP-12: Toggle expand/collapse-all

13. Klik toggle expand-all
14. Verifikasi seluruh level tree terbuka (Head Office, Floor 2, IT Department, Server Room tampil)
15. Klik toggle collapse-all
16. Verifikasi tree tertutup kembali ke level 1 (Floor 2 tidak tampil)

### TC-FA-GRP-13: State sidebar persisten setelah refresh

17. Klik toggle Open/Collapse untuk menutup sidebar
18. Verifikasi sidebar tertutup
19. Muat ulang halaman dengan F5
20. Verifikasi sidebar tetap tertutup setelah F5
21. Klik toggle Open/Collapse untuk membuka sidebar

### TC-FA-GRP-1092: Collapse otomatis di bawah 1280px

22. Verifikasi sidebar Open pada lebar viewport 1440px (preferensi tersimpan Open)
23. Ubah lebar viewport ke 1024px
24. Verifikasi sidebar tersembunyi sementara (collapse otomatis)
25. Ubah lebar viewport kembali ke 1440px
26. Verifikasi sidebar Open kembali sesuai preferensi tersimpan

### TC-FA-GRP-1093: Label node 120 karakter

27. Verifikasi label node group 120 karakter ter-render dalam lebar sidebar
28. Verifikasi panel sidebar tidak memiliki scroll horizontal
29. Hover node group 120 karakter
30. Verifikasi tooltip berisi nama lengkap 120 karakter secara utuh

## Notes

- Langkah penghubung (S-03): langkah 15 (collapse-all agar tree kembali ke level 1), langkah 21 (membuka sidebar kembali agar TC-FA-GRP-1092 memakai preferensi Open, S-09).
- Urutan TC dalam spec: 1085, 12, 13, 1092, 1093. TC-FA-GRP-1085 pertama karena membutuhkan kunjungan pertama tanpa preferensi tersimpan; pada langkah 12 sidebar kembali Open sehingga preferensi tersimpan Open, yang menjadi precondition TC-FA-GRP-1092.
- Temuan untuk QA:
  - TC-FA-GRP-1085 menyebut "preferensi sidebar belum pernah tersimpan" tanpa cara menghapusnya atau tempat penyimpanannya; spec memakai kemampuan yang disediakan tim FE (S-13).
  - TC-FA-GRP-1093 menyebut group 120 karakter pada Tabel B, tetapi Tabel Data Uji Dinamis TC tidak memuat baris itu; spec memakai seed bersuffix (S-12).
  - TC-FA-GRP-1092 tidak menyebut tinggi viewport; spec hanya mengubah lebar.
