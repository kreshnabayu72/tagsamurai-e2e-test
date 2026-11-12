---
id: TC-FA-GRP-E2E-309-tab-assets-sel-asset-value-pending-search-filter-dan-download-dua-kolom
title: "Tab Assets Sel Asset Value Pending pada Kedua Kolom Buku: Filter, Search Teks Pending Tidak Cocok, dan Download Menulis Kosong"
priority: High
caseType: Boundary
status: draft
sourceTc:
  - TC-FA-GRP-1306
coverage:
  web: automated
---

# Tab Assets Sel Asset Value Pending pada Kedua Kolom Buku: Filter, Search Teks Pending Tidak Cocok, dan Download Menulis Kosong

## Prerequisites

- Mode: FE+BE.
- Akun viewAssetValueGroups (Pre-setup No 12; Group Role View asset value pada Value Gate Node A): `viewAssetValueGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_VIEWASSETVALUE_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`) berlaku: sesi API aktor, fixture BE, flag Guided Tooltip `seen`, dan pemulihan state global; tidak ditulis ulang di sini.
- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (dibaca; tidak diubah).
- Data Value Gate Node A (Tabel Dinamis No 10, hanya dibaca, tidak diubah): G1 `Laptop Dell - 1`, G2 `Printer HP - 1`, G3 `Monitor LG - 1`, G4 `Forklift Toyota - 1`, G5 `Kabel Roll - 1`, G6 `Laptop Dell - 2`. Asset Value (Commercial): G1 1500, G2 0, G3 belum ada (`Pending`), G4 8000, G5 120, G6 2300. Asset Value (Fiscal): G1 1200, G2 500, G3 belum ada (`Pending`), G4 7000, G5 150, G6 2000. Buku Commercial dan Fiscal (Tabel Dinamis No 20).
- Kemampuan teknis: membaca isi berkas unduhan CSV (nilai sel, sel kosong, header kolom) disediakan tim FE; asersi berkas memakai kemampuan itu. Menghapus preferensi kolom Setup Column di browser (disediakan tim FE).
- Preferensi kolom Setup Column yang disimpan spec ini dihapus dari browser di hook `after` (kemampuan disediakan tim FE).
- State global: tidak ada yang diubah. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1306: Sel Asset Value Pending pada kedua kolom buku: Search teks Pending tidak cocok dan Download menulis kosong

1. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
2. Buka Detail Value Gate Node A (Tab Assets)
3. Buka Popup Setup Column
4. Centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, klik [Save]
5. Klik icon Filter
6. Isi field `Asset Value (Fiscal)` Min 0 dan Max 99999, klik [Apply]
7. Verifikasi G1, G2, G4, G5, G6 tampil; G3 (`Pending`) tidak tampil
8. Klik icon Filter
9. Klik [Clear Field], klik [Apply]
10. Ketik Search `Pending`, tekan Enter
11. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter." (sel `Pending` tidak cocok teksnya)
12. Klik `(←)` pada kotak Search
13. Klik icon Download
14. Pilih Download as CSV
15. Buka berkas
16. Verifikasi kolom `Asset Value (Commercial)`: G1 = `1500`, G2 = `0`, G4 = `8000`, G5 = `120`, G6 = `2300`
17. Verifikasi kolom `Asset Value (Fiscal)`: G1 = `1200`, G2 = `500`, G4 = `7000`, G5 = `150`, G6 = `2000`
18. Verifikasi G3 pada kedua kolom ditulis kosong (bukan `-`, bukan teks `Pending`)
19. Buka Popup Setup Column, hilangkan centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, klik [Save]

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): menghilangkan centang kedua kolom di akhir agar kolom tidak tersimpan; `Klik icon Filter` sebelum `[Clear Field]` karena Filter Panel menutup setelah `[Apply]`; klik `(←)` pada kotak Search untuk membersihkan Search.
- Langkah penghubung (S-03, S-14, R-16): sebelum `Buka Detail` ditambahkan Search Groups List dengan nama group target (`Value Gate Node A`), karena client memiliki lebih dari 10 node level 1 dan page size 10 sehingga baris target tidak dijamin berada di halaman 1; Search hilang setelah F5, login, atau buka ulang halaman Groups sehingga dipasang lagi.
- Temuan untuk QA:
  - TC-FA-GRP-1306 langkah 4 mengisi Filter lalu `Clear Field` tanpa menyebut `[Apply]`; spec menambah `[Apply]` sebagai langkah penghubung dan memverifikasi hasil Filter sebelum dibersihkan.
  - TC-FA-GRP-1306 tidak menyebut apakah Download dilakukan dengan Search atau Filter aktif; spec melakukannya setelah Filter dan Search dibersihkan.
  - Post Condition TC tidak disebut; tidak diasersi.
