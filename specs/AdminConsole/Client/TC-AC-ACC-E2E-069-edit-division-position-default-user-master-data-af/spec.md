---
id: TC-AC-ACC-E2E-069-edit-division-position-default-user-master-data-af
title: "Edit Division dan Position Default User: Dropdown, Wajib, Stale, Dikosongkan, dan Changelog (Active-Full)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-150
  - TC-AC-ACC-151
  - TC-AC-ACC-152
  - TC-AC-ACC-474
  - TC-AC-ACC-472
  - TC-AC-ACC-473
  - TC-AC-ACC-542
coverage:
  web: automated
---

# Edit Division dan Position Default User: Dropdown, Wajib, Stale, Dikosongkan, dan Changelog (Active-Full)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login akun Active-Full di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya. `{r6}` = 6 digit terakhir `{runId}` (dipakai agar Client Code tetap maksimal 15 karakter).
- Dataset seed (nama bersuffix): Client `PT Teknologi Maju {runId}-069` (replika C-02: Active, Partner CV Mitra Sejati sebagai Anchor dan CV Mitra Lestari, Group Area Jakarta, FAMS Grace, Photo tersimpan, Client Code `TKM-{r6}`, Default User Not Yet Activated dengan Division seed `Finance` dan Position seed `Finance Manager`); Client `PT Posisi Kosong {runId}-069` (replika C-02 dengan Division `Finance` dan Position `Finance Manager`, Default User Not Yet Activated, dipakai TC-472); Client `PT Baru Daftar {runId}-069` (replika C-09: Direct, Group Cabang Menteng, tanpa subscription, tenant tanpa Position, Default User `hadi.prasetyo+{runId}-069@qwertysystem.net`, dipakai TC-473); Client `PT Pilihan Master {runId}-069` (replika C-EDT-4: Direct, Group Area Jakarta, tanpa subscription, Default User Not Yet Activated, Division `Finance` dan `Operations`, Position `Finance Manager` dan `Operations Lead`, dipakai TC-542); Division sementara `Divisi Uji Hapus {runId}-069` pada tenant `PT Teknologi Maju {runId}-069` (dihapus pelaku kedua pada TC-152).
- Pelaku kedua (menghapus Division dan Position) memakai sesi API. Kemampuan teknis: membaca Global Settings tenant Client > Position dan User (cara masuk tidak dijelaskan TC; disediakan tim FE/BE), serta membaca System Log (Settings > User > Detail akun aktor) dan Activity Log dengan Search nama Client unik (baseline nol, S-12). Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Cleanup: hook `after` menghapus Client seed lewat API dan membuat ulang Position yang dihapus.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-150, TC-151, TC-152, TC-474: Dropdown, wajib, dan stale pada PT Teknologi Maju

1. Ketik Search `PT Teknologi Maju {runId}-069`, tekan Enter
2. Buka `⋯` baris `PT Teknologi Maju {runId}-069` lalu klik `Edit`
3. Buka dropdown Division
4. Verifikasi dropdown Division menampilkan minimal 1 opsi hasil seed Create
5. Buka dropdown Position
6. Verifikasi field Position berupa dropdown single-select (bukan input teks) dengan Position terisi "Finance Manager"
7. Verifikasi opsi Position hanya hasil seed Create ("Finance Manager")
8. Kosongkan pilihan Division
9. Klik `[Save]`
10. Verifikasi pesan error "Division must not be empty"
11. Pilih Division "Divisi Uji Hapus {runId}-069"
12. Pelaku kedua (sesi API) menghapus Division "Divisi Uji Hapus {runId}-069" hingga terhapus
13. Tunggu aksi selesai
14. Klik `[Save]`
15. Verifikasi pesan error "This division no longer exists. Please select another."
16. Verifikasi pilihan Division dikosongkan dan opsi dimuat ulang
17. Verifikasi field lain dipertahankan (Company Name "PT Teknologi Maju {runId}-069")
18. Pilih Division "Finance"
19. Ganti isi Fax dengan `0215550100`
20. Pelaku kedua (sesi API) menghapus Position "Finance Manager" hingga terhapus
21. Tunggu aksi selesai
22. Klik `[Save]`
23. Verifikasi pesan error "This position no longer exists. Please select another."
24. Verifikasi pilihan Position dikosongkan dan opsi dimuat ulang
25. Verifikasi Fax tetap "0215550100"
26. Klik `[✕]` di header popup
27. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
28. Klik `[Leave]`

