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

1. Klik nama Warehouse A di tabel (Tab Assets aktif default)
2. Verifikasi Tab Assets aktif
3. Verifikasi kolom default Name, Asset ID, TAG, Brand, Model/Type, Status, Last Updated
4. Verifikasi kolom Measurement, Category, Label, Transactional Policy, Last Scanned, Asset Value, Warranty Expiry, dan Custom Field tersembunyi secara default
5. Verifikasi tidak ada kolom Group
6. Verifikasi tab berisi total 24 aset (22 Active, 1 Draft, 1 Waiting for Approval) sesuai pembacaan fixture BE
7. Verifikasi aset Disposed, aset Deleted, dan 3 aset milik Rack 1 tidak termasuk dalam 24 aset
8. Verifikasi default sort Name A–Z

### TC-FA-GRP-276: Nama aset teks biasa

9. Klik nama aset pertama
10. Verifikasi nama aset tampil sebagai teks biasa (bukan link)
11. Verifikasi klik tidak membuka Asset Detail dan tidak berpindah halaman
12. Tutup popup dengan [X]

### TC-FA-GRP-288: Klik angka Total Asset, himpunan exact-match

13. Klik angka Total Asset (24) pada baris Warehouse A
14. Verifikasi Tab Assets berisi 24 aset (Draft, Waiting for Approval, Active)
15. Verifikasi aset Disposed, aset Deleted, dan aset di Rack 1 tidak termasuk
16. Verifikasi jumlah total aset tab sama dengan angka kolom Total Asset, yaitu 24

### TC-FA-GRP-289: Nama aset teks biasa, read-only, format Name

17. Klik nama aset pertama
18. Verifikasi nama aset teks biasa dan klik tidak membuka Asset Detail
19. Verifikasi Tab Assets tidak memiliki aksi tulis
20. Verifikasi teks Name berformat `[Asset Name] - [Increment]` (mis. `Laptop Dell - 12`)

### TC-FA-GRP-290 dan TC-FA-GRP-987: Status mengikuti Aturan Resolusi Tampilan Status

21. Verifikasi baris aset Active pada halaman 1 menampilkan badge hasil resolusi Custody/Condition sesuai Aturan Resolusi Tampilan Status (`fixed-asset/_foundation/asset-state-machine.md` §6) dengan palette badge platform
22. Klik ikon `Filter`
23. Buka dropdown Status
24. Verifikasi opsi filter Status sama dengan himpunan nilai badge distinct pada data tab sesuai pembacaan fixture BE
25. Pilih Status `Draft`
26. Klik [Apply]
27. Verifikasi baris aset Lifecycle Draft menampilkan badge `Draft`
28. Klik ikon `Filter`
29. Ganti pilihan Status menjadi `Waiting for Approval`
30. Klik [Apply]
31. Verifikasi baris aset Waiting for Approval menampilkan badge `Waiting for Approval`
32. Klik ikon `Filter`
33. Hapus pilihan Status
34. Klik [Apply]
35. Tutup popup dengan [X]

## Notes

- Spec 35 langkah, pada batas sekitar 35 langkah.
- Langkah 21, 24, 27, dan 31 memenuhi Expected TC-FA-GRP-290 dan TC-FA-GRP-987 sekaligus karena kedua TC memuat klausa yang sama (badge Lifecycle Draft dan Waiting for Approval, badge hasil resolusi untuk aset lainnya); opsi filter Status (langkah 24) berasal dari Expected TC-FA-GRP-987 butir c.
- Langkah penghubung (S-03): langkah 12 dan 35 (menutup popup), langkah 22 sampai 26 dan 28 sampai 30 (Filter Status sebagai cara menemukan baris Draft dan Waiting for Approval pada tab 3 halaman, R-16), langkah 32 sampai 34 (membersihkan Filter, S-09).
- Urutan TC dalam spec: 275, 276, 288, 289, 290/987.
- Temuan untuk QA:
  - TC-FA-GRP-275 dan 288 menyebut "24 aset" tanpa cara membaca total pada tab beberapa halaman; spec memakai pembacaan fixture BE untuk himpunan dan jumlah.
  - TC-FA-GRP-290 dan 987 tidak menyebut nama atau halaman aset Draft dan Waiting for Approval; spec menemukannya lewat Filter Status.
  - Opsi Status pada filter tab Assets tidak dirinci TC selain "nilai badge distinct yang tampil".
