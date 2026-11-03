---
id: TC-FA-LIC-E2E-047-modal-edit-allocation-backdrop-nilai-dikembalikan-refresh
title: "Modal Edit Allocation: Backdrop, Nilai Dikembalikan, Refresh Browser, dan Navigasi Internal"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-142
  - TC-FA-LIC-143
  - TC-FA-LIC-144
  - TC-FA-LIC-145
coverage:
  web: automated
---

# Modal Edit Allocation: Backdrop, Nilai Dikembalikan, Refresh Browser, dan Navigasi Internal

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
- Data: Pre-setup #12: Divisi Logistik beralokasi 500. Blok TC-FA-LIC-144 menyimpan Divisi Logistik `600` (Save sukses) dan fixture BE pemulih mengembalikannya (hook `after`).
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup Pre-setup #12 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Last Updated baris alokasi, entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: Mendeteksi dan menangani dialog bawaan browser (`beforeunload`) pada F5 (disediakan tim FE).
- Kemampuan teknis: Tombol Back browser dan navigasi ke menu `Dashboard` pada sidebar.

## Test Steps

### TC-FA-LIC-142: Klik backdrop tidak menutup modal

1. Klik tab `Allocation Quota`
2. Klik node `Kantor Pusat` di Sidebar
3. Klik tombol ikon `[Edit]` pada baris `Divisi Logistik`
4. Klik area di luar modal
5. Verifikasi modal tetap terbuka
6. Ubah nilai menjadi `600`
7. Klik area di luar modal
8. Verifikasi modal tetap terbuka
9. Verifikasi input `600` dipertahankan
10. Verifikasi dialog `Unsaved Changes` tidak muncul

### TC-FA-LIC-143: Nilai diubah lalu dikembalikan identik dianggap bersih

11. Ketik ulang `500`
12. Klik icon `[×]`
13. Verifikasi modal tertutup tanpa dialog `Unsaved Changes`

### TC-FA-LIC-145: Navigasi internal saat modal dirty

14. Klik tombol ikon `[Edit]` pada baris `Divisi Logistik`
15. Ubah nilai menjadi `600`
16. Klik menu `Dashboard` pada sidebar
17. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` muncul sebelum route berubah
18. Klik `[Cancel]`
19. Verifikasi navigasi dibatalkan dan tetap di form
20. Klik tombol Back browser
21. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` muncul
22. Klik `[Leave]`
23. Verifikasi navigasi dilanjutkan tanpa menyimpan

### TC-FA-LIC-144: Refresh browser saat modal dirty

24. Buka kembali halaman Fixed Asset > License
25. Klik tab `Allocation Quota`
26. Klik node `Kantor Pusat` di Sidebar
27. Klik tombol ikon `[Edit]` pada baris `Divisi Logistik`
28. Ubah nilai menjadi `600`
29. Tekan F5
30. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul saat modal dirty
31. Batalkan konfirmasi bawaan browser (tetap di halaman)
32. Klik `[Save]`
33. Verifikasi toast sukses `Success, group license quota updated.`
34. Tekan F5
35. Verifikasi Tabs Bar halaman License tampil
36. Verifikasi konfirmasi bawaan browser tidak muncul setelah Save sukses
37. Klik tab `Allocation Quota`
38. Klik node `Kantor Pusat` di Sidebar
39. Klik tombol ikon `[Edit]` pada baris `Divisi Logistik`
40. Tekan F5
41. Verifikasi Tabs Bar halaman License tampil
42. Verifikasi konfirmasi bawaan browser tidak muncul pada modal bersih

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): klik node Sidebar memilih node blok; `Buka kembali halaman Fixed Asset > License` kembali ke halaman setelah navigasi keluar pada TC-FA-LIC-145; `Batalkan konfirmasi bawaan browser` membiarkan modal dirty tetap terbuka untuk Save.
- Urutan TC: TC-FA-LIC-142, TC-FA-LIC-143, TC-FA-LIC-145 (berakhir di luar halaman License), lalu TC-FA-LIC-144 (reload dan Save sukses) (S-10).
- TC-FA-LIC-143: nilai `600` dari blok sebelumnya diketik ulang menjadi `500` (S-04).
- Temuan untuk QA:
  - TC-FA-LIC-144: Expected b (`tidak muncul ... setelah Save sukses`) tidak punya langkah di TC; spec menambahkan Save `600` lalu F5 sebagai langkah observasi agar klausa itu teruji.
- Alasan di atas sekitar 35 langkah (42 langkah): semua blok satu topik (cara menutup atau meninggalkan modal Edit Allocation yang dirty) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya pembukaan ulang modal dan halaman.
