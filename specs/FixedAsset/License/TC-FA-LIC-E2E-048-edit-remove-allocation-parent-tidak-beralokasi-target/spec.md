---
id: TC-FA-LIC-E2E-048-edit-remove-allocation-parent-tidak-beralokasi-target
title: "Edit dan Remove Allocation: Idempotensi, Parent Tidak Beralokasi, dan Grup Target Terhapus"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-151
  - TC-FA-LIC-153
  - TC-FA-LIC-166
  - TC-FA-LIC-461
coverage:
  web: automated
---

# Edit dan Remove Allocation: Idempotensi, Parent Tidak Beralokasi, dan Grup Target Terhapus

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
- Data: Pre-setup #12: Divisi IT beralokasi 100 (Used 60); Kantor Pusat dan Divisi Keuangan sesuai Pre-setup #12.
- Data: Fixture BE penyetel pada langkah yang disebut: (a) Kantor Pusat tidak beralokasi (alokasi child dihapus lebih dulu) untuk TC-FA-LIC-151; (b) grup bersuffix `Divisi IT+{runId}-048` milik spec ini di bawah Kantor Pusat, beralokasi 100 tanpa aset aktif (guard Delete grup `settings-groups`), untuk TC-FA-LIC-153 dan TC-FA-LIC-166; grup itu dibuat fixture BE penyetel pada langkah yang disebut dan dibersihkan hook `after` bila masih ada. Grup Pre-setup #12 `Divisi IT` tidak dihapus.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup Pre-setup #12 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Last Updated baris alokasi, entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: Kemampuan membaca jumlah entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log sebagai baseline (disediakan tim FE/BE; audit trail permanen sehingga asersi memakai selisih jumlah entri, S-12).
- Kemampuan teknis: Pelaku kedua (penghapus grup) memakai sesi API aktor (dinyatakan di `suite.md`).

## Test Steps

### TC-FA-LIC-461: Idempotensi Edit dan Remove

1. Klik tab `Allocation Quota`
2. Klik node `Kantor Pusat` di Sidebar
3. Klik tombol ikon `[Edit]` pada baris `Divisi IT`
4. Isi New Allocated Quota `120`
5. Klik `[Save]`
6. Verifikasi toast sukses `Success, group license quota updated.`
7. Catat jumlah entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log sebagai baseline
8. Klik tombol ikon `[Edit]` pada baris `Divisi IT`
9. Isi New Allocated Quota `120`
10. Klik `[Save]`
11. Verifikasi toast netral `No changes to save.`
12. Verifikasi Allocated Quota baris `Divisi IT` tetap `120`
13. Periksa `Changelog: Allocation Quota`, System Log aktor, dan Activity Log
14. Verifikasi jumlah entri sama dengan baseline (tidak ada entri dari Edit kedua)
15. Tutup modal `Changelog: Allocation Quota`
16. Klik tombol ikon `[Edit]` pada baris `Divisi IT`
17. Klik `[Clear Field]`
18. Klik `[Save]`
19. Verifikasi toast sukses `Success, group license allocation removed.`
20. Klik tombol ikon `[Edit]` pada baris `Divisi IT`
21. Klik `[Clear Field]`
22. Klik `[Save]`
23. Verifikasi toast netral `No changes to save.` pada grup yang sudah tidak beralokasi

### TC-FA-LIC-151: Edit grup yang parent-nya belum beralokasi

24. Jalankan fixture BE pemulih Pre-setup #12 dan penyetel Kantor Pusat tidak beralokasi hingga tersimpan
25. Muat ulang halaman License, lalu klik tab `Allocation Quota`
26. Klik node `Kantor Pusat` di Sidebar
27. Verifikasi tombol `[Edit]` pada baris child `Divisi Keuangan` enabled
28. Klik tombol ikon `[Edit]` pada baris `Divisi Keuangan`
29. Verifikasi dialog blok satu tombol: Title `Cannot Edit Allocation`, Body `Allocate quota to the parent group first.`, tombol `[OK]`
30. Klik `[OK]`
31. Verifikasi dialog tertutup
32. Verifikasi tidak ada modal Edit yang terbuka

