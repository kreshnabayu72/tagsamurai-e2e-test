---
id: TC-FA-LIC-E2E-041-edit-allocation-validasi-maximum-quota-v-falic-02-03
title: "Edit Allocation: Validasi Maximum Quota V-FALIC-02 dan V-FALIC-03"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-128
  - TC-FA-LIC-129
  - TC-FA-LIC-130
  - TC-FA-LIC-131
  - TC-FA-LIC-134
coverage:
  web: automated
---

# Edit Allocation: Validasi Maximum Quota V-FALIC-02 dan V-FALIC-03

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
- Data: Pre-setup #12: Divisi Logistik beralokasi 500 (Maximum Quota 700) dan Kantor Pusat beralokasi 1500 (Maximum Quota 1.700 = pool 200 + 1.500).
- Data: Grup bersuffix `Divisi Umum+{runId}-041` di bawah Kantor Pusat, belum beralokasi, Used 10 dan Reserved 2 (subtree), Remaining Kantor Pusat 200; dibuat fixture BE penyetel di hook `before` dan dibersihkan hook `after`.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup Pre-setup #12 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Last Updated baris alokasi, entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.

## Test Steps

### TC-FA-LIC-128: Nilai 701 ditolak V-FALIC-02 saat Save

1. Klik tab `Allocation Quota`
2. Klik node `Kantor Pusat` di Sidebar
3. Klik tombol ikon `[Edit]` pada baris `Divisi Logistik`
4. Isi New Allocated Quota `701`
5. Klik `[Save]`
6. Verifikasi field berborder danger
7. Verifikasi alert di bawah input: `Allocated quota exceeds the maximum allowed for this group (700).`
8. Verifikasi modal tetap terbuka dengan input `701` dipertahankan
9. Verifikasi tidak ada perubahan pada tabel
10. Verifikasi tidak ada toast

### TC-FA-LIC-129: Contoh PRD, 800 ditolak dan 600 diterima

11. Isi New Allocated Quota `800`
12. Klik `[Save]`
13. Verifikasi alert V-FALIC-02 tampil: `Allocated quota exceeds the maximum allowed for this group (700).`
14. Ubah nilai menjadi `600`
15. Klik `[Save]`
16. Verifikasi toast sukses `Success, group license quota updated.`
17. Verifikasi Allocated Quota baris `Divisi Logistik` `600`

### TC-FA-LIC-130: Level 1, 1701 ditolak V-FALIC-03

18. Klik node `All Groups` di Sidebar
19. Klik tombol ikon `[Edit]` di samping Allocated Quota baris `Kantor Pusat`
20. Isi New Allocated Quota `1701`
21. Klik `[Save]`
22. Verifikasi alert di bawah input: `Total allocated quota exceeds organization total limit (1,700).`
23. Verifikasi modal tetap terbuka dengan input `1701` dipertahankan

### TC-FA-LIC-131: Level 1, 1700 diterima

24. Ubah nilai menjadi `1700`
25. Klik `[Save]`
26. Verifikasi toast sukses `Success, group license quota updated.`
27. Jalankan fixture BE pemulih Pre-setup #12 hingga tersimpan (Divisi Logistik 500, Kantor Pusat 1500, Remaining Kantor Pusat 200; grup `Divisi Umum+{runId}-041` dengan Used 10 dan Reserved 2 tetap ada)
28. Muat ulang halaman License, lalu klik tab `Allocation Quota`

### TC-FA-LIC-134: Maximum Quota grup belum beralokasi memakai Used ditambah Reserved subtree

29. Klik node `Kantor Pusat` di Sidebar
30. Klik tombol ikon `[Edit]` pada baris `Divisi Umum+{runId}-041`
31. Isi New Allocated Quota `212`
32. Klik `[Save]`
33. Verifikasi `212` diterima (Maximum Quota tepat 200 + 12): modal tertutup
34. Klik tombol ikon `[Edit]` pada baris `Divisi Umum+{runId}-041`
35. Isi New Allocated Quota `213`
36. Klik `[Save]`
37. Verifikasi alert V-FALIC-02 tampil: `Allocated quota exceeds the maximum allowed for this group (212).`
38. Klik icon `[×]`
39. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
40. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): menutup modal dirty lewat `[×]`, dialog `Unsaved Changes`, dan `[Leave]` (S-08); klik node Sidebar memilih node untuk blok berikutnya.
- Urutan TC: validasi diblokir lebih dulu (TC-FA-LIC-128), lalu TC-FA-LIC-129 (bergantung pada TC-FA-LIC-128; modal dari blok sebelumnya masih terbuka), TC-FA-LIC-130 dan TC-FA-LIC-131 (level 1), lalu TC-FA-LIC-134 (S-10).
- TC-FA-LIC-129 dan TC-FA-LIC-131 menyimpan nilai baru (Divisi Logistik 600, Kantor Pusat 1700); fixture BE pemulih mengembalikannya (hook `after`).
- Langkah 27 dan 28 (fixture BE pemulih, muat ulang halaman, dan klik tab) mengembalikan Pre-setup #12 sebelum TC-FA-LIC-134 karena TC-FA-LIC-129 dan TC-FA-LIC-131 mengubah alokasi Divisi Logistik (600) dan Kantor Pusat (1700) sehingga Remaining Kantor Pusat 300 dan Maximum Quota grup `Divisi Umum+{runId}-041` 312, sedangkan asersi `212` dan `(212)` bergantung pada Remaining Kantor Pusat 200.
- TC-FA-LIC-545 ada di spec 133.
- TC-FA-LIC-134: `212 diterima` diasersi lewat modal yang tertutup tanpa pesan error; toast tidak disebut TC pada klausa itu.
- Temuan untuk QA:
  - TC-FA-LIC-134: precondition menyebut grup `Divisi Umum` tanpa nama pengenal unik; spec memakai nama bersuffix (S-12).
- Alasan di atas sekitar 35 langkah (40 langkah): semua blok satu topik (validasi Maximum Quota pada modal Edit Allocation) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
