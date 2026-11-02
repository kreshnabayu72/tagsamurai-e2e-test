---
id: TC-FA-GRP-E2E-269-tab-assets-custom-field-search-sort-teks-tanggal-dan-kolom-di-hide
title: "Tab Assets Custom Field: Search Substring dengan Kolom Di-Hide Tidak Dicari serta Sort Teks (PO Number) dan Tanggal (Purchase Date)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1234
  - TC-FA-GRP-1235
  - TC-FA-GRP-1236
coverage:
  web: automated
---

# Tab Assets Custom Field: Search Substring dengan Kolom Di-Hide Tidak Dicari serta Sort Teks (PO Number) dan Tanggal (Purchase Date)

## Prerequisites

- Mode: FE+BE.
- Hook suite: rujuk `suite.md` (login API aktor, sesi API, fixture BE, flag Guided Tooltip `fa-settings-groups` bernilai `seen`).
- Akun aktor: allValueAccess (Pre-setup No 17: Group Role Manage purchase pada Value Gate Node A, Global Role Manage accounting, lisensi FA-7 aktif) `allValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_ALLVALUEACCESS_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup tambahan (hanya dibaca, tidak diubah): Value Gate Node A (Tabel Dinamis No 10, G1-G6) dan custom field Tabel Dinamis No 13; node di-seed idempotent di hook `before` dengan nama bersuffix `{runId}-269` (mekanisme seeding disediakan tim FE/BE). Langkah dan asersi memakai nama bersuffix itu.
- Nilai uji (diacu dari fixture spec): Cost Center G1 `CC-ALPHA`, G4 `CC-ALPHA`; PO Number G1 `PO-001`, G2 `PO-002`, G6 `PO-006`, G3/G4/G5 tanpa nilai; Cost Account G1 `CA-100`, G2 `CA-150`, G6 `CA-200`; Purchase Date G1 10/02/2026, G2 dan G6 01/03/2026, G4 01/04/2026, G5 05/05/2026, G3 belum diisi. Sort dan search memakai kolom dengan lebih dari dua nilai distinct (S-11).
- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (kondisi awal client uji; spec tidak mengubahnya).
- Setup Column: hook `before` menghapus preferensi kolom Tab Assets di browser; hook `after` menghapus preferensi yang disimpan spec (kemampuan disediakan tim FE). Antar TC, konfigurasi dikembalikan dengan [Reset to Default] lalu [Save] sebagai langkah penghubung.
- State global: tidak ada yang diubah.

## Test Steps

### TC-1234: Search by kolom Custom Field: substring, case-insensitive, dan kolom yang di-hide tidak dicari
1. Buka Detail Value Gate Node A (Tab Assets)
2. Buka Popup Setup Column, centang kolom Cost Center, PO Number, dan Cost Account, klik [Save]
3. Ketik Search `CC-ALPHA`, tekan Enter
4. Verifikasi G1 dan G4 tampil
5. Ganti isi kotak search dengan `po-006`, tekan Enter
6. Verifikasi G6 tampil
7. Verifikasi baris selain G6 tidak tampil
8. Ganti isi kotak search dengan `CA-1`, tekan Enter
9. Verifikasi G1 (`CA-100`) dan G2 (`CA-150`) tampil
10. Buka Popup Setup Column, hide kolom Cost Center, klik [Save]
11. Ganti isi kotak search dengan `CC-ALPHA`, tekan Enter
12. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter."
### TC-1235: Sort kolom Custom Field bertipe teks (PO Number): A-Z, `—` menurut aturan kosong
13. Klik `(←)` pada kotak Search, buka Popup Setup Column, klik [Reset to Default], klik [Save]
14. Buka Popup Setup Column, centang kolom PO Number, klik [Save]
15. Klik header PO Number (Asc)
16. Verifikasi urutan `PO-001` (G1), `PO-002` (G2), `PO-006` (G6)
17. Verifikasi baris `—` (G3, G4, G5) berada di akhir
18. Klik header PO Number lagi (Desc)
19. Verifikasi baris `—` berada di awal
20. Verifikasi urutan sesudahnya `PO-006`, `PO-002`, `PO-001`
21. Klik header PO Number lagi (Netral)
22. Verifikasi urutan kembali ke default tabel (Name A-Z)
### TC-1236: Sort kolom Custom Field bertipe tanggal (Purchase Date): Oldest First / Newest First
23. Buka Popup Setup Column, klik [Reset to Default], klik [Save]
24. Buka Popup Setup Column, centang kolom Purchase Date, klik [Save]
25. Klik header Purchase Date (Asc)
26. Verifikasi urutan Oldest First: G1 (10/02/2026), G2 dan G6 (01/03/2026), G4 (01/04/2026), G5 (05/05/2026)
27. Verifikasi baris `—` (G3) berada di akhir
28. Klik header Purchase Date lagi (Desc)
29. Verifikasi G3 (`—`) berada di awal
30. Verifikasi urutan Newest First sesudahnya: G5, G4, G2 dan G6, G1
31. Klik header Purchase Date lagi (Netral)
32. Verifikasi urutan kembali ke default tabel (Name A-Z)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah pertama TC-1235 (kosongkan Search lewat `(←)` dan [Reset to Default] + [Save]) dan langkah pertama TC-1236 ([Reset to Default] + [Save]) membersihkan state TC sebelumnya (S-09).
- Urutan G2 terhadap G6 pada TC-1236 tidak dinilai (tanggal sama 01/03/2026), sesuai precondition TC.
- Temuan untuk QA:
  - TC-1234 Expected b "hanya G6 tampil" memakai universal; spec memakai G6 tampil sebagai pembanding sebelum asersi baris lain tidak tampil.
  - TC-1235/1236 tidak menyebut urutan antar G3, G4, G5 (sama-sama `—`); tidak diasersi.
