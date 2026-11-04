---
id: TC-FA-LIC-E2E-053-resilience-tulis-kegagalan-5xx-dan-timeout-pada-edit
title: "Resilience Tulis: Kegagalan 5xx dan Timeout pada Edit, Remove, dan Force Logout"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-149
  - TC-FA-LIC-150
  - TC-FA-LIC-165
  - TC-FA-LIC-176
  - TC-FA-LIC-177
coverage:
  web: automated
---

# Resilience Tulis: Kegagalan 5xx dan Timeout pada Edit, Remove, dan Force Logout

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
- Data: Pre-setup #12: Divisi Logistik beralokasi 500 dan Divisi IT beralokasi 100; Pre-setup #14: sesi Budi Santoso (Chrome on Windows) tidak aktif lebih dari 2 jam, Online Users 18/25.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup Pre-setup #12 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Last Updated baris alokasi, entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Pemulihan sesi aktif Pre-setup #14 (18 sesi, seat 25) dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: entri `Changelog: Concurrent User`, System Log aktor, dan Activity Log bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: `Spectra.intercept()` di atas backend nyata memaksa respons 500 dan timeout pada request Save Edit Allocation dan request Force Logout; intercept dilepas segera setelah asersi tiap blok (S-09). Asersi memuat state backend (nilai tersimpan setelah pengulangan), sehingga `Mode: FE+BE`, bukan `mock`.
- Kemampuan teknis: Intercept jaringan juga menghitung request GET daftar sesi (asersi daftar tidak di-refresh).
- Kemampuan teknis: jeda waktu nyata 5 detik pada langkah `Tunggu 5 detik` (TC-FA-LIC-149, 165, dan 176 mengasersi toast error tidak hilang otomatis; TC tidak menyebut durasi, 5 detik dipilih spec karena melampaui auto-hide toast sukses 4 detik pada TC-FA-LIC-171); jam tidak digeser dan jeda di bawah 30 detik memakai waktu nyata.

## Test Steps

### TC-FA-LIC-150: Edit timeout jaringan

1. Klik tab `Allocation Quota`
2. Klik node `Kantor Pusat` di Sidebar
3. Klik tombol ikon `[Edit]` pada baris `Divisi Logistik`
4. Pasang intercept jaringan: request Save di-timeout
5. Isi New Allocated Quota `600`
6. Klik `[Save]`
7. Verifikasi toast `Connection problem. Please try again.` tanpa tombol aksi
8. Verifikasi modal tetap terbuka dengan input `600` dipertahankan
9. Verifikasi `[Save]` enabled
10. Lepas intercept jaringan
11. Tutup toast `Connection problem. Please try again.`

### TC-FA-LIC-149: Edit gagal 5xx

12. Pasang intercept jaringan: request Save digagalkan 500
13. Klik `[Save]`
14. Verifikasi toast error `Error, failed to update group license quota.`
15. Tunggu 5 detik
16. Verifikasi toast error tidak hilang otomatis
17. Tutup toast `Error, failed to update group license quota.`
18. Verifikasi modal tetap terbuka dengan input `600` dipertahankan
19. Verifikasi `[Save]` kembali enabled
20. Lepas intercept jaringan
21. Klik `[Save]`
22. Verifikasi toast sukses `Success, group license quota updated.`

### TC-FA-LIC-165: Remove Allocation gagal 5xx

23. Klik tombol ikon `[Edit]` pada baris `Divisi IT`
24. Klik `[Clear Field]`
25. Pasang intercept jaringan: request Save digagalkan 500
26. Klik `[Save]`
27. Verifikasi toast error `Error, failed to remove group license allocation.`
28. Tunggu 5 detik
29. Verifikasi toast error tidak hilang otomatis
30. Tutup toast `Error, failed to remove group license allocation.`
31. Verifikasi modal tetap terbuka
32. Verifikasi `[Save]` enabled
33. Lepas intercept jaringan
34. Klik icon `[×]`
35. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
36. Klik `[Leave]`
37. Verifikasi Allocated Quota baris `Divisi IT` tetap `100`

