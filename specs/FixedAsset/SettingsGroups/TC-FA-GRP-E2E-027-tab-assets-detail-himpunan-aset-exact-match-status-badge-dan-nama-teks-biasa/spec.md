---
id: TC-FA-GRP-E2E-027-tab-assets-detail-himpunan-aset-exact-match-status-badge-dan-nama-teks-biasa
title: "Tab Assets Detail Group: Himpunan Aset Exact-Match Belum Disposed/Deleted, Status Aturan Resolusi, dan Nama Aset Teks Biasa"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-275
  - TC-FA-GRP-276
  - TC-FA-GRP-288
  - TC-FA-GRP-289
  - TC-FA-GRP-290
  - TC-FA-GRP-987
coverage:
  web: automated
---

# Tab Assets Detail Group: Himpunan Aset Exact-Match Belum Disposed/Deleted, Status Aturan Resolusi, dan Nama Aset Teks Biasa

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): pohon group baku Tabel A (Pre-setup No 9) dengan Warehouse A (Assignable): 22 aset Active (Custody/Condition bervariasi), 1 Draft, 1 Waiting for Approval, 2 Disposed, dan 1 Deleted; child Rack 1 punya 3 aset. Tab Assets Warehouse A menampilkan 24 aset (22 Active, 1 Draft, 1 Waiting for Approval). Spec ini tidak menjalankan aksi tulis.
- Ukuran halaman tab 10 baris per halaman (default). Jumlah total dan himpunan nilai Status distinct dibaca lewat fixture BE.
- Kemampuan teknis: fixture BE (pembacaan himpunan aset dan nilai Status Warehouse A) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-GRP-275: Tab Assets via Detail, himpunan exact-match

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik nama Warehouse A di tabel (Tab Assets aktif default)
3. Verifikasi Tab Assets aktif
4. Verifikasi kolom default Name, Asset ID, TAG, Brand, Model/Type, Status, Last Updated
5. Verifikasi kolom Measurement, Category, Label, Transactional Policy, Last Scanned, Asset Value, Warranty Expiry, dan Custom Field tersembunyi secara default
6. Verifikasi tidak ada kolom Group
7. Verifikasi tab berisi total 24 aset (22 Active, 1 Draft, 1 Waiting for Approval) sesuai pembacaan fixture BE
8. Verifikasi aset Disposed, aset Deleted, dan 3 aset milik Rack 1 tidak termasuk dalam 24 aset
9. Verifikasi default sort Name A–Z

### TC-FA-GRP-276: Nama aset teks biasa

10. Klik nama aset pertama
11. Verifikasi nama aset tampil sebagai teks biasa (bukan link)
12. Verifikasi klik tidak membuka Asset Detail dan tidak berpindah halaman
13. Tutup popup dengan [X]

### TC-FA-GRP-288: Klik angka Total Asset, himpunan exact-match

14. Klik angka Total Asset (24) pada baris Warehouse A
15. Verifikasi Tab Assets berisi 24 aset (Draft, Waiting for Approval, Active)
16. Verifikasi aset Disposed, aset Deleted, dan aset di Rack 1 tidak termasuk
17. Verifikasi jumlah total aset tab sama dengan angka kolom Total Asset, yaitu 24

### TC-FA-GRP-289: Nama aset teks biasa, read-only, format Name

18. Klik nama aset pertama
19. Verifikasi nama aset teks biasa dan klik tidak membuka Asset Detail
20. Verifikasi Tab Assets tidak memiliki aksi tulis
21. Verifikasi teks Name berformat `[Asset Name] - [Increment]` (mis. `Laptop Dell - 12`)

### TC-FA-GRP-290 dan TC-FA-GRP-987: Status mengikuti Aturan Resolusi Tampilan Status

22. Verifikasi baris aset Active pada halaman 1 menampilkan badge hasil resolusi Custody/Condition sesuai Aturan Resolusi Tampilan Status (`fixed-asset/_foundation/asset-state-machine.md` §6) dengan palette badge platform
23. Klik ikon `Filter`
24. Buka dropdown Status
25. Verifikasi opsi filter Status sama dengan himpunan nilai badge distinct pada data tab sesuai pembacaan fixture BE
26. Pilih Status `Draft`
27. Klik [Apply]
28. Verifikasi baris aset Lifecycle Draft menampilkan badge `Draft`
29. Klik ikon `Filter`
30. Ganti pilihan Status menjadi `Waiting for Approval`
31. Klik [Apply]
32. Verifikasi baris aset Waiting for Approval menampilkan badge `Waiting for Approval`
33. Klik ikon `Filter`
34. Hapus pilihan Status
35. Klik [Apply]
36. Tutup popup dengan [X]

## Notes

- Spec 36 langkah, melewati sekitar 35 langkah hanya oleh satu langkah Search penemu baris: seluruh blok adalah satu kelas (Tab Assets Warehouse A) pada dataset yang sama, tiap blok berdiri sendiri, dan memisahkannya hanya menggandakan login, hook, dan cleanup tanpa alur baru.
- Langkah 2 (Ketik Search `Warehouse A`, tekan Enter) menemukan baris target karena client punya lebih dari 10 node level 1 dengan page size 10, sehingga baris tidak diandalkan berada di halaman 1; Search tetap aktif untuk klik angka Total Asset pada langkah 14 (R-16).
- Langkah 22, 25, 28, dan 31 memenuhi Expected TC-FA-GRP-290 dan TC-FA-GRP-987 sekaligus karena kedua TC memuat klausa yang sama (badge Lifecycle Draft dan Waiting for Approval, badge hasil resolusi untuk aset lainnya); opsi filter Status (langkah 25) berasal dari Expected TC-FA-GRP-987 butir c.
- Langkah penghubung (S-03): langkah 13 dan 36 (menutup popup), langkah 23 sampai 27 dan 29 sampai 31 (Filter Status sebagai cara menemukan baris Draft dan Waiting for Approval pada tab 3 halaman, R-16), langkah 33 sampai 35 (membersihkan Filter, S-09).
- Urutan TC dalam spec: 275, 276, 288, 289, 290/987.
- Temuan untuk QA:
  - TC-FA-GRP-275 dan 288 menyebut "24 aset" tanpa cara membaca total pada tab beberapa halaman; spec memakai pembacaan fixture BE untuk himpunan dan jumlah.
  - TC-FA-GRP-290 dan 987 tidak menyebut nama atau halaman aset Draft dan Waiting for Approval; spec menemukannya lewat Filter Status.
  - Opsi Status pada filter tab Assets tidak dirinci TC selain "nilai badge distinct yang tampil".
