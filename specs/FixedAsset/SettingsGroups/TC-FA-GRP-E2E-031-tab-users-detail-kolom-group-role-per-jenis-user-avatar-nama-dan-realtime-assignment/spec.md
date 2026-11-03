---
id: TC-FA-GRP-E2E-031-tab-users-detail-kolom-group-role-per-jenis-user-avatar-nama-dan-realtime-assignment
title: "Tab Users Detail Group: Kolom Group Role per Jenis User, Kolom Name Avatar + Full Name, dan Total User Realtime Setelah Assignment Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-296
  - TC-FA-GRP-299
  - TC-FA-GRP-1011
coverage:
  web: automated
---

# Tab Users Detail Group: Kolom Group Role per Jenis User, Kolom Name Avatar + Full Name, dan Total User Realtime Setelah Assignment Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): pohon group baku Tabel A (Pre-setup No 9): Warehouse A dengan user Total Control, Default User, Read Only, Group Manager, user 1 Group Role (Asset Admin), dan user 2 Group Role (dua role). Email user Total Control, Default User, dan Read Only mengikuti Pre-setup No 1, 2, 3; email Group Manager, user 1, dan user 2 tidak tertulis di Pre-setup TC dan dibaca lewat fixture BE (lihat Temuan untuk QA).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`; node level 1 milik spec, S-06):

| TC | Nama TC | Nama seed | State |
|---|---|---|---|
| TC-FA-GRP-1011 | Warehouse A (user dengan foto, tanpa foto, dan bernama panjang) | `Avatar Node {runId}-031` | Level 1, Assignable, berisi tiga user ber-Group Role: user dengan foto profil `avatarFoto+{runId}-031@qwertysystem.net`, user tanpa foto `avatarTanpaFoto+{runId}-031@qwertysystem.net`, dan user bernama panjang `avatarPanjang+{runId}-031@qwertysystem.net` |
| TC-FA-GRP-299 | Warehouse A (Total User dicatat sebelum uji) | `Realtime Node {runId}-031` | Level 1, Assignable, berisi 1 user ber-Group Role |
| TC-FA-GRP-299 | user baru | `userNew+{runId}-031@qwertysystem.net` | Group Role di-assign ke `Realtime Node {runId}-031` oleh langkah 23 |

- Kemampuan teknis: fixture BE (seeding akun, foto profil, dan assignment; pembacaan himpunan user dan Group Role) dan sesi API aktor yang meng-assign Group Role lewat modul Role & Permission sebagai pemicu state, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-GRP-296: Kolom Group Role per jenis user

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik angka Total User pada baris Warehouse A
3. Verifikasi Group Role user Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` adalah `Total Control`
4. Verifikasi Group Role user Default User `defaultUserGroups_automated_{namaCompany}@qwertysystem.net` adalah `Total Control`
5. Verifikasi Group Role user Read Only `readOnlyGroups_automated_{namaCompany}@qwertysystem.net` adalah `Read Only`
6. Verifikasi Group Role user Group Manager adalah `Group Manager`
7. Verifikasi Group Role user 1 (satu Group Role) adalah nama role `Asset Admin`
8. Verifikasi Group Role user 2 (dua Group Role) adalah `2 roles`
9. Hover nilai `2 roles` pada user 2
10. Verifikasi tidak ada tooltip yang tampil
11. Verifikasi tidak ada baris yang menampilkan `—` pada kolom Group Role
12. Tutup popup dengan [X]

### TC-FA-GRP-1011: Kolom Name avatar + Full Name

13. Ganti isi kotak search dengan `Avatar Node {runId}-031`, tekan Enter
14. Klik angka Total User pada baris `Avatar Node {runId}-031`
15. Verifikasi sel Name berformat `[Avatar] Full Name` dalam satu sel: avatar thumbnail circle (foto dari Settings > User; placeholder generik bila belum upload) diikuti Full Name utuh
16. Verifikasi nama user bernama panjang wrap natural dan tidak dipotong
17. Hover nama user bernama panjang
18. Verifikasi tooltip menampilkan nama lengkap utuh
19. Verifikasi avatar dekoratif dan bukan bagian teks yang dicari Search
20. Tutup popup dengan [X]

### TC-FA-GRP-299: Total User realtime setelah assignment role

21. Ganti isi kotak search dengan `Realtime Node {runId}-031`, tekan Enter
22. Catat angka Total User pada baris `Realtime Node {runId}-031` (N)
23. Assign Group Role user baru `userNew+{runId}-031@qwertysystem.net` ke `Realtime Node {runId}-031` lewat modul Role & Permission (sesi API) hingga tersimpan
24. Muat ulang halaman Settings > Groups dengan F5
25. Ketik Search `Realtime Node {runId}-031`, tekan Enter
26. Verifikasi angka Total User pada baris `Realtime Node {runId}-031` bertambah 1 menjadi N+1
27. Klik node `Realtime Node {runId}-031` di sidebar
28. Verifikasi Total User di header menjadi N+1
29. Klik angka Total User pada header
30. Verifikasi Tab Users berisi N+1 baris, termasuk `userNew+{runId}-031@qwertysystem.net`
31. Tutup popup dengan [X]

## Notes

- Spec 31 langkah, di bawah batas sekitar 35 langkah.
- Langkah penghubung (S-03): langkah 12, 20, 31 (menutup popup), langkah 22 (mencatat baseline), langkah 24 (muat ulang sebagai pengganti "Buka Fixed Asset > Settings > Groups" karena halaman sudah dibuka hook `beforeEach`), langkah 27 (memilih node agar header tampil). Langkah 1, 13, 21, dan 25 (Ketik Search `Warehouse A`, ganti isi kotak search dengan `Avatar Node {runId}-031` dan `Realtime Node {runId}-031`, serta Ketik Search `Realtime Node {runId}-031` sesudah F5 yang menutup kotak Search) menemukan baris target karena client punya lebih dari 10 node level 1 dengan page size 10, sehingga baris tidak diandalkan berada di halaman 1; Search tetap aktif selama popup dibuka dan ditutup (R-16).
- Pemicu pelaku kedua lewat sesi API ditulis "... hingga ... tersimpan" (R-20); bukan konteks kedua (P-2 `[KEPUTUSAN 2026-10-30]`).
- Urutan TC dalam spec: 296, 1011, 299 (assignment yang mengubah data paling akhir, S-10).
- Temuan untuk QA:
  - TC-FA-GRP-296 menyebut user Group Manager, user 1, dan user 2 tanpa email; identitasnya dibaca lewat fixture BE.
  - TC-FA-GRP-1011 menyebut user dengan foto, tanpa foto, dan bernama panjang pada Warehouse A tanpa daftar di Pre-setup; spec men-seed node milik spec berisi ketiganya.
  - TC-FA-GRP-1011 butir d ("avatar dekoratif dan bukan bagian teks yang dicari Search") tidak menyebut cara cek; spec mengasersi atribut dekoratif avatar sesuai Expected.
  - TC-FA-GRP-299 memakai Warehouse A untuk assignment; spec memakai node milik spec agar Total User Warehouse A tidak berubah.
