---
id: TC-FA-GRP-E2E-104-konflik-dua-admin-delete-group-terakhir-create-rename-sama-dan-kondisi-berubah-setelah-dialog
title: "Konflik Dua Admin: Delete Dua Group Terakhir, Create/Rename Nama Sama, Aset/User/Transfer Ditambah Setelah Dialog, dan Would-Empty/Scope-Empty Dievaluasi Ulang Saat Commit"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-936
  - TC-FA-GRP-937
  - TC-FA-GRP-938
  - TC-FA-GRP-939
  - TC-FA-GRP-940
  - TC-FA-GRP-941
  - TC-FA-GRP-942
  - TC-FA-GRP-1063
coverage:
  web: automated
---

# Konflik Dua Admin: Delete Dua Group Terakhir, Create/Rename Nama Sama, Aset/User/Transfer Ditambah Setelah Dialog, dan Would-Empty/Scope-Empty Dievaluasi Ulang Saat Commit

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control (Pre-setup No 1: `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Role yang diuji dan konteks (ganti akun ditulis eksplisit pada langkah 45, 54, 62, 64; semua akun selain Total Control hook disediakan tim FE karena tidak tertulis di Pre-setup TC):

| TC | Konteks | Akun | Env var password |
|---|---|---|---|
| TC-937, TC-938 | Konteks A (hook `before`) dan konteks B (konteks browser kedua, objek asersi) | Total Control A (Pre-setup No 1) dan Total Control B (Pre-setup No 27) pada client utama yang sama; bukan client Multi Role (TC-1144) | `Spectra.env.FA_TC_PASSWORD` dan `Spectra.env.FA_TC_B_PASSWORD` |
| TC-939, TC-940, TC-941 | Konteks A; pelaku kedua lewat sesi API | Total Control A | `Spectra.env.FA_TC_PASSWORD` |
| TC-942 | Konteks aktor A; aktor B lewat sesi API | Total Control client khusus 4 group | `Spectra.env.FA_FOURGRP_TC_PASSWORD` |
| TC-1063 | Aktor; admin lain lewat sesi API | Manage Group R+D scope `Scope C`, `Scope D`, `Scope E` | `Spectra.env.FA_MGRD_CDE_PASSWORD` |
| TC-936 | Konteks A dan konteks B (dua konteks UI, objek asersi) | User A dan User B Total Control client khusus (hanya `Last A` dan `Last B`) | `Spectra.env.FA_LASTAB_A_PASSWORD` dan `Spectra.env.FA_LASTAB_B_PASSWORD` |

- Data Dinamis (di-seed lewat API di `before`): `Same Name` dibuat oleh pemenang balapan (TC-937, dihapus di `after`); `Rn1` dan `Rn2` (sibling di bawah `Head Office`, TC-938); `Race Del` (kosong, TC-939); `Race Warn` (kosong tanpa user, TC-940); `Race Tr` dengan child `Race Tr Child` (kosong, TC-941); `Scope C`, `Scope D`, `Scope E` (kosong, TC-1063). Data Pre-setup `Head Office` (Tabel A, No 9) hanya dibaca sebagai parent. Client khusus 4 group dan client khusus `Last A`/`Last B` adalah Pre-setup (disediakan tim FE) dan group-nya dihapus oleh pemenang balapan; pemulihan dijamin fixture BE di `after`.
- Pelaku kedua yang hanya memicu perubahan state (mendaftarkan aset, meng-assign Group Role, membuat Transfer, menghapus group) memakai sesi API (suite.md, P-2 2026-10-30); konteks browser kedua dipakai hanya pada TC-936, TC-937, dan TC-938 karena hasil di konteks itu diasersi. Kemampuan membuat aset, assignment, dan transfer disediakan tim FE/BE tanpa endpoint karangan. "Bersamaan" dikerjakan lewat kemampuan sinkronisasi dua klik dalam jendela waktu sempit (disediakan tim FE).
- Cleanup di `after`: hapus data seed lewat API dan lepas assignment, aset, dan transfer seed.

## Test Steps

### TC-FA-GRP-937: Dua user Create Group dengan nama sama di parent sama

1. Buka konteks browser kedua (B): login sebagai Total Control B (Pre-setup No 27), lalu buka Fixed Asset > Settings > Groups
2. Konteks A dan B: ketik Search `Head Office`, tekan Enter
3. Konteks A dan B: buka Add Subgroup di `Head Office`, isi Group Name `Same Name`
4. Klik [Submit] pada konteks A dan konteks B bersamaan
5. Verifikasi tepat satu konteks sukses (popup tertutup dan `Same Name` tampil sebagai child `Head Office`)
6. Verifikasi konteks lain menampilkan inline error "Group name already exists in this level"
7. Verifikasi popup konteks lain tetap terbuka
8. Klik `✕` pada popup yang tetap terbuka
9. Verifikasi dialog `Unsaved Changes` tampil
10. Klik [Leave]
11. Konteks A dan B: klik `(←)` pada kotak Search

### TC-FA-GRP-938: Dua user Rename ke nama sama di parent sama

12. Konteks A dan B: klik `Head Office` di sidebar Group Tree
13. Konteks A: ketik Search `Rn1`, tekan Enter; konteks B: ketik Search `Rn2`, tekan Enter
14. Konteks A: buka Edit `Rn1`, ganti Group Name menjadi `Dup Name`; konteks B: buka Edit `Rn2`, ganti Group Name menjadi `Dup Name`
15. Klik [Save] pada konteks A dan konteks B bersamaan
16. Verifikasi tepat satu konteks sukses (popup tertutup)
17. Verifikasi konteks lain menampilkan inline error "Group name already exists in this level"
18. Klik `✕` pada popup yang tetap terbuka
19. Verifikasi dialog `Unsaved Changes` tampil
20. Klik [Leave]
21. Tutup konteks browser kedua (B)
22. Konteks A: klik `(←)` pada kotak Search
23. Klik `All Groups` di sidebar Group Tree

### TC-FA-GRP-939: Aset didaftarkan ke node setelah dialog konfirmasi tampil

24. Ketik Search `Race Del`, tekan Enter
25. Buka elipsis `⋯` baris `Race Del`, pilih `Delete` (dialog konfirmasi normal)
26. User lain (sesi API) mendaftarkan aset ke `Race Del` hingga pendaftaran tersimpan
27. Klik [Delete]
28. Verifikasi dialog "This group or its subgroups still hold assets. Transfer or dispose them first."
29. Verifikasi `Race Del` tidak terhapus (ditolak sebagai konflik)
30. Klik [OK]

### TC-FA-GRP-940: User di-assign ke node setelah dialog konfirmasi normal tampil

31. Ganti isi kotak Search dengan `Race Warn`, tekan Enter
32. Buka elipsis `⋯` baris `Race Warn`, pilih `Delete` (dialog konfirmasi normal)
33. Admin lain (sesi API) meng-assign Group Role ke `Race Warn` hingga assignment tersimpan
34. Klik [Delete]
35. Verifikasi dialog warning user ter-scope sesuai hasil terbaru: "This group has users assigned — deleting it will remove their group roles. This action cannot be undone. Are you sure you want to delete it?"
36. Verifikasi `Race Warn` tidak terhapus (ditolak sebagai konflik)
37. Klik [Cancel]

### TC-FA-GRP-941: Transfer ke descendant dibuat setelah dialog konfirmasi tampil

38. Ganti isi kotak Search dengan `Race Tr`, tekan Enter
39. Buka elipsis `⋯` baris `Race Tr`, pilih `Delete`
40. User lain (sesi API) membuat Transfer tujuan `Race Tr Child` hingga transfer tersimpan
41. Klik [Delete]
42. Verifikasi dialog "This group is the destination of an ongoing transfer. Wait for it to complete or be canceled first."
43. Verifikasi `Race Tr` tidak terhapus (ditolak sebagai konflik)
44. Klik [OK]

### TC-FA-GRP-1063: Bulk Delete, scope-empty aktor dievaluasi ulang di awal commit

45. Logout, lalu login sebagai Manage Group R+D scope `Scope C`, `Scope D`, dan `Scope E`
46. Buka Fixed Asset > Settings > Groups
47. Ketik Search `Scope C`, tekan Enter, centang `Scope C`; ganti isi kotak Search dengan `Scope D`, tekan Enter, centang `Scope D` (centang dipertahankan saat Search berganti, TC-251 dan TC-426); buka Bulk Action, pilih `Delete` (dialog konfirmasi homogen)
48. Admin lain (sesi API) menghapus `Scope E` hingga penghapusan tersimpan
49. Klik [Delete]
50. Verifikasi dialog "Cannot Delete Groups" dengan isi "You can't delete every group you're assigned to. Ask an admin to assign you another group first." dan tombol [OK]
51. Klik [OK]
52. Ganti isi kotak Search tabel All Groups dengan `Scope`, tekan Enter
53. Verifikasi `Scope C` dan `Scope D` tidak terhapus (seluruh aksi ditolak sebagai konflik)

### TC-FA-GRP-942: Bulk Delete, would-empty dievaluasi ulang di awal commit

54. Logout, lalu login sebagai Total Control client khusus 4 group
55. Buka Fixed Asset > Settings > Groups
56. Centang 2 group (aktor A), buka Bulk Action, pilih `Delete`
57. Aktor B (sesi API) menghapus 2 group lainnya hingga penghapusan tersimpan
58. Klik [Delete]
59. Verifikasi dialog would-empty "Cannot Delete Groups" dengan isi "You've selected all remaining groups. At least one group must always exist — deselect at least one group and try again." dan tombol [OK]
60. Verifikasi kedua group yang dipilih aktor A tidak terhapus (seluruh aksi ditolak sebagai konflik)
61. Klik [OK]

### TC-FA-GRP-936: Dua Delete bersamaan atas dua group terakhir

62. Logout, lalu login sebagai User A client khusus `Last A` dan `Last B`
63. Buka Fixed Asset > Settings > Groups
64. Buka konteks browser kedua (B): login sebagai User B, lalu buka Fixed Asset > Settings > Groups
65. Konteks A: buka elipsis `⋯` baris `Last A`, pilih `Delete`; konteks B: buka elipsis `⋯` baris `Last B`, pilih `Delete`
66. Klik [Delete] pada konteks A dan konteks B bersamaan
67. Verifikasi tepat satu Delete sukses (satu konteks menampilkan toast sukses)
68. Verifikasi konteks lain menampilkan dialog "Deleting this group would leave you with no groups. Create another group before deleting this one."
69. Verifikasi client tetap punya satu group
70. Klik [OK], lalu tutup konteks browser kedua (B)

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 2, 11 sampai 13, 21 sampai 24, 26, 30, 31, 33, 37, 38, 40, 44 sampai 46, 48, 51, 52, 54, 55, 57, 61 sampai 64, 70: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state. Langkah 51 (Ganti isi kotak Search tabel All Groups dengan `Scope`, tekan Enter) adalah langkah penghubung (R-16): Search aktif `Scope D` dari langkah 47 menyaring `Scope C` keluar dari tabel, sehingga Search diganti dengan `Scope` agar `Scope C` dan `Scope D` sama-sama terlihat sebelum absence diasersi pada langkah 52.
- Spec FE+BE multi-konteks (kelas c): TC-937, TC-938, dan TC-936 memakai dua konteks UI karena hasil di kedua konteks diasersi. TC-939 sampai TC-942 dan TC-1063 memakai pelaku kedua lewat sesi API (tanpa butir Notes P-2) dan satu konteks UI; tetap berada di spec ini karena seluruhnya skenario race antar admin atas satu objek. Urutan: race yang menambah group dahulu (TC-937, TC-938), race Delete dengan satu akun client utama, lalu race pada akun lain; TC-936 terakhir karena menghapus satu group client khusus. Ganti akun ditulis eksplisit (langkah 45, 54, 62, 64; S-07).
- Pemenang balapan tidak ditentukan oleh TC, sehingga langkah memakai "tepat satu konteks" dan tidak mengasumsikan konteks A atau B (langkah 6 dan 17). Absence penolakan (`Race Del` tidak terhapus dan sejenisnya) didahului verifikasi dialog hasil server yang tampil pada langkah sebelumnya sebagai anchor (langkah 28 dan sejenis, 8b butir 2).
- Menutup popup yang tetap terbuka mengikuti S-08: `✕`, verifikasi dialog `Unsaved Changes`, [Leave].
- Spec berisi lebih dari 35 langkah. Alasan: seluruh blok satu kelas (c, konflik antar admin) dan berdiri sendiri; delapan skenario race pendek, sekitar 20 langkah adalah penghubung (ganti akun, buka halaman, pemicu pelaku kedua lewat API, tutup dialog).
- Client punya lebih dari 10 node level 1 dan page size 10, sehingga baris bernama (`Head Office`, `Rn1`, `Rn2`, `Race Del`, `Race Warn`, `Race Tr`) dicari lewat Search sebelum diklik; `Rn1` dan `Rn2` adalah child `Head Office` sehingga node itu dipilih di sidebar lebih dulu, sedangkan `Race Del`, `Race Warn`, `Race Tr`, `Scope C`, `Scope D`, dan `Scope E` adalah node level 1 seeding (S-03, S-14, R-16). Search tidak terbawa sesudah ganti akun, sehingga langkah 47 mencari `Scope C` dan `Scope D` lewat Search; spec tidak mengasumsikan akun scoped hanya melihat tiga baris.
- Temuan untuk QA:
  - TC-937 dan TC-938 tidak menyebut pesan sukses; spec hanya mengasersi popup tertutup dan hasil di tabel.
  - TC-942 Expected b "dialog would-empty sesuai hasil terbaru" tidak menyebut teks; spec memakai teks dialog would-empty dari TC-259.
  - TC-1063 Precondition menyebut aktor dengan scope Scope C, D, dan E tetapi tidak menyebut cara menetapkan scope; kemampuan seeding disediakan tim FE/BE (R-19).
  - TC-936 Expected a tidak menyebut konteks mana yang menang; dicatat sebagai non-deterministik dan diasersi "tepat satu".