### TC-472: Position dikosongkan, tautan dilepas

29. Ketik Search `PT Posisi Kosong {runId}-069`, tekan Enter
30. Buka `⋯` baris `PT Posisi Kosong {runId}-069` lalu klik `Edit`
31. Kosongkan pilihan Position
32. Klik `[Save]`
33. Verifikasi popup tertutup
34. Verifikasi toast sukses "Success, client has been updated."
35. Buka Global Settings tenant Client > Position
36. Verifikasi Position "Finance Manager" tetap ada
37. Buka Global Settings tenant Client > User dan lihat Default User
38. Verifikasi Default User tidak memiliki Position (kosong)

### TC-473: Tenant tanpa Position

39. Buka Admin Console > Client
40. Ketik Search `PT Baru Daftar {runId}-069`, tekan Enter
41. Buka `⋯` baris `PT Baru Daftar {runId}-069` lalu klik `Edit`
42. Buka dropdown Position
43. Verifikasi dropdown Position menampilkan "No options available"
44. Verifikasi field Position opsional (tanpa penanda wajib dan tanpa pesan error)
45. Klik `[✕]` di header popup

### TC-542: Ubah Division dan Position tercatat di tiga log

46. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Pilihan Master {runId}-069`, tekan Enter
47. Catat jumlah baris hasil Search sebagai N
48. Tutup modal Changelog
49. Ketik Search `PT Pilihan Master {runId}-069`, tekan Enter
50. Buka `⋯` baris `PT Pilihan Master {runId}-069` lalu klik `Edit`
51. Pilih Division "Operations"
52. Pilih Position "Operations Lead"
53. Klik `[Save]`
54. Verifikasi popup tertutup
55. Verifikasi toast sukses "Success, client has been updated."
56. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Pilihan Master {runId}-069`, tekan Enter
57. Verifikasi jumlah baris hasil Search menjadi N + 2
58. Verifikasi dua baris terbaru (Date hari ini, urutan bebas) Action `Edit`, Client Name "PT Pilihan Master {runId}-069", Modified By aktor: Field `Default User Division` (Old Value `Finance`, New Value `Operations`) dan Field `Default User Position` (Old Value `Finance Manager`, New Value `Operations Lead`)
59. Buka Settings > User > Detail akun aktor > Tab System Log, cari `PT Pilihan Master {runId}-069`
60. Verifikasi System Log memuat dua baris baru dengan Object `Client`, Name "PT Pilihan Master {runId}-069", Field `Default User Division` dan `Default User Position` dengan Old Value dan New Value sama dengan Changelog
61. Buka Activity Log Admin Console, cari `PT Pilihan Master {runId}-069`
62. Verifikasi Activity Log memuat dua baris yang sama dengan System Log, Modified By aktor

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Alasan di atas 35 langkah (sekitar 75 langkah): satu role (Active-Full), satu topik (Division dan Position Default User), empat Client seed milik sendiri; blok stale menghapus master data tenant milik Client seed sehingga berada di akhir blok pertama (prinsip 5); tiap blok berdiri sendiri.
- Pelaku kedua memakai sesi API hingga Division dan Position terhapus (R-20); bukan konteks UI kedua.
- Langkah penghubung (S-03): "Pilih Division Finance" memulihkan nilai sebelum TC-474 agar hanya error Position yang teramati; penutup form dirty (S-08); Search nama unik; baseline N diambil di Changelog sebelum aksi (S-12).
- Temuan untuk QA:
  - TC-150 butir b menyebut placeholder "Select position" sementara Position terisi "Finance Manager"; placeholder tampil hanya saat kosong, jadi tidak diasersi pada keadaan terisi (placeholder kosong diasersi di TC-135).
  - TC-152 dan TC-474 menulis "sesi lain" tanpa menyebut mekanisme; spec memakai sesi API.
  - TC-472 dan TC-473 tidak menyebut cara masuk ke Global Settings tenant Client; kemampuan itu ditulis di Prerequisites sebagai disediakan tim FE/BE.
