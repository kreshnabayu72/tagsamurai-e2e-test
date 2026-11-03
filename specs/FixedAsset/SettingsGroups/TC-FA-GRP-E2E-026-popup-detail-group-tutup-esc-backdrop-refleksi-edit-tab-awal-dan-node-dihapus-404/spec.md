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
- Data Pre-setup (hanya dibaca): pohon group baku Tabel A (Pre-setup No 9) dengan Warehouse A (24 aset aktif, sedikitnya satu user). Node level 1 client lebih dari 10 dan page size 10, sehingga baris target dicari dengan Search, bukan diandalkan berada di halaman 1; Search `Warehouse` menampilkan Warehouse A dan Warehouse B (dua nilai distinct untuk asersi sort).
- Data Dinamis (di-seed di hook `before` lewat API, node level 1, dihapus di hook `after` bila masih ada):

| TC | Nama TC | Nama seed | State |
|---|---|---|---|
| TC-FA-GRP-285 | Edit Target | `Edit Target {runId}-026` | Kosong, Function None; diubah oleh langkah 35 sampai 39 |
| TC-FA-GRP-986 | Stale D1, Stale D2, Stale D3 | `Stale D1 {runId}-026`, `Stale D2 {runId}-026`, `Stale D3 {runId}-026` | Masing-masing kosong; dihapus satu per iterasi oleh admin lain (sesi API) pada langkah 49 |

- Parameter perulangan TC-FA-GRP-986 (langkah 49 sampai 56):

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

1. Ketik Search `Warehouse`, tekan Enter
2. Klik header kolom Group 2× (sort Group Z→A)
3. Klik nama Warehouse A
4. Verifikasi Popup Detail Group Warehouse A terbuka
5. Klik [X]
6. Verifikasi popup tertutup tanpa dialog
7. Verifikasi tabel List tampil kembali dengan sort Group Z→A tetap
8. Klik nama Warehouse A
9. Klik area backdrop di luar popup
10. Verifikasi popup tetap terbuka
11. Verifikasi tidak ada dialog yang tampil
12. Klik [X]

### TC-FA-GRP-1148: Tutup lewat Esc

13. Klik nama Warehouse A (Tab Assets)
14. Tekan Esc
15. Verifikasi popup tertutup tanpa dialog
16. Klik angka Total User Warehouse A (Tab Users)
17. Tekan Esc
18. Verifikasi popup tertutup tanpa dialog
19. Verifikasi tabel List tampil kembali dengan sort Group Z→A tetap

### TC-FA-GRP-1017: Tab awal sesuai jalur akses

20. Klik nama Warehouse A
21. Verifikasi popup terbuka dengan Tab Assets aktif
22. Klik [X]
23. Klik (⋯) pada baris Warehouse A
24. Klik `Detail`
25. Verifikasi popup terbuka dengan Tab Assets aktif
26. Klik [X]
27. Klik angka Total Asset Warehouse A
28. Verifikasi popup terbuka dengan Tab Assets aktif
29. Klik [X]
30. Klik angka Total User Warehouse A
31. Verifikasi popup terbuka dengan Tab Users aktif
32. Verifikasi urutan tab Assets, Users
33. Klik [X]

### TC-FA-GRP-285: Refleksi live setelah Edit

34. Ganti isi kotak search dengan `Edit Target {runId}-026`, tekan Enter
35. Klik (⋯) pada baris `Edit Target {runId}-026`
36. Klik `Edit`
37. Ganti Group Name dengan `Edit Renamed {runId}-026`, Code dengan `ER{runId}`, dan Description dengan `Deskripsi {runId}-026`
38. Klik [Save]
39. Tunggu aksi selesai (modal Edit tertutup)
40. Ganti isi kotak search dengan `Edit Renamed {runId}-026`, tekan Enter
41. Klik (⋯) pada baris `Edit Renamed {runId}-026`
42. Klik `Detail`
43. Verifikasi header menampilkan Group Name `Edit Renamed {runId}-026`, Code `ER{runId}`, dan Description `Deskripsi {runId}-026`
44. Klik [X]

### TC-FA-GRP-986: Node dihapus user lain, buka popup menghasilkan 404

