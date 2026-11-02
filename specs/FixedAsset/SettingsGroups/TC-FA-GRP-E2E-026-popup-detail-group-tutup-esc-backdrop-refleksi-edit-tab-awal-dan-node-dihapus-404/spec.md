---
id: TC-FA-GRP-E2E-026-popup-detail-group-tutup-esc-backdrop-refleksi-edit-tab-awal-dan-node-dihapus-404
title: "Popup Detail Group: Tutup via [X] dan Esc, Backdrop Tidak Menutup, Refleksi Live Setelah Edit, Tab Awal per Jalur Akses, dan Node Dihapus (404)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-284
  - TC-FA-GRP-285
  - TC-FA-GRP-986
  - TC-FA-GRP-1017
  - TC-FA-GRP-1148
coverage:
  web: automated
---

# Popup Detail Group: Tutup via [X] dan Esc, Backdrop Tidak Menutup, Refleksi Live Setelah Edit, Tab Awal per Jalur Akses, dan Node Dihapus (404)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca): pohon group baku Tabel A (Pre-setup No 9) dengan Warehouse A (24 aset aktif, sedikitnya satu user). Jumlah node level 1 tidak lebih dari 10 sehingga seluruh baris tampil di halaman 1.
- Data Dinamis (di-seed di hook `before` lewat API, node level 1, dihapus di hook `after` bila masih ada):

| TC | Nama TC | Nama seed | State |
|---|---|---|---|
| TC-FA-GRP-285 | Edit Target | `Edit Target {runId}-026` | Kosong, Function None; diubah oleh langkah 33 sampai 37 |
| TC-FA-GRP-986 | Stale D1, Stale D2, Stale D3 | `Stale D1 {runId}-026`, `Stale D2 {runId}-026`, `Stale D3 {runId}-026` | Masing-masing kosong; dihapus sekaligus oleh admin lain (sesi API) pada langkah 44 |

- Parameter perulangan TC-FA-GRP-986 (langkah 47 sampai 52):

| Node | Jalur klik pada sesi aktor |
|---|---|
| `Stale D1 {runId}-026` | klik nama node di tabel |
| `Stale D2 {runId}-026` | klik angka Total Asset node di tabel (`0`, tetap dapat diklik) |
| `Stale D3 {runId}-026` | klik angka Total User node di tabel |

- Nilai baru Edit TC-FA-GRP-285: Group Name `Edit Renamed {runId}-026`, Code `ER{runId}` (tidak lebih dari 15 karakter), Description `Deskripsi {runId}-026`.
- Kemampuan teknis: fixture BE (seeding, pembacaan jumlah entri Changelog Group, pemulihan data milik spec), sesi API aktor (admin lain Total Control yang menghapus node), dan pencatatan respons jaringan browser untuk membaca status respons permintaan detail group, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-GRP-284: Tutup lewat [X], backdrop tidak menutup

1. Klik header kolom Group 2× (sort Group Z→A)
2. Klik nama Warehouse A
3. Verifikasi Popup Detail Group Warehouse A terbuka
4. Klik [X]
5. Verifikasi popup tertutup tanpa dialog
6. Verifikasi tabel List tampil kembali dengan sort Group Z→A tetap
7. Klik nama Warehouse A
8. Klik area backdrop di luar popup
9. Verifikasi popup tetap terbuka
10. Verifikasi tidak ada dialog yang tampil
11. Klik [X]

### TC-FA-GRP-1148: Tutup lewat Esc

12. Klik nama Warehouse A (Tab Assets)
13. Tekan Esc
14. Verifikasi popup tertutup tanpa dialog
15. Klik angka Total User Warehouse A (Tab Users)
16. Tekan Esc
17. Verifikasi popup tertutup tanpa dialog
18. Verifikasi tabel List tampil kembali dengan sort Group Z→A tetap

### TC-FA-GRP-1017: Tab awal sesuai jalur akses

19. Klik nama Warehouse A
20. Verifikasi popup terbuka dengan Tab Assets aktif
21. Klik [X]
22. Klik (⋯) pada baris Warehouse A
23. Klik `Detail`
24. Verifikasi popup terbuka dengan Tab Assets aktif
25. Klik [X]
26. Klik angka Total Asset Warehouse A
27. Verifikasi popup terbuka dengan Tab Assets aktif
28. Klik [X]
29. Klik angka Total User Warehouse A
30. Verifikasi popup terbuka dengan Tab Users aktif
31. Verifikasi urutan tab Assets, Users
32. Klik [X]

