---
id: TC-FA-SU-E2E-243-tab-system-log-search-dan-sort
title: "Tab System Log: Search dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-738
  - TC-FA-SU-739
  - TC-FA-SU-740
  - TC-FA-SU-741
coverage:
  web: automated
---

# Tab System Log: Search dan Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan System Log (#28). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab System Log Budi Santoso (Pre-setup #28, 7 baris; urutan default Date descending; kolom Name berisi target perubahan). Alias baris yang dipakai langkah (Action | Name | Field):
  - S-1: `Resend Activation Email` | `Hana Kusuma` | `Activation Email`
  - S-2: `Auto-Revert` | `Oscar Pranata` | `Group Manager — IT Infrastructure`
  - S-3: `Edit` | `Oscar Pranata` | `Manage group — IT Infrastructure — Update`
  - S-4: `Assign` | `Lina Marlina` | `Access Level`
  - S-5: `Assign` | `Eka Wulandari` | `Manage group — Finance & Accounting`
  - S-6: `Assign` | `Eka Wulandari` | `Manage accounting`
  - S-7: `Activate` | `Eka Wulandari` | `Status`
- Nilai Date baris S-1 (Pre-setup #28, PRD §4.3f): `18/08/26, 13:10`; dipakai TC-FA-SU-739 (kolom Date tidak dapat dicari lewat Search).
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed System Log #28 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface System Log dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-738: Siklus interaksi Search

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail pengguna Budi Santoso dan klik tab System Log
2. Klik icon Search
3. Verifikasi input melebar
4. Verifikasi kursor fokus di input
5. Verifikasi placeholder `Search action, field, or value...`
6. Hover icon Search
7. Verifikasi tooltip `Search`
8. Ketik 1 karakter dari `Revert` (`R`)
9. Verifikasi icon ✕ tampil di kanan input
10. Verifikasi tabel belum tersaring
11. Ketik sisa `Revert` (`evert`) lalu tekan Enter
12. Verifikasi tabel tersaring menjadi S-2 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
13. Klik ✕
14. Verifikasi input kosong
15. Verifikasi search bar tetap terbuka
16. Verifikasi kursor fokus di input
17. Verifikasi tabel tetap menampilkan hasil search terakhir
18. Tekan Enter pada input kosong
19. Verifikasi tabel kembali ke semua baris
20. Ketik `Revert`, tekan Enter, lalu klik icon ←
21. Verifikasi search bar menutup
22. Verifikasi keyword dikosongkan
23. Verifikasi tabel langsung kembali ke semua baris
24. Klik icon Search
25. Ketik `  Revert  ` (spasi awal dan akhir), tekan Enter
26. Verifikasi hasil sama dengan `Revert` tanpa spasi (S-2; 1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
27. Verifikasi isi input tidak berubah

### TC-FA-SU-739: Guard kolom non-searchable Date

28. Kosongkan isi kotak search, tekan Enter
29. Verifikasi sel Date baris S-1 pada tabel menampilkan `18/08/26, 13:10`
30. Ketik Search `18/08/26, 13:10` (nilai kolom Date S-1), tekan Enter
31. Verifikasi nilai Date `18/08/26, 13:10` tidak mencocokkan baris melalui Search; empty state `No results found` tampil
32. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-740: Search terikat visibilitas kolom Action

33. Ketik Search `Revert`, tekan Enter
34. Verifikasi sebelum hide: keyword `Revert` menyisakan S-2 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
35. Klik header Column Visibility (⋯), hilangkan centang Action
36. Ganti isi kotak search dengan `Revert`, tekan Enter
37. Verifikasi setelah kolom Action di-hide: keyword yang sama menyisakan tidak ada baris (0 baris), empty state `No results found` tampil
38. Klik header Column Visibility (⋯), centang kembali Action
39. Ganti isi kotak search dengan `Revert`, tekan Enter
40. Verifikasi setelah kolom Action di-unhide: hasil kembali S-2 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
41. Klik `(←)` pada kotak Search

### TC-FA-SU-741: Sort kelas date (Date)

42. Klik header Date satu kali
43. Verifikasi urutan relatif baris seed klik 1 ascending (↑), baris non-seed boleh menyisip: S-7, S-6, S-5, S-4, S-2
44. Klik header Date kedua kali
45. Verifikasi urutan relatif baris seed klik 2 descending (↓), baris non-seed boleh menyisip: S-1, S-2, S-3, S-4, S-5
46. Klik header Date ketiga kali
47. Verifikasi urutan relatif baris seed klik 3 netral kembali ke default, baris non-seed boleh menyisip: S-1, S-2, S-3, S-4, S-5

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pembukaan Detail pada langkah 1 didahului Search `Budi Santoso` lalu Enter untuk menemukan baris target (R-16, butir 8b.9 dan 8b.13); User List memuat 25 pengguna pada 3 halaman sehingga posisi baris tidak diandalkan.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 28 (mengosongkan Search agar baris S-1 tampil di tabel sebelum `Verifikasi` sel Date pada langkah 29, bagian 8b butir 15b).
- Asersi tambahan di luar Expected (S-03): empty state `No results found` pada asersi hasil 0 baris TC-FA-SU-740, sebagai anchor positif absence (bagian 8b butir 2).
- Spec ini berjumlah 47 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #28 yang disediakan ulang di hook `before` dan `after` (S-14). Aksi spec lain terhadap Budi Santoso menambah entri System Log, sehingga penyediaan ulang seed menjadi syarat asersi urutan dan jumlah baris. (2) Tanggal baris seed System Log (Pre-setup #28) tidak tertulis di Tabel Pre-setup (kecuali Date S-1 `18/08/26, 13:10` dari PRD §4.3f yang dicatat di Prerequisites); asersi yang memakai nilai atau rentang Date mengikuti angka di TC dan bergantung pada seed yang disediakan tim FE/BE. (3) TC-FA-SU-740 butir b menulis hasil tanpa baris tanpa menyebut empty state; spec menambahkan `Verifikasi` empty state `No results found` sebagai anchor positif asersi 0 baris (bagian 8b butir 2); klausa butir b "kolom lain yang tampil tetap dicari" tidak diasersi karena TC tidak memberi keyword yang hanya cocok pada kolom lain yang tampil. (4) TC-FA-SU-741 mengurutkan ascending urutan relatif baris seed S-7, S-6, S-5, S-4, S-2, sedangkan urutan descending default S-1, S-2, S-3, S-4, S-5 pada tujuh baris seed menyiratkan baris kelima ascending adalah S-3 (Edit Oscar Pranata); S-2 dan S-3 tampak berstempel waktu sama pada ketelitian menit. Spec mengikuti Expected TC.