### TC-FA-LIC-153: Grup target terhapus saat modal Edit terbuka

33. Jalankan fixture BE pemulih Pre-setup #12 dan penyetel grup `Divisi IT+{runId}-048` di bawah Kantor Pusat beralokasi 100 tanpa aset aktif hingga tersimpan
34. Muat ulang halaman License, lalu klik tab `Allocation Quota`
35. Klik node `Kantor Pusat` di Sidebar
36. Klik tombol ikon `[Edit]` pada baris `Divisi IT+{runId}-048`
37. Hapus grup `Divisi IT+{runId}-048` di Settings > Groups lewat sesi API aktor hingga penghapusan tersimpan
38. Isi New Allocated Quota `120`
39. Klik `[Save]`
40. Verifikasi toast netral `This group is no longer available.`
41. Verifikasi modal tertutup
42. Verifikasi daftar di-refresh tanpa baris `Divisi IT+{runId}-048`

### TC-FA-LIC-166: Remove Allocation pada grup yang sudah terhapus

43. Jalankan fixture BE pemulih Pre-setup #12 dan penyetel grup `Divisi IT+{runId}-048` di bawah Kantor Pusat beralokasi 100 tanpa aset aktif hingga tersimpan
44. Muat ulang halaman License, lalu klik tab `Allocation Quota`
45. Klik node `Kantor Pusat` di Sidebar
46. Klik tombol ikon `[Edit]` pada baris `Divisi IT+{runId}-048`
47. Klik `[Clear Field]`
48. Hapus grup `Divisi IT+{runId}-048` di Settings > Groups lewat sesi API aktor hingga penghapusan tersimpan
49. Klik `[Save]`
50. Verifikasi toast netral `This group is no longer available.`
51. Verifikasi modal tertutup
52. Verifikasi daftar di-refresh tanpa baris `Divisi IT+{runId}-048`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): fixture BE pemulih dan penyetel, muat ulang halaman, dan klik tab menyiapkan state tiap blok; `Periksa ...` membuka surface log; `Tutup modal` menutup modal Changelog.
- Urutan TC: TC-FA-LIC-461 pada state Pre-setup #12, lalu TC-FA-LIC-151 (Kantor Pusat tidak beralokasi), TC-FA-LIC-153, dan TC-FA-LIC-166 (Divisi IT dihapus; dipulihkan fixture di antaranya) (S-10).
- TC-FA-LIC-153 dan TC-FA-LIC-166: dialog atau toast hasil server menjadi anchor absence baris `Divisi IT` (bagian 8b butir 2); pelaku kedua memakai sesi API aktor dan langkahnya ditulis `... hingga ... tersimpan` (R-20).
- TC-FA-LIC-153 dan TC-FA-LIC-166 menyebut grup `Divisi IT`; target hapus grup memakai grup bersuffix `Divisi IT+{runId}-048` milik spec ini supaya penghapusan tidak merusak data Pre-setup #12 (S-06, S-12).
- Temuan untuk QA:
  - TC-FA-LIC-153 dan TC-FA-LIC-166: TC menyebut `dua sesi Total Control` dan label Manual Only (dua sesi paralel); spec memakai satu sesi UI dan satu sesi API aktor untuk pemicu penghapusan grup.
  - TC-FA-LIC-461: klausa `nol log` hanya diasersi untuk Edit kedua (selisih jumlah entri terhadap baseline sesudah Edit pertama); TC tidak merinci surface log untuk Remove kedua.
- Alasan di atas sekitar 35 langkah (52 langkah): semua blok satu topik (Edit atau Remove Allocation yang ditolak atau tidak berubah) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya fixture pemulih dan penyetel.
