---
id: TC-FA-GRP-E2E-248-tab-assets-download-isi-berkas-kolom-transactional-policy-last-scanned-dan-group-tidak-berlaku
title: "Tab Assets Download Isi Berkas: Kolom Group Tidak Berlaku, Transactional Policy, dan Last Scanned (Format General Settings)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1190
  - TC-FA-GRP-1207
  - TC-FA-GRP-1212
coverage:
  web: automated
---

# Tab Assets Download Isi Berkas: Kolom Group Tidak Berlaku, Transactional Policy, dan Last Scanned (Format General Settings)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md`.
- Data: Value Gate Node A (Tabel Dinamis No 10, Assignable, level 1) berisi hanya aset G1 `Laptop Dell - 1`, G2 `Printer HP - 1`, G3 `Monitor LG - 1`, G4 `Forklift Toyota - 1`, G5 `Kabel Roll - 1`, G6 `Laptop Dell - 2`. Policy per Asset Name (Tabel Dinamis No 14): Laptop Dell (Borrow On, Self Service Borrow Off, Assign On, Transfer On), Printer HP (semua Off), Monitor LG (hanya Self Service Borrow On), Forklift Toyota (hanya Transfer On), Kabel Roll (hanya Assign On). Pemindaian Audit terbaru (Tabel Dinamis No 15): G3 01/09/2026, G1 10/10/2026, G5 20/10/2026; G2, G4, G6 belum pernah dipindai. Data dibaca apa adanya dan tidak diubah spec; di-seed idempotent oleh hook `before` (kemampuan disediakan tim FE/BE).
- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (prasyarat state, tidak diubah spec; disediakan tim FE/BE).
- Kemampuan teknis: membaca isi berkas unduhan CSV (nilai sel, hyphen `-`, header kolom) disediakan tim FE; asersi berkas memakai kemampuan itu.
- Preferensi kolom Setup Column: dikosongkan di hook `before` supaya tabel mulai dari kolom default, dan dihapus di hook `after` (hapus preferensi kolom di browser, bukan [Reset to Default]; kemampuan disediakan tim FE). Spec mengasumsikan konfigurasi kolom Tab Assets tersimpan per akun lintas group (lihat Temuan untuk QA).
- State global: tidak ada yang diubah; hanya preferensi kolom di browser (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1190: Kolom Group tidak berlaku di Tab Assets

1. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
2. Buka Detail Value Gate Node A (Tab Assets)
3. Amati header kolom tabel
4. Verifikasi header tabel memuat kolom `Name`
5. Verifikasi tidak ada kolom Group di header tabel
6. Buka Popup Setup Column
7. Verifikasi daftar Popup Setup Column memuat kolom `Name`
8. Verifikasi tidak ada kolom Group di daftar Popup Setup Column
9. Klik ✕ pada Popup Setup Column
10. Klik icon Filter
11. Verifikasi Filter Panel memuat field `Status`
12. Verifikasi Filter Panel tidak memuat field Group
13. Klik icon Filter untuk menutup Filter Panel
14. Ketik Search `Value Gate Node A`, tekan Enter
15. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter." (tidak ada kolom Group yang dicari)
16. Klik `(←)` pada kotak Search
17. Klik icon Download
18. Pilih Download as CSV
19. Buka berkas
20. Verifikasi berkas CSV memuat kolom Visible (kolom `Name`)
21. Verifikasi berkas CSV tidak memuat kolom Group

### TC-FA-GRP-1207: Download Tab Assets, kolom Transactional Policy ditulis nama transaksi dipisah koma

22. Buka Popup Setup Column
23. Centang Transactional Policy
24. Klik [Save]
25. Klik icon Download
26. Pilih Download as CSV
27. Verifikasi tidak ada toast sukses
28. Buka berkas
29. Verifikasi G1 dan G6 = `Borrow, Assign, Transfer`, G3 = `Self Service Borrow`, G4 = `Transfer`, G5 = `Assign`
30. Verifikasi sel Transactional Policy G2 ditulis hyphen tunggal `-`

### TC-FA-GRP-1212: Download Tab Assets, kolom Last Scanned mengikuti format General Settings

31. Buka Popup Setup Column
32. Centang Last Scanned
33. Klik [Save]
34. Klik icon Download
35. Pilih Download as CSV
36. Verifikasi tidak ada toast sukses
37. Buka berkas
38. Verifikasi sel Last Scanned G3, G1, dan G5 ditulis tanggal-waktu sesuai format dan timezone General Settings (tanggal `01/09/2026`, `10/10/2026`, `20/10/2026` berurutan)
39. Verifikasi sel Last Scanned G2, G4, dan G6 ditulis hyphen tunggal `-`

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular. TC-1190 bercampur fungsional (header tabel, Setup Column, Filter Panel, Search) dan isi berkas (klausa d), dicatat dalam spec fungsional ini (P-10): alur unduh tidak dapat dipisah dari asersi UI Tab Assets yang mendahuluinya, klausa isi berkas (butir d) diletakkan setelah seluruh klausa UI TC itu. TC-1207 dan TC-1212 adalah kelas harness f (isi berkas). Nama berkas dan jumlah baris diasersi di spec Download fungsional.
- Langkah penghubung (S-03): Klik ✕ pada Popup Setup Column; Klik icon Filter untuk menutup Filter Panel; Klik `(←)` pada kotak Search untuk mengosongkan pencarian; Setup Column centang Transactional Policy dan Last Scanned adalah langkah TC. TC-1190 diletakkan pertama karena memeriksa kolom default; seluruh blok satu topik/dataset (Value Gate Node A, G1 sampai G6) sehingga melebihi 35 langkah tanpa dipecah. Asersi tidak ada toast sukses diletakkan segera sesudah memilih format Download dan sebelum membuka berkas (8b butir 11); anchor positifnya adalah Verifikasi isi berkas sesudahnya.
- Langkah penghubung (S-03, S-14, R-16): sebelum tiap `Buka Detail` ditambahkan Search Groups List dengan nama group target (`Value Gate Node A`), karena client memiliki lebih dari 10 node level 1 dan page size 10 sehingga baris target tidak dijamin berada di halaman 1; Search hilang setelah F5, login, atau buka ulang halaman Groups sehingga dipasang lagi.
- Temuan untuk QA (S-15): (0) TC-1190 adalah TC fungsional (kolom Group tidak berlaku di tabel, Setup Column, Filter Panel, dan Search) yang juga memuat klausa isi berkas (butir d). (1) TC-1190 butir d "hanya memuat kolom Visible" tidak menyebut kolom Visible konkret; spec memakai kolom `Name`. (2) TC-1212 menyebut G3, G1, G5 ditulis "tanggal-waktu" tanpa jam; Tabel Dinamis No 15 hanya memuat tanggal pemindaian, sehingga spec mengasersi tanggal dan format, bukan jam. (3) Berkas CSV mengikuti 8b butir 1 hanya untuk isi; TC memakai "Buka berkas" tanpa nama berkas.
