---
id: TC-FA-LIC-E2E-040-edit-allocation-minimum-quota-memasukkan-reserved
title: "Edit Allocation: Minimum Quota Memasukkan Reserved dan Pemakaian Subtree"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LIC-132
  - TC-FA-LIC-133
coverage:
  web: automated
---

# Edit Allocation: Minimum Quota Memasukkan Reserved dan Pemakaian Subtree

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
- Data: Pre-setup #12: Produksi (level 1) Used 1.450 dan Reserved 5.
- Data: Grup bersuffix `Grup A+{runId}-040` (beralokasi 100, Used 10) di bawah Kantor Pusat dengan child `Grup B+{runId}-040` (tanpa alokasi, Used 10, Reserved 2) dan cucu `Grup C+{runId}-040` (child Grup B, tanpa alokasi, Used 7, Reserved 1); dibuat fixture BE penyetel pada langkah yang disebut dan dibersihkan hook `after`.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup Pre-setup #12 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Last Updated baris alokasi, entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.

## Test Steps

### TC-FA-LIC-132: Minimum Quota memasukkan Reserved (Produksi)

1. Klik tab `Allocation Quota`
2. Klik node `All Groups` di Sidebar
3. Klik tombol ikon `[Edit]` pada baris `Produksi`
4. Verifikasi Field 2: `1,455 = 1,450 assets in this group + 5 reserved + 0 allocated to subgroups`
5. Isi New Allocated Quota `1454`
6. Pindahkan fokus keluar dari field (blur)
7. Verifikasi pesan V-FALIC-01 tampil: `Cannot set quota below used, reserved, and subgroup-allocated quota (1,455).`
8. Isi New Allocated Quota `1455`
9. Pindahkan fokus keluar dari field (blur)
10. Verifikasi tidak ada pesan error
11. Klik icon `[×]`
12. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
13. Klik `[Leave]`

### TC-FA-LIC-133: Minimum Quota memasukkan pemakaian subtree tanpa alokasi sampai tiga level

14. Jalankan fixture BE pemulih Pre-setup #12 dan penyetel `Grup A+{runId}-040`, `Grup B+{runId}-040`, dan `Grup C+{runId}-040` hingga tersimpan
15. Muat ulang halaman License, lalu klik tab `Allocation Quota`
16. Klik node `Kantor Pusat` di Sidebar
17. Klik tombol ikon `[Edit]` pada baris `Grup A+{runId}-040`
18. Verifikasi Field 2: `30 = 10 assets in this group + 0 reserved + 20 allocated to subgroups`
19. Isi New Allocated Quota `29`
20. Pindahkan fokus keluar dari field (blur)
21. Verifikasi pesan V-FALIC-01 tampil: `Cannot set quota below used, reserved, and subgroup-allocated quota (30).`
22. Isi New Allocated Quota `30`
23. Pindahkan fokus keluar dari field (blur)
24. Verifikasi tidak ada pesan error
25. Klik icon `[×]`
26. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
27. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): fixture BE pemulih dan penyetel, muat ulang halaman, dan klik tab menyiapkan state blok kedua; menutup modal dirty lewat `[×]`, dialog `Unsaved Changes`, dan `[Leave]` (S-08).
- Subtree grup B = 10 + 2 + 7 + 1 = 20 (sesuai TC); Minimum Quota grup A = 10 + 0 + 20 = 30.
- TC-FA-LIC-598 ada di spec 134.
- Temuan untuk QA:
  - TC-FA-LIC-133: precondition tidak menyebut parent grup A; spec menempatkannya di bawah Kantor Pusat (Remaining 200 mencukupi alokasi 100), dan Remaining parent tidak diasersi.
  - TC-FA-LIC-132: nilai pre-fill Produksi tidak disebut TC; spec mengasumsikan berbeda dari 1455 sehingga penutupan modal memunculkan dialog `Unsaved Changes`.