### TC-FA-GRP-285: Refleksi live setelah Edit

33. Klik (⋯) pada baris `Edit Target {runId}-026`
34. Klik `Edit`
35. Ganti Group Name dengan `Edit Renamed {runId}-026`, Code dengan `ER{runId}`, dan Description dengan `Deskripsi {runId}-026`
36. Klik [Save]
37. Tunggu aksi selesai (modal Edit tertutup)
38. Klik (⋯) pada baris `Edit Renamed {runId}-026`
39. Klik `Detail`
40. Verifikasi header menampilkan Group Name `Edit Renamed {runId}-026`, Code `ER{runId}`, dan Description `Deskripsi {runId}-026`
41. Klik [X]

### TC-FA-GRP-986: Node dihapus user lain, buka popup menghasilkan 404

42. Muat ulang halaman dengan F5 agar sesi aktor memuat `Stale D1`, `Stale D2`, dan `Stale D3`
43. Verifikasi baris `Stale D1 {runId}-026`, `Stale D2 {runId}-026`, dan `Stale D3 {runId}-026` tampil pada tabel
44. Hapus `Stale D1 {runId}-026`, `Stale D2 {runId}-026`, dan `Stale D3 {runId}-026` lewat sesi API admin lain hingga penghapusan tersimpan
45. Catat jumlah entri Changelog Group lewat fixture BE
46. Untuk setiap baris tabel "Parameter perulangan" di Prerequisites, lakukan langkah 47 sampai 52
47. Buka Popup Detail Group node tersebut lewat jalur klik pada baris tabel (sesi aktor yang dimuat sebelum penghapusan)
48. Verifikasi permintaan detail group node tersebut dijawab 404
49. Verifikasi popup ditutup (tidak ada popup kosong)
50. Verifikasi toast netral `This group is no longer available.`
51. Verifikasi tree di-refresh dan node tersebut hilang dari sidebar dan tabel
52. Verifikasi jumlah entri Changelog Group sama dengan yang dicatat pada langkah 45

## Notes

- Spec melewati sekitar 35 langkah setelah ekspansi (langkah nominal 52; ekspansi 3 iterasi langkah 47 sampai 52 menjadi 18 langkah sehingga total ekspansi 64): seluruh blok adalah satu kelas (perilaku Popup Detail Group) pada layar dan dataset Tabel A yang sama, perulangan TC-FA-GRP-986 per node dari tabel Prerequisites (8b butir 7), tiap blok berdiri sendiri, dan blok yang menghapus data (TC-FA-GRP-986) berada paling akhir (S-10).
- Langkah penghubung (S-03): langkah 1 (menyiapkan sort Group Z→A sebagai state tabel TC-FA-GRP-284 dan 1148), langkah 11 (menutup popup), langkah 37 (tunggu aksi selesai, 8b butir 8), langkah 42 (muat ulang agar sesi aktor memuat node stale), langkah 43 (anchor positif sebelum absence node, 8b butir 2), langkah 44 (admin lain menghapus ketiga node sekaligus), langkah 45 (mencatat baseline jumlah entri).
- Pelaku kedua (admin lain Total Control) hanya memicu perubahan state lewat sesi API, bukan konteks kedua (P-2 `[KEPUTUSAN 2026-10-30]`). Langkah 44 ditulis "... hingga ... tersimpan" (R-20).
- `P-1`: asersi "tidak ada baris log baru" TC-FA-GRP-986 (langkah 45 dan 52) ditulis di spec asal dengan baseline jumlah entri Changelog Group (S-12) karena node stale yang baru dihapus sesi lain adalah state yang dibangun langkah sebelumnya dan tidak dapat diulang di spec absence.
- Urutan TC dalam spec: 284, 1148, 1017, 285, 986.
- Temuan untuk QA:
  - TC-FA-GRP-986 menyebut status 404 dari server tanpa cara mengamati; spec memakai pencatatan respons jaringan browser (disediakan tim FE/BE).
  - TC-FA-GRP-284 tidak menyebut state tabel yang dipertahankan; spec memakai sort Group Z→A seperti TC-FA-GRP-1148.
  - Post Condition TC-FA-GRP-285 (entri log lama tetap snapshot) tidak punya langkah observasi di TC sehingga tidak diasersi.
