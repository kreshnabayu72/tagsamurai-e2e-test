---
id: TC-FA-GRP-E2E-275-tab-assets-gerbang-no-access-sort-filter-dan-search-aktor-tanpa-hak-bergerbang
title: "Tab Assets Gerbang No Access: Baris No Access Tetap Paling Akhir pada Sort, Tidak Cocok dengan Filter, dan Teks No Access Tidak Dicocokkan Search"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-1244
  - TC-FA-GRP-1245
  - TC-FA-GRP-1246
coverage:
  web: automated
---

# Tab Assets Gerbang No Access: Baris No Access Tetap Paling Akhir pada Sort, Tidak Cocok dengan Filter, dan Teks No Access Tidak Dicocokkan Search

## Prerequisites

- Mode: FE+BE.
- Hook suite: rujuk `suite.md` (login API aktor, sesi API, fixture BE, flag Guided Tooltip `fa-settings-groups` bernilai `seen`).
- Akun aktor: noValueAccess (Pre-setup No 16: Manage Group R pada node yang sama dengan No 12; tanpa View asset value, Manage purchase, maupun Manage accounting) `noValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_NOVALUEACCESS_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup tambahan (hanya dibaca): Value Gate Node A (Tabel Dinamis No 10, aset G1-G6) dengan audit scan (No 15: pemindaian terbaru G3 01/09/2026, G1 10/10/2026, G5 20/10/2026; G2, G4, G6 belum pernah dipindai). Node di-seed idempotent di hook `before` dengan nama bersuffix `{runId}-275` (mekanisme seeding disediakan tim FE/BE). Langkah dan asersi memakai nama bersuffix itu. Seluruh baris tabel ini `No access` pada kolom bergerbang karena hak diperiksa per group aset. Nilai asli di server: Asset Value G1 = 1500, Warranty Expiry G1 = 15/03/2027.
- Kolom sort pada TC-1244 (iterasi "Untuk setiap baris tabel"):

| Kolom sort |
|---|
| Asset Value |
| Warranty Expiry |

- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (kondisi awal client uji; spec tidak mengubahnya).
- Setup Column: hook `before` menghapus preferensi kolom Tab Assets di browser; hook `after` menghapus preferensi yang disimpan spec (kemampuan disediakan tim FE). Antar TC, konfigurasi dikembalikan dengan [Reset to Default] lalu [Save] sebagai langkah penghubung.
- State global: tidak ada yang diubah.

## Test Steps

### TC-1244: Sort kolom bergerbang berisi `No access`: baris `No access` tetap paling akhir pada Asc dan Desc
1. Ketik Search `Value Gate Node A {runId}-275` pada Groups List, tekan Enter
2. Buka Detail Value Gate Node A (Tab Assets)
3. Buka Popup Setup Column, centang kolom Asset Value dan Warranty Expiry, klik [Save]
4. Untuk setiap baris tabel "Kolom sort" pada Prerequisites (langkah 5 sampai 13):
5. Klik header kolom sort (Asc)
6. Verifikasi semua 6 baris tampil dengan sel kolom itu `No access`
7. Verifikasi tidak ada baris bernilai atau `—` yang ditempatkan setelah baris `No access`
8. Klik header kolom sort lagi (Desc)
9. Verifikasi semua 6 baris tampil dengan sel kolom itu `No access`
10. Verifikasi tidak ada baris bernilai atau `—` yang ditempatkan setelah baris `No access`
11. Klik header kolom sort lagi (Netral)
12. Verifikasi tidak ada baris hilang (6 baris tampil)
13. Verifikasi urutan kembali ke default tabel (Name A-Z)
### TC-1245: Filter kolom bergerbang: baris `No access` tidak cocok dengan filter apa pun
14. Buka Popup Setup Column, klik [Reset to Default], klik [Save]
15. Buka Popup Setup Column, centang kolom Asset Value, Warranty Expiry, dan Last Scanned, klik [Save]
16. Klik icon Filter; pada field Asset Value isi Min 0, Max 99999, klik [Apply]
17. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter."
18. Klik icon Filter
19. Klik [Clear Field]; pada field Warranty Expiry pilih rentang 01/01/2020-31/12/2035, klik [Apply]
20. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter."
21. Klik icon Filter
22. Klik [Clear Field]; pada field Last Scanned pilih rentang 01/01/2020-31/12/2035, klik [Apply]
23. Verifikasi G1, G3, dan G5 tampil (kontrol: Last Scanned tidak bergerbang)
24. Klik icon Filter
25. Klik [Clear Field]
26. Klik [Apply]
### TC-1246: Search: teks `No access` dan nilai tersembunyi tidak dicocokkan
27. Buka Popup Setup Column, klik [Reset to Default], klik [Save]
28. Buka Popup Setup Column, centang kolom Asset Value dan Warranty Expiry, klik [Save]
29. Ketik Search `No access`, tekan Enter
30. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter." (teks `No access` tidak dicari)
31. Ganti isi kotak search dengan `1500`, tekan Enter
32. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter."
33. Ganti isi kotak search dengan `2027`, tekan Enter
34. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter." (nilai Asset Value dan Warranty Expiry tidak diterima dan tidak dicari)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Iterasi (8b butir 7): pada TC-1244 langkah 5 sampai 13 diulang untuk tiap baris tabel "Kolom sort" (2 iterasi, 9 langkah per iterasi). Parameter hanya nama kolom; tidak ada langkah bersyarat.
- Langkah penghubung (S-03): [Reset to Default] + [Save] membuka TC-1245 dan TC-1246 (S-09); [Clear Field] terakhir TC-1245.
- Asersi absence (empty state "No results found") pada TC-1245 dan TC-1246 memakai empty state sebagai anchor positif hasil Filter/Search (8b butir 2); kontrol Last Scanned (G1, G3, G5 tampil) membuktikan filter berfungsi.
- Alasan di atas ~35 langkah (ekspansi ±43): satu kelas (fungsional gerbang No Access), satu dataset (Value Gate Node A), tiap TC berdiri sendiri, dan sort diulang per kolom dari tabel Prerequisites.
- Langkah penghubung (S-03, S-09, S-14, A-9): `Klik icon Filter` sebelum tiap `[Clear Field]` yang jatuh sesudah `[Apply]`, dan `[Apply]` sesudah `[Clear Field]` terakhir TC-1245 supaya filter Last Scanned tidak masih aktif saat TC-1246 mulai.
- Langkah penghubung (S-03, S-14, R-16): sebelum tiap `Buka Detail` ditambahkan Search Groups List dengan nama group target (`Value Gate Node A {runId}-275`), karena client memiliki lebih dari 10 node level 1 dan page size 10 sehingga baris target tidak dijamin berada di halaman 1; Search hilang setelah F5, login, atau buka ulang halaman Groups sehingga dipasang lagi.
- Temuan untuk QA:
  - TC-1244 menyebut "klik header lagi (Netral)" tanpa menyatakan urutan G1-G6 default; spec memakai "Name A-Z" sesuai Expected b.
  - TC-1246 Expected b: "nilai Asset Value dan Warranty tidak diterima" tidak menjelaskan arti "tidak diterima"; hanya empty state yang diasersi.
