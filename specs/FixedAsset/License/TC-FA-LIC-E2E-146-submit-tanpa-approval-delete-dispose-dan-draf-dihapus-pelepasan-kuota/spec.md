---
id: TC-FA-LIC-E2E-146-submit-tanpa-approval-delete-dispose-dan-draf-dihapus-pelepasan-kuota
title: "Submit Tanpa Approval, Delete dan Dispose Aset, serta Draf Dihapus terhadap Used dan Reserved"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-398
  - TC-FA-LIC-399
  - TC-FA-LIC-400
coverage:
  web: automated
---

# Submit Tanpa Approval, Delete dan Dispose Aset, serta Draf Dihapus terhadap Used dan Reserved

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): hierarki, alokasi grup, kuota, dan status aset dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data Pre-setup: #12 (License Summary Used 4320, Reserved 15; Divisi IT) dan #20 (draf aset di Divisi IT; aset Active di Divisi IT untuk Delete dan Dispose). Kondisi per blok (diatur fixture BE): blok TC-FA-LIC-400 draf ke-1 Pre-setup #20 di Divisi IT; blok TC-FA-LIC-398 approval OFF dan draf ke-1 Pre-setup #20 di Divisi IT; blok TC-FA-LIC-399 sekurangnya dua aset Active di Divisi IT.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup dan aset Pre-setup #12 dan #20 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dan #20 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Used, Reserved, dan Remaining, status aset, dan Last Updated berubah; fixture memulihkannya. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.

## Test Steps

### TC-FA-LIC-400: Draf yang dihapus tidak menahan kuota

1. Jalankan fixture BE pemulih Pre-setup #12 dan #20 dengan draf ke-1 Pre-setup #20 di Divisi IT hingga tersimpan
2. Buka License > All License; catat Used, Reserved, dan Remaining pada License Summary kolom Asset
3. Hapus draf ke-1 Pre-setup #20 di Fixed Asset > Asset Registration
4. Tunggu aksi selesai
5. Muat ulang License > All License
6. Verifikasi Used, Reserved, dan Remaining tidak berubah dibanding nilai pada langkah 2

### TC-FA-LIC-398: Submit tanpa approval langsung menambah Used tanpa Reserved

7. Jalankan fixture BE pemulih Pre-setup #12 dan #20 dengan approval OFF dan draf ke-1 Pre-setup #20 di Divisi IT hingga tersimpan
8. Buka License > All License; catat Used dan Reserved pada License Summary kolom Asset
9. Submit draf ke-1 Pre-setup #20 di Divisi IT di Fixed Asset > Asset Registration
10. Verifikasi aset langsung berstatus `Active`
11. Buka License > All License
12. Verifikasi Used naik 1 dibanding nilai pada langkah 8
13. Verifikasi Reserved tidak berubah dibanding nilai pada langkah 8

### TC-FA-LIC-399: Delete dan Dispose aset melepaskan kuota; aset Disposed tetap tercatat

14. Jalankan fixture BE pemulih Pre-setup #12 dan #20 dengan sekurangnya dua aset Active di Divisi IT hingga tersimpan
15. Buka License > All License; catat Used dan Remaining pada License Summary kolom Asset
16. Delete satu aset Active
17. Tunggu aksi selesai
18. Muat ulang halaman License
19. Verifikasi Used turun 1 dan Remaining naik 1 dibanding nilai pada langkah 15
20. Dispose satu aset Active (selesaikan flow Disposal)
21. Tunggu aksi selesai
22. Muat ulang halaman License
23. Verifikasi Used turun 1 dan Remaining naik 1 dibanding nilai pada langkah 19 (aset Disposed tidak dihitung Used)
24. Buka daftar aset
25. Verifikasi aset Disposed tetap tampil di daftar aset
26. Jalankan fixture BE pemulih Pre-setup #12 dan #20 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 1, 7, 14, dan 26 (fixture BE pemulih dan penyetel state), langkah 18 dan 22 (muat ulang License), langkah 24 (membuka daftar aset), serta navigasi License. Langkah 4, 17, dan 21 menunggu aksi selesai sebelum berpindah surface atau memuat ulang (bagian 8b butir 8). Langkah 2, 8, 15 mencatat nilai License Summary sebagai baseline (S-12).
- Urutan TC diubah dari urutan nomor: TC-FA-LIC-400 dan TC-FA-LIC-398 lebih dulu, TC-FA-LIC-399 (Delete dan Dispose) di akhir karena menghapus data (S-10).
- Expected TC-FA-LIC-399 "tidak dihitung Used" untuk aset Disposed diasersi oleh penurunan Used pada langkah 23.
- Pembagian TC lintas spec: TC-FA-LIC-394 sampai TC-FA-LIC-396 ada di spec 119 dan TC-FA-LIC-397 di spec 153.
- Temuan untuk QA:
  - TC-FA-LIC-398 dan TC-FA-LIC-400 tidak menyebut label tombol Submit dan Hapus; spec mengikuti kalimat TC.
  - TC-FA-LIC-398, TC-FA-LIC-399, dan TC-FA-LIC-400 merujuk draf dan aset Pre-setup #20 tanpa nama; Search nama baris sebelum aksi pada tabel yang dapat memuat lebih dari satu halaman (8b.13) tidak dapat ditulis dengan nama literal, sehingga spec merujuk draf ke-1 Pre-setup #20 dan aset Active Pre-setup #20 yang disediakan fixture BE.
  - TC-FA-LIC-399 tidak menyebut tahap-tahap flow Disposal; spec menulis "selesaikan flow Disposal" sesuai TC.
