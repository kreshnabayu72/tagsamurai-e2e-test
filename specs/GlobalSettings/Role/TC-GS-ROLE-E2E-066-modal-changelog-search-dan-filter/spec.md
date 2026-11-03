---
id: TC-GS-ROLE-E2E-066-modal-changelog-search-dan-filter
title: "Modal Changelog: Search per Kelas Kolom dan Filter Varian Tab Total Control, System, dan Detail"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-199
  - TC-GS-ROLE-200
  - TC-GS-ROLE-201
coverage:
  web: automated
---

# Modal Changelog: Search per Kelas Kolom dan Filter Varian Tab Total Control, System, dan Detail

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Ahmad Fauzi (`Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: kembali ke layar Global Settings > Role & Permission > System.
- Seeding (lewat API oleh akun Ahmad Fauzi di hook `before`, urutan sebagai berikut; kemampuan dari `openapi.yaml`: POST/DELETE `/v2/iam/products/{product}/roles/access-level`, POST/PATCH/DELETE `/v2/iam/products/{product}/roles/capabilities/users`; asumsi seeding lewat API mencatat entri Changelog sama seperti aksi UI). Hanya data yang dipakai `Verifikasi` yang di-seed (S-11):
  - Sari Wulandari (Pre-setup #11): Assign Read Only, lalu Assign Total Control (upgrade; entri dengan Old Value `Read Only`), lalu Remove Total Control (entri `Remove`).
  - Fikri Ramadhan (Pre-setup #18): Assign Total Control, lalu Edit CRUD Update baris Manage TAG dari checked ke unchecked sehingga memicu Auto-Revert (entri `Auto-Revert` di Tab Total Control).
  - Citra Dewanti (Pre-setup #18): Assign Role Manage TAG (entri `Assign`, Field `Access`), lalu Remove baris Manage TAG (entri `Remove`).
  - Hendra Wijaya (Pre-setup #5): Edit CRUD Update pada baris Manage TAG milik sendiri diubah lalu dikembalikan ke nilai semula (dua entri `Edit`, Field `Update`, Old Value dan New Value `Active` dan `Inactive`).
  - Doni Pratama (Pre-setup #10): Edit CRUD Delete pada baris Manage files diubah dari checked ke unchecked lalu dikembalikan (dua entri `Edit`, Field `Delete`).
- Pemulihan di hook `after` (tetap jalan walau spec gagal di tengah): Sari Wulandari, Fikri Ramadhan, dan Citra Dewanti dikembalikan ke kondisi kandidat Pre-setup #11 dan #18 (Active, Access Global Settings dicentang, tanpa access level, tanpa baris role) lewat API; nilai CRUD baris Hendra Wijaya (Manage TAG) dan Doni Pratama (Manage files) kembali ke nilai Pre-setup; Modal Changelog ditutup. Entri Changelog tidak bisa dihapus. Pengubahan baris Pre-setup Hendra Wijaya dan Doni Pratama dipulihkan dalam spec yang sama (S-06).
- Tabel Filter Tab Total Control (parameter perulangan TC-GS-ROLE-200):

| Filter | Nilai yang dipilih | Kriteria baris hasil |
|---|---|---|
| Action | `Remove` | semua baris Action `Remove` |
| User Name | `Sari Wulandari` | semua baris User Name `Sari Wulandari` |
| Modified By | `Ahmad F` | semua baris Modified By `Ahmad F` |
| Date | rentang tanggal hari ini (tanggal run) sampai tanggal hari ini | semua baris Date berada dalam rentang |

- Tabel Filter Tab System (parameter perulangan TC-GS-ROLE-201):

| Filter | Nilai yang dipilih | Kriteria baris hasil |
|---|---|---|
| Role — User | `Manage TAG — Hendra Wijaya` | semua baris Role — User `Manage TAG — Hendra Wijaya` |
| Field | `Update` | semua baris Field `Update` |
| Action | `Edit` | semua baris Action `Edit` |

- Kemampuan teknis: membaca nilai kolom Date baris teratas Modal Changelog; membaca format tanggal dan jam General Settings yang berlaku (spec tidak mengubahnya).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-199: Search Modal Changelog per kelas kolom

1. Klik icon Changelog di Table Tools
2. Catat nilai kolom Date baris teratas
3. Ketik Search `assign`, tekan Enter
4. Verifikasi entri Action `Assign` untuk Citra Dewanti tampil
5. Ganti isi kotak search dengan `hendra`, tekan Enter
6. Verifikasi entri Role — User `Manage TAG — Hendra Wijaya` tampil
7. Ganti isi kotak search dengan `Delete`, tekan Enter
8. Verifikasi entri Field `Delete` tampil
9. Ganti isi kotak search dengan `inactive`, tekan Enter
10. Verifikasi entri dengan Old Value atau New Value `Inactive` tampil
11. Ganti isi kotak search dengan `ahmad`, tekan Enter
12. Verifikasi entri Modified By `Ahmad F` tampil
13. Ganti isi kotak search dengan nilai Date yang dicatat pada langkah 2, tekan Enter
14. Verifikasi "No results found"
15. Klik `(←)` pada kotak Search
16. Tutup Modal Changelog lewat `[✕]`
17. Klik Tab `Total Control`
18. Klik icon Changelog di Table Tools
19. Ketik Search `sari`, tekan Enter
20. Verifikasi entri User Name `Sari Wulandari` tampil
21. Ganti isi kotak search dengan `read only`, tekan Enter
22. Verifikasi entri dengan Old Value `Read Only` tampil
23. Klik `(←)` pada kotak Search

### TC-GS-ROLE-200: Filter Modal Changelog Tab Total Control dan Tab Read Only

24. Klik icon Filter di modal
25. Verifikasi field Date `Select date` (date range)
26. Verifikasi field Action `All actions`
27. Verifikasi field User Name `All users`
28. Verifikasi field Modified By `All users` (multi-select searchable)
29. Verifikasi tidak ada field Field
30. Buka dropdown Action
31. Verifikasi opsi Action hanya `Assign`, `Remove`, dan `Auto-Revert`
32. Tutup dropdown Action dengan Esc
33. Untuk setiap baris tabel Filter Tab Total Control (langkah 33 sampai 37): pilih nilai filter sesuai kolom "Nilai yang dipilih"
34. Klik `[Apply]`
35. Verifikasi sedikitnya satu baris tampil
36. Verifikasi baris hasil sesuai kolom "Kriteria baris hasil" pada tabel
37. Klik `[Clear Field]`
38. Tutup Modal Changelog lewat `[✕]`

### TC-GS-ROLE-201: Filter Modal Changelog Tab System dan Detail

39. Klik Tab `System`
40. Klik icon Changelog di Table Tools
41. Klik icon Filter di modal
42. Verifikasi field Date
43. Verifikasi field Action `All actions`
44. Verifikasi field Role — User `All roles — users`
45. Verifikasi field Field `All fields`
46. Verifikasi field Modified By `All users`
47. Buka dropdown Action
48. Verifikasi opsi Action hanya `Edit`, `Assign`, dan `Remove`
49. Tutup dropdown Action dengan Esc
50. Untuk setiap baris tabel Filter Tab System (langkah 50 sampai 54): pilih nilai filter sesuai kolom "Nilai yang dipilih"
51. Klik `[Apply]`
52. Verifikasi sedikitnya satu baris tampil
53. Verifikasi baris hasil sesuai kolom "Kriteria baris hasil" pada tabel
54. Klik `[Clear Field]`
55. Tutup Modal Changelog lewat `[✕]`
56. Klik Role Name `Manage TAG`
57. Klik icon Changelog di Table Tools
58. Klik icon Filter di modal
59. Buka dropdown Field
60. Verifikasi opsi Field `Update` tampil
61. Verifikasi opsi Field `Access` tampil
62. Verifikasi dropdown Field tidak memuat opsi `Create` dan `Delete`
63. Tutup dropdown Field dengan Esc
64. Tutup Modal Changelog lewat `[✕]`

## Notes

- Sumber TC: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (199, 200, 201) dipertahankan; TC-GS-ROLE-199 memakai Tab System untuk enam Search pertama lalu Tab Total Control untuk Search User Name, Old Value, dan New Value.
- Langkah 33 sampai 37 diulang untuk empat baris tabel Filter Tab Total Control, dan langkah 50 sampai 54 untuk tiga baris tabel Filter Tab System.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2 (mencatat Date untuk Search Date), langkah 15 dan 23 (menutup kotak Search), langkah 16, 38, 55, dan 64 (menutup Modal Changelog), langkah 17, 39 (pindah tab), langkah 32, 49, dan 63 (menutup dropdown), langkah 37 dan 54 (`[Clear Field]` pada tiap iterasi mengosongkan filter, S-09), dan langkah 56 (membuka Detail "Manage TAG" lewat Role Name).
- Langkah 35 dan 52 (sedikitnya satu baris tampil) adalah anchor positif untuk asersi universal "semua baris" pada langkah 36 dan 53 (bagian 8b butir 2). Langkah 14 ("No results found") menjadi anchor positif untuk absence hasil Search Date.
- Spec melewati sekitar 35 langkah (64 langkah nominal, sekitar 85 dengan ekspansi dua blok ulang) karena tiap klausa Expected dipecah menjadi satu `Verifikasi` (S-01) dan Search serta Filter dilakukan pada empat varian modal. Semuanya satu kelas harness (Search dan Filter Modal Changelog), satu akun, dan satu dataset seeding; tiap blok TC berdiri sendiri (membuka modalnya sendiri), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-ROLE-199 dan 201 menyebut precondition "entry Edit dan Assign" tanpa menyebut cara menyediakannya; spec men-seed entri lewat API (Prerequisites). Pengubahan baris Manage TAG Hendra Wijaya dan Manage files Doni Pratama memakai baris Pre-setup dan dipulihkan.
  - TC-GS-ROLE-199 Langkah Uji 7 dan Expected g menyebut Old Value dan New Value bernilai Read Only pada Changelog Tab Total Control; entri dengan New Value `Read Only` dicatat di Changelog Tab Read Only, bukan Tab Total Control, sehingga spec hanya mengasersi entri dengan Old Value `Read Only` (upgrade).
  - TC-GS-ROLE-199 Langkah Uji 6 ("Tanggal entry") tidak menyebut format tanggal; spec memakai nilai kolom Date yang dibaca dari tabel.
  - TC-GS-ROLE-200 Langkah Uji 5 ("Filter Date rentang") tidak menyebut rentang; spec memakai rentang tanggal hari ini, sehingga entri di luar rentang tidak diasersi tidak tampil.
  - TC-GS-ROLE-201 Expected d ("tidak ada opsi untuk kolom yang tidak pernah tercatat") tidak menyebut kolom yang dimaksud; spec memakai `Create` dan `Delete` karena Detail "Manage TAG" hanya memiliki kolom Read dan Update.
