---
id: TC-FA-LIC-E2E-049-remove-allocation-ditolak-bila-subgroup-beralokasi
title: "Remove Allocation: Ditolak bila Subgroup Beralokasi dan Kasus Boleh Dihapus"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-161
  - TC-FA-LIC-162
  - TC-FA-LIC-163
  - TC-FA-LIC-167
coverage:
  web: automated
---

# Remove Allocation: Ditolak bila Subgroup Beralokasi dan Kasus Boleh Dihapus

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
- Data: Pre-setup #12: Divisi Logistik beralokasi 500 dengan child Gudang A beralokasi 100; Divisi Keuangan belum beralokasi; Cabang Medan beralokasi 1.000 dengan Used 880.
- Data: Fixture BE penyetel pada langkah yang disebut: Divisi Logistik beralokasi 500 dengan Gudang A tanpa alokasi (Used 100) untuk TC-FA-LIC-162.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup Pre-setup #12 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Last Updated baris alokasi, entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: Kemampuan membaca jumlah entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log sebagai baseline (disediakan tim FE/BE; audit trail permanen sehingga asersi memakai selisih jumlah entri, S-12).

## Test Steps

### TC-FA-LIC-161: Remove ditolak bila grup masih punya subgroup beralokasi (V-FALIC-04)

1. Klik tab `Allocation Quota`
2. Klik node `Kantor Pusat` di Sidebar
3. Klik tombol ikon `[Edit]` pada baris `Divisi Logistik`
4. Klik `[Clear Field]`
5. Klik `[Save]`
6. Verifikasi error inline di bawah field: `Cannot remove allocation while its subgroups have their own allocation.`
7. Verifikasi modal tetap terbuka
8. Verifikasi tidak ada toast
9. Klik icon `[×]`
10. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
11. Klik `[Leave]`
12. Verifikasi Allocated Quota baris `Divisi Logistik` tetap `500`

### TC-FA-LIC-167: Remove pada grup belum beralokasi (Edit tanpa perubahan)

13. Catat jumlah entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log sebagai baseline
14. Klik tombol ikon `[Edit]` pada baris `Divisi Keuangan`
15. Klik `[Clear Field]`
16. Klik `[Save]`
17. Verifikasi toast netral `No changes to save.`
18. Periksa `Changelog: Allocation Quota`, System Log aktor, dan Activity Log
19. Verifikasi jumlah entri sama dengan baseline (tidak ada entri log)
20. Tutup modal `Changelog: Allocation Quota`

### TC-FA-LIC-163: Remove grup level 1 (Cabang Medan)

21. Klik node `All Groups` di Sidebar
22. Klik tombol ikon `[Edit]` pada baris `Cabang Medan`
23. Klik `[Clear Field]`
24. Klik `[Save]`
25. Verifikasi toast sukses `Success, group license allocation removed.`
26. Klik node `Cabang Medan` di Sidebar
27. Verifikasi `Cabang Medan` menampilkan badge `Not Allocated`

### TC-FA-LIC-162: Remove diizinkan bila child tidak punya baris alokasi walau punya pemakaian

28. Jalankan fixture BE pemulih Pre-setup #12 dan penyetel Gudang A tanpa alokasi (Used 100) di bawah Divisi Logistik beralokasi 500 hingga tersimpan
29. Muat ulang halaman License, lalu klik tab `Allocation Quota`
30. Klik node `Kantor Pusat` di Sidebar
31. Klik tombol ikon `[Edit]` pada baris `Divisi Logistik`
32. Klik `[Clear Field]`
33. Klik `[Save]`
34. Verifikasi toast sukses `Success, group license allocation removed.`
35. Verifikasi pemakaian Divisi Logistik dan subtree tetap mengurangi Remaining Kantor Pusat

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): fixture BE pemulih dan penyetel, muat ulang halaman, dan klik tab menyiapkan blok TC-FA-LIC-162; `Periksa ...` membuka surface log; menutup modal Changelog dan modal dirty (`[×]`, dialog `Unsaved Changes`, `[Leave]`, S-08).
- Urutan TC: penolakan (TC-FA-LIC-161) lebih dulu, lalu TC-FA-LIC-167 (tanpa perubahan), TC-FA-LIC-163 (Cabang Medan), dan TC-FA-LIC-162 (fixture penyetel) (S-10).
- Temuan untuk QA:
  - TC-FA-LIC-163: judul menyebut `Unallocated Pool memperhitungkan pemakaian yang tersisa` tetapi Expected hanya toast dan badge `Not Allocated`; spec mengikuti Expected.
  - TC-FA-LIC-162: klausa b (`tetap mengurangi Remaining Kantor Pusat`) tidak menyebut angka; spec mengasersi tanpa nilai konkret.
  - TC-FA-LIC-167: klausa `tidak ada entri log` diasersi di spec ini dengan baseline karena belum ada spec absence (kelas g) yang memuat aksi nyata untuk TC ini (S-05).
