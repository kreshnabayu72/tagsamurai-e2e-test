---
id: TC-GS-BRAND-E2E-029-bulk-delete-dialog-screening-cancel-dan-blokir
title: "Dialog Bulk Delete: Screening, Cancel, dan Blokir In-Use"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-112
  - TC-GS-BRAND-113
  - TC-GS-BRAND-114
  - TC-GS-BRAND-115
  - TC-GS-BRAND-117
  - TC-GS-BRAND-119
  - TC-GS-BRAND-252
coverage:
  web: automated
---

# Dialog Bulk Delete: Screening, Cancel, dan Blokir In-Use

## Prerequisites

- Mode: FE+BE. Spec hanya membuka dialog Bulk Delete lalu menutupnya lewat [Cancel] atau [OK]; tidak ada brand yang dihapus.
- Akun: Total Control Client A, `Sari Dewi (Sari D)`, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Brand dilakukan sekali di hook `before`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (Last Updated sebelum hari uji) yang dipakai: Orion Tech (bebas relasi), Acme Corp (FAMS Asset Name: Forklift, 1 asset name), Northwind Co (Supply: Copy Paper, 1 item type), Vertex Labs (FAMS: 2 asset names; Supply: 3 item types), Zenith Corp (FAMS: Drill, 1 asset name).
- Seeding: brand bebas relasi Population D-01 yang dipakai spec ini (Iris Optics, Juniper Labs, Keystone Mfg, Harbor Tech, Linear Dynamics) dibuat lewat API di hook `before` dengan nama literal (setara TC-GS-BRAND-1; spec tidak bergantung pada spec lain). Seeding idempotent: brand yang sudah ada dilewati. Spec ini tidak menghapus atau mengubah brand D-01 sehingga aman dipakai bersama spec lain.
- Suite berjalan serial pada Client A (spec 028, 029, dan 035 memakai nama literal Population D-01 yang sama). Dengan 12 brand Pre-setup dan paling banyak 5 brand D-01 spec ini, total paling banyak 17 brand sehingga seluruhnya tampil pada satu halaman dengan page size 25.
- Opsi page size 25 tersedia pada paginasi tabel.
- Cleanup: hook `after` menghapus hanya brand Population yang dibuat spec ini lewat API tanpa berasumsi seeding berhasil penuh, serta memulihkan page size (10) dan seleksi tabel ke default.
- TC-GS-BRAND-112: Orion Tech bebas relasi.
- TC-GS-BRAND-113: Acme Corp in-use.
- TC-GS-BRAND-114 dan TC-GS-BRAND-115: Iris Optics, Juniper Labs, Keystone Mfg bebas relasi (D-01).
- TC-GS-BRAND-117 dan TC-GS-BRAND-252: Harbor Tech dan Linear Dynamics bebas relasi (D-01); Vertex Labs dan Zenith Corp in-use.
- TC-GS-BRAND-119: Vertex Labs dan Northwind Co in-use.

## Test Steps

### TC-GS-BRAND-112: Bulk Delete dengan seleksi 1 brand bebas relasi memakai dialog single

1. Ubah page size tabel menjadi 25
2. Centang Orion Tech
3. Klik `Bulk Action` > `Delete`
4. Verifikasi dialog konfirmasi hapus single (Dialog 1) tampil: title `Delete Brand`, body `• Orion Tech` dan `Are you sure you want to delete it? This action cannot be undone.`
5. Klik [Cancel]
6. Verifikasi dialog tertutup tanpa toast
7. Verifikasi seleksi Orion Tech tetap dan Bulk Action Bar masih tampil

### TC-GS-BRAND-113: Bulk Delete dengan seleksi 1 brand in-use memakai dialog blokir single

8. Klik icon `(✕)` pada Bulk Action Bar
9. Centang Acme Corp
10. Klik `Bulk Action` > `Delete`
11. Verifikasi dialog blokir single sama dengan Delete row Acme Corp: `• Acme Corp`, `- Fixed Asset (1 asset name)`, dan tombol `[OK]`
12. Klik [OK]

### TC-GS-BRAND-114: Screening dialog Bulk Delete homogen bebas relasi (Dialog 4)

13. Klik icon `(✕)` pada Bulk Action Bar
14. Centang Iris Optics, Juniper Labs, dan Keystone Mfg
15. Klik `Bulk Action` > `Delete`
16. Verifikasi title dialog `Delete Brands` (danger)
17. Verifikasi body `The following 3 brands will be deleted:` dengan bullet ketiga nama (Iris Optics, Juniper Labs, Keystone Mfg) di container scrollable
18. Verifikasi teks `Are you sure you want to delete them? This action cannot be undone.`
19. Verifikasi tombol `[Cancel]` dan `[Delete]` (danger)
20. Klik [Cancel]

