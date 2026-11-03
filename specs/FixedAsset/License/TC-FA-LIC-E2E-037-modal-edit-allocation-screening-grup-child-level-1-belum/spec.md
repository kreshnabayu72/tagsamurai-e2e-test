---
id: TC-FA-LIC-E2E-037-modal-edit-allocation-screening-grup-child-level-1-belum
title: "Screening Modal Edit Allocation: Grup Child, Level 1, dan Grup Belum Beralokasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-112
  - TC-FA-LIC-113
  - TC-FA-LIC-114
  - TC-FA-LIC-115
  - TC-FA-LIC-148
coverage:
  web: automated
---

# Screening Modal Edit Allocation: Grup Child, Level 1, dan Grup Belum Beralokasi

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): hierarki dan alokasi grup dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data: Pre-setup #12 (hierarki dan kuota PT Sejahtera): Kantor Pusat beralokasi 1500 dengan Divisi Logistik 500 (Used 350, subgroup Gudang A 100), Divisi IT 100, Divisi Keuangan belum beralokasi, Remaining Kantor Pusat 200.
- Spec read-only: tidak ada Save, data Pre-setup #12 tidak diubah dan tidak butuh pemulihan.

## Test Steps

### TC-FA-LIC-115: Tombol ikon Edit di samping tanda strip Allocated Quota

1. Klik tab `Allocation Quota`
2. Klik node `Kantor Pusat` di Sidebar
3. Verifikasi baris `Divisi Keuangan` pada Child Groups Quota: Allocated Quota menampilkan `—` dan tombol ikon `[Edit]` tampil di sampingnya

### TC-FA-LIC-112 dan TC-FA-LIC-148: Screening modal grup child beralokasi dan field read-only

4. Klik tombol ikon `[Edit]` pada baris `Divisi Logistik`
5. Verifikasi Header modal: Title `Edit Allocation Quota` (tanpa nama grup) dan icon close `[×]`
6. Verifikasi Field 1 Group Name (read-only): `Divisi Logistik (GRP-LOG)`
7. Verifikasi Field 2 Minimum Quota (read-only): `450 = 350 assets in this group + 0 reserved + 100 allocated to subgroups`
8. Verifikasi helper Field 2: `New quota cannot be lower than used, reserved, and subgroup-allocated quota.`
9. Verifikasi Field 3 berlabel `New Allocated Quota` dan ber-pre-fill `500`
10. Verifikasi helper Field 3: `Available in Kantor Pusat: 200 units.`
11. Verifikasi helper Field 3: `Leave empty to remove this group's allocation.`
12. Verifikasi Info Box: `Allocated quota is taken from the parent group and limits asset registration in this group and its subgroups.`
13. Verifikasi Footer: `[Clear Field]` (text, primary) dan `[Save]` (filled, success)
14. Verifikasi tidak ada tombol `[Cancel]` pada Footer
15. Coba mengetik pada Field 1 dan Field 2
16. Verifikasi Field 1 dan Field 2 tidak dapat diedit
17. Klik icon `[×]`

### TC-FA-LIC-113: Screening modal grup level 1 (Kantor Pusat)

18. Klik node `All Groups` di Sidebar
19. Klik tombol ikon `[Edit]` di samping Allocated Quota baris `Kantor Pusat`
20. Verifikasi Field 1: `Kantor Pusat (GRP-HQ)`
21. Verifikasi Field 2: `1,300 = 700 assets in this group + 0 reserved + 600 allocated to subgroups`
22. Verifikasi Field 3 ber-pre-fill `1500`
23. Verifikasi helper Field 3: `Available unallocated pool: 200 units.`
24. Verifikasi helper Field 3: `Leave empty to remove this group's allocation.`
25. Klik icon `[×]`

### TC-FA-LIC-114: Screening modal grup belum beralokasi (Divisi Keuangan)

26. Klik node `Kantor Pusat` di Sidebar
27. Klik tombol ikon `[Edit]` pada baris `Divisi Keuangan`
28. Verifikasi Field 3 kosong dan menampilkan placeholder `Enter allocated quota`
29. Verifikasi Field 2: `0 = 0 assets in this group + 0 reserved + 0 allocated to subgroups`
30. Verifikasi helper Field 3: `Available in Kantor Pusat: 200 units.`
31. Klik icon `[×]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): klik node `All Groups` atau `Kantor Pusat` memilih node Sidebar untuk blok berikutnya; `[×]` menutup modal bersih (tanpa perubahan field) sehingga dialog `Unsaved Changes` tidak muncul.
- Urutan TC: TC-FA-LIC-115 (daftar, tanpa modal) di awal, lalu TC-FA-LIC-112 bersama TC-FA-LIC-148 (field read-only pada modal yang sama), lalu TC-FA-LIC-113 dan TC-FA-LIC-114 (S-10).
