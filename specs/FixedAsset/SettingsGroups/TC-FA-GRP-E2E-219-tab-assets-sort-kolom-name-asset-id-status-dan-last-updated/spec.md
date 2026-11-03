---
id: TC-FA-GRP-E2E-219-tab-assets-sort-kolom-name-asset-id-status-dan-last-updated
title: "Tab Assets Sort Kolom Name, Asset ID, Status, dan Last Updated (Asc, Desc, Netral)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-695
  - TC-FA-GRP-696
  - TC-FA-GRP-697
  - TC-FA-GRP-698
coverage:
  web: automated
---

# Tab Assets Sort Kolom Name, Asset ID, Status, dan Last Updated (Asc, Desc, Netral)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`) berlaku: login default, flag Guided Tooltip `seen`, sesi API aktor, klien HTTP, dan fixture BE disediakan tim FE/BE.
- Data Pre-setup (hanya dibaca, tidak diubah): Warehouse A (Tabel A No 9: 24 aset aktif variasi status + 2 Disposed). Nilai variasi (Name, Asset ID, Status, Brand, Model/Type, Category, Last Updated; sedikitnya dua nilai distinct per kolom yang dipakai Search, Filter, dan Sort, S-11) dan nilai fixture acuan `Fixture.settingsGroups.<kunci>` disediakan tim FE/BE; Tabel Data Uji TC tidak memuat nilai konkret (lihat Temuan untuk QA).
- Data variasi sort: kolom Name, Asset ID, dan Status memuat nilai huruf besar dan kecil, angka, dan kosong; aset bernama sama dengan Increment 2 dan 10 (`Laptop Dell - 2`, `Laptop Dell - 10`); kolom Last Updated memuat sedikitnya dua nilai distinct (S-11).

## Test Steps
1. Ketik Search `Warehouse A`, tekan Enter
2. Klik angka Total Asset Warehouse A untuk membuka Popup Detail Group, Tab Assets

### TC-FA-GRP-695: Sort kolom Name

3. Pastikan kolom Name tampil
4. Klik header Name 1x
5. Verifikasi urutan Ascending A→Z case-insensitive menurut nama aset (mis. anggur sebelum Apel)
6. Verifikasi nama aset sama diurutkan menurut Increment numerik natural (`Laptop Dell - 2` sebelum `Laptop Dell - 10`)
7. Klik header Name untuk kedua kali
8. Verifikasi urutan Descending Z→A
9. Klik header Name untuk ketiga kali
10. Verifikasi urutan kembali ke default tabel (Name A→Z)

### TC-FA-GRP-696: Sort kolom Asset ID

11. Pastikan kolom Asset ID tampil
12. Klik header Asset ID 1x
13. Verifikasi urutan Ascending A→Z case-insensitive (mis. anggur sebelum Apel)
14. Klik header Asset ID untuk kedua kali
15. Verifikasi urutan Descending Z→A
16. Klik header Asset ID untuk ketiga kali
17. Verifikasi urutan kembali ke default tabel (Name A→Z)

### TC-FA-GRP-697: Sort kolom Status

18. Pastikan kolom Status tampil
19. Klik header Status 1x
20. Verifikasi urutan Ascending A→Z berdasarkan label
21. Klik header Status untuk kedua kali
22. Verifikasi urutan Descending Z→A
23. Klik header Status untuk ketiga kali
24. Verifikasi urutan kembali ke default tabel (Name A→Z)

### TC-FA-GRP-698: Sort kolom Last Updated

25. Pastikan kolom Last Updated tampil
26. Klik header Last Updated 1x
27. Verifikasi urutan Oldest First
28. Klik header Last Updated untuk kedua kali
29. Verifikasi urutan Newest First
30. Klik header Last Updated untuk ketiga kali
31. Verifikasi urutan kembali ke default tabel (Name A→Z)

## Notes

- Langkah penghubung (S-03): langkah 2 membuka Popup Detail Group Tab Assets; langkah "Pastikan kolom tampil" adalah aksi tanpa asersi dari langkah TC; sort kembali netral pada klik ketiga sehingga tidak perlu pemulihan antar-blok (S-09).
- Spec memuat 4 blok Sort satu kelas harness dan satu dataset Warehouse A; tiap blok berdiri sendiri dan polanya sama per kolom.
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA:
  - TC-695 sampai 698: Expected "default tabel (Name A→Z)" dipakai sebagai urutan netral; kolom Name sendiri pada klik ketiga kembali ke urutan yang sama dengan Ascending.
  - TC-696 dan TC-697: data uji "nilai kosong" untuk kolom Asset ID dan Status tidak dijelaskan penempatannya dalam urutan.
