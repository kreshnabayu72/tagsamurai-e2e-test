---
id: TC-FA-LIC-E2E-038-modal-edit-allocation-copy-dinamis-helper-level-1-tombol
title: "Modal Edit Allocation: Tombol Saving, Copy Dinamis, Helper Level 1, dan Aksesibilitas"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-116
  - TC-FA-LIC-117
  - TC-FA-LIC-147
  - TC-FA-LIC-526
coverage:
  web: automated
---

# Modal Edit Allocation: Tombol Saving, Copy Dinamis, Helper Level 1, dan Aksesibilitas

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
- Data: Pre-setup #12; grup tambahan `Divisi Kecil+{runId}-038` di bawah Kantor Pusat (fixture BE penyetel pada langkah yang disebut): beralokasi 5, Used 1, Reserved 0, tanpa subgroup, Remaining Kantor Pusat 1.
- Data: Fixture BE penyetel Unallocated Pool tepat 1 (Total Allocated 4.999 dari Total Asset Capacity 5.000) pada langkah yang disebut.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup Pre-setup #12 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Last Updated baris alokasi, entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: Intercept jaringan (`Spectra.intercept()`) di atas backend nyata menunda respons Save 3 detik, dilepas segera setelah asersi Saving selesai (S-09). Menahan respons hanya untuk mengamati state UI, bukan kegagalan.

## Test Steps

### TC-FA-LIC-117: Tombol Save dan Clear Field saat Saving

1. Klik tab `Allocation Quota`
2. Klik node `Kantor Pusat` di Sidebar
3. Klik tombol ikon `[Edit]` pada baris `Divisi IT`
4. Isi New Allocated Quota `120`
5. Pasang intercept jaringan yang menunda respons Save 3 detik
6. Arahkan kursor ke `[Save]`
7. Verifikasi state hover tombol `[Save]` terlihat
8. Klik `[Save]`
9. Verifikasi `[Save]` menampilkan indikator loading dan disabled
10. Verifikasi Field, `[Clear Field]`, dan icon `[×]` disabled selama request berjalan
11. Tunggu respons Save selesai
12. Verifikasi modal tertutup setelah respons diterima
13. Lepas intercept jaringan

### TC-FA-LIC-116: Bentuk tunggal 1 asset dan 1 unit

14. Jalankan fixture BE pemulih Pre-setup #12 dan penyetel `Divisi Kecil+{runId}-038` (beralokasi 5, Used 1, Reserved 0, Remaining Kantor Pusat 1) hingga tersimpan
15. Muat ulang halaman License, lalu klik tab `Allocation Quota`
16. Klik node `Kantor Pusat` di Sidebar
17. Klik tombol ikon `[Edit]` pada baris `Divisi Kecil+{runId}-038`
18. Verifikasi Field 2: `1 = 1 asset in this group + 0 reserved + 0 allocated to subgroups`
19. Verifikasi helper Field 3: `Available in Kantor Pusat: 1 unit.`
20. Klik icon `[×]`

### TC-FA-LIC-147: Aksesibilitas modal: focus trap, label, dan hubungan error

21. Jalankan fixture BE pemulih Pre-setup #12 hingga tersimpan
22. Muat ulang halaman License, lalu klik tab `Allocation Quota`
23. Klik node `Kantor Pusat` di Sidebar
24. Klik tombol ikon `[Edit]` pada baris `Divisi Logistik`
25. Tekan Tab berulang
26. Verifikasi fokus tetap berputar di dalam modal
27. Isi New Allocated Quota `440`
28. Pindahkan fokus keluar dari field (blur)
29. Verifikasi field New Allocated Quota berlabel
30. Verifikasi field memiliki `aria-describedby` yang menunjuk pesan error
31. Verifikasi field tidak wajib (tanpa `aria-required`) karena kosong berarti Remove Allocation
32. Klik icon `[×]`
33. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
34. Klik `[Leave]`

### TC-FA-LIC-526: Bentuk tunggal helper level 1

35. Jalankan fixture BE pemulih Pre-setup #12 dan penyetel Unallocated Pool tepat 1 (Total Allocated 4.999 dari Total Asset Capacity 5.000) hingga tersimpan
36. Muat ulang halaman License, lalu klik tab `Allocation Quota`
37. Klik node `All Groups` di Sidebar
38. Klik tombol ikon `[Edit]` di samping Allocated Quota baris `Kantor Pusat`
39. Verifikasi helper Field 3 memakai bentuk tunggal: `Available unallocated pool: 1 unit.`
40. Verifikasi helper kedua Field 3: `Leave empty to remove this group's allocation.`
41. Klik icon `[×]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): fixture BE pemulih dan penyetel, muat ulang halaman, dan klik tab menyiapkan state tiap blok; `[×]` menutup modal bersih.
- Urutan TC: TC-FA-LIC-117 di awal karena memakai state Pre-setup #12 tanpa fixture penyetel; TC-FA-LIC-116 dan TC-FA-LIC-526 memakai fixture penyetel yang berbeda (S-10).
- TC-FA-LIC-117 berakhir lewat Save sukses (respons ditunda); toast sukses tidak diasersi karena tidak ada di Expected TC. Nilai Divisi IT 120 dipulihkan fixture BE.
- TC-FA-LIC-147 menutup modal dirty lewat `[×]`, dialog `Unsaved Changes`, dan `[Leave]` (S-08).
- Temuan untuk QA:
  - TC-FA-LIC-116: precondition menyebut grup `Divisi Kecil` dengan parent ber-Remaining 1 tanpa menyebut parent; helper Expected `Available in Kantor Pusat: 1 unit.` menunjukkan parent Kantor Pusat, sehingga spec memakai Kantor Pusat sebagai parent.
  - TC-FA-LIC-526: Total Allocated 4.999 dari Total Asset Capacity 5.000 diatur lewat fixture BE yang mekanismenya tidak disebut TC; disediakan tim FE/BE tanpa endpoint karangan (S-13).
- Alasan di atas sekitar 35 langkah (41 langkah): semua blok satu topik (modal Edit Allocation) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya fixture, muat ulang, dan menutup modal.
