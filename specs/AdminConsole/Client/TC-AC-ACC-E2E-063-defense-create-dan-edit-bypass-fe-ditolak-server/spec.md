---
id: TC-AC-ACC-E2E-063-defense-create-dan-edit-bypass-fe-ditolak-server
title: "Defense: Create dan Edit Client dengan Request Dimanipulasi Ditolak Server"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-156
  - TC-AC-ACC-159
  - TC-AC-ACC-948
  - TC-AC-ACC-126
  - TC-AC-ACC-947
  - TC-AC-ACC-160
coverage:
  web: automated
---

# Defense: Create dan Edit Client dengan Request Dimanipulasi Ditolak Server

## Prerequisites

- Mode: FE+BE. Kelas defense-in-depth (K-1): request langsung ke server dan request UI yang dimanipulasi; aksi tulis yang ditolak tidak mengubah data.
- Akun aktor (urutan): Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`; Active-Create-Only (A-05) `activeCreateJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_CREATE_PASSWORD`; Active-Update-Only (A-06) `activeUpdateJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_UPDATE_PASSWORD`; Archived-Read (A-08) `archivedReadJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ARCHIVED_READ_PASSWORD`. Login akun Active-Full di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Kemampuan teknis: klien HTTP berautentikasi sebagai aktor yang sedang login (request langsung ke server, tanpa browser), `Spectra.intercept()` untuk memodifikasi body request yang dikirim UI, dan seeding lewat API/fixture BE. Endpoint tidak dikarang; disediakan tim FE/BE.
- Dataset seed (nama bersuffix): `PT Sejahtera Abadi {runId}-063` (Active, Default User Activated, setara C-01), `PT Wahana Nusantara {runId}-063` (Suspended, FAMS Expired, setara C-03; Fax awal tercatat), `PT Maju Bersama {runId}-063` (Active Derived, Client Code `MJB-{r6}`, Group Area Jakarta, setara C-06), `PT Direct Jakarta {runId}-063` (Direct, Group Area Jakarta, Fax kosong, setara C-ROL-13), `PT Karya Abadi {runId}-063` (Archived, Group Area Jakarta, setara C-04). `{r6}` = 6 digit terakhir `{runId}` (dipakai agar Client Code tetap maksimal 15 karakter). Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Tabel Anggota Default User (TC-156; anggota | nilai pengganti):
  - First Name | Budi Baru
  - Last Name | Santoso Baru
  - Email | budi.baru+{runId}-063@qwertysystem.net
  - Division | Operations
  - Position | Operations Lead
- Tabel Anggota Reflected Client Derived (TC-948; anggota | nilai pengganti pada request):
  - Company Name | PT Maju Bersama Ubah {runId}-063
  - Company Email | bypass.company@qwertysystem.net
  - Industry | Finance & Banking
  - Website | bypass.example.com
  - Fax | 021-5550102
  - Address | Jl. Bypass No. 1
  - Country | Singapore
  - State | Central Region
  - City | Singapore
  - Postal Code | 123456
  - PIC Name | Bypass Uji
  - PIC Email | bypass.uji@qwertysystem.net
  - PIC Phone | 081399990000
- Dataset Dinamis TC-126: `PT Intersep Create {runId}-063` (Default User `Sari Pratiwi`, Email `intersep.create+{runId}-063@qwertysystem.net`).
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### Aktor Active-Full: TC-156 Default User Activated

1. Ketik Search `PT Sejahtera Abadi {runId}-063`, tekan Enter
2. Klik Company Name `PT Sejahtera Abadi {runId}-063` untuk membuka Detail
3. Catat Name, Email, Division, Position, dan status Default User "PT Sejahtera Abadi {runId}-063" dari Detail (nilai awal)
4. Untuk setiap baris tabel Anggota Default User, lakukan langkah 5 sampai 6
5. Kirim request Edit langsung (klien HTTP) untuk "PT Sejahtera Abadi {runId}-063" dengan anggota baris tabel bernilai pengganti
6. Verifikasi respons ditolak server (status bukan 2xx)
7. Muat ulang Detail "PT Sejahtera Abadi {runId}-063"
8. Verifikasi Name, Email, Division, dan Position Default User sama seperti nilai awal
9. Verifikasi status Default User "Activated"

### TC-159: Edit Client Suspended

10. Klik breadcrumb "Client" untuk kembali ke List
11. Klik sub-tab Suspended
12. Ketik Search `PT Wahana Nusantara {runId}-063`, tekan Enter
13. Klik Company Name `PT Wahana Nusantara {runId}-063` untuk membuka Detail dan catat nilai Fax (F0)
14. Kirim request Edit langsung untuk "PT Wahana Nusantara {runId}-063" (Suspended) dengan Fax `0215550177`
15. Verifikasi respons 403 Forbidden
16. Muat ulang Detail "PT Wahana Nusantara {runId}-063"
17. Verifikasi Fax sama dengan F0 (bukan `0215550177`)

### TC-948: Field Reflected Client Derived

18. Klik breadcrumb "Client" untuk kembali ke List
19. Klik sub-tab Active
20. Ketik Search `PT Maju Bersama {runId}-063`, tekan Enter
21. Klik Company Name `PT Maju Bersama {runId}-063` untuk membuka Detail
22. Catat Client Code, Company Name, Company Email, Industry, Website, Fax, Address, Country, State, City, Postal Code, PIC Name, PIC Email, dan PIC Phone (nilai awal)
23. Untuk setiap baris tabel Anggota Reflected, lakukan langkah 24 sampai 30
24. Klik `[Edit]` di header Detail, ubah Client Code menjadi `DRV-948`, lalu klik `[Save]` dengan request Edit dimanipulasi (intercept) sehingga anggota baris tabel bernilai pengganti
25. Verifikasi request ditolak server
26. Verifikasi toast error "Error, failed to update client."
27. Verifikasi popup tetap terbuka
28. Klik `[✕]` di header popup
29. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
30. Klik `[Leave]`
31. Muat ulang halaman (F5)
32. Verifikasi Detail menampilkan seluruh anggota Reflected sama dengan nilai awal
33. Verifikasi Client Code bukan "DRV-948" (seluruh request ditolak termasuk perubahan Client Code)

### Aktor Active-Create-Only: TC-126

34. `Logout`, lalu login sebagai Active-Create-Only (A-05)
35. Klik `[+ New Client]`
36. Isi Company Name `PT Intersep Create {runId}-063`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Default User Sari Pratiwi dengan Email `intersep.create+{runId}-063@qwertysystem.net`, Select Group dikosongkan
37. Pilih Group "Area Jakarta" pada tree Select Group
38. Verifikasi tree Select Group menampilkan "Area Jakarta" terpilih
39. Klik `[Submit]` dengan request Create dimanipulasi (intercept) sehingga Group bernilai Area Surabaya
40. Verifikasi request ditolak server
41. Verifikasi toast error "Error, failed to create client."
42. Verifikasi popup tetap terbuka
43. Klik `[✕]` di header popup
44. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
45. Klik `[Leave]`

### Aktor Active-Update-Only: TC-947

46. `Logout`, lalu login sebagai Active-Update-Only (A-06)
47. Ketik Search `PT Direct Jakarta {runId}-063`, tekan Enter
48. Buka `⋯` baris `PT Direct Jakarta {runId}-063` lalu klik `Edit`
49. Ubah Fax menjadi `021-5550100`
50. Klik `[Save]` dengan request Edit dimanipulasi (intercept) sehingga Group bernilai Area Surabaya
51. Verifikasi request ditolak server
52. Verifikasi toast error "Error, failed to update client."
53. Verifikasi popup tetap terbuka
54. Klik `[✕]` di header popup
55. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
56. Klik `[Leave]`
57. Ketik Search `PT Direct Jakarta {runId}-063`, tekan Enter
58. Verifikasi baris "PT Direct Jakarta {runId}-063" tetap tampil dengan Group "Area Jakarta"
59. Klik `⋯` baris "PT Direct Jakarta {runId}-063" lalu klik `Detail`
60. Verifikasi Detail tidak menampilkan Fax "021-5550100"

### Aktor Archived-Read: TC-160

61. `Logout`, lalu login sebagai Archived-Read (A-08)
62. Klik sub-tab Archived
63. Ketik Search `PT Karya Abadi {runId}-063`, tekan Enter
64. Buka `⋯` baris "PT Karya Abadi {runId}-063"
65. Verifikasi menu `⋯` hanya memuat `Detail` (Edit Hidden)
66. Kirim request Edit langsung untuk "PT Karya Abadi {runId}-063" dengan PIC Name `Hendra Pratama`
67. Verifikasi respons ditolak server (Client dalam scope aktor, bukan 404 netral)
68. Klik Company Name `PT Karya Abadi {runId}-063` untuk membuka Detail
69. Verifikasi Detail tidak menampilkan PIC Name "Hendra Pratama"

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- K-1: TC-156, TC-159, TC-948, TC-126, TC-947, TC-160 adalah TC defense-in-depth (kelas a) dengan Expected respons API; BE mencatatnya di tingkat endpoint, TC granular tetap sumber.
- Request langsung ke server (TC-156, TC-159, TC-160 langkah request) hanya mengasersi status respons dan state data; toast error dan perilaku FE pada request langsung tidak disalin (butir 8b-1). Request yang dimanipulasi di UI (TC-948, TC-126, TC-947) tetap mengasersi toast dan popup karena melewati browser.
- Alasan di atas 35 langkah (sekitar 75 langkah setelah ekspansi): satu kelas harness (defense), empat role dengan Step ganti akun eksplisit, tiap blok memakai Client seed milik sendiri dan berdiri sendiri; hook `after` mengembalikan sesi ke akun default suite (S-07).
- Langkah penghubung (S-03): Search nama unik, Detail, muat ulang Detail (langkah 7), breadcrumb "Client", sub-tab; penutup form dirty (S-08). Langkah 5 sampai 6 diulang untuk 5 baris dan 24 sampai 30 untuk 13 baris.
- Temuan untuk QA:
  - TC-156 Expected butir a, TC-159 butir a, dan TC-160 butir b menyebut toast error "Error, failed to update client." atau toast baku function untuk request langsung; sesuai butir 8b-1 toast tidak diasersi pada request langsung. Perilaku FE untuk respons yang sama ada di jalur form (TC-164, TC-637).
  - TC-159 Expected butir a: toast "Changes can't be saved while this workspace is suspended or expired." muncul dari jalur UI pada TC-637; pada request langsung tidak diasersi.
  - TC-948 langkah 5: perubahan Client Code `DRV-948` dikirim bersama anggota Reflected; Expected butir n menegaskan seluruh request ditolak.