### TC-GS-BRAND-115: Cancel dialog Bulk Delete homogen mempertahankan seleksi

21. Klik icon `(✕)` pada Bulk Action Bar
22. Centang Iris Optics dan Juniper Labs
23. Klik `Bulk Action` > `Delete`
24. Klik [Cancel]
25. Verifikasi dialog tertutup tanpa toast
26. Verifikasi seleksi 2 brand dan Bulk Action Bar tetap

### TC-GS-BRAND-117: Screening dialog Bulk Delete campuran (Dialog 3)

27. Klik icon `(✕)` pada Bulk Action Bar
28. Centang Harbor Tech, Linear Dynamics, Vertex Labs, dan Zenith Corp
29. Klik `Bulk Action` > `Delete`
30. Verifikasi title dialog `Delete Brands` (warning)
31. Verifikasi teks `The following brands will be deleted:` dengan `• Harbor Tech` dan `• Linear Dynamics`
32. Verifikasi teks `The following brands are currently in use and will be skipped:` dengan `• Vertex Labs (Fixed Asset: 2 asset names, Supply: 3 item types)` dan `• Zenith Corp (Fixed Asset: 1 asset name)`
33. Verifikasi teks `Are you sure you want to continue?` dengan tombol `[Cancel]` dan `[Continue]` (filled, danger)
34. Klik [Cancel]

### TC-GS-BRAND-252: Cancel dialog Bulk Delete campuran mempertahankan seleksi

35. Klik icon `(✕)` pada Bulk Action Bar
36. Centang Harbor Tech dan Zenith Corp
37. Klik `Bulk Action` > `Delete`
38. Verifikasi dialog campuran tampil
39. Klik [Cancel]
40. Verifikasi dialog tertutup tanpa toast
41. Verifikasi seleksi 2 brand dan Bulk Action Bar tetap
42. Verifikasi Harbor Tech dan Zenith Corp tetap ada di tabel

### TC-GS-BRAND-119: Bulk Delete seluruhnya in-use memakai dialog blokir dengan bullet per brand

43. Klik icon `(✕)` pada Bulk Action Bar
44. Centang Vertex Labs dan Northwind Co
45. Klik `Bulk Action` > `Delete`
46. Verifikasi dialog `Cannot Delete Brand` memuat `• Vertex Labs` dengan breakdown-nya (`- Fixed Asset (2 asset names)`, `- Supply (3 item types)`) dan `• Northwind Co` dengan `- Supply (1 item type)`
47. Verifikasi penutup dialog `Please remove these references before deleting these brands.`
48. Verifikasi dialog hanya punya tombol `[OK]`
49. Verifikasi tidak ada toast
50. Klik [OK]
51. Verifikasi seleksi Vertex Labs dan Northwind Co tetap setelah [OK]
52. Klik icon `(✕)` pada Bulk Action Bar

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Notasi `Dialog n` merujuk dialog PRD `brand.md` §4.2g (Dialog 1 hapus single, Dialog 3 campuran, Dialog 4 homogen); notasi `D-xx` hanya untuk data uji (Population D-01).
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 (page size 25 supaya seluruh brand yang dicentang berada pada halaman yang sama dengan default urutan A-Z), 8, 13, 21, 27, 35, 43, dan 52 (klik `(✕)` untuk memulai TC berikutnya dari seleksi bersih dan membersihkan seleksi akhir), serta 12, 20, dan 34 (menutup dialog yang di TC sumber tidak ditutup).
- Urutan TC dalam spec: TC-GS-BRAND-252 ditaruh sebelum TC-GS-BRAND-119 supaya dialog campuran (117 dan 252) berurutan; urutan sumber 117, 119, 252 tidak mengubah hasil karena tidak ada TC yang menghapus data.
- Spec ini melebihi sekitar 35 langkah karena memuat tujuh TC dialog pada dataset dan layar yang sama; semua TC non-destruktif sehingga kegagalan satu TC tidak menutupi TC berikutnya.
- Aksi yang benar-benar menghapus (konfirmasi [Delete] dan [Continue]) diuji di spec `TC-GS-BRAND-E2E-030-bulk-delete-sukses-homogen-campuran-dan-double-click`.
