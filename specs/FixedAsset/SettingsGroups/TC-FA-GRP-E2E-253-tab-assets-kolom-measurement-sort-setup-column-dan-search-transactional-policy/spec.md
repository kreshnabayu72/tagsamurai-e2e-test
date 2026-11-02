---
id: TC-FA-GRP-E2E-253-tab-assets-kolom-measurement-sort-setup-column-dan-search-transactional-policy
title: "Tab Assets Kolom Measurement: Sort dan Setup Column, serta Search Kolom Transactional Policy"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1201
  - TC-FA-GRP-1203
  - TC-FA-GRP-1255
coverage:
  web: automated
---

# Tab Assets Kolom Measurement: Sort dan Setup Column, serta Search Kolom Transactional Policy

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md`.
- Data: Value Gate Node A (Tabel Dinamis No 10, Assignable, level 1) berisi hanya aset G1 `Laptop Dell - 1`, G2 `Printer HP - 1`, G3 `Monitor LG - 1`, G4 `Forklift Toyota - 1`, G5 `Kabel Roll - 1`, G6 `Laptop Dell - 2`. Master Measurement (Tabel Dinamis No 14): Piece `pcs`, Unit `unit`, Meter `m`. Policy per Asset Name (Tabel Dinamis No 14): Laptop Dell (Piece; Borrow On, Self Service Borrow Off, Assign On, Transfer On), Printer HP (Piece; semua Off), Monitor LG (Piece; hanya Self Service Borrow On), Forklift Toyota (Unit; hanya Transfer On), Kabel Roll (Meter; hanya Assign On). Data dibaca apa adanya dan tidak diubah spec; di-seed idempotent oleh hook `before` (kemampuan disediakan tim FE/BE).
- Preferensi kolom Setup Column: dikosongkan di hook `before` supaya tabel mulai dari kolom default, dan dihapus di hook `after` (hapus preferensi kolom di browser, bukan [Reset to Default]; kemampuan disediakan tim FE). Spec mengasumsikan konfigurasi kolom Tab Assets tersimpan per akun lintas group (lihat Temuan untuk QA).
- State global: tidak ada yang diubah; hanya preferensi kolom di browser (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1201: Sort by kolom Measurement, siklus Asc, Desc, Netral

1. Buka Detail Value Gate Node A (Tab Assets)
2. Buka Popup Setup Column
3. Centang Measurement
4. Klik [Save]
5. Klik header Measurement (Asc)
6. Verifikasi urutan Ascending A→Z menurut Symbol: `m` (G5), `pcs` (G1, G2, G3, G6), `unit` (G4)
7. Klik header Measurement lagi (Desc)
8. Verifikasi urutan Descending Z→A: `unit` (G4), `pcs`, `m` (G5)
9. Klik header Measurement lagi (Netral)
10. Verifikasi urutan kembali ke default tabel (Name A→Z)

### TC-FA-GRP-1203: Setup Column, kolom curated Measurement: centang, geser (drag), dan pin

11. Buka Popup Setup Column
12. Uncheck Measurement
13. Klik [Save]
14. Buka Popup Setup Column
15. Centang Measurement
16. Klik [Save]
17. Verifikasi kolom Measurement tampil di tabel
18. Refresh F5
19. Buka Detail Value Gate Node A (Tab Assets)
20. Verifikasi kolom Measurement tampil di tabel dan bertahan setelah F5
21. Buka Popup Setup Column
22. Drag Measurement ke posisi setelah Model/Type
23. Klik [Save]
24. Verifikasi urutan kolom tabel mengikuti posisi baru
25. Refresh F5
26. Buka Detail Value Gate Node A (Tab Assets)
27. Verifikasi urutan kolom tabel bertahan setelah F5
28. Buka Popup Setup Column
29. Klik icon Pin Measurement
30. Klik [Save]
31. Scroll tabel horizontal
32. Verifikasi kolom Measurement membeku (sticky) saat scroll horizontal
33. Buka Popup Setup Column
34. Klik icon Pin Measurement untuk unpin
35. Klik [Save]
36. Scroll tabel horizontal
37. Verifikasi kolom Measurement ikut scroll

### TC-FA-GRP-1255: Search by kolom Transactional Policy, nama transaksi tiap ikon

38. Buka Popup Setup Column
39. Centang Transactional Policy
40. Klik [Save]
41. Ketik Search `Transfer`, tekan Enter
42. Verifikasi G1, G4, dan G6 tampil (ikon Transfer On)
43. Verifikasi G2, G3, dan G5 tidak tampil
44. Ganti isi kotak search dengan `self service`, tekan Enter
45. Verifikasi G3 tampil (ikon Self Service Borrow)
46. Verifikasi G2 (semua Off, `—`) tidak tampil
47. Ganti isi kotak search dengan `dispose`, tekan Enter
48. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter."
49. Klik `(←)` pada kotak Search
50. Buka Popup Setup Column
51. Uncheck Transactional Policy
52. Klik [Save]
53. Ketik Search `Transfer`, tekan Enter
54. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter." (kolom Transactional Policy yang di-hide tidak dicari)
55. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): Uncheck lalu Centang Measurement sebelum TC-1203 supaya blok mulai dari Measurement unchecked (blok TC-1201 meninggalkannya tercentang); membuka ulang Detail Value Gate Node A sesudah Refresh F5 dan scroll horizontal ulang; mengosongkan Search dengan `(←)`; langkah hide Transactional Policy dan Search `Transfer` ulang untuk butir d TC-1255 yang tidak punya langkah di TC. Kolom Transactional Policy harus Visible untuk dicari; empty state `dispose` menjadi anchor positif bagi empty state setelah hide (8b butir 2).
- Spec ini 55 langkah, di atas smell 35 langkah: satu kelas (fungsional kolom Measurement dan Transactional Policy), satu dataset (Value Gate Node A), tiga blok TC yang berdiri sendiri dengan state kolom dipulihkan di antaranya; langkah dominan berupa Verifikasi per klausa dan pengulangan Refresh F5.
- Temuan untuk QA (S-15): (1) Expected TC-1255 butir d "Kolom harus Visible: bila di-hide, nama transaksi tidak dicari" tidak punya langkah di TC; spec menambah hide Transactional Policy lalu Search `Transfer`. (2) TC-1203 tidak menyebut kondisi awal Measurement; spec mengembalikannya ke unchecked sebelum blok. (3) TC-1203 tidak menyatakan apakah Popup Detail Group tetap terbuka sesudah F5. (4) Expected TC untuk pin hanya menyebut membeku (sticky) saat scroll horizontal dan ikut scroll setelah unpin; TC tidak menyebut pin bertahan setelah F5, sehingga spec tidak mengasersi pin pasca-F5.