45. Muat ulang halaman dengan F5 agar sesi aktor memuat `Stale D1`, `Stale D2`, dan `Stale D3`
46. Ketik Search `{runId}-026`, tekan Enter
47. Verifikasi baris `Stale D1 {runId}-026`, `Stale D2 {runId}-026`, dan `Stale D3 {runId}-026` tampil pada tabel
48. Untuk setiap baris tabel "Parameter perulangan" di Prerequisites, lakukan langkah 49 sampai 56
49. Hapus node tersebut lewat sesi API admin lain hingga penghapusan tersimpan
50. Catat jumlah entri Changelog Group lewat fixture BE
51. Buka Popup Detail Group node tersebut lewat jalur klik pada baris tabel (sesi aktor yang dimuat sebelum penghapusan)
52. Verifikasi permintaan detail group node tersebut dijawab 404
53. Verifikasi popup ditutup (tidak ada popup kosong)
54. Verifikasi toast netral `This group is no longer available.`
55. Verifikasi tree di-refresh dan node tersebut hilang dari sidebar dan tabel
56. Verifikasi jumlah entri Changelog Group sama dengan yang dicatat pada langkah 50

## Notes

- Spec melewati sekitar 35 langkah setelah ekspansi (langkah nominal 56; ekspansi 3 iterasi langkah 49 sampai 56 menjadi 24 langkah sehingga total ekspansi 72): seluruh blok adalah satu kelas (perilaku Popup Detail Group) pada layar dan dataset Tabel A yang sama, perulangan TC-FA-GRP-986 per node dari tabel Prerequisites (8b butir 7), tiap blok berdiri sendiri, dan blok yang menghapus data (TC-FA-GRP-986) berada paling akhir (S-10).
- Langkah penghubung (S-03): langkah 2 (menyiapkan sort Group Z→A sebagai state tabel TC-FA-GRP-284 dan 1148), langkah 12 (menutup popup), langkah 39 (tunggu aksi selesai, 8b butir 8), langkah 45 (muat ulang agar sesi aktor memuat node stale), langkah 47 (anchor positif sebelum absence node, 8b butir 2), langkah 49 (admin lain menghapus node iterasi ini), langkah 50 (mencatat baseline jumlah entri setelah penghapusan). Langkah 1, 34, 40, dan 46 (Search) menemukan baris target karena client punya lebih dari 10 node level 1 dengan page size 10, sehingga baris tidak diandalkan berada di halaman 1 (R-16); Search `Warehouse` dipertahankan sampai langkah 33 agar asersi sort Z→A tetap punya dua baris; Search langkah 46 dipasang sekali di luar perulangan dan tidak diulang di dalamnya, karena Search ulang atau refresh tree memuat ulang daftar dari server dan ketiga node sudah terhapus bila dihapus sekaligus; node dihapus satu per iterasi (langkah 49) supaya node iterasi berikutnya masih ada di server saat tree di-refresh.
- Pelaku kedua (admin lain Total Control) hanya memicu perubahan state lewat sesi API, bukan konteks kedua (P-2 `[KEPUTUSAN 2026-10-30]`). Langkah 49 ditulis "... hingga ... tersimpan" (R-20).
- `P-1`: asersi "tidak ada baris log baru" TC-FA-GRP-986 (langkah 50 dan 56) ditulis di spec asal dengan baseline jumlah entri Changelog Group (S-12) karena node stale yang baru dihapus sesi lain adalah state yang dibangun langkah sebelumnya dan tidak dapat diulang di spec absence.
- Urutan TC dalam spec: 284, 1148, 1017, 285, 986.
- Temuan untuk QA:
  - TC-FA-GRP-986 menghapus ketiga node sekaligus sebelum sesi A membuka popup, sedangkan Search dan refresh tree memuat ulang keadaan server. Spec menghapus satu node per iterasi (langkah 49) agar baris yang diklik masih ada di sesi A dan di server saat tree di-refresh; ini menyimpang dari urutan harfiah TC, butuh konfirmasi QA.
  - TC-FA-GRP-986 menyebut status 404 dari server tanpa cara mengamati; spec memakai pencatatan respons jaringan browser (disediakan tim FE/BE).
  - TC-FA-GRP-284 tidak menyebut state tabel yang dipertahankan; spec memakai sort Group Z→A seperti TC-FA-GRP-1148.
  - Post Condition TC-FA-GRP-285 (entri log lama tetap snapshot) tidak punya langkah observasi di TC sehingga tidak diasersi.
