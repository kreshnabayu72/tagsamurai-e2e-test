---
id: TC-FA-LIC-E2E-013-tab-allocation-quota-context-header-group-quota-summary
title: "Tab Allocation Quota: Context Header, Group Quota Summary, Badge Not Allocated, dan Remaining Grup Belum Beralokasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-45
  - TC-FA-LIC-46
  - TC-FA-LIC-49
  - TC-FA-LIC-50
  - TC-FA-LIC-51
  - TC-FA-LIC-61
  - TC-FA-LIC-538
coverage:
  web: automated
---

# Tab Allocation Quota: Context Header, Group Quota Summary, Badge Not Allocated, dan Remaining Grup Belum Beralokasi

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (client PT Sejahtera, plan Professional (Paid), `License allocation per group` ON; kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > License dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #12: Total Asset License 5.000; hierarki Produksi, Kantor Pusat (GRP-HQ; Total 1500, Allocated to Subgroups 600, Used 700, Reserved 0, Remaining 200; anak Divisi Logistik, Divisi IT, Divisi Keuangan (GRP-FIN, belum beralokasi)), Cabang Surabaya, Cabang Medan. Nilai dibaca dari `Fixture.fixedAssetLicense.*`; berkas fixture belum ada, disediakan tim FE.
- State yang diubah spec dan dipulihkan: (1) grup level 1 `Cabang Medan` dijadikan belum beralokasi dengan Used 880 sehingga Total Allocated tanpa Cabang Medan 3.800 (TC-FA-LIC-46 dan TC-FA-LIC-51, langkah 22); (2) grup baru `Divisi Umum+{runId}-013` dibuat di bawah Kantor Pusat (TC-FA-LIC-61, langkah 31; padanan `Divisi Umum` pada TC bersuffix per run). Langkah 38 dan hook `after` memulihkan alokasi Cabang Medan ke Pre-setup #12 dan menghapus grup `Divisi Umum+{runId}-013`. Fixture BE penyetel dan pemulih Pre-setup #12 disediakan tim FE/BE; pembuatan grup lewat Settings > Groups tidak dilakukan lewat UI.
- Hook dan kemampuan suite (flag Guided Tooltip seen, sesi API aktor, fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-LIC-45: Screening Tab Allocation Quota default

1. Klik Tab `Allocation Quota`
2. Verifikasi Context Header `All Groups`
3. Verifikasi tidak ada badge `Not Allocated` pada Context Header
4. Verifikasi Section 1 berjudul `All License` berisi tabel License Summary tanpa aksi Edit
5. Verifikasi Section 2 berjudul `Level 1 Groups Quota` berisi 4 grup level 1: Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat
6. Verifikasi Sidebar Group Tree di kanan dengan node pertama `All Groups` terpilih

### TC-FA-LIC-49: Node grup beralokasi

7. Klik node `Kantor Pusat`
8. Verifikasi Context Header `Kantor Pusat (GRP-HQ)` tanpa badge `Not Allocated`
9. Verifikasi Section 1 `Group Quota`, tabel Group Quota Summary: `Total` 1500, `Allocated to Subgroups` 600, `Used by This Group` 700, `Reserved by This Group` 0, `Remaining` 200
10. Verifikasi kolom addon (`+ Audit`, `+ Tracking`, `+ Maintenance Routine`, `+ Repair Ticketing`, `+ Maps`, `+ IT Inventory`) bernilai `—` pada kelima baris termasuk `Total`
11. Verifikasi Section 2 `Child Groups Quota` berisi 3 baris: Divisi Logistik, Divisi IT, Divisi Keuangan
12. Verifikasi tombol ikon `[Edit]` tampil di samping nilai `Total` (1500)

### TC-FA-LIC-50: Node grup belum beralokasi

13. Klik node `Divisi Keuangan`
14. Verifikasi Context Header `Divisi Keuangan (GRP-FIN)` dengan badge `Not Allocated`
15. Verifikasi Group Quota Summary: `Total` `—`, `Allocated to Subgroups` `—`, `Used by This Group` 0, `Reserved by This Group` 0, `Remaining` 200
16. Arahkan kursor ke nilai `Remaining`
17. Verifikasi tooltip `Shared from Kantor Pusat` pada nilai `Remaining`
18. Verifikasi tombol ikon `[Edit]` tampil di samping `—` pada `Total`

### TC-FA-LIC-538: Badge Not Allocated komponen Badge varian Light

19. Verifikasi Badge `Not Allocated` pada Context Header `Divisi Keuangan (GRP-FIN)` berupa komponen `Badge` varian `Light` dengan severity default komponen (bukan `success`, `warning`, `danger`, `primary`, atau `dark`)
20. Klik node `Kantor Pusat`
21. Verifikasi Context Header `Kantor Pusat (GRP-HQ)` tidak memuat badge

### TC-FA-LIC-46: Helper Available unallocated pool

22. Jadikan grup level 1 `Cabang Medan` belum beralokasi dengan Used 880 lewat fixture BE, lalu muat ulang halaman License
23. Klik Tab `Allocation Quota`
24. Klik `[Edit]` pada baris `Kantor Pusat` di Section 2 (node `All Groups`)
25. Verifikasi helper `Available unallocated pool: 320 units.` (5,000 − 3,800 − 880)
26. Tutup modal Edit Allocation dengan `[×]`

### TC-FA-LIC-51: Remaining grup level 1 belum beralokasi

27. Klik node `Cabang Medan`
28. Arahkan kursor ke nilai `Remaining`
29. Verifikasi `Remaining` sama dengan sisa pool organisasi (320, nilai helper pada langkah 25)
30. Verifikasi tooltip `Shared from organization pool`

### TC-FA-LIC-61: Default alokasi grup baru

31. Buat grup `Divisi Umum+{runId}-013` di bawah Kantor Pusat lewat fixture BE, lalu muat ulang halaman License
32. Klik Tab `Allocation Quota`
33. Klik node `Kantor Pusat`
34. Klik nama grup `Divisi Umum+{runId}-013` pada Section 2 `Child Groups Quota`
35. Verifikasi Context Header memuat badge `Not Allocated`
36. Verifikasi Group Quota Summary: `Total` `—`
37. Verifikasi `Remaining` mengikuti Kantor Pusat (200)
38. Pulihkan alokasi `Cabang Medan` dan hapus grup `Divisi Umum+{runId}-013` lewat fixture BE

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-45, 46, 49, 50, 51, 61, 538). Tidak ada TC hanya-BE di spec ini.
- Urutan TC diubah dari urutan nomor: blok baca (TC-45, 49, 50, 538) di awal dan blok yang mengubah alokasi atau membuat grup (TC-46, 51, 61) di akhir (S-10).
- Spec di atas 35 langkah (38 langkah): seluruh blok satu topik (Context Header dan Group Quota Summary Tab Allocation Quota pada dataset #12 yang sama) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 23 dan 32 (membuka Tab `Allocation Quota` sesudah muat ulang), langkah 26 (menutup modal), langkah 33 dan 34 (memilih node grup baru), langkah 38 (pemulihan).
- Temuan untuk QA:
  - TC-51 Expected a ("`Remaining` = sisa pool organisasi") tidak menyebut angka; langkah 29 memakai 320 yang dihitung TC-46 dari data fixture yang sama.
  - TC-61 menyebut grup baru `Divisi Umum` dibuat lewat Settings > Groups; spec membuatnya lewat fixture BE (pemicu, bukan objek uji) dan memakai nama bersuffix per run. Kode grup (`GRP-...`) tidak disebut di TC sehingga tidak diasersi pada Context Header.
  - TC-46 dan TC-51 mensyaratkan Pre-setup #12 diubah (Cabang Medan belum beralokasi), sedangkan TC-52 mengasumsikan Cabang Medan berstatus Used 880 dalam daftar level 1; pemulihan dijamin fixture BE.
