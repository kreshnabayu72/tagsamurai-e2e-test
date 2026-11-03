---
id: TC-FA-LIC-E2E-116-registrasi-aset-terhadap-kuota-grup-ditolak-penuh-leluhur
title: "Registrasi Aset terhadap Kuota Grup: Ditolak Saat Penuh, Memakai Remaining Leluhur, dan Sisa Pool Organisasi"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-384
  - TC-FA-LIC-385
  - TC-FA-LIC-386
  - TC-FA-LIC-387
coverage:
  web: automated
---

# Registrasi Aset terhadap Kuota Grup: Ditolak Saat Penuh, Memakai Remaining Leluhur, dan Sisa Pool Organisasi

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): hierarki, alokasi grup, dan kuota dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data Pre-setup: #12 (Gudang A beralokasi 100; Divisi Keuangan belum beralokasi di bawah Kantor Pusat; Cabang Medan; License Summary Reserved 15 dan Used 4320) dan #20 (draf aset siap Submit di Divisi Keuangan, Gudang A, dan Cabang Medan). Kondisi per blok (diatur fixture BE): blok TC-FA-LIC-384 Gudang A Used 100 dan Remaining 0; blok TC-FA-LIC-385 Remaining Kantor Pusat 0; blok TC-FA-LIC-386 Remaining Kantor Pusat 200 dan approval OFF; blok TC-FA-LIC-387 Cabang Medan belum beralokasi dengan Used 880, Unallocated Pool 320, dan approval OFF.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup dan aset Pre-setup #12 dan #20 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Used dan Remaining grup, status aset, dan Last Updated berubah; fixture memulihkannya. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.

## Test Steps

### TC-FA-LIC-384: Registrasi di grup beralokasi yang penuh ditolak

1. Buka Fixed Asset > Asset Registration
2. Pilih draf aset di group Gudang A
3. Klik `Submit for Approval`
4. Verifikasi pesan `Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.` tampil pada form registrasi
5. Verifikasi aset tetap berstatus `Draft`
6. Buka License > All License
7. Verifikasi License Summary kolom Asset: Reserved `15` dan Used `4320` (sama seperti Pre-setup #12, tidak berubah)

### TC-FA-LIC-385: Grup tanpa alokasi memakai Remaining leluhur beralokasi terdekat dan ditolak saat habis

8. Jalankan fixture BE pemulih Pre-setup #12 dengan Remaining Kantor Pusat `0` dan draf aset di Divisi Keuangan hingga tersimpan
9. Buka Fixed Asset > Asset Registration
10. Submit draf aset di group Divisi Keuangan
11. Verifikasi pesan `Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.` tampil
12. Buka License > Allocation Quota
13. Klik node `Kantor Pusat` di Sidebar
14. Verifikasi Remaining Kantor Pusat (leluhur) tetap `0`
15. Klik node `Divisi Keuangan` di Sidebar
16. Verifikasi Used by This Group Divisi Keuangan tetap `0`

### TC-FA-LIC-386: Registrasi di grup tanpa alokasi mengurangi Remaining leluhur saat berhasil

17. Jalankan fixture BE pemulih Pre-setup #12 dengan Remaining Kantor Pusat `200`, approval OFF, dan draf aset di Divisi Keuangan hingga tersimpan
18. Buka Fixed Asset > Asset Registration
19. Submit draf aset di Divisi Keuangan (tanpa approval)
20. Verifikasi Submit berhasil
21. Verifikasi aset langsung berstatus `Active`
22. Buka License > Allocation Quota
23. Klik node `Kantor Pusat` di Sidebar
24. Klik node `Divisi Keuangan` di Sidebar
25. Verifikasi Divisi Keuangan: Used by This Group `1` dan Remaining `199` (mengikuti Kantor Pusat)
26. Klik node `Kantor Pusat` di Sidebar
27. Verifikasi Kantor Pusat: Allocated to Subgroups `601` dan Remaining `199`

### TC-FA-LIC-387: Grup level 1 tanpa leluhur memakai sisa pool organisasi

28. Jalankan fixture BE: Cabang Medan belum beralokasi dengan Used 880, Unallocated Pool 320, draf aset di Cabang Medan, approval OFF hingga tersimpan
29. Buka Fixed Asset > Asset Registration
30. Submit draf aset di Cabang Medan
31. Verifikasi Submit berhasil
32. Buka License > Allocation Quota
33. Klik node `All Groups` di Sidebar
34. Klik node `Cabang Medan` di Sidebar
35. Verifikasi Group Quota Summary: Used by This Group Cabang Medan `881`
36. Arahkan kursor ke nilai `Remaining`
37. Verifikasi `Remaining` Cabang Medan `319` (sisa pool organisasi 320 dikurangi 1 aset baru)
38. Verifikasi tooltip `Shared from organization pool`
39. Jalankan fixture BE pemulih Pre-setup #12 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 8, 17, 28, dan 39 (fixture BE pemulih dan penyetel state), serta klik tab dan node Sidebar pada langkah 12, 13, 15, 22 sampai 24, 26, dan 32 sampai 34.
- Urutan TC: TC-FA-LIC-384 dan TC-FA-LIC-385 (penolakan) sebelum TC-FA-LIC-386 dan TC-FA-LIC-387 (registrasi berhasil) (S-10).
- Alasan di atas sekitar 35 langkah (39 langkah): semua blok satu topik (registrasi aset terhadap kuota grup) dan berdiri sendiri dengan fixture sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya navigasi dan pemulihan fixture.
- Temuan untuk QA:
  - TC-FA-LIC-384 sampai 387 tidak menyebut label tombol Submit selain `Submit for Approval` (TC-FA-LIC-384); pada blok approval OFF spec menulis "Submit draf aset" sesuai kalimat TC.
  - TC-FA-LIC-387 tidak menyebut cara membaca Unallocated Pool 320 sebelum aksi; hanya hasil `Remaining` 319 yang diasersi.