### TC-FA-LIC-177: Force Logout timeout

38. Klik tab `Concurrent User`
39. Ketik Search `Budi Santoso`, tekan Enter
40. Klik `[Force Logout]` pada baris Budi Santoso
41. Pasang intercept jaringan: request Force Logout di-timeout dan pencatat request GET daftar sesi
42. Klik `[Confirm Logout]`
43. Verifikasi toast `Connection problem. Please try again.` tanpa tombol aksi
44. Verifikasi dialog tetap terbuka
45. Tutup toast `Connection problem. Please try again.`

### TC-FA-LIC-176: Force Logout gagal 5xx

46. Ganti intercept jaringan: request Force Logout digagalkan 500
47. Klik `[Confirm Logout]`
48. Verifikasi toast error `Error, failed to log out user.`
49. Tunggu 5 detik
50. Verifikasi toast error tidak hilang otomatis
51. Tutup toast `Error, failed to log out user.`
52. Verifikasi dialog `Force Logout User` tetap terbuka
53. Verifikasi `[Confirm Logout]` enabled kembali
54. Verifikasi daftar tidak di-refresh (tidak ada request GET daftar sesi baru dan baris Budi Santoso tetap ada)
55. Lepas intercept jaringan
56. Klik `[Confirm Logout]`
57. Verifikasi pengulangan berhasil: toast sukses `Success, user session has been terminated.`
58. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): `Tutup toast` membuang toast `Connection problem` dan toast error persisten (TC-FA-LIC-149, 165, dan 176) sebelum toast berikutnya diasersi (R-12); `Tunggu 5 detik` menunggu lewatnya durasi auto-hide toast; `Lepas intercept` dan `Ganti intercept` mengatur kegagalan tiap blok; `[Clear Field]` dan menutup modal dirty (`[×]`, dialog `Unsaved Changes`, `[Leave]`, S-08).
- Baris Budi Santoso di tabel Active Sessions (18 sesi, lebih dari satu halaman) dibuka lewat Search sebagai langkah penghubung (R-16, bagian 8b butir 13): langkah 39 mengetik Search sebelum intercept dipasang dan langkah 58 membersihkannya dengan `(←)` (S-09).
- Urutan TC: TC-FA-LIC-150 lalu TC-FA-LIC-149 memakai modal yang sama dan tetap terbuka dengan `600` (S-04); TC-FA-LIC-165 pada Divisi IT; TC-FA-LIC-177 lalu TC-FA-LIC-176 memakai dialog Force Logout yang sama (S-10).
- Hasil sukses TC-FA-LIC-149 (Divisi Logistik 600) dan TC-FA-LIC-176 (Budi Santoso diakhiri) dipulihkan fixture BE pemulih (hook `after`).
- Temuan untuk QA:
  - TC-FA-LIC-176: `daftar tidak di-refresh` tidak punya cara observasi di TC; spec mengasersinya lewat tidak adanya request GET daftar sesi baru dan baris Budi Santoso yang tetap ada.
  - TC-FA-LIC-150 dan TC-FA-LIC-177: TC tidak menyebut apakah toast `Connection problem` persisten; spec menutupnya sebelum blok berikutnya.
  - TC-FA-LIC-149 butir c dan TC-FA-LIC-176 butir c menulis pengulangan berhasil tanpa teks toast; spec memakai `Success, group license quota updated.` (teks toast sukses Edit Allocation pada TC-FA-LIC-118) dan `Success, user session has been terminated.` (teks toast sukses Force Logout pada TC-FA-LIC-171).
- Alasan di atas sekitar 35 langkah (58 langkah): semua blok satu kelas harness (resilience tulis, intercept 5xx dan timeout) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya memasang dan melepas intercept.
